# Amazon S3 — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-S3-JN-01

- [ ] **Question:** What is Object/key, and why does it matter in Amazon S3?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-S3-JN-02

- [ ] **Question:** What is Strong consistency, and why does it matter in Amazon S3?
> **Covered in:** [Amazon S3 — Data, consistency and lifecycle](README.md#data-consistency-and-lifecycle)

**Answer:** successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-S3-JN-03

- [ ] **Question:** What is Versioning, and why does it matter in Amazon S3?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** preserves version IDs/delete markers for recovery and is not sufficient if one principal can purge all versions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-S3-JN-04

- [ ] **Question:** What is Storage classes, and why does it matter in Amazon S3?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** trade access/retrieval/minimum-duration/AZ resilience and monitoring cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-S3-JN-05

- [ ] **Question:** What is Lifecycle, and why does it matter in Amazon S3?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** asynchronously transitions/expires current/noncurrent versions and incomplete multipart uploads. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-S3-JN-06

- [ ] **Question:** What is Multipart/checksum, and why does it matter in Amazon S3?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** parallel parts and integrity checks improve large transfer reliability but abandoned uploads cost money. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-S3-JN-07

- [ ] **Question:** What is Authorization intersection, and why does it matter in Amazon S3?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** identity, bucket/access point, SCP/boundary/session, endpoint and KMS policies can all constrain. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-S3-JN-08

- [ ] **Code:** **Question:** What does `aws s3api get-bucket-replication --bucket BUCKET` help you verify for Amazon S3?
> **Covered in:** [Amazon S3 — Availability, observability and recovery](README.md#availability-observability-and-recovery)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: SSE-S3/KMS/DSSE/client methods differ in control, audit, quota and recovery.

### AMAZON-S3-JN-09

- [ ] **Code:** **Question:** What does `aws s3api head-object --bucket BUCKET --key KEY` help you verify for Amazon S3?
> **Covered in:** [Amazon S3 — Availability, observability and recovery](README.md#availability-observability-and-recovery)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: asynchronous SRR/CRR needs versioning, IAM/KMS, existing-object/delete behavior and monitoring.

### AMAZON-S3-JN-10

- [ ] **Code:** **Question:** What does `aws s3api list-object-versions --bucket BUCKET --prefix KEY` help you verify for Amazon S3?
> **Covered in:** [Amazon S3 — Availability, observability and recovery](README.md#availability-observability-and-recovery)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: notifications can duplicate/reorder, so consumers need idempotency and reconciliation.

## Junior — procedural and command questions

### AMAZON-S3-JP-01

- [ ] **Code:** **Question:** A basic Object/key check fails. What would you do first using the CLI?
> **Covered in:** [Amazon S3 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api head-object --bucket BUCKET --key KEY` and capture exact status/reason/request ID. immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-S3-JP-02

- [ ] **Question:** A basic Strong consistency check fails. What would you do first?
> **Covered in:** [Amazon S3 — Data, consistency and lifecycle](README.md#data-consistency-and-lifecycle)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api list-object-versions --bucket BUCKET --prefix KEY` and capture exact status/reason/request ID. successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-S3-JP-03

- [ ] **Question:** A basic Versioning check fails. What would you do first?
> **Covered in:** [Amazon S3 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api get-public-access-block --bucket BUCKET` and capture exact status/reason/request ID. preserves version IDs/delete markers for recovery and is not sufficient if one principal can purge all versions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-S3-JP-04

- [ ] **Code:** **Question:** A basic Storage classes check fails. What would you do first using the CLI?
> **Covered in:** [Amazon S3 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api get-bucket-replication --bucket BUCKET` and capture exact status/reason/request ID. trade access/retrieval/minimum-duration/AZ resilience and monitoring cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-S3-JP-05

- [ ] **Question:** A basic Lifecycle check fails. What would you do first?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api head-object --bucket BUCKET --key KEY` and capture exact status/reason/request ID. asynchronously transitions/expires current/noncurrent versions and incomplete multipart uploads. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-S3-JP-06

- [ ] **Question:** A basic Multipart/checksum check fails. What would you do first?
> **Covered in:** [Amazon S3 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api list-object-versions --bucket BUCKET --prefix KEY` and capture exact status/reason/request ID. parallel parts and integrity checks improve large transfer reliability but abandoned uploads cost money. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-S3-JP-07

- [ ] **Code:** **Question:** A basic Authorization intersection check fails. What would you do first using the CLI?
> **Covered in:** [Amazon S3 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api get-public-access-block --bucket BUCKET` and capture exact status/reason/request ID. identity, bucket/access point, SCP/boundary/session, endpoint and KMS policies can all constrain. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-S3-JP-08

- [ ] **Question:** A basic Encryption check fails. What would you do first?
> **Covered in:** [Amazon S3 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api get-bucket-replication --bucket BUCKET` and capture exact status/reason/request ID. SSE-S3/KMS/DSSE/client methods differ in control, audit, quota and recovery. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-S3-JP-09

- [ ] **Question:** A basic Replication check fails. What would you do first?
> **Covered in:** [Amazon S3 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api head-object --bucket BUCKET --key KEY` and capture exact status/reason/request ID. asynchronous SRR/CRR needs versioning, IAM/KMS, existing-object/delete behavior and monitoring. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-S3-JP-10

- [ ] **Code:** **Question:** A basic Events check fails. What would you do first using the CLI?
> **Covered in:** [Amazon S3 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws s3api list-object-versions --bucket BUCKET --prefix KEY` and capture exact status/reason/request ID. notifications can duplicate/reorder, so consumers need idempotency and reconciliation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-S3-MN-01

- [ ] **Question:** Compare Object/key with Strong consistency. When would each change your design?
> **Covered in:** [Amazon S3 — Data, consistency and lifecycle](README.md#data-consistency-and-lifecycle)

**Answer:** Object/key: immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Strong consistency: successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-S3-MN-02

- [ ] **Question:** Compare Strong consistency with Versioning. When would each change your design?
> **Covered in:** [Amazon S3 — Data, consistency and lifecycle](README.md#data-consistency-and-lifecycle)

**Answer:** Strong consistency: successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. Versioning: preserves version IDs/delete markers for recovery and is not sufficient if one principal can purge all versions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-S3-MN-03

- [ ] **Question:** Compare Versioning with Storage classes. When would each change your design?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Versioning: preserves version IDs/delete markers for recovery and is not sufficient if one principal can purge all versions. Storage classes: trade access/retrieval/minimum-duration/AZ resilience and monitoring cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-S3-MN-04

- [ ] **Configuration review:** **Question:** Compare Storage classes with Lifecycle. When would each change your design?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Storage classes: trade access/retrieval/minimum-duration/AZ resilience and monitoring cost. Lifecycle: asynchronously transitions/expires current/noncurrent versions and incomplete multipart uploads. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-S3-MN-05

- [ ] **Question:** Compare Lifecycle with Multipart/checksum. When would each change your design?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Lifecycle: asynchronously transitions/expires current/noncurrent versions and incomplete multipart uploads. Multipart/checksum: parallel parts and integrity checks improve large transfer reliability but abandoned uploads cost money. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-S3-MN-06

- [ ] **Question:** Compare Multipart/checksum with Authorization intersection. When would each change your design?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Multipart/checksum: parallel parts and integrity checks improve large transfer reliability but abandoned uploads cost money. Authorization intersection: identity, bucket/access point, SCP/boundary/session, endpoint and KMS policies can all constrain. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-S3-MN-07

- [ ] **Configuration review:** **Question:** Compare Authorization intersection with Encryption. When would each change your design?
> **Covered in:** [Amazon S3 — Authorization and encryption](README.md#authorization-and-encryption)

**Answer:** Authorization intersection: identity, bucket/access point, SCP/boundary/session, endpoint and KMS policies can all constrain. Encryption: SSE-S3/KMS/DSSE/client methods differ in control, audit, quota and recovery. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-S3-MN-08

- [ ] **Question:** Compare Encryption with Replication. When would each change your design?
> **Covered in:** [Amazon S3 — Replication, events and analytics](README.md#replication-events-and-analytics)

**Answer:** Encryption: SSE-S3/KMS/DSSE/client methods differ in control, audit, quota and recovery. Replication: asynchronous SRR/CRR needs versioning, IAM/KMS, existing-object/delete behavior and monitoring. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-S3-MN-09

- [ ] **Question:** Compare Replication with Events. When would each change your design?
> **Covered in:** [Amazon S3 — Replication, events and analytics](README.md#replication-events-and-analytics)

**Answer:** Replication: asynchronous SRR/CRR needs versioning, IAM/KMS, existing-object/delete behavior and monitoring. Events: notifications can duplicate/reorder, so consumers need idempotency and reconciliation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-S3-MN-10

- [ ] **Configuration review:** **Question:** Compare Events with Object/key. When would each change your design?
> **Covered in:** [Amazon S3 — Replication, events and analytics](README.md#replication-events-and-analytics)

**Answer:** Events: notifications can duplicate/reorder, so consumers need idempotency and reconciliation. Object/key: immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-S3-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Object/key; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api head-object --bucket BUCKET --key KEY` plus recent events/changes, then correlate the service-specific SLI. immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-S3-MP-02

- [ ] **Question:** Production is degraded around Strong consistency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon S3 — Data, consistency and lifecycle](README.md#data-consistency-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api list-object-versions --bucket BUCKET --prefix KEY` plus recent events/changes, then correlate the service-specific SLI. successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-S3-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Versioning; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api get-public-access-block --bucket BUCKET` plus recent events/changes, then correlate the service-specific SLI. preserves version IDs/delete markers for recovery and is not sufficient if one principal can purge all versions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-S3-MP-04

- [ ] **Question:** Production is degraded around Storage classes; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api get-bucket-replication --bucket BUCKET` plus recent events/changes, then correlate the service-specific SLI. trade access/retrieval/minimum-duration/AZ resilience and monitoring cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-S3-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Lifecycle; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api head-object --bucket BUCKET --key KEY` plus recent events/changes, then correlate the service-specific SLI. asynchronously transitions/expires current/noncurrent versions and incomplete multipart uploads. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-S3-MP-06

- [ ] **Question:** Production is degraded around Multipart/checksum; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api list-object-versions --bucket BUCKET --prefix KEY` plus recent events/changes, then correlate the service-specific SLI. parallel parts and integrity checks improve large transfer reliability but abandoned uploads cost money. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-S3-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Authorization intersection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api get-public-access-block --bucket BUCKET` plus recent events/changes, then correlate the service-specific SLI. identity, bucket/access point, SCP/boundary/session, endpoint and KMS policies can all constrain. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-S3-MP-08

- [ ] **Question:** Production is degraded around Encryption; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon S3 — Authorization and encryption](README.md#authorization-and-encryption)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api get-bucket-replication --bucket BUCKET` plus recent events/changes, then correlate the service-specific SLI. SSE-S3/KMS/DSSE/client methods differ in control, audit, quota and recovery. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-S3-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Replication; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon S3 — Replication, events and analytics](README.md#replication-events-and-analytics)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api head-object --bucket BUCKET --key KEY` plus recent events/changes, then correlate the service-specific SLI. asynchronous SRR/CRR needs versioning, IAM/KMS, existing-object/delete behavior and monitoring. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-S3-MP-10

- [ ] **Question:** Production is degraded around Events; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon S3 — Replication, events and analytics](README.md#replication-events-and-analytics)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws s3api list-object-versions --bucket BUCKET --prefix KEY` plus recent events/changes, then correlate the service-specific SLI. notifications can duplicate/reorder, so consumers need idempotency and reconciliation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-S3-SN-01

- [ ] **Question:** Design a production Amazon S3 capability where Object/key, Storage classes and Authorization intersection are first-class requirements.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. trade access/retrieval/minimum-duration/AZ resilience and monitoring cost. identity, bucket/access point, SCP/boundary/session, endpoint and KMS policies can all constrain. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-S3-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon S3 capability where Strong consistency, Lifecycle and Encryption are first-class requirements.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. asynchronously transitions/expires current/noncurrent versions and incomplete multipart uploads. SSE-S3/KMS/DSSE/client methods differ in control, audit, quota and recovery. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-S3-SN-03

- [ ] **Question:** Design a production Amazon S3 capability where Versioning, Multipart/checksum and Replication are first-class requirements.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: preserves version IDs/delete markers for recovery and is not sufficient if one principal can purge all versions. parallel parts and integrity checks improve large transfer reliability but abandoned uploads cost money. asynchronous SRR/CRR needs versioning, IAM/KMS, existing-object/delete behavior and monitoring. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-S3-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon S3 capability where Storage classes, Authorization intersection and Events are first-class requirements.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: trade access/retrieval/minimum-duration/AZ resilience and monitoring cost. identity, bucket/access point, SCP/boundary/session, endpoint and KMS policies can all constrain. notifications can duplicate/reorder, so consumers need idempotency and reconciliation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-S3-SN-05

- [ ] **Question:** Design a production Amazon S3 capability where Lifecycle, Encryption and Object/key are first-class requirements.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: asynchronously transitions/expires current/noncurrent versions and incomplete multipart uploads. SSE-S3/KMS/DSSE/client methods differ in control, audit, quota and recovery. immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-S3-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon S3 capability where Multipart/checksum, Replication and Strong consistency are first-class requirements.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: parallel parts and integrity checks improve large transfer reliability but abandoned uploads cost money. asynchronous SRR/CRR needs versioning, IAM/KMS, existing-object/delete behavior and monitoring. successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-S3-SN-07

- [ ] **Question:** Design a production Amazon S3 capability where Authorization intersection, Events and Versioning are first-class requirements.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: identity, bucket/access point, SCP/boundary/session, endpoint and KMS policies can all constrain. notifications can duplicate/reorder, so consumers need idempotency and reconciliation. preserves version IDs/delete markers for recovery and is not sufficient if one principal can purge all versions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-S3-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon S3 capability where Encryption, Object/key and Storage classes are first-class requirements.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: SSE-S3/KMS/DSSE/client methods differ in control, audit, quota and recovery. immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. trade access/retrieval/minimum-duration/AZ resilience and monitoring cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-S3-SN-09

- [ ] **Question:** Design a production Amazon S3 capability where Replication, Strong consistency and Lifecycle are first-class requirements.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: asynchronous SRR/CRR needs versioning, IAM/KMS, existing-object/delete behavior and monitoring. successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. asynchronously transitions/expires current/noncurrent versions and incomplete multipart uploads. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-S3-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon S3 capability where Events, Versioning and Multipart/checksum are first-class requirements.
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: notifications can duplicate/reorder, so consumers need idempotency and reconciliation. preserves version IDs/delete markers for recovery and is not sufficient if one principal can purge all versions. parallel parts and integrity checks improve large transfer reliability but abandoned uploads cost money. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-S3-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Object/key. How do you lead it end to end?
> **Covered in:** [Amazon S3 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api head-object --bucket BUCKET --key KEY` as one read-only checkpoint, not the whole diagnosis. immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-S3-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Strong consistency. How do you lead it end to end?
> **Covered in:** [Amazon S3 — Data, consistency and lifecycle](README.md#data-consistency-and-lifecycle)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api list-object-versions --bucket BUCKET --prefix KEY` as one read-only checkpoint, not the whole diagnosis. successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-S3-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Versioning. How do you lead it end to end?
> **Covered in:** [Amazon S3 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api get-public-access-block --bucket BUCKET` as one read-only checkpoint, not the whole diagnosis. preserves version IDs/delete markers for recovery and is not sufficient if one principal can purge all versions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-S3-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Storage classes. How do you lead it end to end?
> **Covered in:** [Amazon S3 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api get-bucket-replication --bucket BUCKET` as one read-only checkpoint, not the whole diagnosis. trade access/retrieval/minimum-duration/AZ resilience and monitoring cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-S3-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lifecycle. How do you lead it end to end?
> **Covered in:** [Amazon S3 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api head-object --bucket BUCKET --key KEY` as one read-only checkpoint, not the whole diagnosis. asynchronously transitions/expires current/noncurrent versions and incomplete multipart uploads. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-S3-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Multipart/checksum. How do you lead it end to end?
> **Covered in:** [Amazon S3 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api list-object-versions --bucket BUCKET --prefix KEY` as one read-only checkpoint, not the whole diagnosis. parallel parts and integrity checks improve large transfer reliability but abandoned uploads cost money. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-S3-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authorization intersection. How do you lead it end to end?
> **Covered in:** [Amazon S3 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api get-public-access-block --bucket BUCKET` as one read-only checkpoint, not the whole diagnosis. identity, bucket/access point, SCP/boundary/session, endpoint and KMS policies can all constrain. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-S3-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Encryption. How do you lead it end to end?
> **Covered in:** [Amazon S3 — Authorization and encryption](README.md#authorization-and-encryption)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api get-bucket-replication --bucket BUCKET` as one read-only checkpoint, not the whole diagnosis. SSE-S3/KMS/DSSE/client methods differ in control, audit, quota and recovery. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-S3-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Replication. How do you lead it end to end?
> **Covered in:** [Amazon S3 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api head-object --bucket BUCKET --key KEY` as one read-only checkpoint, not the whole diagnosis. asynchronous SRR/CRR needs versioning, IAM/KMS, existing-object/delete behavior and monitoring. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-S3-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Events. How do you lead it end to end?
> **Covered in:** [Amazon S3 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws s3api list-object-versions --bucket BUCKET --prefix KEY` as one read-only checkpoint, not the whole diagnosis. notifications can duplicate/reorder, so consumers need idempotency and reconciliation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Storage](../README.md) · [Study note](README.md) · [Next: Amazon EBS →](../02-ebs/README.md)

<!-- reading-navigation:end -->
