# Inference autoscaling and capacity

<!-- chapter-guide:start -->
> **Step 100 of 373 — 06.09.04**
>
> **Builds on:** [KServe, vLLM and Triton on Kubernetes](../03-model-serving/README.md)
>
> **Now:** Learn **Inference autoscaling and capacity** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [LLMOps release and evaluation on Kubernetes](../05-llmops-release-evaluation/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/eks/latest/userguide/ml-inference-autoscaling.html>

## Easy mode: purpose and mental model

Scale model replicas and accelerator nodes from token queue and SLO while accounting for long cold starts and scarce capacity.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Inference autoscaling and capacity control plane]
  C --> D[Inference autoscaling and capacity data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Queue depth/age** | leading overload signal when arrival work exceeds serving goodput. |
| 2 | **Predicted token work** | input/output length estimate better reflects heterogeneous request cost. |
| 3 | **TTFT/inter-token** | user latency separates queue/prefill from decode behavior. |
| 4 | **KV cache pressure** | memory/concurrency saturation can predict rejection before GPU utilization. |
| 5 | **HPA/KEDA** | scales replicas from custom/external metrics with stabilization and activation. |
| 6 | **Node autoscaler** | provisions GPU nodes only after replicas become Pending. |
| 7 | **Cold path** | cloud capacity, boot, driver/plugin, image, model download/load/warm dominate delay. |
| 8 | **Warm buffer** | preprovisioned nodes/replicas/cache trades cost for burst SLO. |
| 9 | **Scale down** | drain streams, protect cache/work, PDB/consolidation and minimum capacity. |
| 10 | **Capacity fallback** | diversified approved hardware/Region/provider requires compatibility/quality/residency tests. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Inference autoscaling and capacity, draw a real request/resource path and label where these mechanisms act: Queue depth/age, Predicted token work, TTFT/inter-token, KV cache pressure, HPA/KEDA, Node autoscaler, Cold path, Warm buffer, Scale down, Capacity fallback. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl describe hpa NAME -n NS
kubectl get scaledobject -A
kubectl get pods -A --field-selector=status.phase=Pending
kubectl logs -n kube-system deploy/karpenter --since=30m
curl -s http://MODEL/metrics
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Inference autoscaling and capacity resource and draw identity/control/data/dependency paths.
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

Explain Inference autoscaling and capacity in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: KServe, vLLM and Triton on Kubernetes](../03-model-serving/README.md) · [Questions](questions-and-answers.md) · [Next: LLMOps release and evaluation on Kubernetes →](../05-llmops-release-evaluation/README.md)

<!-- reading-navigation:end -->
