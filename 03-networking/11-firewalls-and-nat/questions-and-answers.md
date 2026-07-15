# Firewalls and NAT — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### FIREWALLS-AND-NAT-JN-01

- [ ] **Question:** What is Stateless versus stateful firewalls, and why does it matter in Firewalls and NAT?
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FIREWALLS-AND-NAT-JN-02

- [ ] **Question:** What is Ingress and egress rules, and why does it matter in Firewalls and NAT?
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FIREWALLS-AND-NAT-JN-03

- [ ] **Question:** What is NAT, and why does it matter in Firewalls and NAT?
> **Covered in:** [Firewalls and NAT — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FIREWALLS-AND-NAT-JN-04

- [ ] **Question:** What is SNAT, and why does it matter in Firewalls and NAT?
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FIREWALLS-AND-NAT-JN-05

- [ ] **Question:** What is DNAT, and why does it matter in Firewalls and NAT?
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** rewrites destination addressing for published services and must align with routing, policy and connection state. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FIREWALLS-AND-NAT-JN-06

- [ ] **Question:** What is PAT, and why does it matter in Firewalls and NAT?
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FIREWALLS-AND-NAT-JN-07

- [ ] **Question:** What is Connection tracking, and why does it matter in Firewalls and NAT?
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FIREWALLS-AND-NAT-JN-08

- [ ] **Code:** **Question:** What does `tcpdump -ni any 'host IP and port PORT'` help you verify for Firewalls and NAT?
> **Covered in:** [Firewalls and NAT — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### FIREWALLS-AND-NAT-JN-09

- [ ] **Code:** **Question:** What does `ip -br addr; ip route; ip neigh` help you verify for Firewalls and NAT?
> **Covered in:** [Firewalls and NAT — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference.

### FIREWALLS-AND-NAT-JN-10

- [ ] **Code:** **Question:** What does `dig +trace NAME` help you verify for Firewalls and NAT?
> **Covered in:** [Firewalls and NAT — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### FIREWALLS-AND-NAT-JP-01

- [ ] **Code:** **Question:** A basic Stateless versus stateful firewalls check fails. What would you do first using the CLI?
> **Covered in:** [Firewalls and NAT — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FIREWALLS-AND-NAT-JP-02

- [ ] **Question:** A basic Ingress and egress rules check fails. What would you do first?
> **Covered in:** [Firewalls and NAT — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FIREWALLS-AND-NAT-JP-03

- [ ] **Question:** A basic NAT check fails. What would you do first?
> **Covered in:** [Firewalls and NAT — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk URL` and capture exact status/reason/request ID. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FIREWALLS-AND-NAT-JP-04

- [ ] **Code:** **Question:** A basic SNAT check fails. What would you do first using the CLI?
> **Covered in:** [Firewalls and NAT — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any 'host IP and port PORT'` and capture exact status/reason/request ID. rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FIREWALLS-AND-NAT-JP-05

- [ ] **Question:** A basic DNAT check fails. What would you do first?
> **Covered in:** [Firewalls and NAT — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. rewrites destination addressing for published services and must align with routing, policy and connection state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FIREWALLS-AND-NAT-JP-06

- [ ] **Question:** A basic PAT check fails. What would you do first?
> **Covered in:** [Firewalls and NAT — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FIREWALLS-AND-NAT-JP-07

- [ ] **Code:** **Question:** A basic Connection tracking check fails. What would you do first using the CLI?
> **Covered in:** [Firewalls and NAT — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk URL` and capture exact status/reason/request ID. records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FIREWALLS-AND-NAT-JP-08

- [ ] **Question:** A basic Network address exhaustion check fails. What would you do first?
> **Covered in:** [Firewalls and NAT — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any 'host IP and port PORT'` and capture exact status/reason/request ID. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FIREWALLS-AND-NAT-JP-09

- [ ] **Question:** A basic Stateless versus stateful firewalls check fails. What would you do first?
> **Covered in:** [Firewalls and NAT — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FIREWALLS-AND-NAT-JP-10

- [ ] **Code:** **Question:** A basic Ingress and egress rules check fails. What would you do first using the CLI?
> **Covered in:** [Firewalls and NAT — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### FIREWALLS-AND-NAT-MN-01

- [ ] **Question:** Compare Stateless versus stateful firewalls with Ingress and egress rules. When would each change your design?
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Stateless versus stateful firewalls: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Ingress and egress rules: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FIREWALLS-AND-NAT-MN-02

- [ ] **Question:** Compare Ingress and egress rules with NAT. When would each change your design?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Ingress and egress rules: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. NAT: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FIREWALLS-AND-NAT-MN-03

- [ ] **Question:** Compare NAT with SNAT. When would each change your design?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** NAT: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. SNAT: rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FIREWALLS-AND-NAT-MN-04

- [ ] **Configuration review:** **Question:** Compare SNAT with DNAT. When would each change your design?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** SNAT: rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity. DNAT: rewrites destination addressing for published services and must align with routing, policy and connection state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FIREWALLS-AND-NAT-MN-05

- [ ] **Question:** Compare DNAT with PAT. When would each change your design?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** DNAT: rewrites destination addressing for published services and must align with routing, policy and connection state. PAT: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FIREWALLS-AND-NAT-MN-06

- [ ] **Question:** Compare PAT with Connection tracking. When would each change your design?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** PAT: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Connection tracking: records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FIREWALLS-AND-NAT-MN-07

- [ ] **Configuration review:** **Question:** Compare Connection tracking with Network address exhaustion. When would each change your design?
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Connection tracking: records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners. Network address exhaustion: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FIREWALLS-AND-NAT-MN-08

- [ ] **Question:** Compare Network address exhaustion with Stateless versus stateful firewalls. When would each change your design?
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Network address exhaustion: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stateless versus stateful firewalls: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FIREWALLS-AND-NAT-MN-09

- [ ] **Question:** Compare Stateless versus stateful firewalls with Ingress and egress rules. When would each change your design?
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Stateless versus stateful firewalls: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Ingress and egress rules: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FIREWALLS-AND-NAT-MN-10

- [ ] **Configuration review:** **Question:** Compare Ingress and egress rules with Stateless versus stateful firewalls. When would each change your design?
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Ingress and egress rules: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stateless versus stateful firewalls: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### FIREWALLS-AND-NAT-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Stateless versus stateful firewalls; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FIREWALLS-AND-NAT-MP-02

- [ ] **Question:** Production is degraded around Ingress and egress rules; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FIREWALLS-AND-NAT-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around NAT; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk URL` plus recent events/changes, then correlate the service-specific SLI. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FIREWALLS-AND-NAT-MP-04

- [ ] **Question:** Production is degraded around SNAT; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any 'host IP and port PORT'` plus recent events/changes, then correlate the service-specific SLI. rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FIREWALLS-AND-NAT-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around DNAT; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. rewrites destination addressing for published services and must align with routing, policy and connection state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FIREWALLS-AND-NAT-MP-06

- [ ] **Question:** Production is degraded around PAT; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FIREWALLS-AND-NAT-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Connection tracking; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk URL` plus recent events/changes, then correlate the service-specific SLI. records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FIREWALLS-AND-NAT-MP-08

- [ ] **Question:** Production is degraded around Network address exhaustion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any 'host IP and port PORT'` plus recent events/changes, then correlate the service-specific SLI. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FIREWALLS-AND-NAT-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Stateless versus stateful firewalls; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FIREWALLS-AND-NAT-MP-10

- [ ] **Question:** Production is degraded around Ingress and egress rules; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### FIREWALLS-AND-NAT-SN-01

- [ ] **Question:** Design a production Firewalls and NAT capability where Stateless versus stateful firewalls, SNAT and Connection tracking are first-class requirements.
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity. records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FIREWALLS-AND-NAT-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Firewalls and NAT capability where Ingress and egress rules, DNAT and Network address exhaustion are first-class requirements.
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. rewrites destination addressing for published services and must align with routing, policy and connection state. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FIREWALLS-AND-NAT-SN-03

- [ ] **Question:** Design a production Firewalls and NAT capability where NAT, PAT and Stateless versus stateful firewalls are first-class requirements.
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FIREWALLS-AND-NAT-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Firewalls and NAT capability where SNAT, Connection tracking and Ingress and egress rules are first-class requirements.
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity. records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FIREWALLS-AND-NAT-SN-05

- [ ] **Question:** Design a production Firewalls and NAT capability where DNAT, Network address exhaustion and Stateless versus stateful firewalls are first-class requirements.
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: rewrites destination addressing for published services and must align with routing, policy and connection state. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FIREWALLS-AND-NAT-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Firewalls and NAT capability where PAT, Stateless versus stateful firewalls and Ingress and egress rules are first-class requirements.
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FIREWALLS-AND-NAT-SN-07

- [ ] **Question:** Design a production Firewalls and NAT capability where Connection tracking, Ingress and egress rules and NAT are first-class requirements.
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FIREWALLS-AND-NAT-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Firewalls and NAT capability where Network address exhaustion, Stateless versus stateful firewalls and SNAT are first-class requirements.
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FIREWALLS-AND-NAT-SN-09

- [ ] **Question:** Design a production Firewalls and NAT capability where Stateless versus stateful firewalls, Ingress and egress rules and DNAT are first-class requirements.
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. rewrites destination addressing for published services and must align with routing, policy and connection state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FIREWALLS-AND-NAT-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Firewalls and NAT capability where Ingress and egress rules, NAT and PAT are first-class requirements.
> **Covered in:** [Firewalls and NAT — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### FIREWALLS-AND-NAT-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stateless versus stateful firewalls. How do you lead it end to end?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FIREWALLS-AND-NAT-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ingress and egress rules. How do you lead it end to end?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FIREWALLS-AND-NAT-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NAT. How do you lead it end to end?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk URL` as one read-only checkpoint, not the whole diagnosis. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FIREWALLS-AND-NAT-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SNAT. How do you lead it end to end?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any 'host IP and port PORT'` as one read-only checkpoint, not the whole diagnosis. rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FIREWALLS-AND-NAT-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DNAT. How do you lead it end to end?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. rewrites destination addressing for published services and must align with routing, policy and connection state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FIREWALLS-AND-NAT-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving PAT. How do you lead it end to end?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FIREWALLS-AND-NAT-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Connection tracking. How do you lead it end to end?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk URL` as one read-only checkpoint, not the whole diagnosis. records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FIREWALLS-AND-NAT-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Network address exhaustion. How do you lead it end to end?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any 'host IP and port PORT'` as one read-only checkpoint, not the whole diagnosis. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FIREWALLS-AND-NAT-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stateless versus stateful firewalls. How do you lead it end to end?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FIREWALLS-AND-NAT-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ingress and egress rules. How do you lead it end to end?
> **Covered in:** [Firewalls and NAT — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Proxies and gateways](../10-proxies-and-gateways/README.md) · [Study note](README.md) · [Next: Network troubleshooting →](../12-network-troubleshooting/README.md)

<!-- reading-navigation:end -->
