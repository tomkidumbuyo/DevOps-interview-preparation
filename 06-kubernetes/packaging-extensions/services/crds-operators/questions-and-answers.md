# CRDs and operators — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### CRDS-AND-OPERATORS-JN-01

- [ ] **Question:** What is CRD schema, and why does it matter in CRDs and operators?

**Answer:** structural OpenAPI validation/defaulting/pruning define accepted desired state. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CRDS-AND-OPERATORS-JN-02

- [ ] **Question:** What is Reconciler, and why does it matter in CRDs and operators?

**Answer:** level-based idempotent loop converges desired and observed state under retries. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CRDS-AND-OPERATORS-JN-03

- [ ] **Question:** What is Status subresource, and why does it matter in CRDs and operators?

**Answer:** controller reports conditions/observedGeneration without mutating spec. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CRDS-AND-OPERATORS-JN-04

- [ ] **Question:** What is Finalizer, and why does it matter in CRDs and operators?

**Answer:** ensures external cleanup before deletion completes and can stick when controller fails. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CRDS-AND-OPERATORS-JN-05

- [ ] **Question:** What is Owner reference, and why does it matter in CRDs and operators?

**Answer:** drives garbage collection for Kubernetes child resources. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CRDS-AND-OPERATORS-JN-06

- [ ] **Question:** What is Work queue, and why does it matter in CRDs and operators?

**Answer:** event keys, rate limiting and retries coalesce reconciliation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CRDS-AND-OPERATORS-JN-07

- [ ] **Question:** What is Webhook, and why does it matter in CRDs and operators?

**Answer:** default/validate/convert custom resources with HA/certificate/timeout needs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CRDS-AND-OPERATORS-JN-08

- [ ] **Code:** **Question:** What does `kubectl get CRD_KIND NAME -o yaml` help you verify for CRDs and operators?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: served/storage versions and conversion preserve compatibility.

### CRDS-AND-OPERATORS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get events --field-selector=involvedObject.kind=CRD_KIND` help you verify for CRDs and operators?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: only one active replica performs shared mutation while others stand by.

### CRDS-AND-OPERATORS-JN-10

- [ ] **Code:** **Question:** What does `kubectl logs deploy/CONTROLLER --since=30m` help you verify for CRDs and operators?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: controller watches and permissions should be limited to owned resources/tenants.

## Junior — procedural and command questions

### CRDS-AND-OPERATORS-JP-01

- [ ] **Code:** **Question:** A basic CRD schema check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get crd` and capture exact status/reason/request ID. structural OpenAPI validation/defaulting/pruning define accepted desired state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CRDS-AND-OPERATORS-JP-02

- [ ] **Question:** A basic Reconciler check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl explain CRD_KIND.spec --recursive` and capture exact status/reason/request ID. level-based idempotent loop converges desired and observed state under retries. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CRDS-AND-OPERATORS-JP-03

- [ ] **Question:** A basic Status subresource check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get CRD_KIND NAME -o yaml` and capture exact status/reason/request ID. controller reports conditions/observedGeneration without mutating spec. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CRDS-AND-OPERATORS-JP-04

- [ ] **Code:** **Question:** A basic Finalizer check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events --field-selector=involvedObject.kind=CRD_KIND` and capture exact status/reason/request ID. ensures external cleanup before deletion completes and can stick when controller fails. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CRDS-AND-OPERATORS-JP-05

- [ ] **Question:** A basic Owner reference check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs deploy/CONTROLLER --since=30m` and capture exact status/reason/request ID. drives garbage collection for Kubernetes child resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CRDS-AND-OPERATORS-JP-06

- [ ] **Question:** A basic Work queue check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get crd` and capture exact status/reason/request ID. event keys, rate limiting and retries coalesce reconciliation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CRDS-AND-OPERATORS-JP-07

- [ ] **Code:** **Question:** A basic Webhook check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl explain CRD_KIND.spec --recursive` and capture exact status/reason/request ID. default/validate/convert custom resources with HA/certificate/timeout needs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CRDS-AND-OPERATORS-JP-08

- [ ] **Question:** A basic Version conversion check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get CRD_KIND NAME -o yaml` and capture exact status/reason/request ID. served/storage versions and conversion preserve compatibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CRDS-AND-OPERATORS-JP-09

- [ ] **Question:** A basic Controller leader election check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events --field-selector=involvedObject.kind=CRD_KIND` and capture exact status/reason/request ID. only one active replica performs shared mutation while others stand by. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CRDS-AND-OPERATORS-JP-10

- [ ] **Code:** **Question:** A basic RBAC/cache scope check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs deploy/CONTROLLER --since=30m` and capture exact status/reason/request ID. controller watches and permissions should be limited to owned resources/tenants. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### CRDS-AND-OPERATORS-MN-01

- [ ] **Question:** Compare CRD schema with Reconciler. When would each change your design?

**Answer:** CRD schema: structural OpenAPI validation/defaulting/pruning define accepted desired state. Reconciler: level-based idempotent loop converges desired and observed state under retries. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CRDS-AND-OPERATORS-MN-02

- [ ] **Question:** Compare Reconciler with Status subresource. When would each change your design?

**Answer:** Reconciler: level-based idempotent loop converges desired and observed state under retries. Status subresource: controller reports conditions/observedGeneration without mutating spec. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CRDS-AND-OPERATORS-MN-03

- [ ] **Question:** Compare Status subresource with Finalizer. When would each change your design?

**Answer:** Status subresource: controller reports conditions/observedGeneration without mutating spec. Finalizer: ensures external cleanup before deletion completes and can stick when controller fails. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CRDS-AND-OPERATORS-MN-04

- [ ] **Configuration review:** **Question:** Compare Finalizer with Owner reference. When would each change your design?

**Answer:** Finalizer: ensures external cleanup before deletion completes and can stick when controller fails. Owner reference: drives garbage collection for Kubernetes child resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CRDS-AND-OPERATORS-MN-05

- [ ] **Question:** Compare Owner reference with Work queue. When would each change your design?

**Answer:** Owner reference: drives garbage collection for Kubernetes child resources. Work queue: event keys, rate limiting and retries coalesce reconciliation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CRDS-AND-OPERATORS-MN-06

- [ ] **Question:** Compare Work queue with Webhook. When would each change your design?

**Answer:** Work queue: event keys, rate limiting and retries coalesce reconciliation. Webhook: default/validate/convert custom resources with HA/certificate/timeout needs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CRDS-AND-OPERATORS-MN-07

- [ ] **Configuration review:** **Question:** Compare Webhook with Version conversion. When would each change your design?

**Answer:** Webhook: default/validate/convert custom resources with HA/certificate/timeout needs. Version conversion: served/storage versions and conversion preserve compatibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CRDS-AND-OPERATORS-MN-08

- [ ] **Question:** Compare Version conversion with Controller leader election. When would each change your design?

**Answer:** Version conversion: served/storage versions and conversion preserve compatibility. Controller leader election: only one active replica performs shared mutation while others stand by. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CRDS-AND-OPERATORS-MN-09

- [ ] **Question:** Compare Controller leader election with RBAC/cache scope. When would each change your design?

**Answer:** Controller leader election: only one active replica performs shared mutation while others stand by. RBAC/cache scope: controller watches and permissions should be limited to owned resources/tenants. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CRDS-AND-OPERATORS-MN-10

- [ ] **Configuration review:** **Question:** Compare RBAC/cache scope with CRD schema. When would each change your design?

**Answer:** RBAC/cache scope: controller watches and permissions should be limited to owned resources/tenants. CRD schema: structural OpenAPI validation/defaulting/pruning define accepted desired state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### CRDS-AND-OPERATORS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around CRD schema; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get crd` plus recent events/changes, then correlate the service-specific SLI. structural OpenAPI validation/defaulting/pruning define accepted desired state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CRDS-AND-OPERATORS-MP-02

- [ ] **Question:** Production is degraded around Reconciler; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl explain CRD_KIND.spec --recursive` plus recent events/changes, then correlate the service-specific SLI. level-based idempotent loop converges desired and observed state under retries. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CRDS-AND-OPERATORS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Status subresource; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get CRD_KIND NAME -o yaml` plus recent events/changes, then correlate the service-specific SLI. controller reports conditions/observedGeneration without mutating spec. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CRDS-AND-OPERATORS-MP-04

- [ ] **Question:** Production is degraded around Finalizer; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events --field-selector=involvedObject.kind=CRD_KIND` plus recent events/changes, then correlate the service-specific SLI. ensures external cleanup before deletion completes and can stick when controller fails. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CRDS-AND-OPERATORS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Owner reference; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs deploy/CONTROLLER --since=30m` plus recent events/changes, then correlate the service-specific SLI. drives garbage collection for Kubernetes child resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CRDS-AND-OPERATORS-MP-06

- [ ] **Question:** Production is degraded around Work queue; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get crd` plus recent events/changes, then correlate the service-specific SLI. event keys, rate limiting and retries coalesce reconciliation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CRDS-AND-OPERATORS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Webhook; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl explain CRD_KIND.spec --recursive` plus recent events/changes, then correlate the service-specific SLI. default/validate/convert custom resources with HA/certificate/timeout needs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CRDS-AND-OPERATORS-MP-08

- [ ] **Question:** Production is degraded around Version conversion; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get CRD_KIND NAME -o yaml` plus recent events/changes, then correlate the service-specific SLI. served/storage versions and conversion preserve compatibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CRDS-AND-OPERATORS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Controller leader election; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events --field-selector=involvedObject.kind=CRD_KIND` plus recent events/changes, then correlate the service-specific SLI. only one active replica performs shared mutation while others stand by. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CRDS-AND-OPERATORS-MP-10

- [ ] **Question:** Production is degraded around RBAC/cache scope; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs deploy/CONTROLLER --since=30m` plus recent events/changes, then correlate the service-specific SLI. controller watches and permissions should be limited to owned resources/tenants. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### CRDS-AND-OPERATORS-SN-01

- [ ] **Question:** Design a production CRDs and operators capability where CRD schema, Finalizer and Webhook are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: structural OpenAPI validation/defaulting/pruning define accepted desired state. ensures external cleanup before deletion completes and can stick when controller fails. default/validate/convert custom resources with HA/certificate/timeout needs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CRDS-AND-OPERATORS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production CRDs and operators capability where Reconciler, Owner reference and Version conversion are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: level-based idempotent loop converges desired and observed state under retries. drives garbage collection for Kubernetes child resources. served/storage versions and conversion preserve compatibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CRDS-AND-OPERATORS-SN-03

- [ ] **Question:** Design a production CRDs and operators capability where Status subresource, Work queue and Controller leader election are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controller reports conditions/observedGeneration without mutating spec. event keys, rate limiting and retries coalesce reconciliation. only one active replica performs shared mutation while others stand by. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CRDS-AND-OPERATORS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production CRDs and operators capability where Finalizer, Webhook and RBAC/cache scope are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ensures external cleanup before deletion completes and can stick when controller fails. default/validate/convert custom resources with HA/certificate/timeout needs. controller watches and permissions should be limited to owned resources/tenants. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CRDS-AND-OPERATORS-SN-05

- [ ] **Question:** Design a production CRDs and operators capability where Owner reference, Version conversion and CRD schema are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: drives garbage collection for Kubernetes child resources. served/storage versions and conversion preserve compatibility. structural OpenAPI validation/defaulting/pruning define accepted desired state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CRDS-AND-OPERATORS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production CRDs and operators capability where Work queue, Controller leader election and Reconciler are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: event keys, rate limiting and retries coalesce reconciliation. only one active replica performs shared mutation while others stand by. level-based idempotent loop converges desired and observed state under retries. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CRDS-AND-OPERATORS-SN-07

- [ ] **Question:** Design a production CRDs and operators capability where Webhook, RBAC/cache scope and Status subresource are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: default/validate/convert custom resources with HA/certificate/timeout needs. controller watches and permissions should be limited to owned resources/tenants. controller reports conditions/observedGeneration without mutating spec. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CRDS-AND-OPERATORS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production CRDs and operators capability where Version conversion, CRD schema and Finalizer are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: served/storage versions and conversion preserve compatibility. structural OpenAPI validation/defaulting/pruning define accepted desired state. ensures external cleanup before deletion completes and can stick when controller fails. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CRDS-AND-OPERATORS-SN-09

- [ ] **Question:** Design a production CRDs and operators capability where Controller leader election, Reconciler and Owner reference are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: only one active replica performs shared mutation while others stand by. level-based idempotent loop converges desired and observed state under retries. drives garbage collection for Kubernetes child resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CRDS-AND-OPERATORS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production CRDs and operators capability where RBAC/cache scope, Status subresource and Work queue are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controller watches and permissions should be limited to owned resources/tenants. controller reports conditions/observedGeneration without mutating spec. event keys, rate limiting and retries coalesce reconciliation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### CRDS-AND-OPERATORS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CRD schema. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get crd` as one read-only checkpoint, not the whole diagnosis. structural OpenAPI validation/defaulting/pruning define accepted desired state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CRDS-AND-OPERATORS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reconciler. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl explain CRD_KIND.spec --recursive` as one read-only checkpoint, not the whole diagnosis. level-based idempotent loop converges desired and observed state under retries. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CRDS-AND-OPERATORS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Status subresource. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get CRD_KIND NAME -o yaml` as one read-only checkpoint, not the whole diagnosis. controller reports conditions/observedGeneration without mutating spec. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CRDS-AND-OPERATORS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Finalizer. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events --field-selector=involvedObject.kind=CRD_KIND` as one read-only checkpoint, not the whole diagnosis. ensures external cleanup before deletion completes and can stick when controller fails. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CRDS-AND-OPERATORS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Owner reference. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs deploy/CONTROLLER --since=30m` as one read-only checkpoint, not the whole diagnosis. drives garbage collection for Kubernetes child resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CRDS-AND-OPERATORS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Work queue. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get crd` as one read-only checkpoint, not the whole diagnosis. event keys, rate limiting and retries coalesce reconciliation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CRDS-AND-OPERATORS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Webhook. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl explain CRD_KIND.spec --recursive` as one read-only checkpoint, not the whole diagnosis. default/validate/convert custom resources with HA/certificate/timeout needs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CRDS-AND-OPERATORS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Version conversion. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get CRD_KIND NAME -o yaml` as one read-only checkpoint, not the whole diagnosis. served/storage versions and conversion preserve compatibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CRDS-AND-OPERATORS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Controller leader election. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events --field-selector=involvedObject.kind=CRD_KIND` as one read-only checkpoint, not the whole diagnosis. only one active replica performs shared mutation while others stand by. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CRDS-AND-OPERATORS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RBAC/cache scope. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs deploy/CONTROLLER --since=30m` as one read-only checkpoint, not the whole diagnosis. controller watches and permissions should be limited to owned resources/tenants. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
