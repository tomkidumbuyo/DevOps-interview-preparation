# Amazon ECS

<!-- chapter-guide:start -->
> **Step 134 of 373 — 07.06.02**
>
> **Builds on:** [Amazon ECR](../01-ecr/README.md)
>
> **Now:** Learn **Amazon ECS** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Amazon EKS](../03-eks/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html>

## Easy mode: purpose and mental model

Run task/service workloads on EC2 or Fargate with correct identity, networking, deployment and capacity-provider behavior.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Amazon ECS control plane]
  C --> D[Amazon ECS data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Task definition** | versioned container, resource, network, log, secret, volume and role specification. |
| 2 | **Task** | running/scheduled instantiation of a task definition. |
| 3 | **Service** | maintains desired tasks and integrates deployment, load balancing and discovery. |
| 4 | **Task role** | application AWS permissions exposed to containers. |
| 5 | **Execution role** | agent permissions for image pull, logs and startup secret retrieval. |
| 6 | **awsvpc networking** | each task gets an ENI/IP/security groups and consumes subnet capacity. |
| 7 | **Fargate** | managed task compute removes node operations with feature, startup and pricing trade-offs. |
| 8 | **Capacity provider** | associates EC2 ASG/Fargate capacity and placement strategy with services. |
| 9 | **Deployment circuit breaker** | detects failed service stabilization and can roll back. |
| 10 | **Task draining** | load balancer, stop timeout and application signal handling protect in-flight work. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Amazon ECS, draw a real request/resource path and label where these mechanisms act: Task definition, Task, Service, Task role, Execution role, awsvpc networking, Fargate, Capacity provider, Deployment circuit breaker, Task draining. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws ecs describe-clusters --clusters CLUSTER
aws ecs describe-services --cluster CLUSTER --services SERVICE
aws ecs describe-tasks --cluster CLUSTER --tasks TASK
aws ecs execute-command --cluster CLUSTER --task TASK --container CONTAINER --interactive --command /bin/sh
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Amazon ECS resource and draw identity/control/data/dependency paths.
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

Explain Amazon ECS in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon ECR](../01-ecr/README.md) · [Questions](questions-and-answers.md) · [Next: Amazon EKS →](../03-eks/README.md)

<!-- reading-navigation:end -->
