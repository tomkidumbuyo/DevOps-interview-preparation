# Kubernetes multi-tenancy

<!-- chapter-guide:start -->
> **Step 080 of 373 — 06.05.05**
>
> **Builds on:** [Kubernetes admission policies and webhooks](../04-admission-policies-webhooks/README.md)
>
> **Now:** Learn **Kubernetes multi-tenancy** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Scheduling Autoscaling](../../06-scheduling-autoscaling/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/docs/concepts/security/multi-tenancy/>

## Easy mode: purpose and mental model

Isolate tenant identity, data, network, compute, policy, telemetry and noisy-neighbor effects under an explicit threat model.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Kubernetes multi-tenancy control plane]
  C --> D[Kubernetes multi-tenancy data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Namespace tenancy** | soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. |
| 2 | **Cluster-per-tenant** | stronger failure/control isolation at fleet cost and operational scale. |
| 3 | **RBAC boundary** | tenant admins must not create cluster-wide or privilege-escalating resources. |
| 4 | **Network isolation** | default deny plus controlled ingress/egress/DNS prevents lateral paths. |
| 5 | **ResourceQuota** | aggregate namespace object/compute limits constrain consumption/admission. |
| 6 | **LimitRange** | default/min/max per-object requests/limits and can affect scheduling unexpectedly. |
| 7 | **Node isolation** | taints/dedicated pools/runtime classes protect stronger/noisy workloads. |
| 8 | **Secret/data isolation** | separate workload identity, storage, KMS and backup/restore paths. |
| 9 | **Telemetry isolation** | tenant identifiers/access/redaction/quotas prevent cross-tenant leak and cardinality abuse. |
| 10 | **Policy delegation** | platform owns guardrails; tenant owns namespaced workloads within transparent exceptions. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Kubernetes multi-tenancy, draw a real request/resource path and label where these mechanisms act: Namespace tenancy, Cluster-per-tenant, RBAC boundary, Network isolation, ResourceQuota, LimitRange, Node isolation, Secret/data isolation, Telemetry isolation, Policy delegation. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A
kubectl auth can-i --list --as=TENANT -n TENANT_NS
kubectl top pod -n TENANT_NS
kubectl get pods -n TENANT_NS -o wide
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Kubernetes multi-tenancy resource and draw identity/control/data/dependency paths.
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

Explain Kubernetes multi-tenancy in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Kubernetes admission policies and webhooks](../04-admission-policies-webhooks/README.md) · [Questions](questions-and-answers.md) · [Next: Scheduling Autoscaling →](../../06-scheduling-autoscaling/README.md)

<!-- reading-navigation:end -->
