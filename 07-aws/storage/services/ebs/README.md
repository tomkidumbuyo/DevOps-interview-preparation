# Amazon EBS

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html>

## Easy mode: purpose and mental model

Provide AZ-scoped block storage with measured latency/IOPS/throughput, encrypted snapshots and safe expansion.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Amazon EBS control plane]
  C --> D[Amazon EBS data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **gp3** | general SSD with independently configurable size, IOPS and throughput within limits. |
| 2 | **io2** | high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. |
| 3 | **st1/sc1** | throughput/cold HDD choices unsuitable for boot/random latency-sensitive workloads. |
| 4 | **Instance EBS bandwidth** | instance attachment limits can bottleneck a provisioned volume. |
| 5 | **Queue depth/I/O size** | workload concurrency and block size determine realized IOPS/throughput/latency. |
| 6 | **Snapshot** | incremental service copy that is crash-consistent unless the application is quiesced/coordinated. |
| 7 | **Encryption/KMS** | volume/snapshot/copy access requires both EC2 and key permissions. |
| 8 | **Fast Snapshot Restore** | pre-initializes supported snapshots in selected AZs at additional cost. |
| 9 | **Expansion** | grow volume then partition/PV/LV/filesystem without shrinking and with rollback evidence. |
| 10 | **Multi-Attach** | supported volumes/instances still require a cluster-aware filesystem/application. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Amazon EBS, draw a real request/resource path and label where these mechanisms act: gp3, io2, st1/sc1, Instance EBS bandwidth, Queue depth/I/O size, Snapshot, Encryption/KMS, Fast Snapshot Restore, Expansion, Multi-Attach. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws ec2 describe-volumes --volume-ids VOLUME_ID
aws ec2 describe-volume-status --volume-ids VOLUME_ID
aws ec2 modify-volume --volume-id VOLUME_ID --size SIZE
lsblk -f && iostat -xz 1
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Amazon EBS resource and draw identity/control/data/dependency paths.
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

Explain Amazon EBS in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
