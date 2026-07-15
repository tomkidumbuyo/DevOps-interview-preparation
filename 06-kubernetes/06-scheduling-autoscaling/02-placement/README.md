# Affinity, taints and topology placement

<!-- chapter-guide:start -->
> **Step 083 of 373 — 06.06.02**
>
> **Builds on:** [Resource requests, limits and QoS](../01-requests-limits-qos/README.md)
>
> **Now:** Learn **Affinity, taints and topology placement** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [HPA, VPA and KEDA](../03-hpa-vpa-keda/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/>

## Easy mode: purpose and mental model

Express required hardware/data locality and preferred spread without creating impossible or fragile scheduling constraints.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Affinity, taints and topology placement control plane]
  C --> D[Affinity, taints and topology placement data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **nodeSelector** | exact label match for simple required placement. |
| 2 | **Node affinity** | expressive required/preferred label predicates evaluated at scheduling. |
| 3 | **Pod affinity** | co-locates Pods by labels/topology and can be expensive/fragile. |
| 4 | **Pod anti-affinity** | spreads/fences replicas but hard rules can block during failures. |
| 5 | **Taint** | repels Pods by NoSchedule/PreferNoSchedule/NoExecute effects. |
| 6 | **Toleration** | permits but does not require placement on tainted nodes. |
| 7 | **Topology spread** | controls skew across zones/nodes using label selector and unsatisfiable behavior. |
| 8 | **Volume topology** | PV zone/access constrains feasible nodes after/before binding. |
| 9 | **Well-known labels** | topology/arch/os/instance attributes should be trusted and lifecycle-managed. |
| 10 | **Constraint diagnosis** | scheduler events enumerate failed filters; removing safety constraints blindly is not repair. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Affinity, taints and topology placement, draw a real request/resource path and label where these mechanisms act: nodeSelector, Node affinity, Pod affinity, Pod anti-affinity, Taint, Toleration, Topology spread, Volume topology, Well-known labels, Constraint diagnosis. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl get nodes --show-labels
kubectl get events -A --field-selector=reason=FailedScheduling
kubectl describe pod POD -n NS
kubectl taint node NODE key=value:NoSchedule
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Affinity, taints and topology placement resource and draw identity/control/data/dependency paths.
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

Explain Affinity, taints and topology placement in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Resource requests, limits and QoS](../01-requests-limits-qos/README.md) · [Questions](questions-and-answers.md) · [Next: HPA, VPA and KEDA →](../03-hpa-vpa-keda/README.md)

<!-- reading-navigation:end -->
