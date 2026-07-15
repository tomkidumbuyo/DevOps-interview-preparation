# Inference autoscaling and capacity — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### INFERENCE-AUTOSCALING-AND-CAPACITY-JN-01

- [ ] **Question:** What is Queue depth/age, and why does it matter in Inference autoscaling and capacity?

**Answer:** leading overload signal when arrival work exceeds serving goodput. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JN-02

- [ ] **Question:** What is Predicted token work, and why does it matter in Inference autoscaling and capacity?

**Answer:** input/output length estimate better reflects heterogeneous request cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JN-03

- [ ] **Question:** What is TTFT/inter-token, and why does it matter in Inference autoscaling and capacity?

**Answer:** user latency separates queue/prefill from decode behavior. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JN-04

- [ ] **Question:** What is KV cache pressure, and why does it matter in Inference autoscaling and capacity?

**Answer:** memory/concurrency saturation can predict rejection before GPU utilization. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JN-05

- [ ] **Question:** What is HPA/KEDA, and why does it matter in Inference autoscaling and capacity?

**Answer:** scales replicas from custom/external metrics with stabilization and activation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JN-06

- [ ] **Question:** What is Node autoscaler, and why does it matter in Inference autoscaling and capacity?

**Answer:** provisions GPU nodes only after replicas become Pending. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JN-07

- [ ] **Question:** What is Cold path, and why does it matter in Inference autoscaling and capacity?

**Answer:** cloud capacity, boot, driver/plugin, image, model download/load/warm dominate delay. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JN-08

- [ ] **Code:** **Question:** What does `kubectl get pods -A --field-selector=status.phase=Pending` help you verify for Inference autoscaling and capacity?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: preprovisioned nodes/replicas/cache trades cost for burst SLO.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JN-09

- [ ] **Code:** **Question:** What does `kubectl logs -n kube-system deploy/karpenter --since=30m` help you verify for Inference autoscaling and capacity?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: drain streams, protect cache/work, PDB/consolidation and minimum capacity.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JN-10

- [ ] **Code:** **Question:** What does `curl -s http://MODEL/metrics` help you verify for Inference autoscaling and capacity?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: diversified approved hardware/Region/provider requires compatibility/quality/residency tests.

## Junior — procedural and command questions

### INFERENCE-AUTOSCALING-AND-CAPACITY-JP-01

- [ ] **Code:** **Question:** A basic Queue depth/age check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe hpa NAME -n NS` and capture exact status/reason/request ID. leading overload signal when arrival work exceeds serving goodput. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JP-02

- [ ] **Question:** A basic Predicted token work check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get scaledobject -A` and capture exact status/reason/request ID. input/output length estimate better reflects heterogeneous request cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JP-03

- [ ] **Question:** A basic TTFT/inter-token check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A --field-selector=status.phase=Pending` and capture exact status/reason/request ID. user latency separates queue/prefill from decode behavior. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JP-04

- [ ] **Code:** **Question:** A basic KV cache pressure check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/karpenter --since=30m` and capture exact status/reason/request ID. memory/concurrency saturation can predict rejection before GPU utilization. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JP-05

- [ ] **Question:** A basic HPA/KEDA check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. scales replicas from custom/external metrics with stabilization and activation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JP-06

- [ ] **Question:** A basic Node autoscaler check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe hpa NAME -n NS` and capture exact status/reason/request ID. provisions GPU nodes only after replicas become Pending. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JP-07

- [ ] **Code:** **Question:** A basic Cold path check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get scaledobject -A` and capture exact status/reason/request ID. cloud capacity, boot, driver/plugin, image, model download/load/warm dominate delay. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JP-08

- [ ] **Question:** A basic Warm buffer check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A --field-selector=status.phase=Pending` and capture exact status/reason/request ID. preprovisioned nodes/replicas/cache trades cost for burst SLO. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JP-09

- [ ] **Question:** A basic Scale down check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/karpenter --since=30m` and capture exact status/reason/request ID. drain streams, protect cache/work, PDB/consolidation and minimum capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INFERENCE-AUTOSCALING-AND-CAPACITY-JP-10

- [ ] **Code:** **Question:** A basic Capacity fallback check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. diversified approved hardware/Region/provider requires compatibility/quality/residency tests. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### INFERENCE-AUTOSCALING-AND-CAPACITY-MN-01

- [ ] **Question:** Compare Queue depth/age with Predicted token work. When would each change your design?

**Answer:** Queue depth/age: leading overload signal when arrival work exceeds serving goodput. Predicted token work: input/output length estimate better reflects heterogeneous request cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MN-02

- [ ] **Question:** Compare Predicted token work with TTFT/inter-token. When would each change your design?

**Answer:** Predicted token work: input/output length estimate better reflects heterogeneous request cost. TTFT/inter-token: user latency separates queue/prefill from decode behavior. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MN-03

- [ ] **Question:** Compare TTFT/inter-token with KV cache pressure. When would each change your design?

**Answer:** TTFT/inter-token: user latency separates queue/prefill from decode behavior. KV cache pressure: memory/concurrency saturation can predict rejection before GPU utilization. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MN-04

- [ ] **Configuration review:** **Question:** Compare KV cache pressure with HPA/KEDA. When would each change your design?

**Answer:** KV cache pressure: memory/concurrency saturation can predict rejection before GPU utilization. HPA/KEDA: scales replicas from custom/external metrics with stabilization and activation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MN-05

- [ ] **Question:** Compare HPA/KEDA with Node autoscaler. When would each change your design?

**Answer:** HPA/KEDA: scales replicas from custom/external metrics with stabilization and activation. Node autoscaler: provisions GPU nodes only after replicas become Pending. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MN-06

- [ ] **Question:** Compare Node autoscaler with Cold path. When would each change your design?

**Answer:** Node autoscaler: provisions GPU nodes only after replicas become Pending. Cold path: cloud capacity, boot, driver/plugin, image, model download/load/warm dominate delay. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MN-07

- [ ] **Configuration review:** **Question:** Compare Cold path with Warm buffer. When would each change your design?

**Answer:** Cold path: cloud capacity, boot, driver/plugin, image, model download/load/warm dominate delay. Warm buffer: preprovisioned nodes/replicas/cache trades cost for burst SLO. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MN-08

- [ ] **Question:** Compare Warm buffer with Scale down. When would each change your design?

**Answer:** Warm buffer: preprovisioned nodes/replicas/cache trades cost for burst SLO. Scale down: drain streams, protect cache/work, PDB/consolidation and minimum capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MN-09

- [ ] **Question:** Compare Scale down with Capacity fallback. When would each change your design?

**Answer:** Scale down: drain streams, protect cache/work, PDB/consolidation and minimum capacity. Capacity fallback: diversified approved hardware/Region/provider requires compatibility/quality/residency tests. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MN-10

- [ ] **Configuration review:** **Question:** Compare Capacity fallback with Queue depth/age. When would each change your design?

**Answer:** Capacity fallback: diversified approved hardware/Region/provider requires compatibility/quality/residency tests. Queue depth/age: leading overload signal when arrival work exceeds serving goodput. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### INFERENCE-AUTOSCALING-AND-CAPACITY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Queue depth/age; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe hpa NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. leading overload signal when arrival work exceeds serving goodput. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MP-02

- [ ] **Question:** Production is degraded around Predicted token work; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get scaledobject -A` plus recent events/changes, then correlate the service-specific SLI. input/output length estimate better reflects heterogeneous request cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around TTFT/inter-token; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A --field-selector=status.phase=Pending` plus recent events/changes, then correlate the service-specific SLI. user latency separates queue/prefill from decode behavior. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MP-04

- [ ] **Question:** Production is degraded around KV cache pressure; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/karpenter --since=30m` plus recent events/changes, then correlate the service-specific SLI. memory/concurrency saturation can predict rejection before GPU utilization. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around HPA/KEDA; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. scales replicas from custom/external metrics with stabilization and activation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MP-06

- [ ] **Question:** Production is degraded around Node autoscaler; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe hpa NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. provisions GPU nodes only after replicas become Pending. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cold path; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get scaledobject -A` plus recent events/changes, then correlate the service-specific SLI. cloud capacity, boot, driver/plugin, image, model download/load/warm dominate delay. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MP-08

- [ ] **Question:** Production is degraded around Warm buffer; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A --field-selector=status.phase=Pending` plus recent events/changes, then correlate the service-specific SLI. preprovisioned nodes/replicas/cache trades cost for burst SLO. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Scale down; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/karpenter --since=30m` plus recent events/changes, then correlate the service-specific SLI. drain streams, protect cache/work, PDB/consolidation and minimum capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INFERENCE-AUTOSCALING-AND-CAPACITY-MP-10

- [ ] **Question:** Production is degraded around Capacity fallback; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. diversified approved hardware/Region/provider requires compatibility/quality/residency tests. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### INFERENCE-AUTOSCALING-AND-CAPACITY-SN-01

- [ ] **Question:** Design a production Inference autoscaling and capacity capability where Queue depth/age, KV cache pressure and Cold path are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: leading overload signal when arrival work exceeds serving goodput. memory/concurrency saturation can predict rejection before GPU utilization. cloud capacity, boot, driver/plugin, image, model download/load/warm dominate delay. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Inference autoscaling and capacity capability where Predicted token work, HPA/KEDA and Warm buffer are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: input/output length estimate better reflects heterogeneous request cost. scales replicas from custom/external metrics with stabilization and activation. preprovisioned nodes/replicas/cache trades cost for burst SLO. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SN-03

- [ ] **Question:** Design a production Inference autoscaling and capacity capability where TTFT/inter-token, Node autoscaler and Scale down are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: user latency separates queue/prefill from decode behavior. provisions GPU nodes only after replicas become Pending. drain streams, protect cache/work, PDB/consolidation and minimum capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Inference autoscaling and capacity capability where KV cache pressure, Cold path and Capacity fallback are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: memory/concurrency saturation can predict rejection before GPU utilization. cloud capacity, boot, driver/plugin, image, model download/load/warm dominate delay. diversified approved hardware/Region/provider requires compatibility/quality/residency tests. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SN-05

- [ ] **Question:** Design a production Inference autoscaling and capacity capability where HPA/KEDA, Warm buffer and Queue depth/age are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scales replicas from custom/external metrics with stabilization and activation. preprovisioned nodes/replicas/cache trades cost for burst SLO. leading overload signal when arrival work exceeds serving goodput. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Inference autoscaling and capacity capability where Node autoscaler, Scale down and Predicted token work are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: provisions GPU nodes only after replicas become Pending. drain streams, protect cache/work, PDB/consolidation and minimum capacity. input/output length estimate better reflects heterogeneous request cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SN-07

- [ ] **Question:** Design a production Inference autoscaling and capacity capability where Cold path, Capacity fallback and TTFT/inter-token are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cloud capacity, boot, driver/plugin, image, model download/load/warm dominate delay. diversified approved hardware/Region/provider requires compatibility/quality/residency tests. user latency separates queue/prefill from decode behavior. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Inference autoscaling and capacity capability where Warm buffer, Queue depth/age and KV cache pressure are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: preprovisioned nodes/replicas/cache trades cost for burst SLO. leading overload signal when arrival work exceeds serving goodput. memory/concurrency saturation can predict rejection before GPU utilization. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SN-09

- [ ] **Question:** Design a production Inference autoscaling and capacity capability where Scale down, Predicted token work and HPA/KEDA are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: drain streams, protect cache/work, PDB/consolidation and minimum capacity. input/output length estimate better reflects heterogeneous request cost. scales replicas from custom/external metrics with stabilization and activation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Inference autoscaling and capacity capability where Capacity fallback, TTFT/inter-token and Node autoscaler are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: diversified approved hardware/Region/provider requires compatibility/quality/residency tests. user latency separates queue/prefill from decode behavior. provisions GPU nodes only after replicas become Pending. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### INFERENCE-AUTOSCALING-AND-CAPACITY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Queue depth/age. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe hpa NAME -n NS` as one read-only checkpoint, not the whole diagnosis. leading overload signal when arrival work exceeds serving goodput. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Predicted token work. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get scaledobject -A` as one read-only checkpoint, not the whole diagnosis. input/output length estimate better reflects heterogeneous request cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TTFT/inter-token. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A --field-selector=status.phase=Pending` as one read-only checkpoint, not the whole diagnosis. user latency separates queue/prefill from decode behavior. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving KV cache pressure. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/karpenter --since=30m` as one read-only checkpoint, not the whole diagnosis. memory/concurrency saturation can predict rejection before GPU utilization. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving HPA/KEDA. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. scales replicas from custom/external metrics with stabilization and activation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node autoscaler. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe hpa NAME -n NS` as one read-only checkpoint, not the whole diagnosis. provisions GPU nodes only after replicas become Pending. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cold path. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get scaledobject -A` as one read-only checkpoint, not the whole diagnosis. cloud capacity, boot, driver/plugin, image, model download/load/warm dominate delay. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Warm buffer. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A --field-selector=status.phase=Pending` as one read-only checkpoint, not the whole diagnosis. preprovisioned nodes/replicas/cache trades cost for burst SLO. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Scale down. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/karpenter --since=30m` as one read-only checkpoint, not the whole diagnosis. drain streams, protect cache/work, PDB/consolidation and minimum capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INFERENCE-AUTOSCALING-AND-CAPACITY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Capacity fallback. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. diversified approved hardware/Region/provider requires compatibility/quality/residency tests. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
