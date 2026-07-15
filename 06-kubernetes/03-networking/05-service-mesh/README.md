# Service mesh

<!-- chapter-guide:start -->
> **Step 071 of 373 — 06.03.05**
>
> **Builds on:** [Ingress and Gateway API](../04-ingress-gateway-api/README.md)
>
> **Now:** Learn **Service mesh** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Storage](../../04-storage/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://istio.io/latest/docs/concepts/what-is-istio/>

## Easy mode: purpose and mental model

Add workload identity, mTLS, traffic policy and telemetry without losing application/network ownership or overloading sidecars/control planes.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Service mesh control plane]
  C --> D[Service mesh data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Data-plane proxy** | sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. |
| 2 | **Control plane** | distributes service discovery, certificates and policy to proxies. |
| 3 | **Workload identity** | trust-domain/service-account identity authenticates peers rather than IP alone. |
| 4 | **mTLS** | encrypts/authenticates service traffic while certificate issuance/rotation becomes critical. |
| 5 | **Authorization policy** | L4/L7 service identity rules complement Kubernetes NetworkPolicy. |
| 6 | **Traffic policy** | retries/timeouts/circuit/outlier/load balancing can amplify or mask application behavior. |
| 7 | **Telemetry** | proxy metrics/traces improve path visibility at cardinality/resource cost. |
| 8 | **Injection/attachment** | workloads missing sidecar/ambient enrollment can bypass expected controls. |
| 9 | **Control-plane outage** | existing proxy config may continue while new workloads/certs/routes degrade. |
| 10 | **Upgrade** | proxy/control/API skew and canary revision migration prevent fleet-wide breakage. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Service mesh, draw a real request/resource path and label where these mechanisms act: Data-plane proxy, Control plane, Workload identity, mTLS, Authorization policy, Traffic policy, Telemetry, Injection/attachment, Control-plane outage, Upgrade. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'
istioctl proxy-status
istioctl analyze -A
linkerd check
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Service mesh resource and draw identity/control/data/dependency paths.
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

Explain Service mesh in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Ingress and Gateway API](../04-ingress-gateway-api/README.md) · [Questions](questions-and-answers.md) · [Next: Storage →](../../04-storage/README.md)

<!-- reading-navigation:end -->
