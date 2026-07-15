# Kubernetes admission policies and webhooks — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JN-01

- [ ] **Question:** What is Admission sequence, and why does it matter in Kubernetes admission policies and webhooks?

**Answer:** mutation precedes object schema/defaulting stages and validation before persistence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JN-02

- [ ] **Question:** What is ValidatingAdmissionPolicy, and why does it matter in Kubernetes admission policies and webhooks?

**Answer:** CEL policy in API server avoids external webhook network dependency. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JN-03

- [ ] **Question:** What is Policy binding, and why does it matter in Kubernetes admission policies and webhooks?

**Answer:** selects parameters, namespaces/resources and validation actions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JN-04

- [ ] **Question:** What is Mutating webhook, and why does it matter in Kubernetes admission policies and webhooks?

**Answer:** patches objects and must be idempotent/reinvocation aware. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JN-05

- [ ] **Question:** What is Validating webhook, and why does it matter in Kubernetes admission policies and webhooks?

**Answer:** accepts/rejects after mutations and sees admission review context. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JN-06

- [ ] **Question:** What is failurePolicy, and why does it matter in Kubernetes admission policies and webhooks?

**Answer:** Fail protects policy but can block all writes; Ignore preserves availability with bypass risk. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JN-07

- [ ] **Question:** What is Timeout/match conditions, and why does it matter in Kubernetes admission policies and webhooks?

**Answer:** bound webhook latency and exclude irrelevant/system/recovery paths deliberately. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JN-08

- [ ] **Code:** **Question:** What does `kubectl get --raw /metrics | rg admission` help you verify for Kubernetes admission policies and webhooks?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: webhook declaration must truthfully support dry-run safety.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` help you verify for Kubernetes admission policies and webhooks?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: API server must reach trusted webhook endpoint with automated rotation.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JN-10

- [ ] **Code:** **Question:** What does `kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration` help you verify for Kubernetes admission policies and webhooks?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: admission latency/rejection/error/timeout plus policy version explains API failures.

## Junior — procedural and command questions

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JP-01

- [ ] **Code:** **Question:** A basic Admission sequence check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` and capture exact status/reason/request ID. mutation precedes object schema/defaulting stages and validation before persistence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JP-02

- [ ] **Question:** A basic ValidatingAdmissionPolicy check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration` and capture exact status/reason/request ID. CEL policy in API server avoids external webhook network dependency. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JP-03

- [ ] **Question:** A basic Policy binding check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl apply --dry-run=server -f object.yaml` and capture exact status/reason/request ID. selects parameters, namespaces/resources and validation actions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JP-04

- [ ] **Code:** **Question:** A basic Mutating webhook check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /metrics | rg admission` and capture exact status/reason/request ID. patches objects and must be idempotent/reinvocation aware. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JP-05

- [ ] **Question:** A basic Validating webhook check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` and capture exact status/reason/request ID. accepts/rejects after mutations and sees admission review context. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JP-06

- [ ] **Question:** A basic failurePolicy check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration` and capture exact status/reason/request ID. Fail protects policy but can block all writes; Ignore preserves availability with bypass risk. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JP-07

- [ ] **Code:** **Question:** A basic Timeout/match conditions check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl apply --dry-run=server -f object.yaml` and capture exact status/reason/request ID. bound webhook latency and exclude irrelevant/system/recovery paths deliberately. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JP-08

- [ ] **Question:** A basic SideEffects/dry-run check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /metrics | rg admission` and capture exact status/reason/request ID. webhook declaration must truthfully support dry-run safety. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JP-09

- [ ] **Question:** A basic Certificate/service check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` and capture exact status/reason/request ID. API server must reach trusted webhook endpoint with automated rotation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-JP-10

- [ ] **Code:** **Question:** A basic Observability check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration` and capture exact status/reason/request ID. admission latency/rejection/error/timeout plus policy version explains API failures. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MN-01

- [ ] **Question:** Compare Admission sequence with ValidatingAdmissionPolicy. When would each change your design?

**Answer:** Admission sequence: mutation precedes object schema/defaulting stages and validation before persistence. ValidatingAdmissionPolicy: CEL policy in API server avoids external webhook network dependency. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MN-02

- [ ] **Question:** Compare ValidatingAdmissionPolicy with Policy binding. When would each change your design?

**Answer:** ValidatingAdmissionPolicy: CEL policy in API server avoids external webhook network dependency. Policy binding: selects parameters, namespaces/resources and validation actions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MN-03

- [ ] **Question:** Compare Policy binding with Mutating webhook. When would each change your design?

**Answer:** Policy binding: selects parameters, namespaces/resources and validation actions. Mutating webhook: patches objects and must be idempotent/reinvocation aware. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MN-04

- [ ] **Configuration review:** **Question:** Compare Mutating webhook with Validating webhook. When would each change your design?

**Answer:** Mutating webhook: patches objects and must be idempotent/reinvocation aware. Validating webhook: accepts/rejects after mutations and sees admission review context. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MN-05

- [ ] **Question:** Compare Validating webhook with failurePolicy. When would each change your design?

**Answer:** Validating webhook: accepts/rejects after mutations and sees admission review context. failurePolicy: Fail protects policy but can block all writes; Ignore preserves availability with bypass risk. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MN-06

- [ ] **Question:** Compare failurePolicy with Timeout/match conditions. When would each change your design?

**Answer:** failurePolicy: Fail protects policy but can block all writes; Ignore preserves availability with bypass risk. Timeout/match conditions: bound webhook latency and exclude irrelevant/system/recovery paths deliberately. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MN-07

- [ ] **Configuration review:** **Question:** Compare Timeout/match conditions with SideEffects/dry-run. When would each change your design?

**Answer:** Timeout/match conditions: bound webhook latency and exclude irrelevant/system/recovery paths deliberately. SideEffects/dry-run: webhook declaration must truthfully support dry-run safety. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MN-08

- [ ] **Question:** Compare SideEffects/dry-run with Certificate/service. When would each change your design?

**Answer:** SideEffects/dry-run: webhook declaration must truthfully support dry-run safety. Certificate/service: API server must reach trusted webhook endpoint with automated rotation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MN-09

- [ ] **Question:** Compare Certificate/service with Observability. When would each change your design?

**Answer:** Certificate/service: API server must reach trusted webhook endpoint with automated rotation. Observability: admission latency/rejection/error/timeout plus policy version explains API failures. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MN-10

- [ ] **Configuration review:** **Question:** Compare Observability with Admission sequence. When would each change your design?

**Answer:** Observability: admission latency/rejection/error/timeout plus policy version explains API failures. Admission sequence: mutation precedes object schema/defaulting stages and validation before persistence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Admission sequence; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` plus recent events/changes, then correlate the service-specific SLI. mutation precedes object schema/defaulting stages and validation before persistence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MP-02

- [ ] **Question:** Production is degraded around ValidatingAdmissionPolicy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration` plus recent events/changes, then correlate the service-specific SLI. CEL policy in API server avoids external webhook network dependency. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Policy binding; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl apply --dry-run=server -f object.yaml` plus recent events/changes, then correlate the service-specific SLI. selects parameters, namespaces/resources and validation actions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MP-04

- [ ] **Question:** Production is degraded around Mutating webhook; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /metrics | rg admission` plus recent events/changes, then correlate the service-specific SLI. patches objects and must be idempotent/reinvocation aware. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Validating webhook; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` plus recent events/changes, then correlate the service-specific SLI. accepts/rejects after mutations and sees admission review context. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MP-06

- [ ] **Question:** Production is degraded around failurePolicy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration` plus recent events/changes, then correlate the service-specific SLI. Fail protects policy but can block all writes; Ignore preserves availability with bypass risk. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Timeout/match conditions; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl apply --dry-run=server -f object.yaml` plus recent events/changes, then correlate the service-specific SLI. bound webhook latency and exclude irrelevant/system/recovery paths deliberately. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MP-08

- [ ] **Question:** Production is degraded around SideEffects/dry-run; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /metrics | rg admission` plus recent events/changes, then correlate the service-specific SLI. webhook declaration must truthfully support dry-run safety. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Certificate/service; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` plus recent events/changes, then correlate the service-specific SLI. API server must reach trusted webhook endpoint with automated rotation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-MP-10

- [ ] **Question:** Production is degraded around Observability; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration` plus recent events/changes, then correlate the service-specific SLI. admission latency/rejection/error/timeout plus policy version explains API failures. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SN-01

- [ ] **Question:** Design a production Kubernetes admission policies and webhooks capability where Admission sequence, Mutating webhook and Timeout/match conditions are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: mutation precedes object schema/defaulting stages and validation before persistence. patches objects and must be idempotent/reinvocation aware. bound webhook latency and exclude irrelevant/system/recovery paths deliberately. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes admission policies and webhooks capability where ValidatingAdmissionPolicy, Validating webhook and SideEffects/dry-run are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: CEL policy in API server avoids external webhook network dependency. accepts/rejects after mutations and sees admission review context. webhook declaration must truthfully support dry-run safety. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SN-03

- [ ] **Question:** Design a production Kubernetes admission policies and webhooks capability where Policy binding, failurePolicy and Certificate/service are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: selects parameters, namespaces/resources and validation actions. Fail protects policy but can block all writes; Ignore preserves availability with bypass risk. API server must reach trusted webhook endpoint with automated rotation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes admission policies and webhooks capability where Mutating webhook, Timeout/match conditions and Observability are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: patches objects and must be idempotent/reinvocation aware. bound webhook latency and exclude irrelevant/system/recovery paths deliberately. admission latency/rejection/error/timeout plus policy version explains API failures. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SN-05

- [ ] **Question:** Design a production Kubernetes admission policies and webhooks capability where Validating webhook, SideEffects/dry-run and Admission sequence are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: accepts/rejects after mutations and sees admission review context. webhook declaration must truthfully support dry-run safety. mutation precedes object schema/defaulting stages and validation before persistence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes admission policies and webhooks capability where failurePolicy, Certificate/service and ValidatingAdmissionPolicy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Fail protects policy but can block all writes; Ignore preserves availability with bypass risk. API server must reach trusted webhook endpoint with automated rotation. CEL policy in API server avoids external webhook network dependency. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SN-07

- [ ] **Question:** Design a production Kubernetes admission policies and webhooks capability where Timeout/match conditions, Observability and Policy binding are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bound webhook latency and exclude irrelevant/system/recovery paths deliberately. admission latency/rejection/error/timeout plus policy version explains API failures. selects parameters, namespaces/resources and validation actions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes admission policies and webhooks capability where SideEffects/dry-run, Admission sequence and Mutating webhook are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: webhook declaration must truthfully support dry-run safety. mutation precedes object schema/defaulting stages and validation before persistence. patches objects and must be idempotent/reinvocation aware. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SN-09

- [ ] **Question:** Design a production Kubernetes admission policies and webhooks capability where Certificate/service, ValidatingAdmissionPolicy and Validating webhook are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: API server must reach trusted webhook endpoint with automated rotation. CEL policy in API server avoids external webhook network dependency. accepts/rejects after mutations and sees admission review context. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes admission policies and webhooks capability where Observability, Policy binding and failurePolicy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: admission latency/rejection/error/timeout plus policy version explains API failures. selects parameters, namespaces/resources and validation actions. Fail protects policy but can block all writes; Ignore preserves availability with bypass risk. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Admission sequence. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` as one read-only checkpoint, not the whole diagnosis. mutation precedes object schema/defaulting stages and validation before persistence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ValidatingAdmissionPolicy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration` as one read-only checkpoint, not the whole diagnosis. CEL policy in API server avoids external webhook network dependency. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Policy binding. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl apply --dry-run=server -f object.yaml` as one read-only checkpoint, not the whole diagnosis. selects parameters, namespaces/resources and validation actions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Mutating webhook. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /metrics | rg admission` as one read-only checkpoint, not the whole diagnosis. patches objects and must be idempotent/reinvocation aware. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Validating webhook. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` as one read-only checkpoint, not the whole diagnosis. accepts/rejects after mutations and sees admission review context. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving failurePolicy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration` as one read-only checkpoint, not the whole diagnosis. Fail protects policy but can block all writes; Ignore preserves availability with bypass risk. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Timeout/match conditions. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl apply --dry-run=server -f object.yaml` as one read-only checkpoint, not the whole diagnosis. bound webhook latency and exclude irrelevant/system/recovery paths deliberately. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SideEffects/dry-run. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /metrics | rg admission` as one read-only checkpoint, not the whole diagnosis. webhook declaration must truthfully support dry-run safety. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Certificate/service. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding` as one read-only checkpoint, not the whole diagnosis. API server must reach trusted webhook endpoint with automated rotation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-ADMISSION-POLICIES-AND-WEBHOOKS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Observability. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration` as one read-only checkpoint, not the whole diagnosis. admission latency/rejection/error/timeout plus policy version explains API failures. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
