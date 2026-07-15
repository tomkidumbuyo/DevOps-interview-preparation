# Network Load Balancer

<!-- chapter-guide:start -->
> **Step 123 of 373 — 07.04.02**
>
> **Builds on:** [Application Load Balancer](../01-alb/README.md)
>
> **Now:** Learn **Network Load Balancer** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Gateway Load Balancer](../03-gwlb/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html>

## Easy mode: purpose and mental model

Handle TCP, UDP and TLS flows with static zonal addresses, source-IP semantics and PrivateLink integration.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Network Load Balancer control plane]
  C --> D[Network Load Balancer data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Layer 4 flow** | routing is based on connection/protocol rather than HTTP path/header semantics. |
| 2 | **Static zonal addresses** | one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. |
| 3 | **Source IP preservation** | depends on target type/protocol/settings and affects security/logging/return path. |
| 4 | **TLS listener** | terminates TLS with certificates/policy while a TCP listener can pass TLS through. |
| 5 | **UDP** | health/connection assumptions differ because transport is connectionless. |
| 6 | **IP targets** | route to VPC/on-prem IPs under documented reachability and registration constraints. |
| 7 | **ALB target** | combines NLB static/private/TCP endpoint features with downstream ALB L7 routing. |
| 8 | **PrivateLink** | endpoint services commonly use NLB as producer data plane. |
| 9 | **Long-lived connections** | client/LB/target timeouts, draining and resets govern rollout behavior. |
| 10 | **Zonal health/cross-zone** | capacity in each enabled zone and DNS fail-away influence resilience. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Network Load Balancer, draw a real request/resource path and label where these mechanisms act: Layer 4 flow, Static zonal addresses, Source IP preservation, TLS listener, UDP, IP targets, ALB target, PrivateLink, Long-lived connections, Zonal health/cross-zone. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws elbv2 describe-load-balancers --names NAME
aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN
aws elbv2 describe-target-health --target-group-arn TG_ARN
openssl s_client -connect HOST:443 -servername NAME
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Network Load Balancer resource and draw identity/control/data/dependency paths.
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

Explain Network Load Balancer in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Application Load Balancer](../01-alb/README.md) · [Questions](questions-and-answers.md) · [Next: Gateway Load Balancer →](../03-gwlb/README.md)

<!-- reading-navigation:end -->
