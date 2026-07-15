# PDB, priority, preemption and eviction — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JN-01

- [ ] **Question:** What is PDB, and why does it matter in PDB, priority, preemption and eviction?

**Answer:** minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JN-02

- [ ] **Question:** What is Eviction API, and why does it matter in PDB, priority, preemption and eviction?

**Answer:** admission checks PDB and graceful deletion compared with direct delete. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JN-03

- [ ] **Question:** What is Unhealthy eviction policy, and why does it matter in PDB, priority, preemption and eviction?

**Answer:** controls drain behavior for unhealthy Pods under supported API. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JN-04

- [ ] **Question:** What is PriorityClass, and why does it matter in PDB, priority, preemption and eviction?

**Answer:** numeric scheduling/eviction priority with globalDefault/preemption policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JN-05

- [ ] **Question:** What is Preemption, and why does it matter in PDB, priority, preemption and eviction?

**Answer:** scheduler removes lower-priority Pods when that can make a high-priority Pod feasible. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JN-06

- [ ] **Question:** What is Nominated node, and why does it matter in PDB, priority, preemption and eviction?

**Answer:** indicates expected preemption placement but can change before binding. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JN-07

- [ ] **Question:** What is Node-pressure eviction, and why does it matter in PDB, priority, preemption and eviction?

**Answer:** kubelet reclaims resources based on signals/QoS/priority and is involuntary. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JN-08

- [ ] **Code:** **Question:** What does `kubectl get events -A | rg 'Preempt|Evict|Disruption'` help you verify for PDB, priority, preemption and eviction?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: NoExecute taint can evict non-tolerating Pods after tolerationSeconds.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JN-09

- [ ] **Code:** **Question:** What does `kubectl get pdb,priorityclass -A` help you verify for PDB, priority, preemption and eviction?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: cordons then evicts/deletes workload Pods while respecting flags/PDB.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe pdb NAME -n NS` help you verify for PDB, priority, preemption and eviction?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: strict PDB/priority can block maintenance or starve lower-value platform services.

## Junior — procedural and command questions

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JP-01

- [ ] **Code:** **Question:** A basic PDB check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pdb,priorityclass -A` and capture exact status/reason/request ID. minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JP-02

- [ ] **Question:** A basic Eviction API check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pdb NAME -n NS` and capture exact status/reason/request ID. admission checks PDB and graceful deletion compared with direct delete. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JP-03

- [ ] **Question:** A basic Unhealthy eviction policy check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl drain NODE --ignore-daemonsets --dry-run=server` and capture exact status/reason/request ID. controls drain behavior for unhealthy Pods under supported API. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JP-04

- [ ] **Code:** **Question:** A basic PriorityClass check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A | rg 'Preempt|Evict|Disruption'` and capture exact status/reason/request ID. numeric scheduling/eviction priority with globalDefault/preemption policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JP-05

- [ ] **Question:** A basic Preemption check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pdb,priorityclass -A` and capture exact status/reason/request ID. scheduler removes lower-priority Pods when that can make a high-priority Pod feasible. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JP-06

- [ ] **Question:** A basic Nominated node check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pdb NAME -n NS` and capture exact status/reason/request ID. indicates expected preemption placement but can change before binding. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JP-07

- [ ] **Code:** **Question:** A basic Node-pressure eviction check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl drain NODE --ignore-daemonsets --dry-run=server` and capture exact status/reason/request ID. kubelet reclaims resources based on signals/QoS/priority and is involuntary. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JP-08

- [ ] **Question:** A basic Taint eviction check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A | rg 'Preempt|Evict|Disruption'` and capture exact status/reason/request ID. NoExecute taint can evict non-tolerating Pods after tolerationSeconds. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JP-09

- [ ] **Question:** A basic Drain check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pdb,priorityclass -A` and capture exact status/reason/request ID. cordons then evicts/deletes workload Pods while respecting flags/PDB. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-JP-10

- [ ] **Code:** **Question:** A basic Overprotection check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pdb NAME -n NS` and capture exact status/reason/request ID. strict PDB/priority can block maintenance or starve lower-value platform services. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MN-01

- [ ] **Question:** Compare PDB with Eviction API. When would each change your design?

**Answer:** PDB: minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Eviction API: admission checks PDB and graceful deletion compared with direct delete. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MN-02

- [ ] **Question:** Compare Eviction API with Unhealthy eviction policy. When would each change your design?

**Answer:** Eviction API: admission checks PDB and graceful deletion compared with direct delete. Unhealthy eviction policy: controls drain behavior for unhealthy Pods under supported API. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MN-03

- [ ] **Question:** Compare Unhealthy eviction policy with PriorityClass. When would each change your design?

**Answer:** Unhealthy eviction policy: controls drain behavior for unhealthy Pods under supported API. PriorityClass: numeric scheduling/eviction priority with globalDefault/preemption policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MN-04

- [ ] **Configuration review:** **Question:** Compare PriorityClass with Preemption. When would each change your design?

**Answer:** PriorityClass: numeric scheduling/eviction priority with globalDefault/preemption policy. Preemption: scheduler removes lower-priority Pods when that can make a high-priority Pod feasible. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MN-05

- [ ] **Question:** Compare Preemption with Nominated node. When would each change your design?

**Answer:** Preemption: scheduler removes lower-priority Pods when that can make a high-priority Pod feasible. Nominated node: indicates expected preemption placement but can change before binding. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MN-06

- [ ] **Question:** Compare Nominated node with Node-pressure eviction. When would each change your design?

**Answer:** Nominated node: indicates expected preemption placement but can change before binding. Node-pressure eviction: kubelet reclaims resources based on signals/QoS/priority and is involuntary. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MN-07

- [ ] **Configuration review:** **Question:** Compare Node-pressure eviction with Taint eviction. When would each change your design?

**Answer:** Node-pressure eviction: kubelet reclaims resources based on signals/QoS/priority and is involuntary. Taint eviction: NoExecute taint can evict non-tolerating Pods after tolerationSeconds. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MN-08

- [ ] **Question:** Compare Taint eviction with Drain. When would each change your design?

**Answer:** Taint eviction: NoExecute taint can evict non-tolerating Pods after tolerationSeconds. Drain: cordons then evicts/deletes workload Pods while respecting flags/PDB. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MN-09

- [ ] **Question:** Compare Drain with Overprotection. When would each change your design?

**Answer:** Drain: cordons then evicts/deletes workload Pods while respecting flags/PDB. Overprotection: strict PDB/priority can block maintenance or starve lower-value platform services. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MN-10

- [ ] **Configuration review:** **Question:** Compare Overprotection with PDB. When would each change your design?

**Answer:** Overprotection: strict PDB/priority can block maintenance or starve lower-value platform services. PDB: minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around PDB; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pdb,priorityclass -A` plus recent events/changes, then correlate the service-specific SLI. minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MP-02

- [ ] **Question:** Production is degraded around Eviction API; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pdb NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. admission checks PDB and graceful deletion compared with direct delete. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Unhealthy eviction policy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl drain NODE --ignore-daemonsets --dry-run=server` plus recent events/changes, then correlate the service-specific SLI. controls drain behavior for unhealthy Pods under supported API. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MP-04

- [ ] **Question:** Production is degraded around PriorityClass; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A | rg 'Preempt|Evict|Disruption'` plus recent events/changes, then correlate the service-specific SLI. numeric scheduling/eviction priority with globalDefault/preemption policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Preemption; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pdb,priorityclass -A` plus recent events/changes, then correlate the service-specific SLI. scheduler removes lower-priority Pods when that can make a high-priority Pod feasible. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MP-06

- [ ] **Question:** Production is degraded around Nominated node; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pdb NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. indicates expected preemption placement but can change before binding. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Node-pressure eviction; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl drain NODE --ignore-daemonsets --dry-run=server` plus recent events/changes, then correlate the service-specific SLI. kubelet reclaims resources based on signals/QoS/priority and is involuntary. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MP-08

- [ ] **Question:** Production is degraded around Taint eviction; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A | rg 'Preempt|Evict|Disruption'` plus recent events/changes, then correlate the service-specific SLI. NoExecute taint can evict non-tolerating Pods after tolerationSeconds. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Drain; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pdb,priorityclass -A` plus recent events/changes, then correlate the service-specific SLI. cordons then evicts/deletes workload Pods while respecting flags/PDB. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-MP-10

- [ ] **Question:** Production is degraded around Overprotection; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pdb NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. strict PDB/priority can block maintenance or starve lower-value platform services. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SN-01

- [ ] **Question:** Design a production PDB, priority, preemption and eviction capability where PDB, PriorityClass and Node-pressure eviction are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. numeric scheduling/eviction priority with globalDefault/preemption policy. kubelet reclaims resources based on signals/QoS/priority and is involuntary. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production PDB, priority, preemption and eviction capability where Eviction API, Preemption and Taint eviction are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: admission checks PDB and graceful deletion compared with direct delete. scheduler removes lower-priority Pods when that can make a high-priority Pod feasible. NoExecute taint can evict non-tolerating Pods after tolerationSeconds. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SN-03

- [ ] **Question:** Design a production PDB, priority, preemption and eviction capability where Unhealthy eviction policy, Nominated node and Drain are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controls drain behavior for unhealthy Pods under supported API. indicates expected preemption placement but can change before binding. cordons then evicts/deletes workload Pods while respecting flags/PDB. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production PDB, priority, preemption and eviction capability where PriorityClass, Node-pressure eviction and Overprotection are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: numeric scheduling/eviction priority with globalDefault/preemption policy. kubelet reclaims resources based on signals/QoS/priority and is involuntary. strict PDB/priority can block maintenance or starve lower-value platform services. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SN-05

- [ ] **Question:** Design a production PDB, priority, preemption and eviction capability where Preemption, Taint eviction and PDB are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scheduler removes lower-priority Pods when that can make a high-priority Pod feasible. NoExecute taint can evict non-tolerating Pods after tolerationSeconds. minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production PDB, priority, preemption and eviction capability where Nominated node, Drain and Eviction API are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: indicates expected preemption placement but can change before binding. cordons then evicts/deletes workload Pods while respecting flags/PDB. admission checks PDB and graceful deletion compared with direct delete. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SN-07

- [ ] **Question:** Design a production PDB, priority, preemption and eviction capability where Node-pressure eviction, Overprotection and Unhealthy eviction policy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: kubelet reclaims resources based on signals/QoS/priority and is involuntary. strict PDB/priority can block maintenance or starve lower-value platform services. controls drain behavior for unhealthy Pods under supported API. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production PDB, priority, preemption and eviction capability where Taint eviction, PDB and PriorityClass are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: NoExecute taint can evict non-tolerating Pods after tolerationSeconds. minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. numeric scheduling/eviction priority with globalDefault/preemption policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SN-09

- [ ] **Question:** Design a production PDB, priority, preemption and eviction capability where Drain, Eviction API and Preemption are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cordons then evicts/deletes workload Pods while respecting flags/PDB. admission checks PDB and graceful deletion compared with direct delete. scheduler removes lower-priority Pods when that can make a high-priority Pod feasible. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production PDB, priority, preemption and eviction capability where Overprotection, Unhealthy eviction policy and Nominated node are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: strict PDB/priority can block maintenance or starve lower-value platform services. controls drain behavior for unhealthy Pods under supported API. indicates expected preemption placement but can change before binding. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving PDB. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pdb,priorityclass -A` as one read-only checkpoint, not the whole diagnosis. minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Eviction API. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pdb NAME -n NS` as one read-only checkpoint, not the whole diagnosis. admission checks PDB and graceful deletion compared with direct delete. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Unhealthy eviction policy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl drain NODE --ignore-daemonsets --dry-run=server` as one read-only checkpoint, not the whole diagnosis. controls drain behavior for unhealthy Pods under supported API. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving PriorityClass. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A | rg 'Preempt|Evict|Disruption'` as one read-only checkpoint, not the whole diagnosis. numeric scheduling/eviction priority with globalDefault/preemption policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Preemption. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pdb,priorityclass -A` as one read-only checkpoint, not the whole diagnosis. scheduler removes lower-priority Pods when that can make a high-priority Pod feasible. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Nominated node. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pdb NAME -n NS` as one read-only checkpoint, not the whole diagnosis. indicates expected preemption placement but can change before binding. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node-pressure eviction. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl drain NODE --ignore-daemonsets --dry-run=server` as one read-only checkpoint, not the whole diagnosis. kubelet reclaims resources based on signals/QoS/priority and is involuntary. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Taint eviction. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A | rg 'Preempt|Evict|Disruption'` as one read-only checkpoint, not the whole diagnosis. NoExecute taint can evict non-tolerating Pods after tolerationSeconds. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Drain. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pdb,priorityclass -A` as one read-only checkpoint, not the whole diagnosis. cordons then evicts/deletes workload Pods while respecting flags/PDB. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PDB-PRIORITY-PREEMPTION-AND-EVICTION-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Overprotection. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pdb NAME -n NS` as one read-only checkpoint, not the whole diagnosis. strict PDB/priority can block maintenance or starve lower-value platform services. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
