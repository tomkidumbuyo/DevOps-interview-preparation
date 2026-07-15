# CNI, kube-proxy and eBPF data planes

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/docs/concepts/cluster-administration/networking/>

## Easy mode: purpose and mental model

Implement Pod addressing/routing and Service translation under IP, conntrack and policy constraints.

```mermaid
flowchart LR
  I[identity and desired state] --> C[CNI, kube-proxy and eBPF data planes control plane]
  C --> D[CNI, kube-proxy and eBPF data planes data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Kubernetes network model** | Pods have cluster-routable IP identity and communicate without required NAT inside the model. |
| 2 | **CNI plugin** | configures Pod interface, address, route and cleanup when runtime creates sandbox. |
| 3 | **IPAM** | allocates/reclaims Pod addresses and can exhaust/fragment subnet pools. |
| 4 | **kube-proxy iptables** | programs probabilistic NAT rules for Services and endpoints. |
| 5 | **kube-proxy IPVS** | uses kernel virtual server tables with separate synchronization. |
| 6 | **eBPF data plane** | programs kernel hooks/maps for routing, load balancing, policy and observability. |
| 7 | **Conntrack** | tracks NAT/state and can exhaust or retain stale translations. |
| 8 | **MTU** | encapsulation/cloud path mismatch can drop large packets while probes pass. |
| 9 | **SNAT/source preservation** | external/local traffic policy and plugin behavior influence client IP. |
| 10 | **Node-to-Pod routing** | overlay, native routing or cloud ENIs change troubleshooting and scale limits. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For CNI, kube-proxy and eBPF data planes, draw a real request/resource path and label where these mechanisms act: Kubernetes network model, CNI plugin, IPAM, kube-proxy iptables, kube-proxy IPVS, eBPF data plane, Conntrack, MTU, SNAT/source preservation, Node-to-Pod routing. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl get ds -n kube-system
kubectl logs -n kube-system DS_POD --since=30m
ip route && ip link
conntrack -S
bpftool map list
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy CNI, kube-proxy and eBPF data planes resource and draw identity/control/data/dependency paths.
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

Explain CNI, kube-proxy and eBPF data planes in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
