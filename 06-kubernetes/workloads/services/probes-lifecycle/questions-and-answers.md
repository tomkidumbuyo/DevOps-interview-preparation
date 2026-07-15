# Probes and container lifecycle — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### PROBES-AND-CONTAINER-LIFECYCLE-JN-01

- [ ] **Question:** What is Startup probe, and why does it matter in Probes and container lifecycle?

**Answer:** delays liveness/readiness scheduling until slow initialization succeeds. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROBES-AND-CONTAINER-LIFECYCLE-JN-02

- [ ] **Question:** What is Liveness probe, and why does it matter in Probes and container lifecycle?

**Answer:** detects unrecoverable local process state and triggers restart. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROBES-AND-CONTAINER-LIFECYCLE-JN-03

- [ ] **Question:** What is Readiness probe, and why does it matter in Probes and container lifecycle?

**Answer:** removes a Pod from endpoints without restarting it. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROBES-AND-CONTAINER-LIFECYCLE-JN-04

- [ ] **Question:** What is HTTP probe, and why does it matter in Probes and container lifecycle?

**Answer:** kubelet calls path/port/scheme with specific host/header semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROBES-AND-CONTAINER-LIFECYCLE-JN-05

- [ ] **Question:** What is TCP probe, and why does it matter in Probes and container lifecycle?

**Answer:** verifies connection acceptance but not application correctness. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROBES-AND-CONTAINER-LIFECYCLE-JN-06

- [ ] **Question:** What is Exec probe, and why does it matter in Probes and container lifecycle?

**Answer:** runs in container and can consume resources/hang if poorly designed. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROBES-AND-CONTAINER-LIFECYCLE-JN-07

- [ ] **Question:** What is gRPC probe, and why does it matter in Probes and container lifecycle?

**Answer:** calls standard health protocol under supported version/config. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROBES-AND-CONTAINER-LIFECYCLE-JN-08

- [ ] **Code:** **Question:** What does `kubectl logs POD -n NS --previous` help you verify for Probes and container lifecycle?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: period/timeout/success/failure determine detection and recovery timing.

### PROBES-AND-CONTAINER-LIFECYCLE-JN-09

- [ ] **Code:** **Question:** What does `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` help you verify for Probes and container lifecycle?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: hook runs before termination signal and consumes the same grace period.

### PROBES-AND-CONTAINER-LIFECYCLE-JN-10

- [ ] **Code:** **Question:** What does `kubectl get pod POD -n NS -o jsonpath='{.status.containerStatuses}' | jq` help you verify for Probes and container lifecycle?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: image/runtime/Pod signal and application handler determine graceful drain.

## Junior — procedural and command questions

### PROBES-AND-CONTAINER-LIFECYCLE-JP-01

- [ ] **Code:** **Question:** A basic Startup probe check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` and capture exact status/reason/request ID. delays liveness/readiness scheduling until slow initialization succeeds. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROBES-AND-CONTAINER-LIFECYCLE-JP-02

- [ ] **Question:** A basic Liveness probe check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pod POD -n NS -o jsonpath='{.status.containerStatuses}' | jq` and capture exact status/reason/request ID. detects unrecoverable local process state and triggers restart. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROBES-AND-CONTAINER-LIFECYCLE-JP-03

- [ ] **Question:** A basic Readiness probe check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get endpointslice -n NS -l kubernetes.io/service-name=SVC -o yaml` and capture exact status/reason/request ID. removes a Pod from endpoints without restarting it. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROBES-AND-CONTAINER-LIFECYCLE-JP-04

- [ ] **Code:** **Question:** A basic HTTP probe check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs POD -n NS --previous` and capture exact status/reason/request ID. kubelet calls path/port/scheme with specific host/header semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROBES-AND-CONTAINER-LIFECYCLE-JP-05

- [ ] **Question:** A basic TCP probe check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` and capture exact status/reason/request ID. verifies connection acceptance but not application correctness. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROBES-AND-CONTAINER-LIFECYCLE-JP-06

- [ ] **Question:** A basic Exec probe check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pod POD -n NS -o jsonpath='{.status.containerStatuses}' | jq` and capture exact status/reason/request ID. runs in container and can consume resources/hang if poorly designed. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROBES-AND-CONTAINER-LIFECYCLE-JP-07

- [ ] **Code:** **Question:** A basic gRPC probe check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get endpointslice -n NS -l kubernetes.io/service-name=SVC -o yaml` and capture exact status/reason/request ID. calls standard health protocol under supported version/config. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROBES-AND-CONTAINER-LIFECYCLE-JP-08

- [ ] **Question:** A basic Probe thresholds check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs POD -n NS --previous` and capture exact status/reason/request ID. period/timeout/success/failure determine detection and recovery timing. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROBES-AND-CONTAINER-LIFECYCLE-JP-09

- [ ] **Question:** A basic preStop check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` and capture exact status/reason/request ID. hook runs before termination signal and consumes the same grace period. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROBES-AND-CONTAINER-LIFECYCLE-JP-10

- [ ] **Code:** **Question:** A basic Stop signal check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pod POD -n NS -o jsonpath='{.status.containerStatuses}' | jq` and capture exact status/reason/request ID. image/runtime/Pod signal and application handler determine graceful drain. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### PROBES-AND-CONTAINER-LIFECYCLE-MN-01

- [ ] **Question:** Compare Startup probe with Liveness probe. When would each change your design?

**Answer:** Startup probe: delays liveness/readiness scheduling until slow initialization succeeds. Liveness probe: detects unrecoverable local process state and triggers restart. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROBES-AND-CONTAINER-LIFECYCLE-MN-02

- [ ] **Question:** Compare Liveness probe with Readiness probe. When would each change your design?

**Answer:** Liveness probe: detects unrecoverable local process state and triggers restart. Readiness probe: removes a Pod from endpoints without restarting it. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROBES-AND-CONTAINER-LIFECYCLE-MN-03

- [ ] **Question:** Compare Readiness probe with HTTP probe. When would each change your design?

**Answer:** Readiness probe: removes a Pod from endpoints without restarting it. HTTP probe: kubelet calls path/port/scheme with specific host/header semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROBES-AND-CONTAINER-LIFECYCLE-MN-04

- [ ] **Configuration review:** **Question:** Compare HTTP probe with TCP probe. When would each change your design?

**Answer:** HTTP probe: kubelet calls path/port/scheme with specific host/header semantics. TCP probe: verifies connection acceptance but not application correctness. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROBES-AND-CONTAINER-LIFECYCLE-MN-05

- [ ] **Question:** Compare TCP probe with Exec probe. When would each change your design?

**Answer:** TCP probe: verifies connection acceptance but not application correctness. Exec probe: runs in container and can consume resources/hang if poorly designed. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROBES-AND-CONTAINER-LIFECYCLE-MN-06

- [ ] **Question:** Compare Exec probe with gRPC probe. When would each change your design?

**Answer:** Exec probe: runs in container and can consume resources/hang if poorly designed. gRPC probe: calls standard health protocol under supported version/config. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROBES-AND-CONTAINER-LIFECYCLE-MN-07

- [ ] **Configuration review:** **Question:** Compare gRPC probe with Probe thresholds. When would each change your design?

**Answer:** gRPC probe: calls standard health protocol under supported version/config. Probe thresholds: period/timeout/success/failure determine detection and recovery timing. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROBES-AND-CONTAINER-LIFECYCLE-MN-08

- [ ] **Question:** Compare Probe thresholds with preStop. When would each change your design?

**Answer:** Probe thresholds: period/timeout/success/failure determine detection and recovery timing. preStop: hook runs before termination signal and consumes the same grace period. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROBES-AND-CONTAINER-LIFECYCLE-MN-09

- [ ] **Question:** Compare preStop with Stop signal. When would each change your design?

**Answer:** preStop: hook runs before termination signal and consumes the same grace period. Stop signal: image/runtime/Pod signal and application handler determine graceful drain. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROBES-AND-CONTAINER-LIFECYCLE-MN-10

- [ ] **Configuration review:** **Question:** Compare Stop signal with Startup probe. When would each change your design?

**Answer:** Stop signal: image/runtime/Pod signal and application handler determine graceful drain. Startup probe: delays liveness/readiness scheduling until slow initialization succeeds. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### PROBES-AND-CONTAINER-LIFECYCLE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Startup probe; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` plus recent events/changes, then correlate the service-specific SLI. delays liveness/readiness scheduling until slow initialization succeeds. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROBES-AND-CONTAINER-LIFECYCLE-MP-02

- [ ] **Question:** Production is degraded around Liveness probe; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pod POD -n NS -o jsonpath='{.status.containerStatuses}' | jq` plus recent events/changes, then correlate the service-specific SLI. detects unrecoverable local process state and triggers restart. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROBES-AND-CONTAINER-LIFECYCLE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Readiness probe; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get endpointslice -n NS -l kubernetes.io/service-name=SVC -o yaml` plus recent events/changes, then correlate the service-specific SLI. removes a Pod from endpoints without restarting it. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROBES-AND-CONTAINER-LIFECYCLE-MP-04

- [ ] **Question:** Production is degraded around HTTP probe; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs POD -n NS --previous` plus recent events/changes, then correlate the service-specific SLI. kubelet calls path/port/scheme with specific host/header semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROBES-AND-CONTAINER-LIFECYCLE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around TCP probe; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` plus recent events/changes, then correlate the service-specific SLI. verifies connection acceptance but not application correctness. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROBES-AND-CONTAINER-LIFECYCLE-MP-06

- [ ] **Question:** Production is degraded around Exec probe; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pod POD -n NS -o jsonpath='{.status.containerStatuses}' | jq` plus recent events/changes, then correlate the service-specific SLI. runs in container and can consume resources/hang if poorly designed. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROBES-AND-CONTAINER-LIFECYCLE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around gRPC probe; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get endpointslice -n NS -l kubernetes.io/service-name=SVC -o yaml` plus recent events/changes, then correlate the service-specific SLI. calls standard health protocol under supported version/config. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROBES-AND-CONTAINER-LIFECYCLE-MP-08

- [ ] **Question:** Production is degraded around Probe thresholds; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs POD -n NS --previous` plus recent events/changes, then correlate the service-specific SLI. period/timeout/success/failure determine detection and recovery timing. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROBES-AND-CONTAINER-LIFECYCLE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around preStop; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` plus recent events/changes, then correlate the service-specific SLI. hook runs before termination signal and consumes the same grace period. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROBES-AND-CONTAINER-LIFECYCLE-MP-10

- [ ] **Question:** Production is degraded around Stop signal; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pod POD -n NS -o jsonpath='{.status.containerStatuses}' | jq` plus recent events/changes, then correlate the service-specific SLI. image/runtime/Pod signal and application handler determine graceful drain. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### PROBES-AND-CONTAINER-LIFECYCLE-SN-01

- [ ] **Question:** Design a production Probes and container lifecycle capability where Startup probe, HTTP probe and gRPC probe are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: delays liveness/readiness scheduling until slow initialization succeeds. kubelet calls path/port/scheme with specific host/header semantics. calls standard health protocol under supported version/config. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROBES-AND-CONTAINER-LIFECYCLE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Probes and container lifecycle capability where Liveness probe, TCP probe and Probe thresholds are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: detects unrecoverable local process state and triggers restart. verifies connection acceptance but not application correctness. period/timeout/success/failure determine detection and recovery timing. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROBES-AND-CONTAINER-LIFECYCLE-SN-03

- [ ] **Question:** Design a production Probes and container lifecycle capability where Readiness probe, Exec probe and preStop are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: removes a Pod from endpoints without restarting it. runs in container and can consume resources/hang if poorly designed. hook runs before termination signal and consumes the same grace period. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROBES-AND-CONTAINER-LIFECYCLE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Probes and container lifecycle capability where HTTP probe, gRPC probe and Stop signal are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: kubelet calls path/port/scheme with specific host/header semantics. calls standard health protocol under supported version/config. image/runtime/Pod signal and application handler determine graceful drain. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROBES-AND-CONTAINER-LIFECYCLE-SN-05

- [ ] **Question:** Design a production Probes and container lifecycle capability where TCP probe, Probe thresholds and Startup probe are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: verifies connection acceptance but not application correctness. period/timeout/success/failure determine detection and recovery timing. delays liveness/readiness scheduling until slow initialization succeeds. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROBES-AND-CONTAINER-LIFECYCLE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Probes and container lifecycle capability where Exec probe, preStop and Liveness probe are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: runs in container and can consume resources/hang if poorly designed. hook runs before termination signal and consumes the same grace period. detects unrecoverable local process state and triggers restart. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROBES-AND-CONTAINER-LIFECYCLE-SN-07

- [ ] **Question:** Design a production Probes and container lifecycle capability where gRPC probe, Stop signal and Readiness probe are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: calls standard health protocol under supported version/config. image/runtime/Pod signal and application handler determine graceful drain. removes a Pod from endpoints without restarting it. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROBES-AND-CONTAINER-LIFECYCLE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Probes and container lifecycle capability where Probe thresholds, Startup probe and HTTP probe are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: period/timeout/success/failure determine detection and recovery timing. delays liveness/readiness scheduling until slow initialization succeeds. kubelet calls path/port/scheme with specific host/header semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROBES-AND-CONTAINER-LIFECYCLE-SN-09

- [ ] **Question:** Design a production Probes and container lifecycle capability where preStop, Liveness probe and TCP probe are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: hook runs before termination signal and consumes the same grace period. detects unrecoverable local process state and triggers restart. verifies connection acceptance but not application correctness. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROBES-AND-CONTAINER-LIFECYCLE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Probes and container lifecycle capability where Stop signal, Readiness probe and Exec probe are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: image/runtime/Pod signal and application handler determine graceful drain. removes a Pod from endpoints without restarting it. runs in container and can consume resources/hang if poorly designed. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### PROBES-AND-CONTAINER-LIFECYCLE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Startup probe. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` as one read-only checkpoint, not the whole diagnosis. delays liveness/readiness scheduling until slow initialization succeeds. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROBES-AND-CONTAINER-LIFECYCLE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Liveness probe. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pod POD -n NS -o jsonpath='{.status.containerStatuses}' | jq` as one read-only checkpoint, not the whole diagnosis. detects unrecoverable local process state and triggers restart. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROBES-AND-CONTAINER-LIFECYCLE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Readiness probe. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get endpointslice -n NS -l kubernetes.io/service-name=SVC -o yaml` as one read-only checkpoint, not the whole diagnosis. removes a Pod from endpoints without restarting it. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROBES-AND-CONTAINER-LIFECYCLE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving HTTP probe. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs POD -n NS --previous` as one read-only checkpoint, not the whole diagnosis. kubelet calls path/port/scheme with specific host/header semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROBES-AND-CONTAINER-LIFECYCLE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TCP probe. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` as one read-only checkpoint, not the whole diagnosis. verifies connection acceptance but not application correctness. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROBES-AND-CONTAINER-LIFECYCLE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Exec probe. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pod POD -n NS -o jsonpath='{.status.containerStatuses}' | jq` as one read-only checkpoint, not the whole diagnosis. runs in container and can consume resources/hang if poorly designed. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROBES-AND-CONTAINER-LIFECYCLE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving gRPC probe. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get endpointslice -n NS -l kubernetes.io/service-name=SVC -o yaml` as one read-only checkpoint, not the whole diagnosis. calls standard health protocol under supported version/config. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROBES-AND-CONTAINER-LIFECYCLE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Probe thresholds. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs POD -n NS --previous` as one read-only checkpoint, not the whole diagnosis. period/timeout/success/failure determine detection and recovery timing. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROBES-AND-CONTAINER-LIFECYCLE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving preStop. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` as one read-only checkpoint, not the whole diagnosis. hook runs before termination signal and consumes the same grace period. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROBES-AND-CONTAINER-LIFECYCLE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stop signal. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pod POD -n NS -o jsonpath='{.status.containerStatuses}' | jq` as one read-only checkpoint, not the whole diagnosis. image/runtime/Pod signal and application handler determine graceful drain. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
