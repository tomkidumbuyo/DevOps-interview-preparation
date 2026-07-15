# EC2 Auto Scaling — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### EC2-AUTO-SCALING-JN-01

- [ ] **Question:** What is Launch template, and why does it matter in EC2 Auto Scaling?

**Answer:** versions instance image/type/network/role/storage/bootstrap inputs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EC2-AUTO-SCALING-JN-02

- [ ] **Question:** What is Min/max/desired, and why does it matter in EC2 Auto Scaling?

**Answer:** bound fleet capacity while policies adjust desired count. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EC2-AUTO-SCALING-JN-03

- [ ] **Question:** What is Target tracking, and why does it matter in EC2 Auto Scaling?

**Answer:** changes desired capacity to keep an aggregate metric near a target. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EC2-AUTO-SCALING-JN-04

- [ ] **Question:** What is Step scaling, and why does it matter in EC2 Auto Scaling?

**Answer:** maps alarm breach magnitude to capacity adjustments. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EC2-AUTO-SCALING-JN-05

- [ ] **Question:** What is Warm-up, and why does it matter in EC2 Auto Scaling?

**Answer:** prevents new instances distorting metrics before they contribute capacity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EC2-AUTO-SCALING-JN-06

- [ ] **Question:** What is Lifecycle hook, and why does it matter in EC2 Auto Scaling?

**Answer:** pauses launch/termination for initialization, registration, drain or checkpoint. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EC2-AUTO-SCALING-JN-07

- [ ] **Question:** What is Instance refresh, and why does it matter in EC2 Auto Scaling?

**Answer:** replaces instances to a selected template with minimum healthy and checkpoints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EC2-AUTO-SCALING-JN-08

- [ ] **Code:** **Question:** What does `aws autoscaling complete-lifecycle-action --lifecycle-hook-name HOOK --auto-scaling-group-name ASG --lifecycle-action-result CONTINUE --instance-id ID` help you verify for EC2 Auto Scaling?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: diversifies compatible types and On-Demand/Spot allocation strategies.

### EC2-AUTO-SCALING-JN-09

- [ ] **Code:** **Question:** What does `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` help you verify for EC2 Auto Scaling?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: launches replacement on Spot rebalance recommendation before interruption.

### EC2-AUTO-SCALING-JN-10

- [ ] **Code:** **Question:** What does `aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG` help you verify for EC2 Auto Scaling?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: wrong health/grace/bootstrap can continually destroy otherwise diagnosable instances.

## Junior — procedural and command questions

### EC2-AUTO-SCALING-JP-01

- [ ] **Code:** **Question:** A basic Launch template check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` and capture exact status/reason/request ID. versions instance image/type/network/role/storage/bootstrap inputs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EC2-AUTO-SCALING-JP-02

- [ ] **Question:** A basic Min/max/desired check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG` and capture exact status/reason/request ID. bound fleet capacity while policies adjust desired count. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EC2-AUTO-SCALING-JP-03

- [ ] **Question:** A basic Target tracking check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling start-instance-refresh --auto-scaling-group-name ASG --preferences file://preferences.json` and capture exact status/reason/request ID. changes desired capacity to keep an aggregate metric near a target. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EC2-AUTO-SCALING-JP-04

- [ ] **Code:** **Question:** A basic Step scaling check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling complete-lifecycle-action --lifecycle-hook-name HOOK --auto-scaling-group-name ASG --lifecycle-action-result CONTINUE --instance-id ID` and capture exact status/reason/request ID. maps alarm breach magnitude to capacity adjustments. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EC2-AUTO-SCALING-JP-05

- [ ] **Question:** A basic Warm-up check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` and capture exact status/reason/request ID. prevents new instances distorting metrics before they contribute capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EC2-AUTO-SCALING-JP-06

- [ ] **Question:** A basic Lifecycle hook check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG` and capture exact status/reason/request ID. pauses launch/termination for initialization, registration, drain or checkpoint. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EC2-AUTO-SCALING-JP-07

- [ ] **Code:** **Question:** A basic Instance refresh check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling start-instance-refresh --auto-scaling-group-name ASG --preferences file://preferences.json` and capture exact status/reason/request ID. replaces instances to a selected template with minimum healthy and checkpoints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EC2-AUTO-SCALING-JP-08

- [ ] **Question:** A basic Mixed instances check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling complete-lifecycle-action --lifecycle-hook-name HOOK --auto-scaling-group-name ASG --lifecycle-action-result CONTINUE --instance-id ID` and capture exact status/reason/request ID. diversifies compatible types and On-Demand/Spot allocation strategies. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EC2-AUTO-SCALING-JP-09

- [ ] **Question:** A basic Capacity rebalance check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` and capture exact status/reason/request ID. launches replacement on Spot rebalance recommendation before interruption. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EC2-AUTO-SCALING-JP-10

- [ ] **Code:** **Question:** A basic Health replacement loop check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG` and capture exact status/reason/request ID. wrong health/grace/bootstrap can continually destroy otherwise diagnosable instances. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### EC2-AUTO-SCALING-MN-01

- [ ] **Question:** Compare Launch template with Min/max/desired. When would each change your design?

**Answer:** Launch template: versions instance image/type/network/role/storage/bootstrap inputs. Min/max/desired: bound fleet capacity while policies adjust desired count. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EC2-AUTO-SCALING-MN-02

- [ ] **Question:** Compare Min/max/desired with Target tracking. When would each change your design?

**Answer:** Min/max/desired: bound fleet capacity while policies adjust desired count. Target tracking: changes desired capacity to keep an aggregate metric near a target. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EC2-AUTO-SCALING-MN-03

- [ ] **Question:** Compare Target tracking with Step scaling. When would each change your design?

**Answer:** Target tracking: changes desired capacity to keep an aggregate metric near a target. Step scaling: maps alarm breach magnitude to capacity adjustments. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EC2-AUTO-SCALING-MN-04

- [ ] **Configuration review:** **Question:** Compare Step scaling with Warm-up. When would each change your design?

**Answer:** Step scaling: maps alarm breach magnitude to capacity adjustments. Warm-up: prevents new instances distorting metrics before they contribute capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EC2-AUTO-SCALING-MN-05

- [ ] **Question:** Compare Warm-up with Lifecycle hook. When would each change your design?

**Answer:** Warm-up: prevents new instances distorting metrics before they contribute capacity. Lifecycle hook: pauses launch/termination for initialization, registration, drain or checkpoint. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EC2-AUTO-SCALING-MN-06

- [ ] **Question:** Compare Lifecycle hook with Instance refresh. When would each change your design?

**Answer:** Lifecycle hook: pauses launch/termination for initialization, registration, drain or checkpoint. Instance refresh: replaces instances to a selected template with minimum healthy and checkpoints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EC2-AUTO-SCALING-MN-07

- [ ] **Configuration review:** **Question:** Compare Instance refresh with Mixed instances. When would each change your design?

**Answer:** Instance refresh: replaces instances to a selected template with minimum healthy and checkpoints. Mixed instances: diversifies compatible types and On-Demand/Spot allocation strategies. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EC2-AUTO-SCALING-MN-08

- [ ] **Question:** Compare Mixed instances with Capacity rebalance. When would each change your design?

**Answer:** Mixed instances: diversifies compatible types and On-Demand/Spot allocation strategies. Capacity rebalance: launches replacement on Spot rebalance recommendation before interruption. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EC2-AUTO-SCALING-MN-09

- [ ] **Question:** Compare Capacity rebalance with Health replacement loop. When would each change your design?

**Answer:** Capacity rebalance: launches replacement on Spot rebalance recommendation before interruption. Health replacement loop: wrong health/grace/bootstrap can continually destroy otherwise diagnosable instances. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EC2-AUTO-SCALING-MN-10

- [ ] **Configuration review:** **Question:** Compare Health replacement loop with Launch template. When would each change your design?

**Answer:** Health replacement loop: wrong health/grace/bootstrap can continually destroy otherwise diagnosable instances. Launch template: versions instance image/type/network/role/storage/bootstrap inputs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### EC2-AUTO-SCALING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Launch template; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` plus recent events/changes, then correlate the service-specific SLI. versions instance image/type/network/role/storage/bootstrap inputs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EC2-AUTO-SCALING-MP-02

- [ ] **Question:** Production is degraded around Min/max/desired; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG` plus recent events/changes, then correlate the service-specific SLI. bound fleet capacity while policies adjust desired count. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EC2-AUTO-SCALING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Target tracking; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling start-instance-refresh --auto-scaling-group-name ASG --preferences file://preferences.json` plus recent events/changes, then correlate the service-specific SLI. changes desired capacity to keep an aggregate metric near a target. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EC2-AUTO-SCALING-MP-04

- [ ] **Question:** Production is degraded around Step scaling; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling complete-lifecycle-action --lifecycle-hook-name HOOK --auto-scaling-group-name ASG --lifecycle-action-result CONTINUE --instance-id ID` plus recent events/changes, then correlate the service-specific SLI. maps alarm breach magnitude to capacity adjustments. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EC2-AUTO-SCALING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Warm-up; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` plus recent events/changes, then correlate the service-specific SLI. prevents new instances distorting metrics before they contribute capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EC2-AUTO-SCALING-MP-06

- [ ] **Question:** Production is degraded around Lifecycle hook; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG` plus recent events/changes, then correlate the service-specific SLI. pauses launch/termination for initialization, registration, drain or checkpoint. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EC2-AUTO-SCALING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Instance refresh; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling start-instance-refresh --auto-scaling-group-name ASG --preferences file://preferences.json` plus recent events/changes, then correlate the service-specific SLI. replaces instances to a selected template with minimum healthy and checkpoints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EC2-AUTO-SCALING-MP-08

- [ ] **Question:** Production is degraded around Mixed instances; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling complete-lifecycle-action --lifecycle-hook-name HOOK --auto-scaling-group-name ASG --lifecycle-action-result CONTINUE --instance-id ID` plus recent events/changes, then correlate the service-specific SLI. diversifies compatible types and On-Demand/Spot allocation strategies. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EC2-AUTO-SCALING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Capacity rebalance; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` plus recent events/changes, then correlate the service-specific SLI. launches replacement on Spot rebalance recommendation before interruption. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EC2-AUTO-SCALING-MP-10

- [ ] **Question:** Production is degraded around Health replacement loop; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG` plus recent events/changes, then correlate the service-specific SLI. wrong health/grace/bootstrap can continually destroy otherwise diagnosable instances. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### EC2-AUTO-SCALING-SN-01

- [ ] **Question:** Design a production EC2 Auto Scaling capability where Launch template, Step scaling and Instance refresh are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versions instance image/type/network/role/storage/bootstrap inputs. maps alarm breach magnitude to capacity adjustments. replaces instances to a selected template with minimum healthy and checkpoints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EC2-AUTO-SCALING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production EC2 Auto Scaling capability where Min/max/desired, Warm-up and Mixed instances are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bound fleet capacity while policies adjust desired count. prevents new instances distorting metrics before they contribute capacity. diversifies compatible types and On-Demand/Spot allocation strategies. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EC2-AUTO-SCALING-SN-03

- [ ] **Question:** Design a production EC2 Auto Scaling capability where Target tracking, Lifecycle hook and Capacity rebalance are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: changes desired capacity to keep an aggregate metric near a target. pauses launch/termination for initialization, registration, drain or checkpoint. launches replacement on Spot rebalance recommendation before interruption. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EC2-AUTO-SCALING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production EC2 Auto Scaling capability where Step scaling, Instance refresh and Health replacement loop are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: maps alarm breach magnitude to capacity adjustments. replaces instances to a selected template with minimum healthy and checkpoints. wrong health/grace/bootstrap can continually destroy otherwise diagnosable instances. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EC2-AUTO-SCALING-SN-05

- [ ] **Question:** Design a production EC2 Auto Scaling capability where Warm-up, Mixed instances and Launch template are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prevents new instances distorting metrics before they contribute capacity. diversifies compatible types and On-Demand/Spot allocation strategies. versions instance image/type/network/role/storage/bootstrap inputs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EC2-AUTO-SCALING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production EC2 Auto Scaling capability where Lifecycle hook, Capacity rebalance and Min/max/desired are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pauses launch/termination for initialization, registration, drain or checkpoint. launches replacement on Spot rebalance recommendation before interruption. bound fleet capacity while policies adjust desired count. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EC2-AUTO-SCALING-SN-07

- [ ] **Question:** Design a production EC2 Auto Scaling capability where Instance refresh, Health replacement loop and Target tracking are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: replaces instances to a selected template with minimum healthy and checkpoints. wrong health/grace/bootstrap can continually destroy otherwise diagnosable instances. changes desired capacity to keep an aggregate metric near a target. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EC2-AUTO-SCALING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production EC2 Auto Scaling capability where Mixed instances, Launch template and Step scaling are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: diversifies compatible types and On-Demand/Spot allocation strategies. versions instance image/type/network/role/storage/bootstrap inputs. maps alarm breach magnitude to capacity adjustments. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EC2-AUTO-SCALING-SN-09

- [ ] **Question:** Design a production EC2 Auto Scaling capability where Capacity rebalance, Min/max/desired and Warm-up are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: launches replacement on Spot rebalance recommendation before interruption. bound fleet capacity while policies adjust desired count. prevents new instances distorting metrics before they contribute capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EC2-AUTO-SCALING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production EC2 Auto Scaling capability where Health replacement loop, Target tracking and Lifecycle hook are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: wrong health/grace/bootstrap can continually destroy otherwise diagnosable instances. changes desired capacity to keep an aggregate metric near a target. pauses launch/termination for initialization, registration, drain or checkpoint. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### EC2-AUTO-SCALING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Launch template. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` as one read-only checkpoint, not the whole diagnosis. versions instance image/type/network/role/storage/bootstrap inputs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EC2-AUTO-SCALING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Min/max/desired. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG` as one read-only checkpoint, not the whole diagnosis. bound fleet capacity while policies adjust desired count. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EC2-AUTO-SCALING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Target tracking. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling start-instance-refresh --auto-scaling-group-name ASG --preferences file://preferences.json` as one read-only checkpoint, not the whole diagnosis. changes desired capacity to keep an aggregate metric near a target. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EC2-AUTO-SCALING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Step scaling. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling complete-lifecycle-action --lifecycle-hook-name HOOK --auto-scaling-group-name ASG --lifecycle-action-result CONTINUE --instance-id ID` as one read-only checkpoint, not the whole diagnosis. maps alarm breach magnitude to capacity adjustments. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EC2-AUTO-SCALING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Warm-up. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` as one read-only checkpoint, not the whole diagnosis. prevents new instances distorting metrics before they contribute capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EC2-AUTO-SCALING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lifecycle hook. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG` as one read-only checkpoint, not the whole diagnosis. pauses launch/termination for initialization, registration, drain or checkpoint. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EC2-AUTO-SCALING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Instance refresh. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling start-instance-refresh --auto-scaling-group-name ASG --preferences file://preferences.json` as one read-only checkpoint, not the whole diagnosis. replaces instances to a selected template with minimum healthy and checkpoints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EC2-AUTO-SCALING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Mixed instances. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling complete-lifecycle-action --lifecycle-hook-name HOOK --auto-scaling-group-name ASG --lifecycle-action-result CONTINUE --instance-id ID` as one read-only checkpoint, not the whole diagnosis. diversifies compatible types and On-Demand/Spot allocation strategies. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EC2-AUTO-SCALING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Capacity rebalance. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG` as one read-only checkpoint, not the whole diagnosis. launches replacement on Spot rebalance recommendation before interruption. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EC2-AUTO-SCALING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Health replacement loop. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG` as one read-only checkpoint, not the whole diagnosis. wrong health/grace/bootstrap can continually destroy otherwise diagnosable instances. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
