# Operations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-OPERATIONS-JN-01

- [ ] **Question:** What is kube-state-metrics, and why does it matter in Operations?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** exposes object desired/status metrics rather than container usage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-OPERATIONS-JN-02

- [ ] **Question:** What is Metrics Server, and why does it matter in Operations?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** lightweight resource metrics for top/HPA, not a long-term monitoring backend. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-OPERATIONS-JN-03

- [ ] **Question:** What is Version skew, and why does it matter in Operations?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-OPERATIONS-JN-04

- [ ] **Question:** What is API deprecation, and why does it matter in Operations?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** served versions are removed on schedule and manifests/clients/controllers must migrate. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-OPERATIONS-JN-05

- [ ] **Question:** What is etcd snapshot, and why does it matter in Operations?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** captures API storage for self-managed control planes with matching encryption/config needs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-OPERATIONS-JN-06

- [ ] **Question:** What is Resource backup, and why does it matter in Operations?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** exported API objects need CRDs, versions, ownership and secret protection. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-OPERATIONS-JN-07

- [ ] **Question:** What is Object status/conditions, and why does it matter in Operations?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** observedGeneration, reason and message show controller interpretation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-OPERATIONS-JN-08

- [ ] **Code:** **Question:** What does `kubectl describe pod POD -n NS` help you verify for Operations?
> **Covered in:** [Operations — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: scheduling, pull, mount, probe and controller records point to the first failing transition.

### BRANCH-OPERATIONS-JN-09

- [ ] **Code:** **Question:** What does `kubectl top node && kubectl top pod -A --containers` help you verify for Operations?
> **Covered in:** [Operations — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: exposes object desired/status metrics rather than container usage.

### BRANCH-OPERATIONS-JN-10

- [ ] **Code:** **Question:** What does `kubectl version` help you verify for Operations?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: lightweight resource metrics for top/HPA, not a long-term monitoring backend.

## Junior — procedural and command questions

### BRANCH-OPERATIONS-JP-01

- [ ] **Code:** **Question:** A basic kube-state-metrics check fails. What would you do first using the CLI?
> **Covered in:** [Operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top node && kubectl top pod -A --containers` and capture exact status/reason/request ID. exposes object desired/status metrics rather than container usage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-OPERATIONS-JP-02

- [ ] **Question:** A basic Metrics Server check fails. What would you do first?
> **Covered in:** [Kubernetes observability — Command lab](01-observability/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl version` and capture exact status/reason/request ID. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-OPERATIONS-JP-03

- [ ] **Question:** A basic Version skew check fails. What would you do first?
> **Covered in:** [Operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` and capture exact status/reason/request ID. supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-OPERATIONS-JP-04

- [ ] **Code:** **Question:** A basic API deprecation check fails. What would you do first using the CLI?
> **Covered in:** [Operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. served versions are removed on schedule and manifests/clients/controllers must migrate. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-OPERATIONS-JP-05

- [ ] **Question:** A basic etcd snapshot check fails. What would you do first?
> **Covered in:** [Operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top node && kubectl top pod -A --containers` and capture exact status/reason/request ID. captures API storage for self-managed control planes with matching encryption/config needs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-OPERATIONS-JP-06

- [ ] **Question:** A basic Resource backup check fails. What would you do first?
> **Covered in:** [Kubernetes backup and disaster recovery — Command lab](03-backup-dr-etcd/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl version` and capture exact status/reason/request ID. exported API objects need CRDs, versions, ownership and secret protection. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-OPERATIONS-JP-07

- [ ] **Code:** **Question:** A basic Object status/conditions check fails. What would you do first using the CLI?
> **Covered in:** [Operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` and capture exact status/reason/request ID. observedGeneration, reason and message show controller interpretation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-OPERATIONS-JP-08

- [ ] **Question:** A basic Events check fails. What would you do first?
> **Covered in:** [Kubernetes observability — Command lab](01-observability/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. scheduling, pull, mount, probe and controller records point to the first failing transition. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-OPERATIONS-JP-09

- [ ] **Question:** A basic kube-state-metrics check fails. What would you do first?
> **Covered in:** [Operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top node && kubectl top pod -A --containers` and capture exact status/reason/request ID. exposes object desired/status metrics rather than container usage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-OPERATIONS-JP-10

- [ ] **Code:** **Question:** A basic Metrics Server check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes observability — Command lab](01-observability/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl version` and capture exact status/reason/request ID. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-OPERATIONS-MN-01

- [ ] **Question:** Compare kube-state-metrics with Metrics Server. When would each change your design?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** kube-state-metrics: exposes object desired/status metrics rather than container usage. Metrics Server: lightweight resource metrics for top/HPA, not a long-term monitoring backend. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-OPERATIONS-MN-02

- [ ] **Question:** Compare Metrics Server with Version skew. When would each change your design?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Metrics Server: lightweight resource metrics for top/HPA, not a long-term monitoring backend. Version skew: supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-OPERATIONS-MN-03

- [ ] **Question:** Compare Version skew with API deprecation. When would each change your design?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Version skew: supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. API deprecation: served versions are removed on schedule and manifests/clients/controllers must migrate. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-OPERATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare API deprecation with etcd snapshot. When would each change your design?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** API deprecation: served versions are removed on schedule and manifests/clients/controllers must migrate. etcd snapshot: captures API storage for self-managed control planes with matching encryption/config needs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-OPERATIONS-MN-05

- [ ] **Question:** Compare etcd snapshot with Resource backup. When would each change your design?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** etcd snapshot: captures API storage for self-managed control planes with matching encryption/config needs. Resource backup: exported API objects need CRDs, versions, ownership and secret protection. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-OPERATIONS-MN-06

- [ ] **Question:** Compare Resource backup with Object status/conditions. When would each change your design?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Resource backup: exported API objects need CRDs, versions, ownership and secret protection. Object status/conditions: observedGeneration, reason and message show controller interpretation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-OPERATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Object status/conditions with Events. When would each change your design?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Object status/conditions: observedGeneration, reason and message show controller interpretation. Events: scheduling, pull, mount, probe and controller records point to the first failing transition. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-OPERATIONS-MN-08

- [ ] **Question:** Compare Events with kube-state-metrics. When would each change your design?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Events: scheduling, pull, mount, probe and controller records point to the first failing transition. kube-state-metrics: exposes object desired/status metrics rather than container usage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-OPERATIONS-MN-09

- [ ] **Question:** Compare kube-state-metrics with Metrics Server. When would each change your design?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** kube-state-metrics: exposes object desired/status metrics rather than container usage. Metrics Server: lightweight resource metrics for top/HPA, not a long-term monitoring backend. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-OPERATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Metrics Server with kube-state-metrics. When would each change your design?
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Metrics Server: lightweight resource metrics for top/HPA, not a long-term monitoring backend. kube-state-metrics: exposes object desired/status metrics rather than container usage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-OPERATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around kube-state-metrics; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top node && kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. exposes object desired/status metrics rather than container usage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-OPERATIONS-MP-02

- [ ] **Question:** Production is degraded around Metrics Server; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl version` plus recent events/changes, then correlate the service-specific SLI. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-OPERATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Version skew; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` plus recent events/changes, then correlate the service-specific SLI. supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-OPERATIONS-MP-04

- [ ] **Question:** Production is degraded around API deprecation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. served versions are removed on schedule and manifests/clients/controllers must migrate. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-OPERATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around etcd snapshot; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top node && kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. captures API storage for self-managed control planes with matching encryption/config needs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-OPERATIONS-MP-06

- [ ] **Question:** Production is degraded around Resource backup; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl version` plus recent events/changes, then correlate the service-specific SLI. exported API objects need CRDs, versions, ownership and secret protection. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-OPERATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Object status/conditions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes troubleshooting and kubectl — Detailed learning notes](04-troubleshooting-kubectl/README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` plus recent events/changes, then correlate the service-specific SLI. observedGeneration, reason and message show controller interpretation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-OPERATIONS-MP-08

- [ ] **Question:** Production is degraded around Events; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes troubleshooting and kubectl — Detailed learning notes](04-troubleshooting-kubectl/README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. scheduling, pull, mount, probe and controller records point to the first failing transition. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-OPERATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around kube-state-metrics; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top node && kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. exposes object desired/status metrics rather than container usage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-OPERATIONS-MP-10

- [ ] **Question:** Production is degraded around Metrics Server; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl version` plus recent events/changes, then correlate the service-specific SLI. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-OPERATIONS-SN-01

- [ ] **Question:** Design a production Operations capability where kube-state-metrics, API deprecation and Object status/conditions are first-class requirements.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exposes object desired/status metrics rather than container usage. served versions are removed on schedule and manifests/clients/controllers must migrate. observedGeneration, reason and message show controller interpretation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-OPERATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Operations capability where Metrics Server, etcd snapshot and Events are first-class requirements.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: lightweight resource metrics for top/HPA, not a long-term monitoring backend. captures API storage for self-managed control planes with matching encryption/config needs. scheduling, pull, mount, probe and controller records point to the first failing transition. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-OPERATIONS-SN-03

- [ ] **Question:** Design a production Operations capability where Version skew, Resource backup and kube-state-metrics are first-class requirements.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. exported API objects need CRDs, versions, ownership and secret protection. exposes object desired/status metrics rather than container usage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-OPERATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Operations capability where API deprecation, Object status/conditions and Metrics Server are first-class requirements.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: served versions are removed on schedule and manifests/clients/controllers must migrate. observedGeneration, reason and message show controller interpretation. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-OPERATIONS-SN-05

- [ ] **Question:** Design a production Operations capability where etcd snapshot, Events and kube-state-metrics are first-class requirements.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: captures API storage for self-managed control planes with matching encryption/config needs. scheduling, pull, mount, probe and controller records point to the first failing transition. exposes object desired/status metrics rather than container usage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-OPERATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Operations capability where Resource backup, kube-state-metrics and Metrics Server are first-class requirements.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exported API objects need CRDs, versions, ownership and secret protection. exposes object desired/status metrics rather than container usage. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-OPERATIONS-SN-07

- [ ] **Question:** Design a production Operations capability where Object status/conditions, Metrics Server and Version skew are first-class requirements.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: observedGeneration, reason and message show controller interpretation. lightweight resource metrics for top/HPA, not a long-term monitoring backend. supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-OPERATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Operations capability where Events, kube-state-metrics and API deprecation are first-class requirements.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scheduling, pull, mount, probe and controller records point to the first failing transition. exposes object desired/status metrics rather than container usage. served versions are removed on schedule and manifests/clients/controllers must migrate. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-OPERATIONS-SN-09

- [ ] **Question:** Design a production Operations capability where kube-state-metrics, Metrics Server and etcd snapshot are first-class requirements.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exposes object desired/status metrics rather than container usage. lightweight resource metrics for top/HPA, not a long-term monitoring backend. captures API storage for self-managed control planes with matching encryption/config needs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-OPERATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Operations capability where Metrics Server, Version skew and Resource backup are first-class requirements.
> **Covered in:** [Operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: lightweight resource metrics for top/HPA, not a long-term monitoring backend. supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. exported API objects need CRDs, versions, ownership and secret protection. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-OPERATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving kube-state-metrics. How do you lead it end to end?
> **Covered in:** [Operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top node && kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. exposes object desired/status metrics rather than container usage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-OPERATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Metrics Server. How do you lead it end to end?
> **Covered in:** [Operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl version` as one read-only checkpoint, not the whole diagnosis. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-OPERATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Version skew. How do you lead it end to end?
> **Covered in:** [Operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` as one read-only checkpoint, not the whole diagnosis. supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-OPERATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving API deprecation. How do you lead it end to end?
> **Covered in:** [Operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. served versions are removed on schedule and manifests/clients/controllers must migrate. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-OPERATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving etcd snapshot. How do you lead it end to end?
> **Covered in:** [Operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top node && kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. captures API storage for self-managed control planes with matching encryption/config needs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-OPERATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource backup. How do you lead it end to end?
> **Covered in:** [Operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl version` as one read-only checkpoint, not the whole diagnosis. exported API objects need CRDs, versions, ownership and secret protection. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-OPERATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Object status/conditions. How do you lead it end to end?
> **Covered in:** [Operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ETCDCTL_API=3 etcdctl snapshot save snapshot.db` as one read-only checkpoint, not the whole diagnosis. observedGeneration, reason and message show controller interpretation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-OPERATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Events. How do you lead it end to end?
> **Covered in:** [Operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. scheduling, pull, mount, probe and controller records point to the first failing transition. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-OPERATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving kube-state-metrics. How do you lead it end to end?
> **Covered in:** [Operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top node && kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. exposes object desired/status metrics rather than container usage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-OPERATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Metrics Server. How do you lead it end to end?
> **Covered in:** [Operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl version` as one read-only checkpoint, not the whole diagnosis. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Argo CD, Flux and GitOps](../07-packaging-extensions/03-gitops/README.md) · [Study note](README.md) · [Next: Kubernetes observability →](01-observability/README.md)

<!-- reading-navigation:end -->
