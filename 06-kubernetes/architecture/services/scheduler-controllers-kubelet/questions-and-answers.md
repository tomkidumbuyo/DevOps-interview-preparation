# Scheduler, controllers and kubelet — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### SCHEDULER-CONTROLLERS-AND-KUBELET-JN-01

- [ ] **Question:** What is Controller loop, and why does it matter in Scheduler, controllers and kubelet?

**Answer:** watches desired/observed state and performs level-based idempotent reconciliation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JN-02

- [ ] **Question:** What is Scheduler queue, and why does it matter in Scheduler, controllers and kubelet?

**Answer:** unscheduled Pods progress through filtering/scoring/backoff before binding. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JN-03

- [ ] **Question:** What is Filter plugin, and why does it matter in Scheduler, controllers and kubelet?

**Answer:** rejects nodes that cannot satisfy resources, affinity, taints, topology or volumes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JN-04

- [ ] **Question:** What is Score plugin, and why does it matter in Scheduler, controllers and kubelet?

**Answer:** ranks feasible nodes and can favor spread/bin packing/locality. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JN-05

- [ ] **Question:** What is Binding, and why does it matter in Scheduler, controllers and kubelet?

**Answer:** records selected node in Pod spec after scheduling assumptions/reservations. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JN-06

- [ ] **Question:** What is Kubelet Pod sync, and why does it matter in Scheduler, controllers and kubelet?

**Answer:** realizes assigned Pod through volume, sandbox, image and container runtime operations. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JN-07

- [ ] **Question:** What is CRI, and why does it matter in Scheduler, controllers and kubelet?

**Answer:** gRPC boundary from kubelet to containerd/CRI-O runtime. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JN-08

- [ ] **Code:** **Question:** What does `journalctl -u kubelet -u containerd --since '-30 min'` help you verify for Scheduler, controllers and kubelet?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: kubelet heartbeat and conditions drive availability/eviction decisions.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JN-09

- [ ] **Code:** **Question:** What does `kubectl get events -A --field-selector=reason=FailedScheduling` help you verify for Scheduler, controllers and kubelet?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: reconciles nodes/routes/load balancers against cloud APIs.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JN-10

- [ ] **Code:** **Question:** What does `kubectl get lease -n kube-system` help you verify for Scheduler, controllers and kubelet?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: controllers/schedulers use leases so only active leader mutates shared state.

## Junior — procedural and command questions

### SCHEDULER-CONTROLLERS-AND-KUBELET-JP-01

- [ ] **Code:** **Question:** A basic Controller loop check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. watches desired/observed state and performs level-based idempotent reconciliation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JP-02

- [ ] **Question:** A basic Scheduler queue check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get lease -n kube-system` and capture exact status/reason/request ID. unscheduled Pods progress through filtering/scoring/backoff before binding. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JP-03

- [ ] **Question:** A basic Filter plugin check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe node NODE` and capture exact status/reason/request ID. rejects nodes that cannot satisfy resources, affinity, taints, topology or volumes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JP-04

- [ ] **Code:** **Question:** A basic Score plugin check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `journalctl -u kubelet -u containerd --since '-30 min'` and capture exact status/reason/request ID. ranks feasible nodes and can favor spread/bin packing/locality. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JP-05

- [ ] **Question:** A basic Binding check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. records selected node in Pod spec after scheduling assumptions/reservations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JP-06

- [ ] **Question:** A basic Kubelet Pod sync check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get lease -n kube-system` and capture exact status/reason/request ID. realizes assigned Pod through volume, sandbox, image and container runtime operations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JP-07

- [ ] **Code:** **Question:** A basic CRI check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe node NODE` and capture exact status/reason/request ID. gRPC boundary from kubelet to containerd/CRI-O runtime. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JP-08

- [ ] **Question:** A basic Node status/lease check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `journalctl -u kubelet -u containerd --since '-30 min'` and capture exact status/reason/request ID. kubelet heartbeat and conditions drive availability/eviction decisions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JP-09

- [ ] **Question:** A basic Cloud controller check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. reconciles nodes/routes/load balancers against cloud APIs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SCHEDULER-CONTROLLERS-AND-KUBELET-JP-10

- [ ] **Code:** **Question:** A basic Leader election check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get lease -n kube-system` and capture exact status/reason/request ID. controllers/schedulers use leases so only active leader mutates shared state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### SCHEDULER-CONTROLLERS-AND-KUBELET-MN-01

- [ ] **Question:** Compare Controller loop with Scheduler queue. When would each change your design?

**Answer:** Controller loop: watches desired/observed state and performs level-based idempotent reconciliation. Scheduler queue: unscheduled Pods progress through filtering/scoring/backoff before binding. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MN-02

- [ ] **Question:** Compare Scheduler queue with Filter plugin. When would each change your design?

**Answer:** Scheduler queue: unscheduled Pods progress through filtering/scoring/backoff before binding. Filter plugin: rejects nodes that cannot satisfy resources, affinity, taints, topology or volumes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MN-03

- [ ] **Question:** Compare Filter plugin with Score plugin. When would each change your design?

**Answer:** Filter plugin: rejects nodes that cannot satisfy resources, affinity, taints, topology or volumes. Score plugin: ranks feasible nodes and can favor spread/bin packing/locality. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MN-04

- [ ] **Configuration review:** **Question:** Compare Score plugin with Binding. When would each change your design?

**Answer:** Score plugin: ranks feasible nodes and can favor spread/bin packing/locality. Binding: records selected node in Pod spec after scheduling assumptions/reservations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MN-05

- [ ] **Question:** Compare Binding with Kubelet Pod sync. When would each change your design?

**Answer:** Binding: records selected node in Pod spec after scheduling assumptions/reservations. Kubelet Pod sync: realizes assigned Pod through volume, sandbox, image and container runtime operations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MN-06

- [ ] **Question:** Compare Kubelet Pod sync with CRI. When would each change your design?

**Answer:** Kubelet Pod sync: realizes assigned Pod through volume, sandbox, image and container runtime operations. CRI: gRPC boundary from kubelet to containerd/CRI-O runtime. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MN-07

- [ ] **Configuration review:** **Question:** Compare CRI with Node status/lease. When would each change your design?

**Answer:** CRI: gRPC boundary from kubelet to containerd/CRI-O runtime. Node status/lease: kubelet heartbeat and conditions drive availability/eviction decisions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MN-08

- [ ] **Question:** Compare Node status/lease with Cloud controller. When would each change your design?

**Answer:** Node status/lease: kubelet heartbeat and conditions drive availability/eviction decisions. Cloud controller: reconciles nodes/routes/load balancers against cloud APIs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MN-09

- [ ] **Question:** Compare Cloud controller with Leader election. When would each change your design?

**Answer:** Cloud controller: reconciles nodes/routes/load balancers against cloud APIs. Leader election: controllers/schedulers use leases so only active leader mutates shared state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MN-10

- [ ] **Configuration review:** **Question:** Compare Leader election with Controller loop. When would each change your design?

**Answer:** Leader election: controllers/schedulers use leases so only active leader mutates shared state. Controller loop: watches desired/observed state and performs level-based idempotent reconciliation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### SCHEDULER-CONTROLLERS-AND-KUBELET-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Controller loop; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. watches desired/observed state and performs level-based idempotent reconciliation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MP-02

- [ ] **Question:** Production is degraded around Scheduler queue; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get lease -n kube-system` plus recent events/changes, then correlate the service-specific SLI. unscheduled Pods progress through filtering/scoring/backoff before binding. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Filter plugin; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe node NODE` plus recent events/changes, then correlate the service-specific SLI. rejects nodes that cannot satisfy resources, affinity, taints, topology or volumes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MP-04

- [ ] **Question:** Production is degraded around Score plugin; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `journalctl -u kubelet -u containerd --since '-30 min'` plus recent events/changes, then correlate the service-specific SLI. ranks feasible nodes and can favor spread/bin packing/locality. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Binding; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. records selected node in Pod spec after scheduling assumptions/reservations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MP-06

- [ ] **Question:** Production is degraded around Kubelet Pod sync; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get lease -n kube-system` plus recent events/changes, then correlate the service-specific SLI. realizes assigned Pod through volume, sandbox, image and container runtime operations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around CRI; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe node NODE` plus recent events/changes, then correlate the service-specific SLI. gRPC boundary from kubelet to containerd/CRI-O runtime. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MP-08

- [ ] **Question:** Production is degraded around Node status/lease; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `journalctl -u kubelet -u containerd --since '-30 min'` plus recent events/changes, then correlate the service-specific SLI. kubelet heartbeat and conditions drive availability/eviction decisions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cloud controller; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. reconciles nodes/routes/load balancers against cloud APIs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SCHEDULER-CONTROLLERS-AND-KUBELET-MP-10

- [ ] **Question:** Production is degraded around Leader election; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get lease -n kube-system` plus recent events/changes, then correlate the service-specific SLI. controllers/schedulers use leases so only active leader mutates shared state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### SCHEDULER-CONTROLLERS-AND-KUBELET-SN-01

- [ ] **Question:** Design a production Scheduler, controllers and kubelet capability where Controller loop, Score plugin and CRI are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: watches desired/observed state and performs level-based idempotent reconciliation. ranks feasible nodes and can favor spread/bin packing/locality. gRPC boundary from kubelet to containerd/CRI-O runtime. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Scheduler, controllers and kubelet capability where Scheduler queue, Binding and Node status/lease are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: unscheduled Pods progress through filtering/scoring/backoff before binding. records selected node in Pod spec after scheduling assumptions/reservations. kubelet heartbeat and conditions drive availability/eviction decisions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SN-03

- [ ] **Question:** Design a production Scheduler, controllers and kubelet capability where Filter plugin, Kubelet Pod sync and Cloud controller are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: rejects nodes that cannot satisfy resources, affinity, taints, topology or volumes. realizes assigned Pod through volume, sandbox, image and container runtime operations. reconciles nodes/routes/load balancers against cloud APIs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Scheduler, controllers and kubelet capability where Score plugin, CRI and Leader election are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ranks feasible nodes and can favor spread/bin packing/locality. gRPC boundary from kubelet to containerd/CRI-O runtime. controllers/schedulers use leases so only active leader mutates shared state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SN-05

- [ ] **Question:** Design a production Scheduler, controllers and kubelet capability where Binding, Node status/lease and Controller loop are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: records selected node in Pod spec after scheduling assumptions/reservations. kubelet heartbeat and conditions drive availability/eviction decisions. watches desired/observed state and performs level-based idempotent reconciliation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Scheduler, controllers and kubelet capability where Kubelet Pod sync, Cloud controller and Scheduler queue are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: realizes assigned Pod through volume, sandbox, image and container runtime operations. reconciles nodes/routes/load balancers against cloud APIs. unscheduled Pods progress through filtering/scoring/backoff before binding. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SN-07

- [ ] **Question:** Design a production Scheduler, controllers and kubelet capability where CRI, Leader election and Filter plugin are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: gRPC boundary from kubelet to containerd/CRI-O runtime. controllers/schedulers use leases so only active leader mutates shared state. rejects nodes that cannot satisfy resources, affinity, taints, topology or volumes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Scheduler, controllers and kubelet capability where Node status/lease, Controller loop and Score plugin are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: kubelet heartbeat and conditions drive availability/eviction decisions. watches desired/observed state and performs level-based idempotent reconciliation. ranks feasible nodes and can favor spread/bin packing/locality. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SN-09

- [ ] **Question:** Design a production Scheduler, controllers and kubelet capability where Cloud controller, Scheduler queue and Binding are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reconciles nodes/routes/load balancers against cloud APIs. unscheduled Pods progress through filtering/scoring/backoff before binding. records selected node in Pod spec after scheduling assumptions/reservations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Scheduler, controllers and kubelet capability where Leader election, Filter plugin and Kubelet Pod sync are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controllers/schedulers use leases so only active leader mutates shared state. rejects nodes that cannot satisfy resources, affinity, taints, topology or volumes. realizes assigned Pod through volume, sandbox, image and container runtime operations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### SCHEDULER-CONTROLLERS-AND-KUBELET-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Controller loop. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. watches desired/observed state and performs level-based idempotent reconciliation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Scheduler queue. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get lease -n kube-system` as one read-only checkpoint, not the whole diagnosis. unscheduled Pods progress through filtering/scoring/backoff before binding. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Filter plugin. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe node NODE` as one read-only checkpoint, not the whole diagnosis. rejects nodes that cannot satisfy resources, affinity, taints, topology or volumes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Score plugin. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `journalctl -u kubelet -u containerd --since '-30 min'` as one read-only checkpoint, not the whole diagnosis. ranks feasible nodes and can favor spread/bin packing/locality. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Binding. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. records selected node in Pod spec after scheduling assumptions/reservations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Kubelet Pod sync. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get lease -n kube-system` as one read-only checkpoint, not the whole diagnosis. realizes assigned Pod through volume, sandbox, image and container runtime operations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CRI. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe node NODE` as one read-only checkpoint, not the whole diagnosis. gRPC boundary from kubelet to containerd/CRI-O runtime. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node status/lease. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `journalctl -u kubelet -u containerd --since '-30 min'` as one read-only checkpoint, not the whole diagnosis. kubelet heartbeat and conditions drive availability/eviction decisions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cloud controller. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. reconciles nodes/routes/load balancers against cloud APIs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SCHEDULER-CONTROLLERS-AND-KUBELET-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Leader election. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get lease -n kube-system` as one read-only checkpoint, not the whole diagnosis. controllers/schedulers use leases so only active leader mutates shared state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
