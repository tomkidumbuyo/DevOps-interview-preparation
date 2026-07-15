# GPU Operator, device plugins and DRA

<!-- chapter-guide:start -->
> **Step 097 of 373 — 06.09.01**
>
> **Builds on:** [Gpu Llmops](../README.md)
>
> **Now:** Learn **GPU Operator, device plugins and DRA** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [GPU sharing, scheduling and queueing](../02-gpu-sharing-scheduling/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/>

## Easy mode: purpose and mental model

Expose, allocate, monitor and lifecycle GPU devices through a qualified driver/runtime/Kubernetes integration.

```mermaid
flowchart LR
  I[identity and desired state] --> C[GPU Operator, device plugins and DRA control plane]
  C --> D[GPU Operator, device plugins and DRA data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Driver** | host kernel module/firmware is the foundation and must match hardware/kernel/runtime. |
| 2 | **Container toolkit** | injects device/library/runtime configuration into GPU containers. |
| 3 | **Device plugin** | advertises integer extended resources and allocates device nodes. |
| 4 | **GPU Feature Discovery** | labels node hardware/capabilities for scheduling policy. |
| 5 | **GPU Operator** | reconciles driver/toolkit/plugin/GFD/DCGM/MIG components under one version matrix. |
| 6 | **DRA ResourceSlice** | driver publishes device inventory/attributes/topology. |
| 7 | **DeviceClass** | admin policy selects device characteristics using CEL. |
| 8 | **ResourceClaim** | workload requests and records allocated/prepared device. |
| 9 | **Device health** | unhealthy device reduces future allocatable or reports claim/Pod status under mechanism. |
| 10 | **Canary upgrade** | drain one pool, update driver/operator/runtime, qualify CUDA/NCCL/model then expand. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For GPU Operator, device plugins and DRA, draw a real request/resource path and label where these mechanisms act: Driver, Container toolkit, Device plugin, GPU Feature Discovery, GPU Operator, DRA ResourceSlice, DeviceClass, ResourceClaim, Device health, Canary upgrade. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl get pods -n gpu-operator -o wide
kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'
kubectl get deviceclass,resourceslice,resourceclaim -A
kubectl exec -n ai POD -- nvidia-smi
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy GPU Operator, device plugins and DRA resource and draw identity/control/data/dependency paths.
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

Explain GPU Operator, device plugins and DRA in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Gpu Llmops](../README.md) · [Questions](questions-and-answers.md) · [Next: GPU sharing, scheduling and queueing →](../02-gpu-sharing-scheduling/README.md)

<!-- reading-navigation:end -->
