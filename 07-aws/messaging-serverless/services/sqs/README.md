# Amazon SQS

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>

## Easy mode: purpose and mental model

Decouple producers and consumers with visible delivery semantics, idempotency, DLQs and backlog-based scaling.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Amazon SQS control plane]
  C --> D[Amazon SQS data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Standard queue** | at-least-once delivery and best-effort order at very high scale. |
| 2 | **FIFO queue** | ordered message groups and deduplication with throughput/parallelism constraints. |
| 3 | **Visibility timeout** | lease after receive must cover/extend processing or a message becomes visible again. |
| 4 | **Delete message** | consumer commit requires the latest receipt handle after successful effect. |
| 5 | **Long polling** | reduces empty receives/cost and latency compared with tight short polling. |
| 6 | **DLQ redrive** | isolates poison/repeated failures and needs controlled diagnosis/replay tooling. |
| 7 | **Retention** | bounds replay window and storage of unprocessed messages. |
| 8 | **Idempotency** | stable event/effect keys prevent duplicate business side effects. |
| 9 | **Oldest message age** | stronger backlog/SLO signal than queue count alone. |
| 10 | **In-flight quota** | excessive concurrency/long visibility can block further receive progress. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Amazon SQS, draw a real request/resource path and label where these mechanisms act: Standard queue, FIFO queue, Visibility timeout, Delete message, Long polling, DLQ redrive, Retention, Idempotency, Oldest message age, In-flight quota. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws sqs get-queue-attributes --queue-url URL --attribute-names All
aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10
aws sqs start-message-move-task --source-arn DLQ_ARN
aws cloudwatch get-metric-data --metric-data-queries file://sqs.json --start-time START --end-time END
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Amazon SQS resource and draw identity/control/data/dependency paths.
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

Explain Amazon SQS in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
