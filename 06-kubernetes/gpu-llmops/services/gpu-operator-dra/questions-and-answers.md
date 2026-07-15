# GPU Operator, device plugins and DRA — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JN-01

- [ ] **Question:** What is Driver, and why does it matter in GPU Operator, device plugins and DRA?

**Answer:** host kernel module/firmware is the foundation and must match hardware/kernel/runtime. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JN-02

- [ ] **Question:** What is Container toolkit, and why does it matter in GPU Operator, device plugins and DRA?

**Answer:** injects device/library/runtime configuration into GPU containers. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JN-03

- [ ] **Question:** What is Device plugin, and why does it matter in GPU Operator, device plugins and DRA?

**Answer:** advertises integer extended resources and allocates device nodes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JN-04

- [ ] **Question:** What is GPU Feature Discovery, and why does it matter in GPU Operator, device plugins and DRA?

**Answer:** labels node hardware/capabilities for scheduling policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JN-05

- [ ] **Question:** What is GPU Operator, and why does it matter in GPU Operator, device plugins and DRA?

**Answer:** reconciles driver/toolkit/plugin/GFD/DCGM/MIG components under one version matrix. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JN-06

- [ ] **Question:** What is DRA ResourceSlice, and why does it matter in GPU Operator, device plugins and DRA?

**Answer:** driver publishes device inventory/attributes/topology. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JN-07

- [ ] **Question:** What is DeviceClass, and why does it matter in GPU Operator, device plugins and DRA?

**Answer:** admin policy selects device characteristics using CEL. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JN-08

- [ ] **Code:** **Question:** What does `kubectl exec -n ai POD -- nvidia-smi` help you verify for GPU Operator, device plugins and DRA?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: workload requests and records allocated/prepared device.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JN-09

- [ ] **Code:** **Question:** What does `kubectl get pods -n gpu-operator -o wide` help you verify for GPU Operator, device plugins and DRA?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: unhealthy device reduces future allocatable or reports claim/Pod status under mechanism.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JN-10

- [ ] **Code:** **Question:** What does `kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'` help you verify for GPU Operator, device plugins and DRA?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: drain one pool, update driver/operator/runtime, qualify CUDA/NCCL/model then expand.

## Junior — procedural and command questions

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JP-01

- [ ] **Code:** **Question:** A basic Driver check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -n gpu-operator -o wide` and capture exact status/reason/request ID. host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JP-02

- [ ] **Question:** A basic Container toolkit check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'` and capture exact status/reason/request ID. injects device/library/runtime configuration into GPU containers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JP-03

- [ ] **Question:** A basic Device plugin check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get deviceclass,resourceslice,resourceclaim -A` and capture exact status/reason/request ID. advertises integer extended resources and allocates device nodes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JP-04

- [ ] **Code:** **Question:** A basic GPU Feature Discovery check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl exec -n ai POD -- nvidia-smi` and capture exact status/reason/request ID. labels node hardware/capabilities for scheduling policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JP-05

- [ ] **Question:** A basic GPU Operator check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -n gpu-operator -o wide` and capture exact status/reason/request ID. reconciles driver/toolkit/plugin/GFD/DCGM/MIG components under one version matrix. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JP-06

- [ ] **Question:** A basic DRA ResourceSlice check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'` and capture exact status/reason/request ID. driver publishes device inventory/attributes/topology. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JP-07

- [ ] **Code:** **Question:** A basic DeviceClass check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get deviceclass,resourceslice,resourceclaim -A` and capture exact status/reason/request ID. admin policy selects device characteristics using CEL. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JP-08

- [ ] **Question:** A basic ResourceClaim check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl exec -n ai POD -- nvidia-smi` and capture exact status/reason/request ID. workload requests and records allocated/prepared device. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JP-09

- [ ] **Question:** A basic Device health check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -n gpu-operator -o wide` and capture exact status/reason/request ID. unhealthy device reduces future allocatable or reports claim/Pod status under mechanism. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-JP-10

- [ ] **Code:** **Question:** A basic Canary upgrade check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'` and capture exact status/reason/request ID. drain one pool, update driver/operator/runtime, qualify CUDA/NCCL/model then expand. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MN-01

- [ ] **Question:** Compare Driver with Container toolkit. When would each change your design?

**Answer:** Driver: host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Container toolkit: injects device/library/runtime configuration into GPU containers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MN-02

- [ ] **Question:** Compare Container toolkit with Device plugin. When would each change your design?

**Answer:** Container toolkit: injects device/library/runtime configuration into GPU containers. Device plugin: advertises integer extended resources and allocates device nodes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MN-03

- [ ] **Question:** Compare Device plugin with GPU Feature Discovery. When would each change your design?

**Answer:** Device plugin: advertises integer extended resources and allocates device nodes. GPU Feature Discovery: labels node hardware/capabilities for scheduling policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MN-04

- [ ] **Configuration review:** **Question:** Compare GPU Feature Discovery with GPU Operator. When would each change your design?

**Answer:** GPU Feature Discovery: labels node hardware/capabilities for scheduling policy. GPU Operator: reconciles driver/toolkit/plugin/GFD/DCGM/MIG components under one version matrix. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MN-05

- [ ] **Question:** Compare GPU Operator with DRA ResourceSlice. When would each change your design?

**Answer:** GPU Operator: reconciles driver/toolkit/plugin/GFD/DCGM/MIG components under one version matrix. DRA ResourceSlice: driver publishes device inventory/attributes/topology. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MN-06

- [ ] **Question:** Compare DRA ResourceSlice with DeviceClass. When would each change your design?

**Answer:** DRA ResourceSlice: driver publishes device inventory/attributes/topology. DeviceClass: admin policy selects device characteristics using CEL. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MN-07

- [ ] **Configuration review:** **Question:** Compare DeviceClass with ResourceClaim. When would each change your design?

**Answer:** DeviceClass: admin policy selects device characteristics using CEL. ResourceClaim: workload requests and records allocated/prepared device. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MN-08

- [ ] **Question:** Compare ResourceClaim with Device health. When would each change your design?

**Answer:** ResourceClaim: workload requests and records allocated/prepared device. Device health: unhealthy device reduces future allocatable or reports claim/Pod status under mechanism. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MN-09

- [ ] **Question:** Compare Device health with Canary upgrade. When would each change your design?

**Answer:** Device health: unhealthy device reduces future allocatable or reports claim/Pod status under mechanism. Canary upgrade: drain one pool, update driver/operator/runtime, qualify CUDA/NCCL/model then expand. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MN-10

- [ ] **Configuration review:** **Question:** Compare Canary upgrade with Driver. When would each change your design?

**Answer:** Canary upgrade: drain one pool, update driver/operator/runtime, qualify CUDA/NCCL/model then expand. Driver: host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Driver; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -n gpu-operator -o wide` plus recent events/changes, then correlate the service-specific SLI. host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MP-02

- [ ] **Question:** Production is degraded around Container toolkit; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'` plus recent events/changes, then correlate the service-specific SLI. injects device/library/runtime configuration into GPU containers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Device plugin; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get deviceclass,resourceslice,resourceclaim -A` plus recent events/changes, then correlate the service-specific SLI. advertises integer extended resources and allocates device nodes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MP-04

- [ ] **Question:** Production is degraded around GPU Feature Discovery; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl exec -n ai POD -- nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. labels node hardware/capabilities for scheduling policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around GPU Operator; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -n gpu-operator -o wide` plus recent events/changes, then correlate the service-specific SLI. reconciles driver/toolkit/plugin/GFD/DCGM/MIG components under one version matrix. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MP-06

- [ ] **Question:** Production is degraded around DRA ResourceSlice; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'` plus recent events/changes, then correlate the service-specific SLI. driver publishes device inventory/attributes/topology. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around DeviceClass; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get deviceclass,resourceslice,resourceclaim -A` plus recent events/changes, then correlate the service-specific SLI. admin policy selects device characteristics using CEL. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MP-08

- [ ] **Question:** Production is degraded around ResourceClaim; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl exec -n ai POD -- nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. workload requests and records allocated/prepared device. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Device health; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -n gpu-operator -o wide` plus recent events/changes, then correlate the service-specific SLI. unhealthy device reduces future allocatable or reports claim/Pod status under mechanism. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-MP-10

- [ ] **Question:** Production is degraded around Canary upgrade; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'` plus recent events/changes, then correlate the service-specific SLI. drain one pool, update driver/operator/runtime, qualify CUDA/NCCL/model then expand. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SN-01

- [ ] **Question:** Design a production GPU Operator, device plugins and DRA capability where Driver, GPU Feature Discovery and DeviceClass are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: host kernel module/firmware is the foundation and must match hardware/kernel/runtime. labels node hardware/capabilities for scheduling policy. admin policy selects device characteristics using CEL. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production GPU Operator, device plugins and DRA capability where Container toolkit, GPU Operator and ResourceClaim are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: injects device/library/runtime configuration into GPU containers. reconciles driver/toolkit/plugin/GFD/DCGM/MIG components under one version matrix. workload requests and records allocated/prepared device. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SN-03

- [ ] **Question:** Design a production GPU Operator, device plugins and DRA capability where Device plugin, DRA ResourceSlice and Device health are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: advertises integer extended resources and allocates device nodes. driver publishes device inventory/attributes/topology. unhealthy device reduces future allocatable or reports claim/Pod status under mechanism. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production GPU Operator, device plugins and DRA capability where GPU Feature Discovery, DeviceClass and Canary upgrade are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: labels node hardware/capabilities for scheduling policy. admin policy selects device characteristics using CEL. drain one pool, update driver/operator/runtime, qualify CUDA/NCCL/model then expand. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SN-05

- [ ] **Question:** Design a production GPU Operator, device plugins and DRA capability where GPU Operator, ResourceClaim and Driver are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reconciles driver/toolkit/plugin/GFD/DCGM/MIG components under one version matrix. workload requests and records allocated/prepared device. host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production GPU Operator, device plugins and DRA capability where DRA ResourceSlice, Device health and Container toolkit are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: driver publishes device inventory/attributes/topology. unhealthy device reduces future allocatable or reports claim/Pod status under mechanism. injects device/library/runtime configuration into GPU containers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SN-07

- [ ] **Question:** Design a production GPU Operator, device plugins and DRA capability where DeviceClass, Canary upgrade and Device plugin are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: admin policy selects device characteristics using CEL. drain one pool, update driver/operator/runtime, qualify CUDA/NCCL/model then expand. advertises integer extended resources and allocates device nodes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production GPU Operator, device plugins and DRA capability where ResourceClaim, Driver and GPU Feature Discovery are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: workload requests and records allocated/prepared device. host kernel module/firmware is the foundation and must match hardware/kernel/runtime. labels node hardware/capabilities for scheduling policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SN-09

- [ ] **Question:** Design a production GPU Operator, device plugins and DRA capability where Device health, Container toolkit and GPU Operator are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: unhealthy device reduces future allocatable or reports claim/Pod status under mechanism. injects device/library/runtime configuration into GPU containers. reconciles driver/toolkit/plugin/GFD/DCGM/MIG components under one version matrix. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production GPU Operator, device plugins and DRA capability where Canary upgrade, Device plugin and DRA ResourceSlice are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: drain one pool, update driver/operator/runtime, qualify CUDA/NCCL/model then expand. advertises integer extended resources and allocates device nodes. driver publishes device inventory/attributes/topology. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Driver. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -n gpu-operator -o wide` as one read-only checkpoint, not the whole diagnosis. host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Container toolkit. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'` as one read-only checkpoint, not the whole diagnosis. injects device/library/runtime configuration into GPU containers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Device plugin. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get deviceclass,resourceslice,resourceclaim -A` as one read-only checkpoint, not the whole diagnosis. advertises integer extended resources and allocates device nodes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU Feature Discovery. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl exec -n ai POD -- nvidia-smi` as one read-only checkpoint, not the whole diagnosis. labels node hardware/capabilities for scheduling policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU Operator. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -n gpu-operator -o wide` as one read-only checkpoint, not the whole diagnosis. reconciles driver/toolkit/plugin/GFD/DCGM/MIG components under one version matrix. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DRA ResourceSlice. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'` as one read-only checkpoint, not the whole diagnosis. driver publishes device inventory/attributes/topology. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DeviceClass. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get deviceclass,resourceslice,resourceclaim -A` as one read-only checkpoint, not the whole diagnosis. admin policy selects device characteristics using CEL. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ResourceClaim. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl exec -n ai POD -- nvidia-smi` as one read-only checkpoint, not the whole diagnosis. workload requests and records allocated/prepared device. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Device health. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -n gpu-operator -o wide` as one read-only checkpoint, not the whole diagnosis. unhealthy device reduces future allocatable or reports claim/Pod status under mechanism. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-OPERATOR-DEVICE-PLUGINS-AND-DRA-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Canary upgrade. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'` as one read-only checkpoint, not the whole diagnosis. drain one pool, update driver/operator/runtime, qualify CUDA/NCCL/model then expand. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
