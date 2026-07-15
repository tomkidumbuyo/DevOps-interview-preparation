# Services, EndpointSlices and CoreDNS — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JN-01

- [ ] **Question:** What is ClusterIP, and why does it matter in Services, EndpointSlices and CoreDNS?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** virtual internal IP implemented by the cluster service data plane. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JN-02

- [ ] **Question:** What is NodePort, and why does it matter in Services, EndpointSlices and CoreDNS?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** reserves a port on nodes and routes to Service endpoints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JN-03

- [ ] **Question:** What is LoadBalancer, and why does it matter in Services, EndpointSlices and CoreDNS?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** asks a controller/cloud to expose a Service and report ingress status. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JN-04

- [ ] **Question:** What is ExternalName, and why does it matter in Services, EndpointSlices and CoreDNS?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** DNS CNAME indirection without proxying or health. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JN-05

- [ ] **Question:** What is Headless Service, and why does it matter in Services, EndpointSlices and CoreDNS?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** returns endpoint DNS records without ClusterIP load balancing. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JN-06

- [ ] **Question:** What is EndpointSlice, and why does it matter in Services, EndpointSlices and CoreDNS?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** scalable source of endpoint addresses, ports, readiness and topology hints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JN-07

- [ ] **Question:** What is Service selector, and why does it matter in Services, EndpointSlices and CoreDNS?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** label query chooses Pods; mismatch yields no endpoints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JN-08

- [ ] **Code:** **Question:** What does `kubectl logs -n kube-system -l k8s-app=kube-dns --since=30m` help you verify for Services, EndpointSlices and CoreDNS?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: number or named Pod port must match actual listener.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get svc,endpoints,endpointslice -A -o wide` help you verify for Services, EndpointSlices and CoreDNS?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: watches Services/EndpointSlices and answers cluster zones plus forwarded external DNS.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe svc NAME -n NS` help you verify for Services, EndpointSlices and CoreDNS?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: resolver expansion can create latency and surprising external/internal queries.

## Junior — procedural and command questions

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JP-01

- [ ] **Code:** **Question:** A basic ClusterIP check fails. What would you do first using the CLI?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get svc,endpoints,endpointslice -A -o wide` and capture exact status/reason/request ID. virtual internal IP implemented by the cluster service data plane. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JP-02

- [ ] **Question:** A basic NodePort check fails. What would you do first?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe svc NAME -n NS` and capture exact status/reason/request ID. reserves a port on nodes and routes to Service endpoints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JP-03

- [ ] **Question:** A basic LoadBalancer check fails. What would you do first?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl run dns-test --rm -it --image=nicolaka/netshoot -- dig SVC.NS.svc.cluster.local` and capture exact status/reason/request ID. asks a controller/cloud to expose a Service and report ingress status. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JP-04

- [ ] **Code:** **Question:** A basic ExternalName check fails. What would you do first using the CLI?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system -l k8s-app=kube-dns --since=30m` and capture exact status/reason/request ID. DNS CNAME indirection without proxying or health. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JP-05

- [ ] **Question:** A basic Headless Service check fails. What would you do first?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get svc,endpoints,endpointslice -A -o wide` and capture exact status/reason/request ID. returns endpoint DNS records without ClusterIP load balancing. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JP-06

- [ ] **Question:** A basic EndpointSlice check fails. What would you do first?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe svc NAME -n NS` and capture exact status/reason/request ID. scalable source of endpoint addresses, ports, readiness and topology hints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JP-07

- [ ] **Code:** **Question:** A basic Service selector check fails. What would you do first using the CLI?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl run dns-test --rm -it --image=nicolaka/netshoot -- dig SVC.NS.svc.cluster.local` and capture exact status/reason/request ID. label query chooses Pods; mismatch yields no endpoints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JP-08

- [ ] **Question:** A basic targetPort check fails. What would you do first?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system -l k8s-app=kube-dns --since=30m` and capture exact status/reason/request ID. number or named Pod port must match actual listener. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JP-09

- [ ] **Question:** A basic CoreDNS check fails. What would you do first?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get svc,endpoints,endpointslice -A -o wide` and capture exact status/reason/request ID. watches Services/EndpointSlices and answers cluster zones plus forwarded external DNS. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-JP-10

- [ ] **Code:** **Question:** A basic DNS search/ndots check fails. What would you do first using the CLI?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe svc NAME -n NS` and capture exact status/reason/request ID. resolver expansion can create latency and surprising external/internal queries. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MN-01

- [ ] **Question:** Compare ClusterIP with NodePort. When would each change your design?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ClusterIP: virtual internal IP implemented by the cluster service data plane. NodePort: reserves a port on nodes and routes to Service endpoints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MN-02

- [ ] **Question:** Compare NodePort with LoadBalancer. When would each change your design?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** NodePort: reserves a port on nodes and routes to Service endpoints. LoadBalancer: asks a controller/cloud to expose a Service and report ingress status. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MN-03

- [ ] **Question:** Compare LoadBalancer with ExternalName. When would each change your design?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** LoadBalancer: asks a controller/cloud to expose a Service and report ingress status. ExternalName: DNS CNAME indirection without proxying or health. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MN-04

- [ ] **Configuration review:** **Question:** Compare ExternalName with Headless Service. When would each change your design?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ExternalName: DNS CNAME indirection without proxying or health. Headless Service: returns endpoint DNS records without ClusterIP load balancing. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MN-05

- [ ] **Question:** Compare Headless Service with EndpointSlice. When would each change your design?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Headless Service: returns endpoint DNS records without ClusterIP load balancing. EndpointSlice: scalable source of endpoint addresses, ports, readiness and topology hints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MN-06

- [ ] **Question:** Compare EndpointSlice with Service selector. When would each change your design?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** EndpointSlice: scalable source of endpoint addresses, ports, readiness and topology hints. Service selector: label query chooses Pods; mismatch yields no endpoints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MN-07

- [ ] **Configuration review:** **Question:** Compare Service selector with targetPort. When would each change your design?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Service selector: label query chooses Pods; mismatch yields no endpoints. targetPort: number or named Pod port must match actual listener. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MN-08

- [ ] **Question:** Compare targetPort with CoreDNS. When would each change your design?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** targetPort: number or named Pod port must match actual listener. CoreDNS: watches Services/EndpointSlices and answers cluster zones plus forwarded external DNS. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MN-09

- [ ] **Question:** Compare CoreDNS with DNS search/ndots. When would each change your design?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CoreDNS: watches Services/EndpointSlices and answers cluster zones plus forwarded external DNS. DNS search/ndots: resolver expansion can create latency and surprising external/internal queries. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MN-10

- [ ] **Configuration review:** **Question:** Compare DNS search/ndots with ClusterIP. When would each change your design?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** DNS search/ndots: resolver expansion can create latency and surprising external/internal queries. ClusterIP: virtual internal IP implemented by the cluster service data plane. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around ClusterIP; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get svc,endpoints,endpointslice -A -o wide` plus recent events/changes, then correlate the service-specific SLI. virtual internal IP implemented by the cluster service data plane. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MP-02

- [ ] **Question:** Production is degraded around NodePort; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe svc NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. reserves a port on nodes and routes to Service endpoints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around LoadBalancer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl run dns-test --rm -it --image=nicolaka/netshoot -- dig SVC.NS.svc.cluster.local` plus recent events/changes, then correlate the service-specific SLI. asks a controller/cloud to expose a Service and report ingress status. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MP-04

- [ ] **Question:** Production is degraded around ExternalName; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system -l k8s-app=kube-dns --since=30m` plus recent events/changes, then correlate the service-specific SLI. DNS CNAME indirection without proxying or health. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Headless Service; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get svc,endpoints,endpointslice -A -o wide` plus recent events/changes, then correlate the service-specific SLI. returns endpoint DNS records without ClusterIP load balancing. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MP-06

- [ ] **Question:** Production is degraded around EndpointSlice; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe svc NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. scalable source of endpoint addresses, ports, readiness and topology hints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Service selector; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl run dns-test --rm -it --image=nicolaka/netshoot -- dig SVC.NS.svc.cluster.local` plus recent events/changes, then correlate the service-specific SLI. label query chooses Pods; mismatch yields no endpoints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MP-08

- [ ] **Question:** Production is degraded around targetPort; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system -l k8s-app=kube-dns --since=30m` plus recent events/changes, then correlate the service-specific SLI. number or named Pod port must match actual listener. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around CoreDNS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get svc,endpoints,endpointslice -A -o wide` plus recent events/changes, then correlate the service-specific SLI. watches Services/EndpointSlices and answers cluster zones plus forwarded external DNS. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-MP-10

- [ ] **Question:** Production is degraded around DNS search/ndots; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe svc NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. resolver expansion can create latency and surprising external/internal queries. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SN-01

- [ ] **Question:** Design a production Services, EndpointSlices and CoreDNS capability where ClusterIP, ExternalName and Service selector are first-class requirements.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: virtual internal IP implemented by the cluster service data plane. DNS CNAME indirection without proxying or health. label query chooses Pods; mismatch yields no endpoints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Services, EndpointSlices and CoreDNS capability where NodePort, Headless Service and targetPort are first-class requirements.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reserves a port on nodes and routes to Service endpoints. returns endpoint DNS records without ClusterIP load balancing. number or named Pod port must match actual listener. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SN-03

- [ ] **Question:** Design a production Services, EndpointSlices and CoreDNS capability where LoadBalancer, EndpointSlice and CoreDNS are first-class requirements.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: asks a controller/cloud to expose a Service and report ingress status. scalable source of endpoint addresses, ports, readiness and topology hints. watches Services/EndpointSlices and answers cluster zones plus forwarded external DNS. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Services, EndpointSlices and CoreDNS capability where ExternalName, Service selector and DNS search/ndots are first-class requirements.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: DNS CNAME indirection without proxying or health. label query chooses Pods; mismatch yields no endpoints. resolver expansion can create latency and surprising external/internal queries. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SN-05

- [ ] **Question:** Design a production Services, EndpointSlices and CoreDNS capability where Headless Service, targetPort and ClusterIP are first-class requirements.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: returns endpoint DNS records without ClusterIP load balancing. number or named Pod port must match actual listener. virtual internal IP implemented by the cluster service data plane. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Services, EndpointSlices and CoreDNS capability where EndpointSlice, CoreDNS and NodePort are first-class requirements.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scalable source of endpoint addresses, ports, readiness and topology hints. watches Services/EndpointSlices and answers cluster zones plus forwarded external DNS. reserves a port on nodes and routes to Service endpoints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SN-07

- [ ] **Question:** Design a production Services, EndpointSlices and CoreDNS capability where Service selector, DNS search/ndots and LoadBalancer are first-class requirements.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: label query chooses Pods; mismatch yields no endpoints. resolver expansion can create latency and surprising external/internal queries. asks a controller/cloud to expose a Service and report ingress status. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Services, EndpointSlices and CoreDNS capability where targetPort, ClusterIP and ExternalName are first-class requirements.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: number or named Pod port must match actual listener. virtual internal IP implemented by the cluster service data plane. DNS CNAME indirection without proxying or health. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SN-09

- [ ] **Question:** Design a production Services, EndpointSlices and CoreDNS capability where CoreDNS, NodePort and Headless Service are first-class requirements.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: watches Services/EndpointSlices and answers cluster zones plus forwarded external DNS. reserves a port on nodes and routes to Service endpoints. returns endpoint DNS records without ClusterIP load balancing. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Services, EndpointSlices and CoreDNS capability where DNS search/ndots, LoadBalancer and EndpointSlice are first-class requirements.
> **Covered in:** [Services, EndpointSlices and CoreDNS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: resolver expansion can create latency and surprising external/internal queries. asks a controller/cloud to expose a Service and report ingress status. scalable source of endpoint addresses, ports, readiness and topology hints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ClusterIP. How do you lead it end to end?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get svc,endpoints,endpointslice -A -o wide` as one read-only checkpoint, not the whole diagnosis. virtual internal IP implemented by the cluster service data plane. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NodePort. How do you lead it end to end?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe svc NAME -n NS` as one read-only checkpoint, not the whole diagnosis. reserves a port on nodes and routes to Service endpoints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving LoadBalancer. How do you lead it end to end?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl run dns-test --rm -it --image=nicolaka/netshoot -- dig SVC.NS.svc.cluster.local` as one read-only checkpoint, not the whole diagnosis. asks a controller/cloud to expose a Service and report ingress status. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ExternalName. How do you lead it end to end?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system -l k8s-app=kube-dns --since=30m` as one read-only checkpoint, not the whole diagnosis. DNS CNAME indirection without proxying or health. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Headless Service. How do you lead it end to end?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get svc,endpoints,endpointslice -A -o wide` as one read-only checkpoint, not the whole diagnosis. returns endpoint DNS records without ClusterIP load balancing. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving EndpointSlice. How do you lead it end to end?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe svc NAME -n NS` as one read-only checkpoint, not the whole diagnosis. scalable source of endpoint addresses, ports, readiness and topology hints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service selector. How do you lead it end to end?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl run dns-test --rm -it --image=nicolaka/netshoot -- dig SVC.NS.svc.cluster.local` as one read-only checkpoint, not the whole diagnosis. label query chooses Pods; mismatch yields no endpoints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving targetPort. How do you lead it end to end?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system -l k8s-app=kube-dns --since=30m` as one read-only checkpoint, not the whole diagnosis. number or named Pod port must match actual listener. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CoreDNS. How do you lead it end to end?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get svc,endpoints,endpointslice -A -o wide` as one read-only checkpoint, not the whole diagnosis. watches Services/EndpointSlices and answers cluster zones plus forwarded external DNS. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICES-ENDPOINTSLICES-AND-COREDNS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DNS search/ndots. How do you lead it end to end?
> **Covered in:** [Services, EndpointSlices and CoreDNS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe svc NAME -n NS` as one read-only checkpoint, not the whole diagnosis. resolver expansion can create latency and surprising external/internal queries. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Networking](../README.md) · [Study note](README.md) · [Next: CNI, kube-proxy and eBPF data planes →](../02-cni-kubeproxy-ebpf/README.md)

<!-- reading-navigation:end -->
