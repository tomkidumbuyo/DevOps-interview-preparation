# Amazon EC2 — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-EC2-JN-01

- [ ] **Question:** What is Instance family, and why does it matter in Amazon EC2?

**Answer:** general, compute, memory, storage and accelerator families target different bottlenecks. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EC2-JN-02

- [ ] **Question:** What is CPU architecture, and why does it matter in Amazon EC2?

**Answer:** x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EC2-JN-03

- [ ] **Question:** What is Nitro system, and why does it matter in Amazon EC2?

**Answer:** underpins modern isolation, ENA/EBS and hardware-offload capabilities. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EC2-JN-04

- [ ] **Question:** What is Instance lifecycle, and why does it matter in Amazon EC2?

**Answer:** pending/running/stopping/stopped/hibernated/terminated transitions affect billing and storage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EC2-JN-05

- [ ] **Question:** What is Status checks, and why does it matter in Amazon EC2?

**Answer:** system and instance checks distinguish AWS host from guest reachability signals. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EC2-JN-06

- [ ] **Question:** What is Instance profile, and why does it matter in Amazon EC2?

**Answer:** delivers temporary role credentials to the instance rather than static keys. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EC2-JN-07

- [ ] **Question:** What is IMDSv2, and why does it matter in Amazon EC2?

**Answer:** session-oriented metadata access reduces SSRF credential exposure when enforced/configured correctly. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EC2-JN-08

- [ ] **Code:** **Question:** What does `aws ssm start-session --target INSTANCE_ID` help you verify for Amazon EC2?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: enhanced networking and EFA support high throughput/low latency under compatible instances/workloads.

### AMAZON-EC2-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-instances --instance-ids INSTANCE_ID` help you verify for Amazon EC2?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: cluster/partition/spread strategies trade locality, scale and correlated failure.

### AMAZON-EC2-JN-10

- [ ] **Code:** **Question:** What does `aws ec2 describe-instance-status --include-all-instances` help you verify for Amazon EC2?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: On-Demand, Spot, commitments, dedicated tenancy and reservations solve different price/capacity needs.

## Junior — procedural and command questions

### AMAZON-EC2-JP-01

- [ ] **Code:** **Question:** A basic Instance family check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instances --instance-ids INSTANCE_ID` and capture exact status/reason/request ID. general, compute, memory, storage and accelerator families target different bottlenecks. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EC2-JP-02

- [ ] **Question:** A basic CPU architecture check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-status --include-all-instances` and capture exact status/reason/request ID. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EC2-JP-03

- [ ] **Question:** A basic Nitro system check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-types --instance-types TYPE` and capture exact status/reason/request ID. underpins modern isolation, ENA/EBS and hardware-offload capabilities. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EC2-JP-04

- [ ] **Code:** **Question:** A basic Instance lifecycle check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm start-session --target INSTANCE_ID` and capture exact status/reason/request ID. pending/running/stopping/stopped/hibernated/terminated transitions affect billing and storage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EC2-JP-05

- [ ] **Question:** A basic Status checks check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instances --instance-ids INSTANCE_ID` and capture exact status/reason/request ID. system and instance checks distinguish AWS host from guest reachability signals. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EC2-JP-06

- [ ] **Question:** A basic Instance profile check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-status --include-all-instances` and capture exact status/reason/request ID. delivers temporary role credentials to the instance rather than static keys. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EC2-JP-07

- [ ] **Code:** **Question:** A basic IMDSv2 check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-types --instance-types TYPE` and capture exact status/reason/request ID. session-oriented metadata access reduces SSRF credential exposure when enforced/configured correctly. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EC2-JP-08

- [ ] **Question:** A basic ENA/EFA check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm start-session --target INSTANCE_ID` and capture exact status/reason/request ID. enhanced networking and EFA support high throughput/low latency under compatible instances/workloads. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EC2-JP-09

- [ ] **Question:** A basic Placement groups check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instances --instance-ids INSTANCE_ID` and capture exact status/reason/request ID. cluster/partition/spread strategies trade locality, scale and correlated failure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EC2-JP-10

- [ ] **Code:** **Question:** A basic Purchase/capacity check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-status --include-all-instances` and capture exact status/reason/request ID. On-Demand, Spot, commitments, dedicated tenancy and reservations solve different price/capacity needs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-EC2-MN-01

- [ ] **Question:** Compare Instance family with CPU architecture. When would each change your design?

**Answer:** Instance family: general, compute, memory, storage and accelerator families target different bottlenecks. CPU architecture: x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EC2-MN-02

- [ ] **Question:** Compare CPU architecture with Nitro system. When would each change your design?

**Answer:** CPU architecture: x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Nitro system: underpins modern isolation, ENA/EBS and hardware-offload capabilities. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EC2-MN-03

- [ ] **Question:** Compare Nitro system with Instance lifecycle. When would each change your design?

**Answer:** Nitro system: underpins modern isolation, ENA/EBS and hardware-offload capabilities. Instance lifecycle: pending/running/stopping/stopped/hibernated/terminated transitions affect billing and storage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EC2-MN-04

- [ ] **Configuration review:** **Question:** Compare Instance lifecycle with Status checks. When would each change your design?

**Answer:** Instance lifecycle: pending/running/stopping/stopped/hibernated/terminated transitions affect billing and storage. Status checks: system and instance checks distinguish AWS host from guest reachability signals. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EC2-MN-05

- [ ] **Question:** Compare Status checks with Instance profile. When would each change your design?

**Answer:** Status checks: system and instance checks distinguish AWS host from guest reachability signals. Instance profile: delivers temporary role credentials to the instance rather than static keys. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EC2-MN-06

- [ ] **Question:** Compare Instance profile with IMDSv2. When would each change your design?

**Answer:** Instance profile: delivers temporary role credentials to the instance rather than static keys. IMDSv2: session-oriented metadata access reduces SSRF credential exposure when enforced/configured correctly. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EC2-MN-07

- [ ] **Configuration review:** **Question:** Compare IMDSv2 with ENA/EFA. When would each change your design?

**Answer:** IMDSv2: session-oriented metadata access reduces SSRF credential exposure when enforced/configured correctly. ENA/EFA: enhanced networking and EFA support high throughput/low latency under compatible instances/workloads. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EC2-MN-08

- [ ] **Question:** Compare ENA/EFA with Placement groups. When would each change your design?

**Answer:** ENA/EFA: enhanced networking and EFA support high throughput/low latency under compatible instances/workloads. Placement groups: cluster/partition/spread strategies trade locality, scale and correlated failure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EC2-MN-09

- [ ] **Question:** Compare Placement groups with Purchase/capacity. When would each change your design?

**Answer:** Placement groups: cluster/partition/spread strategies trade locality, scale and correlated failure. Purchase/capacity: On-Demand, Spot, commitments, dedicated tenancy and reservations solve different price/capacity needs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EC2-MN-10

- [ ] **Configuration review:** **Question:** Compare Purchase/capacity with Instance family. When would each change your design?

**Answer:** Purchase/capacity: On-Demand, Spot, commitments, dedicated tenancy and reservations solve different price/capacity needs. Instance family: general, compute, memory, storage and accelerator families target different bottlenecks. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-EC2-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Instance family; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instances --instance-ids INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. general, compute, memory, storage and accelerator families target different bottlenecks. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EC2-MP-02

- [ ] **Question:** Production is degraded around CPU architecture; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-status --include-all-instances` plus recent events/changes, then correlate the service-specific SLI. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EC2-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Nitro system; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-types --instance-types TYPE` plus recent events/changes, then correlate the service-specific SLI. underpins modern isolation, ENA/EBS and hardware-offload capabilities. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EC2-MP-04

- [ ] **Question:** Production is degraded around Instance lifecycle; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm start-session --target INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. pending/running/stopping/stopped/hibernated/terminated transitions affect billing and storage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EC2-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Status checks; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instances --instance-ids INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. system and instance checks distinguish AWS host from guest reachability signals. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EC2-MP-06

- [ ] **Question:** Production is degraded around Instance profile; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-status --include-all-instances` plus recent events/changes, then correlate the service-specific SLI. delivers temporary role credentials to the instance rather than static keys. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EC2-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around IMDSv2; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-types --instance-types TYPE` plus recent events/changes, then correlate the service-specific SLI. session-oriented metadata access reduces SSRF credential exposure when enforced/configured correctly. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EC2-MP-08

- [ ] **Question:** Production is degraded around ENA/EFA; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm start-session --target INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. enhanced networking and EFA support high throughput/low latency under compatible instances/workloads. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EC2-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Placement groups; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instances --instance-ids INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. cluster/partition/spread strategies trade locality, scale and correlated failure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EC2-MP-10

- [ ] **Question:** Production is degraded around Purchase/capacity; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-status --include-all-instances` plus recent events/changes, then correlate the service-specific SLI. On-Demand, Spot, commitments, dedicated tenancy and reservations solve different price/capacity needs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-EC2-SN-01

- [ ] **Question:** Design a production Amazon EC2 capability where Instance family, Instance lifecycle and IMDSv2 are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: general, compute, memory, storage and accelerator families target different bottlenecks. pending/running/stopping/stopped/hibernated/terminated transitions affect billing and storage. session-oriented metadata access reduces SSRF credential exposure when enforced/configured correctly. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EC2-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EC2 capability where CPU architecture, Status checks and ENA/EFA are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. system and instance checks distinguish AWS host from guest reachability signals. enhanced networking and EFA support high throughput/low latency under compatible instances/workloads. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EC2-SN-03

- [ ] **Question:** Design a production Amazon EC2 capability where Nitro system, Instance profile and Placement groups are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: underpins modern isolation, ENA/EBS and hardware-offload capabilities. delivers temporary role credentials to the instance rather than static keys. cluster/partition/spread strategies trade locality, scale and correlated failure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EC2-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EC2 capability where Instance lifecycle, IMDSv2 and Purchase/capacity are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pending/running/stopping/stopped/hibernated/terminated transitions affect billing and storage. session-oriented metadata access reduces SSRF credential exposure when enforced/configured correctly. On-Demand, Spot, commitments, dedicated tenancy and reservations solve different price/capacity needs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EC2-SN-05

- [ ] **Question:** Design a production Amazon EC2 capability where Status checks, ENA/EFA and Instance family are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: system and instance checks distinguish AWS host from guest reachability signals. enhanced networking and EFA support high throughput/low latency under compatible instances/workloads. general, compute, memory, storage and accelerator families target different bottlenecks. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EC2-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EC2 capability where Instance profile, Placement groups and CPU architecture are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: delivers temporary role credentials to the instance rather than static keys. cluster/partition/spread strategies trade locality, scale and correlated failure. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EC2-SN-07

- [ ] **Question:** Design a production Amazon EC2 capability where IMDSv2, Purchase/capacity and Nitro system are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: session-oriented metadata access reduces SSRF credential exposure when enforced/configured correctly. On-Demand, Spot, commitments, dedicated tenancy and reservations solve different price/capacity needs. underpins modern isolation, ENA/EBS and hardware-offload capabilities. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EC2-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EC2 capability where ENA/EFA, Instance family and Instance lifecycle are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: enhanced networking and EFA support high throughput/low latency under compatible instances/workloads. general, compute, memory, storage and accelerator families target different bottlenecks. pending/running/stopping/stopped/hibernated/terminated transitions affect billing and storage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EC2-SN-09

- [ ] **Question:** Design a production Amazon EC2 capability where Placement groups, CPU architecture and Status checks are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cluster/partition/spread strategies trade locality, scale and correlated failure. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. system and instance checks distinguish AWS host from guest reachability signals. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EC2-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EC2 capability where Purchase/capacity, Nitro system and Instance profile are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: On-Demand, Spot, commitments, dedicated tenancy and reservations solve different price/capacity needs. underpins modern isolation, ENA/EBS and hardware-offload capabilities. delivers temporary role credentials to the instance rather than static keys. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-EC2-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Instance family. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instances --instance-ids INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. general, compute, memory, storage and accelerator families target different bottlenecks. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EC2-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CPU architecture. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-status --include-all-instances` as one read-only checkpoint, not the whole diagnosis. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EC2-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Nitro system. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-types --instance-types TYPE` as one read-only checkpoint, not the whole diagnosis. underpins modern isolation, ENA/EBS and hardware-offload capabilities. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EC2-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Instance lifecycle. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm start-session --target INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. pending/running/stopping/stopped/hibernated/terminated transitions affect billing and storage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EC2-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Status checks. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instances --instance-ids INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. system and instance checks distinguish AWS host from guest reachability signals. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EC2-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Instance profile. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-status --include-all-instances` as one read-only checkpoint, not the whole diagnosis. delivers temporary role credentials to the instance rather than static keys. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EC2-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IMDSv2. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-types --instance-types TYPE` as one read-only checkpoint, not the whole diagnosis. session-oriented metadata access reduces SSRF credential exposure when enforced/configured correctly. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EC2-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ENA/EFA. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm start-session --target INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. enhanced networking and EFA support high throughput/low latency under compatible instances/workloads. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EC2-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Placement groups. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instances --instance-ids INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. cluster/partition/spread strategies trade locality, scale and correlated failure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EC2-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Purchase/capacity. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-status --include-all-instances` as one read-only checkpoint, not the whole diagnosis. On-Demand, Spot, commitments, dedicated tenancy and reservations solve different price/capacity needs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
