# Training platform operations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### TRAINING-PLATFORM-OPERATIONS-JN-01

- [ ] **Question:** What is Training job spec, and why does it matter in Training platform operations?

**Answer:** image/digest, command, data, config, resources, topology, identity, timeout and outputs are immutable inputs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-PLATFORM-OPERATIONS-JN-02

- [ ] **Question:** What is Workspace, and why does it matter in Training platform operations?

**Answer:** ephemeral code/scratch is separated from durable datasets/checkpoints/artifacts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-PLATFORM-OPERATIONS-JN-03

- [ ] **Question:** What is Queue/admission, and why does it matter in Training platform operations?

**Answer:** cohort quota, priority, fairness and flavor/topology assignment control scarce accelerators. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-PLATFORM-OPERATIONS-JN-04

- [ ] **Question:** What is Node compatibility, and why does it matter in Training platform operations?

**Answer:** GPU/driver/runtime/framework/network/storage versions are qualified together. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-PLATFORM-OPERATIONS-JN-05

- [ ] **Question:** What is Checkpoint, and why does it matter in Training platform operations?

**Answer:** atomic versioned state includes model/optimizer/scheduler/RNG/progress and is tested for resume. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-PLATFORM-OPERATIONS-JN-06

- [ ] **Question:** What is Spot/preemption, and why does it matter in Training platform operations?

**Answer:** checkpoint interval and restart overhead determine whether discounted capacity saves money. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-PLATFORM-OPERATIONS-JN-07

- [ ] **Question:** What is Data loading, and why does it matter in Training platform operations?

**Answer:** sharding, prefetch, cache and worker counts can bottleneck GPUs or overload shared storage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-PLATFORM-OPERATIONS-JN-08

- [ ] **Code:** **Question:** What does `nvidia-smi dmon -s pucvmet` help you verify for Training platform operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: untrusted training code, dataset credentials, host devices and outbound network form a high-risk boundary.

### TRAINING-PLATFORM-OPERATIONS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get trainingjobs,jobs,pods -A -o wide` help you verify for Training platform operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: loss/quality plus step time, samples/tokens per second, GPU, network, I/O and cost reveal goodput.

### TRAINING-PLATFORM-OPERATIONS-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe pod POD -n NS` help you verify for Training platform operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: successful/failed/canceled jobs reconcile pods, disks, IPs, checkpoints, logs and retained evidence.

## Junior — procedural and command questions

### TRAINING-PLATFORM-OPERATIONS-JP-01

- [ ] **Code:** **Question:** A basic Training job spec check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get trainingjobs,jobs,pods -A -o wide` and capture exact status/reason/request ID. image/digest, command, data, config, resources, topology, identity, timeout and outputs are immutable inputs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-PLATFORM-OPERATIONS-JP-02

- [ ] **Question:** A basic Workspace check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. ephemeral code/scratch is separated from durable datasets/checkpoints/artifacts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-PLATFORM-OPERATIONS-JP-03

- [ ] **Question:** A basic Queue/admission check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs POD -n NS --all-containers --since=30m` and capture exact status/reason/request ID. cohort quota, priority, fairness and flavor/topology assignment control scarce accelerators. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-PLATFORM-OPERATIONS-JP-04

- [ ] **Code:** **Question:** A basic Node compatibility check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi dmon -s pucvmet` and capture exact status/reason/request ID. GPU/driver/runtime/framework/network/storage versions are qualified together. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-PLATFORM-OPERATIONS-JP-05

- [ ] **Question:** A basic Checkpoint check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get trainingjobs,jobs,pods -A -o wide` and capture exact status/reason/request ID. atomic versioned state includes model/optimizer/scheduler/RNG/progress and is tested for resume. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-PLATFORM-OPERATIONS-JP-06

- [ ] **Question:** A basic Spot/preemption check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. checkpoint interval and restart overhead determine whether discounted capacity saves money. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-PLATFORM-OPERATIONS-JP-07

- [ ] **Code:** **Question:** A basic Data loading check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs POD -n NS --all-containers --since=30m` and capture exact status/reason/request ID. sharding, prefetch, cache and worker counts can bottleneck GPUs or overload shared storage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-PLATFORM-OPERATIONS-JP-08

- [ ] **Question:** A basic Isolation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi dmon -s pucvmet` and capture exact status/reason/request ID. untrusted training code, dataset credentials, host devices and outbound network form a high-risk boundary. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-PLATFORM-OPERATIONS-JP-09

- [ ] **Question:** A basic Training telemetry check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get trainingjobs,jobs,pods -A -o wide` and capture exact status/reason/request ID. loss/quality plus step time, samples/tokens per second, GPU, network, I/O and cost reveal goodput. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-PLATFORM-OPERATIONS-JP-10

- [ ] **Code:** **Question:** A basic Cleanup check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS` and capture exact status/reason/request ID. successful/failed/canceled jobs reconcile pods, disks, IPs, checkpoints, logs and retained evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### TRAINING-PLATFORM-OPERATIONS-MN-01

- [ ] **Question:** Compare Training job spec with Workspace. When would each change your design?

**Answer:** Training job spec: image/digest, command, data, config, resources, topology, identity, timeout and outputs are immutable inputs. Workspace: ephemeral code/scratch is separated from durable datasets/checkpoints/artifacts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-PLATFORM-OPERATIONS-MN-02

- [ ] **Question:** Compare Workspace with Queue/admission. When would each change your design?

**Answer:** Workspace: ephemeral code/scratch is separated from durable datasets/checkpoints/artifacts. Queue/admission: cohort quota, priority, fairness and flavor/topology assignment control scarce accelerators. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-PLATFORM-OPERATIONS-MN-03

- [ ] **Question:** Compare Queue/admission with Node compatibility. When would each change your design?

**Answer:** Queue/admission: cohort quota, priority, fairness and flavor/topology assignment control scarce accelerators. Node compatibility: GPU/driver/runtime/framework/network/storage versions are qualified together. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-PLATFORM-OPERATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Node compatibility with Checkpoint. When would each change your design?

**Answer:** Node compatibility: GPU/driver/runtime/framework/network/storage versions are qualified together. Checkpoint: atomic versioned state includes model/optimizer/scheduler/RNG/progress and is tested for resume. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-PLATFORM-OPERATIONS-MN-05

- [ ] **Question:** Compare Checkpoint with Spot/preemption. When would each change your design?

**Answer:** Checkpoint: atomic versioned state includes model/optimizer/scheduler/RNG/progress and is tested for resume. Spot/preemption: checkpoint interval and restart overhead determine whether discounted capacity saves money. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-PLATFORM-OPERATIONS-MN-06

- [ ] **Question:** Compare Spot/preemption with Data loading. When would each change your design?

**Answer:** Spot/preemption: checkpoint interval and restart overhead determine whether discounted capacity saves money. Data loading: sharding, prefetch, cache and worker counts can bottleneck GPUs or overload shared storage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-PLATFORM-OPERATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Data loading with Isolation. When would each change your design?

**Answer:** Data loading: sharding, prefetch, cache and worker counts can bottleneck GPUs or overload shared storage. Isolation: untrusted training code, dataset credentials, host devices and outbound network form a high-risk boundary. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-PLATFORM-OPERATIONS-MN-08

- [ ] **Question:** Compare Isolation with Training telemetry. When would each change your design?

**Answer:** Isolation: untrusted training code, dataset credentials, host devices and outbound network form a high-risk boundary. Training telemetry: loss/quality plus step time, samples/tokens per second, GPU, network, I/O and cost reveal goodput. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-PLATFORM-OPERATIONS-MN-09

- [ ] **Question:** Compare Training telemetry with Cleanup. When would each change your design?

**Answer:** Training telemetry: loss/quality plus step time, samples/tokens per second, GPU, network, I/O and cost reveal goodput. Cleanup: successful/failed/canceled jobs reconcile pods, disks, IPs, checkpoints, logs and retained evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-PLATFORM-OPERATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Cleanup with Training job spec. When would each change your design?

**Answer:** Cleanup: successful/failed/canceled jobs reconcile pods, disks, IPs, checkpoints, logs and retained evidence. Training job spec: image/digest, command, data, config, resources, topology, identity, timeout and outputs are immutable inputs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### TRAINING-PLATFORM-OPERATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Training job spec; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get trainingjobs,jobs,pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. image/digest, command, data, config, resources, topology, identity, timeout and outputs are immutable inputs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-PLATFORM-OPERATIONS-MP-02

- [ ] **Question:** Production is degraded around Workspace; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. ephemeral code/scratch is separated from durable datasets/checkpoints/artifacts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-PLATFORM-OPERATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Queue/admission; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs POD -n NS --all-containers --since=30m` plus recent events/changes, then correlate the service-specific SLI. cohort quota, priority, fairness and flavor/topology assignment control scarce accelerators. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-PLATFORM-OPERATIONS-MP-04

- [ ] **Question:** Production is degraded around Node compatibility; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi dmon -s pucvmet` plus recent events/changes, then correlate the service-specific SLI. GPU/driver/runtime/framework/network/storage versions are qualified together. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-PLATFORM-OPERATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Checkpoint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get trainingjobs,jobs,pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. atomic versioned state includes model/optimizer/scheduler/RNG/progress and is tested for resume. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-PLATFORM-OPERATIONS-MP-06

- [ ] **Question:** Production is degraded around Spot/preemption; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. checkpoint interval and restart overhead determine whether discounted capacity saves money. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-PLATFORM-OPERATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Data loading; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs POD -n NS --all-containers --since=30m` plus recent events/changes, then correlate the service-specific SLI. sharding, prefetch, cache and worker counts can bottleneck GPUs or overload shared storage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-PLATFORM-OPERATIONS-MP-08

- [ ] **Question:** Production is degraded around Isolation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi dmon -s pucvmet` plus recent events/changes, then correlate the service-specific SLI. untrusted training code, dataset credentials, host devices and outbound network form a high-risk boundary. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-PLATFORM-OPERATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Training telemetry; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get trainingjobs,jobs,pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. loss/quality plus step time, samples/tokens per second, GPU, network, I/O and cost reveal goodput. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-PLATFORM-OPERATIONS-MP-10

- [ ] **Question:** Production is degraded around Cleanup; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS` plus recent events/changes, then correlate the service-specific SLI. successful/failed/canceled jobs reconcile pods, disks, IPs, checkpoints, logs and retained evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### TRAINING-PLATFORM-OPERATIONS-SN-01

- [ ] **Question:** Design a production Training platform operations capability where Training job spec, Node compatibility and Data loading are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: image/digest, command, data, config, resources, topology, identity, timeout and outputs are immutable inputs. GPU/driver/runtime/framework/network/storage versions are qualified together. sharding, prefetch, cache and worker counts can bottleneck GPUs or overload shared storage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-PLATFORM-OPERATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Training platform operations capability where Workspace, Checkpoint and Isolation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ephemeral code/scratch is separated from durable datasets/checkpoints/artifacts. atomic versioned state includes model/optimizer/scheduler/RNG/progress and is tested for resume. untrusted training code, dataset credentials, host devices and outbound network form a high-risk boundary. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-PLATFORM-OPERATIONS-SN-03

- [ ] **Question:** Design a production Training platform operations capability where Queue/admission, Spot/preemption and Training telemetry are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cohort quota, priority, fairness and flavor/topology assignment control scarce accelerators. checkpoint interval and restart overhead determine whether discounted capacity saves money. loss/quality plus step time, samples/tokens per second, GPU, network, I/O and cost reveal goodput. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-PLATFORM-OPERATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Training platform operations capability where Node compatibility, Data loading and Cleanup are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: GPU/driver/runtime/framework/network/storage versions are qualified together. sharding, prefetch, cache and worker counts can bottleneck GPUs or overload shared storage. successful/failed/canceled jobs reconcile pods, disks, IPs, checkpoints, logs and retained evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-PLATFORM-OPERATIONS-SN-05

- [ ] **Question:** Design a production Training platform operations capability where Checkpoint, Isolation and Training job spec are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: atomic versioned state includes model/optimizer/scheduler/RNG/progress and is tested for resume. untrusted training code, dataset credentials, host devices and outbound network form a high-risk boundary. image/digest, command, data, config, resources, topology, identity, timeout and outputs are immutable inputs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-PLATFORM-OPERATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Training platform operations capability where Spot/preemption, Training telemetry and Workspace are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: checkpoint interval and restart overhead determine whether discounted capacity saves money. loss/quality plus step time, samples/tokens per second, GPU, network, I/O and cost reveal goodput. ephemeral code/scratch is separated from durable datasets/checkpoints/artifacts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-PLATFORM-OPERATIONS-SN-07

- [ ] **Question:** Design a production Training platform operations capability where Data loading, Cleanup and Queue/admission are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: sharding, prefetch, cache and worker counts can bottleneck GPUs or overload shared storage. successful/failed/canceled jobs reconcile pods, disks, IPs, checkpoints, logs and retained evidence. cohort quota, priority, fairness and flavor/topology assignment control scarce accelerators. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-PLATFORM-OPERATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Training platform operations capability where Isolation, Training job spec and Node compatibility are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: untrusted training code, dataset credentials, host devices and outbound network form a high-risk boundary. image/digest, command, data, config, resources, topology, identity, timeout and outputs are immutable inputs. GPU/driver/runtime/framework/network/storage versions are qualified together. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-PLATFORM-OPERATIONS-SN-09

- [ ] **Question:** Design a production Training platform operations capability where Training telemetry, Workspace and Checkpoint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: loss/quality plus step time, samples/tokens per second, GPU, network, I/O and cost reveal goodput. ephemeral code/scratch is separated from durable datasets/checkpoints/artifacts. atomic versioned state includes model/optimizer/scheduler/RNG/progress and is tested for resume. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-PLATFORM-OPERATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Training platform operations capability where Cleanup, Queue/admission and Spot/preemption are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: successful/failed/canceled jobs reconcile pods, disks, IPs, checkpoints, logs and retained evidence. cohort quota, priority, fairness and flavor/topology assignment control scarce accelerators. checkpoint interval and restart overhead determine whether discounted capacity saves money. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### TRAINING-PLATFORM-OPERATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Training job spec. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get trainingjobs,jobs,pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. image/digest, command, data, config, resources, topology, identity, timeout and outputs are immutable inputs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-PLATFORM-OPERATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Workspace. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. ephemeral code/scratch is separated from durable datasets/checkpoints/artifacts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-PLATFORM-OPERATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Queue/admission. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs POD -n NS --all-containers --since=30m` as one read-only checkpoint, not the whole diagnosis. cohort quota, priority, fairness and flavor/topology assignment control scarce accelerators. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-PLATFORM-OPERATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node compatibility. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi dmon -s pucvmet` as one read-only checkpoint, not the whole diagnosis. GPU/driver/runtime/framework/network/storage versions are qualified together. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-PLATFORM-OPERATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Checkpoint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get trainingjobs,jobs,pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. atomic versioned state includes model/optimizer/scheduler/RNG/progress and is tested for resume. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-PLATFORM-OPERATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Spot/preemption. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. checkpoint interval and restart overhead determine whether discounted capacity saves money. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-PLATFORM-OPERATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Data loading. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs POD -n NS --all-containers --since=30m` as one read-only checkpoint, not the whole diagnosis. sharding, prefetch, cache and worker counts can bottleneck GPUs or overload shared storage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-PLATFORM-OPERATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Isolation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi dmon -s pucvmet` as one read-only checkpoint, not the whole diagnosis. untrusted training code, dataset credentials, host devices and outbound network form a high-risk boundary. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-PLATFORM-OPERATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Training telemetry. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get trainingjobs,jobs,pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. loss/quality plus step time, samples/tokens per second, GPU, network, I/O and cost reveal goodput. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-PLATFORM-OPERATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cleanup. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS` as one read-only checkpoint, not the whole diagnosis. successful/failed/canceled jobs reconcile pods, disks, IPs, checkpoints, logs and retained evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
