# Amazon OpenSearch Service

<!-- chapter-guide:start -->
> **Step 143 of 373 — 07.07.05**
>
> **Builds on:** [Amazon ElastiCache](../04-elasticache/README.md)
>
> **Now:** Learn **Amazon OpenSearch Service** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Messaging Serverless](../../08-messaging-serverless/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html>

## Easy mode: purpose and mental model

Operate search/vector indexes with correct mappings, shards, access, snapshots, capacity and query observability.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Amazon OpenSearch Service control plane]
  C --> D[Amazon OpenSearch Service data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Index/mapping** | schema and analyzers determine searchable fields and cannot always be changed in place. |
| 2 | **Primary shard** | unit of index distribution whose count affects scale, recovery and overhead. |
| 3 | **Replica shard** | copies improve availability/read scale when placed on separate nodes/AZs. |
| 4 | **Cluster manager** | coordinates metadata and needs dedicated capacity at production scale. |
| 5 | **JVM heap** | memory pressure/GC/circuit breakers often fail before disk/CPU averages. |
| 6 | **Segment/merge** | indexing creates segments and background merging consumes I/O/CPU. |
| 7 | **Vector search** | dimension/index method/recall/latency/memory and filter behavior need benchmark. |
| 8 | **Snapshot** | service-managed/manual repositories support recovery but require restore testing. |
| 9 | **Fine-grained access** | IAM/domain policy, network and index/document permissions form layers. |
| 10 | **Shard sizing** | too many small shards waste heap; too large slows recovery and relocation. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Amazon OpenSearch Service, draw a real request/resource path and label where these mechanisms act: Index/mapping, Primary shard, Replica shard, Cluster manager, JVM heap, Segment/merge, Vector search, Snapshot, Fine-grained access, Shard sizing. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws opensearch describe-domain --domain-name DOMAIN
curl -s https://HOST/_cluster/health?pretty
curl -s https://HOST/_cat/shards?v
curl -s https://HOST/_nodes/stats/jvm,fs,indices?pretty
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Amazon OpenSearch Service resource and draw identity/control/data/dependency paths.
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

Explain Amazon OpenSearch Service in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon ElastiCache](../04-elasticache/README.md) · [Questions](questions-and-answers.md) · [Next: Messaging Serverless →](../../08-messaging-serverless/README.md)

<!-- reading-navigation:end -->
