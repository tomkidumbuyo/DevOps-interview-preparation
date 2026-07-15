# Kubernetes NetworkPolicy

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/docs/concepts/services-networking/network-policies/>

## Easy mode: purpose and mental model

Implement namespace/workload ingress and egress allow contracts with an enforcing CNI and verifiable DNS/dependency paths.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Kubernetes NetworkPolicy control plane]
  C --> D[Kubernetes NetworkPolicy data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Pod selection** | policy applies only to Pods matched in its namespace. |
| 2 | **Isolation direction** | selecting a Pod for ingress/egress isolates that direction to allowed union. |
| 3 | **Additive policy** | all matching policy allows are unioned; deny rules are not in base API. |
| 4 | **Namespace selector** | selects labeled namespaces and needs protected namespace label governance. |
| 5 | **Pod selector** | selects workload labels in the policy/selected namespace context. |
| 6 | **ipBlock** | CIDR/except matches IPs and can behave unexpectedly after NAT. |
| 7 | **Port/protocol** | L3/L4 policy cannot natively authorize DNS names or HTTP paths. |
| 8 | **Default deny** | empty allow list establishes isolation and requires DNS/control/dependency allowances. |
| 9 | **Both directions** | source egress and destination ingress can independently block one flow. |
| 10 | **CNI enforcement** | unsupported/no plugin means accepted objects may have no runtime effect. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Kubernetes NetworkPolicy, draw a real request/resource path and label where these mechanisms act: Pod selection, Isolation direction, Additive policy, Namespace selector, Pod selector, ipBlock, Port/protocol, Default deny, Both directions, CNI enforcement. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl get networkpolicy -A -o yaml
kubectl describe networkpolicy NAME -n NS
kubectl run netshoot --rm -it -n NS --image=nicolaka/netshoot -- bash
tcpdump -ni any host IP and port PORT
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Kubernetes NetworkPolicy resource and draw identity/control/data/dependency paths.
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

Explain Kubernetes NetworkPolicy in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
