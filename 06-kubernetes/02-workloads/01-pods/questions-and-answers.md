# Kubernetes Pods — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KUBERNETES-PODS-JN-01

- [ ] **Question:** What is Pod sandbox, and why does it matter in Kubernetes Pods?
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** containers share network namespace and can share IPC/process/volumes by configuration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-PODS-JN-02

- [ ] **Question:** What is Phase, and why does it matter in Kubernetes Pods?
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-PODS-JN-03

- [ ] **Question:** What is Init container, and why does it matter in Kubernetes Pods?
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** sequential prerequisite that must complete before app containers. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-PODS-JN-04

- [ ] **Question:** What is Sidecar, and why does it matter in Kubernetes Pods?
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** supporting container lifecycle/order needs explicit startup/termination semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-PODS-JN-05

- [ ] **Question:** What is Ephemeral container, and why does it matter in Kubernetes Pods?
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** debug process added to a running Pod without normal resources/probes/restart. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-PODS-JN-06

- [ ] **Question:** What is Restart policy, and why does it matter in Kubernetes Pods?
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** kubelet restarts containers under Always/OnFailure/Never and exponential backoff. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-PODS-JN-07

- [ ] **Question:** What is Termination grace, and why does it matter in Kubernetes Pods?
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** SIGTERM/preStop/drain must finish before SIGKILL deadline. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-PODS-JN-08

- [ ] **Code:** **Question:** What does `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` help you verify for Kubernetes Pods?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: custom condition can delay readiness beyond container probes.

### KUBERNETES-PODS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get pod POD -n NS -o yaml` help you verify for Kubernetes Pods?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: connects Pod to controller garbage collection and desired count.

### KUBERNETES-PODS-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe pod POD -n NS` help you verify for Kubernetes Pods?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: writable layer/logs/emptyDir count toward requests/limits and node disk pressure.

## Junior — procedural and command questions

### KUBERNETES-PODS-JP-01

- [ ] **Code:** **Question:** A basic Pod sandbox check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pod POD -n NS -o yaml` and capture exact status/reason/request ID. containers share network namespace and can share IPC/process/volumes by configuration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-PODS-JP-02

- [ ] **Question:** A basic Phase check fails. What would you do first?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-PODS-JP-03

- [ ] **Question:** A basic Init container check fails. What would you do first?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs POD -n NS --all-containers --previous` and capture exact status/reason/request ID. sequential prerequisite that must complete before app containers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-PODS-JP-04

- [ ] **Code:** **Question:** A basic Sidecar check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` and capture exact status/reason/request ID. supporting container lifecycle/order needs explicit startup/termination semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-PODS-JP-05

- [ ] **Question:** A basic Ephemeral container check fails. What would you do first?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pod POD -n NS -o yaml` and capture exact status/reason/request ID. debug process added to a running Pod without normal resources/probes/restart. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-PODS-JP-06

- [ ] **Question:** A basic Restart policy check fails. What would you do first?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. kubelet restarts containers under Always/OnFailure/Never and exponential backoff. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-PODS-JP-07

- [ ] **Code:** **Question:** A basic Termination grace check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs POD -n NS --all-containers --previous` and capture exact status/reason/request ID. SIGTERM/preStop/drain must finish before SIGKILL deadline. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-PODS-JP-08

- [ ] **Question:** A basic Pod readiness gate check fails. What would you do first?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` and capture exact status/reason/request ID. custom condition can delay readiness beyond container probes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-PODS-JP-09

- [ ] **Question:** A basic Owner reference check fails. What would you do first?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pod POD -n NS -o yaml` and capture exact status/reason/request ID. connects Pod to controller garbage collection and desired count. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-PODS-JP-10

- [ ] **Code:** **Question:** A basic Ephemeral storage check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes Pods — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. writable layer/logs/emptyDir count toward requests/limits and node disk pressure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KUBERNETES-PODS-MN-01

- [ ] **Question:** Compare Pod sandbox with Phase. When would each change your design?
> **Covered in:** [Kubernetes Pods — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Pod sandbox: containers share network namespace and can share IPC/process/volumes by configuration. Phase: Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-PODS-MN-02

- [ ] **Question:** Compare Phase with Init container. When would each change your design?
> **Covered in:** [Kubernetes Pods — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Phase: Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Init container: sequential prerequisite that must complete before app containers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-PODS-MN-03

- [ ] **Question:** Compare Init container with Sidecar. When would each change your design?
> **Covered in:** [Kubernetes Pods — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Init container: sequential prerequisite that must complete before app containers. Sidecar: supporting container lifecycle/order needs explicit startup/termination semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-PODS-MN-04

- [ ] **Configuration review:** **Question:** Compare Sidecar with Ephemeral container. When would each change your design?
> **Covered in:** [Kubernetes Pods — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Sidecar: supporting container lifecycle/order needs explicit startup/termination semantics. Ephemeral container: debug process added to a running Pod without normal resources/probes/restart. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-PODS-MN-05

- [ ] **Question:** Compare Ephemeral container with Restart policy. When would each change your design?
> **Covered in:** [Kubernetes Pods — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Ephemeral container: debug process added to a running Pod without normal resources/probes/restart. Restart policy: kubelet restarts containers under Always/OnFailure/Never and exponential backoff. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-PODS-MN-06

- [ ] **Question:** Compare Restart policy with Termination grace. When would each change your design?
> **Covered in:** [Kubernetes Pods — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Restart policy: kubelet restarts containers under Always/OnFailure/Never and exponential backoff. Termination grace: SIGTERM/preStop/drain must finish before SIGKILL deadline. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-PODS-MN-07

- [ ] **Configuration review:** **Question:** Compare Termination grace with Pod readiness gate. When would each change your design?
> **Covered in:** [Kubernetes Pods — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Termination grace: SIGTERM/preStop/drain must finish before SIGKILL deadline. Pod readiness gate: custom condition can delay readiness beyond container probes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-PODS-MN-08

- [ ] **Question:** Compare Pod readiness gate with Owner reference. When would each change your design?
> **Covered in:** [Kubernetes Pods — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Pod readiness gate: custom condition can delay readiness beyond container probes. Owner reference: connects Pod to controller garbage collection and desired count. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-PODS-MN-09

- [ ] **Question:** Compare Owner reference with Ephemeral storage. When would each change your design?
> **Covered in:** [Kubernetes Pods — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Owner reference: connects Pod to controller garbage collection and desired count. Ephemeral storage: writable layer/logs/emptyDir count toward requests/limits and node disk pressure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-PODS-MN-10

- [ ] **Configuration review:** **Question:** Compare Ephemeral storage with Pod sandbox. When would each change your design?
> **Covered in:** [Kubernetes Pods — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Ephemeral storage: writable layer/logs/emptyDir count toward requests/limits and node disk pressure. Pod sandbox: containers share network namespace and can share IPC/process/volumes by configuration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KUBERNETES-PODS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pod sandbox; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pod POD -n NS -o yaml` plus recent events/changes, then correlate the service-specific SLI. containers share network namespace and can share IPC/process/volumes by configuration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-PODS-MP-02

- [ ] **Question:** Production is degraded around Phase; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-PODS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Init container; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs POD -n NS --all-containers --previous` plus recent events/changes, then correlate the service-specific SLI. sequential prerequisite that must complete before app containers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-PODS-MP-04

- [ ] **Question:** Production is degraded around Sidecar; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` plus recent events/changes, then correlate the service-specific SLI. supporting container lifecycle/order needs explicit startup/termination semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-PODS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Ephemeral container; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pod POD -n NS -o yaml` plus recent events/changes, then correlate the service-specific SLI. debug process added to a running Pod without normal resources/probes/restart. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-PODS-MP-06

- [ ] **Question:** Production is degraded around Restart policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. kubelet restarts containers under Always/OnFailure/Never and exponential backoff. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-PODS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Termination grace; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs POD -n NS --all-containers --previous` plus recent events/changes, then correlate the service-specific SLI. SIGTERM/preStop/drain must finish before SIGKILL deadline. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-PODS-MP-08

- [ ] **Question:** Production is degraded around Pod readiness gate; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` plus recent events/changes, then correlate the service-specific SLI. custom condition can delay readiness beyond container probes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-PODS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Owner reference; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pod POD -n NS -o yaml` plus recent events/changes, then correlate the service-specific SLI. connects Pod to controller garbage collection and desired count. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-PODS-MP-10

- [ ] **Question:** Production is degraded around Ephemeral storage; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. writable layer/logs/emptyDir count toward requests/limits and node disk pressure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KUBERNETES-PODS-SN-01

- [ ] **Question:** Design a production Kubernetes Pods capability where Pod sandbox, Sidecar and Termination grace are first-class requirements.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: containers share network namespace and can share IPC/process/volumes by configuration. supporting container lifecycle/order needs explicit startup/termination semantics. SIGTERM/preStop/drain must finish before SIGKILL deadline. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-PODS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes Pods capability where Phase, Ephemeral container and Pod readiness gate are first-class requirements.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. debug process added to a running Pod without normal resources/probes/restart. custom condition can delay readiness beyond container probes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-PODS-SN-03

- [ ] **Question:** Design a production Kubernetes Pods capability where Init container, Restart policy and Owner reference are first-class requirements.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: sequential prerequisite that must complete before app containers. kubelet restarts containers under Always/OnFailure/Never and exponential backoff. connects Pod to controller garbage collection and desired count. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-PODS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes Pods capability where Sidecar, Termination grace and Ephemeral storage are first-class requirements.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supporting container lifecycle/order needs explicit startup/termination semantics. SIGTERM/preStop/drain must finish before SIGKILL deadline. writable layer/logs/emptyDir count toward requests/limits and node disk pressure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-PODS-SN-05

- [ ] **Question:** Design a production Kubernetes Pods capability where Ephemeral container, Pod readiness gate and Pod sandbox are first-class requirements.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: debug process added to a running Pod without normal resources/probes/restart. custom condition can delay readiness beyond container probes. containers share network namespace and can share IPC/process/volumes by configuration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-PODS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes Pods capability where Restart policy, Owner reference and Phase are first-class requirements.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: kubelet restarts containers under Always/OnFailure/Never and exponential backoff. connects Pod to controller garbage collection and desired count. Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-PODS-SN-07

- [ ] **Question:** Design a production Kubernetes Pods capability where Termination grace, Ephemeral storage and Init container are first-class requirements.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: SIGTERM/preStop/drain must finish before SIGKILL deadline. writable layer/logs/emptyDir count toward requests/limits and node disk pressure. sequential prerequisite that must complete before app containers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-PODS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes Pods capability where Pod readiness gate, Pod sandbox and Sidecar are first-class requirements.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: custom condition can delay readiness beyond container probes. containers share network namespace and can share IPC/process/volumes by configuration. supporting container lifecycle/order needs explicit startup/termination semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-PODS-SN-09

- [ ] **Question:** Design a production Kubernetes Pods capability where Owner reference, Phase and Ephemeral container are first-class requirements.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: connects Pod to controller garbage collection and desired count. Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. debug process added to a running Pod without normal resources/probes/restart. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-PODS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes Pods capability where Ephemeral storage, Init container and Restart policy are first-class requirements.
> **Covered in:** [Kubernetes Pods — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: writable layer/logs/emptyDir count toward requests/limits and node disk pressure. sequential prerequisite that must complete before app containers. kubelet restarts containers under Always/OnFailure/Never and exponential backoff. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KUBERNETES-PODS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod sandbox. How do you lead it end to end?
> **Covered in:** [Kubernetes Pods — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pod POD -n NS -o yaml` as one read-only checkpoint, not the whole diagnosis. containers share network namespace and can share IPC/process/volumes by configuration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-PODS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Phase. How do you lead it end to end?
> **Covered in:** [Kubernetes Pods — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-PODS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Init container. How do you lead it end to end?
> **Covered in:** [Kubernetes Pods — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs POD -n NS --all-containers --previous` as one read-only checkpoint, not the whole diagnosis. sequential prerequisite that must complete before app containers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-PODS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Sidecar. How do you lead it end to end?
> **Covered in:** [Kubernetes Pods — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` as one read-only checkpoint, not the whole diagnosis. supporting container lifecycle/order needs explicit startup/termination semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-PODS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ephemeral container. How do you lead it end to end?
> **Covered in:** [Kubernetes Pods — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pod POD -n NS -o yaml` as one read-only checkpoint, not the whole diagnosis. debug process added to a running Pod without normal resources/probes/restart. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-PODS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Restart policy. How do you lead it end to end?
> **Covered in:** [Kubernetes Pods — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. kubelet restarts containers under Always/OnFailure/Never and exponential backoff. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-PODS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Termination grace. How do you lead it end to end?
> **Covered in:** [Kubernetes Pods — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs POD -n NS --all-containers --previous` as one read-only checkpoint, not the whole diagnosis. SIGTERM/preStop/drain must finish before SIGKILL deadline. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-PODS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod readiness gate. How do you lead it end to end?
> **Covered in:** [Kubernetes Pods — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` as one read-only checkpoint, not the whole diagnosis. custom condition can delay readiness beyond container probes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-PODS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Owner reference. How do you lead it end to end?
> **Covered in:** [Kubernetes Pods — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pod POD -n NS -o yaml` as one read-only checkpoint, not the whole diagnosis. connects Pod to controller garbage collection and desired count. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-PODS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ephemeral storage. How do you lead it end to end?
> **Covered in:** [Kubernetes Pods — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. writable layer/logs/emptyDir count toward requests/limits and node disk pressure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Workloads](../README.md) · [Study note](README.md) · [Next: Deployments and ReplicaSets →](../02-deployments/README.md)

<!-- reading-navigation:end -->
