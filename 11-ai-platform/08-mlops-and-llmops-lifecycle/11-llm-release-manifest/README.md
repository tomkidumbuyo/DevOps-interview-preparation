# LLM release manifests and compatibility

<!-- chapter-guide:start -->
> **Step 305 of 373 — 11.08.11**
>
> **Builds on:** [Model registry, artifacts and lineage](../10-model-registry-artifact-lineage/README.md)
>
> **Now:** Learn **LLM release manifests and compatibility** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Model validation and release gates](../12-model-validation-release-gates/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://slsa.dev/spec/v1.0/>

## Easy mode: purpose and mental model

Bind every LLM system component into an immutable, verifiable and rollback-ready release identity.

```mermaid
flowchart LR
  I[identity and desired state] --> C[LLM release manifests and compatibility control plane]
  C --> D[LLM release manifests and compatibility data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Weights digest** | base and fine-tuned model byte identity is stronger than a mutable repository revision name. |
| 2 | **Tokenizer** | files, normalization, vocabulary, special tokens and chat template are release-critical. |
| 3 | **Adapter** | base compatibility, target modules, rank/alpha and merge state prevent wrong attachment. |
| 4 | **Runtime** | image digest, server version, engine flags, kernels and quantization affect semantics/performance. |
| 5 | **Hardware** | accelerator/driver/CUDA topology qualification and memory profile bound supported deployment. |
| 6 | **Prompt/tool schema** | template/policy/function contracts and structured-output schema are versioned. |
| 7 | **RAG index** | embedding/chunker/corpus/snapshot/ACL policy and index digest affect every answer. |
| 8 | **Evaluator** | dataset/judge/prompt/rubric/calibration and pass thresholds explain approval. |
| 9 | **Governance** | owner, risk class, licenses, data residency, approval/exception and expiry travel with release. |
| 10 | **Rollback set** | prior compatible release and capacity, database/index schemas and cache invalidation steps are retained. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For LLM release manifests and compatibility, draw a real request/resource path and label where these mechanisms act: Weights digest, Tokenizer, Adapter, Runtime, Hardware, Prompt/tool schema, RAG index, Evaluator, Governance, Rollback set. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
python scripts/validate_release_manifest.py release.yaml
sha256sum model/* tokenizer/*
cosign verify-blob --signature release.sig release.yaml
kubectl get deployment MODEL -n inference -o jsonpath='{.spec.template.spec.containers[0].image}'
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy LLM release manifests and compatibility resource and draw identity/control/data/dependency paths.
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

Explain LLM release manifests and compatibility in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.


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

**Reading path:** [← Back: Model registry, artifacts and lineage](../10-model-registry-artifact-lineage/README.md) · [Questions](questions-and-answers.md) · [Next: Model validation and release gates →](../12-model-validation-release-gates/README.md)

<!-- reading-navigation:end -->
