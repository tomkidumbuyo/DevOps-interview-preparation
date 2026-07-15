# CSI, snapshots and Kubernetes backup

<!-- chapter-guide:start -->
> **Step 074 of 373 — 06.04.02**
>
> **Builds on:** [PersistentVolumes, PVCs and StorageClasses](../01-pv-pvc-storageclass/README.md)
>
> **Now:** Learn **CSI, snapshots and Kubernetes backup** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Security](../../05-security/README.md).
<!-- chapter-guide:end -->

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/docs/concepts/storage/volume-snapshots/>

## Easy mode: purpose and mental model

Provision/attach/mount/snapshot/restore data and reconstruct cluster/application state with tested consistency.

```mermaid
flowchart LR
  I[identity and desired state] --> C[CSI, snapshots and Kubernetes backup control plane]
  C --> D[CSI, snapshots and Kubernetes backup data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **CSI controller** | external components provision/delete/attach/snapshot/resize volumes. |
| 2 | **CSI node plugin** | stages/publishes/mounts volumes on each node. |
| 3 | **CSIDriver/CSINode** | advertise driver lifecycle and node topology/capability. |
| 4 | **VolumeAttachment** | records controller attach intent/status for attachable storage. |
| 5 | **VolumeSnapshotClass** | selects snapshot driver, deletion policy and parameters. |
| 6 | **VolumeSnapshot/content** | namespaced request and cluster snapshot handle mirror PVC/PV model. |
| 7 | **Crash consistency** | block snapshot alone may not capture application transaction consistency. |
| 8 | **Velero/resource backup** | captures API objects and integrates volume backup methods under plugin limits. |
| 9 | **Restore ordering** | CRDs/operators/secrets/classes/data/workloads and identities must be reconstructed coherently. |
| 10 | **Restore validation** | application queries/checksums and measured RPO/RTO prove recovery. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For CSI, snapshots and Kubernetes backup, draw a real request/resource path and label where these mechanisms act: CSI controller, CSI node plugin, CSIDriver/CSINode, VolumeAttachment, VolumeSnapshotClass, VolumeSnapshot/content, Crash consistency, Velero/resource backup, Restore ordering, Restore validation. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl get csidriver,csinode,volumeattachment
kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A
kubectl logs -n kube-system -l app=csi-controller --all-containers
velero backup get && velero restore get
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy CSI, snapshots and Kubernetes backup resource and draw identity/control/data/dependency paths.
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

Explain CSI, snapshots and Kubernetes backup in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: PersistentVolumes, PVCs and StorageClasses](../01-pv-pvc-storageclass/README.md) · [Questions](questions-and-answers.md) · [Next: Security →](../../05-security/README.md)

<!-- reading-navigation:end -->
