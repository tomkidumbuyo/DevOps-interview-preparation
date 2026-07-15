# Kubernetes backup and disaster recovery — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JN-01

- [ ] **Question:** What is etcd snapshot, and why does it matter in Kubernetes backup and disaster recovery?

**Answer:** captures API storage for self-managed control planes with matching encryption/config needs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JN-02

- [ ] **Question:** What is Resource backup, and why does it matter in Kubernetes backup and disaster recovery?

**Answer:** exported API objects need CRDs, versions, ownership and secret protection. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JN-03

- [ ] **Question:** What is Volume backup, and why does it matter in Kubernetes backup and disaster recovery?

**Answer:** CSI snapshot/file backup needs application consistency and external snapshot retention. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JN-04

- [ ] **Question:** What is Velero, and why does it matter in Kubernetes backup and disaster recovery?

**Answer:** orchestrates Kubernetes resources and provider volume/plugin backups under coverage limits. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JN-05

- [ ] **Question:** What is Cluster rebuild, and why does it matter in Kubernetes backup and disaster recovery?

**Answer:** IaC/bootstrap/add-ons/controllers restore platform before workloads. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JN-06

- [ ] **Question:** What is Restore ordering, and why does it matter in Kubernetes backup and disaster recovery?

**Answer:** CRDs/operators, namespaces/policy, secrets, storage, data, services and apps. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JN-07

- [ ] **Question:** What is Identity/KMS, and why does it matter in Kubernetes backup and disaster recovery?

**Answer:** OIDC, CAs, encryption keys and cloud roles are recovery dependencies. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JN-08

- [ ] **Code:** **Question:** What does `velero restore create --from-backup NAME --wait` help you verify for Kubernetes backup and disaster recovery?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: latest consistent recoverable point includes async replication/backup lag.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JN-09

- [ ] **Code:** **Question:** What does `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` help you verify for Kubernetes backup and disaster recovery?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: provisioning, data transfer, model/cache warm and validation time determine recovery.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JN-10

- [ ] **Code:** **Question:** What does `ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table` help you verify for Kubernetes backup and disaster recovery?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: isolated environment plus user/data correctness and failback proves runbook.

## Junior — procedural and command questions

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JP-01

- [ ] **Code:** **Question:** A basic etcd snapshot check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` and capture exact status/reason/request ID. captures API storage for self-managed control planes with matching encryption/config needs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JP-02

- [ ] **Question:** A basic Resource backup check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table` and capture exact status/reason/request ID. exported API objects need CRDs, versions, ownership and secret protection. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JP-03

- [ ] **Question:** A basic Volume backup check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `velero backup create NAME --include-namespaces NS --wait` and capture exact status/reason/request ID. CSI snapshot/file backup needs application consistency and external snapshot retention. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JP-04

- [ ] **Code:** **Question:** A basic Velero check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `velero restore create --from-backup NAME --wait` and capture exact status/reason/request ID. orchestrates Kubernetes resources and provider volume/plugin backups under coverage limits. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JP-05

- [ ] **Question:** A basic Cluster rebuild check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` and capture exact status/reason/request ID. IaC/bootstrap/add-ons/controllers restore platform before workloads. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JP-06

- [ ] **Question:** A basic Restore ordering check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table` and capture exact status/reason/request ID. CRDs/operators, namespaces/policy, secrets, storage, data, services and apps. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JP-07

- [ ] **Code:** **Question:** A basic Identity/KMS check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `velero backup create NAME --include-namespaces NS --wait` and capture exact status/reason/request ID. OIDC, CAs, encryption keys and cloud roles are recovery dependencies. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JP-08

- [ ] **Question:** A basic RPO check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `velero restore create --from-backup NAME --wait` and capture exact status/reason/request ID. latest consistent recoverable point includes async replication/backup lag. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JP-09

- [ ] **Question:** A basic RTO check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` and capture exact status/reason/request ID. provisioning, data transfer, model/cache warm and validation time determine recovery. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-JP-10

- [ ] **Code:** **Question:** A basic Restore test check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table` and capture exact status/reason/request ID. isolated environment plus user/data correctness and failback proves runbook. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MN-01

- [ ] **Question:** Compare etcd snapshot with Resource backup. When would each change your design?

**Answer:** etcd snapshot: captures API storage for self-managed control planes with matching encryption/config needs. Resource backup: exported API objects need CRDs, versions, ownership and secret protection. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MN-02

- [ ] **Question:** Compare Resource backup with Volume backup. When would each change your design?

**Answer:** Resource backup: exported API objects need CRDs, versions, ownership and secret protection. Volume backup: CSI snapshot/file backup needs application consistency and external snapshot retention. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MN-03

- [ ] **Question:** Compare Volume backup with Velero. When would each change your design?

**Answer:** Volume backup: CSI snapshot/file backup needs application consistency and external snapshot retention. Velero: orchestrates Kubernetes resources and provider volume/plugin backups under coverage limits. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MN-04

- [ ] **Configuration review:** **Question:** Compare Velero with Cluster rebuild. When would each change your design?

**Answer:** Velero: orchestrates Kubernetes resources and provider volume/plugin backups under coverage limits. Cluster rebuild: IaC/bootstrap/add-ons/controllers restore platform before workloads. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MN-05

- [ ] **Question:** Compare Cluster rebuild with Restore ordering. When would each change your design?

**Answer:** Cluster rebuild: IaC/bootstrap/add-ons/controllers restore platform before workloads. Restore ordering: CRDs/operators, namespaces/policy, secrets, storage, data, services and apps. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MN-06

- [ ] **Question:** Compare Restore ordering with Identity/KMS. When would each change your design?

**Answer:** Restore ordering: CRDs/operators, namespaces/policy, secrets, storage, data, services and apps. Identity/KMS: OIDC, CAs, encryption keys and cloud roles are recovery dependencies. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MN-07

- [ ] **Configuration review:** **Question:** Compare Identity/KMS with RPO. When would each change your design?

**Answer:** Identity/KMS: OIDC, CAs, encryption keys and cloud roles are recovery dependencies. RPO: latest consistent recoverable point includes async replication/backup lag. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MN-08

- [ ] **Question:** Compare RPO with RTO. When would each change your design?

**Answer:** RPO: latest consistent recoverable point includes async replication/backup lag. RTO: provisioning, data transfer, model/cache warm and validation time determine recovery. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MN-09

- [ ] **Question:** Compare RTO with Restore test. When would each change your design?

**Answer:** RTO: provisioning, data transfer, model/cache warm and validation time determine recovery. Restore test: isolated environment plus user/data correctness and failback proves runbook. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MN-10

- [ ] **Configuration review:** **Question:** Compare Restore test with etcd snapshot. When would each change your design?

**Answer:** Restore test: isolated environment plus user/data correctness and failback proves runbook. etcd snapshot: captures API storage for self-managed control planes with matching encryption/config needs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around etcd snapshot; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` plus recent events/changes, then correlate the service-specific SLI. captures API storage for self-managed control planes with matching encryption/config needs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MP-02

- [ ] **Question:** Production is degraded around Resource backup; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table` plus recent events/changes, then correlate the service-specific SLI. exported API objects need CRDs, versions, ownership and secret protection. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Volume backup; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `velero backup create NAME --include-namespaces NS --wait` plus recent events/changes, then correlate the service-specific SLI. CSI snapshot/file backup needs application consistency and external snapshot retention. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MP-04

- [ ] **Question:** Production is degraded around Velero; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `velero restore create --from-backup NAME --wait` plus recent events/changes, then correlate the service-specific SLI. orchestrates Kubernetes resources and provider volume/plugin backups under coverage limits. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cluster rebuild; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` plus recent events/changes, then correlate the service-specific SLI. IaC/bootstrap/add-ons/controllers restore platform before workloads. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MP-06

- [ ] **Question:** Production is degraded around Restore ordering; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table` plus recent events/changes, then correlate the service-specific SLI. CRDs/operators, namespaces/policy, secrets, storage, data, services and apps. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Identity/KMS; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `velero backup create NAME --include-namespaces NS --wait` plus recent events/changes, then correlate the service-specific SLI. OIDC, CAs, encryption keys and cloud roles are recovery dependencies. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MP-08

- [ ] **Question:** Production is degraded around RPO; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `velero restore create --from-backup NAME --wait` plus recent events/changes, then correlate the service-specific SLI. latest consistent recoverable point includes async replication/backup lag. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around RTO; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` plus recent events/changes, then correlate the service-specific SLI. provisioning, data transfer, model/cache warm and validation time determine recovery. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-MP-10

- [ ] **Question:** Production is degraded around Restore test; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table` plus recent events/changes, then correlate the service-specific SLI. isolated environment plus user/data correctness and failback proves runbook. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SN-01

- [ ] **Question:** Design a production Kubernetes backup and disaster recovery capability where etcd snapshot, Velero and Identity/KMS are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: captures API storage for self-managed control planes with matching encryption/config needs. orchestrates Kubernetes resources and provider volume/plugin backups under coverage limits. OIDC, CAs, encryption keys and cloud roles are recovery dependencies. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes backup and disaster recovery capability where Resource backup, Cluster rebuild and RPO are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exported API objects need CRDs, versions, ownership and secret protection. IaC/bootstrap/add-ons/controllers restore platform before workloads. latest consistent recoverable point includes async replication/backup lag. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SN-03

- [ ] **Question:** Design a production Kubernetes backup and disaster recovery capability where Volume backup, Restore ordering and RTO are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: CSI snapshot/file backup needs application consistency and external snapshot retention. CRDs/operators, namespaces/policy, secrets, storage, data, services and apps. provisioning, data transfer, model/cache warm and validation time determine recovery. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes backup and disaster recovery capability where Velero, Identity/KMS and Restore test are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: orchestrates Kubernetes resources and provider volume/plugin backups under coverage limits. OIDC, CAs, encryption keys and cloud roles are recovery dependencies. isolated environment plus user/data correctness and failback proves runbook. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SN-05

- [ ] **Question:** Design a production Kubernetes backup and disaster recovery capability where Cluster rebuild, RPO and etcd snapshot are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: IaC/bootstrap/add-ons/controllers restore platform before workloads. latest consistent recoverable point includes async replication/backup lag. captures API storage for self-managed control planes with matching encryption/config needs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes backup and disaster recovery capability where Restore ordering, RTO and Resource backup are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: CRDs/operators, namespaces/policy, secrets, storage, data, services and apps. provisioning, data transfer, model/cache warm and validation time determine recovery. exported API objects need CRDs, versions, ownership and secret protection. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SN-07

- [ ] **Question:** Design a production Kubernetes backup and disaster recovery capability where Identity/KMS, Restore test and Volume backup are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: OIDC, CAs, encryption keys and cloud roles are recovery dependencies. isolated environment plus user/data correctness and failback proves runbook. CSI snapshot/file backup needs application consistency and external snapshot retention. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes backup and disaster recovery capability where RPO, etcd snapshot and Velero are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: latest consistent recoverable point includes async replication/backup lag. captures API storage for self-managed control planes with matching encryption/config needs. orchestrates Kubernetes resources and provider volume/plugin backups under coverage limits. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SN-09

- [ ] **Question:** Design a production Kubernetes backup and disaster recovery capability where RTO, Resource backup and Cluster rebuild are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: provisioning, data transfer, model/cache warm and validation time determine recovery. exported API objects need CRDs, versions, ownership and secret protection. IaC/bootstrap/add-ons/controllers restore platform before workloads. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes backup and disaster recovery capability where Restore test, Volume backup and Restore ordering are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: isolated environment plus user/data correctness and failback proves runbook. CSI snapshot/file backup needs application consistency and external snapshot retention. CRDs/operators, namespaces/policy, secrets, storage, data, services and apps. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving etcd snapshot. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` as one read-only checkpoint, not the whole diagnosis. captures API storage for self-managed control planes with matching encryption/config needs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource backup. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table` as one read-only checkpoint, not the whole diagnosis. exported API objects need CRDs, versions, ownership and secret protection. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Volume backup. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `velero backup create NAME --include-namespaces NS --wait` as one read-only checkpoint, not the whole diagnosis. CSI snapshot/file backup needs application consistency and external snapshot retention. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Velero. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `velero restore create --from-backup NAME --wait` as one read-only checkpoint, not the whole diagnosis. orchestrates Kubernetes resources and provider volume/plugin backups under coverage limits. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cluster rebuild. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` as one read-only checkpoint, not the whole diagnosis. IaC/bootstrap/add-ons/controllers restore platform before workloads. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Restore ordering. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table` as one read-only checkpoint, not the whole diagnosis. CRDs/operators, namespaces/policy, secrets, storage, data, services and apps. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Identity/KMS. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `velero backup create NAME --include-namespaces NS --wait` as one read-only checkpoint, not the whole diagnosis. OIDC, CAs, encryption keys and cloud roles are recovery dependencies. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RPO. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `velero restore create --from-backup NAME --wait` as one read-only checkpoint, not the whole diagnosis. latest consistent recoverable point includes async replication/backup lag. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RTO. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` as one read-only checkpoint, not the whole diagnosis. provisioning, data transfer, model/cache warm and validation time determine recovery. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-BACKUP-AND-DISASTER-RECOVERY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Restore test. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table` as one read-only checkpoint, not the whole diagnosis. isolated environment plus user/data correctness and failback proves runbook. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
