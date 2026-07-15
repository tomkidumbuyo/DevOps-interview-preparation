# Kubernetes Secrets and ConfigMaps — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JN-01

- [ ] **Question:** What is ConfigMap, and why does it matter in Kubernetes Secrets and ConfigMaps?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** non-secret key/file configuration consumed via API, env or projected volume. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JN-02

- [ ] **Question:** What is Secret, and why does it matter in Kubernetes Secrets and ConfigMaps?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** API object whose data is base64-encoded and requires encryption/RBAC controls. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JN-03

- [ ] **Question:** What is Environment consumption, and why does it matter in Kubernetes Secrets and ConfigMaps?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** value is fixed at process start and appears in process/runtime surfaces. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JN-04

- [ ] **Question:** What is Projected volume, and why does it matter in Kubernetes Secrets and ConfigMaps?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** kubelet updates mounted data eventually using atomic directory/symlink behavior. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JN-05

- [ ] **Question:** What is subPath, and why does it matter in Kubernetes Secrets and ConfigMaps?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** individual file mount does not receive ordinary projected updates. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JN-06

- [ ] **Question:** What is Immutable object, and why does it matter in Kubernetes Secrets and ConfigMaps?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** prevents accidental mutation and can improve watch load; version name for changes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JN-07

- [ ] **Question:** What is Encryption at rest, and why does it matter in Kubernetes Secrets and ConfigMaps?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** API server provider encrypts selected resources in etcd with key rotation procedure. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JN-08

- [ ] **Code:** **Question:** What does `kubectl create configmap NAME --from-file=config.yaml --dry-run=client -o yaml` help you verify for Kubernetes Secrets and ConfigMaps?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: synchronizes or mounts secret-manager values with availability/identity trade-offs.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get configmap,secret -n NS` help you verify for Kubernetes Secrets and ConfigMaps?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: dual credential/version, reload/restart and dependent revocation must avoid outage.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JN-10

- [ ] **Code:** **Question:** What does `kubectl get secret NAME -n NS -o jsonpath='{.data.KEY}' | base64 -d` help you verify for Kubernetes Secrets and ConfigMaps?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: template annotation hash deliberately restarts Pods on immutable/config change.

## Junior — procedural and command questions

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JP-01

- [ ] **Code:** **Question:** A basic ConfigMap check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get configmap,secret -n NS` and capture exact status/reason/request ID. non-secret key/file configuration consumed via API, env or projected volume. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JP-02

- [ ] **Question:** A basic Secret check fails. What would you do first?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get secret NAME -n NS -o jsonpath='{.data.KEY}' | base64 -d` and capture exact status/reason/request ID. API object whose data is base64-encoded and requires encryption/RBAC controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JP-03

- [ ] **Question:** A basic Environment consumption check fails. What would you do first?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth can-i get secrets --as=system:serviceaccount:NS:SA -n NS` and capture exact status/reason/request ID. value is fixed at process start and appears in process/runtime surfaces. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JP-04

- [ ] **Code:** **Question:** A basic Projected volume check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl create configmap NAME --from-file=config.yaml --dry-run=client -o yaml` and capture exact status/reason/request ID. kubelet updates mounted data eventually using atomic directory/symlink behavior. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JP-05

- [ ] **Question:** A basic subPath check fails. What would you do first?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get configmap,secret -n NS` and capture exact status/reason/request ID. individual file mount does not receive ordinary projected updates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JP-06

- [ ] **Question:** A basic Immutable object check fails. What would you do first?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get secret NAME -n NS -o jsonpath='{.data.KEY}' | base64 -d` and capture exact status/reason/request ID. prevents accidental mutation and can improve watch load; version name for changes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JP-07

- [ ] **Code:** **Question:** A basic Encryption at rest check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth can-i get secrets --as=system:serviceaccount:NS:SA -n NS` and capture exact status/reason/request ID. API server provider encrypts selected resources in etcd with key rotation procedure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JP-08

- [ ] **Question:** A basic External secrets/CSI check fails. What would you do first?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl create configmap NAME --from-file=config.yaml --dry-run=client -o yaml` and capture exact status/reason/request ID. synchronizes or mounts secret-manager values with availability/identity trade-offs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JP-09

- [ ] **Question:** A basic Rotation check fails. What would you do first?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get configmap,secret -n NS` and capture exact status/reason/request ID. dual credential/version, reload/restart and dependent revocation must avoid outage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-JP-10

- [ ] **Code:** **Question:** A basic Checksum rollout check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get secret NAME -n NS -o jsonpath='{.data.KEY}' | base64 -d` and capture exact status/reason/request ID. template annotation hash deliberately restarts Pods on immutable/config change. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MN-01

- [ ] **Question:** Compare ConfigMap with Secret. When would each change your design?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** ConfigMap: non-secret key/file configuration consumed via API, env or projected volume. Secret: API object whose data is base64-encoded and requires encryption/RBAC controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MN-02

- [ ] **Question:** Compare Secret with Environment consumption. When would each change your design?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Secret: API object whose data is base64-encoded and requires encryption/RBAC controls. Environment consumption: value is fixed at process start and appears in process/runtime surfaces. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MN-03

- [ ] **Question:** Compare Environment consumption with Projected volume. When would each change your design?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Environment consumption: value is fixed at process start and appears in process/runtime surfaces. Projected volume: kubelet updates mounted data eventually using atomic directory/symlink behavior. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MN-04

- [ ] **Configuration review:** **Question:** Compare Projected volume with subPath. When would each change your design?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Projected volume: kubelet updates mounted data eventually using atomic directory/symlink behavior. subPath: individual file mount does not receive ordinary projected updates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MN-05

- [ ] **Question:** Compare subPath with Immutable object. When would each change your design?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** subPath: individual file mount does not receive ordinary projected updates. Immutable object: prevents accidental mutation and can improve watch load; version name for changes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MN-06

- [ ] **Question:** Compare Immutable object with Encryption at rest. When would each change your design?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Immutable object: prevents accidental mutation and can improve watch load; version name for changes. Encryption at rest: API server provider encrypts selected resources in etcd with key rotation procedure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MN-07

- [ ] **Configuration review:** **Question:** Compare Encryption at rest with External secrets/CSI. When would each change your design?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Encryption at rest: API server provider encrypts selected resources in etcd with key rotation procedure. External secrets/CSI: synchronizes or mounts secret-manager values with availability/identity trade-offs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MN-08

- [ ] **Question:** Compare External secrets/CSI with Rotation. When would each change your design?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** External secrets/CSI: synchronizes or mounts secret-manager values with availability/identity trade-offs. Rotation: dual credential/version, reload/restart and dependent revocation must avoid outage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MN-09

- [ ] **Question:** Compare Rotation with Checksum rollout. When would each change your design?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Rotation: dual credential/version, reload/restart and dependent revocation must avoid outage. Checksum rollout: template annotation hash deliberately restarts Pods on immutable/config change. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MN-10

- [ ] **Configuration review:** **Question:** Compare Checksum rollout with ConfigMap. When would each change your design?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Checksum rollout: template annotation hash deliberately restarts Pods on immutable/config change. ConfigMap: non-secret key/file configuration consumed via API, env or projected volume. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around ConfigMap; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get configmap,secret -n NS` plus recent events/changes, then correlate the service-specific SLI. non-secret key/file configuration consumed via API, env or projected volume. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MP-02

- [ ] **Question:** Production is degraded around Secret; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get secret NAME -n NS -o jsonpath='{.data.KEY}' | base64 -d` plus recent events/changes, then correlate the service-specific SLI. API object whose data is base64-encoded and requires encryption/RBAC controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Environment consumption; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth can-i get secrets --as=system:serviceaccount:NS:SA -n NS` plus recent events/changes, then correlate the service-specific SLI. value is fixed at process start and appears in process/runtime surfaces. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MP-04

- [ ] **Question:** Production is degraded around Projected volume; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl create configmap NAME --from-file=config.yaml --dry-run=client -o yaml` plus recent events/changes, then correlate the service-specific SLI. kubelet updates mounted data eventually using atomic directory/symlink behavior. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around subPath; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get configmap,secret -n NS` plus recent events/changes, then correlate the service-specific SLI. individual file mount does not receive ordinary projected updates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MP-06

- [ ] **Question:** Production is degraded around Immutable object; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get secret NAME -n NS -o jsonpath='{.data.KEY}' | base64 -d` plus recent events/changes, then correlate the service-specific SLI. prevents accidental mutation and can improve watch load; version name for changes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Encryption at rest; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth can-i get secrets --as=system:serviceaccount:NS:SA -n NS` plus recent events/changes, then correlate the service-specific SLI. API server provider encrypts selected resources in etcd with key rotation procedure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MP-08

- [ ] **Question:** Production is degraded around External secrets/CSI; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl create configmap NAME --from-file=config.yaml --dry-run=client -o yaml` plus recent events/changes, then correlate the service-specific SLI. synchronizes or mounts secret-manager values with availability/identity trade-offs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Rotation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get configmap,secret -n NS` plus recent events/changes, then correlate the service-specific SLI. dual credential/version, reload/restart and dependent revocation must avoid outage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-MP-10

- [ ] **Question:** Production is degraded around Checksum rollout; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get secret NAME -n NS -o jsonpath='{.data.KEY}' | base64 -d` plus recent events/changes, then correlate the service-specific SLI. template annotation hash deliberately restarts Pods on immutable/config change. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SN-01

- [ ] **Question:** Design a production Kubernetes Secrets and ConfigMaps capability where ConfigMap, Projected volume and Encryption at rest are first-class requirements.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: non-secret key/file configuration consumed via API, env or projected volume. kubelet updates mounted data eventually using atomic directory/symlink behavior. API server provider encrypts selected resources in etcd with key rotation procedure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes Secrets and ConfigMaps capability where Secret, subPath and External secrets/CSI are first-class requirements.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: API object whose data is base64-encoded and requires encryption/RBAC controls. individual file mount does not receive ordinary projected updates. synchronizes or mounts secret-manager values with availability/identity trade-offs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SN-03

- [ ] **Question:** Design a production Kubernetes Secrets and ConfigMaps capability where Environment consumption, Immutable object and Rotation are first-class requirements.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: value is fixed at process start and appears in process/runtime surfaces. prevents accidental mutation and can improve watch load; version name for changes. dual credential/version, reload/restart and dependent revocation must avoid outage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes Secrets and ConfigMaps capability where Projected volume, Encryption at rest and Checksum rollout are first-class requirements.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: kubelet updates mounted data eventually using atomic directory/symlink behavior. API server provider encrypts selected resources in etcd with key rotation procedure. template annotation hash deliberately restarts Pods on immutable/config change. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SN-05

- [ ] **Question:** Design a production Kubernetes Secrets and ConfigMaps capability where subPath, External secrets/CSI and ConfigMap are first-class requirements.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: individual file mount does not receive ordinary projected updates. synchronizes or mounts secret-manager values with availability/identity trade-offs. non-secret key/file configuration consumed via API, env or projected volume. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes Secrets and ConfigMaps capability where Immutable object, Rotation and Secret are first-class requirements.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prevents accidental mutation and can improve watch load; version name for changes. dual credential/version, reload/restart and dependent revocation must avoid outage. API object whose data is base64-encoded and requires encryption/RBAC controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SN-07

- [ ] **Question:** Design a production Kubernetes Secrets and ConfigMaps capability where Encryption at rest, Checksum rollout and Environment consumption are first-class requirements.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: API server provider encrypts selected resources in etcd with key rotation procedure. template annotation hash deliberately restarts Pods on immutable/config change. value is fixed at process start and appears in process/runtime surfaces. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes Secrets and ConfigMaps capability where External secrets/CSI, ConfigMap and Projected volume are first-class requirements.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: synchronizes or mounts secret-manager values with availability/identity trade-offs. non-secret key/file configuration consumed via API, env or projected volume. kubelet updates mounted data eventually using atomic directory/symlink behavior. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SN-09

- [ ] **Question:** Design a production Kubernetes Secrets and ConfigMaps capability where Rotation, Secret and subPath are first-class requirements.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: dual credential/version, reload/restart and dependent revocation must avoid outage. API object whose data is base64-encoded and requires encryption/RBAC controls. individual file mount does not receive ordinary projected updates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes Secrets and ConfigMaps capability where Checksum rollout, Environment consumption and Immutable object are first-class requirements.
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: template annotation hash deliberately restarts Pods on immutable/config change. value is fixed at process start and appears in process/runtime surfaces. prevents accidental mutation and can improve watch load; version name for changes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ConfigMap. How do you lead it end to end?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get configmap,secret -n NS` as one read-only checkpoint, not the whole diagnosis. non-secret key/file configuration consumed via API, env or projected volume. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secret. How do you lead it end to end?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get secret NAME -n NS -o jsonpath='{.data.KEY}' | base64 -d` as one read-only checkpoint, not the whole diagnosis. API object whose data is base64-encoded and requires encryption/RBAC controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Environment consumption. How do you lead it end to end?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth can-i get secrets --as=system:serviceaccount:NS:SA -n NS` as one read-only checkpoint, not the whole diagnosis. value is fixed at process start and appears in process/runtime surfaces. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Projected volume. How do you lead it end to end?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl create configmap NAME --from-file=config.yaml --dry-run=client -o yaml` as one read-only checkpoint, not the whole diagnosis. kubelet updates mounted data eventually using atomic directory/symlink behavior. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving subPath. How do you lead it end to end?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get configmap,secret -n NS` as one read-only checkpoint, not the whole diagnosis. individual file mount does not receive ordinary projected updates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Immutable object. How do you lead it end to end?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get secret NAME -n NS -o jsonpath='{.data.KEY}' | base64 -d` as one read-only checkpoint, not the whole diagnosis. prevents accidental mutation and can improve watch load; version name for changes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Encryption at rest. How do you lead it end to end?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth can-i get secrets --as=system:serviceaccount:NS:SA -n NS` as one read-only checkpoint, not the whole diagnosis. API server provider encrypts selected resources in etcd with key rotation procedure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving External secrets/CSI. How do you lead it end to end?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl create configmap NAME --from-file=config.yaml --dry-run=client -o yaml` as one read-only checkpoint, not the whole diagnosis. synchronizes or mounts secret-manager values with availability/identity trade-offs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rotation. How do you lead it end to end?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get configmap,secret -n NS` as one read-only checkpoint, not the whole diagnosis. dual credential/version, reload/restart and dependent revocation must avoid outage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-SECRETS-AND-CONFIGMAPS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Checksum rollout. How do you lead it end to end?
> **Covered in:** [Kubernetes Secrets and ConfigMaps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get secret NAME -n NS -o jsonpath='{.data.KEY}' | base64 -d` as one read-only checkpoint, not the whole diagnosis. template annotation hash deliberately restarts Pods on immutable/config change. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Pod and node workload security](../02-pod-security/README.md) · [Study note](README.md) · [Next: Kubernetes admission policies and webhooks →](../04-admission-policies-webhooks/README.md)

<!-- reading-navigation:end -->
