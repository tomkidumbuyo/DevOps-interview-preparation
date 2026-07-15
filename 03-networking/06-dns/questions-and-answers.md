# DNS — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### DNS-JN-01

- [ ] **Question:** What is DNS hierarchy, and why does it matter in DNS?
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DNS-JN-02

- [ ] **Question:** What is Recursive and authoritative resolvers, and why does it matter in DNS?
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DNS-JN-03

- [ ] **Question:** What is A, AAAA, CNAME, MX, TXT, NS and SRV records, and why does it matter in DNS?
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DNS-JN-04

- [ ] **Question:** What is TTL, and why does it matter in DNS?
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DNS-JN-05

- [ ] **Question:** What is Negative caching, and why does it matter in DNS?
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DNS-JN-06

- [ ] **Question:** What is Split-horizon DNS, and why does it matter in DNS?
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DNS-JN-07

- [ ] **Question:** What is DNSSEC, and why does it matter in DNS?
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** authenticates DNS data with a signed chain of trust but does not encrypt queries and requires careful key/delegation rollover. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DNS-JN-08

- [ ] **Code:** **Question:** What does `tcpdump -ni any 'host IP and port PORT'` help you verify for DNS?
> **Covered in:** [DNS — Hands-on practice: setup → failure → verification → cleanup](README.md#hands-on-practice-setup-failure-verification-cleanup)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### DNS-JN-09

- [ ] **Code:** **Question:** What does `ip -br addr; ip route; ip neigh` help you verify for DNS?
> **Covered in:** [DNS — Hands-on practice: setup → failure → verification → cleanup](README.md#hands-on-practice-setup-failure-verification-cleanup)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair.

### DNS-JN-10

- [ ] **Code:** **Question:** What does `dig +trace NAME` help you verify for DNS?
> **Covered in:** [DNS — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### DNS-JP-01

- [ ] **Code:** **Question:** A basic DNS hierarchy check fails. What would you do first using the CLI?
> **Covered in:** [DNS — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DNS-JP-02

- [ ] **Question:** A basic Recursive and authoritative resolvers check fails. What would you do first?
> **Covered in:** [DNS — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DNS-JP-03

- [ ] **Question:** A basic A, AAAA, CNAME, MX, TXT, NS and SRV records check fails. What would you do first?
> **Covered in:** [DNS — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk URL` and capture exact status/reason/request ID. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DNS-JP-04

- [ ] **Code:** **Question:** A basic TTL check fails. What would you do first using the CLI?
> **Covered in:** [DNS — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any 'host IP and port PORT'` and capture exact status/reason/request ID. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DNS-JP-05

- [ ] **Question:** A basic Negative caching check fails. What would you do first?
> **Covered in:** [DNS — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DNS-JP-06

- [ ] **Question:** A basic Split-horizon DNS check fails. What would you do first?
> **Covered in:** [DNS — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DNS-JP-07

- [ ] **Code:** **Question:** A basic DNSSEC check fails. What would you do first using the CLI?
> **Covered in:** [DNS — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk URL` and capture exact status/reason/request ID. authenticates DNS data with a signed chain of trust but does not encrypt queries and requires careful key/delegation rollover. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DNS-JP-08

- [ ] **Question:** A basic Service discovery check fails. What would you do first?
> **Covered in:** [DNS — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any 'host IP and port PORT'` and capture exact status/reason/request ID. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DNS-JP-09

- [ ] **Question:** A basic DNS troubleshooting check fails. What would you do first?
> **Covered in:** [DNS — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DNS-JP-10

- [ ] **Code:** **Question:** A basic DNS hierarchy check fails. What would you do first using the CLI?
> **Covered in:** [DNS — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### DNS-MN-01

- [ ] **Question:** Compare DNS hierarchy with Recursive and authoritative resolvers. When would each change your design?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** DNS hierarchy: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Recursive and authoritative resolvers: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DNS-MN-02

- [ ] **Question:** Compare Recursive and authoritative resolvers with A, AAAA, CNAME, MX, TXT, NS and SRV records. When would each change your design?
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Recursive and authoritative resolvers: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. A, AAAA, CNAME, MX, TXT, NS and SRV records: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DNS-MN-03

- [ ] **Question:** Compare A, AAAA, CNAME, MX, TXT, NS and SRV records with TTL. When would each change your design?
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** A, AAAA, CNAME, MX, TXT, NS and SRV records: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. TTL: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DNS-MN-04

- [ ] **Configuration review:** **Question:** Compare TTL with Negative caching. When would each change your design?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** TTL: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Negative caching: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DNS-MN-05

- [ ] **Question:** Compare Negative caching with Split-horizon DNS. When would each change your design?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Negative caching: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Split-horizon DNS: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DNS-MN-06

- [ ] **Question:** Compare Split-horizon DNS with DNSSEC. When would each change your design?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Split-horizon DNS: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. DNSSEC: authenticates DNS data with a signed chain of trust but does not encrypt queries and requires careful key/delegation rollover. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DNS-MN-07

- [ ] **Configuration review:** **Question:** Compare DNSSEC with Service discovery. When would each change your design?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** DNSSEC: authenticates DNS data with a signed chain of trust but does not encrypt queries and requires careful key/delegation rollover. Service discovery: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DNS-MN-08

- [ ] **Question:** Compare Service discovery with DNS troubleshooting. When would each change your design?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Service discovery: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. DNS troubleshooting: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DNS-MN-09

- [ ] **Question:** Compare DNS troubleshooting with DNS hierarchy. When would each change your design?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** DNS troubleshooting: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. DNS hierarchy: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DNS-MN-10

- [ ] **Configuration review:** **Question:** Compare DNS hierarchy with DNS hierarchy. When would each change your design?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** DNS hierarchy: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. DNS hierarchy: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### DNS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around DNS hierarchy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DNS-MP-02

- [ ] **Question:** Production is degraded around Recursive and authoritative resolvers; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DNS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around A, AAAA, CNAME, MX, TXT, NS and SRV records; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk URL` plus recent events/changes, then correlate the service-specific SLI. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DNS-MP-04

- [ ] **Question:** Production is degraded around TTL; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any 'host IP and port PORT'` plus recent events/changes, then correlate the service-specific SLI. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DNS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Negative caching; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DNS-MP-06

- [ ] **Question:** Production is degraded around Split-horizon DNS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DNS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around DNSSEC; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk URL` plus recent events/changes, then correlate the service-specific SLI. authenticates DNS data with a signed chain of trust but does not encrypt queries and requires careful key/delegation rollover. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DNS-MP-08

- [ ] **Question:** Production is degraded around Service discovery; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any 'host IP and port PORT'` plus recent events/changes, then correlate the service-specific SLI. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DNS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around DNS troubleshooting; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DNS-MP-10

- [ ] **Question:** Production is degraded around DNS hierarchy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### DNS-SN-01

- [ ] **Question:** Design a production DNS capability where DNS hierarchy, TTL and DNSSEC are first-class requirements.
> **Covered in:** [DNS — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. authenticates DNS data with a signed chain of trust but does not encrypt queries and requires careful key/delegation rollover. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DNS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production DNS capability where Recursive and authoritative resolvers, Negative caching and Service discovery are first-class requirements.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DNS-SN-03

- [ ] **Question:** Design a production DNS capability where A, AAAA, CNAME, MX, TXT, NS and SRV records, Split-horizon DNS and DNS troubleshooting are first-class requirements.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DNS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production DNS capability where TTL, DNSSEC and DNS hierarchy are first-class requirements.
> **Covered in:** [DNS — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. authenticates DNS data with a signed chain of trust but does not encrypt queries and requires careful key/delegation rollover. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DNS-SN-05

- [ ] **Question:** Design a production DNS capability where Negative caching, Service discovery and DNS hierarchy are first-class requirements.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DNS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production DNS capability where Split-horizon DNS, DNS troubleshooting and Recursive and authoritative resolvers are first-class requirements.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DNS-SN-07

- [ ] **Question:** Design a production DNS capability where DNSSEC, DNS hierarchy and A, AAAA, CNAME, MX, TXT, NS and SRV records are first-class requirements.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: authenticates DNS data with a signed chain of trust but does not encrypt queries and requires careful key/delegation rollover. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DNS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production DNS capability where Service discovery, DNS hierarchy and TTL are first-class requirements.
> **Covered in:** [DNS — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DNS-SN-09

- [ ] **Question:** Design a production DNS capability where DNS troubleshooting, Recursive and authoritative resolvers and Negative caching are first-class requirements.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DNS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production DNS capability where DNS hierarchy, A, AAAA, CNAME, MX, TXT, NS and SRV records and Split-horizon DNS are first-class requirements.
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### DNS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DNS hierarchy. How do you lead it end to end?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DNS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Recursive and authoritative resolvers. How do you lead it end to end?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DNS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving A, AAAA, CNAME, MX, TXT, NS and SRV records. How do you lead it end to end?
> **Covered in:** [DNS — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk URL` as one read-only checkpoint, not the whole diagnosis. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DNS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TTL. How do you lead it end to end?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any 'host IP and port PORT'` as one read-only checkpoint, not the whole diagnosis. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DNS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Negative caching. How do you lead it end to end?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DNS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Split-horizon DNS. How do you lead it end to end?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DNS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DNSSEC. How do you lead it end to end?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk URL` as one read-only checkpoint, not the whole diagnosis. authenticates DNS data with a signed chain of trust but does not encrypt queries and requires careful key/delegation rollover. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DNS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service discovery. How do you lead it end to end?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any 'host IP and port PORT'` as one read-only checkpoint, not the whole diagnosis. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DNS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DNS troubleshooting. How do you lead it end to end?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DNS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DNS hierarchy. How do you lead it end to end?
> **Covered in:** [DNS — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of DNS; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: TCP and UDP](../05-tcp-and-udp/README.md) · [Study note](README.md) · [Next: HTTP →](../07-http/README.md)

<!-- reading-navigation:end -->
