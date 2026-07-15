# StatefulSets and DaemonSets — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### STATEFULSETS-AND-DAEMONSETS-JN-01

- [ ] **Question:** What is Stateful ordinal, and why does it matter in StatefulSets and DaemonSets?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** stable Pod name/identity persists across rescheduling but not physical node. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### STATEFULSETS-AND-DAEMONSETS-JN-02

- [ ] **Question:** What is Headless Service, and why does it matter in StatefulSets and DaemonSets?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** publishes per-Pod DNS identity for StatefulSet membership. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### STATEFULSETS-AND-DAEMONSETS-JN-03

- [ ] **Question:** What is VolumeClaimTemplate, and why does it matter in StatefulSets and DaemonSets?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** creates stable per-ordinal PVCs that are not automatically deleted by default semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### STATEFULSETS-AND-DAEMONSETS-JN-04

- [ ] **Question:** What is OrderedReady, and why does it matter in StatefulSets and DaemonSets?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** sequential create/update assumes application readiness and can deadlock bad clusters. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### STATEFULSETS-AND-DAEMONSETS-JN-05

- [ ] **Question:** What is Partitioned update, and why does it matter in StatefulSets and DaemonSets?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** rolls only selected ordinals for canary/manual control. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### STATEFULSETS-AND-DAEMONSETS-JN-06

- [ ] **Question:** What is State replication, and why does it matter in StatefulSets and DaemonSets?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** application/database must implement quorum/failover; StatefulSet does not. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### STATEFULSETS-AND-DAEMONSETS-JN-07

- [ ] **Question:** What is DaemonSet eligibility, and why does it matter in StatefulSets and DaemonSets?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** runs on every matching node and tolerates common node conditions through controller defaults. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### STATEFULSETS-AND-DAEMONSETS-JN-08

- [ ] **Code:** **Question:** What does `kubectl get pvc -n NS -l app=NAME` help you verify for StatefulSets and DaemonSets?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: maxUnavailable/surge support varies by strategy/version and affects node agent coverage.

### STATEFULSETS-AND-DAEMONSETS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get statefulset,daemonset -A` help you verify for StatefulSets and DaemonSets?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: CNI/storage/log/GPU DaemonSets need priority/resources and upgrade ordering.

### STATEFULSETS-AND-DAEMONSETS-JN-10

- [ ] **Code:** **Question:** What does `kubectl rollout status statefulset/NAME -n NS` help you verify for StatefulSets and DaemonSets?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: DaemonSet Pods are ignored/recreated, while stateful eviction must respect PDB/storage.

## Junior — procedural and command questions

### STATEFULSETS-AND-DAEMONSETS-JP-01

- [ ] **Code:** **Question:** A basic Stateful ordinal check fails. What would you do first using the CLI?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get statefulset,daemonset -A` and capture exact status/reason/request ID. stable Pod name/identity persists across rescheduling but not physical node. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### STATEFULSETS-AND-DAEMONSETS-JP-02

- [ ] **Question:** A basic Headless Service check fails. What would you do first?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status statefulset/NAME -n NS` and capture exact status/reason/request ID. publishes per-Pod DNS identity for StatefulSet membership. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### STATEFULSETS-AND-DAEMONSETS-JP-03

- [ ] **Question:** A basic VolumeClaimTemplate check fails. What would you do first?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status daemonset/NAME -n NS` and capture exact status/reason/request ID. creates stable per-ordinal PVCs that are not automatically deleted by default semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### STATEFULSETS-AND-DAEMONSETS-JP-04

- [ ] **Code:** **Question:** A basic OrderedReady check fails. What would you do first using the CLI?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pvc -n NS -l app=NAME` and capture exact status/reason/request ID. sequential create/update assumes application readiness and can deadlock bad clusters. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### STATEFULSETS-AND-DAEMONSETS-JP-05

- [ ] **Question:** A basic Partitioned update check fails. What would you do first?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get statefulset,daemonset -A` and capture exact status/reason/request ID. rolls only selected ordinals for canary/manual control. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### STATEFULSETS-AND-DAEMONSETS-JP-06

- [ ] **Question:** A basic State replication check fails. What would you do first?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status statefulset/NAME -n NS` and capture exact status/reason/request ID. application/database must implement quorum/failover; StatefulSet does not. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### STATEFULSETS-AND-DAEMONSETS-JP-07

- [ ] **Code:** **Question:** A basic DaemonSet eligibility check fails. What would you do first using the CLI?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status daemonset/NAME -n NS` and capture exact status/reason/request ID. runs on every matching node and tolerates common node conditions through controller defaults. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### STATEFULSETS-AND-DAEMONSETS-JP-08

- [ ] **Question:** A basic DaemonSet rollout check fails. What would you do first?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pvc -n NS -l app=NAME` and capture exact status/reason/request ID. maxUnavailable/surge support varies by strategy/version and affects node agent coverage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### STATEFULSETS-AND-DAEMONSETS-JP-09

- [ ] **Question:** A basic Critical agents check fails. What would you do first?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get statefulset,daemonset -A` and capture exact status/reason/request ID. CNI/storage/log/GPU DaemonSets need priority/resources and upgrade ordering. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### STATEFULSETS-AND-DAEMONSETS-JP-10

- [ ] **Code:** **Question:** A basic Node drain check fails. What would you do first using the CLI?
> **Covered in:** [StatefulSets and DaemonSets — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status statefulset/NAME -n NS` and capture exact status/reason/request ID. DaemonSet Pods are ignored/recreated, while stateful eviction must respect PDB/storage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### STATEFULSETS-AND-DAEMONSETS-MN-01

- [ ] **Question:** Compare Stateful ordinal with Headless Service. When would each change your design?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Stateful ordinal: stable Pod name/identity persists across rescheduling but not physical node. Headless Service: publishes per-Pod DNS identity for StatefulSet membership. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### STATEFULSETS-AND-DAEMONSETS-MN-02

- [ ] **Question:** Compare Headless Service with VolumeClaimTemplate. When would each change your design?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Headless Service: publishes per-Pod DNS identity for StatefulSet membership. VolumeClaimTemplate: creates stable per-ordinal PVCs that are not automatically deleted by default semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### STATEFULSETS-AND-DAEMONSETS-MN-03

- [ ] **Question:** Compare VolumeClaimTemplate with OrderedReady. When would each change your design?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** VolumeClaimTemplate: creates stable per-ordinal PVCs that are not automatically deleted by default semantics. OrderedReady: sequential create/update assumes application readiness and can deadlock bad clusters. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### STATEFULSETS-AND-DAEMONSETS-MN-04

- [ ] **Configuration review:** **Question:** Compare OrderedReady with Partitioned update. When would each change your design?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** OrderedReady: sequential create/update assumes application readiness and can deadlock bad clusters. Partitioned update: rolls only selected ordinals for canary/manual control. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### STATEFULSETS-AND-DAEMONSETS-MN-05

- [ ] **Question:** Compare Partitioned update with State replication. When would each change your design?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Partitioned update: rolls only selected ordinals for canary/manual control. State replication: application/database must implement quorum/failover; StatefulSet does not. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### STATEFULSETS-AND-DAEMONSETS-MN-06

- [ ] **Question:** Compare State replication with DaemonSet eligibility. When would each change your design?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** State replication: application/database must implement quorum/failover; StatefulSet does not. DaemonSet eligibility: runs on every matching node and tolerates common node conditions through controller defaults. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### STATEFULSETS-AND-DAEMONSETS-MN-07

- [ ] **Configuration review:** **Question:** Compare DaemonSet eligibility with DaemonSet rollout. When would each change your design?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** DaemonSet eligibility: runs on every matching node and tolerates common node conditions through controller defaults. DaemonSet rollout: maxUnavailable/surge support varies by strategy/version and affects node agent coverage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### STATEFULSETS-AND-DAEMONSETS-MN-08

- [ ] **Question:** Compare DaemonSet rollout with Critical agents. When would each change your design?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** DaemonSet rollout: maxUnavailable/surge support varies by strategy/version and affects node agent coverage. Critical agents: CNI/storage/log/GPU DaemonSets need priority/resources and upgrade ordering. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### STATEFULSETS-AND-DAEMONSETS-MN-09

- [ ] **Question:** Compare Critical agents with Node drain. When would each change your design?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Critical agents: CNI/storage/log/GPU DaemonSets need priority/resources and upgrade ordering. Node drain: DaemonSet Pods are ignored/recreated, while stateful eviction must respect PDB/storage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### STATEFULSETS-AND-DAEMONSETS-MN-10

- [ ] **Configuration review:** **Question:** Compare Node drain with Stateful ordinal. When would each change your design?
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Node drain: DaemonSet Pods are ignored/recreated, while stateful eviction must respect PDB/storage. Stateful ordinal: stable Pod name/identity persists across rescheduling but not physical node. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### STATEFULSETS-AND-DAEMONSETS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Stateful ordinal; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get statefulset,daemonset -A` plus recent events/changes, then correlate the service-specific SLI. stable Pod name/identity persists across rescheduling but not physical node. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### STATEFULSETS-AND-DAEMONSETS-MP-02

- [ ] **Question:** Production is degraded around Headless Service; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status statefulset/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. publishes per-Pod DNS identity for StatefulSet membership. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### STATEFULSETS-AND-DAEMONSETS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around VolumeClaimTemplate; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status daemonset/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. creates stable per-ordinal PVCs that are not automatically deleted by default semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### STATEFULSETS-AND-DAEMONSETS-MP-04

- [ ] **Question:** Production is degraded around OrderedReady; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pvc -n NS -l app=NAME` plus recent events/changes, then correlate the service-specific SLI. sequential create/update assumes application readiness and can deadlock bad clusters. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### STATEFULSETS-AND-DAEMONSETS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Partitioned update; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get statefulset,daemonset -A` plus recent events/changes, then correlate the service-specific SLI. rolls only selected ordinals for canary/manual control. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### STATEFULSETS-AND-DAEMONSETS-MP-06

- [ ] **Question:** Production is degraded around State replication; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status statefulset/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. application/database must implement quorum/failover; StatefulSet does not. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### STATEFULSETS-AND-DAEMONSETS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around DaemonSet eligibility; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status daemonset/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. runs on every matching node and tolerates common node conditions through controller defaults. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### STATEFULSETS-AND-DAEMONSETS-MP-08

- [ ] **Question:** Production is degraded around DaemonSet rollout; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pvc -n NS -l app=NAME` plus recent events/changes, then correlate the service-specific SLI. maxUnavailable/surge support varies by strategy/version and affects node agent coverage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### STATEFULSETS-AND-DAEMONSETS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Critical agents; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get statefulset,daemonset -A` plus recent events/changes, then correlate the service-specific SLI. CNI/storage/log/GPU DaemonSets need priority/resources and upgrade ordering. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### STATEFULSETS-AND-DAEMONSETS-MP-10

- [ ] **Question:** Production is degraded around Node drain; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status statefulset/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. DaemonSet Pods are ignored/recreated, while stateful eviction must respect PDB/storage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### STATEFULSETS-AND-DAEMONSETS-SN-01

- [ ] **Question:** Design a production StatefulSets and DaemonSets capability where Stateful ordinal, OrderedReady and DaemonSet eligibility are first-class requirements.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stable Pod name/identity persists across rescheduling but not physical node. sequential create/update assumes application readiness and can deadlock bad clusters. runs on every matching node and tolerates common node conditions through controller defaults. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### STATEFULSETS-AND-DAEMONSETS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production StatefulSets and DaemonSets capability where Headless Service, Partitioned update and DaemonSet rollout are first-class requirements.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: publishes per-Pod DNS identity for StatefulSet membership. rolls only selected ordinals for canary/manual control. maxUnavailable/surge support varies by strategy/version and affects node agent coverage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### STATEFULSETS-AND-DAEMONSETS-SN-03

- [ ] **Question:** Design a production StatefulSets and DaemonSets capability where VolumeClaimTemplate, State replication and Critical agents are first-class requirements.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: creates stable per-ordinal PVCs that are not automatically deleted by default semantics. application/database must implement quorum/failover; StatefulSet does not. CNI/storage/log/GPU DaemonSets need priority/resources and upgrade ordering. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### STATEFULSETS-AND-DAEMONSETS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production StatefulSets and DaemonSets capability where OrderedReady, DaemonSet eligibility and Node drain are first-class requirements.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: sequential create/update assumes application readiness and can deadlock bad clusters. runs on every matching node and tolerates common node conditions through controller defaults. DaemonSet Pods are ignored/recreated, while stateful eviction must respect PDB/storage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### STATEFULSETS-AND-DAEMONSETS-SN-05

- [ ] **Question:** Design a production StatefulSets and DaemonSets capability where Partitioned update, DaemonSet rollout and Stateful ordinal are first-class requirements.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: rolls only selected ordinals for canary/manual control. maxUnavailable/surge support varies by strategy/version and affects node agent coverage. stable Pod name/identity persists across rescheduling but not physical node. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### STATEFULSETS-AND-DAEMONSETS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production StatefulSets and DaemonSets capability where State replication, Critical agents and Headless Service are first-class requirements.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: application/database must implement quorum/failover; StatefulSet does not. CNI/storage/log/GPU DaemonSets need priority/resources and upgrade ordering. publishes per-Pod DNS identity for StatefulSet membership. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### STATEFULSETS-AND-DAEMONSETS-SN-07

- [ ] **Question:** Design a production StatefulSets and DaemonSets capability where DaemonSet eligibility, Node drain and VolumeClaimTemplate are first-class requirements.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: runs on every matching node and tolerates common node conditions through controller defaults. DaemonSet Pods are ignored/recreated, while stateful eviction must respect PDB/storage. creates stable per-ordinal PVCs that are not automatically deleted by default semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### STATEFULSETS-AND-DAEMONSETS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production StatefulSets and DaemonSets capability where DaemonSet rollout, Stateful ordinal and OrderedReady are first-class requirements.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: maxUnavailable/surge support varies by strategy/version and affects node agent coverage. stable Pod name/identity persists across rescheduling but not physical node. sequential create/update assumes application readiness and can deadlock bad clusters. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### STATEFULSETS-AND-DAEMONSETS-SN-09

- [ ] **Question:** Design a production StatefulSets and DaemonSets capability where Critical agents, Headless Service and Partitioned update are first-class requirements.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: CNI/storage/log/GPU DaemonSets need priority/resources and upgrade ordering. publishes per-Pod DNS identity for StatefulSet membership. rolls only selected ordinals for canary/manual control. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### STATEFULSETS-AND-DAEMONSETS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production StatefulSets and DaemonSets capability where Node drain, VolumeClaimTemplate and State replication are first-class requirements.
> **Covered in:** [StatefulSets and DaemonSets — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: DaemonSet Pods are ignored/recreated, while stateful eviction must respect PDB/storage. creates stable per-ordinal PVCs that are not automatically deleted by default semantics. application/database must implement quorum/failover; StatefulSet does not. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### STATEFULSETS-AND-DAEMONSETS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stateful ordinal. How do you lead it end to end?
> **Covered in:** [StatefulSets and DaemonSets — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get statefulset,daemonset -A` as one read-only checkpoint, not the whole diagnosis. stable Pod name/identity persists across rescheduling but not physical node. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### STATEFULSETS-AND-DAEMONSETS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Headless Service. How do you lead it end to end?
> **Covered in:** [StatefulSets and DaemonSets — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status statefulset/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. publishes per-Pod DNS identity for StatefulSet membership. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### STATEFULSETS-AND-DAEMONSETS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VolumeClaimTemplate. How do you lead it end to end?
> **Covered in:** [StatefulSets and DaemonSets — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status daemonset/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. creates stable per-ordinal PVCs that are not automatically deleted by default semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### STATEFULSETS-AND-DAEMONSETS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving OrderedReady. How do you lead it end to end?
> **Covered in:** [StatefulSets and DaemonSets — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pvc -n NS -l app=NAME` as one read-only checkpoint, not the whole diagnosis. sequential create/update assumes application readiness and can deadlock bad clusters. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### STATEFULSETS-AND-DAEMONSETS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Partitioned update. How do you lead it end to end?
> **Covered in:** [StatefulSets and DaemonSets — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get statefulset,daemonset -A` as one read-only checkpoint, not the whole diagnosis. rolls only selected ordinals for canary/manual control. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### STATEFULSETS-AND-DAEMONSETS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving State replication. How do you lead it end to end?
> **Covered in:** [StatefulSets and DaemonSets — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status statefulset/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. application/database must implement quorum/failover; StatefulSet does not. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### STATEFULSETS-AND-DAEMONSETS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DaemonSet eligibility. How do you lead it end to end?
> **Covered in:** [StatefulSets and DaemonSets — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status daemonset/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. runs on every matching node and tolerates common node conditions through controller defaults. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### STATEFULSETS-AND-DAEMONSETS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DaemonSet rollout. How do you lead it end to end?
> **Covered in:** [StatefulSets and DaemonSets — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pvc -n NS -l app=NAME` as one read-only checkpoint, not the whole diagnosis. maxUnavailable/surge support varies by strategy/version and affects node agent coverage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### STATEFULSETS-AND-DAEMONSETS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Critical agents. How do you lead it end to end?
> **Covered in:** [StatefulSets and DaemonSets — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get statefulset,daemonset -A` as one read-only checkpoint, not the whole diagnosis. CNI/storage/log/GPU DaemonSets need priority/resources and upgrade ordering. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### STATEFULSETS-AND-DAEMONSETS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node drain. How do you lead it end to end?
> **Covered in:** [StatefulSets and DaemonSets — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status statefulset/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. DaemonSet Pods are ignored/recreated, while stateful eviction must respect PDB/storage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Deployments and ReplicaSets](../02-deployments/README.md) · [Study note](README.md) · [Next: Jobs and CronJobs →](../04-jobs-cronjobs/README.md)

<!-- reading-navigation:end -->
