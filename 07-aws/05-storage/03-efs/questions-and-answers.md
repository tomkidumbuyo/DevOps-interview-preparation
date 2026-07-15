# Amazon EFS — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-EFS-JN-01

- [ ] **Question:** What is Mount target, and why does it matter in Amazon EFS?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ENI per selected AZ provides NFS endpoint and security-group boundary. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EFS-JN-02

- [ ] **Question:** What is NFS semantics, and why does it matter in Amazon EFS?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** shared file access, locking, metadata and close-to-open behavior differ from object/block storage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EFS-JN-03

- [ ] **Question:** What is Access point, and why does it matter in Amazon EFS?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** enforces root directory and POSIX identity for an application path. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EFS-JN-04

- [ ] **Question:** What is IAM/TLS mount, and why does it matter in Amazon EFS?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** helper can authenticate/encrypt supported client mount sessions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EFS-JN-05

- [ ] **Question:** What is Performance mode, and why does it matter in Amazon EFS?
> **Covered in:** [Amazon EFS — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** general/max-I/O choices trade latency and scale under service constraints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EFS-JN-06

- [ ] **Question:** What is Throughput mode, and why does it matter in Amazon EFS?
> **Covered in:** [Amazon EFS — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** bursting/provisioned/elastic choices affect limits and billing. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EFS-JN-07

- [ ] **Question:** What is Lifecycle/IA, and why does it matter in Amazon EFS?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** moves files based on access and incurs retrieval/transition considerations. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EFS-JN-08

- [ ] **Code:** **Question:** What does `mount | rg nfs && nfsstat -m` help you verify for Amazon EFS?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: clients should normally use a mount target in their AZ for availability/cost/latency.

### AMAZON-EFS-JN-09

- [ ] **Code:** **Question:** What does `aws efs describe-file-systems` help you verify for Amazon EFS?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: UID/GID/mode/ACL plus access-point behavior determine file access.

### AMAZON-EFS-JN-10

- [ ] **Code:** **Question:** What does `aws efs describe-mount-targets --file-system-id FS_ID` help you verify for Amazon EFS?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: shared filesystem still needs application-consistent policy and restore testing.

## Junior — procedural and command questions

### AMAZON-EFS-JP-01

- [ ] **Code:** **Question:** A basic Mount target check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws efs describe-file-systems` and capture exact status/reason/request ID. ENI per selected AZ provides NFS endpoint and security-group boundary. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EFS-JP-02

- [ ] **Question:** A basic NFS semantics check fails. What would you do first?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws efs describe-mount-targets --file-system-id FS_ID` and capture exact status/reason/request ID. shared file access, locking, metadata and close-to-open behavior differ from object/block storage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EFS-JP-03

- [ ] **Question:** A basic Access point check fails. What would you do first?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws efs describe-access-points --file-system-id FS_ID` and capture exact status/reason/request ID. enforces root directory and POSIX identity for an application path. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EFS-JP-04

- [ ] **Code:** **Question:** A basic IAM/TLS mount check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mount | rg nfs && nfsstat -m` and capture exact status/reason/request ID. helper can authenticate/encrypt supported client mount sessions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EFS-JP-05

- [ ] **Question:** A basic Performance mode check fails. What would you do first?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws efs describe-file-systems` and capture exact status/reason/request ID. general/max-I/O choices trade latency and scale under service constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EFS-JP-06

- [ ] **Question:** A basic Throughput mode check fails. What would you do first?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws efs describe-mount-targets --file-system-id FS_ID` and capture exact status/reason/request ID. bursting/provisioned/elastic choices affect limits and billing. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EFS-JP-07

- [ ] **Code:** **Question:** A basic Lifecycle/IA check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws efs describe-access-points --file-system-id FS_ID` and capture exact status/reason/request ID. moves files based on access and incurs retrieval/transition considerations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EFS-JP-08

- [ ] **Question:** A basic Local-AZ mount check fails. What would you do first?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mount | rg nfs && nfsstat -m` and capture exact status/reason/request ID. clients should normally use a mount target in their AZ for availability/cost/latency. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EFS-JP-09

- [ ] **Question:** A basic POSIX permissions check fails. What would you do first?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws efs describe-file-systems` and capture exact status/reason/request ID. UID/GID/mode/ACL plus access-point behavior determine file access. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EFS-JP-10

- [ ] **Code:** **Question:** A basic Backup/restore check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EFS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws efs describe-mount-targets --file-system-id FS_ID` and capture exact status/reason/request ID. shared filesystem still needs application-consistent policy and restore testing. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-EFS-MN-01

- [ ] **Question:** Compare Mount target with NFS semantics. When would each change your design?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Mount target: ENI per selected AZ provides NFS endpoint and security-group boundary. NFS semantics: shared file access, locking, metadata and close-to-open behavior differ from object/block storage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EFS-MN-02

- [ ] **Question:** Compare NFS semantics with Access point. When would each change your design?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** NFS semantics: shared file access, locking, metadata and close-to-open behavior differ from object/block storage. Access point: enforces root directory and POSIX identity for an application path. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EFS-MN-03

- [ ] **Question:** Compare Access point with IAM/TLS mount. When would each change your design?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Access point: enforces root directory and POSIX identity for an application path. IAM/TLS mount: helper can authenticate/encrypt supported client mount sessions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EFS-MN-04

- [ ] **Configuration review:** **Question:** Compare IAM/TLS mount with Performance mode. When would each change your design?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** IAM/TLS mount: helper can authenticate/encrypt supported client mount sessions. Performance mode: general/max-I/O choices trade latency and scale under service constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EFS-MN-05

- [ ] **Question:** Compare Performance mode with Throughput mode. When would each change your design?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Performance mode: general/max-I/O choices trade latency and scale under service constraints. Throughput mode: bursting/provisioned/elastic choices affect limits and billing. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EFS-MN-06

- [ ] **Question:** Compare Throughput mode with Lifecycle/IA. When would each change your design?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Throughput mode: bursting/provisioned/elastic choices affect limits and billing. Lifecycle/IA: moves files based on access and incurs retrieval/transition considerations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EFS-MN-07

- [ ] **Configuration review:** **Question:** Compare Lifecycle/IA with Local-AZ mount. When would each change your design?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Lifecycle/IA: moves files based on access and incurs retrieval/transition considerations. Local-AZ mount: clients should normally use a mount target in their AZ for availability/cost/latency. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EFS-MN-08

- [ ] **Question:** Compare Local-AZ mount with POSIX permissions. When would each change your design?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Local-AZ mount: clients should normally use a mount target in their AZ for availability/cost/latency. POSIX permissions: UID/GID/mode/ACL plus access-point behavior determine file access. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EFS-MN-09

- [ ] **Question:** Compare POSIX permissions with Backup/restore. When would each change your design?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** POSIX permissions: UID/GID/mode/ACL plus access-point behavior determine file access. Backup/restore: shared filesystem still needs application-consistent policy and restore testing. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EFS-MN-10

- [ ] **Configuration review:** **Question:** Compare Backup/restore with Mount target. When would each change your design?
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Backup/restore: shared filesystem still needs application-consistent policy and restore testing. Mount target: ENI per selected AZ provides NFS endpoint and security-group boundary. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-EFS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Mount target; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws efs describe-file-systems` plus recent events/changes, then correlate the service-specific SLI. ENI per selected AZ provides NFS endpoint and security-group boundary. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EFS-MP-02

- [ ] **Question:** Production is degraded around NFS semantics; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws efs describe-mount-targets --file-system-id FS_ID` plus recent events/changes, then correlate the service-specific SLI. shared file access, locking, metadata and close-to-open behavior differ from object/block storage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EFS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Access point; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws efs describe-access-points --file-system-id FS_ID` plus recent events/changes, then correlate the service-specific SLI. enforces root directory and POSIX identity for an application path. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EFS-MP-04

- [ ] **Question:** Production is degraded around IAM/TLS mount; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mount | rg nfs && nfsstat -m` plus recent events/changes, then correlate the service-specific SLI. helper can authenticate/encrypt supported client mount sessions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EFS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Performance mode; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws efs describe-file-systems` plus recent events/changes, then correlate the service-specific SLI. general/max-I/O choices trade latency and scale under service constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EFS-MP-06

- [ ] **Question:** Production is degraded around Throughput mode; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws efs describe-mount-targets --file-system-id FS_ID` plus recent events/changes, then correlate the service-specific SLI. bursting/provisioned/elastic choices affect limits and billing. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EFS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Lifecycle/IA; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws efs describe-access-points --file-system-id FS_ID` plus recent events/changes, then correlate the service-specific SLI. moves files based on access and incurs retrieval/transition considerations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EFS-MP-08

- [ ] **Question:** Production is degraded around Local-AZ mount; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mount | rg nfs && nfsstat -m` plus recent events/changes, then correlate the service-specific SLI. clients should normally use a mount target in their AZ for availability/cost/latency. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EFS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around POSIX permissions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws efs describe-file-systems` plus recent events/changes, then correlate the service-specific SLI. UID/GID/mode/ACL plus access-point behavior determine file access. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EFS-MP-10

- [ ] **Question:** Production is degraded around Backup/restore; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws efs describe-mount-targets --file-system-id FS_ID` plus recent events/changes, then correlate the service-specific SLI. shared filesystem still needs application-consistent policy and restore testing. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-EFS-SN-01

- [ ] **Question:** Design a production Amazon EFS capability where Mount target, IAM/TLS mount and Lifecycle/IA are first-class requirements.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ENI per selected AZ provides NFS endpoint and security-group boundary. helper can authenticate/encrypt supported client mount sessions. moves files based on access and incurs retrieval/transition considerations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EFS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EFS capability where NFS semantics, Performance mode and Local-AZ mount are first-class requirements.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: shared file access, locking, metadata and close-to-open behavior differ from object/block storage. general/max-I/O choices trade latency and scale under service constraints. clients should normally use a mount target in their AZ for availability/cost/latency. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EFS-SN-03

- [ ] **Question:** Design a production Amazon EFS capability where Access point, Throughput mode and POSIX permissions are first-class requirements.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: enforces root directory and POSIX identity for an application path. bursting/provisioned/elastic choices affect limits and billing. UID/GID/mode/ACL plus access-point behavior determine file access. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EFS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EFS capability where IAM/TLS mount, Lifecycle/IA and Backup/restore are first-class requirements.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: helper can authenticate/encrypt supported client mount sessions. moves files based on access and incurs retrieval/transition considerations. shared filesystem still needs application-consistent policy and restore testing. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EFS-SN-05

- [ ] **Question:** Design a production Amazon EFS capability where Performance mode, Local-AZ mount and Mount target are first-class requirements.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: general/max-I/O choices trade latency and scale under service constraints. clients should normally use a mount target in their AZ for availability/cost/latency. ENI per selected AZ provides NFS endpoint and security-group boundary. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EFS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EFS capability where Throughput mode, POSIX permissions and NFS semantics are first-class requirements.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bursting/provisioned/elastic choices affect limits and billing. UID/GID/mode/ACL plus access-point behavior determine file access. shared file access, locking, metadata and close-to-open behavior differ from object/block storage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EFS-SN-07

- [ ] **Question:** Design a production Amazon EFS capability where Lifecycle/IA, Backup/restore and Access point are first-class requirements.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: moves files based on access and incurs retrieval/transition considerations. shared filesystem still needs application-consistent policy and restore testing. enforces root directory and POSIX identity for an application path. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EFS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EFS capability where Local-AZ mount, Mount target and IAM/TLS mount are first-class requirements.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: clients should normally use a mount target in their AZ for availability/cost/latency. ENI per selected AZ provides NFS endpoint and security-group boundary. helper can authenticate/encrypt supported client mount sessions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EFS-SN-09

- [ ] **Question:** Design a production Amazon EFS capability where POSIX permissions, NFS semantics and Performance mode are first-class requirements.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: UID/GID/mode/ACL plus access-point behavior determine file access. shared file access, locking, metadata and close-to-open behavior differ from object/block storage. general/max-I/O choices trade latency and scale under service constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EFS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EFS capability where Backup/restore, Access point and Throughput mode are first-class requirements.
> **Covered in:** [Amazon EFS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: shared filesystem still needs application-consistent policy and restore testing. enforces root directory and POSIX identity for an application path. bursting/provisioned/elastic choices affect limits and billing. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-EFS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Mount target. How do you lead it end to end?
> **Covered in:** [Amazon EFS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws efs describe-file-systems` as one read-only checkpoint, not the whole diagnosis. ENI per selected AZ provides NFS endpoint and security-group boundary. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EFS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NFS semantics. How do you lead it end to end?
> **Covered in:** [Amazon EFS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws efs describe-mount-targets --file-system-id FS_ID` as one read-only checkpoint, not the whole diagnosis. shared file access, locking, metadata and close-to-open behavior differ from object/block storage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EFS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Access point. How do you lead it end to end?
> **Covered in:** [Amazon EFS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws efs describe-access-points --file-system-id FS_ID` as one read-only checkpoint, not the whole diagnosis. enforces root directory and POSIX identity for an application path. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EFS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IAM/TLS mount. How do you lead it end to end?
> **Covered in:** [Amazon EFS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mount | rg nfs && nfsstat -m` as one read-only checkpoint, not the whole diagnosis. helper can authenticate/encrypt supported client mount sessions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EFS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Performance mode. How do you lead it end to end?
> **Covered in:** [Amazon EFS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws efs describe-file-systems` as one read-only checkpoint, not the whole diagnosis. general/max-I/O choices trade latency and scale under service constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EFS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Throughput mode. How do you lead it end to end?
> **Covered in:** [Amazon EFS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws efs describe-mount-targets --file-system-id FS_ID` as one read-only checkpoint, not the whole diagnosis. bursting/provisioned/elastic choices affect limits and billing. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EFS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lifecycle/IA. How do you lead it end to end?
> **Covered in:** [Amazon EFS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws efs describe-access-points --file-system-id FS_ID` as one read-only checkpoint, not the whole diagnosis. moves files based on access and incurs retrieval/transition considerations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EFS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Local-AZ mount. How do you lead it end to end?
> **Covered in:** [Amazon EFS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mount | rg nfs && nfsstat -m` as one read-only checkpoint, not the whole diagnosis. clients should normally use a mount target in their AZ for availability/cost/latency. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EFS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving POSIX permissions. How do you lead it end to end?
> **Covered in:** [Amazon EFS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws efs describe-file-systems` as one read-only checkpoint, not the whole diagnosis. UID/GID/mode/ACL plus access-point behavior determine file access. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EFS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backup/restore. How do you lead it end to end?
> **Covered in:** [Amazon EFS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws efs describe-mount-targets --file-system-id FS_ID` as one read-only checkpoint, not the whole diagnosis. shared filesystem still needs application-consistent policy and restore testing. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon EBS](../02-ebs/README.md) · [Study note](README.md) · [Next: Amazon FSx →](../04-fsx/README.md)

<!-- reading-navigation:end -->
