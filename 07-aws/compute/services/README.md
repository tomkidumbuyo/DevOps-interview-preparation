# Compute service leaves

<!-- child-topic-toc:start -->
## Table of contents and deeper notes

This parent note explains how the child topics work together. Follow each child link for the deeper mechanism, real commands/configuration, hands-on practice, authoritative documentation, and its local interview bank.

- [AMIs, Image Builder and golden images](amis-image-builder/README.md) — [questions and answers](amis-image-builder/questions-and-answers.md)
- [Amazon EC2](ec2/README.md) — [questions and answers](ec2/questions-and-answers.md)
- [EC2 Auto Scaling](ec2-auto-scaling/README.md) — [questions and answers](ec2-auto-scaling/questions-and-answers.md)
<!-- child-topic-toc:end -->
- [Amazon EC2](ec2/README.md) — [Q&A](ec2/questions-and-answers.md)
- [AMIs, Image Builder and golden images](amis-image-builder/README.md) — [Q&A](amis-image-builder/questions-and-answers.md)
- [EC2 Auto Scaling](ec2-auto-scaling/README.md) — [Q&A](ec2-auto-scaling/questions-and-answers.md)

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html>

## Easy mode: purpose and mental model

Integrate the compute branch as one production capability rather than isolated products.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Compute control plane]
  C --> D[Compute data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Instance family** | general, compute, memory, storage and accelerator families target different bottlenecks. |
| 2 | **CPU architecture** | x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. |
| 3 | **AMI** | boot image metadata and snapshots define instance root and launch compatibility. |
| 4 | **Golden image** | centrally hardened/tested base reduces bootstrap drift and replacement time. |
| 5 | **Launch template** | versions instance image/type/network/role/storage/bootstrap inputs. |
| 6 | **Min/max/desired** | bound fleet capacity while policies adjust desired count. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Compute, draw a real request/resource path and label where these mechanisms act: Instance family, CPU architecture, AMI, Golden image, Launch template, Min/max/desired. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws ec2 describe-instances --instance-ids INSTANCE_ID
aws ec2 describe-images --owners self
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Compute resource and draw identity/control/data/dependency paths.
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

Explain Compute in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
