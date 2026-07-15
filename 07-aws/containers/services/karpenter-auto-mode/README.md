# Karpenter and EKS Auto Mode

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html>

## Easy mode: purpose and mental model

Provision and consolidate nodes from pending-Pod constraints while bounding disruption, compatibility, capacity and spend.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Karpenter and EKS Auto Mode control plane]
  C --> D[Karpenter and EKS Auto Mode data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Pending-Pod demand** | autoscaler reads unschedulable constraints/requests rather than average node CPU alone. |
| 2 | **NodePool** | constrains labels, taints, requirements, disruption and aggregate resource limits. |
| 3 | **NodeClass** | AWS-specific subnets, security groups, AMI, role and storage configuration. |
| 4 | **Instance diversification** | compatible families/sizes/AZs improve capacity and Spot resilience. |
| 5 | **Consolidation** | removes/replaces underutilized nodes after respecting disruption policy. |
| 6 | **Disruption budget** | limits voluntary Karpenter actions but does not stop instance failure. |
| 7 | **Expiration/drift** | rotates nodes for image/config lifecycle under workload availability constraints. |
| 8 | **Scale from zero** | Pod constraints and NodePool metadata must still identify a compatible node. |
| 9 | **EKS Auto Mode** | managed node/storage/network automation builds on Karpenter concepts with supported constraints. |
| 10 | **Spend limits** | NodePool resource limits, quotas/budgets and admission prevent runaway provisioning. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Karpenter and EKS Auto Mode, draw a real request/resource path and label where these mechanisms act: Pending-Pod demand, NodePool, NodeClass, Instance diversification, Consolidation, Disruption budget, Expiration/drift, Scale from zero, EKS Auto Mode, Spend limits. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl get nodepool,ec2nodeclass,nodeclaim
kubectl describe nodeclaim NAME
kubectl logs -n kube-system deploy/karpenter --since=30m
aws ec2 describe-instance-type-offerings --location-type availability-zone
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Karpenter and EKS Auto Mode resource and draw identity/control/data/dependency paths.
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

Explain Karpenter and EKS Auto Mode in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
