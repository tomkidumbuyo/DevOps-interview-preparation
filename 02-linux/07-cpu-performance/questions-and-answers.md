# CPU performance — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### CPU-PERFORMANCE-JN-01

- [ ] **Question:** What is Load average, and why does it matter in CPU performance?
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** counts runnable and uninterruptible tasks over time, so high load can mean CPU contention or blocked I/O rather than CPU percentage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CPU-PERFORMANCE-JN-02

- [ ] **Question:** What is CPU utilization, and why does it matter in CPU performance?
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CPU-PERFORMANCE-JN-03

- [ ] **Question:** What is User time, and why does it matter in CPU performance?
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CPU-PERFORMANCE-JN-04

- [ ] **Question:** What is System time, and why does it matter in CPU performance?
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CPU-PERFORMANCE-JN-05

- [ ] **Question:** What is I/O wait, and why does it matter in CPU performance?
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is CPU accounting for idle time while tasks await I/O and must be correlated with device latency/queue and application blocking. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CPU-PERFORMANCE-JN-06

- [ ] **Question:** What is Steal time, and why does it matter in CPU performance?
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CPU-PERFORMANCE-JN-07

- [ ] **Question:** What is Context switches, and why does it matter in CPU performance?
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CPU-PERFORMANCE-JN-08

- [ ] **Code:** **Question:** What does `ip route; ss -lntup; journalctl -b` help you verify for CPU performance?
> **Covered in:** [CPU performance — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### CPU-PERFORMANCE-JN-09

- [ ] **Code:** **Question:** What does `uname -a; systemd-analyze` help you verify for CPU performance?
> **Covered in:** [CPU performance — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### CPU-PERFORMANCE-JN-10

- [ ] **Code:** **Question:** What does `ps -eo pid,ppid,state,pcpu,pmem,cmd` help you verify for CPU performance?
> **Covered in:** [CPU performance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### CPU-PERFORMANCE-JP-01

- [ ] **Code:** **Question:** A basic Load average check fails. What would you do first using the CLI?
> **Covered in:** [CPU performance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `uname -a; systemd-analyze` and capture exact status/reason/request ID. counts runnable and uninterruptible tasks over time, so high load can mean CPU contention or blocked I/O rather than CPU percentage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CPU-PERFORMANCE-JP-02

- [ ] **Question:** A basic CPU utilization check fails. What would you do first?
> **Covered in:** [CPU performance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ps -eo pid,ppid,state,pcpu,pmem,cmd` and capture exact status/reason/request ID. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CPU-PERFORMANCE-JP-03

- [ ] **Question:** A basic User time check fails. What would you do first?
> **Covered in:** [CPU performance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `vmstat 1; iostat -xz 1` and capture exact status/reason/request ID. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CPU-PERFORMANCE-JP-04

- [ ] **Code:** **Question:** A basic System time check fails. What would you do first using the CLI?
> **Covered in:** [CPU performance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip route; ss -lntup; journalctl -b` and capture exact status/reason/request ID. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CPU-PERFORMANCE-JP-05

- [ ] **Question:** A basic I/O wait check fails. What would you do first?
> **Covered in:** [CPU performance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `uname -a; systemd-analyze` and capture exact status/reason/request ID. is CPU accounting for idle time while tasks await I/O and must be correlated with device latency/queue and application blocking. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CPU-PERFORMANCE-JP-06

- [ ] **Question:** A basic Steal time check fails. What would you do first?
> **Covered in:** [CPU performance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ps -eo pid,ppid,state,pcpu,pmem,cmd` and capture exact status/reason/request ID. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CPU-PERFORMANCE-JP-07

- [ ] **Code:** **Question:** A basic Context switches check fails. What would you do first using the CLI?
> **Covered in:** [CPU performance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `vmstat 1; iostat -xz 1` and capture exact status/reason/request ID. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CPU-PERFORMANCE-JP-08

- [ ] **Question:** A basic Interrupts check fails. What would you do first?
> **Covered in:** [CPU performance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip route; ss -lntup; journalctl -b` and capture exact status/reason/request ID. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CPU-PERFORMANCE-JP-09

- [ ] **Question:** A basic CPU saturation check fails. What would you do first?
> **Covered in:** [CPU performance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `uname -a; systemd-analyze` and capture exact status/reason/request ID. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CPU-PERFORMANCE-JP-10

- [ ] **Code:** **Question:** A basic CPU throttling check fails. What would you do first using the CLI?
> **Covered in:** [CPU performance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ps -eo pid,ppid,state,pcpu,pmem,cmd` and capture exact status/reason/request ID. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### CPU-PERFORMANCE-MN-01

- [ ] **Question:** Compare Load average with CPU utilization. When would each change your design?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Load average: counts runnable and uninterruptible tasks over time, so high load can mean CPU contention or blocked I/O rather than CPU percentage. CPU utilization: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CPU-PERFORMANCE-MN-02

- [ ] **Question:** Compare CPU utilization with User time. When would each change your design?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** CPU utilization: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. User time: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CPU-PERFORMANCE-MN-03

- [ ] **Question:** Compare User time with System time. When would each change your design?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** User time: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. System time: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CPU-PERFORMANCE-MN-04

- [ ] **Configuration review:** **Question:** Compare System time with I/O wait. When would each change your design?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** System time: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. I/O wait: is CPU accounting for idle time while tasks await I/O and must be correlated with device latency/queue and application blocking. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CPU-PERFORMANCE-MN-05

- [ ] **Question:** Compare I/O wait with Steal time. When would each change your design?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** I/O wait: is CPU accounting for idle time while tasks await I/O and must be correlated with device latency/queue and application blocking. Steal time: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CPU-PERFORMANCE-MN-06

- [ ] **Question:** Compare Steal time with Context switches. When would each change your design?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Steal time: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Context switches: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CPU-PERFORMANCE-MN-07

- [ ] **Configuration review:** **Question:** Compare Context switches with Interrupts. When would each change your design?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Context switches: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Interrupts: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CPU-PERFORMANCE-MN-08

- [ ] **Question:** Compare Interrupts with CPU saturation. When would each change your design?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Interrupts: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. CPU saturation: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CPU-PERFORMANCE-MN-09

- [ ] **Question:** Compare CPU saturation with CPU throttling. When would each change your design?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** CPU saturation: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. CPU throttling: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CPU-PERFORMANCE-MN-10

- [ ] **Configuration review:** **Question:** Compare CPU throttling with Load average. When would each change your design?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** CPU throttling: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Load average: counts runnable and uninterruptible tasks over time, so high load can mean CPU contention or blocked I/O rather than CPU percentage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### CPU-PERFORMANCE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Load average; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `uname -a; systemd-analyze` plus recent events/changes, then correlate the service-specific SLI. counts runnable and uninterruptible tasks over time, so high load can mean CPU contention or blocked I/O rather than CPU percentage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CPU-PERFORMANCE-MP-02

- [ ] **Question:** Production is degraded around CPU utilization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ps -eo pid,ppid,state,pcpu,pmem,cmd` plus recent events/changes, then correlate the service-specific SLI. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CPU-PERFORMANCE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around User time; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `vmstat 1; iostat -xz 1` plus recent events/changes, then correlate the service-specific SLI. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CPU-PERFORMANCE-MP-04

- [ ] **Question:** Production is degraded around System time; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip route; ss -lntup; journalctl -b` plus recent events/changes, then correlate the service-specific SLI. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CPU-PERFORMANCE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around I/O wait; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `uname -a; systemd-analyze` plus recent events/changes, then correlate the service-specific SLI. is CPU accounting for idle time while tasks await I/O and must be correlated with device latency/queue and application blocking. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CPU-PERFORMANCE-MP-06

- [ ] **Question:** Production is degraded around Steal time; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ps -eo pid,ppid,state,pcpu,pmem,cmd` plus recent events/changes, then correlate the service-specific SLI. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CPU-PERFORMANCE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Context switches; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `vmstat 1; iostat -xz 1` plus recent events/changes, then correlate the service-specific SLI. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CPU-PERFORMANCE-MP-08

- [ ] **Question:** Production is degraded around Interrupts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip route; ss -lntup; journalctl -b` plus recent events/changes, then correlate the service-specific SLI. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CPU-PERFORMANCE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around CPU saturation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `uname -a; systemd-analyze` plus recent events/changes, then correlate the service-specific SLI. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CPU-PERFORMANCE-MP-10

- [ ] **Question:** Production is degraded around CPU throttling; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ps -eo pid,ppid,state,pcpu,pmem,cmd` plus recent events/changes, then correlate the service-specific SLI. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### CPU-PERFORMANCE-SN-01

- [ ] **Question:** Design a production CPU performance capability where Load average, System time and Context switches are first-class requirements.
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: counts runnable and uninterruptible tasks over time, so high load can mean CPU contention or blocked I/O rather than CPU percentage. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CPU-PERFORMANCE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production CPU performance capability where CPU utilization, I/O wait and Interrupts are first-class requirements.
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is CPU accounting for idle time while tasks await I/O and must be correlated with device latency/queue and application blocking. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CPU-PERFORMANCE-SN-03

- [ ] **Question:** Design a production CPU performance capability where User time, Steal time and CPU saturation are first-class requirements.
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CPU-PERFORMANCE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production CPU performance capability where System time, Context switches and CPU throttling are first-class requirements.
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CPU-PERFORMANCE-SN-05

- [ ] **Question:** Design a production CPU performance capability where I/O wait, Interrupts and Load average are first-class requirements.
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is CPU accounting for idle time while tasks await I/O and must be correlated with device latency/queue and application blocking. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. counts runnable and uninterruptible tasks over time, so high load can mean CPU contention or blocked I/O rather than CPU percentage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CPU-PERFORMANCE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production CPU performance capability where Steal time, CPU saturation and CPU utilization are first-class requirements.
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CPU-PERFORMANCE-SN-07

- [ ] **Question:** Design a production CPU performance capability where Context switches, CPU throttling and User time are first-class requirements.
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CPU-PERFORMANCE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production CPU performance capability where Interrupts, Load average and System time are first-class requirements.
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. counts runnable and uninterruptible tasks over time, so high load can mean CPU contention or blocked I/O rather than CPU percentage. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CPU-PERFORMANCE-SN-09

- [ ] **Question:** Design a production CPU performance capability where CPU saturation, CPU utilization and I/O wait are first-class requirements.
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is CPU accounting for idle time while tasks await I/O and must be correlated with device latency/queue and application blocking. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CPU-PERFORMANCE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production CPU performance capability where CPU throttling, User time and Steal time are first-class requirements.
> **Covered in:** [CPU performance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### CPU-PERFORMANCE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Load average. How do you lead it end to end?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `uname -a; systemd-analyze` as one read-only checkpoint, not the whole diagnosis. counts runnable and uninterruptible tasks over time, so high load can mean CPU contention or blocked I/O rather than CPU percentage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CPU-PERFORMANCE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CPU utilization. How do you lead it end to end?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ps -eo pid,ppid,state,pcpu,pmem,cmd` as one read-only checkpoint, not the whole diagnosis. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CPU-PERFORMANCE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving User time. How do you lead it end to end?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `vmstat 1; iostat -xz 1` as one read-only checkpoint, not the whole diagnosis. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CPU-PERFORMANCE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving System time. How do you lead it end to end?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip route; ss -lntup; journalctl -b` as one read-only checkpoint, not the whole diagnosis. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CPU-PERFORMANCE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving I/O wait. How do you lead it end to end?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `uname -a; systemd-analyze` as one read-only checkpoint, not the whole diagnosis. is CPU accounting for idle time while tasks await I/O and must be correlated with device latency/queue and application blocking. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CPU-PERFORMANCE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Steal time. How do you lead it end to end?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ps -eo pid,ppid,state,pcpu,pmem,cmd` as one read-only checkpoint, not the whole diagnosis. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CPU-PERFORMANCE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Context switches. How do you lead it end to end?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `vmstat 1; iostat -xz 1` as one read-only checkpoint, not the whole diagnosis. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CPU-PERFORMANCE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Interrupts. How do you lead it end to end?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip route; ss -lntup; journalctl -b` as one read-only checkpoint, not the whole diagnosis. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CPU-PERFORMANCE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CPU saturation. How do you lead it end to end?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `uname -a; systemd-analyze` as one read-only checkpoint, not the whole diagnosis. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CPU-PERFORMANCE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CPU throttling. How do you lead it end to end?
> **Covered in:** [CPU performance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ps -eo pid,ppid,state,pcpu,pmem,cmd` as one read-only checkpoint, not the whole diagnosis. is part of CPU performance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Memory](../06-memory/README.md) · [Study note](README.md) · [Next: Storage and I/O →](../08-storage-and-i-o/README.md)

<!-- reading-navigation:end -->
