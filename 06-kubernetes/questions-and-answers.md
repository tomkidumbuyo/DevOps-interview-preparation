# 06 Kubernetes — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-06-KUBERNETES-JN-01

- [ ] **Question:** What is API groups/versions, and why does it matter in 06 Kubernetes?
> **Covered in:** [Kubernetes core platform — 6. Ingress and Gateway API](README.md#6-ingress-and-gateway-api)

**Answer:** resource kinds evolve through served/storage versions and conversion. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-06-KUBERNETES-JN-02

- [ ] **Question:** What is Controller loop, and why does it matter in 06 Kubernetes?
> **Covered in:** [Packaging Extensions — Detailed learning notes](07-packaging-extensions/README.md#detailed-learning-notes)

**Answer:** watches desired/observed state and performs level-based idempotent reconciliation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-06-KUBERNETES-JN-03

- [ ] **Question:** What is Pod sandbox, and why does it matter in 06 Kubernetes?
> **Covered in:** [Kubernetes core platform — 3. Workload controllers and Pod lifecycle](README.md#3-workload-controllers-and-pod-lifecycle)

**Answer:** containers share network namespace and can share IPC/process/volumes by configuration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-06-KUBERNETES-JN-04

- [ ] **Question:** What is Deployment selector, and why does it matter in 06 Kubernetes?
> **Covered in:** [Kubernetes core platform — 2. A complete production-shaped workload](README.md#2-a-complete-production-shaped-workload)

**Answer:** immutable label contract determines which ReplicaSets/Pods are owned. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-06-KUBERNETES-JN-05

- [ ] **Question:** What is Stateful ordinal, and why does it matter in 06 Kubernetes?
> **Covered in:** [Kubernetes core platform — 7. Configuration and secrets](README.md#7-configuration-and-secrets)

**Answer:** stable Pod name/identity persists across rescheduling but not physical node. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-06-KUBERNETES-JN-06

- [ ] **Question:** What is Completion, and why does it matter in 06 Kubernetes?
> **Covered in:** [Kubernetes core platform — 7. Configuration and secrets](README.md#7-configuration-and-secrets)

**Answer:** Job succeeds after required successful Pods/completions under mode semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-06-KUBERNETES-JN-07

- [ ] **Question:** What is Startup probe, and why does it matter in 06 Kubernetes?
> **Covered in:** [Kubernetes core platform — 7. Configuration and secrets](README.md#7-configuration-and-secrets)

**Answer:** delays liveness/readiness scheduling until slow initialization succeeds. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-06-KUBERNETES-JN-08

- [ ] **Code:** **Question:** What does `kubectl get svc,endpoints,endpointslice -A -o wide` help you verify for 06 Kubernetes?
> **Covered in:** [Kubernetes core platform — 13. The kubectl field guide](README.md#13-the-kubectl-field-guide)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: virtual internal IP implemented by the cluster service data plane.

### BRANCH-06-KUBERNETES-JN-09

- [ ] **Code:** **Question:** What does `kubectl get ds -n kube-system` help you verify for 06 Kubernetes?
> **Covered in:** [Kubernetes core platform — 13. The kubectl field guide](README.md#13-the-kubectl-field-guide)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: Pods have cluster-routable IP identity and communicate without required NAT inside the model.

### BRANCH-06-KUBERNETES-JN-10

- [ ] **Code:** **Question:** What does `kubectl get networkpolicy -A -o yaml` help you verify for 06 Kubernetes?
> **Covered in:** [Kubernetes core platform — 13. The kubectl field guide](README.md#13-the-kubectl-field-guide)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: policy applies only to Pods matched in its namespace.

## Junior — procedural and command questions

### BRANCH-06-KUBERNETES-JP-01

- [ ] **Code:** **Question:** A basic API groups/versions check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes API server and etcd — Command lab](01-architecture/01-api-server-etcd/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/readyz?verbose'` and capture exact status/reason/request ID. resource kinds evolve through served/storage versions and conversion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-06-KUBERNETES-JP-02

- [ ] **Question:** A basic Controller loop check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](03-networking/05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. watches desired/observed state and performs level-based idempotent reconciliation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-06-KUBERNETES-JP-03

- [ ] **Question:** A basic Pod sandbox check fails. What would you do first?
> **Covered in:** [Workloads — Command lab](02-workloads/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pod POD -n NS -o yaml` and capture exact status/reason/request ID. containers share network namespace and can share IPC/process/volumes by configuration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-06-KUBERNETES-JP-04

- [ ] **Code:** **Question:** A basic Deployment selector check fails. What would you do first using the CLI?
> **Covered in:** [Service mesh — Command lab](03-networking/05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status deployment/NAME -n NS` and capture exact status/reason/request ID. immutable label contract determines which ReplicaSets/Pods are owned. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-06-KUBERNETES-JP-05

- [ ] **Question:** A basic Stateful ordinal check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](03-networking/05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get statefulset,daemonset -A` and capture exact status/reason/request ID. stable Pod name/identity persists across rescheduling but not physical node. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-06-KUBERNETES-JP-06

- [ ] **Question:** A basic Completion check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](03-networking/05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get job,cronjob -A` and capture exact status/reason/request ID. Job succeeds after required successful Pods/completions under mode semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-06-KUBERNETES-JP-07

- [ ] **Code:** **Question:** A basic Startup probe check fails. What would you do first using the CLI?
> **Covered in:** [Service mesh — Command lab](03-networking/05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` and capture exact status/reason/request ID. delays liveness/readiness scheduling until slow initialization succeeds. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-06-KUBERNETES-JP-08

- [ ] **Question:** A basic ClusterIP check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](03-networking/05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get svc,endpoints,endpointslice -A -o wide` and capture exact status/reason/request ID. virtual internal IP implemented by the cluster service data plane. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-06-KUBERNETES-JP-09

- [ ] **Question:** A basic Kubernetes network model check fails. What would you do first?
> **Covered in:** [Kubernetes multi-tenancy — Easy mode: purpose and mental model](05-security/05-multitenancy/README.md#easy-mode-purpose-and-mental-model)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ds -n kube-system` and capture exact status/reason/request ID. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-06-KUBERNETES-JP-10

- [ ] **Code:** **Question:** A basic Pod selection check fails. What would you do first using the CLI?
> **Covered in:** [Gpu Llmops — 2. Device plugins and basic scheduling](09-gpu-llmops/README.md#2-device-plugins-and-basic-scheduling)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get networkpolicy -A -o yaml` and capture exact status/reason/request ID. policy applies only to Pods matched in its namespace. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-06-KUBERNETES-MN-01

- [ ] **Question:** Compare API groups/versions with Controller loop. When would each change your design?
> **Covered in:** [Architecture — Architecture and lifecycle](01-architecture/README.md#architecture-and-lifecycle)

**Answer:** API groups/versions: resource kinds evolve through served/storage versions and conversion. Controller loop: watches desired/observed state and performs level-based idempotent reconciliation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-06-KUBERNETES-MN-02

- [ ] **Question:** Compare Controller loop with Pod sandbox. When would each change your design?
> **Covered in:** [Scheduler, controllers and kubelet — Architecture and lifecycle](01-architecture/02-scheduler-controllers-kubelet/README.md#architecture-and-lifecycle)

**Answer:** Controller loop: watches desired/observed state and performs level-based idempotent reconciliation. Pod sandbox: containers share network namespace and can share IPC/process/volumes by configuration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-06-KUBERNETES-MN-03

- [ ] **Question:** Compare Pod sandbox with Deployment selector. When would each change your design?
> **Covered in:** [Workloads — Architecture and lifecycle](02-workloads/README.md#architecture-and-lifecycle)

**Answer:** Pod sandbox: containers share network namespace and can share IPC/process/volumes by configuration. Deployment selector: immutable label contract determines which ReplicaSets/Pods are owned. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-06-KUBERNETES-MN-04

- [ ] **Configuration review:** **Question:** Compare Deployment selector with Stateful ordinal. When would each change your design?
> **Covered in:** [Workloads — Architecture and lifecycle](02-workloads/README.md#architecture-and-lifecycle)

**Answer:** Deployment selector: immutable label contract determines which ReplicaSets/Pods are owned. Stateful ordinal: stable Pod name/identity persists across rescheduling but not physical node. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-06-KUBERNETES-MN-05

- [ ] **Question:** Compare Stateful ordinal with Completion. When would each change your design?
> **Covered in:** [Workloads — Architecture and lifecycle](02-workloads/README.md#architecture-and-lifecycle)

**Answer:** Stateful ordinal: stable Pod name/identity persists across rescheduling but not physical node. Completion: Job succeeds after required successful Pods/completions under mode semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-06-KUBERNETES-MN-06

- [ ] **Question:** Compare Completion with Startup probe. When would each change your design?
> **Covered in:** [Workloads — Architecture and lifecycle](02-workloads/README.md#architecture-and-lifecycle)

**Answer:** Completion: Job succeeds after required successful Pods/completions under mode semantics. Startup probe: delays liveness/readiness scheduling until slow initialization succeeds. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-06-KUBERNETES-MN-07

- [ ] **Configuration review:** **Question:** Compare Startup probe with ClusterIP. When would each change your design?
> **Covered in:** [Kubernetes core platform — 7. Configuration and secrets](README.md#7-configuration-and-secrets)

**Answer:** Startup probe: delays liveness/readiness scheduling until slow initialization succeeds. ClusterIP: virtual internal IP implemented by the cluster service data plane. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-06-KUBERNETES-MN-08

- [ ] **Question:** Compare ClusterIP with Kubernetes network model. When would each change your design?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Easy mode: purpose and mental model](05-security/03-secrets-configmaps/README.md#easy-mode-purpose-and-mental-model)

**Answer:** ClusterIP: virtual internal IP implemented by the cluster service data plane. Kubernetes network model: Pods have cluster-routable IP identity and communicate without required NAT inside the model. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-06-KUBERNETES-MN-09

- [ ] **Question:** Compare Kubernetes network model with Pod selection. When would each change your design?
> **Covered in:** [Networking — Architecture and lifecycle](03-networking/README.md#architecture-and-lifecycle)

**Answer:** Kubernetes network model: Pods have cluster-routable IP identity and communicate without required NAT inside the model. Pod selection: policy applies only to Pods matched in its namespace. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-06-KUBERNETES-MN-10

- [ ] **Configuration review:** **Question:** Compare Pod selection with API groups/versions. When would each change your design?
> **Covered in:** [Kubernetes core platform — 7. Configuration and secrets](README.md#7-configuration-and-secrets)

**Answer:** Pod selection: policy applies only to Pods matched in its namespace. API groups/versions: resource kinds evolve through served/storage versions and conversion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-06-KUBERNETES-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around API groups/versions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes core platform — 14. Symptom-to-command troubleshooting table](README.md#14-symptom-to-command-troubleshooting-table)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/readyz?verbose'` plus recent events/changes, then correlate the service-specific SLI. resource kinds evolve through served/storage versions and conversion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-06-KUBERNETES-MP-02

- [ ] **Question:** Production is degraded around Controller loop; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes core platform — 14. Symptom-to-command troubleshooting table](README.md#14-symptom-to-command-troubleshooting-table)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. watches desired/observed state and performs level-based idempotent reconciliation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-06-KUBERNETES-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pod sandbox; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes core platform — 14. Symptom-to-command troubleshooting table](README.md#14-symptom-to-command-troubleshooting-table)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pod POD -n NS -o yaml` plus recent events/changes, then correlate the service-specific SLI. containers share network namespace and can share IPC/process/volumes by configuration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-06-KUBERNETES-MP-04

- [ ] **Question:** Production is degraded around Deployment selector; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Workloads — Architecture and lifecycle](02-workloads/README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status deployment/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. immutable label contract determines which ReplicaSets/Pods are owned. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-06-KUBERNETES-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Stateful ordinal; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Workloads — Architecture and lifecycle](02-workloads/README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get statefulset,daemonset -A` plus recent events/changes, then correlate the service-specific SLI. stable Pod name/identity persists across rescheduling but not physical node. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-06-KUBERNETES-MP-06

- [ ] **Question:** Production is degraded around Completion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes core platform — 14. Symptom-to-command troubleshooting table](README.md#14-symptom-to-command-troubleshooting-table)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get job,cronjob -A` plus recent events/changes, then correlate the service-specific SLI. Job succeeds after required successful Pods/completions under mode semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-06-KUBERNETES-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Startup probe; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes core platform — 14. Symptom-to-command troubleshooting table](README.md#14-symptom-to-command-troubleshooting-table)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` plus recent events/changes, then correlate the service-specific SLI. delays liveness/readiness scheduling until slow initialization succeeds. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-06-KUBERNETES-MP-08

- [ ] **Question:** Production is degraded around ClusterIP; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes core platform — 14. Symptom-to-command troubleshooting table](README.md#14-symptom-to-command-troubleshooting-table)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get svc,endpoints,endpointslice -A -o wide` plus recent events/changes, then correlate the service-specific SLI. virtual internal IP implemented by the cluster service data plane. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-06-KUBERNETES-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Kubernetes network model; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes troubleshooting and kubectl — Easy mode: purpose and mental model](08-operations/04-troubleshooting-kubectl/README.md#easy-mode-purpose-and-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ds -n kube-system` plus recent events/changes, then correlate the service-specific SLI. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-06-KUBERNETES-MP-10

- [ ] **Question:** Production is degraded around Pod selection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes core platform — 14. Symptom-to-command troubleshooting table](README.md#14-symptom-to-command-troubleshooting-table)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get networkpolicy -A -o yaml` plus recent events/changes, then correlate the service-specific SLI. policy applies only to Pods matched in its namespace. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-06-KUBERNETES-SN-01

- [ ] **Question:** Design a production 06 Kubernetes capability where API groups/versions, Deployment selector and Startup probe are first-class requirements.
> **Covered in:** [Workloads — Architecture and lifecycle](02-workloads/README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: resource kinds evolve through served/storage versions and conversion. immutable label contract determines which ReplicaSets/Pods are owned. delays liveness/readiness scheduling until slow initialization succeeds. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-06-KUBERNETES-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production 06 Kubernetes capability where Controller loop, Stateful ordinal and ClusterIP are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](01-architecture/README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: watches desired/observed state and performs level-based idempotent reconciliation. stable Pod name/identity persists across rescheduling but not physical node. virtual internal IP implemented by the cluster service data plane. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-06-KUBERNETES-SN-03

- [ ] **Question:** Design a production 06 Kubernetes capability where Pod sandbox, Completion and Kubernetes network model are first-class requirements.
> **Covered in:** [Networking — Architecture and lifecycle](03-networking/README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: containers share network namespace and can share IPC/process/volumes by configuration. Job succeeds after required successful Pods/completions under mode semantics. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-06-KUBERNETES-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production 06 Kubernetes capability where Deployment selector, Startup probe and Pod selection are first-class requirements.
> **Covered in:** [Workloads — Architecture and lifecycle](02-workloads/README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable label contract determines which ReplicaSets/Pods are owned. delays liveness/readiness scheduling until slow initialization succeeds. policy applies only to Pods matched in its namespace. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-06-KUBERNETES-SN-05

- [ ] **Question:** Design a production 06 Kubernetes capability where Stateful ordinal, ClusterIP and API groups/versions are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](01-architecture/README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stable Pod name/identity persists across rescheduling but not physical node. virtual internal IP implemented by the cluster service data plane. resource kinds evolve through served/storage versions and conversion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-06-KUBERNETES-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production 06 Kubernetes capability where Completion, Kubernetes network model and Controller loop are first-class requirements.
> **Covered in:** [Gpu Llmops — 12. Hard-mode production design](09-gpu-llmops/README.md#12-hard-mode-production-design)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Job succeeds after required successful Pods/completions under mode semantics. Pods have cluster-routable IP identity and communicate without required NAT inside the model. watches desired/observed state and performs level-based idempotent reconciliation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-06-KUBERNETES-SN-07

- [ ] **Question:** Design a production 06 Kubernetes capability where Startup probe, Pod selection and Pod sandbox are first-class requirements.
> **Covered in:** [Workloads — Architecture and lifecycle](02-workloads/README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: delays liveness/readiness scheduling until slow initialization succeeds. policy applies only to Pods matched in its namespace. containers share network namespace and can share IPC/process/volumes by configuration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-06-KUBERNETES-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production 06 Kubernetes capability where ClusterIP, API groups/versions and Deployment selector are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](01-architecture/README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: virtual internal IP implemented by the cluster service data plane. resource kinds evolve through served/storage versions and conversion. immutable label contract determines which ReplicaSets/Pods are owned. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-06-KUBERNETES-SN-09

- [ ] **Question:** Design a production 06 Kubernetes capability where Kubernetes network model, Controller loop and Stateful ordinal are first-class requirements.
> **Covered in:** [Gpu Llmops — 12. Hard-mode production design](09-gpu-llmops/README.md#12-hard-mode-production-design)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Pods have cluster-routable IP identity and communicate without required NAT inside the model. watches desired/observed state and performs level-based idempotent reconciliation. stable Pod name/identity persists across rescheduling but not physical node. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-06-KUBERNETES-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production 06 Kubernetes capability where Pod selection, Pod sandbox and Completion are first-class requirements.
> **Covered in:** [Workloads — Architecture and lifecycle](02-workloads/README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: policy applies only to Pods matched in its namespace. containers share network namespace and can share IPC/process/volumes by configuration. Job succeeds after required successful Pods/completions under mode semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-06-KUBERNETES-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving API groups/versions. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](01-architecture/README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/readyz?verbose'` as one read-only checkpoint, not the whole diagnosis. resource kinds evolve through served/storage versions and conversion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-06-KUBERNETES-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Controller loop. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](01-architecture/README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. watches desired/observed state and performs level-based idempotent reconciliation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-06-KUBERNETES-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod sandbox. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](01-architecture/README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pod POD -n NS -o yaml` as one read-only checkpoint, not the whole diagnosis. containers share network namespace and can share IPC/process/volumes by configuration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-06-KUBERNETES-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deployment selector. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](01-architecture/README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status deployment/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. immutable label contract determines which ReplicaSets/Pods are owned. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-06-KUBERNETES-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stateful ordinal. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](01-architecture/README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get statefulset,daemonset -A` as one read-only checkpoint, not the whole diagnosis. stable Pod name/identity persists across rescheduling but not physical node. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-06-KUBERNETES-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Completion. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](01-architecture/README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get job,cronjob -A` as one read-only checkpoint, not the whole diagnosis. Job succeeds after required successful Pods/completions under mode semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-06-KUBERNETES-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Startup probe. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](01-architecture/README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` as one read-only checkpoint, not the whole diagnosis. delays liveness/readiness scheduling until slow initialization succeeds. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-06-KUBERNETES-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ClusterIP. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](01-architecture/README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get svc,endpoints,endpointslice -A -o wide` as one read-only checkpoint, not the whole diagnosis. virtual internal IP implemented by the cluster service data plane. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-06-KUBERNETES-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Kubernetes network model. How do you lead it end to end?
> **Covered in:** [Kubernetes multi-tenancy — Easy mode: purpose and mental model](05-security/05-multitenancy/README.md#easy-mode-purpose-and-mental-model)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ds -n kube-system` as one read-only checkpoint, not the whole diagnosis. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-06-KUBERNETES-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod selection. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](01-architecture/README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get networkpolicy -A -o yaml` as one read-only checkpoint, not the whole diagnosis. policy applies only to Pods matched in its namespace. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Container security](../05-containers/07-container-security/README.md) · [Study note](README.md) · [Next: Architecture →](01-architecture/README.md)

<!-- reading-navigation:end -->
