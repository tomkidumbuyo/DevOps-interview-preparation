# API and service architecture — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### API-AND-SERVICE-ARCHITECTURE-JN-01

- [ ] **Question:** What is REST, and why does it matter in API and service architecture?
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### API-AND-SERVICE-ARCHITECTURE-JN-02

- [ ] **Question:** What is gRPC, and why does it matter in API and service architecture?
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** uses protobuf contracts and HTTP/2 for typed unary or streaming RPCs, requiring deadline, status, load-balancing and compatibility discipline. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### API-AND-SERVICE-ARCHITECTURE-JN-03

- [ ] **Question:** What is WebSockets, and why does it matter in API and service architecture?
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### API-AND-SERVICE-ARCHITECTURE-JN-04

- [ ] **Question:** What is Streaming APIs, and why does it matter in API and service architecture?
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### API-AND-SERVICE-ARCHITECTURE-JN-05

- [ ] **Question:** What is Synchronous versus asynchronous communication, and why does it matter in API and service architecture?
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### API-AND-SERVICE-ARCHITECTURE-JN-06

- [ ] **Question:** What is API versioning, and why does it matter in API and service architecture?
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### API-AND-SERVICE-ARCHITECTURE-JN-07

- [ ] **Question:** What is Pagination, and why does it matter in API and service architecture?
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### API-AND-SERVICE-ARCHITECTURE-JN-08

- [ ] **Code:** **Question:** What does `dig NAME` help you verify for API and service architecture?
> **Covered in:** [API and service architecture — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### API-AND-SERVICE-ARCHITECTURE-JN-09

- [ ] **Code:** **Question:** What does `lscpu; free -h; lsblk; ip -br addr` help you verify for API and service architecture?
> **Covered in:** [API and service architecture — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### API-AND-SERVICE-ARCHITECTURE-JN-10

- [ ] **Code:** **Question:** What does `ss -s` help you verify for API and service architecture?
> **Covered in:** [API and service architecture — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit.

## Junior — procedural and command questions

### API-AND-SERVICE-ARCHITECTURE-JP-01

- [ ] **Code:** **Question:** A basic REST check fails. What would you do first using the CLI?
> **Covered in:** [API and service architecture — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### API-AND-SERVICE-ARCHITECTURE-JP-02

- [ ] **Question:** A basic gRPC check fails. What would you do first?
> **Covered in:** [API and service architecture — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. uses protobuf contracts and HTTP/2 for typed unary or streaming RPCs, requiring deadline, status, load-balancing and compatibility discipline. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### API-AND-SERVICE-ARCHITECTURE-JP-03

- [ ] **Question:** A basic WebSockets check fails. What would you do first?
> **Covered in:** [API and service architecture — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### API-AND-SERVICE-ARCHITECTURE-JP-04

- [ ] **Code:** **Question:** A basic Streaming APIs check fails. What would you do first using the CLI?
> **Covered in:** [API and service architecture — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### API-AND-SERVICE-ARCHITECTURE-JP-05

- [ ] **Question:** A basic Synchronous versus asynchronous communication check fails. What would you do first?
> **Covered in:** [API and service architecture — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### API-AND-SERVICE-ARCHITECTURE-JP-06

- [ ] **Question:** A basic API versioning check fails. What would you do first?
> **Covered in:** [API and service architecture — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### API-AND-SERVICE-ARCHITECTURE-JP-07

- [ ] **Code:** **Question:** A basic Pagination check fails. What would you do first using the CLI?
> **Covered in:** [API and service architecture — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### API-AND-SERVICE-ARCHITECTURE-JP-08

- [ ] **Question:** A basic Request correlation check fails. What would you do first?
> **Covered in:** [API and service architecture — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### API-AND-SERVICE-ARCHITECTURE-JP-09

- [ ] **Question:** A basic Service discovery check fails. What would you do first?
> **Covered in:** [API and service architecture — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### API-AND-SERVICE-ARCHITECTURE-JP-10

- [ ] **Code:** **Question:** A basic REST check fails. What would you do first using the CLI?
> **Covered in:** [API and service architecture — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### API-AND-SERVICE-ARCHITECTURE-MN-01

- [ ] **Question:** Compare REST with gRPC. When would each change your design?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** REST: models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. gRPC: uses protobuf contracts and HTTP/2 for typed unary or streaming RPCs, requiring deadline, status, load-balancing and compatibility discipline. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### API-AND-SERVICE-ARCHITECTURE-MN-02

- [ ] **Question:** Compare gRPC with WebSockets. When would each change your design?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** gRPC: uses protobuf contracts and HTTP/2 for typed unary or streaming RPCs, requiring deadline, status, load-balancing and compatibility discipline. WebSockets: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### API-AND-SERVICE-ARCHITECTURE-MN-03

- [ ] **Question:** Compare WebSockets with Streaming APIs. When would each change your design?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** WebSockets: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Streaming APIs: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### API-AND-SERVICE-ARCHITECTURE-MN-04

- [ ] **Configuration review:** **Question:** Compare Streaming APIs with Synchronous versus asynchronous communication. When would each change your design?
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Streaming APIs: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Synchronous versus asynchronous communication: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### API-AND-SERVICE-ARCHITECTURE-MN-05

- [ ] **Question:** Compare Synchronous versus asynchronous communication with API versioning. When would each change your design?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Synchronous versus asynchronous communication: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. API versioning: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### API-AND-SERVICE-ARCHITECTURE-MN-06

- [ ] **Question:** Compare API versioning with Pagination. When would each change your design?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** API versioning: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Pagination: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### API-AND-SERVICE-ARCHITECTURE-MN-07

- [ ] **Configuration review:** **Question:** Compare Pagination with Request correlation. When would each change your design?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Pagination: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Request correlation: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### API-AND-SERVICE-ARCHITECTURE-MN-08

- [ ] **Question:** Compare Request correlation with Service discovery. When would each change your design?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Request correlation: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Service discovery: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### API-AND-SERVICE-ARCHITECTURE-MN-09

- [ ] **Question:** Compare Service discovery with REST. When would each change your design?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Service discovery: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. REST: models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### API-AND-SERVICE-ARCHITECTURE-MN-10

- [ ] **Configuration review:** **Question:** Compare REST with REST. When would each change your design?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** REST: models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. REST: models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### API-AND-SERVICE-ARCHITECTURE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around REST; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### API-AND-SERVICE-ARCHITECTURE-MP-02

- [ ] **Question:** Production is degraded around gRPC; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. uses protobuf contracts and HTTP/2 for typed unary or streaming RPCs, requiring deadline, status, load-balancing and compatibility discipline. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### API-AND-SERVICE-ARCHITECTURE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around WebSockets; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### API-AND-SERVICE-ARCHITECTURE-MP-04

- [ ] **Question:** Production is degraded around Streaming APIs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### API-AND-SERVICE-ARCHITECTURE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Synchronous versus asynchronous communication; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### API-AND-SERVICE-ARCHITECTURE-MP-06

- [ ] **Question:** Production is degraded around API versioning; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### API-AND-SERVICE-ARCHITECTURE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pagination; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### API-AND-SERVICE-ARCHITECTURE-MP-08

- [ ] **Question:** Production is degraded around Request correlation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### API-AND-SERVICE-ARCHITECTURE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Service discovery; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### API-AND-SERVICE-ARCHITECTURE-MP-10

- [ ] **Question:** Production is degraded around REST; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### API-AND-SERVICE-ARCHITECTURE-SN-01

- [ ] **Question:** Design a production API and service architecture capability where REST, Streaming APIs and Pagination are first-class requirements.
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### API-AND-SERVICE-ARCHITECTURE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production API and service architecture capability where gRPC, Synchronous versus asynchronous communication and Request correlation are first-class requirements.
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: uses protobuf contracts and HTTP/2 for typed unary or streaming RPCs, requiring deadline, status, load-balancing and compatibility discipline. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### API-AND-SERVICE-ARCHITECTURE-SN-03

- [ ] **Question:** Design a production API and service architecture capability where WebSockets, API versioning and Service discovery are first-class requirements.
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### API-AND-SERVICE-ARCHITECTURE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production API and service architecture capability where Streaming APIs, Pagination and REST are first-class requirements.
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### API-AND-SERVICE-ARCHITECTURE-SN-05

- [ ] **Question:** Design a production API and service architecture capability where Synchronous versus asynchronous communication, Request correlation and REST are first-class requirements.
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### API-AND-SERVICE-ARCHITECTURE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production API and service architecture capability where API versioning, Service discovery and gRPC are first-class requirements.
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. uses protobuf contracts and HTTP/2 for typed unary or streaming RPCs, requiring deadline, status, load-balancing and compatibility discipline. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### API-AND-SERVICE-ARCHITECTURE-SN-07

- [ ] **Question:** Design a production API and service architecture capability where Pagination, REST and WebSockets are first-class requirements.
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### API-AND-SERVICE-ARCHITECTURE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production API and service architecture capability where Request correlation, REST and Streaming APIs are first-class requirements.
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### API-AND-SERVICE-ARCHITECTURE-SN-09

- [ ] **Question:** Design a production API and service architecture capability where Service discovery, gRPC and Synchronous versus asynchronous communication are first-class requirements.
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. uses protobuf contracts and HTTP/2 for typed unary or streaming RPCs, requiring deadline, status, load-balancing and compatibility discipline. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### API-AND-SERVICE-ARCHITECTURE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production API and service architecture capability where REST, WebSockets and API versioning are first-class requirements.
> **Covered in:** [API and service architecture — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### API-AND-SERVICE-ARCHITECTURE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving REST. How do you lead it end to end?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### API-AND-SERVICE-ARCHITECTURE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving gRPC. How do you lead it end to end?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. uses protobuf contracts and HTTP/2 for typed unary or streaming RPCs, requiring deadline, status, load-balancing and compatibility discipline. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### API-AND-SERVICE-ARCHITECTURE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving WebSockets. How do you lead it end to end?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### API-AND-SERVICE-ARCHITECTURE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Streaming APIs. How do you lead it end to end?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### API-AND-SERVICE-ARCHITECTURE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Synchronous versus asynchronous communication. How do you lead it end to end?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### API-AND-SERVICE-ARCHITECTURE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving API versioning. How do you lead it end to end?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### API-AND-SERVICE-ARCHITECTURE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pagination. How do you lead it end to end?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### API-AND-SERVICE-ARCHITECTURE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Request correlation. How do you lead it end to end?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### API-AND-SERVICE-ARCHITECTURE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service discovery. How do you lead it end to end?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. is part of API and service architecture; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### API-AND-SERVICE-ARCHITECTURE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving REST. How do you lead it end to end?
> **Covered in:** [API and service architecture — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Resilience patterns](../05-resilience-patterns/README.md) · [Study note](README.md) · [Next: Architecture styles →](../07-architecture-styles/README.md)

<!-- reading-navigation:end -->
