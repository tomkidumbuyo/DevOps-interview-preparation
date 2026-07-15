# AWS GPUs, Inferentia and Trainium

<!-- chapter-guide:start -->
> **Step 168 of 373 — 07.11.04**
>
> **Builds on:** [AI/ML workloads on Amazon EKS](../03-eks-ai-inference/README.md)
>
> **Now:** Learn **AWS GPUs, Inferentia and Trainium** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Google Cloud Platform](../../../08-gcp/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html>

## Easy mode: purpose and mental model

Select scarce accelerator hardware from model compatibility, memory/compute/topology, capacity, reliability and unit economics.

```mermaid
flowchart LR
  I[identity and desired state] --> C[AWS GPUs, Inferentia and Trainium control plane]
  C --> D[AWS GPUs, Inferentia and Trainium data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **G-family GPU** | graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. |
| 2 | **P-family GPU** | high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. |
| 3 | **Inferentia** | AWS inference accelerator programmed through Neuron SDK and compiled model support. |
| 4 | **Trainium** | AWS training accelerator with Neuron distributed stack and operation compatibility. |
| 5 | **Neuron SDK** | compiler/runtime/framework integration is a qualification and portability dependency. |
| 6 | **Accelerator memory** | weights, KV/activations/workspace/fragmentation determine fit beyond parameter count. |
| 7 | **EFA** | OS-bypass networking improves supported collectives only with compatible topology/software. |
| 8 | **Capacity reservation/block** | commits specific capacity/time and differs from discount-only commitments. |
| 9 | **Spot** | fault-tolerant jobs need checkpoint/restart and diversified capacity. |
| 10 | **Benchmark** | target model/precision/batch/context/goodput/quality and total cost decide hardware. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For AWS GPUs, Inferentia and Trainium, draw a real request/resource path and label where these mechanisms act: G-family GPU, P-family GPU, Inferentia, Trainium, Neuron SDK, Accelerator memory, EFA, Capacity reservation/block, Spot, Benchmark. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'
aws ec2 describe-capacity-reservations
neuron-ls
nvidia-smi topo -m
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy AWS GPUs, Inferentia and Trainium resource and draw identity/control/data/dependency paths.
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

Explain AWS GPUs, Inferentia and Trainium in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AI/ML workloads on Amazon EKS](../03-eks-ai-inference/README.md) · [Questions](questions-and-answers.md) · [Next: Google Cloud Platform →](../../../08-gcp/README.md)

<!-- reading-navigation:end -->
