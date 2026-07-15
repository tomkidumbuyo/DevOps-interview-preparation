# Services, EndpointSlices and CoreDNS

<!-- chapter-guide:start -->
> **Step 067 of 373 — 06.03.01**
>
> **Builds on:** [Networking](../README.md)
>
> **Now:** Learn **Services, EndpointSlices and CoreDNS** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [CNI, kube-proxy and eBPF data planes](../02-cni-kubeproxy-ebpf/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/docs/concepts/services-networking/service/>

## Easy mode: purpose and mental model

Route stable virtual service names to ready Pod endpoints and diagnose DNS/data-plane state separately.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Services, EndpointSlices and CoreDNS control plane]
  C --> D[Services, EndpointSlices and CoreDNS data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **ClusterIP** | virtual internal IP implemented by the cluster service data plane. |
| 2 | **NodePort** | reserves a port on nodes and routes to Service endpoints. |
| 3 | **LoadBalancer** | asks a controller/cloud to expose a Service and report ingress status. |
| 4 | **ExternalName** | DNS CNAME indirection without proxying or health. |
| 5 | **Headless Service** | returns endpoint DNS records without ClusterIP load balancing. |
| 6 | **EndpointSlice** | scalable source of endpoint addresses, ports, readiness and topology hints. |
| 7 | **Service selector** | label query chooses Pods; mismatch yields no endpoints. |
| 8 | **targetPort** | number or named Pod port must match actual listener. |
| 9 | **CoreDNS** | watches Services/EndpointSlices and answers cluster zones plus forwarded external DNS. |
| 10 | **DNS search/ndots** | resolver expansion can create latency and surprising external/internal queries. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Services, EndpointSlices and CoreDNS, draw a real request/resource path and label where these mechanisms act: ClusterIP, NodePort, LoadBalancer, ExternalName, Headless Service, EndpointSlice, Service selector, targetPort, CoreDNS, DNS search/ndots. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

## Security model

Start with the caller/workload identity and evaluate every applicable identity, resource, organization, network-endpoint, encryption-key and admission policy. Minimize public paths, long-lived credentials, wildcard actions/resources and unreviewed cross-account/tenant trust. Encrypt in transit/at rest where applicable, but include key/certificate rotation and recovery. Protect audit evidence and prevent secrets/customer content from entering command history, logs, traces or metric labels.

## Availability and failure modes

List dependencies and failure domains before claiming high availability. Test quota/capacity, identity/control-plane, DNS/network/TLS, configuration drift, downstream saturation, zonal/Regional/node failure and recovery from protected state. Use bounded timeout, retry budget, jitter, idempotency, backpressure, load shedding and graceful drain according to protocol. A green resource status is not a user-facing recovery check.

## Performance, scaling and cost

Measure workload distribution and SLI before sizing. Track rate/work units, latency distribution, errors, saturation/queue and service-specific limits. Separate replica/task scaling from infrastructure/capacity scaling and include cold-start/provisioning delay. Cost includes idle/provisioned capacity, requests/work units, storage/retention, cross-AZ/Region/egress/NAT, observability, licenses/support and failure headroom. Optimize cost per successful SLO/quality-controlled task.

## Observability

Correlate a request/change across user, route/resource, dependency and underlying compute/storage/network. Use stable owner/environment/region/service dimensions; put high-cardinality request/object IDs in sampled logs/traces rather than metric labels. Alert on actionable SLO burn and leading exhaustion. Monitor the telemetry path and keep a read-only diagnostic role.

## Command lab

Run in a sandbox with the correct account/context/Region. Read and explain output before mutation.

```bash
kubectl get svc,endpoints,endpointslice -A -o wide
kubectl describe svc NAME -n NS
kubectl run dns-test --rm -it --image=nicolaka/netshoot -- dig SVC.NS.svc.cluster.local
kubectl logs -n kube-system -l k8s-app=kube-dns --since=30m
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Services, EndpointSlices and CoreDNS resource and draw identity/control/data/dependency paths.
2. **Intermediate:** reproduce a safe configuration change with IaC, preview/diff, apply to a sandbox, verify and roll back.
3. **Hard:** inject one policy/network/quota/capacity/dependency failure, diagnose from user symptom to root mechanism, mitigate without widening access, then add an alert/test/runbook.
4. **Senior:** design the service for two tenants, multi-zone/Region failure, RPO/RTO, regulated data, 10× demand and a 30% cost reduction; quantify trade-offs.

## Common interview traps

- Naming a feature without explaining request/resource lifecycle or failure semantics.
- Treating an allow, encryption checkbox, replica count or managed-service label as a complete security/reliability design.
- Mutating production before capturing identity, status, events, metrics, logs, audit and recent changes.
- Scaling the wrong layer or retrying overload/permanent errors.
- Omitting quotas, cold start, deletion/restore, observability cost or customer/tenant boundaries.

## Revision summary

Explain Services, EndpointSlices and CoreDNS in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Networking](../README.md) · [Questions](questions-and-answers.md) · [Next: CNI, kube-proxy and eBPF data planes →](../02-cni-kubeproxy-ebpf/README.md)

<!-- reading-navigation:end -->
