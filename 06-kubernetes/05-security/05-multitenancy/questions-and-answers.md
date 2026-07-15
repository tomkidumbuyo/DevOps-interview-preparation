# Kubernetes multi-tenancy — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KUBERNETES-MULTI-TENANCY-JN-01

- [ ] **Question:** What is Namespace tenancy, and why does it matter in Kubernetes multi-tenancy?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-MULTI-TENANCY-JN-02

- [ ] **Question:** What is Cluster-per-tenant, and why does it matter in Kubernetes multi-tenancy?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** stronger failure/control isolation at fleet cost and operational scale. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-MULTI-TENANCY-JN-03

- [ ] **Question:** What is RBAC boundary, and why does it matter in Kubernetes multi-tenancy?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** tenant admins must not create cluster-wide or privilege-escalating resources. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-MULTI-TENANCY-JN-04

- [ ] **Question:** What is Network isolation, and why does it matter in Kubernetes multi-tenancy?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** default deny plus controlled ingress/egress/DNS prevents lateral paths. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-MULTI-TENANCY-JN-05

- [ ] **Question:** What is ResourceQuota, and why does it matter in Kubernetes multi-tenancy?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** aggregate namespace object/compute limits constrain consumption/admission. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-MULTI-TENANCY-JN-06

- [ ] **Question:** What is LimitRange, and why does it matter in Kubernetes multi-tenancy?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** default/min/max per-object requests/limits and can affect scheduling unexpectedly. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-MULTI-TENANCY-JN-07

- [ ] **Question:** What is Node isolation, and why does it matter in Kubernetes multi-tenancy?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** taints/dedicated pools/runtime classes protect stronger/noisy workloads. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-MULTI-TENANCY-JN-08

- [ ] **Code:** **Question:** What does `kubectl get pods -n TENANT_NS -o wide` help you verify for Kubernetes multi-tenancy?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: separate workload identity, storage, KMS and backup/restore paths.

### KUBERNETES-MULTI-TENANCY-JN-09

- [ ] **Code:** **Question:** What does `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` help you verify for Kubernetes multi-tenancy?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: tenant identifiers/access/redaction/quotas prevent cross-tenant leak and cardinality abuse.

### KUBERNETES-MULTI-TENANCY-JN-10

- [ ] **Code:** **Question:** What does `kubectl auth can-i --list --as=TENANT -n TENANT_NS` help you verify for Kubernetes multi-tenancy?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: platform owns guardrails; tenant owns namespaced workloads within transparent exceptions.

## Junior — procedural and command questions

### KUBERNETES-MULTI-TENANCY-JP-01

- [ ] **Code:** **Question:** A basic Namespace tenancy check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` and capture exact status/reason/request ID. soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-MULTI-TENANCY-JP-02

- [ ] **Question:** A basic Cluster-per-tenant check fails. What would you do first?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth can-i --list --as=TENANT -n TENANT_NS` and capture exact status/reason/request ID. stronger failure/control isolation at fleet cost and operational scale. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-MULTI-TENANCY-JP-03

- [ ] **Question:** A basic RBAC boundary check fails. What would you do first?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -n TENANT_NS` and capture exact status/reason/request ID. tenant admins must not create cluster-wide or privilege-escalating resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-MULTI-TENANCY-JP-04

- [ ] **Code:** **Question:** A basic Network isolation check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -n TENANT_NS -o wide` and capture exact status/reason/request ID. default deny plus controlled ingress/egress/DNS prevents lateral paths. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-MULTI-TENANCY-JP-05

- [ ] **Question:** A basic ResourceQuota check fails. What would you do first?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` and capture exact status/reason/request ID. aggregate namespace object/compute limits constrain consumption/admission. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-MULTI-TENANCY-JP-06

- [ ] **Question:** A basic LimitRange check fails. What would you do first?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth can-i --list --as=TENANT -n TENANT_NS` and capture exact status/reason/request ID. default/min/max per-object requests/limits and can affect scheduling unexpectedly. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-MULTI-TENANCY-JP-07

- [ ] **Code:** **Question:** A basic Node isolation check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -n TENANT_NS` and capture exact status/reason/request ID. taints/dedicated pools/runtime classes protect stronger/noisy workloads. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-MULTI-TENANCY-JP-08

- [ ] **Question:** A basic Secret/data isolation check fails. What would you do first?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -n TENANT_NS -o wide` and capture exact status/reason/request ID. separate workload identity, storage, KMS and backup/restore paths. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-MULTI-TENANCY-JP-09

- [ ] **Question:** A basic Telemetry isolation check fails. What would you do first?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` and capture exact status/reason/request ID. tenant identifiers/access/redaction/quotas prevent cross-tenant leak and cardinality abuse. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-MULTI-TENANCY-JP-10

- [ ] **Code:** **Question:** A basic Policy delegation check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes multi-tenancy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl auth can-i --list --as=TENANT -n TENANT_NS` and capture exact status/reason/request ID. platform owns guardrails; tenant owns namespaced workloads within transparent exceptions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KUBERNETES-MULTI-TENANCY-MN-01

- [ ] **Question:** Compare Namespace tenancy with Cluster-per-tenant. When would each change your design?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Namespace tenancy: soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Cluster-per-tenant: stronger failure/control isolation at fleet cost and operational scale. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-MULTI-TENANCY-MN-02

- [ ] **Question:** Compare Cluster-per-tenant with RBAC boundary. When would each change your design?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Cluster-per-tenant: stronger failure/control isolation at fleet cost and operational scale. RBAC boundary: tenant admins must not create cluster-wide or privilege-escalating resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-MULTI-TENANCY-MN-03

- [ ] **Question:** Compare RBAC boundary with Network isolation. When would each change your design?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** RBAC boundary: tenant admins must not create cluster-wide or privilege-escalating resources. Network isolation: default deny plus controlled ingress/egress/DNS prevents lateral paths. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-MULTI-TENANCY-MN-04

- [ ] **Configuration review:** **Question:** Compare Network isolation with ResourceQuota. When would each change your design?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Network isolation: default deny plus controlled ingress/egress/DNS prevents lateral paths. ResourceQuota: aggregate namespace object/compute limits constrain consumption/admission. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-MULTI-TENANCY-MN-05

- [ ] **Question:** Compare ResourceQuota with LimitRange. When would each change your design?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ResourceQuota: aggregate namespace object/compute limits constrain consumption/admission. LimitRange: default/min/max per-object requests/limits and can affect scheduling unexpectedly. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-MULTI-TENANCY-MN-06

- [ ] **Question:** Compare LimitRange with Node isolation. When would each change your design?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** LimitRange: default/min/max per-object requests/limits and can affect scheduling unexpectedly. Node isolation: taints/dedicated pools/runtime classes protect stronger/noisy workloads. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-MULTI-TENANCY-MN-07

- [ ] **Configuration review:** **Question:** Compare Node isolation with Secret/data isolation. When would each change your design?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Node isolation: taints/dedicated pools/runtime classes protect stronger/noisy workloads. Secret/data isolation: separate workload identity, storage, KMS and backup/restore paths. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-MULTI-TENANCY-MN-08

- [ ] **Question:** Compare Secret/data isolation with Telemetry isolation. When would each change your design?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Secret/data isolation: separate workload identity, storage, KMS and backup/restore paths. Telemetry isolation: tenant identifiers/access/redaction/quotas prevent cross-tenant leak and cardinality abuse. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-MULTI-TENANCY-MN-09

- [ ] **Question:** Compare Telemetry isolation with Policy delegation. When would each change your design?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Telemetry isolation: tenant identifiers/access/redaction/quotas prevent cross-tenant leak and cardinality abuse. Policy delegation: platform owns guardrails; tenant owns namespaced workloads within transparent exceptions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-MULTI-TENANCY-MN-10

- [ ] **Configuration review:** **Question:** Compare Policy delegation with Namespace tenancy. When would each change your design?
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Policy delegation: platform owns guardrails; tenant owns namespaced workloads within transparent exceptions. Namespace tenancy: soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KUBERNETES-MULTI-TENANCY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Namespace tenancy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` plus recent events/changes, then correlate the service-specific SLI. soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-MULTI-TENANCY-MP-02

- [ ] **Question:** Production is degraded around Cluster-per-tenant; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth can-i --list --as=TENANT -n TENANT_NS` plus recent events/changes, then correlate the service-specific SLI. stronger failure/control isolation at fleet cost and operational scale. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-MULTI-TENANCY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around RBAC boundary; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -n TENANT_NS` plus recent events/changes, then correlate the service-specific SLI. tenant admins must not create cluster-wide or privilege-escalating resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-MULTI-TENANCY-MP-04

- [ ] **Question:** Production is degraded around Network isolation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -n TENANT_NS -o wide` plus recent events/changes, then correlate the service-specific SLI. default deny plus controlled ingress/egress/DNS prevents lateral paths. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-MULTI-TENANCY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around ResourceQuota; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` plus recent events/changes, then correlate the service-specific SLI. aggregate namespace object/compute limits constrain consumption/admission. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-MULTI-TENANCY-MP-06

- [ ] **Question:** Production is degraded around LimitRange; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth can-i --list --as=TENANT -n TENANT_NS` plus recent events/changes, then correlate the service-specific SLI. default/min/max per-object requests/limits and can affect scheduling unexpectedly. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-MULTI-TENANCY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Node isolation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -n TENANT_NS` plus recent events/changes, then correlate the service-specific SLI. taints/dedicated pools/runtime classes protect stronger/noisy workloads. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-MULTI-TENANCY-MP-08

- [ ] **Question:** Production is degraded around Secret/data isolation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -n TENANT_NS -o wide` plus recent events/changes, then correlate the service-specific SLI. separate workload identity, storage, KMS and backup/restore paths. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-MULTI-TENANCY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Telemetry isolation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` plus recent events/changes, then correlate the service-specific SLI. tenant identifiers/access/redaction/quotas prevent cross-tenant leak and cardinality abuse. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-MULTI-TENANCY-MP-10

- [ ] **Question:** Production is degraded around Policy delegation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl auth can-i --list --as=TENANT -n TENANT_NS` plus recent events/changes, then correlate the service-specific SLI. platform owns guardrails; tenant owns namespaced workloads within transparent exceptions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KUBERNETES-MULTI-TENANCY-SN-01

- [ ] **Question:** Design a production Kubernetes multi-tenancy capability where Namespace tenancy, Network isolation and Node isolation are first-class requirements.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. default deny plus controlled ingress/egress/DNS prevents lateral paths. taints/dedicated pools/runtime classes protect stronger/noisy workloads. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-MULTI-TENANCY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes multi-tenancy capability where Cluster-per-tenant, ResourceQuota and Secret/data isolation are first-class requirements.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stronger failure/control isolation at fleet cost and operational scale. aggregate namespace object/compute limits constrain consumption/admission. separate workload identity, storage, KMS and backup/restore paths. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-MULTI-TENANCY-SN-03

- [ ] **Question:** Design a production Kubernetes multi-tenancy capability where RBAC boundary, LimitRange and Telemetry isolation are first-class requirements.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tenant admins must not create cluster-wide or privilege-escalating resources. default/min/max per-object requests/limits and can affect scheduling unexpectedly. tenant identifiers/access/redaction/quotas prevent cross-tenant leak and cardinality abuse. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-MULTI-TENANCY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes multi-tenancy capability where Network isolation, Node isolation and Policy delegation are first-class requirements.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: default deny plus controlled ingress/egress/DNS prevents lateral paths. taints/dedicated pools/runtime classes protect stronger/noisy workloads. platform owns guardrails; tenant owns namespaced workloads within transparent exceptions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-MULTI-TENANCY-SN-05

- [ ] **Question:** Design a production Kubernetes multi-tenancy capability where ResourceQuota, Secret/data isolation and Namespace tenancy are first-class requirements.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: aggregate namespace object/compute limits constrain consumption/admission. separate workload identity, storage, KMS and backup/restore paths. soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-MULTI-TENANCY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes multi-tenancy capability where LimitRange, Telemetry isolation and Cluster-per-tenant are first-class requirements.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: default/min/max per-object requests/limits and can affect scheduling unexpectedly. tenant identifiers/access/redaction/quotas prevent cross-tenant leak and cardinality abuse. stronger failure/control isolation at fleet cost and operational scale. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-MULTI-TENANCY-SN-07

- [ ] **Question:** Design a production Kubernetes multi-tenancy capability where Node isolation, Policy delegation and RBAC boundary are first-class requirements.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: taints/dedicated pools/runtime classes protect stronger/noisy workloads. platform owns guardrails; tenant owns namespaced workloads within transparent exceptions. tenant admins must not create cluster-wide or privilege-escalating resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-MULTI-TENANCY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes multi-tenancy capability where Secret/data isolation, Namespace tenancy and Network isolation are first-class requirements.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: separate workload identity, storage, KMS and backup/restore paths. soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. default deny plus controlled ingress/egress/DNS prevents lateral paths. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-MULTI-TENANCY-SN-09

- [ ] **Question:** Design a production Kubernetes multi-tenancy capability where Telemetry isolation, Cluster-per-tenant and ResourceQuota are first-class requirements.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tenant identifiers/access/redaction/quotas prevent cross-tenant leak and cardinality abuse. stronger failure/control isolation at fleet cost and operational scale. aggregate namespace object/compute limits constrain consumption/admission. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-MULTI-TENANCY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes multi-tenancy capability where Policy delegation, RBAC boundary and LimitRange are first-class requirements.
> **Covered in:** [Kubernetes multi-tenancy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: platform owns guardrails; tenant owns namespaced workloads within transparent exceptions. tenant admins must not create cluster-wide or privilege-escalating resources. default/min/max per-object requests/limits and can affect scheduling unexpectedly. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KUBERNETES-MULTI-TENANCY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Namespace tenancy. How do you lead it end to end?
> **Covered in:** [Kubernetes multi-tenancy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` as one read-only checkpoint, not the whole diagnosis. soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-MULTI-TENANCY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cluster-per-tenant. How do you lead it end to end?
> **Covered in:** [Kubernetes multi-tenancy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth can-i --list --as=TENANT -n TENANT_NS` as one read-only checkpoint, not the whole diagnosis. stronger failure/control isolation at fleet cost and operational scale. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-MULTI-TENANCY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RBAC boundary. How do you lead it end to end?
> **Covered in:** [Kubernetes multi-tenancy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -n TENANT_NS` as one read-only checkpoint, not the whole diagnosis. tenant admins must not create cluster-wide or privilege-escalating resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-MULTI-TENANCY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Network isolation. How do you lead it end to end?
> **Covered in:** [Kubernetes multi-tenancy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -n TENANT_NS -o wide` as one read-only checkpoint, not the whole diagnosis. default deny plus controlled ingress/egress/DNS prevents lateral paths. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-MULTI-TENANCY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ResourceQuota. How do you lead it end to end?
> **Covered in:** [Kubernetes multi-tenancy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` as one read-only checkpoint, not the whole diagnosis. aggregate namespace object/compute limits constrain consumption/admission. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-MULTI-TENANCY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving LimitRange. How do you lead it end to end?
> **Covered in:** [Kubernetes multi-tenancy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth can-i --list --as=TENANT -n TENANT_NS` as one read-only checkpoint, not the whole diagnosis. default/min/max per-object requests/limits and can affect scheduling unexpectedly. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-MULTI-TENANCY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node isolation. How do you lead it end to end?
> **Covered in:** [Kubernetes multi-tenancy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -n TENANT_NS` as one read-only checkpoint, not the whole diagnosis. taints/dedicated pools/runtime classes protect stronger/noisy workloads. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-MULTI-TENANCY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secret/data isolation. How do you lead it end to end?
> **Covered in:** [Kubernetes multi-tenancy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -n TENANT_NS -o wide` as one read-only checkpoint, not the whole diagnosis. separate workload identity, storage, KMS and backup/restore paths. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-MULTI-TENANCY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Telemetry isolation. How do you lead it end to end?
> **Covered in:** [Kubernetes multi-tenancy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A` as one read-only checkpoint, not the whole diagnosis. tenant identifiers/access/redaction/quotas prevent cross-tenant leak and cardinality abuse. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-MULTI-TENANCY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Policy delegation. How do you lead it end to end?
> **Covered in:** [Kubernetes multi-tenancy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl auth can-i --list --as=TENANT -n TENANT_NS` as one read-only checkpoint, not the whole diagnosis. platform owns guardrails; tenant owns namespaced workloads within transparent exceptions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Kubernetes admission policies and webhooks](../04-admission-policies-webhooks/README.md) · [Study note](README.md) · [Next: Scheduling Autoscaling →](../../06-scheduling-autoscaling/README.md)

<!-- reading-navigation:end -->
