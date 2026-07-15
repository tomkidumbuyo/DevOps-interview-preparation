# Argo CD, Flux and GitOps — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### ARGO-CD-FLUX-AND-GITOPS-JN-01

- [ ] **Question:** What is Desired source, and why does it matter in Argo CD, Flux and GitOps?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Git/OCI revision plus render inputs is the audit/reconciliation truth. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ARGO-CD-FLUX-AND-GITOPS-JN-02

- [ ] **Question:** What is Reconciliation, and why does it matter in Argo CD, Flux and GitOps?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** controller compares live and desired then applies/prunes under policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ARGO-CD-FLUX-AND-GITOPS-JN-03

- [ ] **Question:** What is Health, and why does it matter in Argo CD, Flux and GitOps?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** resource-specific status estimates rollout but needs user/SLO verification. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ARGO-CD-FLUX-AND-GITOPS-JN-04

- [ ] **Question:** What is Sync wave/hook, and why does it matter in Argo CD, Flux and GitOps?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** orders dependencies/migrations with failure and idempotency concerns. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ARGO-CD-FLUX-AND-GITOPS-JN-05

- [ ] **Question:** What is ApplicationSet/Flux Kustomization, and why does it matter in Argo CD, Flux and GitOps?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** generates fleet/environment instances from controlled templates. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ARGO-CD-FLUX-AND-GITOPS-JN-06

- [ ] **Question:** What is Project/tenant boundary, and why does it matter in Argo CD, Flux and GitOps?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** limits source repositories, clusters/namespaces and resource kinds. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ARGO-CD-FLUX-AND-GITOPS-JN-07

- [ ] **Question:** What is Prune/self-heal, and why does it matter in Argo CD, Flux and GitOps?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** deletes drifted/removed resources and can amplify a bad commit. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ARGO-CD-FLUX-AND-GITOPS-JN-08

- [ ] **Code:** **Question:** What does `argocd app wait APP --health --sync` help you verify for Argo CD, Flux and GitOps?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: encrypted/external secret references prevent plaintext Git while preserving rotation.

### ARGO-CD-FLUX-AND-GITOPS-JN-09

- [ ] **Code:** **Question:** What does `flux get kustomizations -A` help you verify for Argo CD, Flux and GitOps?
> **Covered in:** [Argo CD, Flux and GitOps — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: pull request updates immutable artifact/version between environment sources.

### ARGO-CD-FLUX-AND-GITOPS-JN-10

- [ ] **Code:** **Question:** What does `flux reconcile kustomization NAME --with-source` help you verify for Argo CD, Flux and GitOps?
> **Covered in:** [Argo CD, Flux and GitOps — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: pause/reconcile source quickly so controller does not revert mitigation.

## Junior — procedural and command questions

### ARGO-CD-FLUX-AND-GITOPS-JP-01

- [ ] **Code:** **Question:** A basic Desired source check fails. What would you do first using the CLI?
> **Covered in:** [Argo CD, Flux and GitOps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argocd app diff APP` and capture exact status/reason/request ID. Git/OCI revision plus render inputs is the audit/reconciliation truth. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ARGO-CD-FLUX-AND-GITOPS-JP-02

- [ ] **Question:** A basic Reconciliation check fails. What would you do first?
> **Covered in:** [Argo CD, Flux and GitOps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argocd app sync APP --revision REV` and capture exact status/reason/request ID. controller compares live and desired then applies/prunes under policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ARGO-CD-FLUX-AND-GITOPS-JP-03

- [ ] **Question:** A basic Health check fails. What would you do first?
> **Covered in:** [Argo CD, Flux and GitOps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argocd app wait APP --health --sync` and capture exact status/reason/request ID. resource-specific status estimates rollout but needs user/SLO verification. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ARGO-CD-FLUX-AND-GITOPS-JP-04

- [ ] **Code:** **Question:** A basic Sync wave/hook check fails. What would you do first using the CLI?
> **Covered in:** [Argo CD, Flux and GitOps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `flux get kustomizations -A` and capture exact status/reason/request ID. orders dependencies/migrations with failure and idempotency concerns. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ARGO-CD-FLUX-AND-GITOPS-JP-05

- [ ] **Question:** A basic ApplicationSet/Flux Kustomization check fails. What would you do first?
> **Covered in:** [Argo CD, Flux and GitOps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `flux reconcile kustomization NAME --with-source` and capture exact status/reason/request ID. generates fleet/environment instances from controlled templates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ARGO-CD-FLUX-AND-GITOPS-JP-06

- [ ] **Question:** A basic Project/tenant boundary check fails. What would you do first?
> **Covered in:** [Argo CD, Flux and GitOps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argocd app diff APP` and capture exact status/reason/request ID. limits source repositories, clusters/namespaces and resource kinds. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ARGO-CD-FLUX-AND-GITOPS-JP-07

- [ ] **Code:** **Question:** A basic Prune/self-heal check fails. What would you do first using the CLI?
> **Covered in:** [Argo CD, Flux and GitOps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argocd app sync APP --revision REV` and capture exact status/reason/request ID. deletes drifted/removed resources and can amplify a bad commit. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ARGO-CD-FLUX-AND-GITOPS-JP-08

- [ ] **Question:** A basic Secret workflow check fails. What would you do first?
> **Covered in:** [Argo CD, Flux and GitOps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argocd app wait APP --health --sync` and capture exact status/reason/request ID. encrypted/external secret references prevent plaintext Git while preserving rotation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ARGO-CD-FLUX-AND-GITOPS-JP-09

- [ ] **Question:** A basic Promotion check fails. What would you do first?
> **Covered in:** [Argo CD, Flux and GitOps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `flux get kustomizations -A` and capture exact status/reason/request ID. pull request updates immutable artifact/version between environment sources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ARGO-CD-FLUX-AND-GITOPS-JP-10

- [ ] **Code:** **Question:** A basic Emergency change check fails. What would you do first using the CLI?
> **Covered in:** [Argo CD, Flux and GitOps — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `flux reconcile kustomization NAME --with-source` and capture exact status/reason/request ID. pause/reconcile source quickly so controller does not revert mitigation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### ARGO-CD-FLUX-AND-GITOPS-MN-01

- [ ] **Question:** Compare Desired source with Reconciliation. When would each change your design?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Desired source: Git/OCI revision plus render inputs is the audit/reconciliation truth. Reconciliation: controller compares live and desired then applies/prunes under policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ARGO-CD-FLUX-AND-GITOPS-MN-02

- [ ] **Question:** Compare Reconciliation with Health. When would each change your design?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Reconciliation: controller compares live and desired then applies/prunes under policy. Health: resource-specific status estimates rollout but needs user/SLO verification. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ARGO-CD-FLUX-AND-GITOPS-MN-03

- [ ] **Question:** Compare Health with Sync wave/hook. When would each change your design?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Health: resource-specific status estimates rollout but needs user/SLO verification. Sync wave/hook: orders dependencies/migrations with failure and idempotency concerns. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ARGO-CD-FLUX-AND-GITOPS-MN-04

- [ ] **Configuration review:** **Question:** Compare Sync wave/hook with ApplicationSet/Flux Kustomization. When would each change your design?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Sync wave/hook: orders dependencies/migrations with failure and idempotency concerns. ApplicationSet/Flux Kustomization: generates fleet/environment instances from controlled templates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ARGO-CD-FLUX-AND-GITOPS-MN-05

- [ ] **Question:** Compare ApplicationSet/Flux Kustomization with Project/tenant boundary. When would each change your design?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ApplicationSet/Flux Kustomization: generates fleet/environment instances from controlled templates. Project/tenant boundary: limits source repositories, clusters/namespaces and resource kinds. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ARGO-CD-FLUX-AND-GITOPS-MN-06

- [ ] **Question:** Compare Project/tenant boundary with Prune/self-heal. When would each change your design?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Project/tenant boundary: limits source repositories, clusters/namespaces and resource kinds. Prune/self-heal: deletes drifted/removed resources and can amplify a bad commit. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ARGO-CD-FLUX-AND-GITOPS-MN-07

- [ ] **Configuration review:** **Question:** Compare Prune/self-heal with Secret workflow. When would each change your design?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Prune/self-heal: deletes drifted/removed resources and can amplify a bad commit. Secret workflow: encrypted/external secret references prevent plaintext Git while preserving rotation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ARGO-CD-FLUX-AND-GITOPS-MN-08

- [ ] **Question:** Compare Secret workflow with Promotion. When would each change your design?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Secret workflow: encrypted/external secret references prevent plaintext Git while preserving rotation. Promotion: pull request updates immutable artifact/version between environment sources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ARGO-CD-FLUX-AND-GITOPS-MN-09

- [ ] **Question:** Compare Promotion with Emergency change. When would each change your design?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Promotion: pull request updates immutable artifact/version between environment sources. Emergency change: pause/reconcile source quickly so controller does not revert mitigation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ARGO-CD-FLUX-AND-GITOPS-MN-10

- [ ] **Configuration review:** **Question:** Compare Emergency change with Desired source. When would each change your design?
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Emergency change: pause/reconcile source quickly so controller does not revert mitigation. Desired source: Git/OCI revision plus render inputs is the audit/reconciliation truth. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### ARGO-CD-FLUX-AND-GITOPS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Desired source; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argocd app diff APP` plus recent events/changes, then correlate the service-specific SLI. Git/OCI revision plus render inputs is the audit/reconciliation truth. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ARGO-CD-FLUX-AND-GITOPS-MP-02

- [ ] **Question:** Production is degraded around Reconciliation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argocd app sync APP --revision REV` plus recent events/changes, then correlate the service-specific SLI. controller compares live and desired then applies/prunes under policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ARGO-CD-FLUX-AND-GITOPS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Health; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argocd app wait APP --health --sync` plus recent events/changes, then correlate the service-specific SLI. resource-specific status estimates rollout but needs user/SLO verification. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ARGO-CD-FLUX-AND-GITOPS-MP-04

- [ ] **Question:** Production is degraded around Sync wave/hook; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `flux get kustomizations -A` plus recent events/changes, then correlate the service-specific SLI. orders dependencies/migrations with failure and idempotency concerns. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ARGO-CD-FLUX-AND-GITOPS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around ApplicationSet/Flux Kustomization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `flux reconcile kustomization NAME --with-source` plus recent events/changes, then correlate the service-specific SLI. generates fleet/environment instances from controlled templates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ARGO-CD-FLUX-AND-GITOPS-MP-06

- [ ] **Question:** Production is degraded around Project/tenant boundary; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argocd app diff APP` plus recent events/changes, then correlate the service-specific SLI. limits source repositories, clusters/namespaces and resource kinds. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ARGO-CD-FLUX-AND-GITOPS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Prune/self-heal; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argocd app sync APP --revision REV` plus recent events/changes, then correlate the service-specific SLI. deletes drifted/removed resources and can amplify a bad commit. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ARGO-CD-FLUX-AND-GITOPS-MP-08

- [ ] **Question:** Production is degraded around Secret workflow; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argocd app wait APP --health --sync` plus recent events/changes, then correlate the service-specific SLI. encrypted/external secret references prevent plaintext Git while preserving rotation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ARGO-CD-FLUX-AND-GITOPS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Promotion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `flux get kustomizations -A` plus recent events/changes, then correlate the service-specific SLI. pull request updates immutable artifact/version between environment sources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ARGO-CD-FLUX-AND-GITOPS-MP-10

- [ ] **Question:** Production is degraded around Emergency change; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `flux reconcile kustomization NAME --with-source` plus recent events/changes, then correlate the service-specific SLI. pause/reconcile source quickly so controller does not revert mitigation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### ARGO-CD-FLUX-AND-GITOPS-SN-01

- [ ] **Question:** Design a production Argo CD, Flux and GitOps capability where Desired source, Sync wave/hook and Prune/self-heal are first-class requirements.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Git/OCI revision plus render inputs is the audit/reconciliation truth. orders dependencies/migrations with failure and idempotency concerns. deletes drifted/removed resources and can amplify a bad commit. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ARGO-CD-FLUX-AND-GITOPS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Argo CD, Flux and GitOps capability where Reconciliation, ApplicationSet/Flux Kustomization and Secret workflow are first-class requirements.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controller compares live and desired then applies/prunes under policy. generates fleet/environment instances from controlled templates. encrypted/external secret references prevent plaintext Git while preserving rotation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ARGO-CD-FLUX-AND-GITOPS-SN-03

- [ ] **Question:** Design a production Argo CD, Flux and GitOps capability where Health, Project/tenant boundary and Promotion are first-class requirements.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: resource-specific status estimates rollout but needs user/SLO verification. limits source repositories, clusters/namespaces and resource kinds. pull request updates immutable artifact/version between environment sources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ARGO-CD-FLUX-AND-GITOPS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Argo CD, Flux and GitOps capability where Sync wave/hook, Prune/self-heal and Emergency change are first-class requirements.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: orders dependencies/migrations with failure and idempotency concerns. deletes drifted/removed resources and can amplify a bad commit. pause/reconcile source quickly so controller does not revert mitigation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ARGO-CD-FLUX-AND-GITOPS-SN-05

- [ ] **Question:** Design a production Argo CD, Flux and GitOps capability where ApplicationSet/Flux Kustomization, Secret workflow and Desired source are first-class requirements.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: generates fleet/environment instances from controlled templates. encrypted/external secret references prevent plaintext Git while preserving rotation. Git/OCI revision plus render inputs is the audit/reconciliation truth. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ARGO-CD-FLUX-AND-GITOPS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Argo CD, Flux and GitOps capability where Project/tenant boundary, Promotion and Reconciliation are first-class requirements.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: limits source repositories, clusters/namespaces and resource kinds. pull request updates immutable artifact/version between environment sources. controller compares live and desired then applies/prunes under policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ARGO-CD-FLUX-AND-GITOPS-SN-07

- [ ] **Question:** Design a production Argo CD, Flux and GitOps capability where Prune/self-heal, Emergency change and Health are first-class requirements.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: deletes drifted/removed resources and can amplify a bad commit. pause/reconcile source quickly so controller does not revert mitigation. resource-specific status estimates rollout but needs user/SLO verification. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ARGO-CD-FLUX-AND-GITOPS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Argo CD, Flux and GitOps capability where Secret workflow, Desired source and Sync wave/hook are first-class requirements.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: encrypted/external secret references prevent plaintext Git while preserving rotation. Git/OCI revision plus render inputs is the audit/reconciliation truth. orders dependencies/migrations with failure and idempotency concerns. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ARGO-CD-FLUX-AND-GITOPS-SN-09

- [ ] **Question:** Design a production Argo CD, Flux and GitOps capability where Promotion, Reconciliation and ApplicationSet/Flux Kustomization are first-class requirements.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pull request updates immutable artifact/version between environment sources. controller compares live and desired then applies/prunes under policy. generates fleet/environment instances from controlled templates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ARGO-CD-FLUX-AND-GITOPS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Argo CD, Flux and GitOps capability where Emergency change, Health and Project/tenant boundary are first-class requirements.
> **Covered in:** [Argo CD, Flux and GitOps — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pause/reconcile source quickly so controller does not revert mitigation. resource-specific status estimates rollout but needs user/SLO verification. limits source repositories, clusters/namespaces and resource kinds. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### ARGO-CD-FLUX-AND-GITOPS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Desired source. How do you lead it end to end?
> **Covered in:** [Argo CD, Flux and GitOps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argocd app diff APP` as one read-only checkpoint, not the whole diagnosis. Git/OCI revision plus render inputs is the audit/reconciliation truth. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ARGO-CD-FLUX-AND-GITOPS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reconciliation. How do you lead it end to end?
> **Covered in:** [Argo CD, Flux and GitOps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argocd app sync APP --revision REV` as one read-only checkpoint, not the whole diagnosis. controller compares live and desired then applies/prunes under policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ARGO-CD-FLUX-AND-GITOPS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Health. How do you lead it end to end?
> **Covered in:** [Argo CD, Flux and GitOps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argocd app wait APP --health --sync` as one read-only checkpoint, not the whole diagnosis. resource-specific status estimates rollout but needs user/SLO verification. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ARGO-CD-FLUX-AND-GITOPS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Sync wave/hook. How do you lead it end to end?
> **Covered in:** [Argo CD, Flux and GitOps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `flux get kustomizations -A` as one read-only checkpoint, not the whole diagnosis. orders dependencies/migrations with failure and idempotency concerns. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ARGO-CD-FLUX-AND-GITOPS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ApplicationSet/Flux Kustomization. How do you lead it end to end?
> **Covered in:** [Argo CD, Flux and GitOps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `flux reconcile kustomization NAME --with-source` as one read-only checkpoint, not the whole diagnosis. generates fleet/environment instances from controlled templates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ARGO-CD-FLUX-AND-GITOPS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Project/tenant boundary. How do you lead it end to end?
> **Covered in:** [Argo CD, Flux and GitOps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argocd app diff APP` as one read-only checkpoint, not the whole diagnosis. limits source repositories, clusters/namespaces and resource kinds. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ARGO-CD-FLUX-AND-GITOPS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prune/self-heal. How do you lead it end to end?
> **Covered in:** [Argo CD, Flux and GitOps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argocd app sync APP --revision REV` as one read-only checkpoint, not the whole diagnosis. deletes drifted/removed resources and can amplify a bad commit. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ARGO-CD-FLUX-AND-GITOPS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secret workflow. How do you lead it end to end?
> **Covered in:** [Argo CD, Flux and GitOps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argocd app wait APP --health --sync` as one read-only checkpoint, not the whole diagnosis. encrypted/external secret references prevent plaintext Git while preserving rotation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ARGO-CD-FLUX-AND-GITOPS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Promotion. How do you lead it end to end?
> **Covered in:** [Argo CD, Flux and GitOps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `flux get kustomizations -A` as one read-only checkpoint, not the whole diagnosis. pull request updates immutable artifact/version between environment sources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ARGO-CD-FLUX-AND-GITOPS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Emergency change. How do you lead it end to end?
> **Covered in:** [Argo CD, Flux and GitOps — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `flux reconcile kustomization NAME --with-source` as one read-only checkpoint, not the whole diagnosis. pause/reconcile source quickly so controller does not revert mitigation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: CRDs and operators](../02-crds-operators/README.md) · [Study note](README.md) · [Next: Operations →](../../08-operations/README.md)

<!-- reading-navigation:end -->
