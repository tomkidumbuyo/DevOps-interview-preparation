# Distributed training and checkpoint recovery

<!-- chapter-guide:start -->
> **Step 301 of 373 — 11.08.07**
>
> **Builds on:** [Training platform operations](../06-training-platform/README.md)
>
> **Now:** Learn **Distributed training and checkpoint recovery** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Hyperparameter tuning and experiment search](../08-hyperparameter-tuning/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.pytorch.org/tutorials/distributed.html>

## Easy mode: purpose and mental model

Operate DDP/FSDP/tensor/pipeline parallel training across failure-prone GPU networks and storage.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Distributed training and checkpoint recovery control plane]
  C --> D[Distributed training and checkpoint recovery data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Data parallel** | replicas process different batches and synchronize gradients; global batch and optimizer behavior change with world size. |
| 2 | **DDP** | one process per GPU and collective gradient reduction require rank/world/rendezvous correctness. |
| 3 | **FSDP/ZeRO** | shard parameters, gradients and optimizer state to trade communication/complexity for memory scale. |
| 4 | **Tensor parallel** | partitions matrix operations within a layer and benefits from high-bandwidth low-latency topology. |
| 5 | **Pipeline parallel** | partitions layers into stages with microbatches, bubbles and failure coordination. |
| 6 | **NCCL collectives** | ring/tree algorithms depend on rank, interface, RDMA/EFA, topology and version compatibility. |
| 7 | **Elasticity** | worker loss/restart changes membership only when algorithm/checkpoint semantics support it. |
| 8 | **Distributed checkpoint** | sharded state needs a committed manifest and compatible reshard/load procedure. |
| 9 | **Straggler** | one slow GPU/network/data worker holds synchronous progress and can hide behind average utilization. |
| 10 | **Reproducibility** | seeds alone do not eliminate nondeterministic kernels, asynchronous order or topology differences. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Distributed training and checkpoint recovery, draw a real request/resource path and label where these mechanisms act: Data parallel, DDP, FSDP/ZeRO, Tensor parallel, Pipeline parallel, NCCL collectives, Elasticity, Distributed checkpoint, Straggler, Reproducibility. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
torchrun --standalone --nproc-per-node=2 train.py --smoke-test
nvidia-smi topo -m
NCCL_DEBUG=INFO torchrun --nproc-per-node=2 diagnose.py
kubectl logs -n NS -l job-name=TRAINING_JOB --prefix
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Distributed training and checkpoint recovery resource and draw identity/control/data/dependency paths.
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

Explain Distributed training and checkpoint recovery in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.


## Hands-on proof: easy → hard

Use a disposable local environment, sandbox project/account or isolated Kubernetes namespace. Define all uppercase placeholders before running commands and confirm identity/context, data classification and cost boundary.

1. **Inventory:** run the read-only commands above, capture exact versions/IDs and explain which desired or observed state each proves.
2. **Build:** implement the smallest version-controlled example with an immutable input/artifact manifest and one automated test.
3. **Failure:** inject one bounded invalid input, dependency outage, incompatible revision, quota or stale-state condition; preserve the error and distinguish its layer without restarting blindly.
4. **Release:** generate evidence, compare a candidate with a baseline, make an explicit pass/fail decision and prove the deployed/run revision.
5. **Recover:** roll back or resume from a protected artifact/checkpoint, re-run the original quality and operational verification, and reconcile the source of truth.
6. **Cleanup:** delete only named lab resources and confirm no job, endpoint, volume, artifact, credential or billable accelerator remains. Retain only non-sensitive learning evidence allowed by policy.

Hard extension: put the lab in CI with short-lived identity, policy/evaluation gates, bounded concurrency/cost, an artifact digest, a failure-path test and a five-step runbook.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Training platform operations](../06-training-platform/README.md) · [Questions](questions-and-answers.md) · [Next: Hyperparameter tuning and experiment search →](../08-hyperparameter-tuning/README.md)

<!-- reading-navigation:end -->
