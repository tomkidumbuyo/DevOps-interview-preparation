# Jobs and CronJobs — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### JOBS-AND-CRONJOBS-JN-01

- [ ] **Question:** What is Completion, and why does it matter in Jobs and CronJobs?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Job succeeds after required successful Pods/completions under mode semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### JOBS-AND-CRONJOBS-JN-02

- [ ] **Question:** What is Parallelism, and why does it matter in Jobs and CronJobs?
> **Covered in:** [Jobs and CronJobs — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** number of Pods executing concurrently and downstream load. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### JOBS-AND-CRONJOBS-JN-03

- [ ] **Question:** What is Backoff limit, and why does it matter in Jobs and CronJobs?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** bounds Pod failures before Job fails but retries can repeat effects. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### JOBS-AND-CRONJOBS-JN-04

- [ ] **Question:** What is Active deadline, and why does it matter in Jobs and CronJobs?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** limits total Job runtime including retries. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### JOBS-AND-CRONJOBS-JN-05

- [ ] **Question:** What is Indexed Job, and why does it matter in Jobs and CronJobs?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** gives stable completion indexes for partitioned work. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### JOBS-AND-CRONJOBS-JN-06

- [ ] **Question:** What is Pod failure policy, and why does it matter in Jobs and CronJobs?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** classifies exit/status outcomes to fail/ignore/count under supported versions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### JOBS-AND-CRONJOBS-JN-07

- [ ] **Question:** What is TTL after finish, and why does it matter in Jobs and CronJobs?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** garbage-collects completed Jobs after evidence retention window. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### JOBS-AND-CRONJOBS-JN-08

- [ ] **Code:** **Question:** What does `kubectl logs -n NS job/NAME --all-containers` help you verify for Jobs and CronJobs?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: controller creates Jobs from wall-clock schedule with missed-run handling.

### JOBS-AND-CRONJOBS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get job,cronjob -A` help you verify for Jobs and CronJobs?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: Allow/Forbid/Replace controls overlap but application locks may still be needed.

### JOBS-AND-CRONJOBS-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe job NAME -n NS` help you verify for Jobs and CronJobs?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: skips or starts missed schedules within a tolerance window.

## Junior — procedural and command questions

### JOBS-AND-CRONJOBS-JP-01

- [ ] **Code:** **Question:** A basic Completion check fails. What would you do first using the CLI?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get job,cronjob -A` and capture exact status/reason/request ID. Job succeeds after required successful Pods/completions under mode semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### JOBS-AND-CRONJOBS-JP-02

- [ ] **Question:** A basic Parallelism check fails. What would you do first?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe job NAME -n NS` and capture exact status/reason/request ID. number of Pods executing concurrently and downstream load. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### JOBS-AND-CRONJOBS-JP-03

- [ ] **Question:** A basic Backoff limit check fails. What would you do first?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl create job --from=cronjob/NAME MANUAL -n NS` and capture exact status/reason/request ID. bounds Pod failures before Job fails but retries can repeat effects. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### JOBS-AND-CRONJOBS-JP-04

- [ ] **Code:** **Question:** A basic Active deadline check fails. What would you do first using the CLI?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n NS job/NAME --all-containers` and capture exact status/reason/request ID. limits total Job runtime including retries. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### JOBS-AND-CRONJOBS-JP-05

- [ ] **Question:** A basic Indexed Job check fails. What would you do first?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get job,cronjob -A` and capture exact status/reason/request ID. gives stable completion indexes for partitioned work. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### JOBS-AND-CRONJOBS-JP-06

- [ ] **Question:** A basic Pod failure policy check fails. What would you do first?
> **Covered in:** [Jobs and CronJobs — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe job NAME -n NS` and capture exact status/reason/request ID. classifies exit/status outcomes to fail/ignore/count under supported versions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### JOBS-AND-CRONJOBS-JP-07

- [ ] **Code:** **Question:** A basic TTL after finish check fails. What would you do first using the CLI?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl create job --from=cronjob/NAME MANUAL -n NS` and capture exact status/reason/request ID. garbage-collects completed Jobs after evidence retention window. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### JOBS-AND-CRONJOBS-JP-08

- [ ] **Question:** A basic Cron schedule/time zone check fails. What would you do first?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n NS job/NAME --all-containers` and capture exact status/reason/request ID. controller creates Jobs from wall-clock schedule with missed-run handling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### JOBS-AND-CRONJOBS-JP-09

- [ ] **Question:** A basic Concurrency policy check fails. What would you do first?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get job,cronjob -A` and capture exact status/reason/request ID. Allow/Forbid/Replace controls overlap but application locks may still be needed. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### JOBS-AND-CRONJOBS-JP-10

- [ ] **Code:** **Question:** A basic Starting deadline check fails. What would you do first using the CLI?
> **Covered in:** [Jobs and CronJobs — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe job NAME -n NS` and capture exact status/reason/request ID. skips or starts missed schedules within a tolerance window. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### JOBS-AND-CRONJOBS-MN-01

- [ ] **Question:** Compare Completion with Parallelism. When would each change your design?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Completion: Job succeeds after required successful Pods/completions under mode semantics. Parallelism: number of Pods executing concurrently and downstream load. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### JOBS-AND-CRONJOBS-MN-02

- [ ] **Question:** Compare Parallelism with Backoff limit. When would each change your design?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Parallelism: number of Pods executing concurrently and downstream load. Backoff limit: bounds Pod failures before Job fails but retries can repeat effects. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### JOBS-AND-CRONJOBS-MN-03

- [ ] **Question:** Compare Backoff limit with Active deadline. When would each change your design?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Backoff limit: bounds Pod failures before Job fails but retries can repeat effects. Active deadline: limits total Job runtime including retries. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### JOBS-AND-CRONJOBS-MN-04

- [ ] **Configuration review:** **Question:** Compare Active deadline with Indexed Job. When would each change your design?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Active deadline: limits total Job runtime including retries. Indexed Job: gives stable completion indexes for partitioned work. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### JOBS-AND-CRONJOBS-MN-05

- [ ] **Question:** Compare Indexed Job with Pod failure policy. When would each change your design?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Indexed Job: gives stable completion indexes for partitioned work. Pod failure policy: classifies exit/status outcomes to fail/ignore/count under supported versions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### JOBS-AND-CRONJOBS-MN-06

- [ ] **Question:** Compare Pod failure policy with TTL after finish. When would each change your design?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Pod failure policy: classifies exit/status outcomes to fail/ignore/count under supported versions. TTL after finish: garbage-collects completed Jobs after evidence retention window. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### JOBS-AND-CRONJOBS-MN-07

- [ ] **Configuration review:** **Question:** Compare TTL after finish with Cron schedule/time zone. When would each change your design?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** TTL after finish: garbage-collects completed Jobs after evidence retention window. Cron schedule/time zone: controller creates Jobs from wall-clock schedule with missed-run handling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### JOBS-AND-CRONJOBS-MN-08

- [ ] **Question:** Compare Cron schedule/time zone with Concurrency policy. When would each change your design?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Cron schedule/time zone: controller creates Jobs from wall-clock schedule with missed-run handling. Concurrency policy: Allow/Forbid/Replace controls overlap but application locks may still be needed. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### JOBS-AND-CRONJOBS-MN-09

- [ ] **Question:** Compare Concurrency policy with Starting deadline. When would each change your design?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Concurrency policy: Allow/Forbid/Replace controls overlap but application locks may still be needed. Starting deadline: skips or starts missed schedules within a tolerance window. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### JOBS-AND-CRONJOBS-MN-10

- [ ] **Configuration review:** **Question:** Compare Starting deadline with Completion. When would each change your design?
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Starting deadline: skips or starts missed schedules within a tolerance window. Completion: Job succeeds after required successful Pods/completions under mode semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### JOBS-AND-CRONJOBS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Completion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get job,cronjob -A` plus recent events/changes, then correlate the service-specific SLI. Job succeeds after required successful Pods/completions under mode semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### JOBS-AND-CRONJOBS-MP-02

- [ ] **Question:** Production is degraded around Parallelism; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe job NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. number of Pods executing concurrently and downstream load. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### JOBS-AND-CRONJOBS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Backoff limit; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl create job --from=cronjob/NAME MANUAL -n NS` plus recent events/changes, then correlate the service-specific SLI. bounds Pod failures before Job fails but retries can repeat effects. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### JOBS-AND-CRONJOBS-MP-04

- [ ] **Question:** Production is degraded around Active deadline; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n NS job/NAME --all-containers` plus recent events/changes, then correlate the service-specific SLI. limits total Job runtime including retries. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### JOBS-AND-CRONJOBS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Indexed Job; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get job,cronjob -A` plus recent events/changes, then correlate the service-specific SLI. gives stable completion indexes for partitioned work. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### JOBS-AND-CRONJOBS-MP-06

- [ ] **Question:** Production is degraded around Pod failure policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe job NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. classifies exit/status outcomes to fail/ignore/count under supported versions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### JOBS-AND-CRONJOBS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around TTL after finish; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl create job --from=cronjob/NAME MANUAL -n NS` plus recent events/changes, then correlate the service-specific SLI. garbage-collects completed Jobs after evidence retention window. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### JOBS-AND-CRONJOBS-MP-08

- [ ] **Question:** Production is degraded around Cron schedule/time zone; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n NS job/NAME --all-containers` plus recent events/changes, then correlate the service-specific SLI. controller creates Jobs from wall-clock schedule with missed-run handling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### JOBS-AND-CRONJOBS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Concurrency policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get job,cronjob -A` plus recent events/changes, then correlate the service-specific SLI. Allow/Forbid/Replace controls overlap but application locks may still be needed. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### JOBS-AND-CRONJOBS-MP-10

- [ ] **Question:** Production is degraded around Starting deadline; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe job NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. skips or starts missed schedules within a tolerance window. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### JOBS-AND-CRONJOBS-SN-01

- [ ] **Question:** Design a production Jobs and CronJobs capability where Completion, Active deadline and TTL after finish are first-class requirements.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Job succeeds after required successful Pods/completions under mode semantics. limits total Job runtime including retries. garbage-collects completed Jobs after evidence retention window. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### JOBS-AND-CRONJOBS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Jobs and CronJobs capability where Parallelism, Indexed Job and Cron schedule/time zone are first-class requirements.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: number of Pods executing concurrently and downstream load. gives stable completion indexes for partitioned work. controller creates Jobs from wall-clock schedule with missed-run handling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### JOBS-AND-CRONJOBS-SN-03

- [ ] **Question:** Design a production Jobs and CronJobs capability where Backoff limit, Pod failure policy and Concurrency policy are first-class requirements.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bounds Pod failures before Job fails but retries can repeat effects. classifies exit/status outcomes to fail/ignore/count under supported versions. Allow/Forbid/Replace controls overlap but application locks may still be needed. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### JOBS-AND-CRONJOBS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Jobs and CronJobs capability where Active deadline, TTL after finish and Starting deadline are first-class requirements.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: limits total Job runtime including retries. garbage-collects completed Jobs after evidence retention window. skips or starts missed schedules within a tolerance window. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### JOBS-AND-CRONJOBS-SN-05

- [ ] **Question:** Design a production Jobs and CronJobs capability where Indexed Job, Cron schedule/time zone and Completion are first-class requirements.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: gives stable completion indexes for partitioned work. controller creates Jobs from wall-clock schedule with missed-run handling. Job succeeds after required successful Pods/completions under mode semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### JOBS-AND-CRONJOBS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Jobs and CronJobs capability where Pod failure policy, Concurrency policy and Parallelism are first-class requirements.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: classifies exit/status outcomes to fail/ignore/count under supported versions. Allow/Forbid/Replace controls overlap but application locks may still be needed. number of Pods executing concurrently and downstream load. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### JOBS-AND-CRONJOBS-SN-07

- [ ] **Question:** Design a production Jobs and CronJobs capability where TTL after finish, Starting deadline and Backoff limit are first-class requirements.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: garbage-collects completed Jobs after evidence retention window. skips or starts missed schedules within a tolerance window. bounds Pod failures before Job fails but retries can repeat effects. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### JOBS-AND-CRONJOBS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Jobs and CronJobs capability where Cron schedule/time zone, Completion and Active deadline are first-class requirements.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controller creates Jobs from wall-clock schedule with missed-run handling. Job succeeds after required successful Pods/completions under mode semantics. limits total Job runtime including retries. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### JOBS-AND-CRONJOBS-SN-09

- [ ] **Question:** Design a production Jobs and CronJobs capability where Concurrency policy, Parallelism and Indexed Job are first-class requirements.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Allow/Forbid/Replace controls overlap but application locks may still be needed. number of Pods executing concurrently and downstream load. gives stable completion indexes for partitioned work. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### JOBS-AND-CRONJOBS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Jobs and CronJobs capability where Starting deadline, Backoff limit and Pod failure policy are first-class requirements.
> **Covered in:** [Jobs and CronJobs — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: skips or starts missed schedules within a tolerance window. bounds Pod failures before Job fails but retries can repeat effects. classifies exit/status outcomes to fail/ignore/count under supported versions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### JOBS-AND-CRONJOBS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Completion. How do you lead it end to end?
> **Covered in:** [Jobs and CronJobs — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get job,cronjob -A` as one read-only checkpoint, not the whole diagnosis. Job succeeds after required successful Pods/completions under mode semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### JOBS-AND-CRONJOBS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Parallelism. How do you lead it end to end?
> **Covered in:** [Jobs and CronJobs — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe job NAME -n NS` as one read-only checkpoint, not the whole diagnosis. number of Pods executing concurrently and downstream load. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### JOBS-AND-CRONJOBS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backoff limit. How do you lead it end to end?
> **Covered in:** [Jobs and CronJobs — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl create job --from=cronjob/NAME MANUAL -n NS` as one read-only checkpoint, not the whole diagnosis. bounds Pod failures before Job fails but retries can repeat effects. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### JOBS-AND-CRONJOBS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Active deadline. How do you lead it end to end?
> **Covered in:** [Jobs and CronJobs — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n NS job/NAME --all-containers` as one read-only checkpoint, not the whole diagnosis. limits total Job runtime including retries. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### JOBS-AND-CRONJOBS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Indexed Job. How do you lead it end to end?
> **Covered in:** [Jobs and CronJobs — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get job,cronjob -A` as one read-only checkpoint, not the whole diagnosis. gives stable completion indexes for partitioned work. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### JOBS-AND-CRONJOBS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod failure policy. How do you lead it end to end?
> **Covered in:** [Jobs and CronJobs — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe job NAME -n NS` as one read-only checkpoint, not the whole diagnosis. classifies exit/status outcomes to fail/ignore/count under supported versions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### JOBS-AND-CRONJOBS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TTL after finish. How do you lead it end to end?
> **Covered in:** [Jobs and CronJobs — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl create job --from=cronjob/NAME MANUAL -n NS` as one read-only checkpoint, not the whole diagnosis. garbage-collects completed Jobs after evidence retention window. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### JOBS-AND-CRONJOBS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cron schedule/time zone. How do you lead it end to end?
> **Covered in:** [Jobs and CronJobs — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n NS job/NAME --all-containers` as one read-only checkpoint, not the whole diagnosis. controller creates Jobs from wall-clock schedule with missed-run handling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### JOBS-AND-CRONJOBS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Concurrency policy. How do you lead it end to end?
> **Covered in:** [Jobs and CronJobs — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get job,cronjob -A` as one read-only checkpoint, not the whole diagnosis. Allow/Forbid/Replace controls overlap but application locks may still be needed. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### JOBS-AND-CRONJOBS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Starting deadline. How do you lead it end to end?
> **Covered in:** [Jobs and CronJobs — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe job NAME -n NS` as one read-only checkpoint, not the whole diagnosis. skips or starts missed schedules within a tolerance window. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: StatefulSets and DaemonSets](../03-statefulsets-daemonsets/README.md) · [Study note](README.md) · [Next: Probes and container lifecycle →](../05-probes-lifecycle/README.md)

<!-- reading-navigation:end -->
