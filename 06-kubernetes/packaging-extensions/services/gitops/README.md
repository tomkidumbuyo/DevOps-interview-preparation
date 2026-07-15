# Argo CD, Flux and GitOps

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://argo-cd.readthedocs.io/en/stable/>

## Easy mode: purpose and mental model

Continuously reconcile signed reviewed desired state across clusters with explicit tenancy, promotion, secrets and emergency workflow.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Argo CD, Flux and GitOps control plane]
  C --> D[Argo CD, Flux and GitOps data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Desired source** | Git/OCI revision plus render inputs is the audit/reconciliation truth. |
| 2 | **Reconciliation** | controller compares live and desired then applies/prunes under policy. |
| 3 | **Health** | resource-specific status estimates rollout but needs user/SLO verification. |
| 4 | **Sync wave/hook** | orders dependencies/migrations with failure and idempotency concerns. |
| 5 | **ApplicationSet/Flux Kustomization** | generates fleet/environment instances from controlled templates. |
| 6 | **Project/tenant boundary** | limits source repositories, clusters/namespaces and resource kinds. |
| 7 | **Prune/self-heal** | deletes drifted/removed resources and can amplify a bad commit. |
| 8 | **Secret workflow** | encrypted/external secret references prevent plaintext Git while preserving rotation. |
| 9 | **Promotion** | pull request updates immutable artifact/version between environment sources. |
| 10 | **Emergency change** | pause/reconcile source quickly so controller does not revert mitigation. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Argo CD, Flux and GitOps, draw a real request/resource path and label where these mechanisms act: Desired source, Reconciliation, Health, Sync wave/hook, ApplicationSet/Flux Kustomization, Project/tenant boundary, Prune/self-heal, Secret workflow, Promotion, Emergency change. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
argocd app diff APP
argocd app sync APP --revision REV
argocd app wait APP --health --sync
flux get kustomizations -A
flux reconcile kustomization NAME --with-source
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Argo CD, Flux and GitOps resource and draw identity/control/data/dependency paths.
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

Explain Argo CD, Flux and GitOps in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
