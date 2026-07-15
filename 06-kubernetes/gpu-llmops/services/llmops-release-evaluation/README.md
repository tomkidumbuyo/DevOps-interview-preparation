# LLMOps release and evaluation on Kubernetes

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kserve.github.io/website/docs/model-serving/predictive-inference/rollout-strategies/canary-examples>

## Easy mode: purpose and mental model

Bind prompts, models, RAG indexes, runtimes and evaluators into reproducible quality-gated progressive delivery.

```mermaid
flowchart LR
  I[identity and desired state] --> C[LLMOps release and evaluation on Kubernetes control plane]
  C --> D[LLMOps release and evaluation on Kubernetes data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Release manifest** | exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. |
| 2 | **Golden dataset** | versioned owned task examples and edge/adversarial cases. |
| 3 | **Offline evaluation** | compares quality/safety/latency/cost before production under reproducible inputs. |
| 4 | **Model-as-judge** | scalable evaluator with bias/non-determinism/calibration and version risk. |
| 5 | **Shadow evaluation** | production input copy provides realism under privacy/side-effect/cost controls. |
| 6 | **Canary** | small user/tenant traffic with automated infrastructure and quality rollback gates. |
| 7 | **Champion/challenger** | compares incumbent/candidate while retaining explicit promotion authority. |
| 8 | **Prompt/index drift** | prompt or retrieval changes are model-release changes and need lineage/eval. |
| 9 | **Rollback** | retains prior artifacts/config/index and handles in-flight/cache/schema compatibility. |
| 10 | **Audit** | approval links dataset/evaluator/results/exception/actor to deployed revision. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For LLMOps release and evaluation on Kubernetes, draw a real request/resource path and label where these mechanisms act: Release manifest, Golden dataset, Offline evaluation, Model-as-judge, Shadow evaluation, Canary, Champion/challenger, Prompt/index drift, Rollback, Audit. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl get deployment,inferenceservice -n inference -o yaml
kubectl rollout history deployment/NAME -n inference
argocd app history APP
python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy LLMOps release and evaluation on Kubernetes resource and draw identity/control/data/dependency paths.
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

Explain LLMOps release and evaluation on Kubernetes in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
