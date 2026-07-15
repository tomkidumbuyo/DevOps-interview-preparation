# Storage — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-STORAGE-JN-01

- [ ] **Question:** What is Object/key, and why does it matter in Storage?

**Answer:** immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-STORAGE-JN-02

- [ ] **Question:** What is Strong consistency, and why does it matter in Storage?

**Answer:** successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-STORAGE-JN-03

- [ ] **Question:** What is gp3, and why does it matter in Storage?

**Answer:** general SSD with independently configurable size, IOPS and throughput within limits. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-STORAGE-JN-04

- [ ] **Question:** What is io2, and why does it matter in Storage?

**Answer:** high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-STORAGE-JN-05

- [ ] **Question:** What is Mount target, and why does it matter in Storage?

**Answer:** ENI per selected AZ provides NFS endpoint and security-group boundary. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-STORAGE-JN-06

- [ ] **Question:** What is NFS semantics, and why does it matter in Storage?

**Answer:** shared file access, locking, metadata and close-to-open behavior differ from object/block storage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-STORAGE-JN-07

- [ ] **Question:** What is FSx for Lustre, and why does it matter in Storage?

**Answer:** parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-STORAGE-JN-08

- [ ] **Code:** **Question:** What does `aws efs describe-file-systems` help you verify for Storage?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: imports/exports metadata/data between Lustre and S3 under explicit lifecycle.

### BRANCH-STORAGE-JN-09

- [ ] **Code:** **Question:** What does `aws fsx describe-file-systems` help you verify for Storage?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: schedule, window, lifecycle and copy rules define intended RPO/retention.

### BRANCH-STORAGE-JN-10

- [ ] **Code:** **Question:** What does `aws backup list-backup-plans` help you verify for Storage?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: tags/ARNs/roles determine coverage and need inventory validation.

## Junior — procedural and command questions

### BRANCH-STORAGE-JP-01

- [ ] **Code:** **Question:** A basic Object/key check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api head-object --bucket BUCKET --key KEY` and capture exact status/reason/request ID. immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-STORAGE-JP-02

- [ ] **Question:** A basic Strong consistency check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-volumes --volume-ids VOLUME_ID` and capture exact status/reason/request ID. successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-STORAGE-JP-03

- [ ] **Question:** A basic gp3 check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws efs describe-file-systems` and capture exact status/reason/request ID. general SSD with independently configurable size, IOPS and throughput within limits. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-STORAGE-JP-04

- [ ] **Code:** **Question:** A basic io2 check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws fsx describe-file-systems` and capture exact status/reason/request ID. high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-STORAGE-JP-05

- [ ] **Question:** A basic Mount target check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-backup-plans` and capture exact status/reason/request ID. ENI per selected AZ provides NFS endpoint and security-group boundary. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-STORAGE-JP-06

- [ ] **Question:** A basic NFS semantics check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api head-object --bucket BUCKET --key KEY` and capture exact status/reason/request ID. shared file access, locking, metadata and close-to-open behavior differ from object/block storage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-STORAGE-JP-07

- [ ] **Code:** **Question:** A basic FSx for Lustre check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-volumes --volume-ids VOLUME_ID` and capture exact status/reason/request ID. parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-STORAGE-JP-08

- [ ] **Question:** A basic Data repository association check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws efs describe-file-systems` and capture exact status/reason/request ID. imports/exports metadata/data between Lustre and S3 under explicit lifecycle. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-STORAGE-JP-09

- [ ] **Question:** A basic Backup plan check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws fsx describe-file-systems` and capture exact status/reason/request ID. schedule, window, lifecycle and copy rules define intended RPO/retention. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-STORAGE-JP-10

- [ ] **Code:** **Question:** A basic Resource selection check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-backup-plans` and capture exact status/reason/request ID. tags/ARNs/roles determine coverage and need inventory validation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-STORAGE-MN-01

- [ ] **Question:** Compare Object/key with Strong consistency. When would each change your design?

**Answer:** Object/key: immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Strong consistency: successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-STORAGE-MN-02

- [ ] **Question:** Compare Strong consistency with gp3. When would each change your design?

**Answer:** Strong consistency: successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. gp3: general SSD with independently configurable size, IOPS and throughput within limits. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-STORAGE-MN-03

- [ ] **Question:** Compare gp3 with io2. When would each change your design?

**Answer:** gp3: general SSD with independently configurable size, IOPS and throughput within limits. io2: high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-STORAGE-MN-04

- [ ] **Configuration review:** **Question:** Compare io2 with Mount target. When would each change your design?

**Answer:** io2: high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. Mount target: ENI per selected AZ provides NFS endpoint and security-group boundary. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-STORAGE-MN-05

- [ ] **Question:** Compare Mount target with NFS semantics. When would each change your design?

**Answer:** Mount target: ENI per selected AZ provides NFS endpoint and security-group boundary. NFS semantics: shared file access, locking, metadata and close-to-open behavior differ from object/block storage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-STORAGE-MN-06

- [ ] **Question:** Compare NFS semantics with FSx for Lustre. When would each change your design?

**Answer:** NFS semantics: shared file access, locking, metadata and close-to-open behavior differ from object/block storage. FSx for Lustre: parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-STORAGE-MN-07

- [ ] **Configuration review:** **Question:** Compare FSx for Lustre with Data repository association. When would each change your design?

**Answer:** FSx for Lustre: parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Data repository association: imports/exports metadata/data between Lustre and S3 under explicit lifecycle. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-STORAGE-MN-08

- [ ] **Question:** Compare Data repository association with Backup plan. When would each change your design?

**Answer:** Data repository association: imports/exports metadata/data between Lustre and S3 under explicit lifecycle. Backup plan: schedule, window, lifecycle and copy rules define intended RPO/retention. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-STORAGE-MN-09

- [ ] **Question:** Compare Backup plan with Resource selection. When would each change your design?

**Answer:** Backup plan: schedule, window, lifecycle and copy rules define intended RPO/retention. Resource selection: tags/ARNs/roles determine coverage and need inventory validation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-STORAGE-MN-10

- [ ] **Configuration review:** **Question:** Compare Resource selection with Object/key. When would each change your design?

**Answer:** Resource selection: tags/ARNs/roles determine coverage and need inventory validation. Object/key: immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-STORAGE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Object/key; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api head-object --bucket BUCKET --key KEY` plus recent events/changes, then correlate the service-specific SLI. immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-STORAGE-MP-02

- [ ] **Question:** Production is degraded around Strong consistency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-volumes --volume-ids VOLUME_ID` plus recent events/changes, then correlate the service-specific SLI. successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-STORAGE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around gp3; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws efs describe-file-systems` plus recent events/changes, then correlate the service-specific SLI. general SSD with independently configurable size, IOPS and throughput within limits. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-STORAGE-MP-04

- [ ] **Question:** Production is degraded around io2; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws fsx describe-file-systems` plus recent events/changes, then correlate the service-specific SLI. high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-STORAGE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Mount target; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-backup-plans` plus recent events/changes, then correlate the service-specific SLI. ENI per selected AZ provides NFS endpoint and security-group boundary. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-STORAGE-MP-06

- [ ] **Question:** Production is degraded around NFS semantics; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api head-object --bucket BUCKET --key KEY` plus recent events/changes, then correlate the service-specific SLI. shared file access, locking, metadata and close-to-open behavior differ from object/block storage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-STORAGE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around FSx for Lustre; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-volumes --volume-ids VOLUME_ID` plus recent events/changes, then correlate the service-specific SLI. parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-STORAGE-MP-08

- [ ] **Question:** Production is degraded around Data repository association; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws efs describe-file-systems` plus recent events/changes, then correlate the service-specific SLI. imports/exports metadata/data between Lustre and S3 under explicit lifecycle. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-STORAGE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Backup plan; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws fsx describe-file-systems` plus recent events/changes, then correlate the service-specific SLI. schedule, window, lifecycle and copy rules define intended RPO/retention. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-STORAGE-MP-10

- [ ] **Question:** Production is degraded around Resource selection; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-backup-plans` plus recent events/changes, then correlate the service-specific SLI. tags/ARNs/roles determine coverage and need inventory validation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-STORAGE-SN-01

- [ ] **Question:** Design a production Storage capability where Object/key, io2 and FSx for Lustre are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-STORAGE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Storage capability where Strong consistency, Mount target and Data repository association are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. ENI per selected AZ provides NFS endpoint and security-group boundary. imports/exports metadata/data between Lustre and S3 under explicit lifecycle. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-STORAGE-SN-03

- [ ] **Question:** Design a production Storage capability where gp3, NFS semantics and Backup plan are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: general SSD with independently configurable size, IOPS and throughput within limits. shared file access, locking, metadata and close-to-open behavior differ from object/block storage. schedule, window, lifecycle and copy rules define intended RPO/retention. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-STORAGE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Storage capability where io2, FSx for Lustre and Resource selection are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. tags/ARNs/roles determine coverage and need inventory validation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-STORAGE-SN-05

- [ ] **Question:** Design a production Storage capability where Mount target, Data repository association and Object/key are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ENI per selected AZ provides NFS endpoint and security-group boundary. imports/exports metadata/data between Lustre and S3 under explicit lifecycle. immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-STORAGE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Storage capability where NFS semantics, Backup plan and Strong consistency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: shared file access, locking, metadata and close-to-open behavior differ from object/block storage. schedule, window, lifecycle and copy rules define intended RPO/retention. successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-STORAGE-SN-07

- [ ] **Question:** Design a production Storage capability where FSx for Lustre, Resource selection and gp3 are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. tags/ARNs/roles determine coverage and need inventory validation. general SSD with independently configurable size, IOPS and throughput within limits. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-STORAGE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Storage capability where Data repository association, Object/key and io2 are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: imports/exports metadata/data between Lustre and S3 under explicit lifecycle. immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-STORAGE-SN-09

- [ ] **Question:** Design a production Storage capability where Backup plan, Strong consistency and Mount target are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: schedule, window, lifecycle and copy rules define intended RPO/retention. successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. ENI per selected AZ provides NFS endpoint and security-group boundary. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-STORAGE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Storage capability where Resource selection, gp3 and NFS semantics are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tags/ARNs/roles determine coverage and need inventory validation. general SSD with independently configurable size, IOPS and throughput within limits. shared file access, locking, metadata and close-to-open behavior differ from object/block storage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-STORAGE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Object/key. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api head-object --bucket BUCKET --key KEY` as one read-only checkpoint, not the whole diagnosis. immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-STORAGE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Strong consistency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-volumes --volume-ids VOLUME_ID` as one read-only checkpoint, not the whole diagnosis. successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-STORAGE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving gp3. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws efs describe-file-systems` as one read-only checkpoint, not the whole diagnosis. general SSD with independently configurable size, IOPS and throughput within limits. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-STORAGE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving io2. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws fsx describe-file-systems` as one read-only checkpoint, not the whole diagnosis. high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-STORAGE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Mount target. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-backup-plans` as one read-only checkpoint, not the whole diagnosis. ENI per selected AZ provides NFS endpoint and security-group boundary. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-STORAGE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NFS semantics. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api head-object --bucket BUCKET --key KEY` as one read-only checkpoint, not the whole diagnosis. shared file access, locking, metadata and close-to-open behavior differ from object/block storage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-STORAGE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving FSx for Lustre. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-volumes --volume-ids VOLUME_ID` as one read-only checkpoint, not the whole diagnosis. parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-STORAGE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Data repository association. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws efs describe-file-systems` as one read-only checkpoint, not the whole diagnosis. imports/exports metadata/data between Lustre and S3 under explicit lifecycle. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-STORAGE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backup plan. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws fsx describe-file-systems` as one read-only checkpoint, not the whole diagnosis. schedule, window, lifecycle and copy rules define intended RPO/retention. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-STORAGE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource selection. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-backup-plans` as one read-only checkpoint, not the whole diagnosis. tags/ARNs/roles determine coverage and need inventory validation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
