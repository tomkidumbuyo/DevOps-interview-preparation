# Kubernetes observability — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KUBERNETES-OBSERVABILITY-JN-01

- [ ] **Question:** What is kube-state-metrics, and why does it matter in Kubernetes observability?
> **Covered in:** [Kubernetes observability — Observability](README.md#observability)

**Answer:** exposes object desired/status metrics rather than container usage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-OBSERVABILITY-JN-02

- [ ] **Question:** What is Metrics Server, and why does it matter in Kubernetes observability?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** lightweight resource metrics for top/HPA, not a long-term monitoring backend. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-OBSERVABILITY-JN-03

- [ ] **Question:** What is kubelet/cAdvisor, and why does it matter in Kubernetes observability?
> **Covered in:** [Kubernetes observability — Observability](README.md#observability)

**Answer:** node/container CPU/memory/filesystem/network metrics under version/runtime coverage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-OBSERVABILITY-JN-04

- [ ] **Question:** What is Control-plane metrics, and why does it matter in Kubernetes observability?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** API latency/errors/inflight, scheduler attempts, controller queue and etcd latency/space. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-OBSERVABILITY-JN-05

- [ ] **Question:** What is Events, and why does it matter in Kubernetes observability?
> **Covered in:** [Kubernetes observability — Observability](README.md#observability)

**Answer:** best-effort short-retention diagnostic records, not an audit log. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-OBSERVABILITY-JN-06

- [ ] **Question:** What is Audit log, and why does it matter in Kubernetes observability?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** API request identity/verb/resource/stage evidence with privacy/volume policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-OBSERVABILITY-JN-07

- [ ] **Question:** What is Container logs, and why does it matter in Kubernetes observability?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** stdout/stderr rotation/collection requires node agent and structured context. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-OBSERVABILITY-JN-08

- [ ] **Code:** **Question:** What does `kubectl logs -n monitoring deploy/prometheus --since=30m` help you verify for Kubernetes observability?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: DNS/CNI/conntrack/eBPF/flow/LB signals locate service paths.

### KUBERNETES-OBSERVABILITY-JN-09

- [ ] **Code:** **Question:** What does `kubectl top node && kubectl top pod -A --containers` help you verify for Kubernetes observability?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: CSI operations, attach/mount, volume latency/capacity and snapshot state.

### KUBERNETES-OBSERVABILITY-JN-10

- [ ] **Code:** **Question:** What does `kubectl get --raw /metrics | head` help you verify for Kubernetes observability?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: Pod/container/UID labels already churn; user/request IDs must not become metric labels.

## Junior — procedural and command questions

### KUBERNETES-OBSERVABILITY-JP-01

- [ ] **Code:** **Question:** A basic kube-state-metrics check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top node && kubectl top pod -A --containers` and capture exact status/reason/request ID. exposes object desired/status metrics rather than container usage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-OBSERVABILITY-JP-02

- [ ] **Question:** A basic Metrics Server check fails. What would you do first?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /metrics | head` and capture exact status/reason/request ID. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-OBSERVABILITY-JP-03

- [ ] **Question:** A basic kubelet/cAdvisor check fails. What would you do first?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.metadata.creationTimestamp` and capture exact status/reason/request ID. node/container CPU/memory/filesystem/network metrics under version/runtime coverage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-OBSERVABILITY-JP-04

- [ ] **Code:** **Question:** A basic Control-plane metrics check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n monitoring deploy/prometheus --since=30m` and capture exact status/reason/request ID. API latency/errors/inflight, scheduler attempts, controller queue and etcd latency/space. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-OBSERVABILITY-JP-05

- [ ] **Question:** A basic Events check fails. What would you do first?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top node && kubectl top pod -A --containers` and capture exact status/reason/request ID. best-effort short-retention diagnostic records, not an audit log. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-OBSERVABILITY-JP-06

- [ ] **Question:** A basic Audit log check fails. What would you do first?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /metrics | head` and capture exact status/reason/request ID. API request identity/verb/resource/stage evidence with privacy/volume policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-OBSERVABILITY-JP-07

- [ ] **Code:** **Question:** A basic Container logs check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.metadata.creationTimestamp` and capture exact status/reason/request ID. stdout/stderr rotation/collection requires node agent and structured context. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-OBSERVABILITY-JP-08

- [ ] **Question:** A basic Network telemetry check fails. What would you do first?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n monitoring deploy/prometheus --since=30m` and capture exact status/reason/request ID. DNS/CNI/conntrack/eBPF/flow/LB signals locate service paths. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-OBSERVABILITY-JP-09

- [ ] **Question:** A basic Storage telemetry check fails. What would you do first?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top node && kubectl top pod -A --containers` and capture exact status/reason/request ID. CSI operations, attach/mount, volume latency/capacity and snapshot state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-OBSERVABILITY-JP-10

- [ ] **Code:** **Question:** A basic Cardinality check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes observability — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /metrics | head` and capture exact status/reason/request ID. Pod/container/UID labels already churn; user/request IDs must not become metric labels. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KUBERNETES-OBSERVABILITY-MN-01

- [ ] **Question:** Compare kube-state-metrics with Metrics Server. When would each change your design?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** kube-state-metrics: exposes object desired/status metrics rather than container usage. Metrics Server: lightweight resource metrics for top/HPA, not a long-term monitoring backend. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-OBSERVABILITY-MN-02

- [ ] **Question:** Compare Metrics Server with kubelet/cAdvisor. When would each change your design?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Metrics Server: lightweight resource metrics for top/HPA, not a long-term monitoring backend. kubelet/cAdvisor: node/container CPU/memory/filesystem/network metrics under version/runtime coverage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-OBSERVABILITY-MN-03

- [ ] **Question:** Compare kubelet/cAdvisor with Control-plane metrics. When would each change your design?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** kubelet/cAdvisor: node/container CPU/memory/filesystem/network metrics under version/runtime coverage. Control-plane metrics: API latency/errors/inflight, scheduler attempts, controller queue and etcd latency/space. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-OBSERVABILITY-MN-04

- [ ] **Configuration review:** **Question:** Compare Control-plane metrics with Events. When would each change your design?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Control-plane metrics: API latency/errors/inflight, scheduler attempts, controller queue and etcd latency/space. Events: best-effort short-retention diagnostic records, not an audit log. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-OBSERVABILITY-MN-05

- [ ] **Question:** Compare Events with Audit log. When would each change your design?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Events: best-effort short-retention diagnostic records, not an audit log. Audit log: API request identity/verb/resource/stage evidence with privacy/volume policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-OBSERVABILITY-MN-06

- [ ] **Question:** Compare Audit log with Container logs. When would each change your design?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Audit log: API request identity/verb/resource/stage evidence with privacy/volume policy. Container logs: stdout/stderr rotation/collection requires node agent and structured context. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-OBSERVABILITY-MN-07

- [ ] **Configuration review:** **Question:** Compare Container logs with Network telemetry. When would each change your design?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Container logs: stdout/stderr rotation/collection requires node agent and structured context. Network telemetry: DNS/CNI/conntrack/eBPF/flow/LB signals locate service paths. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-OBSERVABILITY-MN-08

- [ ] **Question:** Compare Network telemetry with Storage telemetry. When would each change your design?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Network telemetry: DNS/CNI/conntrack/eBPF/flow/LB signals locate service paths. Storage telemetry: CSI operations, attach/mount, volume latency/capacity and snapshot state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-OBSERVABILITY-MN-09

- [ ] **Question:** Compare Storage telemetry with Cardinality. When would each change your design?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Storage telemetry: CSI operations, attach/mount, volume latency/capacity and snapshot state. Cardinality: Pod/container/UID labels already churn; user/request IDs must not become metric labels. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-OBSERVABILITY-MN-10

- [ ] **Configuration review:** **Question:** Compare Cardinality with kube-state-metrics. When would each change your design?
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Cardinality: Pod/container/UID labels already churn; user/request IDs must not become metric labels. kube-state-metrics: exposes object desired/status metrics rather than container usage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KUBERNETES-OBSERVABILITY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around kube-state-metrics; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top node && kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. exposes object desired/status metrics rather than container usage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-OBSERVABILITY-MP-02

- [ ] **Question:** Production is degraded around Metrics Server; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /metrics | head` plus recent events/changes, then correlate the service-specific SLI. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-OBSERVABILITY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around kubelet/cAdvisor; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.metadata.creationTimestamp` plus recent events/changes, then correlate the service-specific SLI. node/container CPU/memory/filesystem/network metrics under version/runtime coverage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-OBSERVABILITY-MP-04

- [ ] **Question:** Production is degraded around Control-plane metrics; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n monitoring deploy/prometheus --since=30m` plus recent events/changes, then correlate the service-specific SLI. API latency/errors/inflight, scheduler attempts, controller queue and etcd latency/space. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-OBSERVABILITY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Events; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top node && kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. best-effort short-retention diagnostic records, not an audit log. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-OBSERVABILITY-MP-06

- [ ] **Question:** Production is degraded around Audit log; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /metrics | head` plus recent events/changes, then correlate the service-specific SLI. API request identity/verb/resource/stage evidence with privacy/volume policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-OBSERVABILITY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Container logs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.metadata.creationTimestamp` plus recent events/changes, then correlate the service-specific SLI. stdout/stderr rotation/collection requires node agent and structured context. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-OBSERVABILITY-MP-08

- [ ] **Question:** Production is degraded around Network telemetry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n monitoring deploy/prometheus --since=30m` plus recent events/changes, then correlate the service-specific SLI. DNS/CNI/conntrack/eBPF/flow/LB signals locate service paths. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-OBSERVABILITY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Storage telemetry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top node && kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. CSI operations, attach/mount, volume latency/capacity and snapshot state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-OBSERVABILITY-MP-10

- [ ] **Question:** Production is degraded around Cardinality; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /metrics | head` plus recent events/changes, then correlate the service-specific SLI. Pod/container/UID labels already churn; user/request IDs must not become metric labels. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KUBERNETES-OBSERVABILITY-SN-01

- [ ] **Question:** Design a production Kubernetes observability capability where kube-state-metrics, Control-plane metrics and Container logs are first-class requirements.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exposes object desired/status metrics rather than container usage. API latency/errors/inflight, scheduler attempts, controller queue and etcd latency/space. stdout/stderr rotation/collection requires node agent and structured context. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-OBSERVABILITY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes observability capability where Metrics Server, Events and Network telemetry are first-class requirements.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: lightweight resource metrics for top/HPA, not a long-term monitoring backend. best-effort short-retention diagnostic records, not an audit log. DNS/CNI/conntrack/eBPF/flow/LB signals locate service paths. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-OBSERVABILITY-SN-03

- [ ] **Question:** Design a production Kubernetes observability capability where kubelet/cAdvisor, Audit log and Storage telemetry are first-class requirements.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: node/container CPU/memory/filesystem/network metrics under version/runtime coverage. API request identity/verb/resource/stage evidence with privacy/volume policy. CSI operations, attach/mount, volume latency/capacity and snapshot state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-OBSERVABILITY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes observability capability where Control-plane metrics, Container logs and Cardinality are first-class requirements.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: API latency/errors/inflight, scheduler attempts, controller queue and etcd latency/space. stdout/stderr rotation/collection requires node agent and structured context. Pod/container/UID labels already churn; user/request IDs must not become metric labels. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-OBSERVABILITY-SN-05

- [ ] **Question:** Design a production Kubernetes observability capability where Events, Network telemetry and kube-state-metrics are first-class requirements.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: best-effort short-retention diagnostic records, not an audit log. DNS/CNI/conntrack/eBPF/flow/LB signals locate service paths. exposes object desired/status metrics rather than container usage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-OBSERVABILITY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes observability capability where Audit log, Storage telemetry and Metrics Server are first-class requirements.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: API request identity/verb/resource/stage evidence with privacy/volume policy. CSI operations, attach/mount, volume latency/capacity and snapshot state. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-OBSERVABILITY-SN-07

- [ ] **Question:** Design a production Kubernetes observability capability where Container logs, Cardinality and kubelet/cAdvisor are first-class requirements.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stdout/stderr rotation/collection requires node agent and structured context. Pod/container/UID labels already churn; user/request IDs must not become metric labels. node/container CPU/memory/filesystem/network metrics under version/runtime coverage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-OBSERVABILITY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes observability capability where Network telemetry, kube-state-metrics and Control-plane metrics are first-class requirements.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: DNS/CNI/conntrack/eBPF/flow/LB signals locate service paths. exposes object desired/status metrics rather than container usage. API latency/errors/inflight, scheduler attempts, controller queue and etcd latency/space. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-OBSERVABILITY-SN-09

- [ ] **Question:** Design a production Kubernetes observability capability where Storage telemetry, Metrics Server and Events are first-class requirements.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: CSI operations, attach/mount, volume latency/capacity and snapshot state. lightweight resource metrics for top/HPA, not a long-term monitoring backend. best-effort short-retention diagnostic records, not an audit log. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-OBSERVABILITY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes observability capability where Cardinality, kubelet/cAdvisor and Audit log are first-class requirements.
> **Covered in:** [Kubernetes observability — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Pod/container/UID labels already churn; user/request IDs must not become metric labels. node/container CPU/memory/filesystem/network metrics under version/runtime coverage. API request identity/verb/resource/stage evidence with privacy/volume policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KUBERNETES-OBSERVABILITY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving kube-state-metrics. How do you lead it end to end?
> **Covered in:** [Kubernetes observability — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top node && kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. exposes object desired/status metrics rather than container usage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-OBSERVABILITY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Metrics Server. How do you lead it end to end?
> **Covered in:** [Kubernetes observability — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /metrics | head` as one read-only checkpoint, not the whole diagnosis. lightweight resource metrics for top/HPA, not a long-term monitoring backend. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-OBSERVABILITY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving kubelet/cAdvisor. How do you lead it end to end?
> **Covered in:** [Kubernetes observability — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.metadata.creationTimestamp` as one read-only checkpoint, not the whole diagnosis. node/container CPU/memory/filesystem/network metrics under version/runtime coverage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-OBSERVABILITY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control-plane metrics. How do you lead it end to end?
> **Covered in:** [Kubernetes observability — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n monitoring deploy/prometheus --since=30m` as one read-only checkpoint, not the whole diagnosis. API latency/errors/inflight, scheduler attempts, controller queue and etcd latency/space. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-OBSERVABILITY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Events. How do you lead it end to end?
> **Covered in:** [Kubernetes observability — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top node && kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. best-effort short-retention diagnostic records, not an audit log. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-OBSERVABILITY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Audit log. How do you lead it end to end?
> **Covered in:** [Kubernetes observability — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /metrics | head` as one read-only checkpoint, not the whole diagnosis. API request identity/verb/resource/stage evidence with privacy/volume policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-OBSERVABILITY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Container logs. How do you lead it end to end?
> **Covered in:** [Kubernetes observability — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.metadata.creationTimestamp` as one read-only checkpoint, not the whole diagnosis. stdout/stderr rotation/collection requires node agent and structured context. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-OBSERVABILITY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Network telemetry. How do you lead it end to end?
> **Covered in:** [Kubernetes observability — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n monitoring deploy/prometheus --since=30m` as one read-only checkpoint, not the whole diagnosis. DNS/CNI/conntrack/eBPF/flow/LB signals locate service paths. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-OBSERVABILITY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Storage telemetry. How do you lead it end to end?
> **Covered in:** [Kubernetes observability — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top node && kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. CSI operations, attach/mount, volume latency/capacity and snapshot state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-OBSERVABILITY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cardinality. How do you lead it end to end?
> **Covered in:** [Kubernetes observability — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /metrics | head` as one read-only checkpoint, not the whole diagnosis. Pod/container/UID labels already churn; user/request IDs must not become metric labels. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Operations](../README.md) · [Study note](README.md) · [Next: Kubernetes upgrades and API deprecations →](../02-upgrades/README.md)

<!-- reading-navigation:end -->
