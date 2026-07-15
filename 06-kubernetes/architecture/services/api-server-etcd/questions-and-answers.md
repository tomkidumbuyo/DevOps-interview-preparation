# Kubernetes API server and etcd — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KUBERNETES-API-SERVER-AND-ETCD-JN-01

- [ ] **Question:** What is API groups/versions, and why does it matter in Kubernetes API server and etcd?

**Answer:** resource kinds evolve through served/storage versions and conversion. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-API-SERVER-AND-ETCD-JN-02

- [ ] **Question:** What is Request path, and why does it matter in Kubernetes API server and etcd?

**Answer:** authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-API-SERVER-AND-ETCD-JN-03

- [ ] **Question:** What is Watch, and why does it matter in Kubernetes API server and etcd?

**Answer:** streams resource changes from a revision and powers controllers efficiently. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-API-SERVER-AND-ETCD-JN-04

- [ ] **Question:** What is ResourceVersion, and why does it matter in Kubernetes API server and etcd?

**Answer:** identifies observed revisions for concurrency/watch rather than a user timestamp. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-API-SERVER-AND-ETCD-JN-05

- [ ] **Question:** What is Server-side apply, and why does it matter in Kubernetes API server and etcd?

**Answer:** merges declarative fields by field manager and reports ownership conflicts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-API-SERVER-AND-ETCD-JN-06

- [ ] **Question:** What is etcd quorum, and why does it matter in Kubernetes API server and etcd?

**Answer:** majority of voting members is required for writes and consistent operation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-API-SERVER-AND-ETCD-JN-07

- [ ] **Question:** What is Compaction, and why does it matter in Kubernetes API server and etcd?

**Answer:** removes old MVCC revisions so watches must restart when too old. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-API-SERVER-AND-ETCD-JN-08

- [ ] **Code:** **Question:** What does `ETCDCTL_API=3 etcdctl endpoint status --cluster -w table` help you verify for Kubernetes API server and etcd?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: reclaims backend file space after compaction under operational care.

### KUBERNETES-API-SERVER-AND-ETCD-JN-09

- [ ] **Code:** **Question:** What does `kubectl get --raw '/readyz?verbose'` help you verify for Kubernetes API server and etcd?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: protects selected API resource values with key/provider lifecycle.

### KUBERNETES-API-SERVER-AND-ETCD-JN-10

- [ ] **Code:** **Question:** What does `kubectl get --raw '/metrics' | rg 'apiserver|etcd'` help you verify for Kubernetes API server and etcd?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: queues/shares requests to protect critical flows from noisy clients.

## Junior — procedural and command questions

### KUBERNETES-API-SERVER-AND-ETCD-JP-01

- [ ] **Code:** **Question:** A basic API groups/versions check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/readyz?verbose'` and capture exact status/reason/request ID. resource kinds evolve through served/storage versions and conversion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-API-SERVER-AND-ETCD-JP-02

- [ ] **Question:** A basic Request path check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/metrics' | rg 'apiserver|etcd'` and capture exact status/reason/request ID. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-API-SERVER-AND-ETCD-JP-03

- [ ] **Question:** A basic Watch check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl api-resources` and capture exact status/reason/request ID. streams resource changes from a revision and powers controllers efficiently. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-API-SERVER-AND-ETCD-JP-04

- [ ] **Code:** **Question:** A basic ResourceVersion check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ETCDCTL_API=3 etcdctl endpoint status --cluster -w table` and capture exact status/reason/request ID. identifies observed revisions for concurrency/watch rather than a user timestamp. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-API-SERVER-AND-ETCD-JP-05

- [ ] **Question:** A basic Server-side apply check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/readyz?verbose'` and capture exact status/reason/request ID. merges declarative fields by field manager and reports ownership conflicts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-API-SERVER-AND-ETCD-JP-06

- [ ] **Question:** A basic etcd quorum check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/metrics' | rg 'apiserver|etcd'` and capture exact status/reason/request ID. majority of voting members is required for writes and consistent operation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-API-SERVER-AND-ETCD-JP-07

- [ ] **Code:** **Question:** A basic Compaction check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl api-resources` and capture exact status/reason/request ID. removes old MVCC revisions so watches must restart when too old. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-API-SERVER-AND-ETCD-JP-08

- [ ] **Question:** A basic Defragmentation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ETCDCTL_API=3 etcdctl endpoint status --cluster -w table` and capture exact status/reason/request ID. reclaims backend file space after compaction under operational care. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-API-SERVER-AND-ETCD-JP-09

- [ ] **Question:** A basic Encryption at rest check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/readyz?verbose'` and capture exact status/reason/request ID. protects selected API resource values with key/provider lifecycle. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-API-SERVER-AND-ETCD-JP-10

- [ ] **Code:** **Question:** A basic API priority/fairness check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/metrics' | rg 'apiserver|etcd'` and capture exact status/reason/request ID. queues/shares requests to protect critical flows from noisy clients. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KUBERNETES-API-SERVER-AND-ETCD-MN-01

- [ ] **Question:** Compare API groups/versions with Request path. When would each change your design?

**Answer:** API groups/versions: resource kinds evolve through served/storage versions and conversion. Request path: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-API-SERVER-AND-ETCD-MN-02

- [ ] **Question:** Compare Request path with Watch. When would each change your design?

**Answer:** Request path: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Watch: streams resource changes from a revision and powers controllers efficiently. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-API-SERVER-AND-ETCD-MN-03

- [ ] **Question:** Compare Watch with ResourceVersion. When would each change your design?

**Answer:** Watch: streams resource changes from a revision and powers controllers efficiently. ResourceVersion: identifies observed revisions for concurrency/watch rather than a user timestamp. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-API-SERVER-AND-ETCD-MN-04

- [ ] **Configuration review:** **Question:** Compare ResourceVersion with Server-side apply. When would each change your design?

**Answer:** ResourceVersion: identifies observed revisions for concurrency/watch rather than a user timestamp. Server-side apply: merges declarative fields by field manager and reports ownership conflicts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-API-SERVER-AND-ETCD-MN-05

- [ ] **Question:** Compare Server-side apply with etcd quorum. When would each change your design?

**Answer:** Server-side apply: merges declarative fields by field manager and reports ownership conflicts. etcd quorum: majority of voting members is required for writes and consistent operation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-API-SERVER-AND-ETCD-MN-06

- [ ] **Question:** Compare etcd quorum with Compaction. When would each change your design?

**Answer:** etcd quorum: majority of voting members is required for writes and consistent operation. Compaction: removes old MVCC revisions so watches must restart when too old. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-API-SERVER-AND-ETCD-MN-07

- [ ] **Configuration review:** **Question:** Compare Compaction with Defragmentation. When would each change your design?

**Answer:** Compaction: removes old MVCC revisions so watches must restart when too old. Defragmentation: reclaims backend file space after compaction under operational care. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-API-SERVER-AND-ETCD-MN-08

- [ ] **Question:** Compare Defragmentation with Encryption at rest. When would each change your design?

**Answer:** Defragmentation: reclaims backend file space after compaction under operational care. Encryption at rest: protects selected API resource values with key/provider lifecycle. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-API-SERVER-AND-ETCD-MN-09

- [ ] **Question:** Compare Encryption at rest with API priority/fairness. When would each change your design?

**Answer:** Encryption at rest: protects selected API resource values with key/provider lifecycle. API priority/fairness: queues/shares requests to protect critical flows from noisy clients. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-API-SERVER-AND-ETCD-MN-10

- [ ] **Configuration review:** **Question:** Compare API priority/fairness with API groups/versions. When would each change your design?

**Answer:** API priority/fairness: queues/shares requests to protect critical flows from noisy clients. API groups/versions: resource kinds evolve through served/storage versions and conversion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KUBERNETES-API-SERVER-AND-ETCD-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around API groups/versions; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/readyz?verbose'` plus recent events/changes, then correlate the service-specific SLI. resource kinds evolve through served/storage versions and conversion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-API-SERVER-AND-ETCD-MP-02

- [ ] **Question:** Production is degraded around Request path; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/metrics' | rg 'apiserver|etcd'` plus recent events/changes, then correlate the service-specific SLI. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-API-SERVER-AND-ETCD-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Watch; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl api-resources` plus recent events/changes, then correlate the service-specific SLI. streams resource changes from a revision and powers controllers efficiently. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-API-SERVER-AND-ETCD-MP-04

- [ ] **Question:** Production is degraded around ResourceVersion; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ETCDCTL_API=3 etcdctl endpoint status --cluster -w table` plus recent events/changes, then correlate the service-specific SLI. identifies observed revisions for concurrency/watch rather than a user timestamp. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-API-SERVER-AND-ETCD-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Server-side apply; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/readyz?verbose'` plus recent events/changes, then correlate the service-specific SLI. merges declarative fields by field manager and reports ownership conflicts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-API-SERVER-AND-ETCD-MP-06

- [ ] **Question:** Production is degraded around etcd quorum; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/metrics' | rg 'apiserver|etcd'` plus recent events/changes, then correlate the service-specific SLI. majority of voting members is required for writes and consistent operation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-API-SERVER-AND-ETCD-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Compaction; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl api-resources` plus recent events/changes, then correlate the service-specific SLI. removes old MVCC revisions so watches must restart when too old. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-API-SERVER-AND-ETCD-MP-08

- [ ] **Question:** Production is degraded around Defragmentation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ETCDCTL_API=3 etcdctl endpoint status --cluster -w table` plus recent events/changes, then correlate the service-specific SLI. reclaims backend file space after compaction under operational care. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-API-SERVER-AND-ETCD-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Encryption at rest; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/readyz?verbose'` plus recent events/changes, then correlate the service-specific SLI. protects selected API resource values with key/provider lifecycle. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-API-SERVER-AND-ETCD-MP-10

- [ ] **Question:** Production is degraded around API priority/fairness; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/metrics' | rg 'apiserver|etcd'` plus recent events/changes, then correlate the service-specific SLI. queues/shares requests to protect critical flows from noisy clients. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KUBERNETES-API-SERVER-AND-ETCD-SN-01

- [ ] **Question:** Design a production Kubernetes API server and etcd capability where API groups/versions, ResourceVersion and Compaction are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: resource kinds evolve through served/storage versions and conversion. identifies observed revisions for concurrency/watch rather than a user timestamp. removes old MVCC revisions so watches must restart when too old. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-API-SERVER-AND-ETCD-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes API server and etcd capability where Request path, Server-side apply and Defragmentation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. merges declarative fields by field manager and reports ownership conflicts. reclaims backend file space after compaction under operational care. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-API-SERVER-AND-ETCD-SN-03

- [ ] **Question:** Design a production Kubernetes API server and etcd capability where Watch, etcd quorum and Encryption at rest are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: streams resource changes from a revision and powers controllers efficiently. majority of voting members is required for writes and consistent operation. protects selected API resource values with key/provider lifecycle. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-API-SERVER-AND-ETCD-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes API server and etcd capability where ResourceVersion, Compaction and API priority/fairness are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: identifies observed revisions for concurrency/watch rather than a user timestamp. removes old MVCC revisions so watches must restart when too old. queues/shares requests to protect critical flows from noisy clients. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-API-SERVER-AND-ETCD-SN-05

- [ ] **Question:** Design a production Kubernetes API server and etcd capability where Server-side apply, Defragmentation and API groups/versions are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: merges declarative fields by field manager and reports ownership conflicts. reclaims backend file space after compaction under operational care. resource kinds evolve through served/storage versions and conversion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-API-SERVER-AND-ETCD-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes API server and etcd capability where etcd quorum, Encryption at rest and Request path are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: majority of voting members is required for writes and consistent operation. protects selected API resource values with key/provider lifecycle. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-API-SERVER-AND-ETCD-SN-07

- [ ] **Question:** Design a production Kubernetes API server and etcd capability where Compaction, API priority/fairness and Watch are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: removes old MVCC revisions so watches must restart when too old. queues/shares requests to protect critical flows from noisy clients. streams resource changes from a revision and powers controllers efficiently. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-API-SERVER-AND-ETCD-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes API server and etcd capability where Defragmentation, API groups/versions and ResourceVersion are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reclaims backend file space after compaction under operational care. resource kinds evolve through served/storage versions and conversion. identifies observed revisions for concurrency/watch rather than a user timestamp. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-API-SERVER-AND-ETCD-SN-09

- [ ] **Question:** Design a production Kubernetes API server and etcd capability where Encryption at rest, Request path and Server-side apply are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: protects selected API resource values with key/provider lifecycle. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. merges declarative fields by field manager and reports ownership conflicts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-API-SERVER-AND-ETCD-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes API server and etcd capability where API priority/fairness, Watch and etcd quorum are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: queues/shares requests to protect critical flows from noisy clients. streams resource changes from a revision and powers controllers efficiently. majority of voting members is required for writes and consistent operation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KUBERNETES-API-SERVER-AND-ETCD-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving API groups/versions. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/readyz?verbose'` as one read-only checkpoint, not the whole diagnosis. resource kinds evolve through served/storage versions and conversion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-API-SERVER-AND-ETCD-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Request path. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/metrics' | rg 'apiserver|etcd'` as one read-only checkpoint, not the whole diagnosis. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-API-SERVER-AND-ETCD-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Watch. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl api-resources` as one read-only checkpoint, not the whole diagnosis. streams resource changes from a revision and powers controllers efficiently. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-API-SERVER-AND-ETCD-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ResourceVersion. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ETCDCTL_API=3 etcdctl endpoint status --cluster -w table` as one read-only checkpoint, not the whole diagnosis. identifies observed revisions for concurrency/watch rather than a user timestamp. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-API-SERVER-AND-ETCD-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Server-side apply. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/readyz?verbose'` as one read-only checkpoint, not the whole diagnosis. merges declarative fields by field manager and reports ownership conflicts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-API-SERVER-AND-ETCD-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving etcd quorum. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/metrics' | rg 'apiserver|etcd'` as one read-only checkpoint, not the whole diagnosis. majority of voting members is required for writes and consistent operation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-API-SERVER-AND-ETCD-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Compaction. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl api-resources` as one read-only checkpoint, not the whole diagnosis. removes old MVCC revisions so watches must restart when too old. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-API-SERVER-AND-ETCD-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Defragmentation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ETCDCTL_API=3 etcdctl endpoint status --cluster -w table` as one read-only checkpoint, not the whole diagnosis. reclaims backend file space after compaction under operational care. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-API-SERVER-AND-ETCD-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Encryption at rest. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/readyz?verbose'` as one read-only checkpoint, not the whole diagnosis. protects selected API resource values with key/provider lifecycle. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-API-SERVER-AND-ETCD-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving API priority/fairness. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/metrics' | rg 'apiserver|etcd'` as one read-only checkpoint, not the whole diagnosis. queues/shares requests to protect critical flows from noisy clients. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
