# CSI, snapshots and Kubernetes backup — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JN-01

- [ ] **Question:** What is CSI controller, and why does it matter in CSI, snapshots and Kubernetes backup?

**Answer:** external components provision/delete/attach/snapshot/resize volumes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JN-02

- [ ] **Question:** What is CSI node plugin, and why does it matter in CSI, snapshots and Kubernetes backup?

**Answer:** stages/publishes/mounts volumes on each node. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JN-03

- [ ] **Question:** What is CSIDriver/CSINode, and why does it matter in CSI, snapshots and Kubernetes backup?

**Answer:** advertise driver lifecycle and node topology/capability. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JN-04

- [ ] **Question:** What is VolumeAttachment, and why does it matter in CSI, snapshots and Kubernetes backup?

**Answer:** records controller attach intent/status for attachable storage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JN-05

- [ ] **Question:** What is VolumeSnapshotClass, and why does it matter in CSI, snapshots and Kubernetes backup?

**Answer:** selects snapshot driver, deletion policy and parameters. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JN-06

- [ ] **Question:** What is VolumeSnapshot/content, and why does it matter in CSI, snapshots and Kubernetes backup?

**Answer:** namespaced request and cluster snapshot handle mirror PVC/PV model. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JN-07

- [ ] **Question:** What is Crash consistency, and why does it matter in CSI, snapshots and Kubernetes backup?

**Answer:** block snapshot alone may not capture application transaction consistency. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JN-08

- [ ] **Code:** **Question:** What does `velero backup get && velero restore get` help you verify for CSI, snapshots and Kubernetes backup?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: captures API objects and integrates volume backup methods under plugin limits.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JN-09

- [ ] **Code:** **Question:** What does `kubectl get csidriver,csinode,volumeattachment` help you verify for CSI, snapshots and Kubernetes backup?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: CRDs/operators/secrets/classes/data/workloads and identities must be reconstructed coherently.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JN-10

- [ ] **Code:** **Question:** What does `kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A` help you verify for CSI, snapshots and Kubernetes backup?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: application queries/checksums and measured RPO/RTO prove recovery.

## Junior — procedural and command questions

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JP-01

- [ ] **Code:** **Question:** A basic CSI controller check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get csidriver,csinode,volumeattachment` and capture exact status/reason/request ID. external components provision/delete/attach/snapshot/resize volumes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JP-02

- [ ] **Question:** A basic CSI node plugin check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A` and capture exact status/reason/request ID. stages/publishes/mounts volumes on each node. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JP-03

- [ ] **Question:** A basic CSIDriver/CSINode check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system -l app=csi-controller --all-containers` and capture exact status/reason/request ID. advertise driver lifecycle and node topology/capability. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JP-04

- [ ] **Code:** **Question:** A basic VolumeAttachment check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `velero backup get && velero restore get` and capture exact status/reason/request ID. records controller attach intent/status for attachable storage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JP-05

- [ ] **Question:** A basic VolumeSnapshotClass check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get csidriver,csinode,volumeattachment` and capture exact status/reason/request ID. selects snapshot driver, deletion policy and parameters. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JP-06

- [ ] **Question:** A basic VolumeSnapshot/content check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A` and capture exact status/reason/request ID. namespaced request and cluster snapshot handle mirror PVC/PV model. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JP-07

- [ ] **Code:** **Question:** A basic Crash consistency check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system -l app=csi-controller --all-containers` and capture exact status/reason/request ID. block snapshot alone may not capture application transaction consistency. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JP-08

- [ ] **Question:** A basic Velero/resource backup check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `velero backup get && velero restore get` and capture exact status/reason/request ID. captures API objects and integrates volume backup methods under plugin limits. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JP-09

- [ ] **Question:** A basic Restore ordering check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get csidriver,csinode,volumeattachment` and capture exact status/reason/request ID. CRDs/operators/secrets/classes/data/workloads and identities must be reconstructed coherently. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-JP-10

- [ ] **Code:** **Question:** A basic Restore validation check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A` and capture exact status/reason/request ID. application queries/checksums and measured RPO/RTO prove recovery. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MN-01

- [ ] **Question:** Compare CSI controller with CSI node plugin. When would each change your design?

**Answer:** CSI controller: external components provision/delete/attach/snapshot/resize volumes. CSI node plugin: stages/publishes/mounts volumes on each node. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MN-02

- [ ] **Question:** Compare CSI node plugin with CSIDriver/CSINode. When would each change your design?

**Answer:** CSI node plugin: stages/publishes/mounts volumes on each node. CSIDriver/CSINode: advertise driver lifecycle and node topology/capability. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MN-03

- [ ] **Question:** Compare CSIDriver/CSINode with VolumeAttachment. When would each change your design?

**Answer:** CSIDriver/CSINode: advertise driver lifecycle and node topology/capability. VolumeAttachment: records controller attach intent/status for attachable storage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MN-04

- [ ] **Configuration review:** **Question:** Compare VolumeAttachment with VolumeSnapshotClass. When would each change your design?

**Answer:** VolumeAttachment: records controller attach intent/status for attachable storage. VolumeSnapshotClass: selects snapshot driver, deletion policy and parameters. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MN-05

- [ ] **Question:** Compare VolumeSnapshotClass with VolumeSnapshot/content. When would each change your design?

**Answer:** VolumeSnapshotClass: selects snapshot driver, deletion policy and parameters. VolumeSnapshot/content: namespaced request and cluster snapshot handle mirror PVC/PV model. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MN-06

- [ ] **Question:** Compare VolumeSnapshot/content with Crash consistency. When would each change your design?

**Answer:** VolumeSnapshot/content: namespaced request and cluster snapshot handle mirror PVC/PV model. Crash consistency: block snapshot alone may not capture application transaction consistency. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MN-07

- [ ] **Configuration review:** **Question:** Compare Crash consistency with Velero/resource backup. When would each change your design?

**Answer:** Crash consistency: block snapshot alone may not capture application transaction consistency. Velero/resource backup: captures API objects and integrates volume backup methods under plugin limits. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MN-08

- [ ] **Question:** Compare Velero/resource backup with Restore ordering. When would each change your design?

**Answer:** Velero/resource backup: captures API objects and integrates volume backup methods under plugin limits. Restore ordering: CRDs/operators/secrets/classes/data/workloads and identities must be reconstructed coherently. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MN-09

- [ ] **Question:** Compare Restore ordering with Restore validation. When would each change your design?

**Answer:** Restore ordering: CRDs/operators/secrets/classes/data/workloads and identities must be reconstructed coherently. Restore validation: application queries/checksums and measured RPO/RTO prove recovery. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MN-10

- [ ] **Configuration review:** **Question:** Compare Restore validation with CSI controller. When would each change your design?

**Answer:** Restore validation: application queries/checksums and measured RPO/RTO prove recovery. CSI controller: external components provision/delete/attach/snapshot/resize volumes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around CSI controller; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get csidriver,csinode,volumeattachment` plus recent events/changes, then correlate the service-specific SLI. external components provision/delete/attach/snapshot/resize volumes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MP-02

- [ ] **Question:** Production is degraded around CSI node plugin; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A` plus recent events/changes, then correlate the service-specific SLI. stages/publishes/mounts volumes on each node. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around CSIDriver/CSINode; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system -l app=csi-controller --all-containers` plus recent events/changes, then correlate the service-specific SLI. advertise driver lifecycle and node topology/capability. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MP-04

- [ ] **Question:** Production is degraded around VolumeAttachment; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `velero backup get && velero restore get` plus recent events/changes, then correlate the service-specific SLI. records controller attach intent/status for attachable storage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around VolumeSnapshotClass; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get csidriver,csinode,volumeattachment` plus recent events/changes, then correlate the service-specific SLI. selects snapshot driver, deletion policy and parameters. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MP-06

- [ ] **Question:** Production is degraded around VolumeSnapshot/content; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A` plus recent events/changes, then correlate the service-specific SLI. namespaced request and cluster snapshot handle mirror PVC/PV model. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Crash consistency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system -l app=csi-controller --all-containers` plus recent events/changes, then correlate the service-specific SLI. block snapshot alone may not capture application transaction consistency. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MP-08

- [ ] **Question:** Production is degraded around Velero/resource backup; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `velero backup get && velero restore get` plus recent events/changes, then correlate the service-specific SLI. captures API objects and integrates volume backup methods under plugin limits. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Restore ordering; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get csidriver,csinode,volumeattachment` plus recent events/changes, then correlate the service-specific SLI. CRDs/operators/secrets/classes/data/workloads and identities must be reconstructed coherently. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-MP-10

- [ ] **Question:** Production is degraded around Restore validation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A` plus recent events/changes, then correlate the service-specific SLI. application queries/checksums and measured RPO/RTO prove recovery. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SN-01

- [ ] **Question:** Design a production CSI, snapshots and Kubernetes backup capability where CSI controller, VolumeAttachment and Crash consistency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: external components provision/delete/attach/snapshot/resize volumes. records controller attach intent/status for attachable storage. block snapshot alone may not capture application transaction consistency. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production CSI, snapshots and Kubernetes backup capability where CSI node plugin, VolumeSnapshotClass and Velero/resource backup are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stages/publishes/mounts volumes on each node. selects snapshot driver, deletion policy and parameters. captures API objects and integrates volume backup methods under plugin limits. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SN-03

- [ ] **Question:** Design a production CSI, snapshots and Kubernetes backup capability where CSIDriver/CSINode, VolumeSnapshot/content and Restore ordering are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: advertise driver lifecycle and node topology/capability. namespaced request and cluster snapshot handle mirror PVC/PV model. CRDs/operators/secrets/classes/data/workloads and identities must be reconstructed coherently. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production CSI, snapshots and Kubernetes backup capability where VolumeAttachment, Crash consistency and Restore validation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: records controller attach intent/status for attachable storage. block snapshot alone may not capture application transaction consistency. application queries/checksums and measured RPO/RTO prove recovery. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SN-05

- [ ] **Question:** Design a production CSI, snapshots and Kubernetes backup capability where VolumeSnapshotClass, Velero/resource backup and CSI controller are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: selects snapshot driver, deletion policy and parameters. captures API objects and integrates volume backup methods under plugin limits. external components provision/delete/attach/snapshot/resize volumes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production CSI, snapshots and Kubernetes backup capability where VolumeSnapshot/content, Restore ordering and CSI node plugin are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: namespaced request and cluster snapshot handle mirror PVC/PV model. CRDs/operators/secrets/classes/data/workloads and identities must be reconstructed coherently. stages/publishes/mounts volumes on each node. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SN-07

- [ ] **Question:** Design a production CSI, snapshots and Kubernetes backup capability where Crash consistency, Restore validation and CSIDriver/CSINode are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: block snapshot alone may not capture application transaction consistency. application queries/checksums and measured RPO/RTO prove recovery. advertise driver lifecycle and node topology/capability. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production CSI, snapshots and Kubernetes backup capability where Velero/resource backup, CSI controller and VolumeAttachment are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: captures API objects and integrates volume backup methods under plugin limits. external components provision/delete/attach/snapshot/resize volumes. records controller attach intent/status for attachable storage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SN-09

- [ ] **Question:** Design a production CSI, snapshots and Kubernetes backup capability where Restore ordering, CSI node plugin and VolumeSnapshotClass are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: CRDs/operators/secrets/classes/data/workloads and identities must be reconstructed coherently. stages/publishes/mounts volumes on each node. selects snapshot driver, deletion policy and parameters. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production CSI, snapshots and Kubernetes backup capability where Restore validation, CSIDriver/CSINode and VolumeSnapshot/content are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: application queries/checksums and measured RPO/RTO prove recovery. advertise driver lifecycle and node topology/capability. namespaced request and cluster snapshot handle mirror PVC/PV model. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CSI controller. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get csidriver,csinode,volumeattachment` as one read-only checkpoint, not the whole diagnosis. external components provision/delete/attach/snapshot/resize volumes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CSI node plugin. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A` as one read-only checkpoint, not the whole diagnosis. stages/publishes/mounts volumes on each node. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CSIDriver/CSINode. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system -l app=csi-controller --all-containers` as one read-only checkpoint, not the whole diagnosis. advertise driver lifecycle and node topology/capability. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VolumeAttachment. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `velero backup get && velero restore get` as one read-only checkpoint, not the whole diagnosis. records controller attach intent/status for attachable storage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VolumeSnapshotClass. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get csidriver,csinode,volumeattachment` as one read-only checkpoint, not the whole diagnosis. selects snapshot driver, deletion policy and parameters. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VolumeSnapshot/content. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A` as one read-only checkpoint, not the whole diagnosis. namespaced request and cluster snapshot handle mirror PVC/PV model. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Crash consistency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system -l app=csi-controller --all-containers` as one read-only checkpoint, not the whole diagnosis. block snapshot alone may not capture application transaction consistency. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Velero/resource backup. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `velero backup get && velero restore get` as one read-only checkpoint, not the whole diagnosis. captures API objects and integrates volume backup methods under plugin limits. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Restore ordering. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get csidriver,csinode,volumeattachment` as one read-only checkpoint, not the whole diagnosis. CRDs/operators/secrets/classes/data/workloads and identities must be reconstructed coherently. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CSI-SNAPSHOTS-AND-KUBERNETES-BACKUP-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Restore validation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A` as one read-only checkpoint, not the whole diagnosis. application queries/checksums and measured RPO/RTO prove recovery. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
