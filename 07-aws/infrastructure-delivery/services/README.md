# Infrastructure Delivery service leaves

<!-- child-topic-toc:start -->
## Table of contents and deeper notes

This parent note explains how the child topics work together. Follow each child link for the deeper mechanism, real commands/configuration, hands-on practice, authoritative documentation, and its local interview bank.

- [AWS CDK](cdk/README.md) — [questions and answers](cdk/questions-and-answers.md)
- [AWS CloudFormation](cloudformation/README.md) — [questions and answers](cloudformation/questions-and-answers.md)
- [CodeBuild, CodePipeline and CodeDeploy](code-services/README.md) — [questions and answers](code-services/questions-and-answers.md)
- [AWS Service Catalog and Proton](service-catalog-proton/README.md) — [questions and answers](service-catalog-proton/questions-and-answers.md)
<!-- child-topic-toc:end -->
- [AWS CloudFormation](cloudformation/README.md) — [Q&A](cloudformation/questions-and-answers.md)
- [AWS CDK](cdk/README.md) — [Q&A](cdk/questions-and-answers.md)
- [CodeBuild, CodePipeline and CodeDeploy](code-services/README.md) — [Q&A](code-services/questions-and-answers.md)
- [AWS Service Catalog and Proton](service-catalog-proton/README.md) — [Q&A](service-catalog-proton/questions-and-answers.md)

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html>

## Easy mode: purpose and mental model

Integrate the infrastructure delivery branch as one production capability rather than isolated products.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Infrastructure Delivery control plane]
  C --> D[Infrastructure Delivery data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Stack** | ownership/lifecycle boundary for a set of resources and outputs. |
| 2 | **Change set** | previews create/update/import actions but cannot predict every service-side effect. |
| 3 | **App/stack/construct tree** | code composes logical resources and ownership hierarchy. |
| 4 | **L1 construct** | direct generated CloudFormation resource mapping. |
| 5 | **CodeBuild project** | image/compute/VPC/service role/buildspec define a privileged ephemeral build. |
| 6 | **Buildspec** | phases/commands/artifacts/cache/reports are executable supply-chain code. |
| 7 | **Portfolio/product** | curated products and versions are shared to approved principals/accounts. |
| 8 | **Launch constraint** | service role separates user permission from provisioned-resource permission. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Infrastructure Delivery, draw a real request/resource path and label where these mechanisms act: Stack, Change set, App/stack/construct tree, L1 construct, CodeBuild project, Buildspec, Portfolio/product, Launch constraint. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE
cdk synth
aws codebuild batch-get-builds --ids BUILD_ID
aws servicecatalog search-products-as-admin
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Infrastructure Delivery resource and draw identity/control/data/dependency paths.
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

Explain Infrastructure Delivery in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
