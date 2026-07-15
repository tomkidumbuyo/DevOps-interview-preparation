# Data versioning, quality and lineage — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JN-01

- [ ] **Question:** What is Logical dataset version, and why does it matter in Data versioning, quality and lineage?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** immutable manifest identifies source snapshot/partitions/files and schema rather than relying on a mutable path. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JN-02

- [ ] **Question:** What is Content digest, and why does it matter in Data versioning, quality and lineage?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** hashes prove byte identity but require canonical manifests and cannot prove authorization or semantic quality. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JN-03

- [ ] **Question:** What is Schema contract, and why does it matter in Data versioning, quality and lineage?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** names/types/nullability/ranges/keys and evolution compatibility fail early before expensive training. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JN-04

- [ ] **Question:** What is Statistical validation, and why does it matter in Data versioning, quality and lineage?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** distribution, missingness, duplicates, label balance and leakage tests compare against owned baselines. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JN-05

- [ ] **Question:** What is Point-in-time correctness, and why does it matter in Data versioning, quality and lineage?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** feature joins must use only information available at prediction time to prevent future leakage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JN-06

- [ ] **Question:** What is Lineage graph, and why does it matter in Data versioning, quality and lineage?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** source→transform code/config→dataset→run→model→release supports impact and deletion analysis. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JN-07

- [ ] **Question:** What is Sensitive data, and why does it matter in Data versioning, quality and lineage?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** classification, purpose, consent, residency, minimization and access policy follow derived datasets. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JN-08

- [ ] **Code:** **Question:** What does `python scripts/verify_dataset_manifest.py data/manifest.json` help you verify for Data versioning, quality and lineage?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: source deletion must reconcile caches, snapshots, embeddings, indexes and retained models under policy.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JN-09

- [ ] **Code:** **Question:** What does `dvc status; dvc dag; dvc repro` help you verify for Data versioning, quality and lineage?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: changed production input is a signal for investigation/evaluation, not automatic proof that retraining helps.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JN-10

- [ ] **Code:** **Question:** What does `dvc data status --json` help you verify for Data versioning, quality and lineage?
> **Covered in:** [Data versioning, quality and lineage — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: versioned entity/time-aware train/validation/test assignment avoids overlap and evaluation contamination.

## Junior — procedural and command questions

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JP-01

- [ ] **Code:** **Question:** A basic Logical dataset version check fails. What would you do first using the CLI?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dvc status; dvc dag; dvc repro` and capture exact status/reason/request ID. immutable manifest identifies source snapshot/partitions/files and schema rather than relying on a mutable path. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JP-02

- [ ] **Question:** A basic Content digest check fails. What would you do first?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dvc data status --json` and capture exact status/reason/request ID. hashes prove byte identity but require canonical manifests and cannot prove authorization or semantic quality. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JP-03

- [ ] **Question:** A basic Schema contract check fails. What would you do first?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `great_expectations checkpoint run CHECKPOINT` and capture exact status/reason/request ID. names/types/nullability/ranges/keys and evolution compatibility fail early before expensive training. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JP-04

- [ ] **Code:** **Question:** A basic Statistical validation check fails. What would you do first using the CLI?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/verify_dataset_manifest.py data/manifest.json` and capture exact status/reason/request ID. distribution, missingness, duplicates, label balance and leakage tests compare against owned baselines. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JP-05

- [ ] **Question:** A basic Point-in-time correctness check fails. What would you do first?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dvc status; dvc dag; dvc repro` and capture exact status/reason/request ID. feature joins must use only information available at prediction time to prevent future leakage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JP-06

- [ ] **Question:** A basic Lineage graph check fails. What would you do first?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dvc data status --json` and capture exact status/reason/request ID. source→transform code/config→dataset→run→model→release supports impact and deletion analysis. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JP-07

- [ ] **Code:** **Question:** A basic Sensitive data check fails. What would you do first using the CLI?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `great_expectations checkpoint run CHECKPOINT` and capture exact status/reason/request ID. classification, purpose, consent, residency, minimization and access policy follow derived datasets. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JP-08

- [ ] **Question:** A basic Deletion propagation check fails. What would you do first?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/verify_dataset_manifest.py data/manifest.json` and capture exact status/reason/request ID. source deletion must reconcile caches, snapshots, embeddings, indexes and retained models under policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JP-09

- [ ] **Question:** A basic Data drift check fails. What would you do first?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dvc status; dvc dag; dvc repro` and capture exact status/reason/request ID. changed production input is a signal for investigation/evaluation, not automatic proof that retraining helps. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-JP-10

- [ ] **Code:** **Question:** A basic Reproducible split check fails. What would you do first using the CLI?
> **Covered in:** [Data versioning, quality and lineage — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dvc data status --json` and capture exact status/reason/request ID. versioned entity/time-aware train/validation/test assignment avoids overlap and evaluation contamination. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MN-01

- [ ] **Question:** Compare Logical dataset version with Content digest. When would each change your design?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Logical dataset version: immutable manifest identifies source snapshot/partitions/files and schema rather than relying on a mutable path. Content digest: hashes prove byte identity but require canonical manifests and cannot prove authorization or semantic quality. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MN-02

- [ ] **Question:** Compare Content digest with Schema contract. When would each change your design?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Content digest: hashes prove byte identity but require canonical manifests and cannot prove authorization or semantic quality. Schema contract: names/types/nullability/ranges/keys and evolution compatibility fail early before expensive training. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MN-03

- [ ] **Question:** Compare Schema contract with Statistical validation. When would each change your design?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Schema contract: names/types/nullability/ranges/keys and evolution compatibility fail early before expensive training. Statistical validation: distribution, missingness, duplicates, label balance and leakage tests compare against owned baselines. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MN-04

- [ ] **Configuration review:** **Question:** Compare Statistical validation with Point-in-time correctness. When would each change your design?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Statistical validation: distribution, missingness, duplicates, label balance and leakage tests compare against owned baselines. Point-in-time correctness: feature joins must use only information available at prediction time to prevent future leakage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MN-05

- [ ] **Question:** Compare Point-in-time correctness with Lineage graph. When would each change your design?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Point-in-time correctness: feature joins must use only information available at prediction time to prevent future leakage. Lineage graph: source→transform code/config→dataset→run→model→release supports impact and deletion analysis. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MN-06

- [ ] **Question:** Compare Lineage graph with Sensitive data. When would each change your design?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Lineage graph: source→transform code/config→dataset→run→model→release supports impact and deletion analysis. Sensitive data: classification, purpose, consent, residency, minimization and access policy follow derived datasets. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MN-07

- [ ] **Configuration review:** **Question:** Compare Sensitive data with Deletion propagation. When would each change your design?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Sensitive data: classification, purpose, consent, residency, minimization and access policy follow derived datasets. Deletion propagation: source deletion must reconcile caches, snapshots, embeddings, indexes and retained models under policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MN-08

- [ ] **Question:** Compare Deletion propagation with Data drift. When would each change your design?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Deletion propagation: source deletion must reconcile caches, snapshots, embeddings, indexes and retained models under policy. Data drift: changed production input is a signal for investigation/evaluation, not automatic proof that retraining helps. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MN-09

- [ ] **Question:** Compare Data drift with Reproducible split. When would each change your design?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Data drift: changed production input is a signal for investigation/evaluation, not automatic proof that retraining helps. Reproducible split: versioned entity/time-aware train/validation/test assignment avoids overlap and evaluation contamination. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MN-10

- [ ] **Configuration review:** **Question:** Compare Reproducible split with Logical dataset version. When would each change your design?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Reproducible split: versioned entity/time-aware train/validation/test assignment avoids overlap and evaluation contamination. Logical dataset version: immutable manifest identifies source snapshot/partitions/files and schema rather than relying on a mutable path. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Logical dataset version; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dvc status; dvc dag; dvc repro` plus recent events/changes, then correlate the service-specific SLI. immutable manifest identifies source snapshot/partitions/files and schema rather than relying on a mutable path. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MP-02

- [ ] **Question:** Production is degraded around Content digest; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dvc data status --json` plus recent events/changes, then correlate the service-specific SLI. hashes prove byte identity but require canonical manifests and cannot prove authorization or semantic quality. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Schema contract; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `great_expectations checkpoint run CHECKPOINT` plus recent events/changes, then correlate the service-specific SLI. names/types/nullability/ranges/keys and evolution compatibility fail early before expensive training. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MP-04

- [ ] **Question:** Production is degraded around Statistical validation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/verify_dataset_manifest.py data/manifest.json` plus recent events/changes, then correlate the service-specific SLI. distribution, missingness, duplicates, label balance and leakage tests compare against owned baselines. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Point-in-time correctness; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dvc status; dvc dag; dvc repro` plus recent events/changes, then correlate the service-specific SLI. feature joins must use only information available at prediction time to prevent future leakage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MP-06

- [ ] **Question:** Production is degraded around Lineage graph; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dvc data status --json` plus recent events/changes, then correlate the service-specific SLI. source→transform code/config→dataset→run→model→release supports impact and deletion analysis. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Sensitive data; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `great_expectations checkpoint run CHECKPOINT` plus recent events/changes, then correlate the service-specific SLI. classification, purpose, consent, residency, minimization and access policy follow derived datasets. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MP-08

- [ ] **Question:** Production is degraded around Deletion propagation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/verify_dataset_manifest.py data/manifest.json` plus recent events/changes, then correlate the service-specific SLI. source deletion must reconcile caches, snapshots, embeddings, indexes and retained models under policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Data drift; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dvc status; dvc dag; dvc repro` plus recent events/changes, then correlate the service-specific SLI. changed production input is a signal for investigation/evaluation, not automatic proof that retraining helps. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-MP-10

- [ ] **Question:** Production is degraded around Reproducible split; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dvc data status --json` plus recent events/changes, then correlate the service-specific SLI. versioned entity/time-aware train/validation/test assignment avoids overlap and evaluation contamination. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SN-01

- [ ] **Question:** Design a production Data versioning, quality and lineage capability where Logical dataset version, Statistical validation and Sensitive data are first-class requirements.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable manifest identifies source snapshot/partitions/files and schema rather than relying on a mutable path. distribution, missingness, duplicates, label balance and leakage tests compare against owned baselines. classification, purpose, consent, residency, minimization and access policy follow derived datasets. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Data versioning, quality and lineage capability where Content digest, Point-in-time correctness and Deletion propagation are first-class requirements.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: hashes prove byte identity but require canonical manifests and cannot prove authorization or semantic quality. feature joins must use only information available at prediction time to prevent future leakage. source deletion must reconcile caches, snapshots, embeddings, indexes and retained models under policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SN-03

- [ ] **Question:** Design a production Data versioning, quality and lineage capability where Schema contract, Lineage graph and Data drift are first-class requirements.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: names/types/nullability/ranges/keys and evolution compatibility fail early before expensive training. source→transform code/config→dataset→run→model→release supports impact and deletion analysis. changed production input is a signal for investigation/evaluation, not automatic proof that retraining helps. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Data versioning, quality and lineage capability where Statistical validation, Sensitive data and Reproducible split are first-class requirements.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: distribution, missingness, duplicates, label balance and leakage tests compare against owned baselines. classification, purpose, consent, residency, minimization and access policy follow derived datasets. versioned entity/time-aware train/validation/test assignment avoids overlap and evaluation contamination. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SN-05

- [ ] **Question:** Design a production Data versioning, quality and lineage capability where Point-in-time correctness, Deletion propagation and Logical dataset version are first-class requirements.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: feature joins must use only information available at prediction time to prevent future leakage. source deletion must reconcile caches, snapshots, embeddings, indexes and retained models under policy. immutable manifest identifies source snapshot/partitions/files and schema rather than relying on a mutable path. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Data versioning, quality and lineage capability where Lineage graph, Data drift and Content digest are first-class requirements.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: source→transform code/config→dataset→run→model→release supports impact and deletion analysis. changed production input is a signal for investigation/evaluation, not automatic proof that retraining helps. hashes prove byte identity but require canonical manifests and cannot prove authorization or semantic quality. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SN-07

- [ ] **Question:** Design a production Data versioning, quality and lineage capability where Sensitive data, Reproducible split and Schema contract are first-class requirements.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: classification, purpose, consent, residency, minimization and access policy follow derived datasets. versioned entity/time-aware train/validation/test assignment avoids overlap and evaluation contamination. names/types/nullability/ranges/keys and evolution compatibility fail early before expensive training. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Data versioning, quality and lineage capability where Deletion propagation, Logical dataset version and Statistical validation are first-class requirements.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: source deletion must reconcile caches, snapshots, embeddings, indexes and retained models under policy. immutable manifest identifies source snapshot/partitions/files and schema rather than relying on a mutable path. distribution, missingness, duplicates, label balance and leakage tests compare against owned baselines. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SN-09

- [ ] **Question:** Design a production Data versioning, quality and lineage capability where Data drift, Content digest and Point-in-time correctness are first-class requirements.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: changed production input is a signal for investigation/evaluation, not automatic proof that retraining helps. hashes prove byte identity but require canonical manifests and cannot prove authorization or semantic quality. feature joins must use only information available at prediction time to prevent future leakage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Data versioning, quality and lineage capability where Reproducible split, Schema contract and Lineage graph are first-class requirements.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versioned entity/time-aware train/validation/test assignment avoids overlap and evaluation contamination. names/types/nullability/ranges/keys and evolution compatibility fail early before expensive training. source→transform code/config→dataset→run→model→release supports impact and deletion analysis. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Logical dataset version. How do you lead it end to end?
> **Covered in:** [Data versioning, quality and lineage — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dvc status; dvc dag; dvc repro` as one read-only checkpoint, not the whole diagnosis. immutable manifest identifies source snapshot/partitions/files and schema rather than relying on a mutable path. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Content digest. How do you lead it end to end?
> **Covered in:** [Data versioning, quality and lineage — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dvc data status --json` as one read-only checkpoint, not the whole diagnosis. hashes prove byte identity but require canonical manifests and cannot prove authorization or semantic quality. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Schema contract. How do you lead it end to end?
> **Covered in:** [Data versioning, quality and lineage — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `great_expectations checkpoint run CHECKPOINT` as one read-only checkpoint, not the whole diagnosis. names/types/nullability/ranges/keys and evolution compatibility fail early before expensive training. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Statistical validation. How do you lead it end to end?
> **Covered in:** [Data versioning, quality and lineage — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/verify_dataset_manifest.py data/manifest.json` as one read-only checkpoint, not the whole diagnosis. distribution, missingness, duplicates, label balance and leakage tests compare against owned baselines. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Point-in-time correctness. How do you lead it end to end?
> **Covered in:** [Data versioning, quality and lineage — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dvc status; dvc dag; dvc repro` as one read-only checkpoint, not the whole diagnosis. feature joins must use only information available at prediction time to prevent future leakage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lineage graph. How do you lead it end to end?
> **Covered in:** [Data versioning, quality and lineage — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dvc data status --json` as one read-only checkpoint, not the whole diagnosis. source→transform code/config→dataset→run→model→release supports impact and deletion analysis. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Sensitive data. How do you lead it end to end?
> **Covered in:** [Data versioning, quality and lineage — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `great_expectations checkpoint run CHECKPOINT` as one read-only checkpoint, not the whole diagnosis. classification, purpose, consent, residency, minimization and access policy follow derived datasets. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deletion propagation. How do you lead it end to end?
> **Covered in:** [Data versioning, quality and lineage — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/verify_dataset_manifest.py data/manifest.json` as one read-only checkpoint, not the whole diagnosis. source deletion must reconcile caches, snapshots, embeddings, indexes and retained models under policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Data drift. How do you lead it end to end?
> **Covered in:** [Data versioning, quality and lineage — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dvc status; dvc dag; dvc repro` as one read-only checkpoint, not the whole diagnosis. changed production input is a signal for investigation/evaluation, not automatic proof that retraining helps. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-VERSIONING-QUALITY-AND-LINEAGE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reproducible split. How do you lead it end to end?
> **Covered in:** [Data versioning, quality and lineage — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dvc data status --json` as one read-only checkpoint, not the whole diagnosis. versioned entity/time-aware train/validation/test assignment avoids overlap and evaluation contamination. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Experiment tracking and comparison](../02-experiment-tracking/README.md) · [Study note](README.md) · [Next: Feature stores and training-serving consistency →](../04-feature-store-training-serving/README.md)

<!-- reading-navigation:end -->
