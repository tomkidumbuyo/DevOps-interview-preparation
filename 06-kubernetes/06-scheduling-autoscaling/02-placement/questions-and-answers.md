# Affinity, taints and topology placement — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JN-01

- [ ] **Question:** What is nodeSelector, and why does it matter in Affinity, taints and topology placement?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** exact label match for simple required placement. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JN-02

- [ ] **Question:** What is Node affinity, and why does it matter in Affinity, taints and topology placement?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** expressive required/preferred label predicates evaluated at scheduling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JN-03

- [ ] **Question:** What is Pod affinity, and why does it matter in Affinity, taints and topology placement?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** co-locates Pods by labels/topology and can be expensive/fragile. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JN-04

- [ ] **Question:** What is Pod anti-affinity, and why does it matter in Affinity, taints and topology placement?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** spreads/fences replicas but hard rules can block during failures. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JN-05

- [ ] **Question:** What is Taint, and why does it matter in Affinity, taints and topology placement?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** repels Pods by NoSchedule/PreferNoSchedule/NoExecute effects. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JN-06

- [ ] **Question:** What is Toleration, and why does it matter in Affinity, taints and topology placement?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** permits but does not require placement on tainted nodes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JN-07

- [ ] **Question:** What is Topology spread, and why does it matter in Affinity, taints and topology placement?
> **Covered in:** [Affinity, taints and topology placement — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** controls skew across zones/nodes using label selector and unsatisfiable behavior. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JN-08

- [ ] **Code:** **Question:** What does `kubectl taint node NODE key=value:NoSchedule` help you verify for Affinity, taints and topology placement?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: PV zone/access constrains feasible nodes after/before binding.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JN-09

- [ ] **Code:** **Question:** What does `kubectl get nodes --show-labels` help you verify for Affinity, taints and topology placement?
> **Covered in:** [Affinity, taints and topology placement — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: topology/arch/os/instance attributes should be trusted and lifecycle-managed.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JN-10

- [ ] **Code:** **Question:** What does `kubectl get events -A --field-selector=reason=FailedScheduling` help you verify for Affinity, taints and topology placement?
> **Covered in:** [Affinity, taints and topology placement — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: scheduler events enumerate failed filters; removing safety constraints blindly is not repair.

## Junior — procedural and command questions

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JP-01

- [ ] **Code:** **Question:** A basic nodeSelector check fails. What would you do first using the CLI?
> **Covered in:** [Affinity, taints and topology placement — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes --show-labels` and capture exact status/reason/request ID. exact label match for simple required placement. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JP-02

- [ ] **Question:** A basic Node affinity check fails. What would you do first?
> **Covered in:** [Affinity, taints and topology placement — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. expressive required/preferred label predicates evaluated at scheduling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JP-03

- [ ] **Question:** A basic Pod affinity check fails. What would you do first?
> **Covered in:** [Affinity, taints and topology placement — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. co-locates Pods by labels/topology and can be expensive/fragile. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JP-04

- [ ] **Code:** **Question:** A basic Pod anti-affinity check fails. What would you do first using the CLI?
> **Covered in:** [Affinity, taints and topology placement — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl taint node NODE key=value:NoSchedule` and capture exact status/reason/request ID. spreads/fences replicas but hard rules can block during failures. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JP-05

- [ ] **Question:** A basic Taint check fails. What would you do first?
> **Covered in:** [Affinity, taints and topology placement — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes --show-labels` and capture exact status/reason/request ID. repels Pods by NoSchedule/PreferNoSchedule/NoExecute effects. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JP-06

- [ ] **Question:** A basic Toleration check fails. What would you do first?
> **Covered in:** [Affinity, taints and topology placement — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. permits but does not require placement on tainted nodes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JP-07

- [ ] **Code:** **Question:** A basic Topology spread check fails. What would you do first using the CLI?
> **Covered in:** [Affinity, taints and topology placement — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. controls skew across zones/nodes using label selector and unsatisfiable behavior. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JP-08

- [ ] **Question:** A basic Volume topology check fails. What would you do first?
> **Covered in:** [Affinity, taints and topology placement — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl taint node NODE key=value:NoSchedule` and capture exact status/reason/request ID. PV zone/access constrains feasible nodes after/before binding. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JP-09

- [ ] **Question:** A basic Well-known labels check fails. What would you do first?
> **Covered in:** [Affinity, taints and topology placement — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes --show-labels` and capture exact status/reason/request ID. topology/arch/os/instance attributes should be trusted and lifecycle-managed. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-JP-10

- [ ] **Code:** **Question:** A basic Constraint diagnosis check fails. What would you do first using the CLI?
> **Covered in:** [Affinity, taints and topology placement — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. scheduler events enumerate failed filters; removing safety constraints blindly is not repair. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MN-01

- [ ] **Question:** Compare nodeSelector with Node affinity. When would each change your design?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** nodeSelector: exact label match for simple required placement. Node affinity: expressive required/preferred label predicates evaluated at scheduling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MN-02

- [ ] **Question:** Compare Node affinity with Pod affinity. When would each change your design?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Node affinity: expressive required/preferred label predicates evaluated at scheduling. Pod affinity: co-locates Pods by labels/topology and can be expensive/fragile. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MN-03

- [ ] **Question:** Compare Pod affinity with Pod anti-affinity. When would each change your design?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Pod affinity: co-locates Pods by labels/topology and can be expensive/fragile. Pod anti-affinity: spreads/fences replicas but hard rules can block during failures. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MN-04

- [ ] **Configuration review:** **Question:** Compare Pod anti-affinity with Taint. When would each change your design?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Pod anti-affinity: spreads/fences replicas but hard rules can block during failures. Taint: repels Pods by NoSchedule/PreferNoSchedule/NoExecute effects. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MN-05

- [ ] **Question:** Compare Taint with Toleration. When would each change your design?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Taint: repels Pods by NoSchedule/PreferNoSchedule/NoExecute effects. Toleration: permits but does not require placement on tainted nodes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MN-06

- [ ] **Question:** Compare Toleration with Topology spread. When would each change your design?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Toleration: permits but does not require placement on tainted nodes. Topology spread: controls skew across zones/nodes using label selector and unsatisfiable behavior. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MN-07

- [ ] **Configuration review:** **Question:** Compare Topology spread with Volume topology. When would each change your design?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Topology spread: controls skew across zones/nodes using label selector and unsatisfiable behavior. Volume topology: PV zone/access constrains feasible nodes after/before binding. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MN-08

- [ ] **Question:** Compare Volume topology with Well-known labels. When would each change your design?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Volume topology: PV zone/access constrains feasible nodes after/before binding. Well-known labels: topology/arch/os/instance attributes should be trusted and lifecycle-managed. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MN-09

- [ ] **Question:** Compare Well-known labels with Constraint diagnosis. When would each change your design?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Well-known labels: topology/arch/os/instance attributes should be trusted and lifecycle-managed. Constraint diagnosis: scheduler events enumerate failed filters; removing safety constraints blindly is not repair. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MN-10

- [ ] **Configuration review:** **Question:** Compare Constraint diagnosis with nodeSelector. When would each change your design?
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Constraint diagnosis: scheduler events enumerate failed filters; removing safety constraints blindly is not repair. nodeSelector: exact label match for simple required placement. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around nodeSelector; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes --show-labels` plus recent events/changes, then correlate the service-specific SLI. exact label match for simple required placement. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MP-02

- [ ] **Question:** Production is degraded around Node affinity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. expressive required/preferred label predicates evaluated at scheduling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pod affinity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. co-locates Pods by labels/topology and can be expensive/fragile. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MP-04

- [ ] **Question:** Production is degraded around Pod anti-affinity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl taint node NODE key=value:NoSchedule` plus recent events/changes, then correlate the service-specific SLI. spreads/fences replicas but hard rules can block during failures. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Taint; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes --show-labels` plus recent events/changes, then correlate the service-specific SLI. repels Pods by NoSchedule/PreferNoSchedule/NoExecute effects. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MP-06

- [ ] **Question:** Production is degraded around Toleration; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. permits but does not require placement on tainted nodes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Topology spread; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. controls skew across zones/nodes using label selector and unsatisfiable behavior. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MP-08

- [ ] **Question:** Production is degraded around Volume topology; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl taint node NODE key=value:NoSchedule` plus recent events/changes, then correlate the service-specific SLI. PV zone/access constrains feasible nodes after/before binding. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Well-known labels; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes --show-labels` plus recent events/changes, then correlate the service-specific SLI. topology/arch/os/instance attributes should be trusted and lifecycle-managed. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-MP-10

- [ ] **Question:** Production is degraded around Constraint diagnosis; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. scheduler events enumerate failed filters; removing safety constraints blindly is not repair. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SN-01

- [ ] **Question:** Design a production Affinity, taints and topology placement capability where nodeSelector, Pod anti-affinity and Topology spread are first-class requirements.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exact label match for simple required placement. spreads/fences replicas but hard rules can block during failures. controls skew across zones/nodes using label selector and unsatisfiable behavior. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Affinity, taints and topology placement capability where Node affinity, Taint and Volume topology are first-class requirements.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: expressive required/preferred label predicates evaluated at scheduling. repels Pods by NoSchedule/PreferNoSchedule/NoExecute effects. PV zone/access constrains feasible nodes after/before binding. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SN-03

- [ ] **Question:** Design a production Affinity, taints and topology placement capability where Pod affinity, Toleration and Well-known labels are first-class requirements.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: co-locates Pods by labels/topology and can be expensive/fragile. permits but does not require placement on tainted nodes. topology/arch/os/instance attributes should be trusted and lifecycle-managed. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Affinity, taints and topology placement capability where Pod anti-affinity, Topology spread and Constraint diagnosis are first-class requirements.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: spreads/fences replicas but hard rules can block during failures. controls skew across zones/nodes using label selector and unsatisfiable behavior. scheduler events enumerate failed filters; removing safety constraints blindly is not repair. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SN-05

- [ ] **Question:** Design a production Affinity, taints and topology placement capability where Taint, Volume topology and nodeSelector are first-class requirements.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: repels Pods by NoSchedule/PreferNoSchedule/NoExecute effects. PV zone/access constrains feasible nodes after/before binding. exact label match for simple required placement. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Affinity, taints and topology placement capability where Toleration, Well-known labels and Node affinity are first-class requirements.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: permits but does not require placement on tainted nodes. topology/arch/os/instance attributes should be trusted and lifecycle-managed. expressive required/preferred label predicates evaluated at scheduling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SN-07

- [ ] **Question:** Design a production Affinity, taints and topology placement capability where Topology spread, Constraint diagnosis and Pod affinity are first-class requirements.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controls skew across zones/nodes using label selector and unsatisfiable behavior. scheduler events enumerate failed filters; removing safety constraints blindly is not repair. co-locates Pods by labels/topology and can be expensive/fragile. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Affinity, taints and topology placement capability where Volume topology, nodeSelector and Pod anti-affinity are first-class requirements.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: PV zone/access constrains feasible nodes after/before binding. exact label match for simple required placement. spreads/fences replicas but hard rules can block during failures. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SN-09

- [ ] **Question:** Design a production Affinity, taints and topology placement capability where Well-known labels, Node affinity and Taint are first-class requirements.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: topology/arch/os/instance attributes should be trusted and lifecycle-managed. expressive required/preferred label predicates evaluated at scheduling. repels Pods by NoSchedule/PreferNoSchedule/NoExecute effects. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Affinity, taints and topology placement capability where Constraint diagnosis, Pod affinity and Toleration are first-class requirements.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scheduler events enumerate failed filters; removing safety constraints blindly is not repair. co-locates Pods by labels/topology and can be expensive/fragile. permits but does not require placement on tainted nodes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving nodeSelector. How do you lead it end to end?
> **Covered in:** [Affinity, taints and topology placement — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes --show-labels` as one read-only checkpoint, not the whole diagnosis. exact label match for simple required placement. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node affinity. How do you lead it end to end?
> **Covered in:** [Affinity, taints and topology placement — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. expressive required/preferred label predicates evaluated at scheduling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod affinity. How do you lead it end to end?
> **Covered in:** [Affinity, taints and topology placement — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. co-locates Pods by labels/topology and can be expensive/fragile. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod anti-affinity. How do you lead it end to end?
> **Covered in:** [Affinity, taints and topology placement — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl taint node NODE key=value:NoSchedule` as one read-only checkpoint, not the whole diagnosis. spreads/fences replicas but hard rules can block during failures. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Taint. How do you lead it end to end?
> **Covered in:** [Affinity, taints and topology placement — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes --show-labels` as one read-only checkpoint, not the whole diagnosis. repels Pods by NoSchedule/PreferNoSchedule/NoExecute effects. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Toleration. How do you lead it end to end?
> **Covered in:** [Affinity, taints and topology placement — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. permits but does not require placement on tainted nodes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Topology spread. How do you lead it end to end?
> **Covered in:** [Affinity, taints and topology placement — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. controls skew across zones/nodes using label selector and unsatisfiable behavior. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Volume topology. How do you lead it end to end?
> **Covered in:** [Affinity, taints and topology placement — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl taint node NODE key=value:NoSchedule` as one read-only checkpoint, not the whole diagnosis. PV zone/access constrains feasible nodes after/before binding. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Well-known labels. How do you lead it end to end?
> **Covered in:** [Affinity, taints and topology placement — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes --show-labels` as one read-only checkpoint, not the whole diagnosis. topology/arch/os/instance attributes should be trusted and lifecycle-managed. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AFFINITY-TAINTS-AND-TOPOLOGY-PLACEMENT-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Constraint diagnosis. How do you lead it end to end?
> **Covered in:** [Affinity, taints and topology placement — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. scheduler events enumerate failed filters; removing safety constraints blindly is not repair. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Resource requests, limits and QoS](../01-requests-limits-qos/README.md) · [Study note](README.md) · [Next: HPA, VPA and KEDA →](../03-hpa-vpa-keda/README.md)

<!-- reading-navigation:end -->
