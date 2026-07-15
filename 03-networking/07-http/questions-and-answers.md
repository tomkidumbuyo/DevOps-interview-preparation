# HTTP — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### HTTP-JN-01

- [ ] **Question:** What is HTTP methods, and why does it matter in HTTP?
> **Covered in:** [HTTP — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HTTP-JN-02

- [ ] **Question:** What is Headers, and why does it matter in HTTP?
> **Covered in:** [HTTP — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HTTP-JN-03

- [ ] **Question:** What is Status codes, and why does it matter in HTTP?
> **Covered in:** [HTTP — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HTTP-JN-04

- [ ] **Question:** What is Cookies, and why does it matter in HTTP?
> **Covered in:** [HTTP — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HTTP-JN-05

- [ ] **Question:** What is Keep-alive, and why does it matter in HTTP?
> **Covered in:** [HTTP — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HTTP-JN-06

- [ ] **Question:** What is HTTP/1.1, and why does it matter in HTTP?
> **Covered in:** [HTTP — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HTTP-JN-07

- [ ] **Question:** What is HTTP/2, and why does it matter in HTTP?
> **Covered in:** [HTTP — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** multiplexes streams over one TCP connection with header compression, but connection loss and transport head-of-line effects remain. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HTTP-JN-08

- [ ] **Code:** **Question:** What does `tcpdump -ni any 'host IP and port PORT'` help you verify for HTTP?
> **Covered in:** [HTTP — Hands-on practice: setup → failure → verification → cleanup](README.md#hands-on-practice-setup-failure-verification-cleanup)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### HTTP-JN-09

- [ ] **Code:** **Question:** What does `ip -br addr; ip route; ip neigh` help you verify for HTTP?
> **Covered in:** [HTTP — Hands-on practice: setup → failure → verification → cleanup](README.md#hands-on-practice-setup-failure-verification-cleanup)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### HTTP-JN-10

- [ ] **Code:** **Question:** What does `dig +trace NAME` help you verify for HTTP?
> **Covered in:** [HTTP — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### HTTP-JP-01

- [ ] **Code:** **Question:** A basic HTTP methods check fails. What would you do first using the CLI?
> **Covered in:** [HTTP — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HTTP-JP-02

- [ ] **Question:** A basic Headers check fails. What would you do first?
> **Covered in:** [HTTP — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HTTP-JP-03

- [ ] **Question:** A basic Status codes check fails. What would you do first?
> **Covered in:** [HTTP — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk URL` and capture exact status/reason/request ID. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HTTP-JP-04

- [ ] **Code:** **Question:** A basic Cookies check fails. What would you do first using the CLI?
> **Covered in:** [HTTP — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any 'host IP and port PORT'` and capture exact status/reason/request ID. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HTTP-JP-05

- [ ] **Question:** A basic Keep-alive check fails. What would you do first?
> **Covered in:** [HTTP — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HTTP-JP-06

- [ ] **Question:** A basic HTTP/1.1 check fails. What would you do first?
> **Covered in:** [HTTP — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HTTP-JP-07

- [ ] **Code:** **Question:** A basic HTTP/2 check fails. What would you do first using the CLI?
> **Covered in:** [HTTP — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk URL` and capture exact status/reason/request ID. multiplexes streams over one TCP connection with header compression, but connection loss and transport head-of-line effects remain. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HTTP-JP-08

- [ ] **Question:** A basic HTTP/3 check fails. What would you do first?
> **Covered in:** [HTTP — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `tcpdump -ni any 'host IP and port PORT'` and capture exact status/reason/request ID. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HTTP-JP-09

- [ ] **Question:** A basic Chunked encoding check fails. What would you do first?
> **Covered in:** [HTTP — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip -br addr; ip route; ip neigh` and capture exact status/reason/request ID. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HTTP-JP-10

- [ ] **Code:** **Question:** A basic Streaming check fails. What would you do first using the CLI?
> **Covered in:** [HTTP — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### HTTP-MN-01

- [ ] **Question:** Compare HTTP methods with Headers. When would each change your design?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** HTTP methods: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Headers: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HTTP-MN-02

- [ ] **Question:** Compare Headers with Status codes. When would each change your design?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Headers: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Status codes: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HTTP-MN-03

- [ ] **Question:** Compare Status codes with Cookies. When would each change your design?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Status codes: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Cookies: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HTTP-MN-04

- [ ] **Configuration review:** **Question:** Compare Cookies with Keep-alive. When would each change your design?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Cookies: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Keep-alive: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HTTP-MN-05

- [ ] **Question:** Compare Keep-alive with HTTP/1.1. When would each change your design?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Keep-alive: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. HTTP/1.1: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HTTP-MN-06

- [ ] **Question:** Compare HTTP/1.1 with HTTP/2. When would each change your design?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** HTTP/1.1: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. HTTP/2: multiplexes streams over one TCP connection with header compression, but connection loss and transport head-of-line effects remain. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HTTP-MN-07

- [ ] **Configuration review:** **Question:** Compare HTTP/2 with HTTP/3. When would each change your design?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** HTTP/2: multiplexes streams over one TCP connection with header compression, but connection loss and transport head-of-line effects remain. HTTP/3: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HTTP-MN-08

- [ ] **Question:** Compare HTTP/3 with Chunked encoding. When would each change your design?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** HTTP/3: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Chunked encoding: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HTTP-MN-09

- [ ] **Question:** Compare Chunked encoding with Streaming. When would each change your design?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Chunked encoding: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Streaming: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HTTP-MN-10

- [ ] **Configuration review:** **Question:** Compare Streaming with HTTP methods. When would each change your design?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Streaming: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. HTTP methods: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### HTTP-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around HTTP methods; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HTTP-MP-02

- [ ] **Question:** Production is degraded around Headers; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HTTP-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Status codes; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk URL` plus recent events/changes, then correlate the service-specific SLI. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HTTP-MP-04

- [ ] **Question:** Production is degraded around Cookies; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any 'host IP and port PORT'` plus recent events/changes, then correlate the service-specific SLI. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HTTP-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Keep-alive; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HTTP-MP-06

- [ ] **Question:** Production is degraded around HTTP/1.1; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HTTP-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around HTTP/2; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk URL` plus recent events/changes, then correlate the service-specific SLI. multiplexes streams over one TCP connection with header compression, but connection loss and transport head-of-line effects remain. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HTTP-MP-08

- [ ] **Question:** Production is degraded around HTTP/3; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `tcpdump -ni any 'host IP and port PORT'` plus recent events/changes, then correlate the service-specific SLI. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HTTP-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Chunked encoding; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip -br addr; ip route; ip neigh` plus recent events/changes, then correlate the service-specific SLI. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HTTP-MP-10

- [ ] **Question:** Production is degraded around Streaming; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### HTTP-SN-01

- [ ] **Question:** Design a production HTTP capability where HTTP methods, Cookies and HTTP/2 are first-class requirements.
> **Covered in:** [HTTP — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. multiplexes streams over one TCP connection with header compression, but connection loss and transport head-of-line effects remain. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HTTP-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production HTTP capability where Headers, Keep-alive and HTTP/3 are first-class requirements.
> **Covered in:** [HTTP — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HTTP-SN-03

- [ ] **Question:** Design a production HTTP capability where Status codes, HTTP/1.1 and Chunked encoding are first-class requirements.
> **Covered in:** [HTTP — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HTTP-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production HTTP capability where Cookies, HTTP/2 and Streaming are first-class requirements.
> **Covered in:** [HTTP — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. multiplexes streams over one TCP connection with header compression, but connection loss and transport head-of-line effects remain. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HTTP-SN-05

- [ ] **Question:** Design a production HTTP capability where Keep-alive, HTTP/3 and HTTP methods are first-class requirements.
> **Covered in:** [HTTP — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HTTP-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production HTTP capability where HTTP/1.1, Chunked encoding and Headers are first-class requirements.
> **Covered in:** [HTTP — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HTTP-SN-07

- [ ] **Question:** Design a production HTTP capability where HTTP/2, Streaming and Status codes are first-class requirements.
> **Covered in:** [HTTP — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: multiplexes streams over one TCP connection with header compression, but connection loss and transport head-of-line effects remain. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HTTP-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production HTTP capability where HTTP/3, HTTP methods and Cookies are first-class requirements.
> **Covered in:** [HTTP — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HTTP-SN-09

- [ ] **Question:** Design a production HTTP capability where Chunked encoding, Headers and Keep-alive are first-class requirements.
> **Covered in:** [HTTP — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HTTP-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production HTTP capability where Streaming, Status codes and HTTP/1.1 are first-class requirements.
> **Covered in:** [HTTP — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### HTTP-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving HTTP methods. How do you lead it end to end?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HTTP-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Headers. How do you lead it end to end?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HTTP-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Status codes. How do you lead it end to end?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk URL` as one read-only checkpoint, not the whole diagnosis. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HTTP-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cookies. How do you lead it end to end?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any 'host IP and port PORT'` as one read-only checkpoint, not the whole diagnosis. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HTTP-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Keep-alive. How do you lead it end to end?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HTTP-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving HTTP/1.1. How do you lead it end to end?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HTTP-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving HTTP/2. How do you lead it end to end?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk URL` as one read-only checkpoint, not the whole diagnosis. multiplexes streams over one TCP connection with header compression, but connection loss and transport head-of-line effects remain. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HTTP-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving HTTP/3. How do you lead it end to end?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `tcpdump -ni any 'host IP and port PORT'` as one read-only checkpoint, not the whole diagnosis. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HTTP-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Chunked encoding. How do you lead it end to end?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip -br addr; ip route; ip neigh` as one read-only checkpoint, not the whole diagnosis. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HTTP-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Streaming. How do you lead it end to end?
> **Covered in:** [HTTP — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. is part of HTTP; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: DNS](../06-dns/README.md) · [Study note](README.md) · [Next: TLS and certificates →](../08-tls-and-certificates/README.md)

<!-- reading-navigation:end -->
