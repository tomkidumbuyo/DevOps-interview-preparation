# HPA, VPA and KEDA — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### HPA-VPA-AND-KEDA-JN-01

- [ ] **Question:** What is HPA ratio, and why does it matter in HPA, VPA and KEDA?
> **Covered in:** [HPA, VPA and KEDA — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** desired replicas derives current/target metric with tolerance and missing/not-ready handling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HPA-VPA-AND-KEDA-JN-02

- [ ] **Question:** What is Resource utilization, and why does it matter in HPA, VPA and KEDA?
> **Covered in:** [HPA, VPA and KEDA — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** usage divided by requests means bad/missing requests break CPU/memory scaling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HPA-VPA-AND-KEDA-JN-03

- [ ] **Question:** What is Custom/external metric, and why does it matter in HPA, VPA and KEDA?
> **Covered in:** [HPA, VPA and KEDA — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** adapter exposes application/provider signal with availability/cardinality semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HPA-VPA-AND-KEDA-JN-04

- [ ] **Question:** What is HPA behavior, and why does it matter in HPA, VPA and KEDA?
> **Covered in:** [HPA, VPA and KEDA — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** stabilization and policies bound scale-up/down rate. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HPA-VPA-AND-KEDA-JN-05

- [ ] **Question:** What is VPA recommendation, and why does it matter in HPA, VPA and KEDA?
> **Covered in:** [HPA, VPA and KEDA — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** learns requests from usage history and can restart Pods to apply changes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HPA-VPA-AND-KEDA-JN-06

- [ ] **Question:** What is VPA/HPA interaction, and why does it matter in HPA, VPA and KEDA?
> **Covered in:** [HPA, VPA and KEDA — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** both changing CPU requests/replicas can create feedback without design. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HPA-VPA-AND-KEDA-JN-07

- [ ] **Question:** What is KEDA trigger, and why does it matter in HPA, VPA and KEDA?
> **Covered in:** [HPA, VPA and KEDA — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** event source drives Scale subresource and supports activation/scale-to-zero. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HPA-VPA-AND-KEDA-JN-08

- [ ] **Code:** **Question:** What does `kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1 | jq` help you verify for HPA, VPA and KEDA?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: leading demand signal but must account for service time/token work.

### HPA-VPA-AND-KEDA-JN-09

- [ ] **Code:** **Question:** What does `kubectl get scaledobject -A` help you verify for HPA, VPA and KEDA?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: cold start and missing metric/activation path must meet SLO.

### HPA-VPA-AND-KEDA-JN-10

- [ ] **Code:** **Question:** What does `kubectl get vpa -A` help you verify for HPA, VPA and KEDA?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: replica scale cannot exceed database/provider/tenant capacity.

## Junior — procedural and command questions

### HPA-VPA-AND-KEDA-JP-01

- [ ] **Code:** **Question:** A basic HPA ratio check fails. What would you do first using the CLI?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get hpa -A` and capture exact status/reason/request ID. desired replicas derives current/target metric with tolerance and missing/not-ready handling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HPA-VPA-AND-KEDA-JP-02

- [ ] **Question:** A basic Resource utilization check fails. What would you do first?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe hpa NAME -n NS` and capture exact status/reason/request ID. usage divided by requests means bad/missing requests break CPU/memory scaling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HPA-VPA-AND-KEDA-JP-03

- [ ] **Question:** A basic Custom/external metric check fails. What would you do first?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1 | jq` and capture exact status/reason/request ID. adapter exposes application/provider signal with availability/cardinality semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HPA-VPA-AND-KEDA-JP-04

- [ ] **Code:** **Question:** A basic HPA behavior check fails. What would you do first using the CLI?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get scaledobject -A` and capture exact status/reason/request ID. stabilization and policies bound scale-up/down rate. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HPA-VPA-AND-KEDA-JP-05

- [ ] **Question:** A basic VPA recommendation check fails. What would you do first?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get vpa -A` and capture exact status/reason/request ID. learns requests from usage history and can restart Pods to apply changes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HPA-VPA-AND-KEDA-JP-06

- [ ] **Question:** A basic VPA/HPA interaction check fails. What would you do first?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get hpa -A` and capture exact status/reason/request ID. both changing CPU requests/replicas can create feedback without design. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HPA-VPA-AND-KEDA-JP-07

- [ ] **Code:** **Question:** A basic KEDA trigger check fails. What would you do first using the CLI?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe hpa NAME -n NS` and capture exact status/reason/request ID. event source drives Scale subresource and supports activation/scale-to-zero. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HPA-VPA-AND-KEDA-JP-08

- [ ] **Question:** A basic Queue age/depth check fails. What would you do first?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1 | jq` and capture exact status/reason/request ID. leading demand signal but must account for service time/token work. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HPA-VPA-AND-KEDA-JP-09

- [ ] **Question:** A basic Scale-to-zero check fails. What would you do first?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get scaledobject -A` and capture exact status/reason/request ID. cold start and missing metric/activation path must meet SLO. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HPA-VPA-AND-KEDA-JP-10

- [ ] **Code:** **Question:** A basic Downstream protection check fails. What would you do first using the CLI?
> **Covered in:** [HPA, VPA and KEDA — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get vpa -A` and capture exact status/reason/request ID. replica scale cannot exceed database/provider/tenant capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### HPA-VPA-AND-KEDA-MN-01

- [ ] **Question:** Compare HPA ratio with Resource utilization. When would each change your design?
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** HPA ratio: desired replicas derives current/target metric with tolerance and missing/not-ready handling. Resource utilization: usage divided by requests means bad/missing requests break CPU/memory scaling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HPA-VPA-AND-KEDA-MN-02

- [ ] **Question:** Compare Resource utilization with Custom/external metric. When would each change your design?
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Resource utilization: usage divided by requests means bad/missing requests break CPU/memory scaling. Custom/external metric: adapter exposes application/provider signal with availability/cardinality semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HPA-VPA-AND-KEDA-MN-03

- [ ] **Question:** Compare Custom/external metric with HPA behavior. When would each change your design?
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Custom/external metric: adapter exposes application/provider signal with availability/cardinality semantics. HPA behavior: stabilization and policies bound scale-up/down rate. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HPA-VPA-AND-KEDA-MN-04

- [ ] **Configuration review:** **Question:** Compare HPA behavior with VPA recommendation. When would each change your design?
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** HPA behavior: stabilization and policies bound scale-up/down rate. VPA recommendation: learns requests from usage history and can restart Pods to apply changes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HPA-VPA-AND-KEDA-MN-05

- [ ] **Question:** Compare VPA recommendation with VPA/HPA interaction. When would each change your design?
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** VPA recommendation: learns requests from usage history and can restart Pods to apply changes. VPA/HPA interaction: both changing CPU requests/replicas can create feedback without design. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HPA-VPA-AND-KEDA-MN-06

- [ ] **Question:** Compare VPA/HPA interaction with KEDA trigger. When would each change your design?
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** VPA/HPA interaction: both changing CPU requests/replicas can create feedback without design. KEDA trigger: event source drives Scale subresource and supports activation/scale-to-zero. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HPA-VPA-AND-KEDA-MN-07

- [ ] **Configuration review:** **Question:** Compare KEDA trigger with Queue age/depth. When would each change your design?
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** KEDA trigger: event source drives Scale subresource and supports activation/scale-to-zero. Queue age/depth: leading demand signal but must account for service time/token work. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HPA-VPA-AND-KEDA-MN-08

- [ ] **Question:** Compare Queue age/depth with Scale-to-zero. When would each change your design?
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Queue age/depth: leading demand signal but must account for service time/token work. Scale-to-zero: cold start and missing metric/activation path must meet SLO. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HPA-VPA-AND-KEDA-MN-09

- [ ] **Question:** Compare Scale-to-zero with Downstream protection. When would each change your design?
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Scale-to-zero: cold start and missing metric/activation path must meet SLO. Downstream protection: replica scale cannot exceed database/provider/tenant capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HPA-VPA-AND-KEDA-MN-10

- [ ] **Configuration review:** **Question:** Compare Downstream protection with HPA ratio. When would each change your design?
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Downstream protection: replica scale cannot exceed database/provider/tenant capacity. HPA ratio: desired replicas derives current/target metric with tolerance and missing/not-ready handling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### HPA-VPA-AND-KEDA-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around HPA ratio; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get hpa -A` plus recent events/changes, then correlate the service-specific SLI. desired replicas derives current/target metric with tolerance and missing/not-ready handling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HPA-VPA-AND-KEDA-MP-02

- [ ] **Question:** Production is degraded around Resource utilization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe hpa NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. usage divided by requests means bad/missing requests break CPU/memory scaling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HPA-VPA-AND-KEDA-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Custom/external metric; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1 | jq` plus recent events/changes, then correlate the service-specific SLI. adapter exposes application/provider signal with availability/cardinality semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HPA-VPA-AND-KEDA-MP-04

- [ ] **Question:** Production is degraded around HPA behavior; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get scaledobject -A` plus recent events/changes, then correlate the service-specific SLI. stabilization and policies bound scale-up/down rate. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HPA-VPA-AND-KEDA-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around VPA recommendation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get vpa -A` plus recent events/changes, then correlate the service-specific SLI. learns requests from usage history and can restart Pods to apply changes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HPA-VPA-AND-KEDA-MP-06

- [ ] **Question:** Production is degraded around VPA/HPA interaction; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get hpa -A` plus recent events/changes, then correlate the service-specific SLI. both changing CPU requests/replicas can create feedback without design. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HPA-VPA-AND-KEDA-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around KEDA trigger; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe hpa NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. event source drives Scale subresource and supports activation/scale-to-zero. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HPA-VPA-AND-KEDA-MP-08

- [ ] **Question:** Production is degraded around Queue age/depth; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1 | jq` plus recent events/changes, then correlate the service-specific SLI. leading demand signal but must account for service time/token work. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HPA-VPA-AND-KEDA-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Scale-to-zero; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get scaledobject -A` plus recent events/changes, then correlate the service-specific SLI. cold start and missing metric/activation path must meet SLO. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HPA-VPA-AND-KEDA-MP-10

- [ ] **Question:** Production is degraded around Downstream protection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get vpa -A` plus recent events/changes, then correlate the service-specific SLI. replica scale cannot exceed database/provider/tenant capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### HPA-VPA-AND-KEDA-SN-01

- [ ] **Question:** Design a production HPA, VPA and KEDA capability where HPA ratio, HPA behavior and KEDA trigger are first-class requirements.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: desired replicas derives current/target metric with tolerance and missing/not-ready handling. stabilization and policies bound scale-up/down rate. event source drives Scale subresource and supports activation/scale-to-zero. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HPA-VPA-AND-KEDA-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production HPA, VPA and KEDA capability where Resource utilization, VPA recommendation and Queue age/depth are first-class requirements.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: usage divided by requests means bad/missing requests break CPU/memory scaling. learns requests from usage history and can restart Pods to apply changes. leading demand signal but must account for service time/token work. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HPA-VPA-AND-KEDA-SN-03

- [ ] **Question:** Design a production HPA, VPA and KEDA capability where Custom/external metric, VPA/HPA interaction and Scale-to-zero are first-class requirements.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: adapter exposes application/provider signal with availability/cardinality semantics. both changing CPU requests/replicas can create feedback without design. cold start and missing metric/activation path must meet SLO. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HPA-VPA-AND-KEDA-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production HPA, VPA and KEDA capability where HPA behavior, KEDA trigger and Downstream protection are first-class requirements.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stabilization and policies bound scale-up/down rate. event source drives Scale subresource and supports activation/scale-to-zero. replica scale cannot exceed database/provider/tenant capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HPA-VPA-AND-KEDA-SN-05

- [ ] **Question:** Design a production HPA, VPA and KEDA capability where VPA recommendation, Queue age/depth and HPA ratio are first-class requirements.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: learns requests from usage history and can restart Pods to apply changes. leading demand signal but must account for service time/token work. desired replicas derives current/target metric with tolerance and missing/not-ready handling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HPA-VPA-AND-KEDA-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production HPA, VPA and KEDA capability where VPA/HPA interaction, Scale-to-zero and Resource utilization are first-class requirements.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: both changing CPU requests/replicas can create feedback without design. cold start and missing metric/activation path must meet SLO. usage divided by requests means bad/missing requests break CPU/memory scaling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HPA-VPA-AND-KEDA-SN-07

- [ ] **Question:** Design a production HPA, VPA and KEDA capability where KEDA trigger, Downstream protection and Custom/external metric are first-class requirements.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: event source drives Scale subresource and supports activation/scale-to-zero. replica scale cannot exceed database/provider/tenant capacity. adapter exposes application/provider signal with availability/cardinality semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HPA-VPA-AND-KEDA-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production HPA, VPA and KEDA capability where Queue age/depth, HPA ratio and HPA behavior are first-class requirements.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: leading demand signal but must account for service time/token work. desired replicas derives current/target metric with tolerance and missing/not-ready handling. stabilization and policies bound scale-up/down rate. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HPA-VPA-AND-KEDA-SN-09

- [ ] **Question:** Design a production HPA, VPA and KEDA capability where Scale-to-zero, Resource utilization and VPA recommendation are first-class requirements.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cold start and missing metric/activation path must meet SLO. usage divided by requests means bad/missing requests break CPU/memory scaling. learns requests from usage history and can restart Pods to apply changes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HPA-VPA-AND-KEDA-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production HPA, VPA and KEDA capability where Downstream protection, Custom/external metric and VPA/HPA interaction are first-class requirements.
> **Covered in:** [HPA, VPA and KEDA — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: replica scale cannot exceed database/provider/tenant capacity. adapter exposes application/provider signal with availability/cardinality semantics. both changing CPU requests/replicas can create feedback without design. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### HPA-VPA-AND-KEDA-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving HPA ratio. How do you lead it end to end?
> **Covered in:** [HPA, VPA and KEDA — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get hpa -A` as one read-only checkpoint, not the whole diagnosis. desired replicas derives current/target metric with tolerance and missing/not-ready handling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HPA-VPA-AND-KEDA-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource utilization. How do you lead it end to end?
> **Covered in:** [HPA, VPA and KEDA — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe hpa NAME -n NS` as one read-only checkpoint, not the whole diagnosis. usage divided by requests means bad/missing requests break CPU/memory scaling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HPA-VPA-AND-KEDA-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Custom/external metric. How do you lead it end to end?
> **Covered in:** [HPA, VPA and KEDA — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1 | jq` as one read-only checkpoint, not the whole diagnosis. adapter exposes application/provider signal with availability/cardinality semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HPA-VPA-AND-KEDA-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving HPA behavior. How do you lead it end to end?
> **Covered in:** [HPA, VPA and KEDA — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get scaledobject -A` as one read-only checkpoint, not the whole diagnosis. stabilization and policies bound scale-up/down rate. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HPA-VPA-AND-KEDA-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPA recommendation. How do you lead it end to end?
> **Covered in:** [HPA, VPA and KEDA — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get vpa -A` as one read-only checkpoint, not the whole diagnosis. learns requests from usage history and can restart Pods to apply changes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HPA-VPA-AND-KEDA-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPA/HPA interaction. How do you lead it end to end?
> **Covered in:** [HPA, VPA and KEDA — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get hpa -A` as one read-only checkpoint, not the whole diagnosis. both changing CPU requests/replicas can create feedback without design. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HPA-VPA-AND-KEDA-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving KEDA trigger. How do you lead it end to end?
> **Covered in:** [HPA, VPA and KEDA — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe hpa NAME -n NS` as one read-only checkpoint, not the whole diagnosis. event source drives Scale subresource and supports activation/scale-to-zero. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HPA-VPA-AND-KEDA-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Queue age/depth. How do you lead it end to end?
> **Covered in:** [HPA, VPA and KEDA — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1 | jq` as one read-only checkpoint, not the whole diagnosis. leading demand signal but must account for service time/token work. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HPA-VPA-AND-KEDA-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Scale-to-zero. How do you lead it end to end?
> **Covered in:** [HPA, VPA and KEDA — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get scaledobject -A` as one read-only checkpoint, not the whole diagnosis. cold start and missing metric/activation path must meet SLO. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HPA-VPA-AND-KEDA-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Downstream protection. How do you lead it end to end?
> **Covered in:** [HPA, VPA and KEDA — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get vpa -A` as one read-only checkpoint, not the whole diagnosis. replica scale cannot exceed database/provider/tenant capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Affinity, taints and topology placement](../02-placement/README.md) · [Study note](README.md) · [Next: Cluster Autoscaler, Karpenter and node lifecycle →](../04-node-autoscaling/README.md)

<!-- reading-navigation:end -->
