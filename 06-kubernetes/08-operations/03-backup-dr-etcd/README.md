# Kubernetes backup and disaster recovery

<!-- chapter-guide:start -->
> **Step 094 of 373 — 06.08.03**
>
> **Builds on:** [Kubernetes upgrades and API deprecations](../02-upgrades/README.md)
>
> **Now:** Learn **Kubernetes backup and disaster recovery** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Kubernetes troubleshooting and kubectl](../04-troubleshooting-kubectl/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/>

## Easy mode: purpose and mental model

Reconstruct API desired state and application-consistent data, identity, network and platform dependencies within tested RPO/RTO.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Kubernetes backup and disaster recovery control plane]
  C --> D[Kubernetes backup and disaster recovery data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **etcd snapshot** | captures API storage for self-managed control planes with matching encryption/config needs. |
| 2 | **Resource backup** | exported API objects need CRDs, versions, ownership and secret protection. |
| 3 | **Volume backup** | CSI snapshot/file backup needs application consistency and external snapshot retention. |
| 4 | **Velero** | orchestrates Kubernetes resources and provider volume/plugin backups under coverage limits. |
| 5 | **Cluster rebuild** | IaC/bootstrap/add-ons/controllers restore platform before workloads. |
| 6 | **Restore ordering** | CRDs/operators, namespaces/policy, secrets, storage, data, services and apps. |
| 7 | **Identity/KMS** | OIDC, CAs, encryption keys and cloud roles are recovery dependencies. |
| 8 | **RPO** | latest consistent recoverable point includes async replication/backup lag. |
| 9 | **RTO** | provisioning, data transfer, model/cache warm and validation time determine recovery. |
| 10 | **Restore test** | isolated environment plus user/data correctness and failback proves runbook. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Kubernetes backup and disaster recovery, draw a real request/resource path and label where these mechanisms act: etcd snapshot, Resource backup, Volume backup, Velero, Cluster rebuild, Restore ordering, Identity/KMS, RPO, RTO, Restore test. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
ETCDCTL_API=3 etcdctl snapshot save snapshot.db
ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table
velero backup create NAME --include-namespaces NS --wait
velero restore create --from-backup NAME --wait
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Kubernetes backup and disaster recovery resource and draw identity/control/data/dependency paths.
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

Explain Kubernetes backup and disaster recovery in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Kubernetes upgrades and API deprecations](../02-upgrades/README.md) · [Questions](questions-and-answers.md) · [Next: Kubernetes troubleshooting and kubectl →](../04-troubleshooting-kubectl/README.md)

<!-- reading-navigation:end -->
