# AWS Global Accelerator — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-GLOBAL-ACCELERATOR-JN-01

- [ ] **Question:** What is Anycast IP, and why does it matter in AWS Global Accelerator?
> **Covered in:** [AWS Global Accelerator — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** the same static addresses advertise globally and enter a nearby AWS edge. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GLOBAL-ACCELERATOR-JN-02

- [ ] **Question:** What is Accelerator listener, and why does it matter in AWS Global Accelerator?
> **Covered in:** [AWS Global Accelerator — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** accepts TCP/UDP port ranges and distributes to endpoint groups. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GLOBAL-ACCELERATOR-JN-03

- [ ] **Question:** What is Endpoint group, and why does it matter in AWS Global Accelerator?
> **Covered in:** [AWS Global Accelerator — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** regional endpoints, traffic dial and health/check settings. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GLOBAL-ACCELERATOR-JN-04

- [ ] **Question:** What is Endpoint weight, and why does it matter in AWS Global Accelerator?
> **Covered in:** [AWS Global Accelerator — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** shifts traffic among endpoints within a group under health/capacity policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GLOBAL-ACCELERATOR-JN-05

- [ ] **Question:** What is Health failover, and why does it matter in AWS Global Accelerator?
> **Covered in:** [AWS Global Accelerator — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** unhealthy endpoints/regions are removed under detection thresholds and state implications. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GLOBAL-ACCELERATOR-JN-06

- [ ] **Question:** What is Client IP preservation, and why does it matter in AWS Global Accelerator?
> **Covered in:** [AWS Global Accelerator — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** supported endpoint patterns retain source information under constraints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GLOBAL-ACCELERATOR-JN-07

- [ ] **Question:** What is Traffic dial, and why does it matter in AWS Global Accelerator?
> **Covered in:** [AWS Global Accelerator — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** controls percentage sent to a Region for canary/maintenance/capacity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GLOBAL-ACCELERATOR-JN-08

- [ ] **Code:** **Question:** What does `aws globalaccelerator describe-endpoint-group --endpoint-group-arn ARN --region us-west-2` help you verify for AWS Global Accelerator?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: supported endpoint types provide different L7/L4 and address properties.

### AWS-GLOBAL-ACCELERATOR-JN-09

- [ ] **Code:** **Question:** What does `aws globalaccelerator list-accelerators --region us-west-2` help you verify for AWS Global Accelerator?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: Global Accelerator reacts at network routing without waiting for client DNS TTL.

### AWS-GLOBAL-ACCELERATOR-JN-10

- [ ] **Code:** **Question:** What does `aws globalaccelerator list-listeners --accelerator-arn ARN --region us-west-2` help you verify for AWS Global Accelerator?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: global routing must not send data to a disallowed Region or unprepared replica.

## Junior — procedural and command questions

### AWS-GLOBAL-ACCELERATOR-JP-01

- [ ] **Code:** **Question:** A basic Anycast IP check fails. What would you do first using the CLI?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator list-accelerators --region us-west-2` and capture exact status/reason/request ID. the same static addresses advertise globally and enter a nearby AWS edge. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GLOBAL-ACCELERATOR-JP-02

- [ ] **Question:** A basic Accelerator listener check fails. What would you do first?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator list-listeners --accelerator-arn ARN --region us-west-2` and capture exact status/reason/request ID. accepts TCP/UDP port ranges and distributes to endpoint groups. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GLOBAL-ACCELERATOR-JP-03

- [ ] **Question:** A basic Endpoint group check fails. What would you do first?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator list-endpoint-groups --listener-arn ARN --region us-west-2` and capture exact status/reason/request ID. regional endpoints, traffic dial and health/check settings. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GLOBAL-ACCELERATOR-JP-04

- [ ] **Code:** **Question:** A basic Endpoint weight check fails. What would you do first using the CLI?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator describe-endpoint-group --endpoint-group-arn ARN --region us-west-2` and capture exact status/reason/request ID. shifts traffic among endpoints within a group under health/capacity policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GLOBAL-ACCELERATOR-JP-05

- [ ] **Question:** A basic Health failover check fails. What would you do first?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator list-accelerators --region us-west-2` and capture exact status/reason/request ID. unhealthy endpoints/regions are removed under detection thresholds and state implications. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GLOBAL-ACCELERATOR-JP-06

- [ ] **Question:** A basic Client IP preservation check fails. What would you do first?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator list-listeners --accelerator-arn ARN --region us-west-2` and capture exact status/reason/request ID. supported endpoint patterns retain source information under constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GLOBAL-ACCELERATOR-JP-07

- [ ] **Code:** **Question:** A basic Traffic dial check fails. What would you do first using the CLI?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator list-endpoint-groups --listener-arn ARN --region us-west-2` and capture exact status/reason/request ID. controls percentage sent to a Region for canary/maintenance/capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GLOBAL-ACCELERATOR-JP-08

- [ ] **Question:** A basic ALB/NLB/EC2/EIP endpoints check fails. What would you do first?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator describe-endpoint-group --endpoint-group-arn ARN --region us-west-2` and capture exact status/reason/request ID. supported endpoint types provide different L7/L4 and address properties. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GLOBAL-ACCELERATOR-JP-09

- [ ] **Question:** A basic DNS vs anycast check fails. What would you do first?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator list-accelerators --region us-west-2` and capture exact status/reason/request ID. Global Accelerator reacts at network routing without waiting for client DNS TTL. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GLOBAL-ACCELERATOR-JP-10

- [ ] **Code:** **Question:** A basic Residency/state check fails. What would you do first using the CLI?
> **Covered in:** [AWS Global Accelerator — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator list-listeners --accelerator-arn ARN --region us-west-2` and capture exact status/reason/request ID. global routing must not send data to a disallowed Region or unprepared replica. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-GLOBAL-ACCELERATOR-MN-01

- [ ] **Question:** Compare Anycast IP with Accelerator listener. When would each change your design?
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Anycast IP: the same static addresses advertise globally and enter a nearby AWS edge. Accelerator listener: accepts TCP/UDP port ranges and distributes to endpoint groups. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GLOBAL-ACCELERATOR-MN-02

- [ ] **Question:** Compare Accelerator listener with Endpoint group. When would each change your design?
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Accelerator listener: accepts TCP/UDP port ranges and distributes to endpoint groups. Endpoint group: regional endpoints, traffic dial and health/check settings. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GLOBAL-ACCELERATOR-MN-03

- [ ] **Question:** Compare Endpoint group with Endpoint weight. When would each change your design?
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Endpoint group: regional endpoints, traffic dial and health/check settings. Endpoint weight: shifts traffic among endpoints within a group under health/capacity policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GLOBAL-ACCELERATOR-MN-04

- [ ] **Configuration review:** **Question:** Compare Endpoint weight with Health failover. When would each change your design?
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Endpoint weight: shifts traffic among endpoints within a group under health/capacity policy. Health failover: unhealthy endpoints/regions are removed under detection thresholds and state implications. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GLOBAL-ACCELERATOR-MN-05

- [ ] **Question:** Compare Health failover with Client IP preservation. When would each change your design?
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Health failover: unhealthy endpoints/regions are removed under detection thresholds and state implications. Client IP preservation: supported endpoint patterns retain source information under constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GLOBAL-ACCELERATOR-MN-06

- [ ] **Question:** Compare Client IP preservation with Traffic dial. When would each change your design?
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Client IP preservation: supported endpoint patterns retain source information under constraints. Traffic dial: controls percentage sent to a Region for canary/maintenance/capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GLOBAL-ACCELERATOR-MN-07

- [ ] **Configuration review:** **Question:** Compare Traffic dial with ALB/NLB/EC2/EIP endpoints. When would each change your design?
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Traffic dial: controls percentage sent to a Region for canary/maintenance/capacity. ALB/NLB/EC2/EIP endpoints: supported endpoint types provide different L7/L4 and address properties. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GLOBAL-ACCELERATOR-MN-08

- [ ] **Question:** Compare ALB/NLB/EC2/EIP endpoints with DNS vs anycast. When would each change your design?
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ALB/NLB/EC2/EIP endpoints: supported endpoint types provide different L7/L4 and address properties. DNS vs anycast: Global Accelerator reacts at network routing without waiting for client DNS TTL. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GLOBAL-ACCELERATOR-MN-09

- [ ] **Question:** Compare DNS vs anycast with Residency/state. When would each change your design?
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** DNS vs anycast: Global Accelerator reacts at network routing without waiting for client DNS TTL. Residency/state: global routing must not send data to a disallowed Region or unprepared replica. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GLOBAL-ACCELERATOR-MN-10

- [ ] **Configuration review:** **Question:** Compare Residency/state with Anycast IP. When would each change your design?
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Residency/state: global routing must not send data to a disallowed Region or unprepared replica. Anycast IP: the same static addresses advertise globally and enter a nearby AWS edge. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-GLOBAL-ACCELERATOR-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Anycast IP; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator list-accelerators --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. the same static addresses advertise globally and enter a nearby AWS edge. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GLOBAL-ACCELERATOR-MP-02

- [ ] **Question:** Production is degraded around Accelerator listener; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator list-listeners --accelerator-arn ARN --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. accepts TCP/UDP port ranges and distributes to endpoint groups. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GLOBAL-ACCELERATOR-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Endpoint group; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator list-endpoint-groups --listener-arn ARN --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. regional endpoints, traffic dial and health/check settings. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GLOBAL-ACCELERATOR-MP-04

- [ ] **Question:** Production is degraded around Endpoint weight; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator describe-endpoint-group --endpoint-group-arn ARN --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. shifts traffic among endpoints within a group under health/capacity policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GLOBAL-ACCELERATOR-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Health failover; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator list-accelerators --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. unhealthy endpoints/regions are removed under detection thresholds and state implications. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GLOBAL-ACCELERATOR-MP-06

- [ ] **Question:** Production is degraded around Client IP preservation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator list-listeners --accelerator-arn ARN --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. supported endpoint patterns retain source information under constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GLOBAL-ACCELERATOR-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Traffic dial; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator list-endpoint-groups --listener-arn ARN --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. controls percentage sent to a Region for canary/maintenance/capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GLOBAL-ACCELERATOR-MP-08

- [ ] **Question:** Production is degraded around ALB/NLB/EC2/EIP endpoints; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator describe-endpoint-group --endpoint-group-arn ARN --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. supported endpoint types provide different L7/L4 and address properties. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GLOBAL-ACCELERATOR-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around DNS vs anycast; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator list-accelerators --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. Global Accelerator reacts at network routing without waiting for client DNS TTL. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GLOBAL-ACCELERATOR-MP-10

- [ ] **Question:** Production is degraded around Residency/state; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator list-listeners --accelerator-arn ARN --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. global routing must not send data to a disallowed Region or unprepared replica. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-GLOBAL-ACCELERATOR-SN-01

- [ ] **Question:** Design a production AWS Global Accelerator capability where Anycast IP, Endpoint weight and Traffic dial are first-class requirements.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: the same static addresses advertise globally and enter a nearby AWS edge. shifts traffic among endpoints within a group under health/capacity policy. controls percentage sent to a Region for canary/maintenance/capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GLOBAL-ACCELERATOR-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Global Accelerator capability where Accelerator listener, Health failover and ALB/NLB/EC2/EIP endpoints are first-class requirements.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: accepts TCP/UDP port ranges and distributes to endpoint groups. unhealthy endpoints/regions are removed under detection thresholds and state implications. supported endpoint types provide different L7/L4 and address properties. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GLOBAL-ACCELERATOR-SN-03

- [ ] **Question:** Design a production AWS Global Accelerator capability where Endpoint group, Client IP preservation and DNS vs anycast are first-class requirements.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: regional endpoints, traffic dial and health/check settings. supported endpoint patterns retain source information under constraints. Global Accelerator reacts at network routing without waiting for client DNS TTL. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GLOBAL-ACCELERATOR-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Global Accelerator capability where Endpoint weight, Traffic dial and Residency/state are first-class requirements.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: shifts traffic among endpoints within a group under health/capacity policy. controls percentage sent to a Region for canary/maintenance/capacity. global routing must not send data to a disallowed Region or unprepared replica. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GLOBAL-ACCELERATOR-SN-05

- [ ] **Question:** Design a production AWS Global Accelerator capability where Health failover, ALB/NLB/EC2/EIP endpoints and Anycast IP are first-class requirements.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: unhealthy endpoints/regions are removed under detection thresholds and state implications. supported endpoint types provide different L7/L4 and address properties. the same static addresses advertise globally and enter a nearby AWS edge. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GLOBAL-ACCELERATOR-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Global Accelerator capability where Client IP preservation, DNS vs anycast and Accelerator listener are first-class requirements.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supported endpoint patterns retain source information under constraints. Global Accelerator reacts at network routing without waiting for client DNS TTL. accepts TCP/UDP port ranges and distributes to endpoint groups. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GLOBAL-ACCELERATOR-SN-07

- [ ] **Question:** Design a production AWS Global Accelerator capability where Traffic dial, Residency/state and Endpoint group are first-class requirements.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controls percentage sent to a Region for canary/maintenance/capacity. global routing must not send data to a disallowed Region or unprepared replica. regional endpoints, traffic dial and health/check settings. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GLOBAL-ACCELERATOR-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Global Accelerator capability where ALB/NLB/EC2/EIP endpoints, Anycast IP and Endpoint weight are first-class requirements.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supported endpoint types provide different L7/L4 and address properties. the same static addresses advertise globally and enter a nearby AWS edge. shifts traffic among endpoints within a group under health/capacity policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GLOBAL-ACCELERATOR-SN-09

- [ ] **Question:** Design a production AWS Global Accelerator capability where DNS vs anycast, Accelerator listener and Health failover are first-class requirements.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Global Accelerator reacts at network routing without waiting for client DNS TTL. accepts TCP/UDP port ranges and distributes to endpoint groups. unhealthy endpoints/regions are removed under detection thresholds and state implications. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GLOBAL-ACCELERATOR-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Global Accelerator capability where Residency/state, Endpoint group and Client IP preservation are first-class requirements.
> **Covered in:** [AWS Global Accelerator — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: global routing must not send data to a disallowed Region or unprepared replica. regional endpoints, traffic dial and health/check settings. supported endpoint patterns retain source information under constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-GLOBAL-ACCELERATOR-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Anycast IP. How do you lead it end to end?
> **Covered in:** [AWS Global Accelerator — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator list-accelerators --region us-west-2` as one read-only checkpoint, not the whole diagnosis. the same static addresses advertise globally and enter a nearby AWS edge. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GLOBAL-ACCELERATOR-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Accelerator listener. How do you lead it end to end?
> **Covered in:** [AWS Global Accelerator — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator list-listeners --accelerator-arn ARN --region us-west-2` as one read-only checkpoint, not the whole diagnosis. accepts TCP/UDP port ranges and distributes to endpoint groups. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GLOBAL-ACCELERATOR-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Endpoint group. How do you lead it end to end?
> **Covered in:** [AWS Global Accelerator — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator list-endpoint-groups --listener-arn ARN --region us-west-2` as one read-only checkpoint, not the whole diagnosis. regional endpoints, traffic dial and health/check settings. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GLOBAL-ACCELERATOR-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Endpoint weight. How do you lead it end to end?
> **Covered in:** [AWS Global Accelerator — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator describe-endpoint-group --endpoint-group-arn ARN --region us-west-2` as one read-only checkpoint, not the whole diagnosis. shifts traffic among endpoints within a group under health/capacity policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GLOBAL-ACCELERATOR-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Health failover. How do you lead it end to end?
> **Covered in:** [AWS Global Accelerator — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator list-accelerators --region us-west-2` as one read-only checkpoint, not the whole diagnosis. unhealthy endpoints/regions are removed under detection thresholds and state implications. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GLOBAL-ACCELERATOR-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Client IP preservation. How do you lead it end to end?
> **Covered in:** [AWS Global Accelerator — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator list-listeners --accelerator-arn ARN --region us-west-2` as one read-only checkpoint, not the whole diagnosis. supported endpoint patterns retain source information under constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GLOBAL-ACCELERATOR-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Traffic dial. How do you lead it end to end?
> **Covered in:** [AWS Global Accelerator — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator list-endpoint-groups --listener-arn ARN --region us-west-2` as one read-only checkpoint, not the whole diagnosis. controls percentage sent to a Region for canary/maintenance/capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GLOBAL-ACCELERATOR-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ALB/NLB/EC2/EIP endpoints. How do you lead it end to end?
> **Covered in:** [AWS Global Accelerator — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator describe-endpoint-group --endpoint-group-arn ARN --region us-west-2` as one read-only checkpoint, not the whole diagnosis. supported endpoint types provide different L7/L4 and address properties. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GLOBAL-ACCELERATOR-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DNS vs anycast. How do you lead it end to end?
> **Covered in:** [AWS Global Accelerator — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator list-accelerators --region us-west-2` as one read-only checkpoint, not the whole diagnosis. Global Accelerator reacts at network routing without waiting for client DNS TTL. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GLOBAL-ACCELERATOR-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Residency/state. How do you lead it end to end?
> **Covered in:** [AWS Global Accelerator — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator list-listeners --accelerator-arn ARN --region us-west-2` as one read-only checkpoint, not the whole diagnosis. global routing must not send data to a disallowed Region or unprepared replica. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Gateway Load Balancer](../03-gwlb/README.md) · [Study note](README.md) · [Next: Storage →](../../05-storage/README.md)

<!-- reading-navigation:end -->
