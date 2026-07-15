# VPC endpoints and AWS PrivateLink

<!-- chapter-guide:start -->
> **Step 113 of 373 — 07.02.04**
>
> **Builds on:** [NAT and egress architecture](../03-nat-egress/README.md)
>
> **Now:** Learn **VPC endpoints and AWS PrivateLink** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [VPC peering, Transit Gateway and Cloud WAN](../05-peering-tgw-cloudwan/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html>

## Easy mode: purpose and mental model

Reach AWS or producer services privately with explicit DNS, endpoint, resource and identity policy.

```mermaid
flowchart LR
  I[identity and desired state] --> C[VPC endpoints and AWS PrivateLink control plane]
  C --> D[VPC endpoints and AWS PrivateLink data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Gateway endpoint** | route-table target for supported services such as S3/DynamoDB without endpoint ENIs. |
| 2 | **Interface endpoint** | PrivateLink ENIs in subnets with security groups and per-hour/data cost. |
| 3 | **Private DNS** | maps standard service hostname to endpoint addresses inside associated VPCs. |
| 4 | **Endpoint policy** | constrains calls through the endpoint but does not grant principal/resource permission. |
| 5 | **Endpoint service** | NLB-backed producer service exposed privately to approved consumers. |
| 6 | **Acceptance/permissions** | service owners control which accounts/principals may create endpoint connections. |
| 7 | **Zonal design** | endpoint ENIs and DNS answers must align with AZ resilience and client paths. |
| 8 | **Resource policy conditions** | source VPC/endpoint conditions can constrain data access under known service semantics. |
| 9 | **Hybrid DNS/path** | on-prem clients need Resolver/routing to use private endpoints correctly. |
| 10 | **Cost comparison** | endpoint hours/data versus NAT processing/cross-AZ/exposure depends on traffic and topology. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For VPC endpoints and AWS PrivateLink, draw a real request/resource path and label where these mechanisms act: Gateway endpoint, Interface endpoint, Private DNS, Endpoint policy, Endpoint service, Acceptance/permissions, Zonal design, Resource policy conditions, Hybrid DNS/path, Cost comparison. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID
aws ec2 describe-vpc-endpoint-services
aws ec2 describe-vpc-endpoint-connections
dig SERVICE.REGION.amazonaws.com
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy VPC endpoints and AWS PrivateLink resource and draw identity/control/data/dependency paths.
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

Explain VPC endpoints and AWS PrivateLink in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: NAT and egress architecture](../03-nat-egress/README.md) · [Questions](questions-and-answers.md) · [Next: VPC peering, Transit Gateway and Cloud WAN →](../05-peering-tgw-cloudwan/README.md)

<!-- reading-navigation:end -->
