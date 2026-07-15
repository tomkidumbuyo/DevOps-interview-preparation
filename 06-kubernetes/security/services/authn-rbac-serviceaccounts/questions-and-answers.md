# Kubernetes authentication, RBAC and ServiceAccounts — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JN-01

- [ ] **Question:** What is Authentication, and why does it matter in Kubernetes authentication, RBAC and ServiceAccounts?

**Answer:** client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JN-02

- [ ] **Question:** What is Authorization, and why does it matter in Kubernetes authentication, RBAC and ServiceAccounts?

**Answer:** RBAC/webhook/node/ABAC modes decide a request after authentication. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JN-03

- [ ] **Question:** What is Role/ClusterRole, and why does it matter in Kubernetes authentication, RBAC and ServiceAccounts?

**Answer:** namespaced/cluster rule collections over API group/resource/subresource/verb. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JN-04

- [ ] **Question:** What is RoleBinding, and why does it matter in Kubernetes authentication, RBAC and ServiceAccounts?

**Answer:** grants a Role or ClusterRole within one namespace. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JN-05

- [ ] **Question:** What is ClusterRoleBinding, and why does it matter in Kubernetes authentication, RBAC and ServiceAccounts?

**Answer:** grants cluster-wide and is a high-blast-radius object. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JN-06

- [ ] **Question:** What is ServiceAccount, and why does it matter in Kubernetes authentication, RBAC and ServiceAccounts?

**Answer:** namespaced workload identity with projected bound token support. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JN-07

- [ ] **Question:** What is TokenRequest, and why does it matter in Kubernetes authentication, RBAC and ServiceAccounts?

**Answer:** short-lived audience/expiry-bound token avoids legacy static secret tokens. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JN-08

- [ ] **Code:** **Question:** What does `kubectl create token SA -n NS --duration=10m` help you verify for Kubernetes authentication, RBAC and ServiceAccounts?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: powerful diagnostic/delegation verb that must be narrowly controlled/audited.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JN-09

- [ ] **Code:** **Question:** What does `kubectl auth whoami` help you verify for Kubernetes authentication, RBAC and ServiceAccounts?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: permissions can create bindings/roles beyond a caller's current rights.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JN-10

- [ ] **Code:** **Question:** What does `kubectl auth can-i --list -n NS` help you verify for Kubernetes authentication, RBAC and ServiceAccounts?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: create Pod can expose mounted secrets, service account, host/device or node credentials.

## Junior — procedural and command questions

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JP-01

- [ ] **Code:** **Question:** A basic Authentication check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth whoami` and capture exact status/reason/request ID. client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JP-02

- [ ] **Question:** A basic Authorization check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth can-i --list -n NS` and capture exact status/reason/request ID. RBAC/webhook/node/ABAC modes decide a request after authentication. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JP-03

- [ ] **Question:** A basic Role/ClusterRole check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth can-i VERB RESOURCE --as=USER --as-group=GROUP -n NS` and capture exact status/reason/request ID. namespaced/cluster rule collections over API group/resource/subresource/verb. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JP-04

- [ ] **Code:** **Question:** A basic RoleBinding check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl create token SA -n NS --duration=10m` and capture exact status/reason/request ID. grants a Role or ClusterRole within one namespace. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JP-05

- [ ] **Question:** A basic ClusterRoleBinding check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth whoami` and capture exact status/reason/request ID. grants cluster-wide and is a high-blast-radius object. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JP-06

- [ ] **Question:** A basic ServiceAccount check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth can-i --list -n NS` and capture exact status/reason/request ID. namespaced workload identity with projected bound token support. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JP-07

- [ ] **Code:** **Question:** A basic TokenRequest check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth can-i VERB RESOURCE --as=USER --as-group=GROUP -n NS` and capture exact status/reason/request ID. short-lived audience/expiry-bound token avoids legacy static secret tokens. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JP-08

- [ ] **Question:** A basic Impersonation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl create token SA -n NS --duration=10m` and capture exact status/reason/request ID. powerful diagnostic/delegation verb that must be narrowly controlled/audited. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JP-09

- [ ] **Question:** A basic bind/escalate check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth whoami` and capture exact status/reason/request ID. permissions can create bindings/roles beyond a caller's current rights. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-JP-10

- [ ] **Code:** **Question:** A basic Workload escalation check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth can-i --list -n NS` and capture exact status/reason/request ID. create Pod can expose mounted secrets, service account, host/device or node credentials. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MN-01

- [ ] **Question:** Compare Authentication with Authorization. When would each change your design?

**Answer:** Authentication: client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Authorization: RBAC/webhook/node/ABAC modes decide a request after authentication. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MN-02

- [ ] **Question:** Compare Authorization with Role/ClusterRole. When would each change your design?

**Answer:** Authorization: RBAC/webhook/node/ABAC modes decide a request after authentication. Role/ClusterRole: namespaced/cluster rule collections over API group/resource/subresource/verb. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MN-03

- [ ] **Question:** Compare Role/ClusterRole with RoleBinding. When would each change your design?

**Answer:** Role/ClusterRole: namespaced/cluster rule collections over API group/resource/subresource/verb. RoleBinding: grants a Role or ClusterRole within one namespace. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MN-04

- [ ] **Configuration review:** **Question:** Compare RoleBinding with ClusterRoleBinding. When would each change your design?

**Answer:** RoleBinding: grants a Role or ClusterRole within one namespace. ClusterRoleBinding: grants cluster-wide and is a high-blast-radius object. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MN-05

- [ ] **Question:** Compare ClusterRoleBinding with ServiceAccount. When would each change your design?

**Answer:** ClusterRoleBinding: grants cluster-wide and is a high-blast-radius object. ServiceAccount: namespaced workload identity with projected bound token support. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MN-06

- [ ] **Question:** Compare ServiceAccount with TokenRequest. When would each change your design?

**Answer:** ServiceAccount: namespaced workload identity with projected bound token support. TokenRequest: short-lived audience/expiry-bound token avoids legacy static secret tokens. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MN-07

- [ ] **Configuration review:** **Question:** Compare TokenRequest with Impersonation. When would each change your design?

**Answer:** TokenRequest: short-lived audience/expiry-bound token avoids legacy static secret tokens. Impersonation: powerful diagnostic/delegation verb that must be narrowly controlled/audited. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MN-08

- [ ] **Question:** Compare Impersonation with bind/escalate. When would each change your design?

**Answer:** Impersonation: powerful diagnostic/delegation verb that must be narrowly controlled/audited. bind/escalate: permissions can create bindings/roles beyond a caller's current rights. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MN-09

- [ ] **Question:** Compare bind/escalate with Workload escalation. When would each change your design?

**Answer:** bind/escalate: permissions can create bindings/roles beyond a caller's current rights. Workload escalation: create Pod can expose mounted secrets, service account, host/device or node credentials. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MN-10

- [ ] **Configuration review:** **Question:** Compare Workload escalation with Authentication. When would each change your design?

**Answer:** Workload escalation: create Pod can expose mounted secrets, service account, host/device or node credentials. Authentication: client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Authentication; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth whoami` plus recent events/changes, then correlate the service-specific SLI. client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MP-02

- [ ] **Question:** Production is degraded around Authorization; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth can-i --list -n NS` plus recent events/changes, then correlate the service-specific SLI. RBAC/webhook/node/ABAC modes decide a request after authentication. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Role/ClusterRole; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth can-i VERB RESOURCE --as=USER --as-group=GROUP -n NS` plus recent events/changes, then correlate the service-specific SLI. namespaced/cluster rule collections over API group/resource/subresource/verb. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MP-04

- [ ] **Question:** Production is degraded around RoleBinding; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl create token SA -n NS --duration=10m` plus recent events/changes, then correlate the service-specific SLI. grants a Role or ClusterRole within one namespace. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around ClusterRoleBinding; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth whoami` plus recent events/changes, then correlate the service-specific SLI. grants cluster-wide and is a high-blast-radius object. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MP-06

- [ ] **Question:** Production is degraded around ServiceAccount; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth can-i --list -n NS` plus recent events/changes, then correlate the service-specific SLI. namespaced workload identity with projected bound token support. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around TokenRequest; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth can-i VERB RESOURCE --as=USER --as-group=GROUP -n NS` plus recent events/changes, then correlate the service-specific SLI. short-lived audience/expiry-bound token avoids legacy static secret tokens. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MP-08

- [ ] **Question:** Production is degraded around Impersonation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl create token SA -n NS --duration=10m` plus recent events/changes, then correlate the service-specific SLI. powerful diagnostic/delegation verb that must be narrowly controlled/audited. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around bind/escalate; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth whoami` plus recent events/changes, then correlate the service-specific SLI. permissions can create bindings/roles beyond a caller's current rights. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-MP-10

- [ ] **Question:** Production is degraded around Workload escalation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth can-i --list -n NS` plus recent events/changes, then correlate the service-specific SLI. create Pod can expose mounted secrets, service account, host/device or node credentials. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SN-01

- [ ] **Question:** Design a production Kubernetes authentication, RBAC and ServiceAccounts capability where Authentication, RoleBinding and TokenRequest are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. grants a Role or ClusterRole within one namespace. short-lived audience/expiry-bound token avoids legacy static secret tokens. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes authentication, RBAC and ServiceAccounts capability where Authorization, ClusterRoleBinding and Impersonation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: RBAC/webhook/node/ABAC modes decide a request after authentication. grants cluster-wide and is a high-blast-radius object. powerful diagnostic/delegation verb that must be narrowly controlled/audited. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SN-03

- [ ] **Question:** Design a production Kubernetes authentication, RBAC and ServiceAccounts capability where Role/ClusterRole, ServiceAccount and bind/escalate are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: namespaced/cluster rule collections over API group/resource/subresource/verb. namespaced workload identity with projected bound token support. permissions can create bindings/roles beyond a caller's current rights. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes authentication, RBAC and ServiceAccounts capability where RoleBinding, TokenRequest and Workload escalation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: grants a Role or ClusterRole within one namespace. short-lived audience/expiry-bound token avoids legacy static secret tokens. create Pod can expose mounted secrets, service account, host/device or node credentials. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SN-05

- [ ] **Question:** Design a production Kubernetes authentication, RBAC and ServiceAccounts capability where ClusterRoleBinding, Impersonation and Authentication are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: grants cluster-wide and is a high-blast-radius object. powerful diagnostic/delegation verb that must be narrowly controlled/audited. client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes authentication, RBAC and ServiceAccounts capability where ServiceAccount, bind/escalate and Authorization are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: namespaced workload identity with projected bound token support. permissions can create bindings/roles beyond a caller's current rights. RBAC/webhook/node/ABAC modes decide a request after authentication. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SN-07

- [ ] **Question:** Design a production Kubernetes authentication, RBAC and ServiceAccounts capability where TokenRequest, Workload escalation and Role/ClusterRole are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: short-lived audience/expiry-bound token avoids legacy static secret tokens. create Pod can expose mounted secrets, service account, host/device or node credentials. namespaced/cluster rule collections over API group/resource/subresource/verb. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes authentication, RBAC and ServiceAccounts capability where Impersonation, Authentication and RoleBinding are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: powerful diagnostic/delegation verb that must be narrowly controlled/audited. client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. grants a Role or ClusterRole within one namespace. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SN-09

- [ ] **Question:** Design a production Kubernetes authentication, RBAC and ServiceAccounts capability where bind/escalate, Authorization and ClusterRoleBinding are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: permissions can create bindings/roles beyond a caller's current rights. RBAC/webhook/node/ABAC modes decide a request after authentication. grants cluster-wide and is a high-blast-radius object. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes authentication, RBAC and ServiceAccounts capability where Workload escalation, Role/ClusterRole and ServiceAccount are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: create Pod can expose mounted secrets, service account, host/device or node credentials. namespaced/cluster rule collections over API group/resource/subresource/verb. namespaced workload identity with projected bound token support. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authentication. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth whoami` as one read-only checkpoint, not the whole diagnosis. client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authorization. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth can-i --list -n NS` as one read-only checkpoint, not the whole diagnosis. RBAC/webhook/node/ABAC modes decide a request after authentication. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Role/ClusterRole. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth can-i VERB RESOURCE --as=USER --as-group=GROUP -n NS` as one read-only checkpoint, not the whole diagnosis. namespaced/cluster rule collections over API group/resource/subresource/verb. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RoleBinding. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl create token SA -n NS --duration=10m` as one read-only checkpoint, not the whole diagnosis. grants a Role or ClusterRole within one namespace. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ClusterRoleBinding. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth whoami` as one read-only checkpoint, not the whole diagnosis. grants cluster-wide and is a high-blast-radius object. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ServiceAccount. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth can-i --list -n NS` as one read-only checkpoint, not the whole diagnosis. namespaced workload identity with projected bound token support. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TokenRequest. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth can-i VERB RESOURCE --as=USER --as-group=GROUP -n NS` as one read-only checkpoint, not the whole diagnosis. short-lived audience/expiry-bound token avoids legacy static secret tokens. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Impersonation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl create token SA -n NS --duration=10m` as one read-only checkpoint, not the whole diagnosis. powerful diagnostic/delegation verb that must be narrowly controlled/audited. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving bind/escalate. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth whoami` as one read-only checkpoint, not the whole diagnosis. permissions can create bindings/roles beyond a caller's current rights. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-AUTHENTICATION-RBAC-AND-SERVICEACCOUN-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Workload escalation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth can-i --list -n NS` as one read-only checkpoint, not the whole diagnosis. create Pod can expose mounted secrets, service account, host/device or node credentials. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
