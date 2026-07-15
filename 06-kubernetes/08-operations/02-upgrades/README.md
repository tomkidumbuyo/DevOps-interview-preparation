# Kubernetes upgrades and API deprecations

<!-- chapter-guide:start -->
> **Step 093 of 373 — 06.08.02**
>
> **Builds on:** [Kubernetes observability](../01-observability/README.md)
>
> **Now:** Learn **Kubernetes upgrades and API deprecations** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Kubernetes backup and disaster recovery](../03-backup-dr-etcd/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/releases/version-skew-policy/>

## Easy mode: purpose and mental model

Upgrade control plane, nodes, add-ons, CRDs and workloads within version-skew and compatibility evidence.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Kubernetes upgrades and API deprecations control plane]
  C --> D[Kubernetes upgrades and API deprecations data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Version skew** | supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. |
| 2 | **API deprecation** | served versions are removed on schedule and manifests/clients/controllers must migrate. |
| 3 | **Storage version** | existing objects may remain encoded in old version until storage migration/update. |
| 4 | **Control-plane first** | managed/self-managed procedures normally upgrade API before nodes within skew. |
| 5 | **Add-on compatibility** | CNI/CSI/CoreDNS/proxy/metrics/admission/operator versions need matrices. |
| 6 | **Canary node pool** | validates image/runtime/kernel/driver/workload before fleet drain. |
| 7 | **Drain/PDB** | maintenance success depends on budgets, state/storage and graceful termination. |
| 8 | **CRD conversion** | webhook and stored-version correctness must precede removing versions. |
| 9 | **Rollback** | control-plane downgrade is often unavailable, so backups/blue-green cluster migration matter. |
| 10 | **Qualification** | conformance plus real workload/SLO/security/DR validates more than node Ready. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Kubernetes upgrades and API deprecations, draw a real request/resource path and label where these mechanisms act: Version skew, API deprecation, Storage version, Control-plane first, Add-on compatibility, Canary node pool, Drain/PDB, CRD conversion, Rollback, Qualification. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl version
kubectl get --raw /version
kubectl get --raw /metrics | rg apiserver_requested_deprecated_apis
kubectl get crd -o json | jq '.items[] | {name:.metadata.name,storedVersions:.status.storedVersions}'
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Kubernetes upgrades and API deprecations resource and draw identity/control/data/dependency paths.
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

Explain Kubernetes upgrades and API deprecations in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Kubernetes observability](../01-observability/README.md) · [Questions](questions-and-answers.md) · [Next: Kubernetes backup and disaster recovery →](../03-backup-dr-etcd/README.md)

<!-- reading-navigation:end -->
