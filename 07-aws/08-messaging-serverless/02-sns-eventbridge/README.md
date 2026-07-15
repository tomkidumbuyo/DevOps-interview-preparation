# Amazon SNS and EventBridge

<!-- chapter-guide:start -->
> **Step 146 of 373 — 07.08.02**
>
> **Builds on:** [Amazon SQS](../01-sqs/README.md)
>
> **Now:** Learn **Amazon SNS and EventBridge** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [AWS Step Functions](../03-step-functions/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html>

## Easy mode: purpose and mental model

Fan out notifications and route domain events with filters, retries, archives and controlled cross-account policy.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Amazon SNS and EventBridge control plane]
  C --> D[Amazon SNS and EventBridge data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **SNS topic** | publisher fan-out to protocol subscriptions under topic policy. |
| 2 | **Subscription filter** | routes messages by attributes/body and can drop unexpected schemas. |
| 3 | **Delivery retry/DLQ** | endpoint-specific retry and dead-letter behavior must be observed. |
| 4 | **EventBridge bus** | account/custom/partner buses receive events under resource policy. |
| 5 | **Rule pattern** | matches structured event fields and routes to targets. |
| 6 | **Input transformation** | reshapes event for a target but creates schema coupling. |
| 7 | **Archive/replay** | retained bus events can be replayed with duplicate/side-effect controls. |
| 8 | **Schema registry** | documents/discovers schemas but compatibility governance remains owned. |
| 9 | **Cross-account routing** | organization/resource policies and target roles define trust. |
| 10 | **Scheduler** | invokes targets on time patterns with retry/DLQ and idempotency requirements. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Amazon SNS and EventBridge, draw a real request/resource path and label where these mechanisms act: SNS topic, Subscription filter, Delivery retry/DLQ, EventBridge bus, Rule pattern, Input transformation, Archive/replay, Schema registry, Cross-account routing, Scheduler. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws sns list-topics
aws sns list-subscriptions-by-topic --topic-arn ARN
aws events list-event-buses
aws events list-rules --event-bus-name BUS
aws events test-event-pattern --event-pattern file://pattern.json --event file://event.json
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Amazon SNS and EventBridge resource and draw identity/control/data/dependency paths.
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

Explain Amazon SNS and EventBridge in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon SQS](../01-sqs/README.md) · [Questions](questions-and-answers.md) · [Next: AWS Step Functions →](../03-step-functions/README.md)

<!-- reading-navigation:end -->
