# Pod and node workload security — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### POD-AND-NODE-WORKLOAD-SECURITY-JN-01

- [ ] **Question:** What is runAsNonRoot, and why does it matter in Pod and node workload security?

**Answer:** prevents UID 0 execution when image/runtime identity can be determined. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### POD-AND-NODE-WORKLOAD-SECURITY-JN-02

- [ ] **Question:** What is allowPrivilegeEscalation, and why does it matter in Pod and node workload security?

**Answer:** blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### POD-AND-NODE-WORKLOAD-SECURITY-JN-03

- [ ] **Question:** What is Capabilities, and why does it matter in Pod and node workload security?

**Answer:** drop ALL and add only exact kernel privileges required. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### POD-AND-NODE-WORKLOAD-SECURITY-JN-04

- [ ] **Question:** What is Seccomp, and why does it matter in Pod and node workload security?

**Answer:** RuntimeDefault/local profiles reduce syscall attack surface. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### POD-AND-NODE-WORKLOAD-SECURITY-JN-05

- [ ] **Question:** What is Read-only root, and why does it matter in Pod and node workload security?

**Answer:** prevents image filesystem mutation and requires explicit writable volumes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### POD-AND-NODE-WORKLOAD-SECURITY-JN-06

- [ ] **Question:** What is Privileged container, and why does it matter in Pod and node workload security?

**Answer:** largely bypasses container isolation and is equivalent to host-level trust. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### POD-AND-NODE-WORKLOAD-SECURITY-JN-07

- [ ] **Question:** What is Host namespaces/path, and why does it matter in Pod and node workload security?

**Answer:** hostNetwork/PID/IPC/hostPath expose shared host attack surface. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### POD-AND-NODE-WORKLOAD-SECURITY-JN-08

- [ ] **Code:** **Question:** What does `kubectl apply --dry-run=server -f pod.yaml` help you verify for Pod and node workload security?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: privileged/baseline/restricted profiles define portable control sets.

### POD-AND-NODE-WORKLOAD-SECURITY-JN-09

- [ ] **Code:** **Question:** What does `kubectl get ns --show-labels` help you verify for Pod and node workload security?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: namespace labels enforce/audit/warn standards by version.

### POD-AND-NODE-WORKLOAD-SECURITY-JN-10

- [ ] **Code:** **Question:** What does `kubectl label ns NS pod-security.kubernetes.io/enforce=restricted` help you verify for Pod and node workload security?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: kernel/runtime/kubelet/metadata/patch and tenant separation remain outside Pod spec.

## Junior — procedural and command questions

### POD-AND-NODE-WORKLOAD-SECURITY-JP-01

- [ ] **Code:** **Question:** A basic runAsNonRoot check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ns --show-labels` and capture exact status/reason/request ID. prevents UID 0 execution when image/runtime identity can be determined. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### POD-AND-NODE-WORKLOAD-SECURITY-JP-02

- [ ] **Question:** A basic allowPrivilegeEscalation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl label ns NS pod-security.kubernetes.io/enforce=restricted` and capture exact status/reason/request ID. blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### POD-AND-NODE-WORKLOAD-SECURITY-JP-03

- [ ] **Question:** A basic Capabilities check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o json | jq '.items[] | select(any(.spec.containers[]; .securityContext.privileged==true))'` and capture exact status/reason/request ID. drop ALL and add only exact kernel privileges required. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### POD-AND-NODE-WORKLOAD-SECURITY-JP-04

- [ ] **Code:** **Question:** A basic Seccomp check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl apply --dry-run=server -f pod.yaml` and capture exact status/reason/request ID. RuntimeDefault/local profiles reduce syscall attack surface. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### POD-AND-NODE-WORKLOAD-SECURITY-JP-05

- [ ] **Question:** A basic Read-only root check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ns --show-labels` and capture exact status/reason/request ID. prevents image filesystem mutation and requires explicit writable volumes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### POD-AND-NODE-WORKLOAD-SECURITY-JP-06

- [ ] **Question:** A basic Privileged container check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl label ns NS pod-security.kubernetes.io/enforce=restricted` and capture exact status/reason/request ID. largely bypasses container isolation and is equivalent to host-level trust. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### POD-AND-NODE-WORKLOAD-SECURITY-JP-07

- [ ] **Code:** **Question:** A basic Host namespaces/path check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o json | jq '.items[] | select(any(.spec.containers[]; .securityContext.privileged==true))'` and capture exact status/reason/request ID. hostNetwork/PID/IPC/hostPath expose shared host attack surface. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### POD-AND-NODE-WORKLOAD-SECURITY-JP-08

- [ ] **Question:** A basic Pod Security Standards check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl apply --dry-run=server -f pod.yaml` and capture exact status/reason/request ID. privileged/baseline/restricted profiles define portable control sets. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### POD-AND-NODE-WORKLOAD-SECURITY-JP-09

- [ ] **Question:** A basic Pod Security Admission check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ns --show-labels` and capture exact status/reason/request ID. namespace labels enforce/audit/warn standards by version. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### POD-AND-NODE-WORKLOAD-SECURITY-JP-10

- [ ] **Code:** **Question:** A basic Node hardening check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl label ns NS pod-security.kubernetes.io/enforce=restricted` and capture exact status/reason/request ID. kernel/runtime/kubelet/metadata/patch and tenant separation remain outside Pod spec. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### POD-AND-NODE-WORKLOAD-SECURITY-MN-01

- [ ] **Question:** Compare runAsNonRoot with allowPrivilegeEscalation. When would each change your design?

**Answer:** runAsNonRoot: prevents UID 0 execution when image/runtime identity can be determined. allowPrivilegeEscalation: blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### POD-AND-NODE-WORKLOAD-SECURITY-MN-02

- [ ] **Question:** Compare allowPrivilegeEscalation with Capabilities. When would each change your design?

**Answer:** allowPrivilegeEscalation: blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. Capabilities: drop ALL and add only exact kernel privileges required. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### POD-AND-NODE-WORKLOAD-SECURITY-MN-03

- [ ] **Question:** Compare Capabilities with Seccomp. When would each change your design?

**Answer:** Capabilities: drop ALL and add only exact kernel privileges required. Seccomp: RuntimeDefault/local profiles reduce syscall attack surface. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### POD-AND-NODE-WORKLOAD-SECURITY-MN-04

- [ ] **Configuration review:** **Question:** Compare Seccomp with Read-only root. When would each change your design?

**Answer:** Seccomp: RuntimeDefault/local profiles reduce syscall attack surface. Read-only root: prevents image filesystem mutation and requires explicit writable volumes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### POD-AND-NODE-WORKLOAD-SECURITY-MN-05

- [ ] **Question:** Compare Read-only root with Privileged container. When would each change your design?

**Answer:** Read-only root: prevents image filesystem mutation and requires explicit writable volumes. Privileged container: largely bypasses container isolation and is equivalent to host-level trust. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### POD-AND-NODE-WORKLOAD-SECURITY-MN-06

- [ ] **Question:** Compare Privileged container with Host namespaces/path. When would each change your design?

**Answer:** Privileged container: largely bypasses container isolation and is equivalent to host-level trust. Host namespaces/path: hostNetwork/PID/IPC/hostPath expose shared host attack surface. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### POD-AND-NODE-WORKLOAD-SECURITY-MN-07

- [ ] **Configuration review:** **Question:** Compare Host namespaces/path with Pod Security Standards. When would each change your design?

**Answer:** Host namespaces/path: hostNetwork/PID/IPC/hostPath expose shared host attack surface. Pod Security Standards: privileged/baseline/restricted profiles define portable control sets. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### POD-AND-NODE-WORKLOAD-SECURITY-MN-08

- [ ] **Question:** Compare Pod Security Standards with Pod Security Admission. When would each change your design?

**Answer:** Pod Security Standards: privileged/baseline/restricted profiles define portable control sets. Pod Security Admission: namespace labels enforce/audit/warn standards by version. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### POD-AND-NODE-WORKLOAD-SECURITY-MN-09

- [ ] **Question:** Compare Pod Security Admission with Node hardening. When would each change your design?

**Answer:** Pod Security Admission: namespace labels enforce/audit/warn standards by version. Node hardening: kernel/runtime/kubelet/metadata/patch and tenant separation remain outside Pod spec. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### POD-AND-NODE-WORKLOAD-SECURITY-MN-10

- [ ] **Configuration review:** **Question:** Compare Node hardening with runAsNonRoot. When would each change your design?

**Answer:** Node hardening: kernel/runtime/kubelet/metadata/patch and tenant separation remain outside Pod spec. runAsNonRoot: prevents UID 0 execution when image/runtime identity can be determined. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### POD-AND-NODE-WORKLOAD-SECURITY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around runAsNonRoot; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ns --show-labels` plus recent events/changes, then correlate the service-specific SLI. prevents UID 0 execution when image/runtime identity can be determined. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### POD-AND-NODE-WORKLOAD-SECURITY-MP-02

- [ ] **Question:** Production is degraded around allowPrivilegeEscalation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl label ns NS pod-security.kubernetes.io/enforce=restricted` plus recent events/changes, then correlate the service-specific SLI. blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### POD-AND-NODE-WORKLOAD-SECURITY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Capabilities; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o json | jq '.items[] | select(any(.spec.containers[]; .securityContext.privileged==true))'` plus recent events/changes, then correlate the service-specific SLI. drop ALL and add only exact kernel privileges required. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### POD-AND-NODE-WORKLOAD-SECURITY-MP-04

- [ ] **Question:** Production is degraded around Seccomp; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl apply --dry-run=server -f pod.yaml` plus recent events/changes, then correlate the service-specific SLI. RuntimeDefault/local profiles reduce syscall attack surface. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### POD-AND-NODE-WORKLOAD-SECURITY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Read-only root; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ns --show-labels` plus recent events/changes, then correlate the service-specific SLI. prevents image filesystem mutation and requires explicit writable volumes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### POD-AND-NODE-WORKLOAD-SECURITY-MP-06

- [ ] **Question:** Production is degraded around Privileged container; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl label ns NS pod-security.kubernetes.io/enforce=restricted` plus recent events/changes, then correlate the service-specific SLI. largely bypasses container isolation and is equivalent to host-level trust. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### POD-AND-NODE-WORKLOAD-SECURITY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Host namespaces/path; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o json | jq '.items[] | select(any(.spec.containers[]; .securityContext.privileged==true))'` plus recent events/changes, then correlate the service-specific SLI. hostNetwork/PID/IPC/hostPath expose shared host attack surface. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### POD-AND-NODE-WORKLOAD-SECURITY-MP-08

- [ ] **Question:** Production is degraded around Pod Security Standards; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl apply --dry-run=server -f pod.yaml` plus recent events/changes, then correlate the service-specific SLI. privileged/baseline/restricted profiles define portable control sets. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### POD-AND-NODE-WORKLOAD-SECURITY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pod Security Admission; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ns --show-labels` plus recent events/changes, then correlate the service-specific SLI. namespace labels enforce/audit/warn standards by version. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### POD-AND-NODE-WORKLOAD-SECURITY-MP-10

- [ ] **Question:** Production is degraded around Node hardening; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl label ns NS pod-security.kubernetes.io/enforce=restricted` plus recent events/changes, then correlate the service-specific SLI. kernel/runtime/kubelet/metadata/patch and tenant separation remain outside Pod spec. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### POD-AND-NODE-WORKLOAD-SECURITY-SN-01

- [ ] **Question:** Design a production Pod and node workload security capability where runAsNonRoot, Seccomp and Host namespaces/path are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prevents UID 0 execution when image/runtime identity can be determined. RuntimeDefault/local profiles reduce syscall attack surface. hostNetwork/PID/IPC/hostPath expose shared host attack surface. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### POD-AND-NODE-WORKLOAD-SECURITY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Pod and node workload security capability where allowPrivilegeEscalation, Read-only root and Pod Security Standards are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. prevents image filesystem mutation and requires explicit writable volumes. privileged/baseline/restricted profiles define portable control sets. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### POD-AND-NODE-WORKLOAD-SECURITY-SN-03

- [ ] **Question:** Design a production Pod and node workload security capability where Capabilities, Privileged container and Pod Security Admission are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: drop ALL and add only exact kernel privileges required. largely bypasses container isolation and is equivalent to host-level trust. namespace labels enforce/audit/warn standards by version. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### POD-AND-NODE-WORKLOAD-SECURITY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Pod and node workload security capability where Seccomp, Host namespaces/path and Node hardening are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: RuntimeDefault/local profiles reduce syscall attack surface. hostNetwork/PID/IPC/hostPath expose shared host attack surface. kernel/runtime/kubelet/metadata/patch and tenant separation remain outside Pod spec. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### POD-AND-NODE-WORKLOAD-SECURITY-SN-05

- [ ] **Question:** Design a production Pod and node workload security capability where Read-only root, Pod Security Standards and runAsNonRoot are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prevents image filesystem mutation and requires explicit writable volumes. privileged/baseline/restricted profiles define portable control sets. prevents UID 0 execution when image/runtime identity can be determined. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### POD-AND-NODE-WORKLOAD-SECURITY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Pod and node workload security capability where Privileged container, Pod Security Admission and allowPrivilegeEscalation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: largely bypasses container isolation and is equivalent to host-level trust. namespace labels enforce/audit/warn standards by version. blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### POD-AND-NODE-WORKLOAD-SECURITY-SN-07

- [ ] **Question:** Design a production Pod and node workload security capability where Host namespaces/path, Node hardening and Capabilities are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: hostNetwork/PID/IPC/hostPath expose shared host attack surface. kernel/runtime/kubelet/metadata/patch and tenant separation remain outside Pod spec. drop ALL and add only exact kernel privileges required. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### POD-AND-NODE-WORKLOAD-SECURITY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Pod and node workload security capability where Pod Security Standards, runAsNonRoot and Seccomp are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: privileged/baseline/restricted profiles define portable control sets. prevents UID 0 execution when image/runtime identity can be determined. RuntimeDefault/local profiles reduce syscall attack surface. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### POD-AND-NODE-WORKLOAD-SECURITY-SN-09

- [ ] **Question:** Design a production Pod and node workload security capability where Pod Security Admission, allowPrivilegeEscalation and Read-only root are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: namespace labels enforce/audit/warn standards by version. blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. prevents image filesystem mutation and requires explicit writable volumes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### POD-AND-NODE-WORKLOAD-SECURITY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Pod and node workload security capability where Node hardening, Capabilities and Privileged container are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: kernel/runtime/kubelet/metadata/patch and tenant separation remain outside Pod spec. drop ALL and add only exact kernel privileges required. largely bypasses container isolation and is equivalent to host-level trust. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### POD-AND-NODE-WORKLOAD-SECURITY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving runAsNonRoot. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ns --show-labels` as one read-only checkpoint, not the whole diagnosis. prevents UID 0 execution when image/runtime identity can be determined. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### POD-AND-NODE-WORKLOAD-SECURITY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving allowPrivilegeEscalation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl label ns NS pod-security.kubernetes.io/enforce=restricted` as one read-only checkpoint, not the whole diagnosis. blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### POD-AND-NODE-WORKLOAD-SECURITY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Capabilities. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o json | jq '.items[] | select(any(.spec.containers[]; .securityContext.privileged==true))'` as one read-only checkpoint, not the whole diagnosis. drop ALL and add only exact kernel privileges required. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### POD-AND-NODE-WORKLOAD-SECURITY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Seccomp. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl apply --dry-run=server -f pod.yaml` as one read-only checkpoint, not the whole diagnosis. RuntimeDefault/local profiles reduce syscall attack surface. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### POD-AND-NODE-WORKLOAD-SECURITY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Read-only root. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ns --show-labels` as one read-only checkpoint, not the whole diagnosis. prevents image filesystem mutation and requires explicit writable volumes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### POD-AND-NODE-WORKLOAD-SECURITY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Privileged container. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl label ns NS pod-security.kubernetes.io/enforce=restricted` as one read-only checkpoint, not the whole diagnosis. largely bypasses container isolation and is equivalent to host-level trust. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### POD-AND-NODE-WORKLOAD-SECURITY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Host namespaces/path. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o json | jq '.items[] | select(any(.spec.containers[]; .securityContext.privileged==true))'` as one read-only checkpoint, not the whole diagnosis. hostNetwork/PID/IPC/hostPath expose shared host attack surface. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### POD-AND-NODE-WORKLOAD-SECURITY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod Security Standards. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl apply --dry-run=server -f pod.yaml` as one read-only checkpoint, not the whole diagnosis. privileged/baseline/restricted profiles define portable control sets. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### POD-AND-NODE-WORKLOAD-SECURITY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod Security Admission. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ns --show-labels` as one read-only checkpoint, not the whole diagnosis. namespace labels enforce/audit/warn standards by version. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### POD-AND-NODE-WORKLOAD-SECURITY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node hardening. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl label ns NS pod-security.kubernetes.io/enforce=restricted` as one read-only checkpoint, not the whole diagnosis. kernel/runtime/kubelet/metadata/patch and tenant separation remain outside Pod spec. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
