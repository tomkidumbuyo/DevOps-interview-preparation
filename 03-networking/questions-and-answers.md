# Networking — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-NETWORKING-JN-01

- [ ] **Question:** What is Physical, data-link, network and transport layers, and why does it matter in Networking?
> **Covered in:** [OSI and TCP/IP models — Complete curriculum checklist](01-osi-and-tcp-ip-models/README.md#complete-curriculum-checklist)

**Answer:** is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-02

- [ ] **Question:** What is Application protocols, and why does it matter in Networking?
> **Covered in:** [OSI and TCP/IP models — Complete curriculum checklist](01-osi-and-tcp-ip-models/README.md#complete-curriculum-checklist)

**Answer:** is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-03

- [ ] **Question:** What is Encapsulation, and why does it matter in Networking?
> **Covered in:** [Networking — Packet mental model](README.md#packet-mental-model)

**Answer:** is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-04

- [ ] **Question:** What is Packets, frames and segments, and why does it matter in Networking?
> **Covered in:** [OSI and TCP/IP models — Complete curriculum checklist](01-osi-and-tcp-ip-models/README.md#complete-curriculum-checklist)

**Answer:** is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-05

- [ ] **Question:** What is MTU, and why does it matter in Networking?
> **Covered in:** [Networking — Packet mental model](README.md#packet-mental-model)

**Answer:** bounds packet/frame payload per link; encapsulation and blocked path-MTU discovery can create large-packet black holes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-06

- [ ] **Question:** What is Fragmentation, and why does it matter in Networking?
> **Covered in:** [OSI and TCP/IP models — Complete curriculum checklist](01-osi-and-tcp-ip-models/README.md#complete-curriculum-checklist)

**Answer:** is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-07

- [ ] **Question:** What is Path MTU discovery, and why does it matter in Networking?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-08

- [ ] **Code:** **Question:** What does `tcpdump -ni any 'host IP and port PORT'` help you verify for Networking?
> **Covered in:** [OSI and TCP/IP models — Command and configuration lab](01-osi-and-tcp-ip-models/README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-NETWORKING-JN-09

- [ ] **Code:** **Question:** What does `ip -br addr; ip route; ip neigh` help you verify for Networking?
> **Covered in:** [OSI and TCP/IP models — Command and configuration lab](01-osi-and-tcp-ip-models/README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-NETWORKING-JN-10

- [ ] **Code:** **Question:** What does `dig +trace NAME` help you verify for Networking?
> **Covered in:** [Networking — DNS, HTTP and TLS](README.md#dns-http-and-tls)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-NETWORKING-JP-01

- [ ] **Code:** **Question:** A basic Physical, data-link, network and transport layers check fails. What would you do first using the CLI?
> **Covered in:** [IP addressing — Command and configuration lab](02-ip-addressing/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-02

- [ ] **Question:** A basic Application protocols check fails. What would you do first?
> **Covered in:** [OSI and TCP/IP models — Command and configuration lab](01-osi-and-tcp-ip-models/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-03

- [ ] **Question:** A basic Encapsulation check fails. What would you do first?
> **Covered in:** [OSI and TCP/IP models — Command and configuration lab](01-osi-and-tcp-ip-models/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk URL` and capture exact status/reason/request ID. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-04

- [ ] **Code:** **Question:** A basic Packets, frames and segments check fails. What would you do first using the CLI?
> **Covered in:** [OSI and TCP/IP models — Command and configuration lab](01-osi-and-tcp-ip-models/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any 'host IP and port PORT'` and capture exact status/reason/request ID. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-05

- [ ] **Question:** A basic MTU check fails. What would you do first?
> **Covered in:** [OSI and TCP/IP models — Command and configuration lab](01-osi-and-tcp-ip-models/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. bounds packet/frame payload per link; encapsulation and blocked path-MTU discovery can create large-packet black holes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-06

- [ ] **Question:** A basic Fragmentation check fails. What would you do first?
> **Covered in:** [OSI and TCP/IP models — Command and configuration lab](01-osi-and-tcp-ip-models/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-07

- [ ] **Code:** **Question:** A basic Path MTU discovery check fails. What would you do first using the CLI?
> **Covered in:** [OSI and TCP/IP models — Command and configuration lab](01-osi-and-tcp-ip-models/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk URL` and capture exact status/reason/request ID. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-08

- [ ] **Question:** A basic IPv4 check fails. What would you do first?
> **Covered in:** [OSI and TCP/IP models — Command and configuration lab](01-osi-and-tcp-ip-models/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any 'host IP and port PORT'` and capture exact status/reason/request ID. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-09

- [ ] **Question:** A basic IPv6 check fails. What would you do first?
> **Covered in:** [OSI and TCP/IP models — Command and configuration lab](01-osi-and-tcp-ip-models/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-10

- [ ] **Code:** **Question:** A basic Public and private addresses check fails. What would you do first using the CLI?
> **Covered in:** [OSI and TCP/IP models — Command and configuration lab](01-osi-and-tcp-ip-models/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-NETWORKING-MN-01

- [ ] **Question:** Compare Physical, data-link, network and transport layers with Application protocols. When would each change your design?
> **Covered in:** [OSI and TCP/IP models — Complete curriculum checklist](01-osi-and-tcp-ip-models/README.md#complete-curriculum-checklist)

**Answer:** Physical, data-link, network and transport layers: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Application protocols: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-02

- [ ] **Question:** Compare Application protocols with Encapsulation. When would each change your design?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Application protocols: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Encapsulation: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-03

- [ ] **Question:** Compare Encapsulation with Packets, frames and segments. When would each change your design?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Encapsulation: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Packets, frames and segments: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-04

- [ ] **Configuration review:** **Question:** Compare Packets, frames and segments with MTU. When would each change your design?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Packets, frames and segments: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. MTU: bounds packet/frame payload per link; encapsulation and blocked path-MTU discovery can create large-packet black holes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-05

- [ ] **Question:** Compare MTU with Fragmentation. When would each change your design?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** MTU: bounds packet/frame payload per link; encapsulation and blocked path-MTU discovery can create large-packet black holes. Fragmentation: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-06

- [ ] **Question:** Compare Fragmentation with Path MTU discovery. When would each change your design?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Fragmentation: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Path MTU discovery: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-07

- [ ] **Configuration review:** **Question:** Compare Path MTU discovery with IPv4. When would each change your design?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Path MTU discovery: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. IPv4: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-08

- [ ] **Question:** Compare IPv4 with IPv6. When would each change your design?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** IPv4: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. IPv6: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-09

- [ ] **Question:** Compare IPv6 with Public and private addresses. When would each change your design?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** IPv6: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Public and private addresses: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-10

- [ ] **Configuration review:** **Question:** Compare Public and private addresses with Physical, data-link, network and transport layers. When would each change your design?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Public and private addresses: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Physical, data-link, network and transport layers: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-NETWORKING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Physical, data-link, network and transport layers; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [OSI and TCP/IP models — Complete curriculum checklist](01-osi-and-tcp-ip-models/README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-02

- [ ] **Question:** Production is degraded around Application protocols; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Troubleshooting sequence](README.md#troubleshooting-sequence)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Encapsulation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Troubleshooting sequence](README.md#troubleshooting-sequence)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk URL` plus recent events/changes, then correlate the service-specific SLI. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-04

- [ ] **Question:** Production is degraded around Packets, frames and segments; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Troubleshooting sequence](README.md#troubleshooting-sequence)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any 'host IP and port PORT'` plus recent events/changes, then correlate the service-specific SLI. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around MTU; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Troubleshooting sequence](README.md#troubleshooting-sequence)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. bounds packet/frame payload per link; encapsulation and blocked path-MTU discovery can create large-packet black holes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-06

- [ ] **Question:** Production is degraded around Fragmentation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Troubleshooting sequence](README.md#troubleshooting-sequence)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Path MTU discovery; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Troubleshooting sequence](README.md#troubleshooting-sequence)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk URL` plus recent events/changes, then correlate the service-specific SLI. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-08

- [ ] **Question:** Production is degraded around IPv4; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Troubleshooting sequence](README.md#troubleshooting-sequence)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any 'host IP and port PORT'` plus recent events/changes, then correlate the service-specific SLI. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around IPv6; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Troubleshooting sequence](README.md#troubleshooting-sequence)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-10

- [ ] **Question:** Production is degraded around Public and private addresses; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Troubleshooting sequence](README.md#troubleshooting-sequence)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-NETWORKING-SN-01

- [ ] **Question:** Design a production Networking capability where Physical, data-link, network and transport layers, Packets, frames and segments and Path MTU discovery are first-class requirements.
> **Covered in:** [OSI and TCP/IP models — Complete curriculum checklist](01-osi-and-tcp-ip-models/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where Application protocols, MTU and IPv4 are first-class requirements.
> **Covered in:** [OSI and TCP/IP models — Senior design checklist](01-osi-and-tcp-ip-models/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. bounds packet/frame payload per link; encapsulation and blocked path-MTU discovery can create large-packet black holes. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-03

- [ ] **Question:** Design a production Networking capability where Encapsulation, Fragmentation and IPv6 are first-class requirements.
> **Covered in:** [OSI and TCP/IP models — Senior design checklist](01-osi-and-tcp-ip-models/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where Packets, frames and segments, Path MTU discovery and Public and private addresses are first-class requirements.
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-05

- [ ] **Question:** Design a production Networking capability where MTU, IPv4 and Physical, data-link, network and transport layers are first-class requirements.
> **Covered in:** [OSI and TCP/IP models — Complete curriculum checklist](01-osi-and-tcp-ip-models/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bounds packet/frame payload per link; encapsulation and blocked path-MTU discovery can create large-packet black holes. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where Fragmentation, IPv6 and Application protocols are first-class requirements.
> **Covered in:** [OSI and TCP/IP models — Senior design checklist](01-osi-and-tcp-ip-models/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-07

- [ ] **Question:** Design a production Networking capability where Path MTU discovery, Public and private addresses and Encapsulation are first-class requirements.
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where IPv4, Physical, data-link, network and transport layers and Packets, frames and segments are first-class requirements.
> **Covered in:** [OSI and TCP/IP models — Complete curriculum checklist](01-osi-and-tcp-ip-models/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-09

- [ ] **Question:** Design a production Networking capability where IPv6, Application protocols and MTU are first-class requirements.
> **Covered in:** [OSI and TCP/IP models — Senior design checklist](01-osi-and-tcp-ip-models/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. bounds packet/frame payload per link; encapsulation and blocked path-MTU discovery can create large-packet black holes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where Public and private addresses, Encapsulation and Fragmentation are first-class requirements.
> **Covered in:** [OSI and TCP/IP models — Senior design checklist](01-osi-and-tcp-ip-models/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-NETWORKING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Physical, data-link, network and transport layers. How do you lead it end to end?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Application protocols. How do you lead it end to end?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Encapsulation. How do you lead it end to end?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk URL` as one read-only checkpoint, not the whole diagnosis. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Packets, frames and segments. How do you lead it end to end?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any 'host IP and port PORT'` as one read-only checkpoint, not the whole diagnosis. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving MTU. How do you lead it end to end?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. bounds packet/frame payload per link; encapsulation and blocked path-MTU discovery can create large-packet black holes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Fragmentation. How do you lead it end to end?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Path MTU discovery. How do you lead it end to end?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk URL` as one read-only checkpoint, not the whole diagnosis. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IPv4. How do you lead it end to end?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any 'host IP and port PORT'` as one read-only checkpoint, not the whole diagnosis. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IPv6. How do you lead it end to end?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Public and private addresses. How do you lead it end to end?
> **Covered in:** [OSI and TCP/IP models — Beginner → mid-level → senior learning path](01-osi-and-tcp-ip-models/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of Networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Essential Linux commands](../02-linux/12-essential-linux-commands/README.md) · [Study note](README.md) · [Next: OSI and TCP/IP models →](01-osi-and-tcp-ip-models/README.md)

<!-- reading-navigation:end -->
