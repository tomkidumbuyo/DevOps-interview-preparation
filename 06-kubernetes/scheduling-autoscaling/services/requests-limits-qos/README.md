# Resource requests, limits and QoS

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>

## Easy mode: purpose and mental model

Schedule and isolate CPU, memory, ephemeral storage and extended resources from measured workload needs.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Resource requests, limits and QoS control plane]
  C --> D[Resource requests, limits and QoS data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **CPU request** | scheduler reservation and HPA utilization denominator, expressed in cores/millicores. |
| 2 | **CPU limit** | cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. |
| 3 | **Memory request** | scheduling reservation/eviction signal rather than guaranteed preallocation. |
| 4 | **Memory limit** | cgroup hard boundary can OOM-kill a container. |
| 5 | **Ephemeral-storage** | writable layer/log/emptyDir request/limit interacts with node disk eviction. |
| 6 | **Guaranteed QoS** | equal CPU/memory request/limit on every container gives strongest eviction priority. |
| 7 | **Burstable QoS** | at least one request/limit but not Guaranteed; common production class. |
| 8 | **BestEffort QoS** | no requests/limits and first under resource pressure. |
| 9 | **LimitRange** | injects/enforces per-container defaults and bounds. |
| 10 | **ResourceQuota** | namespace aggregate limits can reject objects or cap priority/storage/GPU counts. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Resource requests, limits and QoS, draw a real request/resource path and label where these mechanisms act: CPU request, CPU limit, Memory request, Memory limit, Ephemeral-storage, Guaranteed QoS, Burstable QoS, BestEffort QoS, LimitRange, ResourceQuota. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl describe node NODE
kubectl get pod POD -o jsonpath='{.status.qosClass}'
kubectl get resourcequota,limitrange -A
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Resource requests, limits and QoS resource and draw identity/control/data/dependency paths.
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

Explain Resource requests, limits and QoS in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
