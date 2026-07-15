# Kubernetes upgrades and API deprecations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JN-01

- [ ] **Question:** What is Version skew, and why does it matter in Kubernetes upgrades and API deprecations?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JN-02

- [ ] **Question:** What is API deprecation, and why does it matter in Kubernetes upgrades and API deprecations?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** served versions are removed on schedule and manifests/clients/controllers must migrate. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JN-03

- [ ] **Question:** What is Storage version, and why does it matter in Kubernetes upgrades and API deprecations?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** existing objects may remain encoded in old version until storage migration/update. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JN-04

- [ ] **Question:** What is Control-plane first, and why does it matter in Kubernetes upgrades and API deprecations?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** managed/self-managed procedures normally upgrade API before nodes within skew. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JN-05

- [ ] **Question:** What is Add-on compatibility, and why does it matter in Kubernetes upgrades and API deprecations?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CNI/CSI/CoreDNS/proxy/metrics/admission/operator versions need matrices. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JN-06

- [ ] **Question:** What is Canary node pool, and why does it matter in Kubernetes upgrades and API deprecations?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** validates image/runtime/kernel/driver/workload before fleet drain. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JN-07

- [ ] **Question:** What is Drain/PDB, and why does it matter in Kubernetes upgrades and API deprecations?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** maintenance success depends on budgets, state/storage and graceful termination. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JN-08

- [ ] **Code:** **Question:** What does `kubectl get crd -o json | jq '.items[] | {name:.metadata.name,storedVersions:.status.storedVersions}'` help you verify for Kubernetes upgrades and API deprecations?
> **Covered in:** [Kubernetes upgrades and API deprecations — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: webhook and stored-version correctness must precede removing versions.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JN-09

- [ ] **Code:** **Question:** What does `kubectl version` help you verify for Kubernetes upgrades and API deprecations?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: control-plane downgrade is often unavailable, so backups/blue-green cluster migration matter.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JN-10

- [ ] **Code:** **Question:** What does `kubectl get --raw /version` help you verify for Kubernetes upgrades and API deprecations?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: conformance plus real workload/SLO/security/DR validates more than node Ready.

## Junior — procedural and command questions

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JP-01

- [ ] **Code:** **Question:** A basic Version skew check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes upgrades and API deprecations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl version` and capture exact status/reason/request ID. supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JP-02

- [ ] **Question:** A basic API deprecation check fails. What would you do first?
> **Covered in:** [Kubernetes upgrades and API deprecations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /version` and capture exact status/reason/request ID. served versions are removed on schedule and manifests/clients/controllers must migrate. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JP-03

- [ ] **Question:** A basic Storage version check fails. What would you do first?
> **Covered in:** [Kubernetes upgrades and API deprecations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /metrics | rg apiserver_requested_deprecated_apis` and capture exact status/reason/request ID. existing objects may remain encoded in old version until storage migration/update. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JP-04

- [ ] **Code:** **Question:** A basic Control-plane first check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes upgrades and API deprecations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get crd -o json | jq '.items[] | {name:.metadata.name,storedVersions:.status.storedVersions}'` and capture exact status/reason/request ID. managed/self-managed procedures normally upgrade API before nodes within skew. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JP-05

- [ ] **Question:** A basic Add-on compatibility check fails. What would you do first?
> **Covered in:** [Kubernetes upgrades and API deprecations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl version` and capture exact status/reason/request ID. CNI/CSI/CoreDNS/proxy/metrics/admission/operator versions need matrices. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JP-06

- [ ] **Question:** A basic Canary node pool check fails. What would you do first?
> **Covered in:** [Kubernetes upgrades and API deprecations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /version` and capture exact status/reason/request ID. validates image/runtime/kernel/driver/workload before fleet drain. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JP-07

- [ ] **Code:** **Question:** A basic Drain/PDB check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes upgrades and API deprecations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /metrics | rg apiserver_requested_deprecated_apis` and capture exact status/reason/request ID. maintenance success depends on budgets, state/storage and graceful termination. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JP-08

- [ ] **Question:** A basic CRD conversion check fails. What would you do first?
> **Covered in:** [Kubernetes upgrades and API deprecations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get crd -o json | jq '.items[] | {name:.metadata.name,storedVersions:.status.storedVersions}'` and capture exact status/reason/request ID. webhook and stored-version correctness must precede removing versions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JP-09

- [ ] **Question:** A basic Rollback check fails. What would you do first?
> **Covered in:** [Kubernetes upgrades and API deprecations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl version` and capture exact status/reason/request ID. control-plane downgrade is often unavailable, so backups/blue-green cluster migration matter. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-JP-10

- [ ] **Code:** **Question:** A basic Qualification check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes upgrades and API deprecations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw /version` and capture exact status/reason/request ID. conformance plus real workload/SLO/security/DR validates more than node Ready. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MN-01

- [ ] **Question:** Compare Version skew with API deprecation. When would each change your design?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Version skew: supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. API deprecation: served versions are removed on schedule and manifests/clients/controllers must migrate. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MN-02

- [ ] **Question:** Compare API deprecation with Storage version. When would each change your design?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** API deprecation: served versions are removed on schedule and manifests/clients/controllers must migrate. Storage version: existing objects may remain encoded in old version until storage migration/update. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MN-03

- [ ] **Question:** Compare Storage version with Control-plane first. When would each change your design?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Storage version: existing objects may remain encoded in old version until storage migration/update. Control-plane first: managed/self-managed procedures normally upgrade API before nodes within skew. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Control-plane first with Add-on compatibility. When would each change your design?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Control-plane first: managed/self-managed procedures normally upgrade API before nodes within skew. Add-on compatibility: CNI/CSI/CoreDNS/proxy/metrics/admission/operator versions need matrices. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MN-05

- [ ] **Question:** Compare Add-on compatibility with Canary node pool. When would each change your design?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Add-on compatibility: CNI/CSI/CoreDNS/proxy/metrics/admission/operator versions need matrices. Canary node pool: validates image/runtime/kernel/driver/workload before fleet drain. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MN-06

- [ ] **Question:** Compare Canary node pool with Drain/PDB. When would each change your design?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Canary node pool: validates image/runtime/kernel/driver/workload before fleet drain. Drain/PDB: maintenance success depends on budgets, state/storage and graceful termination. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Drain/PDB with CRD conversion. When would each change your design?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Drain/PDB: maintenance success depends on budgets, state/storage and graceful termination. CRD conversion: webhook and stored-version correctness must precede removing versions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MN-08

- [ ] **Question:** Compare CRD conversion with Rollback. When would each change your design?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CRD conversion: webhook and stored-version correctness must precede removing versions. Rollback: control-plane downgrade is often unavailable, so backups/blue-green cluster migration matter. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MN-09

- [ ] **Question:** Compare Rollback with Qualification. When would each change your design?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Rollback: control-plane downgrade is often unavailable, so backups/blue-green cluster migration matter. Qualification: conformance plus real workload/SLO/security/DR validates more than node Ready. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Qualification with Version skew. When would each change your design?
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Qualification: conformance plus real workload/SLO/security/DR validates more than node Ready. Version skew: supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Version skew; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl version` plus recent events/changes, then correlate the service-specific SLI. supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MP-02

- [ ] **Question:** Production is degraded around API deprecation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /version` plus recent events/changes, then correlate the service-specific SLI. served versions are removed on schedule and manifests/clients/controllers must migrate. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Storage version; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /metrics | rg apiserver_requested_deprecated_apis` plus recent events/changes, then correlate the service-specific SLI. existing objects may remain encoded in old version until storage migration/update. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MP-04

- [ ] **Question:** Production is degraded around Control-plane first; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get crd -o json | jq '.items[] | {name:.metadata.name,storedVersions:.status.storedVersions}'` plus recent events/changes, then correlate the service-specific SLI. managed/self-managed procedures normally upgrade API before nodes within skew. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Add-on compatibility; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl version` plus recent events/changes, then correlate the service-specific SLI. CNI/CSI/CoreDNS/proxy/metrics/admission/operator versions need matrices. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MP-06

- [ ] **Question:** Production is degraded around Canary node pool; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /version` plus recent events/changes, then correlate the service-specific SLI. validates image/runtime/kernel/driver/workload before fleet drain. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Drain/PDB; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /metrics | rg apiserver_requested_deprecated_apis` plus recent events/changes, then correlate the service-specific SLI. maintenance success depends on budgets, state/storage and graceful termination. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MP-08

- [ ] **Question:** Production is degraded around CRD conversion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get crd -o json | jq '.items[] | {name:.metadata.name,storedVersions:.status.storedVersions}'` plus recent events/changes, then correlate the service-specific SLI. webhook and stored-version correctness must precede removing versions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Rollback; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl version` plus recent events/changes, then correlate the service-specific SLI. control-plane downgrade is often unavailable, so backups/blue-green cluster migration matter. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-MP-10

- [ ] **Question:** Production is degraded around Qualification; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw /version` plus recent events/changes, then correlate the service-specific SLI. conformance plus real workload/SLO/security/DR validates more than node Ready. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SN-01

- [ ] **Question:** Design a production Kubernetes upgrades and API deprecations capability where Version skew, Control-plane first and Drain/PDB are first-class requirements.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. managed/self-managed procedures normally upgrade API before nodes within skew. maintenance success depends on budgets, state/storage and graceful termination. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes upgrades and API deprecations capability where API deprecation, Add-on compatibility and CRD conversion are first-class requirements.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: served versions are removed on schedule and manifests/clients/controllers must migrate. CNI/CSI/CoreDNS/proxy/metrics/admission/operator versions need matrices. webhook and stored-version correctness must precede removing versions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SN-03

- [ ] **Question:** Design a production Kubernetes upgrades and API deprecations capability where Storage version, Canary node pool and Rollback are first-class requirements.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: existing objects may remain encoded in old version until storage migration/update. validates image/runtime/kernel/driver/workload before fleet drain. control-plane downgrade is often unavailable, so backups/blue-green cluster migration matter. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes upgrades and API deprecations capability where Control-plane first, Drain/PDB and Qualification are first-class requirements.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed/self-managed procedures normally upgrade API before nodes within skew. maintenance success depends on budgets, state/storage and graceful termination. conformance plus real workload/SLO/security/DR validates more than node Ready. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SN-05

- [ ] **Question:** Design a production Kubernetes upgrades and API deprecations capability where Add-on compatibility, CRD conversion and Version skew are first-class requirements.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: CNI/CSI/CoreDNS/proxy/metrics/admission/operator versions need matrices. webhook and stored-version correctness must precede removing versions. supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes upgrades and API deprecations capability where Canary node pool, Rollback and API deprecation are first-class requirements.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: validates image/runtime/kernel/driver/workload before fleet drain. control-plane downgrade is often unavailable, so backups/blue-green cluster migration matter. served versions are removed on schedule and manifests/clients/controllers must migrate. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SN-07

- [ ] **Question:** Design a production Kubernetes upgrades and API deprecations capability where Drain/PDB, Qualification and Storage version are first-class requirements.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: maintenance success depends on budgets, state/storage and graceful termination. conformance plus real workload/SLO/security/DR validates more than node Ready. existing objects may remain encoded in old version until storage migration/update. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes upgrades and API deprecations capability where CRD conversion, Version skew and Control-plane first are first-class requirements.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: webhook and stored-version correctness must precede removing versions. supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. managed/self-managed procedures normally upgrade API before nodes within skew. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SN-09

- [ ] **Question:** Design a production Kubernetes upgrades and API deprecations capability where Rollback, API deprecation and Add-on compatibility are first-class requirements.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: control-plane downgrade is often unavailable, so backups/blue-green cluster migration matter. served versions are removed on schedule and manifests/clients/controllers must migrate. CNI/CSI/CoreDNS/proxy/metrics/admission/operator versions need matrices. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes upgrades and API deprecations capability where Qualification, Storage version and Canary node pool are first-class requirements.
> **Covered in:** [Kubernetes upgrades and API deprecations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: conformance plus real workload/SLO/security/DR validates more than node Ready. existing objects may remain encoded in old version until storage migration/update. validates image/runtime/kernel/driver/workload before fleet drain. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Version skew. How do you lead it end to end?
> **Covered in:** [Kubernetes upgrades and API deprecations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl version` as one read-only checkpoint, not the whole diagnosis. supported kubelet/kube-proxy/controller relationships bound rolling upgrade order. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving API deprecation. How do you lead it end to end?
> **Covered in:** [Kubernetes upgrades and API deprecations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /version` as one read-only checkpoint, not the whole diagnosis. served versions are removed on schedule and manifests/clients/controllers must migrate. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Storage version. How do you lead it end to end?
> **Covered in:** [Kubernetes upgrades and API deprecations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /metrics | rg apiserver_requested_deprecated_apis` as one read-only checkpoint, not the whole diagnosis. existing objects may remain encoded in old version until storage migration/update. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control-plane first. How do you lead it end to end?
> **Covered in:** [Kubernetes upgrades and API deprecations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get crd -o json | jq '.items[] | {name:.metadata.name,storedVersions:.status.storedVersions}'` as one read-only checkpoint, not the whole diagnosis. managed/self-managed procedures normally upgrade API before nodes within skew. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Add-on compatibility. How do you lead it end to end?
> **Covered in:** [Kubernetes upgrades and API deprecations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl version` as one read-only checkpoint, not the whole diagnosis. CNI/CSI/CoreDNS/proxy/metrics/admission/operator versions need matrices. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Canary node pool. How do you lead it end to end?
> **Covered in:** [Kubernetes upgrades and API deprecations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /version` as one read-only checkpoint, not the whole diagnosis. validates image/runtime/kernel/driver/workload before fleet drain. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Drain/PDB. How do you lead it end to end?
> **Covered in:** [Kubernetes upgrades and API deprecations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /metrics | rg apiserver_requested_deprecated_apis` as one read-only checkpoint, not the whole diagnosis. maintenance success depends on budgets, state/storage and graceful termination. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CRD conversion. How do you lead it end to end?
> **Covered in:** [Kubernetes upgrades and API deprecations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get crd -o json | jq '.items[] | {name:.metadata.name,storedVersions:.status.storedVersions}'` as one read-only checkpoint, not the whole diagnosis. webhook and stored-version correctness must precede removing versions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rollback. How do you lead it end to end?
> **Covered in:** [Kubernetes upgrades and API deprecations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl version` as one read-only checkpoint, not the whole diagnosis. control-plane downgrade is often unavailable, so backups/blue-green cluster migration matter. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-UPGRADES-AND-API-DEPRECATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Qualification. How do you lead it end to end?
> **Covered in:** [Kubernetes upgrades and API deprecations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw /version` as one read-only checkpoint, not the whole diagnosis. conformance plus real workload/SLO/security/DR validates more than node Ready. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Kubernetes observability](../01-observability/README.md) · [Study note](README.md) · [Next: Kubernetes backup and disaster recovery →](../03-backup-dr-etcd/README.md)

<!-- reading-navigation:end -->
