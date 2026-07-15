# EC2 Auto Scaling

<!-- chapter-guide:start -->
> **Step 120 of 373 — 07.03.03**
>
> **Builds on:** [AMIs, Image Builder and golden images](../02-amis-image-builder/README.md)
>
> **Now:** Learn **EC2 Auto Scaling** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Load Balancing](../../04-load-balancing/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html>

## Easy mode: purpose and mental model

Maintain an EC2 fleet at safe capacity and roll images/configuration without losing state or traffic.

```mermaid
flowchart LR
  I[identity and desired state] --> C[EC2 Auto Scaling control plane]
  C --> D[EC2 Auto Scaling data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Launch template** | versions instance image/type/network/role/storage/bootstrap inputs. |
| 2 | **Min/max/desired** | bound fleet capacity while policies adjust desired count. |
| 3 | **Target tracking** | changes desired capacity to keep an aggregate metric near a target. |
| 4 | **Step scaling** | maps alarm breach magnitude to capacity adjustments. |
| 5 | **Warm-up** | prevents new instances distorting metrics before they contribute capacity. |
| 6 | **Lifecycle hook** | pauses launch/termination for initialization, registration, drain or checkpoint. |
| 7 | **Instance refresh** | replaces instances to a selected template with minimum healthy and checkpoints. |
| 8 | **Mixed instances** | diversifies compatible types and On-Demand/Spot allocation strategies. |
| 9 | **Capacity rebalance** | launches replacement on Spot rebalance recommendation before interruption. |
| 10 | **Health replacement loop** | wrong health/grace/bootstrap can continually destroy otherwise diagnosable instances. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For EC2 Auto Scaling, draw a real request/resource path and label where these mechanisms act: Launch template, Min/max/desired, Target tracking, Step scaling, Warm-up, Lifecycle hook, Instance refresh, Mixed instances, Capacity rebalance, Health replacement loop. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG
aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG
aws autoscaling start-instance-refresh --auto-scaling-group-name ASG --preferences file://preferences.json
aws autoscaling complete-lifecycle-action --lifecycle-hook-name HOOK --auto-scaling-group-name ASG --lifecycle-action-result CONTINUE --instance-id ID
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy EC2 Auto Scaling resource and draw identity/control/data/dependency paths.
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

Explain EC2 Auto Scaling in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AMIs, Image Builder and golden images](../02-amis-image-builder/README.md) · [Questions](questions-and-answers.md) · [Next: Load Balancing →](../../04-load-balancing/README.md)

<!-- reading-navigation:end -->
