# Compute — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-COMPUTE-JN-01

- [ ] **Question:** What is Instance family, and why does it matter in Compute?

**Answer:** general, compute, memory, storage and accelerator families target different bottlenecks. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTE-JN-02

- [ ] **Question:** What is CPU architecture, and why does it matter in Compute?

**Answer:** x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTE-JN-03

- [ ] **Question:** What is AMI, and why does it matter in Compute?

**Answer:** boot image metadata and snapshots define instance root and launch compatibility. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTE-JN-04

- [ ] **Question:** What is Golden image, and why does it matter in Compute?

**Answer:** centrally hardened/tested base reduces bootstrap drift and replacement time. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTE-JN-05

- [ ] **Question:** What is Launch template, and why does it matter in Compute?

**Answer:** versions instance image/type/network/role/storage/bootstrap inputs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTE-JN-06

- [ ] **Question:** What is Min/max/desired, and why does it matter in Compute?

**Answer:** bound fleet capacity while policies adjust desired count. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTE-JN-07

- [ ] **Question:** What is Instance family, and why does it matter in Compute?

**Answer:** general, compute, memory, storage and accelerator families target different bottlenecks. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTE-JN-08

- [ ] **Code:** **Question:** What does `aws ec2 describe-images --owners self` help you verify for Compute?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts.

### BRANCH-COMPUTE-JN-09

- [ ] **Code:** **Question:** What does `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` help you verify for Compute?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: boot image metadata and snapshots define instance root and launch compatibility.

### BRANCH-COMPUTE-JN-10

- [ ] **Code:** **Question:** What does `aws ec2 describe-instances --instance-ids INSTANCE_ID` help you verify for Compute?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: centrally hardened/tested base reduces bootstrap drift and replacement time.

## Junior — procedural and command questions

### BRANCH-COMPUTE-JP-01

- [ ] **Code:** **Question:** A basic Instance family check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instances --instance-ids INSTANCE_ID` and capture exact status/reason/request ID. general, compute, memory, storage and accelerator families target different bottlenecks. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTE-JP-02

- [ ] **Question:** A basic CPU architecture check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-images --owners self` and capture exact status/reason/request ID. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTE-JP-03

- [ ] **Question:** A basic AMI check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` and capture exact status/reason/request ID. boot image metadata and snapshots define instance root and launch compatibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTE-JP-04

- [ ] **Code:** **Question:** A basic Golden image check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instances --instance-ids INSTANCE_ID` and capture exact status/reason/request ID. centrally hardened/tested base reduces bootstrap drift and replacement time. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTE-JP-05

- [ ] **Question:** A basic Launch template check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-images --owners self` and capture exact status/reason/request ID. versions instance image/type/network/role/storage/bootstrap inputs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTE-JP-06

- [ ] **Question:** A basic Min/max/desired check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` and capture exact status/reason/request ID. bound fleet capacity while policies adjust desired count. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTE-JP-07

- [ ] **Code:** **Question:** A basic Instance family check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instances --instance-ids INSTANCE_ID` and capture exact status/reason/request ID. general, compute, memory, storage and accelerator families target different bottlenecks. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTE-JP-08

- [ ] **Question:** A basic CPU architecture check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-images --owners self` and capture exact status/reason/request ID. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTE-JP-09

- [ ] **Question:** A basic AMI check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` and capture exact status/reason/request ID. boot image metadata and snapshots define instance root and launch compatibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTE-JP-10

- [ ] **Code:** **Question:** A basic Golden image check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instances --instance-ids INSTANCE_ID` and capture exact status/reason/request ID. centrally hardened/tested base reduces bootstrap drift and replacement time. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-COMPUTE-MN-01

- [ ] **Question:** Compare Instance family with CPU architecture. When would each change your design?

**Answer:** Instance family: general, compute, memory, storage and accelerator families target different bottlenecks. CPU architecture: x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTE-MN-02

- [ ] **Question:** Compare CPU architecture with AMI. When would each change your design?

**Answer:** CPU architecture: x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. AMI: boot image metadata and snapshots define instance root and launch compatibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTE-MN-03

- [ ] **Question:** Compare AMI with Golden image. When would each change your design?

**Answer:** AMI: boot image metadata and snapshots define instance root and launch compatibility. Golden image: centrally hardened/tested base reduces bootstrap drift and replacement time. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTE-MN-04

- [ ] **Configuration review:** **Question:** Compare Golden image with Launch template. When would each change your design?

**Answer:** Golden image: centrally hardened/tested base reduces bootstrap drift and replacement time. Launch template: versions instance image/type/network/role/storage/bootstrap inputs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTE-MN-05

- [ ] **Question:** Compare Launch template with Min/max/desired. When would each change your design?

**Answer:** Launch template: versions instance image/type/network/role/storage/bootstrap inputs. Min/max/desired: bound fleet capacity while policies adjust desired count. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTE-MN-06

- [ ] **Question:** Compare Min/max/desired with Instance family. When would each change your design?

**Answer:** Min/max/desired: bound fleet capacity while policies adjust desired count. Instance family: general, compute, memory, storage and accelerator families target different bottlenecks. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTE-MN-07

- [ ] **Configuration review:** **Question:** Compare Instance family with CPU architecture. When would each change your design?

**Answer:** Instance family: general, compute, memory, storage and accelerator families target different bottlenecks. CPU architecture: x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTE-MN-08

- [ ] **Question:** Compare CPU architecture with AMI. When would each change your design?

**Answer:** CPU architecture: x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. AMI: boot image metadata and snapshots define instance root and launch compatibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTE-MN-09

- [ ] **Question:** Compare AMI with Golden image. When would each change your design?

**Answer:** AMI: boot image metadata and snapshots define instance root and launch compatibility. Golden image: centrally hardened/tested base reduces bootstrap drift and replacement time. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTE-MN-10

- [ ] **Configuration review:** **Question:** Compare Golden image with Instance family. When would each change your design?

**Answer:** Golden image: centrally hardened/tested base reduces bootstrap drift and replacement time. Instance family: general, compute, memory, storage and accelerator families target different bottlenecks. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-COMPUTE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Instance family; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instances --instance-ids INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. general, compute, memory, storage and accelerator families target different bottlenecks. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTE-MP-02

- [ ] **Question:** Production is degraded around CPU architecture; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-images --owners self` plus recent events/changes, then correlate the service-specific SLI. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around AMI; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` plus recent events/changes, then correlate the service-specific SLI. boot image metadata and snapshots define instance root and launch compatibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTE-MP-04

- [ ] **Question:** Production is degraded around Golden image; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instances --instance-ids INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. centrally hardened/tested base reduces bootstrap drift and replacement time. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Launch template; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-images --owners self` plus recent events/changes, then correlate the service-specific SLI. versions instance image/type/network/role/storage/bootstrap inputs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTE-MP-06

- [ ] **Question:** Production is degraded around Min/max/desired; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` plus recent events/changes, then correlate the service-specific SLI. bound fleet capacity while policies adjust desired count. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Instance family; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instances --instance-ids INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. general, compute, memory, storage and accelerator families target different bottlenecks. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTE-MP-08

- [ ] **Question:** Production is degraded around CPU architecture; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-images --owners self` plus recent events/changes, then correlate the service-specific SLI. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around AMI; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` plus recent events/changes, then correlate the service-specific SLI. boot image metadata and snapshots define instance root and launch compatibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTE-MP-10

- [ ] **Question:** Production is degraded around Golden image; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instances --instance-ids INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. centrally hardened/tested base reduces bootstrap drift and replacement time. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-COMPUTE-SN-01

- [ ] **Question:** Design a production Compute capability where Instance family, Golden image and Instance family are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: general, compute, memory, storage and accelerator families target different bottlenecks. centrally hardened/tested base reduces bootstrap drift and replacement time. general, compute, memory, storage and accelerator families target different bottlenecks. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Compute capability where CPU architecture, Launch template and CPU architecture are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. versions instance image/type/network/role/storage/bootstrap inputs. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTE-SN-03

- [ ] **Question:** Design a production Compute capability where AMI, Min/max/desired and AMI are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: boot image metadata and snapshots define instance root and launch compatibility. bound fleet capacity while policies adjust desired count. boot image metadata and snapshots define instance root and launch compatibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Compute capability where Golden image, Instance family and Golden image are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: centrally hardened/tested base reduces bootstrap drift and replacement time. general, compute, memory, storage and accelerator families target different bottlenecks. centrally hardened/tested base reduces bootstrap drift and replacement time. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTE-SN-05

- [ ] **Question:** Design a production Compute capability where Launch template, CPU architecture and Instance family are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versions instance image/type/network/role/storage/bootstrap inputs. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. general, compute, memory, storage and accelerator families target different bottlenecks. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Compute capability where Min/max/desired, AMI and CPU architecture are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bound fleet capacity while policies adjust desired count. boot image metadata and snapshots define instance root and launch compatibility. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTE-SN-07

- [ ] **Question:** Design a production Compute capability where Instance family, Golden image and AMI are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: general, compute, memory, storage and accelerator families target different bottlenecks. centrally hardened/tested base reduces bootstrap drift and replacement time. boot image metadata and snapshots define instance root and launch compatibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Compute capability where CPU architecture, Instance family and Golden image are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. general, compute, memory, storage and accelerator families target different bottlenecks. centrally hardened/tested base reduces bootstrap drift and replacement time. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTE-SN-09

- [ ] **Question:** Design a production Compute capability where AMI, CPU architecture and Launch template are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: boot image metadata and snapshots define instance root and launch compatibility. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. versions instance image/type/network/role/storage/bootstrap inputs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Compute capability where Golden image, AMI and Min/max/desired are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: centrally hardened/tested base reduces bootstrap drift and replacement time. boot image metadata and snapshots define instance root and launch compatibility. bound fleet capacity while policies adjust desired count. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-COMPUTE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Instance family. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instances --instance-ids INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. general, compute, memory, storage and accelerator families target different bottlenecks. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CPU architecture. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-images --owners self` as one read-only checkpoint, not the whole diagnosis. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AMI. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` as one read-only checkpoint, not the whole diagnosis. boot image metadata and snapshots define instance root and launch compatibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Golden image. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instances --instance-ids INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. centrally hardened/tested base reduces bootstrap drift and replacement time. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Launch template. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-images --owners self` as one read-only checkpoint, not the whole diagnosis. versions instance image/type/network/role/storage/bootstrap inputs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Min/max/desired. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` as one read-only checkpoint, not the whole diagnosis. bound fleet capacity while policies adjust desired count. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Instance family. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instances --instance-ids INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. general, compute, memory, storage and accelerator families target different bottlenecks. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CPU architecture. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-images --owners self` as one read-only checkpoint, not the whole diagnosis. x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AMI. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` as one read-only checkpoint, not the whole diagnosis. boot image metadata and snapshots define instance root and launch compatibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Golden image. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instances --instance-ids INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. centrally hardened/tested base reduces bootstrap drift and replacement time. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
