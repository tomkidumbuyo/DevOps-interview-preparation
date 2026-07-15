# Resource requests, limits and QoS — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JN-01

- [ ] **Question:** What is CPU request, and why does it matter in Resource requests, limits and QoS?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** scheduler reservation and HPA utilization denominator, expressed in cores/millicores. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JN-02

- [ ] **Question:** What is CPU limit, and why does it matter in Resource requests, limits and QoS?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JN-03

- [ ] **Question:** What is Memory request, and why does it matter in Resource requests, limits and QoS?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** scheduling reservation/eviction signal rather than guaranteed preallocation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JN-04

- [ ] **Question:** What is Memory limit, and why does it matter in Resource requests, limits and QoS?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** cgroup hard boundary can OOM-kill a container. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JN-05

- [ ] **Question:** What is Ephemeral-storage, and why does it matter in Resource requests, limits and QoS?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** writable layer/log/emptyDir request/limit interacts with node disk eviction. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JN-06

- [ ] **Question:** What is Guaranteed QoS, and why does it matter in Resource requests, limits and QoS?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** equal CPU/memory request/limit on every container gives strongest eviction priority. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JN-07

- [ ] **Question:** What is Burstable QoS, and why does it matter in Resource requests, limits and QoS?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** at least one request/limit but not Guaranteed; common production class. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JN-08

- [ ] **Code:** **Question:** What does `kubectl get resourcequota,limitrange -A` help you verify for Resource requests, limits and QoS?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: no requests/limits and first under resource pressure.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JN-09

- [ ] **Code:** **Question:** What does `kubectl top pod -A --containers` help you verify for Resource requests, limits and QoS?
> **Covered in:** [Resource requests, limits and QoS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: injects/enforces per-container defaults and bounds.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe node NODE` help you verify for Resource requests, limits and QoS?
> **Covered in:** [Resource requests, limits and QoS — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: namespace aggregate limits can reject objects or cap priority/storage/GPU counts.

## Junior — procedural and command questions

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JP-01

- [ ] **Code:** **Question:** A basic CPU request check fails. What would you do first using the CLI?
> **Covered in:** [Resource requests, limits and QoS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -A --containers` and capture exact status/reason/request ID. scheduler reservation and HPA utilization denominator, expressed in cores/millicores. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JP-02

- [ ] **Question:** A basic CPU limit check fails. What would you do first?
> **Covered in:** [Resource requests, limits and QoS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe node NODE` and capture exact status/reason/request ID. cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JP-03

- [ ] **Question:** A basic Memory request check fails. What would you do first?
> **Covered in:** [Resource requests, limits and QoS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pod POD -o jsonpath='{.status.qosClass}'` and capture exact status/reason/request ID. scheduling reservation/eviction signal rather than guaranteed preallocation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JP-04

- [ ] **Code:** **Question:** A basic Memory limit check fails. What would you do first using the CLI?
> **Covered in:** [Resource requests, limits and QoS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get resourcequota,limitrange -A` and capture exact status/reason/request ID. cgroup hard boundary can OOM-kill a container. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JP-05

- [ ] **Question:** A basic Ephemeral-storage check fails. What would you do first?
> **Covered in:** [Resource requests, limits and QoS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -A --containers` and capture exact status/reason/request ID. writable layer/log/emptyDir request/limit interacts with node disk eviction. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JP-06

- [ ] **Question:** A basic Guaranteed QoS check fails. What would you do first?
> **Covered in:** [Resource requests, limits and QoS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe node NODE` and capture exact status/reason/request ID. equal CPU/memory request/limit on every container gives strongest eviction priority. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JP-07

- [ ] **Code:** **Question:** A basic Burstable QoS check fails. What would you do first using the CLI?
> **Covered in:** [Resource requests, limits and QoS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pod POD -o jsonpath='{.status.qosClass}'` and capture exact status/reason/request ID. at least one request/limit but not Guaranteed; common production class. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JP-08

- [ ] **Question:** A basic BestEffort QoS check fails. What would you do first?
> **Covered in:** [Resource requests, limits and QoS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get resourcequota,limitrange -A` and capture exact status/reason/request ID. no requests/limits and first under resource pressure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JP-09

- [ ] **Question:** A basic LimitRange check fails. What would you do first?
> **Covered in:** [Resource requests, limits and QoS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -A --containers` and capture exact status/reason/request ID. injects/enforces per-container defaults and bounds. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-JP-10

- [ ] **Code:** **Question:** A basic ResourceQuota check fails. What would you do first using the CLI?
> **Covered in:** [Resource requests, limits and QoS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe node NODE` and capture exact status/reason/request ID. namespace aggregate limits can reject objects or cap priority/storage/GPU counts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MN-01

- [ ] **Question:** Compare CPU request with CPU limit. When would each change your design?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CPU request: scheduler reservation and HPA utilization denominator, expressed in cores/millicores. CPU limit: cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MN-02

- [ ] **Question:** Compare CPU limit with Memory request. When would each change your design?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CPU limit: cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. Memory request: scheduling reservation/eviction signal rather than guaranteed preallocation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MN-03

- [ ] **Question:** Compare Memory request with Memory limit. When would each change your design?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Memory request: scheduling reservation/eviction signal rather than guaranteed preallocation. Memory limit: cgroup hard boundary can OOM-kill a container. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MN-04

- [ ] **Configuration review:** **Question:** Compare Memory limit with Ephemeral-storage. When would each change your design?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Memory limit: cgroup hard boundary can OOM-kill a container. Ephemeral-storage: writable layer/log/emptyDir request/limit interacts with node disk eviction. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MN-05

- [ ] **Question:** Compare Ephemeral-storage with Guaranteed QoS. When would each change your design?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Ephemeral-storage: writable layer/log/emptyDir request/limit interacts with node disk eviction. Guaranteed QoS: equal CPU/memory request/limit on every container gives strongest eviction priority. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MN-06

- [ ] **Question:** Compare Guaranteed QoS with Burstable QoS. When would each change your design?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Guaranteed QoS: equal CPU/memory request/limit on every container gives strongest eviction priority. Burstable QoS: at least one request/limit but not Guaranteed; common production class. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MN-07

- [ ] **Configuration review:** **Question:** Compare Burstable QoS with BestEffort QoS. When would each change your design?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Burstable QoS: at least one request/limit but not Guaranteed; common production class. BestEffort QoS: no requests/limits and first under resource pressure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MN-08

- [ ] **Question:** Compare BestEffort QoS with LimitRange. When would each change your design?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** BestEffort QoS: no requests/limits and first under resource pressure. LimitRange: injects/enforces per-container defaults and bounds. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MN-09

- [ ] **Question:** Compare LimitRange with ResourceQuota. When would each change your design?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** LimitRange: injects/enforces per-container defaults and bounds. ResourceQuota: namespace aggregate limits can reject objects or cap priority/storage/GPU counts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MN-10

- [ ] **Configuration review:** **Question:** Compare ResourceQuota with CPU request. When would each change your design?
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ResourceQuota: namespace aggregate limits can reject objects or cap priority/storage/GPU counts. CPU request: scheduler reservation and HPA utilization denominator, expressed in cores/millicores. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around CPU request; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. scheduler reservation and HPA utilization denominator, expressed in cores/millicores. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MP-02

- [ ] **Question:** Production is degraded around CPU limit; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe node NODE` plus recent events/changes, then correlate the service-specific SLI. cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Memory request; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pod POD -o jsonpath='{.status.qosClass}'` plus recent events/changes, then correlate the service-specific SLI. scheduling reservation/eviction signal rather than guaranteed preallocation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MP-04

- [ ] **Question:** Production is degraded around Memory limit; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get resourcequota,limitrange -A` plus recent events/changes, then correlate the service-specific SLI. cgroup hard boundary can OOM-kill a container. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Ephemeral-storage; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. writable layer/log/emptyDir request/limit interacts with node disk eviction. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MP-06

- [ ] **Question:** Production is degraded around Guaranteed QoS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe node NODE` plus recent events/changes, then correlate the service-specific SLI. equal CPU/memory request/limit on every container gives strongest eviction priority. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Burstable QoS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pod POD -o jsonpath='{.status.qosClass}'` plus recent events/changes, then correlate the service-specific SLI. at least one request/limit but not Guaranteed; common production class. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MP-08

- [ ] **Question:** Production is degraded around BestEffort QoS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get resourcequota,limitrange -A` plus recent events/changes, then correlate the service-specific SLI. no requests/limits and first under resource pressure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around LimitRange; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. injects/enforces per-container defaults and bounds. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-MP-10

- [ ] **Question:** Production is degraded around ResourceQuota; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe node NODE` plus recent events/changes, then correlate the service-specific SLI. namespace aggregate limits can reject objects or cap priority/storage/GPU counts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SN-01

- [ ] **Question:** Design a production Resource requests, limits and QoS capability where CPU request, Memory limit and Burstable QoS are first-class requirements.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scheduler reservation and HPA utilization denominator, expressed in cores/millicores. cgroup hard boundary can OOM-kill a container. at least one request/limit but not Guaranteed; common production class. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Resource requests, limits and QoS capability where CPU limit, Ephemeral-storage and BestEffort QoS are first-class requirements.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. writable layer/log/emptyDir request/limit interacts with node disk eviction. no requests/limits and first under resource pressure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SN-03

- [ ] **Question:** Design a production Resource requests, limits and QoS capability where Memory request, Guaranteed QoS and LimitRange are first-class requirements.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scheduling reservation/eviction signal rather than guaranteed preallocation. equal CPU/memory request/limit on every container gives strongest eviction priority. injects/enforces per-container defaults and bounds. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Resource requests, limits and QoS capability where Memory limit, Burstable QoS and ResourceQuota are first-class requirements.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cgroup hard boundary can OOM-kill a container. at least one request/limit but not Guaranteed; common production class. namespace aggregate limits can reject objects or cap priority/storage/GPU counts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SN-05

- [ ] **Question:** Design a production Resource requests, limits and QoS capability where Ephemeral-storage, BestEffort QoS and CPU request are first-class requirements.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: writable layer/log/emptyDir request/limit interacts with node disk eviction. no requests/limits and first under resource pressure. scheduler reservation and HPA utilization denominator, expressed in cores/millicores. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Resource requests, limits and QoS capability where Guaranteed QoS, LimitRange and CPU limit are first-class requirements.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: equal CPU/memory request/limit on every container gives strongest eviction priority. injects/enforces per-container defaults and bounds. cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SN-07

- [ ] **Question:** Design a production Resource requests, limits and QoS capability where Burstable QoS, ResourceQuota and Memory request are first-class requirements.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: at least one request/limit but not Guaranteed; common production class. namespace aggregate limits can reject objects or cap priority/storage/GPU counts. scheduling reservation/eviction signal rather than guaranteed preallocation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Resource requests, limits and QoS capability where BestEffort QoS, CPU request and Memory limit are first-class requirements.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: no requests/limits and first under resource pressure. scheduler reservation and HPA utilization denominator, expressed in cores/millicores. cgroup hard boundary can OOM-kill a container. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SN-09

- [ ] **Question:** Design a production Resource requests, limits and QoS capability where LimitRange, CPU limit and Ephemeral-storage are first-class requirements.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: injects/enforces per-container defaults and bounds. cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. writable layer/log/emptyDir request/limit interacts with node disk eviction. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Resource requests, limits and QoS capability where ResourceQuota, Memory request and Guaranteed QoS are first-class requirements.
> **Covered in:** [Resource requests, limits and QoS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: namespace aggregate limits can reject objects or cap priority/storage/GPU counts. scheduling reservation/eviction signal rather than guaranteed preallocation. equal CPU/memory request/limit on every container gives strongest eviction priority. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CPU request. How do you lead it end to end?
> **Covered in:** [Resource requests, limits and QoS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. scheduler reservation and HPA utilization denominator, expressed in cores/millicores. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CPU limit. How do you lead it end to end?
> **Covered in:** [Resource requests, limits and QoS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe node NODE` as one read-only checkpoint, not the whole diagnosis. cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Memory request. How do you lead it end to end?
> **Covered in:** [Resource requests, limits and QoS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pod POD -o jsonpath='{.status.qosClass}'` as one read-only checkpoint, not the whole diagnosis. scheduling reservation/eviction signal rather than guaranteed preallocation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Memory limit. How do you lead it end to end?
> **Covered in:** [Resource requests, limits and QoS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get resourcequota,limitrange -A` as one read-only checkpoint, not the whole diagnosis. cgroup hard boundary can OOM-kill a container. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ephemeral-storage. How do you lead it end to end?
> **Covered in:** [Resource requests, limits and QoS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. writable layer/log/emptyDir request/limit interacts with node disk eviction. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Guaranteed QoS. How do you lead it end to end?
> **Covered in:** [Resource requests, limits and QoS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe node NODE` as one read-only checkpoint, not the whole diagnosis. equal CPU/memory request/limit on every container gives strongest eviction priority. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Burstable QoS. How do you lead it end to end?
> **Covered in:** [Resource requests, limits and QoS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pod POD -o jsonpath='{.status.qosClass}'` as one read-only checkpoint, not the whole diagnosis. at least one request/limit but not Guaranteed; common production class. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving BestEffort QoS. How do you lead it end to end?
> **Covered in:** [Resource requests, limits and QoS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get resourcequota,limitrange -A` as one read-only checkpoint, not the whole diagnosis. no requests/limits and first under resource pressure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving LimitRange. How do you lead it end to end?
> **Covered in:** [Resource requests, limits and QoS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. injects/enforces per-container defaults and bounds. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESOURCE-REQUESTS-LIMITS-AND-QOS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ResourceQuota. How do you lead it end to end?
> **Covered in:** [Resource requests, limits and QoS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe node NODE` as one read-only checkpoint, not the whole diagnosis. namespace aggregate limits can reject objects or cap priority/storage/GPU counts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Scheduling Autoscaling](../README.md) · [Study note](README.md) · [Next: Affinity, taints and topology placement →](../02-placement/README.md)

<!-- reading-navigation:end -->
