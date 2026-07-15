# Scheduling Autoscaling

<!-- chapter-guide:start -->
> **Step 081 of 373 — 06.06**
>
> **Builds on:** [Kubernetes multi-tenancy](../05-security/05-multitenancy/README.md)
>
> **Now:** Learn **Scheduling Autoscaling** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Resource requests, limits and QoS](01-requests-limits-qos/README.md).
<!-- chapter-guide:end -->

This branch README is both the study note and the map. Each service leaf keeps its notes in its own README and its answered interview bank in a separate file.

```mermaid
flowchart LR
  B[Scheduling Autoscaling]
  B --> S1[Resource requests, limits and QoS]
  B --> S2[Affinity, taints and topology placement]
  B --> S3[HPA, VPA and KEDA]
  B --> S4[Cluster Autoscaler, Karpenter and node lifecycle]
  B --> S5[PDB, priority, preemption and eviction]
```


## Branch learning contract

Learn the easy mental model first, run the read-only commands in a sandbox, render/apply the examples only in disposable environments, then break and repair one dependency at a time. Be able to connect these topics across the branch: CPU request, CPU limit, Memory request, nodeSelector, Node affinity, Pod affinity, HPA ratio, Resource utilization, Custom/external metric, Unschedulable Pod, Node group template, Karpenter NodePool, PDB, Eviction API, Unhealthy eviction policy.

## Branch interview bank

See [questions-and-answers.md](questions-and-answers.md) for 60 additional branch-level questions and answers. Service-specific banks contain another 60 per service.

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>

## Easy mode: purpose and mental model

Integrate the scheduling autoscaling branch as one production capability rather than isolated products.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Scheduling Autoscaling control plane]
  C --> D[Scheduling Autoscaling data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **CPU request** | scheduler reservation and HPA utilization denominator, expressed in cores/millicores. |
| 2 | **CPU limit** | cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. |
| 3 | **nodeSelector** | exact label match for simple required placement. |
| 4 | **Node affinity** | expressive required/preferred label predicates evaluated at scheduling. |
| 5 | **HPA ratio** | desired replicas derives current/target metric with tolerance and missing/not-ready handling. |
| 6 | **Resource utilization** | usage divided by requests means bad/missing requests break CPU/memory scaling. |
| 7 | **Unschedulable Pod** | requests/constraints are the node capacity specification. |
| 8 | **Node group template** | Cluster Autoscaler simulates predefined group capacity/labels/taints. |
| 9 | **PDB** | minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. |
| 10 | **Eviction API** | admission checks PDB and graceful deletion compared with direct delete. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Scheduling Autoscaling, draw a real request/resource path and label where these mechanisms act: CPU request, CPU limit, nodeSelector, Node affinity, HPA ratio, Resource utilization, Unschedulable Pod, Node group template, PDB, Eviction API. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl top pod -A --containers
kubectl get nodes --show-labels
kubectl get hpa -A
kubectl get pods -A --field-selector=status.phase=Pending
kubectl get pdb,priorityclass -A
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Scheduling Autoscaling resource and draw identity/control/data/dependency paths.
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

Explain Scheduling Autoscaling in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Kubernetes multi-tenancy](../05-security/05-multitenancy/README.md) · [Questions](questions-and-answers.md) · [Next: Resource requests, limits and QoS →](01-requests-limits-qos/README.md)

<!-- reading-navigation:end -->
