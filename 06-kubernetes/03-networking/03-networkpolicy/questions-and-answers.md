# Kubernetes NetworkPolicy — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KUBERNETES-NETWORKPOLICY-JN-01

- [ ] **Question:** What is Pod selection, and why does it matter in Kubernetes NetworkPolicy?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** policy applies only to Pods matched in its namespace. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-NETWORKPOLICY-JN-02

- [ ] **Question:** What is Isolation direction, and why does it matter in Kubernetes NetworkPolicy?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** selecting a Pod for ingress/egress isolates that direction to allowed union. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-NETWORKPOLICY-JN-03

- [ ] **Question:** What is Additive policy, and why does it matter in Kubernetes NetworkPolicy?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** all matching policy allows are unioned; deny rules are not in base API. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-NETWORKPOLICY-JN-04

- [ ] **Question:** What is Namespace selector, and why does it matter in Kubernetes NetworkPolicy?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** selects labeled namespaces and needs protected namespace label governance. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-NETWORKPOLICY-JN-05

- [ ] **Question:** What is Pod selector, and why does it matter in Kubernetes NetworkPolicy?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** selects workload labels in the policy/selected namespace context. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-NETWORKPOLICY-JN-06

- [ ] **Question:** What is ipBlock, and why does it matter in Kubernetes NetworkPolicy?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CIDR/except matches IPs and can behave unexpectedly after NAT. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-NETWORKPOLICY-JN-07

- [ ] **Question:** What is Port/protocol, and why does it matter in Kubernetes NetworkPolicy?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** L3/L4 policy cannot natively authorize DNS names or HTTP paths. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KUBERNETES-NETWORKPOLICY-JN-08

- [ ] **Code:** **Question:** What does `tcpdump -ni any host IP and port PORT` help you verify for Kubernetes NetworkPolicy?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: empty allow list establishes isolation and requires DNS/control/dependency allowances.

### KUBERNETES-NETWORKPOLICY-JN-09

- [ ] **Code:** **Question:** What does `kubectl get networkpolicy -A -o yaml` help you verify for Kubernetes NetworkPolicy?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: source egress and destination ingress can independently block one flow.

### KUBERNETES-NETWORKPOLICY-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe networkpolicy NAME -n NS` help you verify for Kubernetes NetworkPolicy?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: unsupported/no plugin means accepted objects may have no runtime effect.

## Junior — procedural and command questions

### KUBERNETES-NETWORKPOLICY-JP-01

- [ ] **Code:** **Question:** A basic Pod selection check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get networkpolicy -A -o yaml` and capture exact status/reason/request ID. policy applies only to Pods matched in its namespace. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-NETWORKPOLICY-JP-02

- [ ] **Question:** A basic Isolation direction check fails. What would you do first?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe networkpolicy NAME -n NS` and capture exact status/reason/request ID. selecting a Pod for ingress/egress isolates that direction to allowed union. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-NETWORKPOLICY-JP-03

- [ ] **Question:** A basic Additive policy check fails. What would you do first?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl run netshoot --rm -it -n NS --image=nicolaka/netshoot -- bash` and capture exact status/reason/request ID. all matching policy allows are unioned; deny rules are not in base API. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-NETWORKPOLICY-JP-04

- [ ] **Code:** **Question:** A basic Namespace selector check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any host IP and port PORT` and capture exact status/reason/request ID. selects labeled namespaces and needs protected namespace label governance. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-NETWORKPOLICY-JP-05

- [ ] **Question:** A basic Pod selector check fails. What would you do first?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get networkpolicy -A -o yaml` and capture exact status/reason/request ID. selects workload labels in the policy/selected namespace context. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-NETWORKPOLICY-JP-06

- [ ] **Question:** A basic ipBlock check fails. What would you do first?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe networkpolicy NAME -n NS` and capture exact status/reason/request ID. CIDR/except matches IPs and can behave unexpectedly after NAT. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-NETWORKPOLICY-JP-07

- [ ] **Code:** **Question:** A basic Port/protocol check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl run netshoot --rm -it -n NS --image=nicolaka/netshoot -- bash` and capture exact status/reason/request ID. L3/L4 policy cannot natively authorize DNS names or HTTP paths. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-NETWORKPOLICY-JP-08

- [ ] **Question:** A basic Default deny check fails. What would you do first?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any host IP and port PORT` and capture exact status/reason/request ID. empty allow list establishes isolation and requires DNS/control/dependency allowances. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-NETWORKPOLICY-JP-09

- [ ] **Question:** A basic Both directions check fails. What would you do first?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get networkpolicy -A -o yaml` and capture exact status/reason/request ID. source egress and destination ingress can independently block one flow. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KUBERNETES-NETWORKPOLICY-JP-10

- [ ] **Code:** **Question:** A basic CNI enforcement check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes NetworkPolicy — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe networkpolicy NAME -n NS` and capture exact status/reason/request ID. unsupported/no plugin means accepted objects may have no runtime effect. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KUBERNETES-NETWORKPOLICY-MN-01

- [ ] **Question:** Compare Pod selection with Isolation direction. When would each change your design?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Pod selection: policy applies only to Pods matched in its namespace. Isolation direction: selecting a Pod for ingress/egress isolates that direction to allowed union. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-NETWORKPOLICY-MN-02

- [ ] **Question:** Compare Isolation direction with Additive policy. When would each change your design?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Isolation direction: selecting a Pod for ingress/egress isolates that direction to allowed union. Additive policy: all matching policy allows are unioned; deny rules are not in base API. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-NETWORKPOLICY-MN-03

- [ ] **Question:** Compare Additive policy with Namespace selector. When would each change your design?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Additive policy: all matching policy allows are unioned; deny rules are not in base API. Namespace selector: selects labeled namespaces and needs protected namespace label governance. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-NETWORKPOLICY-MN-04

- [ ] **Configuration review:** **Question:** Compare Namespace selector with Pod selector. When would each change your design?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Namespace selector: selects labeled namespaces and needs protected namespace label governance. Pod selector: selects workload labels in the policy/selected namespace context. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-NETWORKPOLICY-MN-05

- [ ] **Question:** Compare Pod selector with ipBlock. When would each change your design?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Pod selector: selects workload labels in the policy/selected namespace context. ipBlock: CIDR/except matches IPs and can behave unexpectedly after NAT. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-NETWORKPOLICY-MN-06

- [ ] **Question:** Compare ipBlock with Port/protocol. When would each change your design?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ipBlock: CIDR/except matches IPs and can behave unexpectedly after NAT. Port/protocol: L3/L4 policy cannot natively authorize DNS names or HTTP paths. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-NETWORKPOLICY-MN-07

- [ ] **Configuration review:** **Question:** Compare Port/protocol with Default deny. When would each change your design?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Port/protocol: L3/L4 policy cannot natively authorize DNS names or HTTP paths. Default deny: empty allow list establishes isolation and requires DNS/control/dependency allowances. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-NETWORKPOLICY-MN-08

- [ ] **Question:** Compare Default deny with Both directions. When would each change your design?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Default deny: empty allow list establishes isolation and requires DNS/control/dependency allowances. Both directions: source egress and destination ingress can independently block one flow. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-NETWORKPOLICY-MN-09

- [ ] **Question:** Compare Both directions with CNI enforcement. When would each change your design?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Both directions: source egress and destination ingress can independently block one flow. CNI enforcement: unsupported/no plugin means accepted objects may have no runtime effect. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KUBERNETES-NETWORKPOLICY-MN-10

- [ ] **Configuration review:** **Question:** Compare CNI enforcement with Pod selection. When would each change your design?
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CNI enforcement: unsupported/no plugin means accepted objects may have no runtime effect. Pod selection: policy applies only to Pods matched in its namespace. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KUBERNETES-NETWORKPOLICY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pod selection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get networkpolicy -A -o yaml` plus recent events/changes, then correlate the service-specific SLI. policy applies only to Pods matched in its namespace. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-NETWORKPOLICY-MP-02

- [ ] **Question:** Production is degraded around Isolation direction; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe networkpolicy NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. selecting a Pod for ingress/egress isolates that direction to allowed union. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-NETWORKPOLICY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Additive policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl run netshoot --rm -it -n NS --image=nicolaka/netshoot -- bash` plus recent events/changes, then correlate the service-specific SLI. all matching policy allows are unioned; deny rules are not in base API. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-NETWORKPOLICY-MP-04

- [ ] **Question:** Production is degraded around Namespace selector; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any host IP and port PORT` plus recent events/changes, then correlate the service-specific SLI. selects labeled namespaces and needs protected namespace label governance. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-NETWORKPOLICY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pod selector; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get networkpolicy -A -o yaml` plus recent events/changes, then correlate the service-specific SLI. selects workload labels in the policy/selected namespace context. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-NETWORKPOLICY-MP-06

- [ ] **Question:** Production is degraded around ipBlock; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe networkpolicy NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. CIDR/except matches IPs and can behave unexpectedly after NAT. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-NETWORKPOLICY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Port/protocol; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl run netshoot --rm -it -n NS --image=nicolaka/netshoot -- bash` plus recent events/changes, then correlate the service-specific SLI. L3/L4 policy cannot natively authorize DNS names or HTTP paths. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-NETWORKPOLICY-MP-08

- [ ] **Question:** Production is degraded around Default deny; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any host IP and port PORT` plus recent events/changes, then correlate the service-specific SLI. empty allow list establishes isolation and requires DNS/control/dependency allowances. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-NETWORKPOLICY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Both directions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get networkpolicy -A -o yaml` plus recent events/changes, then correlate the service-specific SLI. source egress and destination ingress can independently block one flow. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KUBERNETES-NETWORKPOLICY-MP-10

- [ ] **Question:** Production is degraded around CNI enforcement; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe networkpolicy NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. unsupported/no plugin means accepted objects may have no runtime effect. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KUBERNETES-NETWORKPOLICY-SN-01

- [ ] **Question:** Design a production Kubernetes NetworkPolicy capability where Pod selection, Namespace selector and Port/protocol are first-class requirements.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: policy applies only to Pods matched in its namespace. selects labeled namespaces and needs protected namespace label governance. L3/L4 policy cannot natively authorize DNS names or HTTP paths. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-NETWORKPOLICY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes NetworkPolicy capability where Isolation direction, Pod selector and Default deny are first-class requirements.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: selecting a Pod for ingress/egress isolates that direction to allowed union. selects workload labels in the policy/selected namespace context. empty allow list establishes isolation and requires DNS/control/dependency allowances. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-NETWORKPOLICY-SN-03

- [ ] **Question:** Design a production Kubernetes NetworkPolicy capability where Additive policy, ipBlock and Both directions are first-class requirements.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: all matching policy allows are unioned; deny rules are not in base API. CIDR/except matches IPs and can behave unexpectedly after NAT. source egress and destination ingress can independently block one flow. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-NETWORKPOLICY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes NetworkPolicy capability where Namespace selector, Port/protocol and CNI enforcement are first-class requirements.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: selects labeled namespaces and needs protected namespace label governance. L3/L4 policy cannot natively authorize DNS names or HTTP paths. unsupported/no plugin means accepted objects may have no runtime effect. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-NETWORKPOLICY-SN-05

- [ ] **Question:** Design a production Kubernetes NetworkPolicy capability where Pod selector, Default deny and Pod selection are first-class requirements.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: selects workload labels in the policy/selected namespace context. empty allow list establishes isolation and requires DNS/control/dependency allowances. policy applies only to Pods matched in its namespace. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-NETWORKPOLICY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes NetworkPolicy capability where ipBlock, Both directions and Isolation direction are first-class requirements.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: CIDR/except matches IPs and can behave unexpectedly after NAT. source egress and destination ingress can independently block one flow. selecting a Pod for ingress/egress isolates that direction to allowed union. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-NETWORKPOLICY-SN-07

- [ ] **Question:** Design a production Kubernetes NetworkPolicy capability where Port/protocol, CNI enforcement and Additive policy are first-class requirements.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: L3/L4 policy cannot natively authorize DNS names or HTTP paths. unsupported/no plugin means accepted objects may have no runtime effect. all matching policy allows are unioned; deny rules are not in base API. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-NETWORKPOLICY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes NetworkPolicy capability where Default deny, Pod selection and Namespace selector are first-class requirements.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: empty allow list establishes isolation and requires DNS/control/dependency allowances. policy applies only to Pods matched in its namespace. selects labeled namespaces and needs protected namespace label governance. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-NETWORKPOLICY-SN-09

- [ ] **Question:** Design a production Kubernetes NetworkPolicy capability where Both directions, Isolation direction and Pod selector are first-class requirements.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: source egress and destination ingress can independently block one flow. selecting a Pod for ingress/egress isolates that direction to allowed union. selects workload labels in the policy/selected namespace context. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KUBERNETES-NETWORKPOLICY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kubernetes NetworkPolicy capability where CNI enforcement, Additive policy and ipBlock are first-class requirements.
> **Covered in:** [Kubernetes NetworkPolicy — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: unsupported/no plugin means accepted objects may have no runtime effect. all matching policy allows are unioned; deny rules are not in base API. CIDR/except matches IPs and can behave unexpectedly after NAT. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KUBERNETES-NETWORKPOLICY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod selection. How do you lead it end to end?
> **Covered in:** [Kubernetes NetworkPolicy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get networkpolicy -A -o yaml` as one read-only checkpoint, not the whole diagnosis. policy applies only to Pods matched in its namespace. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-NETWORKPOLICY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Isolation direction. How do you lead it end to end?
> **Covered in:** [Kubernetes NetworkPolicy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe networkpolicy NAME -n NS` as one read-only checkpoint, not the whole diagnosis. selecting a Pod for ingress/egress isolates that direction to allowed union. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-NETWORKPOLICY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Additive policy. How do you lead it end to end?
> **Covered in:** [Kubernetes NetworkPolicy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl run netshoot --rm -it -n NS --image=nicolaka/netshoot -- bash` as one read-only checkpoint, not the whole diagnosis. all matching policy allows are unioned; deny rules are not in base API. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-NETWORKPOLICY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Namespace selector. How do you lead it end to end?
> **Covered in:** [Kubernetes NetworkPolicy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any host IP and port PORT` as one read-only checkpoint, not the whole diagnosis. selects labeled namespaces and needs protected namespace label governance. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-NETWORKPOLICY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod selector. How do you lead it end to end?
> **Covered in:** [Kubernetes NetworkPolicy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get networkpolicy -A -o yaml` as one read-only checkpoint, not the whole diagnosis. selects workload labels in the policy/selected namespace context. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-NETWORKPOLICY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ipBlock. How do you lead it end to end?
> **Covered in:** [Kubernetes NetworkPolicy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe networkpolicy NAME -n NS` as one read-only checkpoint, not the whole diagnosis. CIDR/except matches IPs and can behave unexpectedly after NAT. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-NETWORKPOLICY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Port/protocol. How do you lead it end to end?
> **Covered in:** [Kubernetes NetworkPolicy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl run netshoot --rm -it -n NS --image=nicolaka/netshoot -- bash` as one read-only checkpoint, not the whole diagnosis. L3/L4 policy cannot natively authorize DNS names or HTTP paths. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-NETWORKPOLICY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Default deny. How do you lead it end to end?
> **Covered in:** [Kubernetes NetworkPolicy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any host IP and port PORT` as one read-only checkpoint, not the whole diagnosis. empty allow list establishes isolation and requires DNS/control/dependency allowances. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-NETWORKPOLICY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Both directions. How do you lead it end to end?
> **Covered in:** [Kubernetes NetworkPolicy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get networkpolicy -A -o yaml` as one read-only checkpoint, not the whole diagnosis. source egress and destination ingress can independently block one flow. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KUBERNETES-NETWORKPOLICY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CNI enforcement. How do you lead it end to end?
> **Covered in:** [Kubernetes NetworkPolicy — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe networkpolicy NAME -n NS` as one read-only checkpoint, not the whole diagnosis. unsupported/no plugin means accepted objects may have no runtime effect. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: CNI, kube-proxy and eBPF data planes](../02-cni-kubeproxy-ebpf/README.md) · [Study note](README.md) · [Next: Ingress and Gateway API →](../04-ingress-gateway-api/README.md)

<!-- reading-navigation:end -->
