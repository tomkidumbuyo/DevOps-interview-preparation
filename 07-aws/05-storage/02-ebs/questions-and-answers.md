# Amazon EBS — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-EBS-JN-01

- [ ] **Question:** What is gp3, and why does it matter in Amazon EBS?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** general SSD with independently configurable size, IOPS and throughput within limits. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EBS-JN-02

- [ ] **Question:** What is io2, and why does it matter in Amazon EBS?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EBS-JN-03

- [ ] **Question:** What is st1/sc1, and why does it matter in Amazon EBS?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** throughput/cold HDD choices unsuitable for boot/random latency-sensitive workloads. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EBS-JN-04

- [ ] **Question:** What is Instance EBS bandwidth, and why does it matter in Amazon EBS?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** instance attachment limits can bottleneck a provisioned volume. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EBS-JN-05

- [ ] **Question:** What is Queue depth/I/O size, and why does it matter in Amazon EBS?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** workload concurrency and block size determine realized IOPS/throughput/latency. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EBS-JN-06

- [ ] **Question:** What is Snapshot, and why does it matter in Amazon EBS?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** incremental service copy that is crash-consistent unless the application is quiesced/coordinated. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EBS-JN-07

- [ ] **Question:** What is Encryption/KMS, and why does it matter in Amazon EBS?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** volume/snapshot/copy access requires both EC2 and key permissions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EBS-JN-08

- [ ] **Code:** **Question:** What does `lsblk -f && iostat -xz 1` help you verify for Amazon EBS?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: pre-initializes supported snapshots in selected AZs at additional cost.

### AMAZON-EBS-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-volumes --volume-ids VOLUME_ID` help you verify for Amazon EBS?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: grow volume then partition/PV/LV/filesystem without shrinking and with rollback evidence.

### AMAZON-EBS-JN-10

- [ ] **Code:** **Question:** What does `aws ec2 describe-volume-status --volume-ids VOLUME_ID` help you verify for Amazon EBS?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: supported volumes/instances still require a cluster-aware filesystem/application.

## Junior — procedural and command questions

### AMAZON-EBS-JP-01

- [ ] **Code:** **Question:** A basic gp3 check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-volumes --volume-ids VOLUME_ID` and capture exact status/reason/request ID. general SSD with independently configurable size, IOPS and throughput within limits. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EBS-JP-02

- [ ] **Question:** A basic io2 check fails. What would you do first?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-volume-status --volume-ids VOLUME_ID` and capture exact status/reason/request ID. high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EBS-JP-03

- [ ] **Question:** A basic st1/sc1 check fails. What would you do first?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 modify-volume --volume-id VOLUME_ID --size SIZE` and capture exact status/reason/request ID. throughput/cold HDD choices unsuitable for boot/random latency-sensitive workloads. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EBS-JP-04

- [ ] **Code:** **Question:** A basic Instance EBS bandwidth check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lsblk -f && iostat -xz 1` and capture exact status/reason/request ID. instance attachment limits can bottleneck a provisioned volume. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EBS-JP-05

- [ ] **Question:** A basic Queue depth/I/O size check fails. What would you do first?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-volumes --volume-ids VOLUME_ID` and capture exact status/reason/request ID. workload concurrency and block size determine realized IOPS/throughput/latency. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EBS-JP-06

- [ ] **Question:** A basic Snapshot check fails. What would you do first?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-volume-status --volume-ids VOLUME_ID` and capture exact status/reason/request ID. incremental service copy that is crash-consistent unless the application is quiesced/coordinated. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EBS-JP-07

- [ ] **Code:** **Question:** A basic Encryption/KMS check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 modify-volume --volume-id VOLUME_ID --size SIZE` and capture exact status/reason/request ID. volume/snapshot/copy access requires both EC2 and key permissions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EBS-JP-08

- [ ] **Question:** A basic Fast Snapshot Restore check fails. What would you do first?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lsblk -f && iostat -xz 1` and capture exact status/reason/request ID. pre-initializes supported snapshots in selected AZs at additional cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EBS-JP-09

- [ ] **Question:** A basic Expansion check fails. What would you do first?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-volumes --volume-ids VOLUME_ID` and capture exact status/reason/request ID. grow volume then partition/PV/LV/filesystem without shrinking and with rollback evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EBS-JP-10

- [ ] **Code:** **Question:** A basic Multi-Attach check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EBS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-volume-status --volume-ids VOLUME_ID` and capture exact status/reason/request ID. supported volumes/instances still require a cluster-aware filesystem/application. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-EBS-MN-01

- [ ] **Question:** Compare gp3 with io2. When would each change your design?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** gp3: general SSD with independently configurable size, IOPS and throughput within limits. io2: high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EBS-MN-02

- [ ] **Question:** Compare io2 with st1/sc1. When would each change your design?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** io2: high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. st1/sc1: throughput/cold HDD choices unsuitable for boot/random latency-sensitive workloads. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EBS-MN-03

- [ ] **Question:** Compare st1/sc1 with Instance EBS bandwidth. When would each change your design?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** st1/sc1: throughput/cold HDD choices unsuitable for boot/random latency-sensitive workloads. Instance EBS bandwidth: instance attachment limits can bottleneck a provisioned volume. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EBS-MN-04

- [ ] **Configuration review:** **Question:** Compare Instance EBS bandwidth with Queue depth/I/O size. When would each change your design?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Instance EBS bandwidth: instance attachment limits can bottleneck a provisioned volume. Queue depth/I/O size: workload concurrency and block size determine realized IOPS/throughput/latency. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EBS-MN-05

- [ ] **Question:** Compare Queue depth/I/O size with Snapshot. When would each change your design?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Queue depth/I/O size: workload concurrency and block size determine realized IOPS/throughput/latency. Snapshot: incremental service copy that is crash-consistent unless the application is quiesced/coordinated. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EBS-MN-06

- [ ] **Question:** Compare Snapshot with Encryption/KMS. When would each change your design?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Snapshot: incremental service copy that is crash-consistent unless the application is quiesced/coordinated. Encryption/KMS: volume/snapshot/copy access requires both EC2 and key permissions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EBS-MN-07

- [ ] **Configuration review:** **Question:** Compare Encryption/KMS with Fast Snapshot Restore. When would each change your design?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Encryption/KMS: volume/snapshot/copy access requires both EC2 and key permissions. Fast Snapshot Restore: pre-initializes supported snapshots in selected AZs at additional cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EBS-MN-08

- [ ] **Question:** Compare Fast Snapshot Restore with Expansion. When would each change your design?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Fast Snapshot Restore: pre-initializes supported snapshots in selected AZs at additional cost. Expansion: grow volume then partition/PV/LV/filesystem without shrinking and with rollback evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EBS-MN-09

- [ ] **Question:** Compare Expansion with Multi-Attach. When would each change your design?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Expansion: grow volume then partition/PV/LV/filesystem without shrinking and with rollback evidence. Multi-Attach: supported volumes/instances still require a cluster-aware filesystem/application. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EBS-MN-10

- [ ] **Configuration review:** **Question:** Compare Multi-Attach with gp3. When would each change your design?
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Multi-Attach: supported volumes/instances still require a cluster-aware filesystem/application. gp3: general SSD with independently configurable size, IOPS and throughput within limits. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-EBS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around gp3; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-volumes --volume-ids VOLUME_ID` plus recent events/changes, then correlate the service-specific SLI. general SSD with independently configurable size, IOPS and throughput within limits. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EBS-MP-02

- [ ] **Question:** Production is degraded around io2; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-volume-status --volume-ids VOLUME_ID` plus recent events/changes, then correlate the service-specific SLI. high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EBS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around st1/sc1; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 modify-volume --volume-id VOLUME_ID --size SIZE` plus recent events/changes, then correlate the service-specific SLI. throughput/cold HDD choices unsuitable for boot/random latency-sensitive workloads. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EBS-MP-04

- [ ] **Question:** Production is degraded around Instance EBS bandwidth; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lsblk -f && iostat -xz 1` plus recent events/changes, then correlate the service-specific SLI. instance attachment limits can bottleneck a provisioned volume. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EBS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Queue depth/I/O size; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-volumes --volume-ids VOLUME_ID` plus recent events/changes, then correlate the service-specific SLI. workload concurrency and block size determine realized IOPS/throughput/latency. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EBS-MP-06

- [ ] **Question:** Production is degraded around Snapshot; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-volume-status --volume-ids VOLUME_ID` plus recent events/changes, then correlate the service-specific SLI. incremental service copy that is crash-consistent unless the application is quiesced/coordinated. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EBS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Encryption/KMS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 modify-volume --volume-id VOLUME_ID --size SIZE` plus recent events/changes, then correlate the service-specific SLI. volume/snapshot/copy access requires both EC2 and key permissions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EBS-MP-08

- [ ] **Question:** Production is degraded around Fast Snapshot Restore; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lsblk -f && iostat -xz 1` plus recent events/changes, then correlate the service-specific SLI. pre-initializes supported snapshots in selected AZs at additional cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EBS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Expansion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-volumes --volume-ids VOLUME_ID` plus recent events/changes, then correlate the service-specific SLI. grow volume then partition/PV/LV/filesystem without shrinking and with rollback evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EBS-MP-10

- [ ] **Question:** Production is degraded around Multi-Attach; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-volume-status --volume-ids VOLUME_ID` plus recent events/changes, then correlate the service-specific SLI. supported volumes/instances still require a cluster-aware filesystem/application. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-EBS-SN-01

- [ ] **Question:** Design a production Amazon EBS capability where gp3, Instance EBS bandwidth and Encryption/KMS are first-class requirements.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: general SSD with independently configurable size, IOPS and throughput within limits. instance attachment limits can bottleneck a provisioned volume. volume/snapshot/copy access requires both EC2 and key permissions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EBS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EBS capability where io2, Queue depth/I/O size and Fast Snapshot Restore are first-class requirements.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. workload concurrency and block size determine realized IOPS/throughput/latency. pre-initializes supported snapshots in selected AZs at additional cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EBS-SN-03

- [ ] **Question:** Design a production Amazon EBS capability where st1/sc1, Snapshot and Expansion are first-class requirements.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: throughput/cold HDD choices unsuitable for boot/random latency-sensitive workloads. incremental service copy that is crash-consistent unless the application is quiesced/coordinated. grow volume then partition/PV/LV/filesystem without shrinking and with rollback evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EBS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EBS capability where Instance EBS bandwidth, Encryption/KMS and Multi-Attach are first-class requirements.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: instance attachment limits can bottleneck a provisioned volume. volume/snapshot/copy access requires both EC2 and key permissions. supported volumes/instances still require a cluster-aware filesystem/application. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EBS-SN-05

- [ ] **Question:** Design a production Amazon EBS capability where Queue depth/I/O size, Fast Snapshot Restore and gp3 are first-class requirements.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: workload concurrency and block size determine realized IOPS/throughput/latency. pre-initializes supported snapshots in selected AZs at additional cost. general SSD with independently configurable size, IOPS and throughput within limits. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EBS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EBS capability where Snapshot, Expansion and io2 are first-class requirements.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: incremental service copy that is crash-consistent unless the application is quiesced/coordinated. grow volume then partition/PV/LV/filesystem without shrinking and with rollback evidence. high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EBS-SN-07

- [ ] **Question:** Design a production Amazon EBS capability where Encryption/KMS, Multi-Attach and st1/sc1 are first-class requirements.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: volume/snapshot/copy access requires both EC2 and key permissions. supported volumes/instances still require a cluster-aware filesystem/application. throughput/cold HDD choices unsuitable for boot/random latency-sensitive workloads. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EBS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EBS capability where Fast Snapshot Restore, gp3 and Instance EBS bandwidth are first-class requirements.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pre-initializes supported snapshots in selected AZs at additional cost. general SSD with independently configurable size, IOPS and throughput within limits. instance attachment limits can bottleneck a provisioned volume. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EBS-SN-09

- [ ] **Question:** Design a production Amazon EBS capability where Expansion, io2 and Queue depth/I/O size are first-class requirements.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: grow volume then partition/PV/LV/filesystem without shrinking and with rollback evidence. high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. workload concurrency and block size determine realized IOPS/throughput/latency. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EBS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EBS capability where Multi-Attach, st1/sc1 and Snapshot are first-class requirements.
> **Covered in:** [Amazon EBS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supported volumes/instances still require a cluster-aware filesystem/application. throughput/cold HDD choices unsuitable for boot/random latency-sensitive workloads. incremental service copy that is crash-consistent unless the application is quiesced/coordinated. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-EBS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving gp3. How do you lead it end to end?
> **Covered in:** [Amazon EBS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-volumes --volume-ids VOLUME_ID` as one read-only checkpoint, not the whole diagnosis. general SSD with independently configurable size, IOPS and throughput within limits. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EBS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving io2. How do you lead it end to end?
> **Covered in:** [Amazon EBS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-volume-status --volume-ids VOLUME_ID` as one read-only checkpoint, not the whole diagnosis. high-performance/durability SSD for sustained I/O and supported Multi-Attach cases. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EBS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving st1/sc1. How do you lead it end to end?
> **Covered in:** [Amazon EBS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 modify-volume --volume-id VOLUME_ID --size SIZE` as one read-only checkpoint, not the whole diagnosis. throughput/cold HDD choices unsuitable for boot/random latency-sensitive workloads. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EBS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Instance EBS bandwidth. How do you lead it end to end?
> **Covered in:** [Amazon EBS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lsblk -f && iostat -xz 1` as one read-only checkpoint, not the whole diagnosis. instance attachment limits can bottleneck a provisioned volume. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EBS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Queue depth/I/O size. How do you lead it end to end?
> **Covered in:** [Amazon EBS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-volumes --volume-ids VOLUME_ID` as one read-only checkpoint, not the whole diagnosis. workload concurrency and block size determine realized IOPS/throughput/latency. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EBS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Snapshot. How do you lead it end to end?
> **Covered in:** [Amazon EBS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-volume-status --volume-ids VOLUME_ID` as one read-only checkpoint, not the whole diagnosis. incremental service copy that is crash-consistent unless the application is quiesced/coordinated. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EBS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Encryption/KMS. How do you lead it end to end?
> **Covered in:** [Amazon EBS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 modify-volume --volume-id VOLUME_ID --size SIZE` as one read-only checkpoint, not the whole diagnosis. volume/snapshot/copy access requires both EC2 and key permissions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EBS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Fast Snapshot Restore. How do you lead it end to end?
> **Covered in:** [Amazon EBS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lsblk -f && iostat -xz 1` as one read-only checkpoint, not the whole diagnosis. pre-initializes supported snapshots in selected AZs at additional cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EBS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Expansion. How do you lead it end to end?
> **Covered in:** [Amazon EBS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-volumes --volume-ids VOLUME_ID` as one read-only checkpoint, not the whole diagnosis. grow volume then partition/PV/LV/filesystem without shrinking and with rollback evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EBS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Multi-Attach. How do you lead it end to end?
> **Covered in:** [Amazon EBS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-volume-status --volume-ids VOLUME_ID` as one read-only checkpoint, not the whole diagnosis. supported volumes/instances still require a cluster-aware filesystem/application. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon S3](../01-s3/README.md) · [Study note](README.md) · [Next: Amazon EFS →](../03-efs/README.md)

<!-- reading-navigation:end -->
