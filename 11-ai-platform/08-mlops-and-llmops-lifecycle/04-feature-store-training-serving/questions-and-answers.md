# Feature stores and training-serving consistency — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JN-01

- [ ] **Question:** What is Feature definition, and why does it matter in Feature stores and training-serving consistency?
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** owner, entity key, schema, source, transformation, freshness and documentation form a versioned contract. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JN-02

- [ ] **Question:** What is Offline store, and why does it matter in Feature stores and training-serving consistency?
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** historical values support point-in-time training datasets and batch retrieval. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JN-03

- [ ] **Question:** What is Online store, and why does it matter in Feature stores and training-serving consistency?
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** low-latency current values trade history and consistency for serving needs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JN-04

- [ ] **Question:** What is Registry, and why does it matter in Feature stores and training-serving consistency?
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** versioned metadata connects feature views, entities, sources and ownership but is not necessarily the data store. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JN-05

- [ ] **Question:** What is Materialization, and why does it matter in Feature stores and training-serving consistency?
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** loads computed feature values into online storage with retry, watermark and freshness evidence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JN-06

- [ ] **Question:** What is Point-in-time join, and why does it matter in Feature stores and training-serving consistency?
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** retrieves each entity's latest valid feature before the event timestamp to prevent leakage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JN-07

- [ ] **Question:** What is Training-serving skew, and why does it matter in Feature stores and training-serving consistency?
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** code/schema/default/freshness differences between training and inference change behavior. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JN-08

- [ ] **Code:** **Question:** What does `feast get-historical-features --help` help you verify for Feature stores and training-serving consistency?
> **Covered in:** [Feature stores and training-serving consistency — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: event/source/materialization/serve ages distinguish pipeline delay from missing values.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JN-09

- [ ] **Code:** **Question:** What does `feast apply` help you verify for Feature stores and training-serving consistency?
> **Covered in:** [Feature stores and training-serving consistency — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: sensitive feature values need entity/tenant authorization and purpose-aware audit.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JN-10

- [ ] **Code:** **Question:** What does `feast feature-views list` help you verify for Feature stores and training-serving consistency?
> **Covered in:** [Feature stores and training-serving consistency — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: historical recomputation needs immutable transformation versions, capacity control and comparison before promotion.

## Junior — procedural and command questions

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JP-01

- [ ] **Code:** **Question:** A basic Feature definition check fails. What would you do first using the CLI?
> **Covered in:** [Feature stores and training-serving consistency — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `feast apply` and capture exact status/reason/request ID. owner, entity key, schema, source, transformation, freshness and documentation form a versioned contract. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JP-02

- [ ] **Question:** A basic Offline store check fails. What would you do first?
> **Covered in:** [Feature stores and training-serving consistency — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `feast feature-views list` and capture exact status/reason/request ID. historical values support point-in-time training datasets and batch retrieval. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JP-03

- [ ] **Question:** A basic Online store check fails. What would you do first?
> **Covered in:** [Feature stores and training-serving consistency — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `feast materialize-incremental $(date -u +%Y-%m-%dT%H:%M:%S)` and capture exact status/reason/request ID. low-latency current values trade history and consistency for serving needs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JP-04

- [ ] **Code:** **Question:** A basic Registry check fails. What would you do first using the CLI?
> **Covered in:** [Feature stores and training-serving consistency — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `feast get-historical-features --help` and capture exact status/reason/request ID. versioned metadata connects feature views, entities, sources and ownership but is not necessarily the data store. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JP-05

- [ ] **Question:** A basic Materialization check fails. What would you do first?
> **Covered in:** [Feature stores and training-serving consistency — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `feast apply` and capture exact status/reason/request ID. loads computed feature values into online storage with retry, watermark and freshness evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JP-06

- [ ] **Question:** A basic Point-in-time join check fails. What would you do first?
> **Covered in:** [Feature stores and training-serving consistency — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `feast feature-views list` and capture exact status/reason/request ID. retrieves each entity's latest valid feature before the event timestamp to prevent leakage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JP-07

- [ ] **Code:** **Question:** A basic Training-serving skew check fails. What would you do first using the CLI?
> **Covered in:** [Feature stores and training-serving consistency — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `feast materialize-incremental $(date -u +%Y-%m-%dT%H:%M:%S)` and capture exact status/reason/request ID. code/schema/default/freshness differences between training and inference change behavior. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JP-08

- [ ] **Question:** A basic Freshness SLI check fails. What would you do first?
> **Covered in:** [Feature stores and training-serving consistency — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `feast get-historical-features --help` and capture exact status/reason/request ID. event/source/materialization/serve ages distinguish pipeline delay from missing values. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JP-09

- [ ] **Question:** A basic Access control check fails. What would you do first?
> **Covered in:** [Feature stores and training-serving consistency — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `feast apply` and capture exact status/reason/request ID. sensitive feature values need entity/tenant authorization and purpose-aware audit. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-JP-10

- [ ] **Code:** **Question:** A basic Backfill check fails. What would you do first using the CLI?
> **Covered in:** [Feature stores and training-serving consistency — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `feast feature-views list` and capture exact status/reason/request ID. historical recomputation needs immutable transformation versions, capacity control and comparison before promotion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MN-01

- [ ] **Question:** Compare Feature definition with Offline store. When would each change your design?
> **Covered in:** [Feature stores and training-serving consistency — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Feature definition: owner, entity key, schema, source, transformation, freshness and documentation form a versioned contract. Offline store: historical values support point-in-time training datasets and batch retrieval. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MN-02

- [ ] **Question:** Compare Offline store with Online store. When would each change your design?
> **Covered in:** [Feature stores and training-serving consistency — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Offline store: historical values support point-in-time training datasets and batch retrieval. Online store: low-latency current values trade history and consistency for serving needs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MN-03

- [ ] **Question:** Compare Online store with Registry. When would each change your design?
> **Covered in:** [Feature stores and training-serving consistency — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Online store: low-latency current values trade history and consistency for serving needs. Registry: versioned metadata connects feature views, entities, sources and ownership but is not necessarily the data store. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MN-04

- [ ] **Configuration review:** **Question:** Compare Registry with Materialization. When would each change your design?
> **Covered in:** [Feature stores and training-serving consistency — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Registry: versioned metadata connects feature views, entities, sources and ownership but is not necessarily the data store. Materialization: loads computed feature values into online storage with retry, watermark and freshness evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MN-05

- [ ] **Question:** Compare Materialization with Point-in-time join. When would each change your design?
> **Covered in:** [Feature stores and training-serving consistency — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Materialization: loads computed feature values into online storage with retry, watermark and freshness evidence. Point-in-time join: retrieves each entity's latest valid feature before the event timestamp to prevent leakage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MN-06

- [ ] **Question:** Compare Point-in-time join with Training-serving skew. When would each change your design?
> **Covered in:** [Feature stores and training-serving consistency — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Point-in-time join: retrieves each entity's latest valid feature before the event timestamp to prevent leakage. Training-serving skew: code/schema/default/freshness differences between training and inference change behavior. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MN-07

- [ ] **Configuration review:** **Question:** Compare Training-serving skew with Freshness SLI. When would each change your design?
> **Covered in:** [Feature stores and training-serving consistency — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Training-serving skew: code/schema/default/freshness differences between training and inference change behavior. Freshness SLI: event/source/materialization/serve ages distinguish pipeline delay from missing values. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MN-08

- [ ] **Question:** Compare Freshness SLI with Access control. When would each change your design?
> **Covered in:** [Feature stores and training-serving consistency — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Freshness SLI: event/source/materialization/serve ages distinguish pipeline delay from missing values. Access control: sensitive feature values need entity/tenant authorization and purpose-aware audit. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MN-09

- [ ] **Question:** Compare Access control with Backfill. When would each change your design?
> **Covered in:** [Feature stores and training-serving consistency — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Access control: sensitive feature values need entity/tenant authorization and purpose-aware audit. Backfill: historical recomputation needs immutable transformation versions, capacity control and comparison before promotion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MN-10

- [ ] **Configuration review:** **Question:** Compare Backfill with Feature definition. When would each change your design?
> **Covered in:** [Feature stores and training-serving consistency — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Backfill: historical recomputation needs immutable transformation versions, capacity control and comparison before promotion. Feature definition: owner, entity key, schema, source, transformation, freshness and documentation form a versioned contract. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Feature definition; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `feast apply` plus recent events/changes, then correlate the service-specific SLI. owner, entity key, schema, source, transformation, freshness and documentation form a versioned contract. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MP-02

- [ ] **Question:** Production is degraded around Offline store; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `feast feature-views list` plus recent events/changes, then correlate the service-specific SLI. historical values support point-in-time training datasets and batch retrieval. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Online store; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `feast materialize-incremental $(date -u +%Y-%m-%dT%H:%M:%S)` plus recent events/changes, then correlate the service-specific SLI. low-latency current values trade history and consistency for serving needs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MP-04

- [ ] **Question:** Production is degraded around Registry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `feast get-historical-features --help` plus recent events/changes, then correlate the service-specific SLI. versioned metadata connects feature views, entities, sources and ownership but is not necessarily the data store. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Materialization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `feast apply` plus recent events/changes, then correlate the service-specific SLI. loads computed feature values into online storage with retry, watermark and freshness evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MP-06

- [ ] **Question:** Production is degraded around Point-in-time join; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `feast feature-views list` plus recent events/changes, then correlate the service-specific SLI. retrieves each entity's latest valid feature before the event timestamp to prevent leakage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Training-serving skew; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `feast materialize-incremental $(date -u +%Y-%m-%dT%H:%M:%S)` plus recent events/changes, then correlate the service-specific SLI. code/schema/default/freshness differences between training and inference change behavior. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MP-08

- [ ] **Question:** Production is degraded around Freshness SLI; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `feast get-historical-features --help` plus recent events/changes, then correlate the service-specific SLI. event/source/materialization/serve ages distinguish pipeline delay from missing values. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Access control; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `feast apply` plus recent events/changes, then correlate the service-specific SLI. sensitive feature values need entity/tenant authorization and purpose-aware audit. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-MP-10

- [ ] **Question:** Production is degraded around Backfill; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `feast feature-views list` plus recent events/changes, then correlate the service-specific SLI. historical recomputation needs immutable transformation versions, capacity control and comparison before promotion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SN-01

- [ ] **Question:** Design a production Feature stores and training-serving consistency capability where Feature definition, Registry and Training-serving skew are first-class requirements.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: owner, entity key, schema, source, transformation, freshness and documentation form a versioned contract. versioned metadata connects feature views, entities, sources and ownership but is not necessarily the data store. code/schema/default/freshness differences between training and inference change behavior. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Feature stores and training-serving consistency capability where Offline store, Materialization and Freshness SLI are first-class requirements.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: historical values support point-in-time training datasets and batch retrieval. loads computed feature values into online storage with retry, watermark and freshness evidence. event/source/materialization/serve ages distinguish pipeline delay from missing values. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SN-03

- [ ] **Question:** Design a production Feature stores and training-serving consistency capability where Online store, Point-in-time join and Access control are first-class requirements.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: low-latency current values trade history and consistency for serving needs. retrieves each entity's latest valid feature before the event timestamp to prevent leakage. sensitive feature values need entity/tenant authorization and purpose-aware audit. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Feature stores and training-serving consistency capability where Registry, Training-serving skew and Backfill are first-class requirements.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versioned metadata connects feature views, entities, sources and ownership but is not necessarily the data store. code/schema/default/freshness differences between training and inference change behavior. historical recomputation needs immutable transformation versions, capacity control and comparison before promotion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SN-05

- [ ] **Question:** Design a production Feature stores and training-serving consistency capability where Materialization, Freshness SLI and Feature definition are first-class requirements.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: loads computed feature values into online storage with retry, watermark and freshness evidence. event/source/materialization/serve ages distinguish pipeline delay from missing values. owner, entity key, schema, source, transformation, freshness and documentation form a versioned contract. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Feature stores and training-serving consistency capability where Point-in-time join, Access control and Offline store are first-class requirements.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retrieves each entity's latest valid feature before the event timestamp to prevent leakage. sensitive feature values need entity/tenant authorization and purpose-aware audit. historical values support point-in-time training datasets and batch retrieval. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SN-07

- [ ] **Question:** Design a production Feature stores and training-serving consistency capability where Training-serving skew, Backfill and Online store are first-class requirements.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: code/schema/default/freshness differences between training and inference change behavior. historical recomputation needs immutable transformation versions, capacity control and comparison before promotion. low-latency current values trade history and consistency for serving needs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Feature stores and training-serving consistency capability where Freshness SLI, Feature definition and Registry are first-class requirements.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: event/source/materialization/serve ages distinguish pipeline delay from missing values. owner, entity key, schema, source, transformation, freshness and documentation form a versioned contract. versioned metadata connects feature views, entities, sources and ownership but is not necessarily the data store. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SN-09

- [ ] **Question:** Design a production Feature stores and training-serving consistency capability where Access control, Offline store and Materialization are first-class requirements.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: sensitive feature values need entity/tenant authorization and purpose-aware audit. historical values support point-in-time training datasets and batch retrieval. loads computed feature values into online storage with retry, watermark and freshness evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Feature stores and training-serving consistency capability where Backfill, Online store and Point-in-time join are first-class requirements.
> **Covered in:** [Feature stores and training-serving consistency — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: historical recomputation needs immutable transformation versions, capacity control and comparison before promotion. low-latency current values trade history and consistency for serving needs. retrieves each entity's latest valid feature before the event timestamp to prevent leakage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Feature definition. How do you lead it end to end?
> **Covered in:** [Feature stores and training-serving consistency — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `feast apply` as one read-only checkpoint, not the whole diagnosis. owner, entity key, schema, source, transformation, freshness and documentation form a versioned contract. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Offline store. How do you lead it end to end?
> **Covered in:** [Feature stores and training-serving consistency — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `feast feature-views list` as one read-only checkpoint, not the whole diagnosis. historical values support point-in-time training datasets and batch retrieval. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Online store. How do you lead it end to end?
> **Covered in:** [Feature stores and training-serving consistency — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `feast materialize-incremental $(date -u +%Y-%m-%dT%H:%M:%S)` as one read-only checkpoint, not the whole diagnosis. low-latency current values trade history and consistency for serving needs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Registry. How do you lead it end to end?
> **Covered in:** [Feature stores and training-serving consistency — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `feast get-historical-features --help` as one read-only checkpoint, not the whole diagnosis. versioned metadata connects feature views, entities, sources and ownership but is not necessarily the data store. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Materialization. How do you lead it end to end?
> **Covered in:** [Feature stores and training-serving consistency — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `feast apply` as one read-only checkpoint, not the whole diagnosis. loads computed feature values into online storage with retry, watermark and freshness evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Point-in-time join. How do you lead it end to end?
> **Covered in:** [Feature stores and training-serving consistency — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `feast feature-views list` as one read-only checkpoint, not the whole diagnosis. retrieves each entity's latest valid feature before the event timestamp to prevent leakage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Training-serving skew. How do you lead it end to end?
> **Covered in:** [Feature stores and training-serving consistency — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `feast materialize-incremental $(date -u +%Y-%m-%dT%H:%M:%S)` as one read-only checkpoint, not the whole diagnosis. code/schema/default/freshness differences between training and inference change behavior. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Freshness SLI. How do you lead it end to end?
> **Covered in:** [Feature stores and training-serving consistency — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `feast get-historical-features --help` as one read-only checkpoint, not the whole diagnosis. event/source/materialization/serve ages distinguish pipeline delay from missing values. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Access control. How do you lead it end to end?
> **Covered in:** [Feature stores and training-serving consistency — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `feast apply` as one read-only checkpoint, not the whole diagnosis. sensitive feature values need entity/tenant authorization and purpose-aware audit. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FEATURE-STORES-AND-TRAINING-SERVING-CONSISTENCY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backfill. How do you lead it end to end?
> **Covered in:** [Feature stores and training-serving consistency — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `feast feature-views list` as one read-only checkpoint, not the whole diagnosis. historical recomputation needs immutable transformation versions, capacity control and comparison before promotion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Data versioning, quality and lineage](../03-data-versioning-quality-lineage/README.md) · [Study note](README.md) · [Next: ML pipeline orchestration →](../05-pipeline-orchestration/README.md)

<!-- reading-navigation:end -->
