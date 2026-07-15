# Kubernetes troubleshooting and kubectl — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JN-01

- [ ] **Question:** What is Object status/conditions, and why does it matter in Kubernetes troubleshooting and kubectl?

**Answer:** observedGeneration, reason and message show controller interpretation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JN-02

- [ ] **Question:** What is Events, and why does it matter in Kubernetes troubleshooting and kubectl?

**Answer:** scheduling, pull, mount, probe and controller records point to the first failing transition. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JN-03

- [ ] **Question:** What is Previous logs, and why does it matter in Kubernetes troubleshooting and kubectl?

**Answer:** retrieve terminated container output during CrashLoopBackOff. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JN-04

- [ ] **Question:** What is Ephemeral debug, and why does it matter in Kubernetes troubleshooting and kubectl?

**Answer:** add diagnostic tooling without rebuilding the production image. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JN-05

- [ ] **Question:** What is Raw API/jsonpath/jq, and why does it matter in Kubernetes troubleshooting and kubectl?

**Answer:** inspect exact fields and aggregated status rather than visually scanning YAML. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JN-06

- [ ] **Question:** What is Node debug, and why does it matter in Kubernetes troubleshooting and kubectl?

**Answer:** enter host namespaces/filesystem carefully for kubelet/runtime/CNI evidence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JN-07

- [ ] **Question:** What is EndpointSlice, and why does it matter in Kubernetes troubleshooting and kubectl?

**Answer:** confirms whether readiness/selector produced routable Service targets. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JN-08

- [ ] **Code:** **Question:** What does `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` help you verify for Kubernetes troubleshooting and kubectl?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: separate scheduler topology from controller attach and node mount.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JN-09

- [ ] **Code:** **Question:** What does `kubectl get events -A --sort-by=.lastTimestamp` help you verify for Kubernetes troubleshooting and kubectl?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: identify which manager owns or overwrites a field.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JN-10

- [ ] **Code:** **Question:** What does `kubectl cluster-info dump --output-directory=./dump` help you verify for Kubernetes troubleshooting and kubectl?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: repair Git/Helm/operator/IaC after any imperative mitigation.

## Junior — procedural and command questions

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JP-01

- [ ] **Code:** **Question:** A basic Object status/conditions check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. observedGeneration, reason and message show controller interpretation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JP-02

- [ ] **Question:** A basic Events check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs POD -n NS --all-containers --previous` and capture exact status/reason/request ID. scheduling, pull, mount, probe and controller records point to the first failing transition. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JP-03

- [ ] **Question:** A basic Previous logs check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` and capture exact status/reason/request ID. retrieve terminated container output during CrashLoopBackOff. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JP-04

- [ ] **Code:** **Question:** A basic Ephemeral debug check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. add diagnostic tooling without rebuilding the production image. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JP-05

- [ ] **Question:** A basic Raw API/jsonpath/jq check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl cluster-info dump --output-directory=./dump` and capture exact status/reason/request ID. inspect exact fields and aggregated status rather than visually scanning YAML. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JP-06

- [ ] **Question:** A basic Node debug check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. enter host namespaces/filesystem carefully for kubelet/runtime/CNI evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JP-07

- [ ] **Code:** **Question:** A basic EndpointSlice check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs POD -n NS --all-containers --previous` and capture exact status/reason/request ID. confirms whether readiness/selector produced routable Service targets. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JP-08

- [ ] **Question:** A basic VolumeAttachment/CSI logs check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` and capture exact status/reason/request ID. separate scheduler topology from controller attach and node mount. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JP-09

- [ ] **Question:** A basic Managed fields check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. identify which manager owns or overwrites a field. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-JP-10

- [ ] **Code:** **Question:** A basic Source reconciliation check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl cluster-info dump --output-directory=./dump` and capture exact status/reason/request ID. repair Git/Helm/operator/IaC after any imperative mitigation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MN-01

- [ ] **Question:** Compare Object status/conditions with Events. When would each change your design?

**Answer:** Object status/conditions: observedGeneration, reason and message show controller interpretation. Events: scheduling, pull, mount, probe and controller records point to the first failing transition. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MN-02

- [ ] **Question:** Compare Events with Previous logs. When would each change your design?

**Answer:** Events: scheduling, pull, mount, probe and controller records point to the first failing transition. Previous logs: retrieve terminated container output during CrashLoopBackOff. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MN-03

- [ ] **Question:** Compare Previous logs with Ephemeral debug. When would each change your design?

**Answer:** Previous logs: retrieve terminated container output during CrashLoopBackOff. Ephemeral debug: add diagnostic tooling without rebuilding the production image. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MN-04

- [ ] **Configuration review:** **Question:** Compare Ephemeral debug with Raw API/jsonpath/jq. When would each change your design?

**Answer:** Ephemeral debug: add diagnostic tooling without rebuilding the production image. Raw API/jsonpath/jq: inspect exact fields and aggregated status rather than visually scanning YAML. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MN-05

- [ ] **Question:** Compare Raw API/jsonpath/jq with Node debug. When would each change your design?

**Answer:** Raw API/jsonpath/jq: inspect exact fields and aggregated status rather than visually scanning YAML. Node debug: enter host namespaces/filesystem carefully for kubelet/runtime/CNI evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MN-06

- [ ] **Question:** Compare Node debug with EndpointSlice. When would each change your design?

**Answer:** Node debug: enter host namespaces/filesystem carefully for kubelet/runtime/CNI evidence. EndpointSlice: confirms whether readiness/selector produced routable Service targets. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MN-07

- [ ] **Configuration review:** **Question:** Compare EndpointSlice with VolumeAttachment/CSI logs. When would each change your design?

**Answer:** EndpointSlice: confirms whether readiness/selector produced routable Service targets. VolumeAttachment/CSI logs: separate scheduler topology from controller attach and node mount. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MN-08

- [ ] **Question:** Compare VolumeAttachment/CSI logs with Managed fields. When would each change your design?

**Answer:** VolumeAttachment/CSI logs: separate scheduler topology from controller attach and node mount. Managed fields: identify which manager owns or overwrites a field. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MN-09

- [ ] **Question:** Compare Managed fields with Source reconciliation. When would each change your design?

**Answer:** Managed fields: identify which manager owns or overwrites a field. Source reconciliation: repair Git/Helm/operator/IaC after any imperative mitigation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MN-10

- [ ] **Configuration review:** **Question:** Compare Source reconciliation with Object status/conditions. When would each change your design?

**Answer:** Source reconciliation: repair Git/Helm/operator/IaC after any imperative mitigation. Object status/conditions: observedGeneration, reason and message show controller interpretation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Object status/conditions; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. observedGeneration, reason and message show controller interpretation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MP-02

- [ ] **Question:** Production is degraded around Events; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs POD -n NS --all-containers --previous` plus recent events/changes, then correlate the service-specific SLI. scheduling, pull, mount, probe and controller records point to the first failing transition. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Previous logs; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` plus recent events/changes, then correlate the service-specific SLI. retrieve terminated container output during CrashLoopBackOff. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MP-04

- [ ] **Question:** Production is degraded around Ephemeral debug; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. add diagnostic tooling without rebuilding the production image. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Raw API/jsonpath/jq; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl cluster-info dump --output-directory=./dump` plus recent events/changes, then correlate the service-specific SLI. inspect exact fields and aggregated status rather than visually scanning YAML. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MP-06

- [ ] **Question:** Production is degraded around Node debug; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. enter host namespaces/filesystem carefully for kubelet/runtime/CNI evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around EndpointSlice; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs POD -n NS --all-containers --previous` plus recent events/changes, then correlate the service-specific SLI. confirms whether readiness/selector produced routable Service targets. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MP-08

- [ ] **Question:** Production is degraded around VolumeAttachment/CSI logs; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` plus recent events/changes, then correlate the service-specific SLI. separate scheduler topology from controller attach and node mount. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Managed fields; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. identify which manager owns or overwrites a field. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-MP-10

- [ ] **Question:** Production is degraded around Source reconciliation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl cluster-info dump --output-directory=./dump` plus recent events/changes, then correlate the service-specific SLI. repair Git/Helm/operator/IaC after any imperative mitigation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SN-01

- [ ] **Question:** Design a production Kubernetes troubleshooting and kubectl capability where Object status/conditions, Ephemeral debug and EndpointSlice are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: observedGeneration, reason and message show controller interpretation. add diagnostic tooling without rebuilding the production image. confirms whether readiness/selector produced routable Service targets. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes troubleshooting and kubectl capability where Events, Raw API/jsonpath/jq and VolumeAttachment/CSI logs are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scheduling, pull, mount, probe and controller records point to the first failing transition. inspect exact fields and aggregated status rather than visually scanning YAML. separate scheduler topology from controller attach and node mount. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SN-03

- [ ] **Question:** Design a production Kubernetes troubleshooting and kubectl capability where Previous logs, Node debug and Managed fields are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retrieve terminated container output during CrashLoopBackOff. enter host namespaces/filesystem carefully for kubelet/runtime/CNI evidence. identify which manager owns or overwrites a field. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes troubleshooting and kubectl capability where Ephemeral debug, EndpointSlice and Source reconciliation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: add diagnostic tooling without rebuilding the production image. confirms whether readiness/selector produced routable Service targets. repair Git/Helm/operator/IaC after any imperative mitigation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SN-05

- [ ] **Question:** Design a production Kubernetes troubleshooting and kubectl capability where Raw API/jsonpath/jq, VolumeAttachment/CSI logs and Object status/conditions are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: inspect exact fields and aggregated status rather than visually scanning YAML. separate scheduler topology from controller attach and node mount. observedGeneration, reason and message show controller interpretation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes troubleshooting and kubectl capability where Node debug, Managed fields and Events are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: enter host namespaces/filesystem carefully for kubelet/runtime/CNI evidence. identify which manager owns or overwrites a field. scheduling, pull, mount, probe and controller records point to the first failing transition. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SN-07

- [ ] **Question:** Design a production Kubernetes troubleshooting and kubectl capability where EndpointSlice, Source reconciliation and Previous logs are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: confirms whether readiness/selector produced routable Service targets. repair Git/Helm/operator/IaC after any imperative mitigation. retrieve terminated container output during CrashLoopBackOff. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes troubleshooting and kubectl capability where VolumeAttachment/CSI logs, Object status/conditions and Ephemeral debug are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: separate scheduler topology from controller attach and node mount. observedGeneration, reason and message show controller interpretation. add diagnostic tooling without rebuilding the production image. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SN-09

- [ ] **Question:** Design a production Kubernetes troubleshooting and kubectl capability where Managed fields, Events and Raw API/jsonpath/jq are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: identify which manager owns or overwrites a field. scheduling, pull, mount, probe and controller records point to the first failing transition. inspect exact fields and aggregated status rather than visually scanning YAML. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes troubleshooting and kubectl capability where Source reconciliation, Previous logs and Node debug are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: repair Git/Helm/operator/IaC after any imperative mitigation. retrieve terminated container output during CrashLoopBackOff. enter host namespaces/filesystem carefully for kubelet/runtime/CNI evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Object status/conditions. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. observedGeneration, reason and message show controller interpretation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Events. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs POD -n NS --all-containers --previous` as one read-only checkpoint, not the whole diagnosis. scheduling, pull, mount, probe and controller records point to the first failing transition. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Previous logs. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` as one read-only checkpoint, not the whole diagnosis. retrieve terminated container output during CrashLoopBackOff. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ephemeral debug. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. add diagnostic tooling without rebuilding the production image. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Raw API/jsonpath/jq. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl cluster-info dump --output-directory=./dump` as one read-only checkpoint, not the whole diagnosis. inspect exact fields and aggregated status rather than visually scanning YAML. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node debug. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. enter host namespaces/filesystem carefully for kubelet/runtime/CNI evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving EndpointSlice. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs POD -n NS --all-containers --previous` as one read-only checkpoint, not the whole diagnosis. confirms whether readiness/selector produced routable Service targets. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VolumeAttachment/CSI logs. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER` as one read-only checkpoint, not the whole diagnosis. separate scheduler topology from controller attach and node mount. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Managed fields. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. identify which manager owns or overwrites a field. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-TROUBLESHOOTING-AND-KUBECTL-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Source reconciliation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl cluster-info dump --output-directory=./dump` as one read-only checkpoint, not the whole diagnosis. repair Git/Helm/operator/IaC after any imperative mitigation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
