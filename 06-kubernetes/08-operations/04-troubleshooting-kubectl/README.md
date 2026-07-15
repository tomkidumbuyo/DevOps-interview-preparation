# Kubernetes troubleshooting and kubectl

<!-- chapter-guide:start -->
> **Step 095 of 373 — 06.08.04**
>
> **Builds on:** [Kubernetes backup and disaster recovery](../03-backup-dr-etcd/README.md)
>
> **Now:** Learn **Kubernetes troubleshooting and kubectl** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Gpu Llmops](../../09-gpu-llmops/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/docs/tasks/debug/>

## Easy mode: purpose and mental model

Diagnose desired state through API, controllers, scheduler, node/runtime, network, storage and application using read-only evidence first.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Kubernetes troubleshooting and kubectl control plane]
  C --> D[Kubernetes troubleshooting and kubectl data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Object status/conditions** | observedGeneration, reason and message show controller interpretation. |
| 2 | **Events** | scheduling, pull, mount, probe and controller records point to the first failing transition. |
| 3 | **Previous logs** | retrieve terminated container output during CrashLoopBackOff. |
| 4 | **Ephemeral debug** | add diagnostic tooling without rebuilding the production image. |
| 5 | **Raw API/jsonpath/jq** | inspect exact fields and aggregated status rather than visually scanning YAML. |
| 6 | **Node debug** | enter host namespaces/filesystem carefully for kubelet/runtime/CNI evidence. |
| 7 | **EndpointSlice** | confirms whether readiness/selector produced routable Service targets. |
| 8 | **VolumeAttachment/CSI logs** | separate scheduler topology from controller attach and node mount. |
| 9 | **Managed fields** | identify which manager owns or overwrites a field. |
| 10 | **Source reconciliation** | repair Git/Helm/operator/IaC after any imperative mitigation. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Kubernetes troubleshooting and kubectl, draw a real request/resource path and label where these mechanisms act: Object status/conditions, Events, Previous logs, Ephemeral debug, Raw API/jsonpath/jq, Node debug, EndpointSlice, VolumeAttachment/CSI logs, Managed fields, Source reconciliation. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl describe pod POD -n NS
kubectl logs POD -n NS --all-containers --previous
kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER
kubectl get events -A --sort-by=.lastTimestamp
kubectl cluster-info dump --output-directory=./dump
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Kubernetes troubleshooting and kubectl resource and draw identity/control/data/dependency paths.
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

Explain Kubernetes troubleshooting and kubectl in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Kubernetes backup and disaster recovery](../03-backup-dr-etcd/README.md) · [Questions](questions-and-answers.md) · [Next: Gpu Llmops →](../../09-gpu-llmops/README.md)

<!-- reading-navigation:end -->
