# Packaging Extensions — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-PACKAGING-EXTENSIONS-JN-01

- [ ] **Question:** What is Helm chart, and why does it matter in Packaging Extensions?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** templates/default values/schema/dependencies/hooks package Kubernetes resources. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PACKAGING-EXTENSIONS-JN-02

- [ ] **Question:** What is Values merge, and why does it matter in Packaging Extensions?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** files/--set precedence and type coercion can produce surprising rendered output. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PACKAGING-EXTENSIONS-JN-03

- [ ] **Question:** What is CRD schema, and why does it matter in Packaging Extensions?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** structural OpenAPI validation/defaulting/pruning define accepted desired state. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PACKAGING-EXTENSIONS-JN-04

- [ ] **Question:** What is Reconciler, and why does it matter in Packaging Extensions?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** level-based idempotent loop converges desired and observed state under retries. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PACKAGING-EXTENSIONS-JN-05

- [ ] **Question:** What is Desired source, and why does it matter in Packaging Extensions?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Git/OCI revision plus render inputs is the audit/reconciliation truth. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PACKAGING-EXTENSIONS-JN-06

- [ ] **Question:** What is Reconciliation, and why does it matter in Packaging Extensions?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** controller compares live and desired then applies/prunes under policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PACKAGING-EXTENSIONS-JN-07

- [ ] **Question:** What is Helm chart, and why does it matter in Packaging Extensions?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** templates/default values/schema/dependencies/hooks package Kubernetes resources. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PACKAGING-EXTENSIONS-JN-08

- [ ] **Code:** **Question:** What does `kubectl get crd` help you verify for Packaging Extensions?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: files/--set precedence and type coercion can produce surprising rendered output.

### BRANCH-PACKAGING-EXTENSIONS-JN-09

- [ ] **Code:** **Question:** What does `argocd app diff APP` help you verify for Packaging Extensions?
> **Covered in:** [Packaging Extensions — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: structural OpenAPI validation/defaulting/pruning define accepted desired state.

### BRANCH-PACKAGING-EXTENSIONS-JN-10

- [ ] **Code:** **Question:** What does `helm lint CHART` help you verify for Packaging Extensions?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: level-based idempotent loop converges desired and observed state under retries.

## Junior — procedural and command questions

### BRANCH-PACKAGING-EXTENSIONS-JP-01

- [ ] **Code:** **Question:** A basic Helm chart check fails. What would you do first using the CLI?
> **Covered in:** [Packaging Extensions — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `helm lint CHART` and capture exact status/reason/request ID. templates/default values/schema/dependencies/hooks package Kubernetes resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PACKAGING-EXTENSIONS-JP-02

- [ ] **Question:** A basic Values merge check fails. What would you do first?
> **Covered in:** [Packaging Extensions — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get crd` and capture exact status/reason/request ID. files/--set precedence and type coercion can produce surprising rendered output. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PACKAGING-EXTENSIONS-JP-03

- [ ] **Question:** A basic CRD schema check fails. What would you do first?
> **Covered in:** [Packaging Extensions — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argocd app diff APP` and capture exact status/reason/request ID. structural OpenAPI validation/defaulting/pruning define accepted desired state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PACKAGING-EXTENSIONS-JP-04

- [ ] **Code:** **Question:** A basic Reconciler check fails. What would you do first using the CLI?
> **Covered in:** [Packaging Extensions — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `helm lint CHART` and capture exact status/reason/request ID. level-based idempotent loop converges desired and observed state under retries. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PACKAGING-EXTENSIONS-JP-05

- [ ] **Question:** A basic Desired source check fails. What would you do first?
> **Covered in:** [Packaging Extensions — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get crd` and capture exact status/reason/request ID. Git/OCI revision plus render inputs is the audit/reconciliation truth. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PACKAGING-EXTENSIONS-JP-06

- [ ] **Question:** A basic Reconciliation check fails. What would you do first?
> **Covered in:** [Packaging Extensions — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argocd app diff APP` and capture exact status/reason/request ID. controller compares live and desired then applies/prunes under policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PACKAGING-EXTENSIONS-JP-07

- [ ] **Code:** **Question:** A basic Helm chart check fails. What would you do first using the CLI?
> **Covered in:** [Packaging Extensions — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `helm lint CHART` and capture exact status/reason/request ID. templates/default values/schema/dependencies/hooks package Kubernetes resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PACKAGING-EXTENSIONS-JP-08

- [ ] **Question:** A basic Values merge check fails. What would you do first?
> **Covered in:** [Packaging Extensions — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get crd` and capture exact status/reason/request ID. files/--set precedence and type coercion can produce surprising rendered output. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PACKAGING-EXTENSIONS-JP-09

- [ ] **Question:** A basic CRD schema check fails. What would you do first?
> **Covered in:** [Packaging Extensions — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argocd app diff APP` and capture exact status/reason/request ID. structural OpenAPI validation/defaulting/pruning define accepted desired state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PACKAGING-EXTENSIONS-JP-10

- [ ] **Code:** **Question:** A basic Reconciler check fails. What would you do first using the CLI?
> **Covered in:** [Packaging Extensions — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `helm lint CHART` and capture exact status/reason/request ID. level-based idempotent loop converges desired and observed state under retries. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-PACKAGING-EXTENSIONS-MN-01

- [ ] **Question:** Compare Helm chart with Values merge. When would each change your design?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Helm chart: templates/default values/schema/dependencies/hooks package Kubernetes resources. Values merge: files/--set precedence and type coercion can produce surprising rendered output. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PACKAGING-EXTENSIONS-MN-02

- [ ] **Question:** Compare Values merge with CRD schema. When would each change your design?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Values merge: files/--set precedence and type coercion can produce surprising rendered output. CRD schema: structural OpenAPI validation/defaulting/pruning define accepted desired state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PACKAGING-EXTENSIONS-MN-03

- [ ] **Question:** Compare CRD schema with Reconciler. When would each change your design?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CRD schema: structural OpenAPI validation/defaulting/pruning define accepted desired state. Reconciler: level-based idempotent loop converges desired and observed state under retries. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PACKAGING-EXTENSIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Reconciler with Desired source. When would each change your design?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Reconciler: level-based idempotent loop converges desired and observed state under retries. Desired source: Git/OCI revision plus render inputs is the audit/reconciliation truth. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PACKAGING-EXTENSIONS-MN-05

- [ ] **Question:** Compare Desired source with Reconciliation. When would each change your design?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Desired source: Git/OCI revision plus render inputs is the audit/reconciliation truth. Reconciliation: controller compares live and desired then applies/prunes under policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PACKAGING-EXTENSIONS-MN-06

- [ ] **Question:** Compare Reconciliation with Helm chart. When would each change your design?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Reconciliation: controller compares live and desired then applies/prunes under policy. Helm chart: templates/default values/schema/dependencies/hooks package Kubernetes resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PACKAGING-EXTENSIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Helm chart with Values merge. When would each change your design?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Helm chart: templates/default values/schema/dependencies/hooks package Kubernetes resources. Values merge: files/--set precedence and type coercion can produce surprising rendered output. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PACKAGING-EXTENSIONS-MN-08

- [ ] **Question:** Compare Values merge with CRD schema. When would each change your design?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Values merge: files/--set precedence and type coercion can produce surprising rendered output. CRD schema: structural OpenAPI validation/defaulting/pruning define accepted desired state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PACKAGING-EXTENSIONS-MN-09

- [ ] **Question:** Compare CRD schema with Reconciler. When would each change your design?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CRD schema: structural OpenAPI validation/defaulting/pruning define accepted desired state. Reconciler: level-based idempotent loop converges desired and observed state under retries. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PACKAGING-EXTENSIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Reconciler with Helm chart. When would each change your design?
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Reconciler: level-based idempotent loop converges desired and observed state under retries. Helm chart: templates/default values/schema/dependencies/hooks package Kubernetes resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-PACKAGING-EXTENSIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Helm chart; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `helm lint CHART` plus recent events/changes, then correlate the service-specific SLI. templates/default values/schema/dependencies/hooks package Kubernetes resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PACKAGING-EXTENSIONS-MP-02

- [ ] **Question:** Production is degraded around Values merge; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get crd` plus recent events/changes, then correlate the service-specific SLI. files/--set precedence and type coercion can produce surprising rendered output. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PACKAGING-EXTENSIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around CRD schema; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argocd app diff APP` plus recent events/changes, then correlate the service-specific SLI. structural OpenAPI validation/defaulting/pruning define accepted desired state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PACKAGING-EXTENSIONS-MP-04

- [ ] **Question:** Production is degraded around Reconciler; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `helm lint CHART` plus recent events/changes, then correlate the service-specific SLI. level-based idempotent loop converges desired and observed state under retries. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PACKAGING-EXTENSIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Desired source; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get crd` plus recent events/changes, then correlate the service-specific SLI. Git/OCI revision plus render inputs is the audit/reconciliation truth. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PACKAGING-EXTENSIONS-MP-06

- [ ] **Question:** Production is degraded around Reconciliation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argocd app diff APP` plus recent events/changes, then correlate the service-specific SLI. controller compares live and desired then applies/prunes under policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PACKAGING-EXTENSIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Helm chart; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `helm lint CHART` plus recent events/changes, then correlate the service-specific SLI. templates/default values/schema/dependencies/hooks package Kubernetes resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PACKAGING-EXTENSIONS-MP-08

- [ ] **Question:** Production is degraded around Values merge; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get crd` plus recent events/changes, then correlate the service-specific SLI. files/--set precedence and type coercion can produce surprising rendered output. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PACKAGING-EXTENSIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around CRD schema; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argocd app diff APP` plus recent events/changes, then correlate the service-specific SLI. structural OpenAPI validation/defaulting/pruning define accepted desired state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PACKAGING-EXTENSIONS-MP-10

- [ ] **Question:** Production is degraded around Reconciler; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `helm lint CHART` plus recent events/changes, then correlate the service-specific SLI. level-based idempotent loop converges desired and observed state under retries. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-PACKAGING-EXTENSIONS-SN-01

- [ ] **Question:** Design a production Packaging Extensions capability where Helm chart, Reconciler and Helm chart are first-class requirements.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: templates/default values/schema/dependencies/hooks package Kubernetes resources. level-based idempotent loop converges desired and observed state under retries. templates/default values/schema/dependencies/hooks package Kubernetes resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PACKAGING-EXTENSIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Packaging Extensions capability where Values merge, Desired source and Values merge are first-class requirements.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: files/--set precedence and type coercion can produce surprising rendered output. Git/OCI revision plus render inputs is the audit/reconciliation truth. files/--set precedence and type coercion can produce surprising rendered output. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PACKAGING-EXTENSIONS-SN-03

- [ ] **Question:** Design a production Packaging Extensions capability where CRD schema, Reconciliation and CRD schema are first-class requirements.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: structural OpenAPI validation/defaulting/pruning define accepted desired state. controller compares live and desired then applies/prunes under policy. structural OpenAPI validation/defaulting/pruning define accepted desired state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PACKAGING-EXTENSIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Packaging Extensions capability where Reconciler, Helm chart and Reconciler are first-class requirements.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: level-based idempotent loop converges desired and observed state under retries. templates/default values/schema/dependencies/hooks package Kubernetes resources. level-based idempotent loop converges desired and observed state under retries. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PACKAGING-EXTENSIONS-SN-05

- [ ] **Question:** Design a production Packaging Extensions capability where Desired source, Values merge and Helm chart are first-class requirements.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Git/OCI revision plus render inputs is the audit/reconciliation truth. files/--set precedence and type coercion can produce surprising rendered output. templates/default values/schema/dependencies/hooks package Kubernetes resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PACKAGING-EXTENSIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Packaging Extensions capability where Reconciliation, CRD schema and Values merge are first-class requirements.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controller compares live and desired then applies/prunes under policy. structural OpenAPI validation/defaulting/pruning define accepted desired state. files/--set precedence and type coercion can produce surprising rendered output. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PACKAGING-EXTENSIONS-SN-07

- [ ] **Question:** Design a production Packaging Extensions capability where Helm chart, Reconciler and CRD schema are first-class requirements.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: templates/default values/schema/dependencies/hooks package Kubernetes resources. level-based idempotent loop converges desired and observed state under retries. structural OpenAPI validation/defaulting/pruning define accepted desired state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PACKAGING-EXTENSIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Packaging Extensions capability where Values merge, Helm chart and Reconciler are first-class requirements.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: files/--set precedence and type coercion can produce surprising rendered output. templates/default values/schema/dependencies/hooks package Kubernetes resources. level-based idempotent loop converges desired and observed state under retries. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PACKAGING-EXTENSIONS-SN-09

- [ ] **Question:** Design a production Packaging Extensions capability where CRD schema, Values merge and Desired source are first-class requirements.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: structural OpenAPI validation/defaulting/pruning define accepted desired state. files/--set precedence and type coercion can produce surprising rendered output. Git/OCI revision plus render inputs is the audit/reconciliation truth. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PACKAGING-EXTENSIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Packaging Extensions capability where Reconciler, CRD schema and Reconciliation are first-class requirements.
> **Covered in:** [Packaging Extensions — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: level-based idempotent loop converges desired and observed state under retries. structural OpenAPI validation/defaulting/pruning define accepted desired state. controller compares live and desired then applies/prunes under policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-PACKAGING-EXTENSIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Helm chart. How do you lead it end to end?
> **Covered in:** [Packaging Extensions — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `helm lint CHART` as one read-only checkpoint, not the whole diagnosis. templates/default values/schema/dependencies/hooks package Kubernetes resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PACKAGING-EXTENSIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Values merge. How do you lead it end to end?
> **Covered in:** [Packaging Extensions — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get crd` as one read-only checkpoint, not the whole diagnosis. files/--set precedence and type coercion can produce surprising rendered output. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PACKAGING-EXTENSIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CRD schema. How do you lead it end to end?
> **Covered in:** [Packaging Extensions — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argocd app diff APP` as one read-only checkpoint, not the whole diagnosis. structural OpenAPI validation/defaulting/pruning define accepted desired state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PACKAGING-EXTENSIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reconciler. How do you lead it end to end?
> **Covered in:** [Packaging Extensions — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `helm lint CHART` as one read-only checkpoint, not the whole diagnosis. level-based idempotent loop converges desired and observed state under retries. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PACKAGING-EXTENSIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Desired source. How do you lead it end to end?
> **Covered in:** [Packaging Extensions — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get crd` as one read-only checkpoint, not the whole diagnosis. Git/OCI revision plus render inputs is the audit/reconciliation truth. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PACKAGING-EXTENSIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reconciliation. How do you lead it end to end?
> **Covered in:** [Packaging Extensions — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argocd app diff APP` as one read-only checkpoint, not the whole diagnosis. controller compares live and desired then applies/prunes under policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PACKAGING-EXTENSIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Helm chart. How do you lead it end to end?
> **Covered in:** [Packaging Extensions — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `helm lint CHART` as one read-only checkpoint, not the whole diagnosis. templates/default values/schema/dependencies/hooks package Kubernetes resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PACKAGING-EXTENSIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Values merge. How do you lead it end to end?
> **Covered in:** [Packaging Extensions — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get crd` as one read-only checkpoint, not the whole diagnosis. files/--set precedence and type coercion can produce surprising rendered output. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PACKAGING-EXTENSIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CRD schema. How do you lead it end to end?
> **Covered in:** [Packaging Extensions — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argocd app diff APP` as one read-only checkpoint, not the whole diagnosis. structural OpenAPI validation/defaulting/pruning define accepted desired state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PACKAGING-EXTENSIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reconciler. How do you lead it end to end?
> **Covered in:** [Packaging Extensions — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `helm lint CHART` as one read-only checkpoint, not the whole diagnosis. level-based idempotent loop converges desired and observed state under retries. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: PDB, priority, preemption and eviction](../06-scheduling-autoscaling/05-disruption-priority/README.md) · [Study note](README.md) · [Next: Helm and Kustomize →](01-helm-kustomize/README.md)

<!-- reading-navigation:end -->
