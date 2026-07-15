# CNI, kube-proxy and eBPF data planes — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JN-01

- [ ] **Question:** What is Kubernetes network model, and why does it matter in CNI, kube-proxy and eBPF data planes?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Pods have cluster-routable IP identity and communicate without required NAT inside the model. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JN-02

- [ ] **Question:** What is CNI plugin, and why does it matter in CNI, kube-proxy and eBPF data planes?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** configures Pod interface, address, route and cleanup when runtime creates sandbox. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JN-03

- [ ] **Question:** What is IPAM, and why does it matter in CNI, kube-proxy and eBPF data planes?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** allocates/reclaims Pod addresses and can exhaust/fragment subnet pools. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JN-04

- [ ] **Question:** What is kube-proxy iptables, and why does it matter in CNI, kube-proxy and eBPF data planes?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** programs probabilistic NAT rules for Services and endpoints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JN-05

- [ ] **Question:** What is kube-proxy IPVS, and why does it matter in CNI, kube-proxy and eBPF data planes?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** uses kernel virtual server tables with separate synchronization. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JN-06

- [ ] **Question:** What is eBPF data plane, and why does it matter in CNI, kube-proxy and eBPF data planes?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** programs kernel hooks/maps for routing, load balancing, policy and observability. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JN-07

- [ ] **Question:** What is Conntrack, and why does it matter in CNI, kube-proxy and eBPF data planes?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** tracks NAT/state and can exhaust or retain stale translations. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JN-08

- [ ] **Code:** **Question:** What does `ip route && ip link` help you verify for CNI, kube-proxy and eBPF data planes?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: encapsulation/cloud path mismatch can drop large packets while probes pass.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JN-09

- [ ] **Code:** **Question:** What does `conntrack -S` help you verify for CNI, kube-proxy and eBPF data planes?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: external/local traffic policy and plugin behavior influence client IP.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JN-10

- [ ] **Code:** **Question:** What does `bpftool map list` help you verify for CNI, kube-proxy and eBPF data planes?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: overlay, native routing or cloud ENIs change troubleshooting and scale limits.

## Junior — procedural and command questions

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JP-01

- [ ] **Code:** **Question:** A basic Kubernetes network model check fails. What would you do first using the CLI?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Security model](README.md#security-model)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ds -n kube-system` and capture exact status/reason/request ID. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JP-02

- [ ] **Question:** A basic CNI plugin check fails. What would you do first?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system DS_POD --since=30m` and capture exact status/reason/request ID. configures Pod interface, address, route and cleanup when runtime creates sandbox. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JP-03

- [ ] **Question:** A basic IPAM check fails. What would you do first?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip route && ip link` and capture exact status/reason/request ID. allocates/reclaims Pod addresses and can exhaust/fragment subnet pools. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JP-04

- [ ] **Code:** **Question:** A basic kube-proxy iptables check fails. What would you do first using the CLI?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `conntrack -S` and capture exact status/reason/request ID. programs probabilistic NAT rules for Services and endpoints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JP-05

- [ ] **Question:** A basic kube-proxy IPVS check fails. What would you do first?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `bpftool map list` and capture exact status/reason/request ID. uses kernel virtual server tables with separate synchronization. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JP-06

- [ ] **Question:** A basic eBPF data plane check fails. What would you do first?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ds -n kube-system` and capture exact status/reason/request ID. programs kernel hooks/maps for routing, load balancing, policy and observability. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JP-07

- [ ] **Code:** **Question:** A basic Conntrack check fails. What would you do first using the CLI?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system DS_POD --since=30m` and capture exact status/reason/request ID. tracks NAT/state and can exhaust or retain stale translations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JP-08

- [ ] **Question:** A basic MTU check fails. What would you do first?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip route && ip link` and capture exact status/reason/request ID. encapsulation/cloud path mismatch can drop large packets while probes pass. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JP-09

- [ ] **Question:** A basic SNAT/source preservation check fails. What would you do first?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `conntrack -S` and capture exact status/reason/request ID. external/local traffic policy and plugin behavior influence client IP. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-JP-10

- [ ] **Code:** **Question:** A basic Node-to-Pod routing check fails. What would you do first using the CLI?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `bpftool map list` and capture exact status/reason/request ID. overlay, native routing or cloud ENIs change troubleshooting and scale limits. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MN-01

- [ ] **Question:** Compare Kubernetes network model with CNI plugin. When would each change your design?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Kubernetes network model: Pods have cluster-routable IP identity and communicate without required NAT inside the model. CNI plugin: configures Pod interface, address, route and cleanup when runtime creates sandbox. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MN-02

- [ ] **Question:** Compare CNI plugin with IPAM. When would each change your design?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CNI plugin: configures Pod interface, address, route and cleanup when runtime creates sandbox. IPAM: allocates/reclaims Pod addresses and can exhaust/fragment subnet pools. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MN-03

- [ ] **Question:** Compare IPAM with kube-proxy iptables. When would each change your design?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** IPAM: allocates/reclaims Pod addresses and can exhaust/fragment subnet pools. kube-proxy iptables: programs probabilistic NAT rules for Services and endpoints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MN-04

- [ ] **Configuration review:** **Question:** Compare kube-proxy iptables with kube-proxy IPVS. When would each change your design?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** kube-proxy iptables: programs probabilistic NAT rules for Services and endpoints. kube-proxy IPVS: uses kernel virtual server tables with separate synchronization. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MN-05

- [ ] **Question:** Compare kube-proxy IPVS with eBPF data plane. When would each change your design?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** kube-proxy IPVS: uses kernel virtual server tables with separate synchronization. eBPF data plane: programs kernel hooks/maps for routing, load balancing, policy and observability. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MN-06

- [ ] **Question:** Compare eBPF data plane with Conntrack. When would each change your design?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** eBPF data plane: programs kernel hooks/maps for routing, load balancing, policy and observability. Conntrack: tracks NAT/state and can exhaust or retain stale translations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MN-07

- [ ] **Configuration review:** **Question:** Compare Conntrack with MTU. When would each change your design?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Conntrack: tracks NAT/state and can exhaust or retain stale translations. MTU: encapsulation/cloud path mismatch can drop large packets while probes pass. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MN-08

- [ ] **Question:** Compare MTU with SNAT/source preservation. When would each change your design?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** MTU: encapsulation/cloud path mismatch can drop large packets while probes pass. SNAT/source preservation: external/local traffic policy and plugin behavior influence client IP. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MN-09

- [ ] **Question:** Compare SNAT/source preservation with Node-to-Pod routing. When would each change your design?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** SNAT/source preservation: external/local traffic policy and plugin behavior influence client IP. Node-to-Pod routing: overlay, native routing or cloud ENIs change troubleshooting and scale limits. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MN-10

- [ ] **Configuration review:** **Question:** Compare Node-to-Pod routing with Kubernetes network model. When would each change your design?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Node-to-Pod routing: overlay, native routing or cloud ENIs change troubleshooting and scale limits. Kubernetes network model: Pods have cluster-routable IP identity and communicate without required NAT inside the model. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Kubernetes network model; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ds -n kube-system` plus recent events/changes, then correlate the service-specific SLI. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MP-02

- [ ] **Question:** Production is degraded around CNI plugin; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system DS_POD --since=30m` plus recent events/changes, then correlate the service-specific SLI. configures Pod interface, address, route and cleanup when runtime creates sandbox. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around IPAM; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip route && ip link` plus recent events/changes, then correlate the service-specific SLI. allocates/reclaims Pod addresses and can exhaust/fragment subnet pools. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MP-04

- [ ] **Question:** Production is degraded around kube-proxy iptables; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `conntrack -S` plus recent events/changes, then correlate the service-specific SLI. programs probabilistic NAT rules for Services and endpoints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around kube-proxy IPVS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `bpftool map list` plus recent events/changes, then correlate the service-specific SLI. uses kernel virtual server tables with separate synchronization. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MP-06

- [ ] **Question:** Production is degraded around eBPF data plane; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ds -n kube-system` plus recent events/changes, then correlate the service-specific SLI. programs kernel hooks/maps for routing, load balancing, policy and observability. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Conntrack; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system DS_POD --since=30m` plus recent events/changes, then correlate the service-specific SLI. tracks NAT/state and can exhaust or retain stale translations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MP-08

- [ ] **Question:** Production is degraded around MTU; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip route && ip link` plus recent events/changes, then correlate the service-specific SLI. encapsulation/cloud path mismatch can drop large packets while probes pass. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around SNAT/source preservation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `conntrack -S` plus recent events/changes, then correlate the service-specific SLI. external/local traffic policy and plugin behavior influence client IP. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-MP-10

- [ ] **Question:** Production is degraded around Node-to-Pod routing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `bpftool map list` plus recent events/changes, then correlate the service-specific SLI. overlay, native routing or cloud ENIs change troubleshooting and scale limits. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SN-01

- [ ] **Question:** Design a production CNI, kube-proxy and eBPF data planes capability where Kubernetes network model, kube-proxy iptables and Conntrack are first-class requirements.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Pods have cluster-routable IP identity and communicate without required NAT inside the model. programs probabilistic NAT rules for Services and endpoints. tracks NAT/state and can exhaust or retain stale translations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production CNI, kube-proxy and eBPF data planes capability where CNI plugin, kube-proxy IPVS and MTU are first-class requirements.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: configures Pod interface, address, route and cleanup when runtime creates sandbox. uses kernel virtual server tables with separate synchronization. encapsulation/cloud path mismatch can drop large packets while probes pass. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SN-03

- [ ] **Question:** Design a production CNI, kube-proxy and eBPF data planes capability where IPAM, eBPF data plane and SNAT/source preservation are first-class requirements.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: allocates/reclaims Pod addresses and can exhaust/fragment subnet pools. programs kernel hooks/maps for routing, load balancing, policy and observability. external/local traffic policy and plugin behavior influence client IP. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production CNI, kube-proxy and eBPF data planes capability where kube-proxy iptables, Conntrack and Node-to-Pod routing are first-class requirements.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: programs probabilistic NAT rules for Services and endpoints. tracks NAT/state and can exhaust or retain stale translations. overlay, native routing or cloud ENIs change troubleshooting and scale limits. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SN-05

- [ ] **Question:** Design a production CNI, kube-proxy and eBPF data planes capability where kube-proxy IPVS, MTU and Kubernetes network model are first-class requirements.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: uses kernel virtual server tables with separate synchronization. encapsulation/cloud path mismatch can drop large packets while probes pass. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production CNI, kube-proxy and eBPF data planes capability where eBPF data plane, SNAT/source preservation and CNI plugin are first-class requirements.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: programs kernel hooks/maps for routing, load balancing, policy and observability. external/local traffic policy and plugin behavior influence client IP. configures Pod interface, address, route and cleanup when runtime creates sandbox. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SN-07

- [ ] **Question:** Design a production CNI, kube-proxy and eBPF data planes capability where Conntrack, Node-to-Pod routing and IPAM are first-class requirements.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tracks NAT/state and can exhaust or retain stale translations. overlay, native routing or cloud ENIs change troubleshooting and scale limits. allocates/reclaims Pod addresses and can exhaust/fragment subnet pools. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production CNI, kube-proxy and eBPF data planes capability where MTU, Kubernetes network model and kube-proxy iptables are first-class requirements.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: encapsulation/cloud path mismatch can drop large packets while probes pass. Pods have cluster-routable IP identity and communicate without required NAT inside the model. programs probabilistic NAT rules for Services and endpoints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SN-09

- [ ] **Question:** Design a production CNI, kube-proxy and eBPF data planes capability where SNAT/source preservation, CNI plugin and kube-proxy IPVS are first-class requirements.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: external/local traffic policy and plugin behavior influence client IP. configures Pod interface, address, route and cleanup when runtime creates sandbox. uses kernel virtual server tables with separate synchronization. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production CNI, kube-proxy and eBPF data planes capability where Node-to-Pod routing, IPAM and eBPF data plane are first-class requirements.
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: overlay, native routing or cloud ENIs change troubleshooting and scale limits. allocates/reclaims Pod addresses and can exhaust/fragment subnet pools. programs kernel hooks/maps for routing, load balancing, policy and observability. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Kubernetes network model. How do you lead it end to end?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ds -n kube-system` as one read-only checkpoint, not the whole diagnosis. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CNI plugin. How do you lead it end to end?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system DS_POD --since=30m` as one read-only checkpoint, not the whole diagnosis. configures Pod interface, address, route and cleanup when runtime creates sandbox. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IPAM. How do you lead it end to end?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip route && ip link` as one read-only checkpoint, not the whole diagnosis. allocates/reclaims Pod addresses and can exhaust/fragment subnet pools. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving kube-proxy iptables. How do you lead it end to end?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `conntrack -S` as one read-only checkpoint, not the whole diagnosis. programs probabilistic NAT rules for Services and endpoints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving kube-proxy IPVS. How do you lead it end to end?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `bpftool map list` as one read-only checkpoint, not the whole diagnosis. uses kernel virtual server tables with separate synchronization. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving eBPF data plane. How do you lead it end to end?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ds -n kube-system` as one read-only checkpoint, not the whole diagnosis. programs kernel hooks/maps for routing, load balancing, policy and observability. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Conntrack. How do you lead it end to end?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system DS_POD --since=30m` as one read-only checkpoint, not the whole diagnosis. tracks NAT/state and can exhaust or retain stale translations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving MTU. How do you lead it end to end?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip route && ip link` as one read-only checkpoint, not the whole diagnosis. encapsulation/cloud path mismatch can drop large packets while probes pass. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SNAT/source preservation. How do you lead it end to end?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `conntrack -S` as one read-only checkpoint, not the whole diagnosis. external/local traffic policy and plugin behavior influence client IP. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CNI-KUBE-PROXY-AND-EBPF-DATA-PLANES-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node-to-Pod routing. How do you lead it end to end?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `bpftool map list` as one read-only checkpoint, not the whole diagnosis. overlay, native routing or cloud ENIs change troubleshooting and scale limits. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Services, EndpointSlices and CoreDNS](../01-services-endpoints-dns/README.md) · [Study note](README.md) · [Next: Kubernetes NetworkPolicy →](../03-networkpolicy/README.md)

<!-- reading-navigation:end -->
