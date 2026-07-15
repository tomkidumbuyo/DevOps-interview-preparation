# Security — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-SECURITY-JN-01

- [ ] **Question:** What is Authentication, and why does it matter in Security?
> **Covered in:** [Security — Security model](README.md#security-model)

**Answer:** client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-JN-02

- [ ] **Question:** What is Authorization, and why does it matter in Security?
> **Covered in:** [Security — Security model](README.md#security-model)

**Answer:** RBAC/webhook/node/ABAC modes decide a request after authentication. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-JN-03

- [ ] **Question:** What is runAsNonRoot, and why does it matter in Security?
> **Covered in:** [Security — Security model](README.md#security-model)

**Answer:** prevents UID 0 execution when image/runtime identity can be determined. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-JN-04

- [ ] **Question:** What is allowPrivilegeEscalation, and why does it matter in Security?
> **Covered in:** [Security — Security model](README.md#security-model)

**Answer:** blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-JN-05

- [ ] **Question:** What is ConfigMap, and why does it matter in Security?
> **Covered in:** [Security — Security model](README.md#security-model)

**Answer:** non-secret key/file configuration consumed via API, env or projected volume. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-JN-06

- [ ] **Question:** What is Secret, and why does it matter in Security?
> **Covered in:** [Security — Security model](README.md#security-model)

**Answer:** API object whose data is base64-encoded and requires encryption/RBAC controls. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-JN-07

- [ ] **Question:** What is Admission sequence, and why does it matter in Security?
> **Covered in:** [Security — Security model](README.md#security-model)

**Answer:** mutation precedes object schema/defaulting stages and validation before persistence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-JN-08

- [ ] **Code:** **Question:** What does `kubectl get configmap,secret -n NS` help you verify for Security?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: CEL policy in API server avoids external webhook network dependency.

### BRANCH-SECURITY-JN-09

- [ ] **Code:** **Question:** What does `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` help you verify for Security?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins.

### BRANCH-SECURITY-JN-10

- [ ] **Code:** **Question:** What does `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` help you verify for Security?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: stronger failure/control isolation at fleet cost and operational scale.

## Junior — procedural and command questions

### BRANCH-SECURITY-JP-01

- [ ] **Code:** **Question:** A basic Authentication check fails. What would you do first using the CLI?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth whoami` and capture exact status/reason/request ID. client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-JP-02

- [ ] **Question:** A basic Authorization check fails. What would you do first?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ns --show-labels` and capture exact status/reason/request ID. RBAC/webhook/node/ABAC modes decide a request after authentication. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-JP-03

- [ ] **Question:** A basic runAsNonRoot check fails. What would you do first?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get configmap,secret -n NS` and capture exact status/reason/request ID. prevents UID 0 execution when image/runtime identity can be determined. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-JP-04

- [ ] **Code:** **Question:** A basic allowPrivilegeEscalation check fails. What would you do first using the CLI?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` and capture exact status/reason/request ID. blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-JP-05

- [ ] **Question:** A basic ConfigMap check fails. What would you do first?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` and capture exact status/reason/request ID. non-secret key/file configuration consumed via API, env or projected volume. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-JP-06

- [ ] **Question:** A basic Secret check fails. What would you do first?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth whoami` and capture exact status/reason/request ID. API object whose data is base64-encoded and requires encryption/RBAC controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-JP-07

- [ ] **Code:** **Question:** A basic Admission sequence check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes admission policies and webhooks — Command lab](04-admission-policies-webhooks/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ns --show-labels` and capture exact status/reason/request ID. mutation precedes object schema/defaulting stages and validation before persistence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-JP-08

- [ ] **Question:** A basic ValidatingAdmissionPolicy check fails. What would you do first?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get configmap,secret -n NS` and capture exact status/reason/request ID. CEL policy in API server avoids external webhook network dependency. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-JP-09

- [ ] **Question:** A basic Namespace tenancy check fails. What would you do first?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` and capture exact status/reason/request ID. soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-JP-10

- [ ] **Code:** **Question:** A basic Cluster-per-tenant check fails. What would you do first using the CLI?
> **Covered in:** [Security — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` and capture exact status/reason/request ID. stronger failure/control isolation at fleet cost and operational scale. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-SECURITY-MN-01

- [ ] **Question:** Compare Authentication with Authorization. When would each change your design?
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Authentication: client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Authorization: RBAC/webhook/node/ABAC modes decide a request after authentication. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-MN-02

- [ ] **Question:** Compare Authorization with runAsNonRoot. When would each change your design?
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Authorization: RBAC/webhook/node/ABAC modes decide a request after authentication. runAsNonRoot: prevents UID 0 execution when image/runtime identity can be determined. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-MN-03

- [ ] **Question:** Compare runAsNonRoot with allowPrivilegeEscalation. When would each change your design?
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** runAsNonRoot: prevents UID 0 execution when image/runtime identity can be determined. allowPrivilegeEscalation: blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-MN-04

- [ ] **Configuration review:** **Question:** Compare allowPrivilegeEscalation with ConfigMap. When would each change your design?
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** allowPrivilegeEscalation: blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. ConfigMap: non-secret key/file configuration consumed via API, env or projected volume. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-MN-05

- [ ] **Question:** Compare ConfigMap with Secret. When would each change your design?
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ConfigMap: non-secret key/file configuration consumed via API, env or projected volume. Secret: API object whose data is base64-encoded and requires encryption/RBAC controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-MN-06

- [ ] **Question:** Compare Secret with Admission sequence. When would each change your design?
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Secret: API object whose data is base64-encoded and requires encryption/RBAC controls. Admission sequence: mutation precedes object schema/defaulting stages and validation before persistence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-MN-07

- [ ] **Configuration review:** **Question:** Compare Admission sequence with ValidatingAdmissionPolicy. When would each change your design?
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Admission sequence: mutation precedes object schema/defaulting stages and validation before persistence. ValidatingAdmissionPolicy: CEL policy in API server avoids external webhook network dependency. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-MN-08

- [ ] **Question:** Compare ValidatingAdmissionPolicy with Namespace tenancy. When would each change your design?
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ValidatingAdmissionPolicy: CEL policy in API server avoids external webhook network dependency. Namespace tenancy: soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-MN-09

- [ ] **Question:** Compare Namespace tenancy with Cluster-per-tenant. When would each change your design?
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Namespace tenancy: soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Cluster-per-tenant: stronger failure/control isolation at fleet cost and operational scale. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-MN-10

- [ ] **Configuration review:** **Question:** Compare Cluster-per-tenant with Authentication. When would each change your design?
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Cluster-per-tenant: stronger failure/control isolation at fleet cost and operational scale. Authentication: client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-SECURITY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Authentication; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth whoami` plus recent events/changes, then correlate the service-specific SLI. client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-MP-02

- [ ] **Question:** Production is degraded around Authorization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ns --show-labels` plus recent events/changes, then correlate the service-specific SLI. RBAC/webhook/node/ABAC modes decide a request after authentication. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around runAsNonRoot; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get configmap,secret -n NS` plus recent events/changes, then correlate the service-specific SLI. prevents UID 0 execution when image/runtime identity can be determined. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-MP-04

- [ ] **Question:** Production is degraded around allowPrivilegeEscalation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` plus recent events/changes, then correlate the service-specific SLI. blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around ConfigMap; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` plus recent events/changes, then correlate the service-specific SLI. non-secret key/file configuration consumed via API, env or projected volume. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-MP-06

- [ ] **Question:** Production is degraded around Secret; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth whoami` plus recent events/changes, then correlate the service-specific SLI. API object whose data is base64-encoded and requires encryption/RBAC controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Admission sequence; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ns --show-labels` plus recent events/changes, then correlate the service-specific SLI. mutation precedes object schema/defaulting stages and validation before persistence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-MP-08

- [ ] **Question:** Production is degraded around ValidatingAdmissionPolicy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get configmap,secret -n NS` plus recent events/changes, then correlate the service-specific SLI. CEL policy in API server avoids external webhook network dependency. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Namespace tenancy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` plus recent events/changes, then correlate the service-specific SLI. soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-MP-10

- [ ] **Question:** Production is degraded around Cluster-per-tenant; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` plus recent events/changes, then correlate the service-specific SLI. stronger failure/control isolation at fleet cost and operational scale. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-SECURITY-SN-01

- [ ] **Question:** Design a production Security capability where Authentication, allowPrivilegeEscalation and Admission sequence are first-class requirements.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. mutation precedes object schema/defaulting stages and validation before persistence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Security capability where Authorization, ConfigMap and ValidatingAdmissionPolicy are first-class requirements.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: RBAC/webhook/node/ABAC modes decide a request after authentication. non-secret key/file configuration consumed via API, env or projected volume. CEL policy in API server avoids external webhook network dependency. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-SN-03

- [ ] **Question:** Design a production Security capability where runAsNonRoot, Secret and Namespace tenancy are first-class requirements.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prevents UID 0 execution when image/runtime identity can be determined. API object whose data is base64-encoded and requires encryption/RBAC controls. soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Security capability where allowPrivilegeEscalation, Admission sequence and Cluster-per-tenant are first-class requirements.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. mutation precedes object schema/defaulting stages and validation before persistence. stronger failure/control isolation at fleet cost and operational scale. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-SN-05

- [ ] **Question:** Design a production Security capability where ConfigMap, ValidatingAdmissionPolicy and Authentication are first-class requirements.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: non-secret key/file configuration consumed via API, env or projected volume. CEL policy in API server avoids external webhook network dependency. client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Security capability where Secret, Namespace tenancy and Authorization are first-class requirements.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: API object whose data is base64-encoded and requires encryption/RBAC controls. soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. RBAC/webhook/node/ABAC modes decide a request after authentication. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-SN-07

- [ ] **Question:** Design a production Security capability where Admission sequence, Cluster-per-tenant and runAsNonRoot are first-class requirements.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: mutation precedes object schema/defaulting stages and validation before persistence. stronger failure/control isolation at fleet cost and operational scale. prevents UID 0 execution when image/runtime identity can be determined. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Security capability where ValidatingAdmissionPolicy, Authentication and allowPrivilegeEscalation are first-class requirements.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: CEL policy in API server avoids external webhook network dependency. client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-SN-09

- [ ] **Question:** Design a production Security capability where Namespace tenancy, Authorization and ConfigMap are first-class requirements.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. RBAC/webhook/node/ABAC modes decide a request after authentication. non-secret key/file configuration consumed via API, env or projected volume. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Security capability where Cluster-per-tenant, runAsNonRoot and Secret are first-class requirements.
> **Covered in:** [Security — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stronger failure/control isolation at fleet cost and operational scale. prevents UID 0 execution when image/runtime identity can be determined. API object whose data is base64-encoded and requires encryption/RBAC controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-SECURITY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authentication. How do you lead it end to end?
> **Covered in:** [Security — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth whoami` as one read-only checkpoint, not the whole diagnosis. client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authorization. How do you lead it end to end?
> **Covered in:** [Security — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ns --show-labels` as one read-only checkpoint, not the whole diagnosis. RBAC/webhook/node/ABAC modes decide a request after authentication. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving runAsNonRoot. How do you lead it end to end?
> **Covered in:** [Security — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get configmap,secret -n NS` as one read-only checkpoint, not the whole diagnosis. prevents UID 0 execution when image/runtime identity can be determined. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving allowPrivilegeEscalation. How do you lead it end to end?
> **Covered in:** [Security — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` as one read-only checkpoint, not the whole diagnosis. blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ConfigMap. How do you lead it end to end?
> **Covered in:** [Security — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` as one read-only checkpoint, not the whole diagnosis. non-secret key/file configuration consumed via API, env or projected volume. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secret. How do you lead it end to end?
> **Covered in:** [Security — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth whoami` as one read-only checkpoint, not the whole diagnosis. API object whose data is base64-encoded and requires encryption/RBAC controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Admission sequence. How do you lead it end to end?
> **Covered in:** [Security — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ns --show-labels` as one read-only checkpoint, not the whole diagnosis. mutation precedes object schema/defaulting stages and validation before persistence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ValidatingAdmissionPolicy. How do you lead it end to end?
> **Covered in:** [Security — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get configmap,secret -n NS` as one read-only checkpoint, not the whole diagnosis. CEL policy in API server avoids external webhook network dependency. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Namespace tenancy. How do you lead it end to end?
> **Covered in:** [Security — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` as one read-only checkpoint, not the whole diagnosis. soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cluster-per-tenant. How do you lead it end to end?
> **Covered in:** [Security — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` as one read-only checkpoint, not the whole diagnosis. stronger failure/control isolation at fleet cost and operational scale. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: CSI, snapshots and Kubernetes backup](../04-storage/02-csi-snapshots-backup/README.md) · [Study note](README.md) · [Next: Kubernetes authentication, RBAC and ServiceAccounts →](01-authn-rbac-serviceaccounts/README.md)

<!-- reading-navigation:end -->
