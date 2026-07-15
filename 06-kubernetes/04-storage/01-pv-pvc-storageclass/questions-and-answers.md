# PersistentVolumes, PVCs and StorageClasses — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JN-01

- [ ] **Question:** What is PersistentVolume, and why does it matter in PersistentVolumes, PVCs and StorageClasses?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** cluster object representing provisioned storage and reclaim policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JN-02

- [ ] **Question:** What is PersistentVolumeClaim, and why does it matter in PersistentVolumes, PVCs and StorageClasses?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** namespaced request for class, capacity, access mode and volume mode. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JN-03

- [ ] **Question:** What is StorageClass, and why does it matter in PersistentVolumes, PVCs and StorageClasses?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** provisioner and parameters define dynamic storage policy/default. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JN-04

- [ ] **Question:** What is Immediate binding, and why does it matter in PersistentVolumes, PVCs and StorageClasses?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** provisions/binds before scheduling and can choose wrong topology. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JN-05

- [ ] **Question:** What is WaitForFirstConsumer, and why does it matter in PersistentVolumes, PVCs and StorageClasses?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** delays provisioning until scheduler knows Pod node topology. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JN-06

- [ ] **Question:** What is Access mode, and why does it matter in PersistentVolumes, PVCs and StorageClasses?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** RWO/ROX/RWX/RWOP express supported attachment, not application concurrency safety. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JN-07

- [ ] **Question:** What is Volume mode, and why does it matter in PersistentVolumes, PVCs and StorageClasses?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Filesystem mounts a formatted FS; Block exposes raw device. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JN-08

- [ ] **Code:** **Question:** What does `kubectl get events -n NS --field-selector=involvedObject.kind=PersistentVolumeClaim` help you verify for PersistentVolumes, PVCs and StorageClasses?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: Delete/Retain controls storage after claim release and data lifecycle.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JN-09

- [ ] **Code:** **Question:** What does `kubectl get sc,pv,pvc -A` help you verify for PersistentVolumes, PVCs and StorageClasses?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: controller/node/filesystem phases must support and report status.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe pvc NAME -n NS` help you verify for PersistentVolumes, PVCs and StorageClasses?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: prevent deleting bound/in-use objects until controllers finish cleanup.

## Junior — procedural and command questions

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JP-01

- [ ] **Code:** **Question:** A basic PersistentVolume check fails. What would you do first using the CLI?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get sc,pv,pvc -A` and capture exact status/reason/request ID. cluster object representing provisioned storage and reclaim policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JP-02

- [ ] **Question:** A basic PersistentVolumeClaim check fails. What would you do first?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pvc NAME -n NS` and capture exact status/reason/request ID. namespaced request for class, capacity, access mode and volume mode. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JP-03

- [ ] **Question:** A basic StorageClass check fails. What would you do first?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pv PV -o yaml` and capture exact status/reason/request ID. provisioner and parameters define dynamic storage policy/default. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JP-04

- [ ] **Code:** **Question:** A basic Immediate binding check fails. What would you do first using the CLI?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -n NS --field-selector=involvedObject.kind=PersistentVolumeClaim` and capture exact status/reason/request ID. provisions/binds before scheduling and can choose wrong topology. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JP-05

- [ ] **Question:** A basic WaitForFirstConsumer check fails. What would you do first?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get sc,pv,pvc -A` and capture exact status/reason/request ID. delays provisioning until scheduler knows Pod node topology. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JP-06

- [ ] **Question:** A basic Access mode check fails. What would you do first?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pvc NAME -n NS` and capture exact status/reason/request ID. RWO/ROX/RWX/RWOP express supported attachment, not application concurrency safety. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JP-07

- [ ] **Code:** **Question:** A basic Volume mode check fails. What would you do first using the CLI?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pv PV -o yaml` and capture exact status/reason/request ID. Filesystem mounts a formatted FS; Block exposes raw device. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JP-08

- [ ] **Question:** A basic Reclaim policy check fails. What would you do first?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -n NS --field-selector=involvedObject.kind=PersistentVolumeClaim` and capture exact status/reason/request ID. Delete/Retain controls storage after claim release and data lifecycle. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JP-09

- [ ] **Question:** A basic Volume expansion check fails. What would you do first?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get sc,pv,pvc -A` and capture exact status/reason/request ID. controller/node/filesystem phases must support and report status. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-JP-10

- [ ] **Code:** **Question:** A basic Finalizers/protection check fails. What would you do first using the CLI?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pvc NAME -n NS` and capture exact status/reason/request ID. prevent deleting bound/in-use objects until controllers finish cleanup. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MN-01

- [ ] **Question:** Compare PersistentVolume with PersistentVolumeClaim. When would each change your design?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** PersistentVolume: cluster object representing provisioned storage and reclaim policy. PersistentVolumeClaim: namespaced request for class, capacity, access mode and volume mode. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MN-02

- [ ] **Question:** Compare PersistentVolumeClaim with StorageClass. When would each change your design?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** PersistentVolumeClaim: namespaced request for class, capacity, access mode and volume mode. StorageClass: provisioner and parameters define dynamic storage policy/default. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MN-03

- [ ] **Question:** Compare StorageClass with Immediate binding. When would each change your design?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** StorageClass: provisioner and parameters define dynamic storage policy/default. Immediate binding: provisions/binds before scheduling and can choose wrong topology. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MN-04

- [ ] **Configuration review:** **Question:** Compare Immediate binding with WaitForFirstConsumer. When would each change your design?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Immediate binding: provisions/binds before scheduling and can choose wrong topology. WaitForFirstConsumer: delays provisioning until scheduler knows Pod node topology. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MN-05

- [ ] **Question:** Compare WaitForFirstConsumer with Access mode. When would each change your design?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** WaitForFirstConsumer: delays provisioning until scheduler knows Pod node topology. Access mode: RWO/ROX/RWX/RWOP express supported attachment, not application concurrency safety. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MN-06

- [ ] **Question:** Compare Access mode with Volume mode. When would each change your design?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Access mode: RWO/ROX/RWX/RWOP express supported attachment, not application concurrency safety. Volume mode: Filesystem mounts a formatted FS; Block exposes raw device. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MN-07

- [ ] **Configuration review:** **Question:** Compare Volume mode with Reclaim policy. When would each change your design?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Volume mode: Filesystem mounts a formatted FS; Block exposes raw device. Reclaim policy: Delete/Retain controls storage after claim release and data lifecycle. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MN-08

- [ ] **Question:** Compare Reclaim policy with Volume expansion. When would each change your design?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Reclaim policy: Delete/Retain controls storage after claim release and data lifecycle. Volume expansion: controller/node/filesystem phases must support and report status. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MN-09

- [ ] **Question:** Compare Volume expansion with Finalizers/protection. When would each change your design?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Volume expansion: controller/node/filesystem phases must support and report status. Finalizers/protection: prevent deleting bound/in-use objects until controllers finish cleanup. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MN-10

- [ ] **Configuration review:** **Question:** Compare Finalizers/protection with PersistentVolume. When would each change your design?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Finalizers/protection: prevent deleting bound/in-use objects until controllers finish cleanup. PersistentVolume: cluster object representing provisioned storage and reclaim policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around PersistentVolume; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get sc,pv,pvc -A` plus recent events/changes, then correlate the service-specific SLI. cluster object representing provisioned storage and reclaim policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MP-02

- [ ] **Question:** Production is degraded around PersistentVolumeClaim; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pvc NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. namespaced request for class, capacity, access mode and volume mode. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around StorageClass; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pv PV -o yaml` plus recent events/changes, then correlate the service-specific SLI. provisioner and parameters define dynamic storage policy/default. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MP-04

- [ ] **Question:** Production is degraded around Immediate binding; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -n NS --field-selector=involvedObject.kind=PersistentVolumeClaim` plus recent events/changes, then correlate the service-specific SLI. provisions/binds before scheduling and can choose wrong topology. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around WaitForFirstConsumer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get sc,pv,pvc -A` plus recent events/changes, then correlate the service-specific SLI. delays provisioning until scheduler knows Pod node topology. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MP-06

- [ ] **Question:** Production is degraded around Access mode; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pvc NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. RWO/ROX/RWX/RWOP express supported attachment, not application concurrency safety. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Volume mode; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pv PV -o yaml` plus recent events/changes, then correlate the service-specific SLI. Filesystem mounts a formatted FS; Block exposes raw device. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MP-08

- [ ] **Question:** Production is degraded around Reclaim policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -n NS --field-selector=involvedObject.kind=PersistentVolumeClaim` plus recent events/changes, then correlate the service-specific SLI. Delete/Retain controls storage after claim release and data lifecycle. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Volume expansion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get sc,pv,pvc -A` plus recent events/changes, then correlate the service-specific SLI. controller/node/filesystem phases must support and report status. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-MP-10

- [ ] **Question:** Production is degraded around Finalizers/protection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pvc NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. prevent deleting bound/in-use objects until controllers finish cleanup. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SN-01

- [ ] **Question:** Design a production PersistentVolumes, PVCs and StorageClasses capability where PersistentVolume, Immediate binding and Volume mode are first-class requirements.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cluster object representing provisioned storage and reclaim policy. provisions/binds before scheduling and can choose wrong topology. Filesystem mounts a formatted FS; Block exposes raw device. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production PersistentVolumes, PVCs and StorageClasses capability where PersistentVolumeClaim, WaitForFirstConsumer and Reclaim policy are first-class requirements.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: namespaced request for class, capacity, access mode and volume mode. delays provisioning until scheduler knows Pod node topology. Delete/Retain controls storage after claim release and data lifecycle. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SN-03

- [ ] **Question:** Design a production PersistentVolumes, PVCs and StorageClasses capability where StorageClass, Access mode and Volume expansion are first-class requirements.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: provisioner and parameters define dynamic storage policy/default. RWO/ROX/RWX/RWOP express supported attachment, not application concurrency safety. controller/node/filesystem phases must support and report status. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production PersistentVolumes, PVCs and StorageClasses capability where Immediate binding, Volume mode and Finalizers/protection are first-class requirements.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: provisions/binds before scheduling and can choose wrong topology. Filesystem mounts a formatted FS; Block exposes raw device. prevent deleting bound/in-use objects until controllers finish cleanup. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SN-05

- [ ] **Question:** Design a production PersistentVolumes, PVCs and StorageClasses capability where WaitForFirstConsumer, Reclaim policy and PersistentVolume are first-class requirements.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: delays provisioning until scheduler knows Pod node topology. Delete/Retain controls storage after claim release and data lifecycle. cluster object representing provisioned storage and reclaim policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production PersistentVolumes, PVCs and StorageClasses capability where Access mode, Volume expansion and PersistentVolumeClaim are first-class requirements.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: RWO/ROX/RWX/RWOP express supported attachment, not application concurrency safety. controller/node/filesystem phases must support and report status. namespaced request for class, capacity, access mode and volume mode. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SN-07

- [ ] **Question:** Design a production PersistentVolumes, PVCs and StorageClasses capability where Volume mode, Finalizers/protection and StorageClass are first-class requirements.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Filesystem mounts a formatted FS; Block exposes raw device. prevent deleting bound/in-use objects until controllers finish cleanup. provisioner and parameters define dynamic storage policy/default. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production PersistentVolumes, PVCs and StorageClasses capability where Reclaim policy, PersistentVolume and Immediate binding are first-class requirements.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Delete/Retain controls storage after claim release and data lifecycle. cluster object representing provisioned storage and reclaim policy. provisions/binds before scheduling and can choose wrong topology. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SN-09

- [ ] **Question:** Design a production PersistentVolumes, PVCs and StorageClasses capability where Volume expansion, PersistentVolumeClaim and WaitForFirstConsumer are first-class requirements.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controller/node/filesystem phases must support and report status. namespaced request for class, capacity, access mode and volume mode. delays provisioning until scheduler knows Pod node topology. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production PersistentVolumes, PVCs and StorageClasses capability where Finalizers/protection, StorageClass and Access mode are first-class requirements.
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prevent deleting bound/in-use objects until controllers finish cleanup. provisioner and parameters define dynamic storage policy/default. RWO/ROX/RWX/RWOP express supported attachment, not application concurrency safety. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving PersistentVolume. How do you lead it end to end?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get sc,pv,pvc -A` as one read-only checkpoint, not the whole diagnosis. cluster object representing provisioned storage and reclaim policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving PersistentVolumeClaim. How do you lead it end to end?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pvc NAME -n NS` as one read-only checkpoint, not the whole diagnosis. namespaced request for class, capacity, access mode and volume mode. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving StorageClass. How do you lead it end to end?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pv PV -o yaml` as one read-only checkpoint, not the whole diagnosis. provisioner and parameters define dynamic storage policy/default. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Immediate binding. How do you lead it end to end?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -n NS --field-selector=involvedObject.kind=PersistentVolumeClaim` as one read-only checkpoint, not the whole diagnosis. provisions/binds before scheduling and can choose wrong topology. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving WaitForFirstConsumer. How do you lead it end to end?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get sc,pv,pvc -A` as one read-only checkpoint, not the whole diagnosis. delays provisioning until scheduler knows Pod node topology. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Access mode. How do you lead it end to end?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pvc NAME -n NS` as one read-only checkpoint, not the whole diagnosis. RWO/ROX/RWX/RWOP express supported attachment, not application concurrency safety. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Volume mode. How do you lead it end to end?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pv PV -o yaml` as one read-only checkpoint, not the whole diagnosis. Filesystem mounts a formatted FS; Block exposes raw device. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reclaim policy. How do you lead it end to end?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -n NS --field-selector=involvedObject.kind=PersistentVolumeClaim` as one read-only checkpoint, not the whole diagnosis. Delete/Retain controls storage after claim release and data lifecycle. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Volume expansion. How do you lead it end to end?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get sc,pv,pvc -A` as one read-only checkpoint, not the whole diagnosis. controller/node/filesystem phases must support and report status. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PERSISTENTVOLUMES-PVCS-AND-STORAGECLASSES-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Finalizers/protection. How do you lead it end to end?
> **Covered in:** [PersistentVolumes, PVCs and StorageClasses — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pvc NAME -n NS` as one read-only checkpoint, not the whole diagnosis. prevent deleting bound/in-use objects until controllers finish cleanup. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Storage](../README.md) · [Study note](README.md) · [Next: CSI, snapshots and Kubernetes backup →](../02-csi-snapshots-backup/README.md)

<!-- reading-navigation:end -->
