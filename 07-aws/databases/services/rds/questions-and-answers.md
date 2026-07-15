# Amazon RDS — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-RDS-JN-01

- [ ] **Question:** What is DB instance, and why does it matter in Amazon RDS?

**Answer:** managed engine compute/storage inside subnet/parameter/security configuration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-RDS-JN-02

- [ ] **Question:** What is Multi-AZ, and why does it matter in Amazon RDS?

**Answer:** synchronous standby/failover for availability rather than read scaling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-RDS-JN-03

- [ ] **Question:** What is Read replica, and why does it matter in Amazon RDS?

**Answer:** asynchronous copy for read scale/DR with lag and promotion implications. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-RDS-JN-04

- [ ] **Question:** What is Automated backups/PITR, and why does it matter in Amazon RDS?

**Answer:** transaction-log retention enables restore to a new instance within window. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-RDS-JN-05

- [ ] **Question:** What is Parameter group, and why does it matter in Amazon RDS?

**Answer:** engine settings can be dynamic or require reboot and need tested rollout. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-RDS-JN-06

- [ ] **Question:** What is RDS Proxy, and why does it matter in Amazon RDS?

**Answer:** pools/multiplexes supported connections and credentials with transaction pinning constraints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-RDS-JN-07

- [ ] **Question:** What is Maintenance window, and why does it matter in Amazon RDS?

**Answer:** provider maintenance/reboot still needs application failover/retry testing. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-RDS-JN-08

- [ ] **Code:** **Question:** What does `aws rds reboot-db-instance --db-instance-identifier DB --force-failover` help you verify for Amazon RDS?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: grows storage under thresholds but cannot shrink or fix I/O design.

### AMAZON-RDS-JN-09

- [ ] **Code:** **Question:** What does `aws rds describe-db-instances --db-instance-identifier DB` help you verify for Amazon RDS?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: pool size, Lambda scaling and long transactions can overload before CPU.

### AMAZON-RDS-JN-10

- [ ] **Code:** **Question:** What does `aws rds describe-events --source-identifier DB --source-type db-instance` help you verify for Amazon RDS?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: OS/database wait evidence complements CloudWatch.

## Junior — procedural and command questions

### AMAZON-RDS-JP-01

- [ ] **Code:** **Question:** A basic DB instance check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-instances --db-instance-identifier DB` and capture exact status/reason/request ID. managed engine compute/storage inside subnet/parameter/security configuration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-RDS-JP-02

- [ ] **Question:** A basic Multi-AZ check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-events --source-identifier DB --source-type db-instance` and capture exact status/reason/request ID. synchronous standby/failover for availability rather than read scaling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-RDS-JP-03

- [ ] **Question:** A basic Read replica check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-snapshots --db-instance-identifier DB` and capture exact status/reason/request ID. asynchronous copy for read scale/DR with lag and promotion implications. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-RDS-JP-04

- [ ] **Code:** **Question:** A basic Automated backups/PITR check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds reboot-db-instance --db-instance-identifier DB --force-failover` and capture exact status/reason/request ID. transaction-log retention enables restore to a new instance within window. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-RDS-JP-05

- [ ] **Question:** A basic Parameter group check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-instances --db-instance-identifier DB` and capture exact status/reason/request ID. engine settings can be dynamic or require reboot and need tested rollout. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-RDS-JP-06

- [ ] **Question:** A basic RDS Proxy check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-events --source-identifier DB --source-type db-instance` and capture exact status/reason/request ID. pools/multiplexes supported connections and credentials with transaction pinning constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-RDS-JP-07

- [ ] **Code:** **Question:** A basic Maintenance window check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-snapshots --db-instance-identifier DB` and capture exact status/reason/request ID. provider maintenance/reboot still needs application failover/retry testing. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-RDS-JP-08

- [ ] **Question:** A basic Storage autoscaling check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds reboot-db-instance --db-instance-identifier DB --force-failover` and capture exact status/reason/request ID. grows storage under thresholds but cannot shrink or fix I/O design. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-RDS-JP-09

- [ ] **Question:** A basic Connection exhaustion check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-instances --db-instance-identifier DB` and capture exact status/reason/request ID. pool size, Lambda scaling and long transactions can overload before CPU. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-RDS-JP-10

- [ ] **Code:** **Question:** A basic Enhanced Monitoring/Performance Insights check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-events --source-identifier DB --source-type db-instance` and capture exact status/reason/request ID. OS/database wait evidence complements CloudWatch. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-RDS-MN-01

- [ ] **Question:** Compare DB instance with Multi-AZ. When would each change your design?

**Answer:** DB instance: managed engine compute/storage inside subnet/parameter/security configuration. Multi-AZ: synchronous standby/failover for availability rather than read scaling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-RDS-MN-02

- [ ] **Question:** Compare Multi-AZ with Read replica. When would each change your design?

**Answer:** Multi-AZ: synchronous standby/failover for availability rather than read scaling. Read replica: asynchronous copy for read scale/DR with lag and promotion implications. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-RDS-MN-03

- [ ] **Question:** Compare Read replica with Automated backups/PITR. When would each change your design?

**Answer:** Read replica: asynchronous copy for read scale/DR with lag and promotion implications. Automated backups/PITR: transaction-log retention enables restore to a new instance within window. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-RDS-MN-04

- [ ] **Configuration review:** **Question:** Compare Automated backups/PITR with Parameter group. When would each change your design?

**Answer:** Automated backups/PITR: transaction-log retention enables restore to a new instance within window. Parameter group: engine settings can be dynamic or require reboot and need tested rollout. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-RDS-MN-05

- [ ] **Question:** Compare Parameter group with RDS Proxy. When would each change your design?

**Answer:** Parameter group: engine settings can be dynamic or require reboot and need tested rollout. RDS Proxy: pools/multiplexes supported connections and credentials with transaction pinning constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-RDS-MN-06

- [ ] **Question:** Compare RDS Proxy with Maintenance window. When would each change your design?

**Answer:** RDS Proxy: pools/multiplexes supported connections and credentials with transaction pinning constraints. Maintenance window: provider maintenance/reboot still needs application failover/retry testing. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-RDS-MN-07

- [ ] **Configuration review:** **Question:** Compare Maintenance window with Storage autoscaling. When would each change your design?

**Answer:** Maintenance window: provider maintenance/reboot still needs application failover/retry testing. Storage autoscaling: grows storage under thresholds but cannot shrink or fix I/O design. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-RDS-MN-08

- [ ] **Question:** Compare Storage autoscaling with Connection exhaustion. When would each change your design?

**Answer:** Storage autoscaling: grows storage under thresholds but cannot shrink or fix I/O design. Connection exhaustion: pool size, Lambda scaling and long transactions can overload before CPU. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-RDS-MN-09

- [ ] **Question:** Compare Connection exhaustion with Enhanced Monitoring/Performance Insights. When would each change your design?

**Answer:** Connection exhaustion: pool size, Lambda scaling and long transactions can overload before CPU. Enhanced Monitoring/Performance Insights: OS/database wait evidence complements CloudWatch. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-RDS-MN-10

- [ ] **Configuration review:** **Question:** Compare Enhanced Monitoring/Performance Insights with DB instance. When would each change your design?

**Answer:** Enhanced Monitoring/Performance Insights: OS/database wait evidence complements CloudWatch. DB instance: managed engine compute/storage inside subnet/parameter/security configuration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-RDS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around DB instance; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-instances --db-instance-identifier DB` plus recent events/changes, then correlate the service-specific SLI. managed engine compute/storage inside subnet/parameter/security configuration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-RDS-MP-02

- [ ] **Question:** Production is degraded around Multi-AZ; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-events --source-identifier DB --source-type db-instance` plus recent events/changes, then correlate the service-specific SLI. synchronous standby/failover for availability rather than read scaling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-RDS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Read replica; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-snapshots --db-instance-identifier DB` plus recent events/changes, then correlate the service-specific SLI. asynchronous copy for read scale/DR with lag and promotion implications. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-RDS-MP-04

- [ ] **Question:** Production is degraded around Automated backups/PITR; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds reboot-db-instance --db-instance-identifier DB --force-failover` plus recent events/changes, then correlate the service-specific SLI. transaction-log retention enables restore to a new instance within window. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-RDS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Parameter group; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-instances --db-instance-identifier DB` plus recent events/changes, then correlate the service-specific SLI. engine settings can be dynamic or require reboot and need tested rollout. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-RDS-MP-06

- [ ] **Question:** Production is degraded around RDS Proxy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-events --source-identifier DB --source-type db-instance` plus recent events/changes, then correlate the service-specific SLI. pools/multiplexes supported connections and credentials with transaction pinning constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-RDS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Maintenance window; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-snapshots --db-instance-identifier DB` plus recent events/changes, then correlate the service-specific SLI. provider maintenance/reboot still needs application failover/retry testing. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-RDS-MP-08

- [ ] **Question:** Production is degraded around Storage autoscaling; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds reboot-db-instance --db-instance-identifier DB --force-failover` plus recent events/changes, then correlate the service-specific SLI. grows storage under thresholds but cannot shrink or fix I/O design. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-RDS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Connection exhaustion; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-instances --db-instance-identifier DB` plus recent events/changes, then correlate the service-specific SLI. pool size, Lambda scaling and long transactions can overload before CPU. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-RDS-MP-10

- [ ] **Question:** Production is degraded around Enhanced Monitoring/Performance Insights; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-events --source-identifier DB --source-type db-instance` plus recent events/changes, then correlate the service-specific SLI. OS/database wait evidence complements CloudWatch. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-RDS-SN-01

- [ ] **Question:** Design a production Amazon RDS capability where DB instance, Automated backups/PITR and Maintenance window are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed engine compute/storage inside subnet/parameter/security configuration. transaction-log retention enables restore to a new instance within window. provider maintenance/reboot still needs application failover/retry testing. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-RDS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon RDS capability where Multi-AZ, Parameter group and Storage autoscaling are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: synchronous standby/failover for availability rather than read scaling. engine settings can be dynamic or require reboot and need tested rollout. grows storage under thresholds but cannot shrink or fix I/O design. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-RDS-SN-03

- [ ] **Question:** Design a production Amazon RDS capability where Read replica, RDS Proxy and Connection exhaustion are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: asynchronous copy for read scale/DR with lag and promotion implications. pools/multiplexes supported connections and credentials with transaction pinning constraints. pool size, Lambda scaling and long transactions can overload before CPU. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-RDS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon RDS capability where Automated backups/PITR, Maintenance window and Enhanced Monitoring/Performance Insights are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: transaction-log retention enables restore to a new instance within window. provider maintenance/reboot still needs application failover/retry testing. OS/database wait evidence complements CloudWatch. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-RDS-SN-05

- [ ] **Question:** Design a production Amazon RDS capability where Parameter group, Storage autoscaling and DB instance are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: engine settings can be dynamic or require reboot and need tested rollout. grows storage under thresholds but cannot shrink or fix I/O design. managed engine compute/storage inside subnet/parameter/security configuration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-RDS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon RDS capability where RDS Proxy, Connection exhaustion and Multi-AZ are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pools/multiplexes supported connections and credentials with transaction pinning constraints. pool size, Lambda scaling and long transactions can overload before CPU. synchronous standby/failover for availability rather than read scaling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-RDS-SN-07

- [ ] **Question:** Design a production Amazon RDS capability where Maintenance window, Enhanced Monitoring/Performance Insights and Read replica are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: provider maintenance/reboot still needs application failover/retry testing. OS/database wait evidence complements CloudWatch. asynchronous copy for read scale/DR with lag and promotion implications. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-RDS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon RDS capability where Storage autoscaling, DB instance and Automated backups/PITR are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: grows storage under thresholds but cannot shrink or fix I/O design. managed engine compute/storage inside subnet/parameter/security configuration. transaction-log retention enables restore to a new instance within window. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-RDS-SN-09

- [ ] **Question:** Design a production Amazon RDS capability where Connection exhaustion, Multi-AZ and Parameter group are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pool size, Lambda scaling and long transactions can overload before CPU. synchronous standby/failover for availability rather than read scaling. engine settings can be dynamic or require reboot and need tested rollout. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-RDS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon RDS capability where Enhanced Monitoring/Performance Insights, Read replica and RDS Proxy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: OS/database wait evidence complements CloudWatch. asynchronous copy for read scale/DR with lag and promotion implications. pools/multiplexes supported connections and credentials with transaction pinning constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-RDS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DB instance. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-instances --db-instance-identifier DB` as one read-only checkpoint, not the whole diagnosis. managed engine compute/storage inside subnet/parameter/security configuration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-RDS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Multi-AZ. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-events --source-identifier DB --source-type db-instance` as one read-only checkpoint, not the whole diagnosis. synchronous standby/failover for availability rather than read scaling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-RDS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Read replica. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-snapshots --db-instance-identifier DB` as one read-only checkpoint, not the whole diagnosis. asynchronous copy for read scale/DR with lag and promotion implications. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-RDS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Automated backups/PITR. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds reboot-db-instance --db-instance-identifier DB --force-failover` as one read-only checkpoint, not the whole diagnosis. transaction-log retention enables restore to a new instance within window. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-RDS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Parameter group. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-instances --db-instance-identifier DB` as one read-only checkpoint, not the whole diagnosis. engine settings can be dynamic or require reboot and need tested rollout. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-RDS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RDS Proxy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-events --source-identifier DB --source-type db-instance` as one read-only checkpoint, not the whole diagnosis. pools/multiplexes supported connections and credentials with transaction pinning constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-RDS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Maintenance window. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-snapshots --db-instance-identifier DB` as one read-only checkpoint, not the whole diagnosis. provider maintenance/reboot still needs application failover/retry testing. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-RDS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Storage autoscaling. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds reboot-db-instance --db-instance-identifier DB --force-failover` as one read-only checkpoint, not the whole diagnosis. grows storage under thresholds but cannot shrink or fix I/O design. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-RDS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Connection exhaustion. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-instances --db-instance-identifier DB` as one read-only checkpoint, not the whole diagnosis. pool size, Lambda scaling and long transactions can overload before CPU. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-RDS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Enhanced Monitoring/Performance Insights. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-events --source-identifier DB --source-type db-instance` as one read-only checkpoint, not the whole diagnosis. OS/database wait evidence complements CloudWatch. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
