# Databases service leaves

<!-- child-topic-toc:start -->
## Table of contents and deeper notes

This parent note explains how the child topics work together. Follow each child link for the deeper mechanism, real commands/configuration, hands-on practice, authoritative documentation, and its local interview bank.

- [Amazon Aurora](aurora/README.md) — [questions and answers](aurora/questions-and-answers.md)
- [Amazon DynamoDB](dynamodb/README.md) — [questions and answers](dynamodb/questions-and-answers.md)
- [Amazon ElastiCache](elasticache/README.md) — [questions and answers](elasticache/questions-and-answers.md)
- [Amazon OpenSearch Service](opensearch/README.md) — [questions and answers](opensearch/questions-and-answers.md)
- [Amazon RDS](rds/README.md) — [questions and answers](rds/questions-and-answers.md)
<!-- child-topic-toc:end -->
- [Amazon RDS](rds/README.md) — [Q&A](rds/questions-and-answers.md)
- [Amazon Aurora](aurora/README.md) — [Q&A](aurora/questions-and-answers.md)
- [Amazon DynamoDB](dynamodb/README.md) — [Q&A](dynamodb/questions-and-answers.md)
- [Amazon ElastiCache](elasticache/README.md) — [Q&A](elasticache/questions-and-answers.md)
- [Amazon OpenSearch Service](opensearch/README.md) — [Q&A](opensearch/questions-and-answers.md)

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html>

## Easy mode: purpose and mental model

Integrate the databases branch as one production capability rather than isolated products.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Databases control plane]
  C --> D[Databases data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **DB instance** | managed engine compute/storage inside subnet/parameter/security configuration. |
| 2 | **Multi-AZ** | synchronous standby/failover for availability rather than read scaling. |
| 3 | **Cluster volume** | replicated distributed storage is shared by writer/readers. |
| 4 | **Writer endpoint** | follows current writer and should be used for write-capable connections. |
| 5 | **Partition key** | hashes items across physical partitions and must distribute request volume. |
| 6 | **Sort key** | orders items within a partition and enables range/prefix access patterns. |
| 7 | **Valkey/Redis replication group** | primary and replicas provide failover/read paths under node/AZ design. |
| 8 | **Cluster mode** | shards keys across node groups and requires compatible clients/key strategy. |
| 9 | **Index/mapping** | schema and analyzers determine searchable fields and cannot always be changed in place. |
| 10 | **Primary shard** | unit of index distribution whose count affects scale, recovery and overhead. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Databases, draw a real request/resource path and label where these mechanisms act: DB instance, Multi-AZ, Cluster volume, Writer endpoint, Partition key, Sort key, Valkey/Redis replication group, Cluster mode, Index/mapping, Primary shard. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws rds describe-db-instances --db-instance-identifier DB
aws rds describe-db-clusters --db-cluster-identifier CLUSTER
aws dynamodb describe-table --table-name TABLE
aws elasticache describe-replication-groups
aws opensearch describe-domain --domain-name DOMAIN
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Databases resource and draw identity/control/data/dependency paths.
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

Explain Databases in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
