# Amazon Route 53

<!-- chapter-guide:start -->
> **Step 116 of 373 — 07.02.07**
>
> **Builds on:** [AWS hybrid networking](../06-hybrid-networking/README.md)
>
> **Now:** Learn **Amazon Route 53** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Compute](../../03-compute/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html>

## Easy mode: purpose and mental model

Operate authoritative/private DNS, routing policy, resolver integration and health-based failover under caching.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Amazon Route 53 control plane]
  C --> D[Amazon Route 53 data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Hosted zone** | authoritative public or VPC-associated private namespace. |
| 2 | **Alias record** | AWS-specific record that targets supported resources without a CNAME at the zone apex. |
| 3 | **Weighted routing** | probabilistically distributes DNS answers and is affected by resolver/client caching. |
| 4 | **Latency routing** | chooses Region from measured AWS network latency rather than application load. |
| 5 | **Failover routing** | health-check state selects primary/secondary answers but recovery still depends on data/service readiness. |
| 6 | **TTL** | balances cache/query load against change/failover responsiveness. |
| 7 | **Resolver endpoints** | inbound/outbound interfaces bridge VPC and external DNS with forwarding rules. |
| 8 | **Split-horizon DNS** | public/private views can intentionally answer differently and complicate diagnosis. |
| 9 | **DNSSEC** | authenticates signed DNS data; it does not encrypt queries. |
| 10 | **Health checks** | endpoint/calculated/CloudWatch checks need quorum, firewall and false-positive design. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Amazon Route 53, draw a real request/resource path and label where these mechanisms act: Hosted zone, Alias record, Weighted routing, Latency routing, Failover routing, TTL, Resolver endpoints, Split-horizon DNS, DNSSEC, Health checks. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws route53 list-hosted-zones
aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID
aws route53 get-health-check-status --health-check-id ID
aws route53resolver list-resolver-rules
dig +trace NAME
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Amazon Route 53 resource and draw identity/control/data/dependency paths.
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

Explain Amazon Route 53 in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AWS hybrid networking](../06-hybrid-networking/README.md) · [Questions](questions-and-answers.md) · [Next: Compute →](../../03-compute/README.md)

<!-- reading-navigation:end -->
