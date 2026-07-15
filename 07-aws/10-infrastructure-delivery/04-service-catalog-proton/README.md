# AWS Service Catalog and Proton

<!-- chapter-guide:start -->
> **Step 163 of 373 — 07.10.04**
>
> **Builds on:** [CodeBuild, CodePipeline and CodeDeploy](../03-code-services/README.md)
>
> **Now:** Learn **AWS Service Catalog and Proton** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Ai Platform](../../11-ai-platform/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html>

## Easy mode: purpose and mental model

Publish versioned governed infrastructure/service golden paths with ownership, constraints and safe upgrades.

```mermaid
flowchart LR
  I[identity and desired state] --> C[AWS Service Catalog and Proton control plane]
  C --> D[AWS Service Catalog and Proton data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Portfolio/product** | curated products and versions are shared to approved principals/accounts. |
| 2 | **Launch constraint** | service role separates user permission from provisioned-resource permission. |
| 3 | **Template constraint** | restricts product parameters to policy-safe combinations. |
| 4 | **Provisioned product** | launched stack/resource lifecycle needs owner/status/termination handling. |
| 5 | **Product version** | upgrades need compatibility, migration and deprecation communication. |
| 6 | **TagOptions** | standardize tags but do not replace enforcement or runtime ownership. |
| 7 | **Proton environment** | shared infrastructure context for service instances/templates. |
| 8 | **Service template** | standardizes service pipeline/infrastructure under platform ownership. |
| 9 | **Self-managed provisioning** | integrates external IaC workflows and must reconcile status/failures. |
| 10 | **Golden-path metrics** | adoption, time-to-deploy, success, exceptions and toil measure product value. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For AWS Service Catalog and Proton, draw a real request/resource path and label where these mechanisms act: Portfolio/product, Launch constraint, Template constraint, Provisioned product, Product version, TagOptions, Proton environment, Service template, Self-managed provisioning, Golden-path metrics. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws servicecatalog search-products-as-admin
aws servicecatalog scan-provisioned-products
aws proton list-environments
aws proton list-service-templates
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy AWS Service Catalog and Proton resource and draw identity/control/data/dependency paths.
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

Explain AWS Service Catalog and Proton in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: CodeBuild, CodePipeline and CodeDeploy](../03-code-services/README.md) · [Questions](questions-and-answers.md) · [Next: Ai Platform →](../../11-ai-platform/README.md)

<!-- reading-navigation:end -->
