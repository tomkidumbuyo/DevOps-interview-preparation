# AWS Load Balancer Controller

<!-- chapter-guide:start -->
> **Step 137 of 373 — 07.06.05**
>
> **Builds on:** [Karpenter and EKS Auto Mode](../04-karpenter-auto-mode/README.md)
>
> **Now:** Learn **AWS Load Balancer Controller** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Databases](../../07-databases/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/>

## Easy mode: purpose and mental model

Reconcile Kubernetes Ingress/Service/Gateway intent into safe ALB/NLB resources and target health.

```mermaid
flowchart LR
  I[identity and desired state] --> C[AWS Load Balancer Controller control plane]
  C --> D[AWS Load Balancer Controller data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Ingress reconciliation** | annotations/spec/class generate ALB listeners/rules/target groups. |
| 2 | **Service LoadBalancer** | controller provisions NLB behavior from Service annotations/spec. |
| 3 | **Target type ip** | registers Pod IPs directly and depends on VPC routability/readiness. |
| 4 | **Target type instance** | registers nodes/NodePorts and adds another data-plane hop. |
| 5 | **IngressGroup** | shares an ALB across Ingresses and expands who can change listener rules. |
| 6 | **Subnet discovery** | tags/explicit subnets determine AZ/scheme and can fail silently through events. |
| 7 | **IAM workload role** | controller requires broad-looking but bounded ELB/EC2/ACM/WAF/tag actions. |
| 8 | **Certificate/TLS** | ACM discovery/ARN/listener policy and host rules must align. |
| 9 | **Finalizers** | controller cleanup can block Kubernetes deletion when AWS/API/IAM fails. |
| 10 | **Controller events/logs** | reconcile errors plus AWS target health locate desired-vs-cloud drift. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For AWS Load Balancer Controller, draw a real request/resource path and label where these mechanisms act: Ingress reconciliation, Service LoadBalancer, Target type ip, Target type instance, IngressGroup, Subnet discovery, IAM workload role, Certificate/TLS, Finalizers, Controller events/logs. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl get ingress,service -A
kubectl describe ingress NAME -n NS
kubectl logs -n kube-system deploy/aws-load-balancer-controller --since=30m
aws elbv2 describe-target-health --target-group-arn TG_ARN
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy AWS Load Balancer Controller resource and draw identity/control/data/dependency paths.
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

Explain AWS Load Balancer Controller in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Karpenter and EKS Auto Mode](../04-karpenter-auto-mode/README.md) · [Questions](questions-and-answers.md) · [Next: Databases →](../../07-databases/README.md)

<!-- reading-navigation:end -->
