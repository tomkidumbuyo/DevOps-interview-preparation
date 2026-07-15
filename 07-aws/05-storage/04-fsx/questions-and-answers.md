# Amazon FSx — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-FSX-JN-01

- [ ] **Question:** What is FSx for Lustre, and why does it matter in Amazon FSx?
> **Covered in:** [Amazon FSx — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-FSX-JN-02

- [ ] **Question:** What is Data repository association, and why does it matter in Amazon FSx?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** imports/exports metadata/data between Lustre and S3 under explicit lifecycle. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-FSX-JN-03

- [ ] **Question:** What is FSx for ONTAP, and why does it matter in Amazon FSx?
> **Covered in:** [Amazon FSx — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** NFS/SMB/iSCSI plus snapshots/clones/tiering for enterprise data workflows. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-FSX-JN-04

- [ ] **Question:** What is FSx for Windows, and why does it matter in Amazon FSx?
> **Covered in:** [Amazon FSx — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** SMB/Active Directory integration for Windows applications. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-FSX-JN-05

- [ ] **Question:** What is FSx for OpenZFS, and why does it matter in Amazon FSx?
> **Covered in:** [Amazon FSx — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** NFS and ZFS snapshot/clone/compression semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-FSX-JN-06

- [ ] **Question:** What is Deployment type, and why does it matter in Amazon FSx?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** scratch/persistent or single/multi-AZ options vary by filesystem and durability need. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-FSX-JN-07

- [ ] **Question:** What is Throughput/capacity, and why does it matter in Amazon FSx?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** provisioned storage, throughput, SSD/metadata and cache must match I/O profile. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-FSX-JN-08

- [ ] **Code:** **Question:** What does `lfs df -h && lfs osts` help you verify for Amazon FSx?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: subnets/routes/SG and directory identity are part of mount path.

### AMAZON-FSX-JN-09

- [ ] **Code:** **Question:** What does `aws fsx describe-file-systems` help you verify for Amazon FSx?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: feature and recovery behavior differ by filesystem; test application restore.

### AMAZON-FSX-JN-10

- [ ] **Code:** **Question:** What does `aws fsx describe-backups` help you verify for Amazon FSx?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: benchmark metadata, aggregate read, first load and node count rather than headline throughput.

## Junior — procedural and command questions

### AMAZON-FSX-JP-01

- [ ] **Code:** **Question:** A basic FSx for Lustre check fails. What would you do first using the CLI?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws fsx describe-file-systems` and capture exact status/reason/request ID. parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-FSX-JP-02

- [ ] **Question:** A basic Data repository association check fails. What would you do first?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws fsx describe-backups` and capture exact status/reason/request ID. imports/exports metadata/data between Lustre and S3 under explicit lifecycle. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-FSX-JP-03

- [ ] **Question:** A basic FSx for ONTAP check fails. What would you do first?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws fsx describe-data-repository-associations` and capture exact status/reason/request ID. NFS/SMB/iSCSI plus snapshots/clones/tiering for enterprise data workflows. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-FSX-JP-04

- [ ] **Code:** **Question:** A basic FSx for Windows check fails. What would you do first using the CLI?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lfs df -h && lfs osts` and capture exact status/reason/request ID. SMB/Active Directory integration for Windows applications. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-FSX-JP-05

- [ ] **Question:** A basic FSx for OpenZFS check fails. What would you do first?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws fsx describe-file-systems` and capture exact status/reason/request ID. NFS and ZFS snapshot/clone/compression semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-FSX-JP-06

- [ ] **Question:** A basic Deployment type check fails. What would you do first?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws fsx describe-backups` and capture exact status/reason/request ID. scratch/persistent or single/multi-AZ options vary by filesystem and durability need. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-FSX-JP-07

- [ ] **Code:** **Question:** A basic Throughput/capacity check fails. What would you do first using the CLI?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws fsx describe-data-repository-associations` and capture exact status/reason/request ID. provisioned storage, throughput, SSD/metadata and cache must match I/O profile. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-FSX-JP-08

- [ ] **Question:** A basic Network/DNS/security check fails. What would you do first?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lfs df -h && lfs osts` and capture exact status/reason/request ID. subnets/routes/SG and directory identity are part of mount path. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-FSX-JP-09

- [ ] **Question:** A basic Backup/snapshot check fails. What would you do first?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws fsx describe-file-systems` and capture exact status/reason/request ID. feature and recovery behavior differ by filesystem; test application restore. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-FSX-JP-10

- [ ] **Code:** **Question:** A basic Model/training cache check fails. What would you do first using the CLI?
> **Covered in:** [Amazon FSx — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws fsx describe-backups` and capture exact status/reason/request ID. benchmark metadata, aggregate read, first load and node count rather than headline throughput. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-FSX-MN-01

- [ ] **Question:** Compare FSx for Lustre with Data repository association. When would each change your design?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** FSx for Lustre: parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Data repository association: imports/exports metadata/data between Lustre and S3 under explicit lifecycle. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-FSX-MN-02

- [ ] **Question:** Compare Data repository association with FSx for ONTAP. When would each change your design?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Data repository association: imports/exports metadata/data between Lustre and S3 under explicit lifecycle. FSx for ONTAP: NFS/SMB/iSCSI plus snapshots/clones/tiering for enterprise data workflows. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-FSX-MN-03

- [ ] **Question:** Compare FSx for ONTAP with FSx for Windows. When would each change your design?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** FSx for ONTAP: NFS/SMB/iSCSI plus snapshots/clones/tiering for enterprise data workflows. FSx for Windows: SMB/Active Directory integration for Windows applications. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-FSX-MN-04

- [ ] **Configuration review:** **Question:** Compare FSx for Windows with FSx for OpenZFS. When would each change your design?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** FSx for Windows: SMB/Active Directory integration for Windows applications. FSx for OpenZFS: NFS and ZFS snapshot/clone/compression semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-FSX-MN-05

- [ ] **Question:** Compare FSx for OpenZFS with Deployment type. When would each change your design?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** FSx for OpenZFS: NFS and ZFS snapshot/clone/compression semantics. Deployment type: scratch/persistent or single/multi-AZ options vary by filesystem and durability need. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-FSX-MN-06

- [ ] **Question:** Compare Deployment type with Throughput/capacity. When would each change your design?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Deployment type: scratch/persistent or single/multi-AZ options vary by filesystem and durability need. Throughput/capacity: provisioned storage, throughput, SSD/metadata and cache must match I/O profile. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-FSX-MN-07

- [ ] **Configuration review:** **Question:** Compare Throughput/capacity with Network/DNS/security. When would each change your design?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Throughput/capacity: provisioned storage, throughput, SSD/metadata and cache must match I/O profile. Network/DNS/security: subnets/routes/SG and directory identity are part of mount path. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-FSX-MN-08

- [ ] **Question:** Compare Network/DNS/security with Backup/snapshot. When would each change your design?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Network/DNS/security: subnets/routes/SG and directory identity are part of mount path. Backup/snapshot: feature and recovery behavior differ by filesystem; test application restore. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-FSX-MN-09

- [ ] **Question:** Compare Backup/snapshot with Model/training cache. When would each change your design?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Backup/snapshot: feature and recovery behavior differ by filesystem; test application restore. Model/training cache: benchmark metadata, aggregate read, first load and node count rather than headline throughput. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-FSX-MN-10

- [ ] **Configuration review:** **Question:** Compare Model/training cache with FSx for Lustre. When would each change your design?
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Model/training cache: benchmark metadata, aggregate read, first load and node count rather than headline throughput. FSx for Lustre: parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-FSX-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around FSx for Lustre; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws fsx describe-file-systems` plus recent events/changes, then correlate the service-specific SLI. parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-FSX-MP-02

- [ ] **Question:** Production is degraded around Data repository association; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws fsx describe-backups` plus recent events/changes, then correlate the service-specific SLI. imports/exports metadata/data between Lustre and S3 under explicit lifecycle. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-FSX-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around FSx for ONTAP; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws fsx describe-data-repository-associations` plus recent events/changes, then correlate the service-specific SLI. NFS/SMB/iSCSI plus snapshots/clones/tiering for enterprise data workflows. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-FSX-MP-04

- [ ] **Question:** Production is degraded around FSx for Windows; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lfs df -h && lfs osts` plus recent events/changes, then correlate the service-specific SLI. SMB/Active Directory integration for Windows applications. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-FSX-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around FSx for OpenZFS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws fsx describe-file-systems` plus recent events/changes, then correlate the service-specific SLI. NFS and ZFS snapshot/clone/compression semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-FSX-MP-06

- [ ] **Question:** Production is degraded around Deployment type; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws fsx describe-backups` plus recent events/changes, then correlate the service-specific SLI. scratch/persistent or single/multi-AZ options vary by filesystem and durability need. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-FSX-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Throughput/capacity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws fsx describe-data-repository-associations` plus recent events/changes, then correlate the service-specific SLI. provisioned storage, throughput, SSD/metadata and cache must match I/O profile. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-FSX-MP-08

- [ ] **Question:** Production is degraded around Network/DNS/security; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lfs df -h && lfs osts` plus recent events/changes, then correlate the service-specific SLI. subnets/routes/SG and directory identity are part of mount path. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-FSX-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Backup/snapshot; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws fsx describe-file-systems` plus recent events/changes, then correlate the service-specific SLI. feature and recovery behavior differ by filesystem; test application restore. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-FSX-MP-10

- [ ] **Question:** Production is degraded around Model/training cache; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws fsx describe-backups` plus recent events/changes, then correlate the service-specific SLI. benchmark metadata, aggregate read, first load and node count rather than headline throughput. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-FSX-SN-01

- [ ] **Question:** Design a production Amazon FSx capability where FSx for Lustre, FSx for Windows and Throughput/capacity are first-class requirements.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. SMB/Active Directory integration for Windows applications. provisioned storage, throughput, SSD/metadata and cache must match I/O profile. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-FSX-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon FSx capability where Data repository association, FSx for OpenZFS and Network/DNS/security are first-class requirements.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: imports/exports metadata/data between Lustre and S3 under explicit lifecycle. NFS and ZFS snapshot/clone/compression semantics. subnets/routes/SG and directory identity are part of mount path. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-FSX-SN-03

- [ ] **Question:** Design a production Amazon FSx capability where FSx for ONTAP, Deployment type and Backup/snapshot are first-class requirements.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: NFS/SMB/iSCSI plus snapshots/clones/tiering for enterprise data workflows. scratch/persistent or single/multi-AZ options vary by filesystem and durability need. feature and recovery behavior differ by filesystem; test application restore. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-FSX-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon FSx capability where FSx for Windows, Throughput/capacity and Model/training cache are first-class requirements.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: SMB/Active Directory integration for Windows applications. provisioned storage, throughput, SSD/metadata and cache must match I/O profile. benchmark metadata, aggregate read, first load and node count rather than headline throughput. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-FSX-SN-05

- [ ] **Question:** Design a production Amazon FSx capability where FSx for OpenZFS, Network/DNS/security and FSx for Lustre are first-class requirements.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: NFS and ZFS snapshot/clone/compression semantics. subnets/routes/SG and directory identity are part of mount path. parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-FSX-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon FSx capability where Deployment type, Backup/snapshot and Data repository association are first-class requirements.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scratch/persistent or single/multi-AZ options vary by filesystem and durability need. feature and recovery behavior differ by filesystem; test application restore. imports/exports metadata/data between Lustre and S3 under explicit lifecycle. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-FSX-SN-07

- [ ] **Question:** Design a production Amazon FSx capability where Throughput/capacity, Model/training cache and FSx for ONTAP are first-class requirements.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: provisioned storage, throughput, SSD/metadata and cache must match I/O profile. benchmark metadata, aggregate read, first load and node count rather than headline throughput. NFS/SMB/iSCSI plus snapshots/clones/tiering for enterprise data workflows. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-FSX-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon FSx capability where Network/DNS/security, FSx for Lustre and FSx for Windows are first-class requirements.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: subnets/routes/SG and directory identity are part of mount path. parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. SMB/Active Directory integration for Windows applications. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-FSX-SN-09

- [ ] **Question:** Design a production Amazon FSx capability where Backup/snapshot, Data repository association and FSx for OpenZFS are first-class requirements.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: feature and recovery behavior differ by filesystem; test application restore. imports/exports metadata/data between Lustre and S3 under explicit lifecycle. NFS and ZFS snapshot/clone/compression semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-FSX-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon FSx capability where Model/training cache, FSx for ONTAP and Deployment type are first-class requirements.
> **Covered in:** [Amazon FSx — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: benchmark metadata, aggregate read, first load and node count rather than headline throughput. NFS/SMB/iSCSI plus snapshots/clones/tiering for enterprise data workflows. scratch/persistent or single/multi-AZ options vary by filesystem and durability need. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-FSX-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving FSx for Lustre. How do you lead it end to end?
> **Covered in:** [Amazon FSx — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws fsx describe-file-systems` as one read-only checkpoint, not the whole diagnosis. parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-FSX-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Data repository association. How do you lead it end to end?
> **Covered in:** [Amazon FSx — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws fsx describe-backups` as one read-only checkpoint, not the whole diagnosis. imports/exports metadata/data between Lustre and S3 under explicit lifecycle. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-FSX-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving FSx for ONTAP. How do you lead it end to end?
> **Covered in:** [Amazon FSx — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws fsx describe-data-repository-associations` as one read-only checkpoint, not the whole diagnosis. NFS/SMB/iSCSI plus snapshots/clones/tiering for enterprise data workflows. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-FSX-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving FSx for Windows. How do you lead it end to end?
> **Covered in:** [Amazon FSx — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lfs df -h && lfs osts` as one read-only checkpoint, not the whole diagnosis. SMB/Active Directory integration for Windows applications. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-FSX-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving FSx for OpenZFS. How do you lead it end to end?
> **Covered in:** [Amazon FSx — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws fsx describe-file-systems` as one read-only checkpoint, not the whole diagnosis. NFS and ZFS snapshot/clone/compression semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-FSX-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deployment type. How do you lead it end to end?
> **Covered in:** [Amazon FSx — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws fsx describe-backups` as one read-only checkpoint, not the whole diagnosis. scratch/persistent or single/multi-AZ options vary by filesystem and durability need. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-FSX-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Throughput/capacity. How do you lead it end to end?
> **Covered in:** [Amazon FSx — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws fsx describe-data-repository-associations` as one read-only checkpoint, not the whole diagnosis. provisioned storage, throughput, SSD/metadata and cache must match I/O profile. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-FSX-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Network/DNS/security. How do you lead it end to end?
> **Covered in:** [Amazon FSx — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lfs df -h && lfs osts` as one read-only checkpoint, not the whole diagnosis. subnets/routes/SG and directory identity are part of mount path. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-FSX-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backup/snapshot. How do you lead it end to end?
> **Covered in:** [Amazon FSx — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws fsx describe-file-systems` as one read-only checkpoint, not the whole diagnosis. feature and recovery behavior differ by filesystem; test application restore. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-FSX-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model/training cache. How do you lead it end to end?
> **Covered in:** [Amazon FSx — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws fsx describe-backups` as one read-only checkpoint, not the whole diagnosis. benchmark metadata, aggregate read, first load and node count rather than headline throughput. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon EFS](../03-efs/README.md) · [Study note](README.md) · [Next: AWS Backup →](../05-aws-backup/README.md)

<!-- reading-navigation:end -->
