# Layer 2 networking — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### LAYER-2-NETWORKING-JN-01

- [ ] **Question:** What is Ethernet, and why does it matter in Layer 2 networking?
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LAYER-2-NETWORKING-JN-02

- [ ] **Question:** What is MAC addresses, and why does it matter in Layer 2 networking?
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LAYER-2-NETWORKING-JN-03

- [ ] **Question:** What is ARP, and why does it matter in Layer 2 networking?
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LAYER-2-NETWORKING-JN-04

- [ ] **Question:** What is VLANs, and why does it matter in Layer 2 networking?
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LAYER-2-NETWORKING-JN-05

- [ ] **Question:** What is Switching, and why does it matter in Layer 2 networking?
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LAYER-2-NETWORKING-JN-06

- [ ] **Question:** What is Broadcast domains, and why does it matter in Layer 2 networking?
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LAYER-2-NETWORKING-JN-07

- [ ] **Question:** What is Spanning Tree, and why does it matter in Layer 2 networking?
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LAYER-2-NETWORKING-JN-08

- [ ] **Code:** **Question:** What does `tcpdump -ni any 'host IP and port PORT'` help you verify for Layer 2 networking?
> **Covered in:** [Layer 2 networking — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### LAYER-2-NETWORKING-JN-09

- [ ] **Code:** **Question:** What does `ip -br addr; ip route; ip neigh` help you verify for Layer 2 networking?
> **Covered in:** [Layer 2 networking — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### LAYER-2-NETWORKING-JN-10

- [ ] **Code:** **Question:** What does `dig +trace NAME` help you verify for Layer 2 networking?
> **Covered in:** [Layer 2 networking — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability.

## Junior — procedural and command questions

### LAYER-2-NETWORKING-JP-01

- [ ] **Code:** **Question:** A basic Ethernet check fails. What would you do first using the CLI?
> **Covered in:** [Layer 2 networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LAYER-2-NETWORKING-JP-02

- [ ] **Question:** A basic MAC addresses check fails. What would you do first?
> **Covered in:** [Layer 2 networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LAYER-2-NETWORKING-JP-03

- [ ] **Question:** A basic ARP check fails. What would you do first?
> **Covered in:** [Layer 2 networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk URL` and capture exact status/reason/request ID. resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LAYER-2-NETWORKING-JP-04

- [ ] **Code:** **Question:** A basic VLANs check fails. What would you do first using the CLI?
> **Covered in:** [Layer 2 networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any 'host IP and port PORT'` and capture exact status/reason/request ID. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LAYER-2-NETWORKING-JP-05

- [ ] **Question:** A basic Switching check fails. What would you do first?
> **Covered in:** [Layer 2 networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LAYER-2-NETWORKING-JP-06

- [ ] **Question:** A basic Broadcast domains check fails. What would you do first?
> **Covered in:** [Layer 2 networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LAYER-2-NETWORKING-JP-07

- [ ] **Code:** **Question:** A basic Spanning Tree check fails. What would you do first using the CLI?
> **Covered in:** [Layer 2 networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk URL` and capture exact status/reason/request ID. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LAYER-2-NETWORKING-JP-08

- [ ] **Question:** A basic Ethernet check fails. What would you do first?
> **Covered in:** [Layer 2 networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any 'host IP and port PORT'` and capture exact status/reason/request ID. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LAYER-2-NETWORKING-JP-09

- [ ] **Question:** A basic MAC addresses check fails. What would you do first?
> **Covered in:** [Layer 2 networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LAYER-2-NETWORKING-JP-10

- [ ] **Code:** **Question:** A basic ARP check fails. What would you do first using the CLI?
> **Covered in:** [Layer 2 networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### LAYER-2-NETWORKING-MN-01

- [ ] **Question:** Compare Ethernet with MAC addresses. When would each change your design?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Ethernet: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. MAC addresses: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LAYER-2-NETWORKING-MN-02

- [ ] **Question:** Compare MAC addresses with ARP. When would each change your design?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** MAC addresses: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. ARP: resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LAYER-2-NETWORKING-MN-03

- [ ] **Question:** Compare ARP with VLANs. When would each change your design?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** ARP: resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. VLANs: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LAYER-2-NETWORKING-MN-04

- [ ] **Configuration review:** **Question:** Compare VLANs with Switching. When would each change your design?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** VLANs: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Switching: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LAYER-2-NETWORKING-MN-05

- [ ] **Question:** Compare Switching with Broadcast domains. When would each change your design?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Switching: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Broadcast domains: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LAYER-2-NETWORKING-MN-06

- [ ] **Question:** Compare Broadcast domains with Spanning Tree. When would each change your design?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Broadcast domains: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Spanning Tree: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LAYER-2-NETWORKING-MN-07

- [ ] **Configuration review:** **Question:** Compare Spanning Tree with Ethernet. When would each change your design?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Spanning Tree: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Ethernet: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LAYER-2-NETWORKING-MN-08

- [ ] **Question:** Compare Ethernet with MAC addresses. When would each change your design?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Ethernet: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. MAC addresses: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LAYER-2-NETWORKING-MN-09

- [ ] **Question:** Compare MAC addresses with ARP. When would each change your design?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** MAC addresses: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. ARP: resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LAYER-2-NETWORKING-MN-10

- [ ] **Configuration review:** **Question:** Compare ARP with Ethernet. When would each change your design?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** ARP: resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. Ethernet: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### LAYER-2-NETWORKING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Ethernet; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LAYER-2-NETWORKING-MP-02

- [ ] **Question:** Production is degraded around MAC addresses; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LAYER-2-NETWORKING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around ARP; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk URL` plus recent events/changes, then correlate the service-specific SLI. resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LAYER-2-NETWORKING-MP-04

- [ ] **Question:** Production is degraded around VLANs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any 'host IP and port PORT'` plus recent events/changes, then correlate the service-specific SLI. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LAYER-2-NETWORKING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Switching; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LAYER-2-NETWORKING-MP-06

- [ ] **Question:** Production is degraded around Broadcast domains; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LAYER-2-NETWORKING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Spanning Tree; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk URL` plus recent events/changes, then correlate the service-specific SLI. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LAYER-2-NETWORKING-MP-08

- [ ] **Question:** Production is degraded around Ethernet; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any 'host IP and port PORT'` plus recent events/changes, then correlate the service-specific SLI. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LAYER-2-NETWORKING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around MAC addresses; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LAYER-2-NETWORKING-MP-10

- [ ] **Question:** Production is degraded around ARP; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### LAYER-2-NETWORKING-SN-01

- [ ] **Question:** Design a production Layer 2 networking capability where Ethernet, VLANs and Spanning Tree are first-class requirements.
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LAYER-2-NETWORKING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Layer 2 networking capability where MAC addresses, Switching and Ethernet are first-class requirements.
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LAYER-2-NETWORKING-SN-03

- [ ] **Question:** Design a production Layer 2 networking capability where ARP, Broadcast domains and MAC addresses are first-class requirements.
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LAYER-2-NETWORKING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Layer 2 networking capability where VLANs, Spanning Tree and ARP are first-class requirements.
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LAYER-2-NETWORKING-SN-05

- [ ] **Question:** Design a production Layer 2 networking capability where Switching, Ethernet and Ethernet are first-class requirements.
> **Covered in:** [Layer 2 networking — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LAYER-2-NETWORKING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Layer 2 networking capability where Broadcast domains, MAC addresses and MAC addresses are first-class requirements.
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LAYER-2-NETWORKING-SN-07

- [ ] **Question:** Design a production Layer 2 networking capability where Spanning Tree, ARP and ARP are first-class requirements.
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LAYER-2-NETWORKING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Layer 2 networking capability where Ethernet, Ethernet and VLANs are first-class requirements.
> **Covered in:** [Layer 2 networking — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LAYER-2-NETWORKING-SN-09

- [ ] **Question:** Design a production Layer 2 networking capability where MAC addresses, MAC addresses and Switching are first-class requirements.
> **Covered in:** [Layer 2 networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LAYER-2-NETWORKING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Layer 2 networking capability where ARP, ARP and Broadcast domains are first-class requirements.
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### LAYER-2-NETWORKING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ethernet. How do you lead it end to end?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LAYER-2-NETWORKING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving MAC addresses. How do you lead it end to end?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LAYER-2-NETWORKING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ARP. How do you lead it end to end?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk URL` as one read-only checkpoint, not the whole diagnosis. resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LAYER-2-NETWORKING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VLANs. How do you lead it end to end?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any 'host IP and port PORT'` as one read-only checkpoint, not the whole diagnosis. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LAYER-2-NETWORKING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Switching. How do you lead it end to end?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LAYER-2-NETWORKING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Broadcast domains. How do you lead it end to end?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LAYER-2-NETWORKING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Spanning Tree. How do you lead it end to end?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk URL` as one read-only checkpoint, not the whole diagnosis. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LAYER-2-NETWORKING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ethernet. How do you lead it end to end?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any 'host IP and port PORT'` as one read-only checkpoint, not the whole diagnosis. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LAYER-2-NETWORKING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving MAC addresses. How do you lead it end to end?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is part of Layer 2 networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LAYER-2-NETWORKING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ARP. How do you lead it end to end?
> **Covered in:** [Layer 2 networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: IP addressing](../02-ip-addressing/README.md) · [Study note](README.md) · [Next: Routing →](../04-routing/README.md)

<!-- reading-navigation:end -->
