# Mega DevOps and AI Platform interview questions and answers

> Mark a question complete by changing `- [ ]` to `- [x]`. This bank contains 180 answered questions; every topic folder has its own additional bank.

# General DevOps foundations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JN-01

- [ ] **Question:** What is Linux resource path, and why does it matter in General DevOps foundations?

**Answer:** CPU, memory, disk, descriptors, processes, cgroups and kernel evidence explain application symptoms. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JN-02

- [ ] **Question:** What is Network request path, and why does it matter in General DevOps foundations?

**Answer:** DNS, route, firewall/NAT, transport, TLS, proxy/load balancer and application must all agree. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JN-03

- [ ] **Question:** What is Distributed failure, and why does it matter in General DevOps foundations?

**Answer:** timeout does not reveal whether a remote side effect occurred, so idempotency and reconciliation matter. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JN-04

- [ ] **Question:** What is Git delivery, and why does it matter in General DevOps foundations?

**Answer:** reviewed source must bind to immutable artifact, provenance, environment and rollback evidence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JN-05

- [ ] **Question:** What is Container isolation, and why does it matter in General DevOps foundations?

**Answer:** namespaces, cgroups, capabilities, seccomp and mounts constrain ordinary host processes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JN-06

- [ ] **Question:** What is CI/CD security, and why does it matter in General DevOps foundations?

**Answer:** untrusted code near runner credentials requires isolation, pinning and short-lived identity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JN-07

- [ ] **Question:** What is Observability, and why does it matter in General DevOps foundations?

**Answer:** metrics, logs, traces and profiles answer distinct questions under cardinality/privacy/cost limits. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JN-08

- [ ] **Code:** **Question:** What does `docker inspect CONTAINER` help you verify for General DevOps foundations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: user outcome target and burn rate guide paging and risk decisions.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JN-09

- [ ] **Code:** **Question:** What does `uptime; vmstat 1; iostat -xz 1` help you verify for General DevOps foundations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: command, containment, evidence, reversible mitigation, verification and prevention form the lifecycle.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JN-10

- [ ] **Code:** **Question:** What does `ip route; ss -lntp; dig NAME; curl -v URL` help you verify for General DevOps foundations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: protected backup plus timed application restore/failover proves RPO and RTO.

## Junior — procedural and command questions

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JP-01

- [ ] **Code:** **Question:** A basic Linux resource path check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `uptime; vmstat 1; iostat -xz 1` and capture exact status/reason/request ID. CPU, memory, disk, descriptors, processes, cgroups and kernel evidence explain application symptoms. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JP-02

- [ ] **Question:** A basic Network request path check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip route; ss -lntp; dig NAME; curl -v URL` and capture exact status/reason/request ID. DNS, route, firewall/NAT, transport, TLS, proxy/load balancer and application must all agree. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JP-03

- [ ] **Question:** A basic Distributed failure check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --graph --oneline --all` and capture exact status/reason/request ID. timeout does not reveal whether a remote side effect occurred, so idempotency and reconciliation matter. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JP-04

- [ ] **Code:** **Question:** A basic Git delivery check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker inspect CONTAINER` and capture exact status/reason/request ID. reviewed source must bind to immutable artifact, provenance, environment and rollback evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JP-05

- [ ] **Question:** A basic Container isolation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `uptime; vmstat 1; iostat -xz 1` and capture exact status/reason/request ID. namespaces, cgroups, capabilities, seccomp and mounts constrain ordinary host processes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JP-06

- [ ] **Question:** A basic CI/CD security check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip route; ss -lntp; dig NAME; curl -v URL` and capture exact status/reason/request ID. untrusted code near runner credentials requires isolation, pinning and short-lived identity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JP-07

- [ ] **Code:** **Question:** A basic Observability check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --graph --oneline --all` and capture exact status/reason/request ID. metrics, logs, traces and profiles answer distinct questions under cardinality/privacy/cost limits. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JP-08

- [ ] **Question:** A basic SLO/error budget check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker inspect CONTAINER` and capture exact status/reason/request ID. user outcome target and burn rate guide paging and risk decisions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JP-09

- [ ] **Question:** A basic Incident response check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `uptime; vmstat 1; iostat -xz 1` and capture exact status/reason/request ID. command, containment, evidence, reversible mitigation, verification and prevention form the lifecycle. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-JP-10

- [ ] **Code:** **Question:** A basic Disaster recovery check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip route; ss -lntp; dig NAME; curl -v URL` and capture exact status/reason/request ID. protected backup plus timed application restore/failover proves RPO and RTO. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MN-01

- [ ] **Question:** Compare Linux resource path with Network request path. When would each change your design?

**Answer:** Linux resource path: CPU, memory, disk, descriptors, processes, cgroups and kernel evidence explain application symptoms. Network request path: DNS, route, firewall/NAT, transport, TLS, proxy/load balancer and application must all agree. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MN-02

- [ ] **Question:** Compare Network request path with Distributed failure. When would each change your design?

**Answer:** Network request path: DNS, route, firewall/NAT, transport, TLS, proxy/load balancer and application must all agree. Distributed failure: timeout does not reveal whether a remote side effect occurred, so idempotency and reconciliation matter. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MN-03

- [ ] **Question:** Compare Distributed failure with Git delivery. When would each change your design?

**Answer:** Distributed failure: timeout does not reveal whether a remote side effect occurred, so idempotency and reconciliation matter. Git delivery: reviewed source must bind to immutable artifact, provenance, environment and rollback evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Git delivery with Container isolation. When would each change your design?

**Answer:** Git delivery: reviewed source must bind to immutable artifact, provenance, environment and rollback evidence. Container isolation: namespaces, cgroups, capabilities, seccomp and mounts constrain ordinary host processes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MN-05

- [ ] **Question:** Compare Container isolation with CI/CD security. When would each change your design?

**Answer:** Container isolation: namespaces, cgroups, capabilities, seccomp and mounts constrain ordinary host processes. CI/CD security: untrusted code near runner credentials requires isolation, pinning and short-lived identity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MN-06

- [ ] **Question:** Compare CI/CD security with Observability. When would each change your design?

**Answer:** CI/CD security: untrusted code near runner credentials requires isolation, pinning and short-lived identity. Observability: metrics, logs, traces and profiles answer distinct questions under cardinality/privacy/cost limits. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Observability with SLO/error budget. When would each change your design?

**Answer:** Observability: metrics, logs, traces and profiles answer distinct questions under cardinality/privacy/cost limits. SLO/error budget: user outcome target and burn rate guide paging and risk decisions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MN-08

- [ ] **Question:** Compare SLO/error budget with Incident response. When would each change your design?

**Answer:** SLO/error budget: user outcome target and burn rate guide paging and risk decisions. Incident response: command, containment, evidence, reversible mitigation, verification and prevention form the lifecycle. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MN-09

- [ ] **Question:** Compare Incident response with Disaster recovery. When would each change your design?

**Answer:** Incident response: command, containment, evidence, reversible mitigation, verification and prevention form the lifecycle. Disaster recovery: protected backup plus timed application restore/failover proves RPO and RTO. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Disaster recovery with Linux resource path. When would each change your design?

**Answer:** Disaster recovery: protected backup plus timed application restore/failover proves RPO and RTO. Linux resource path: CPU, memory, disk, descriptors, processes, cgroups and kernel evidence explain application symptoms. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Linux resource path; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `uptime; vmstat 1; iostat -xz 1` plus recent events/changes, then correlate the service-specific SLI. CPU, memory, disk, descriptors, processes, cgroups and kernel evidence explain application symptoms. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MP-02

- [ ] **Question:** Production is degraded around Network request path; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip route; ss -lntp; dig NAME; curl -v URL` plus recent events/changes, then correlate the service-specific SLI. DNS, route, firewall/NAT, transport, TLS, proxy/load balancer and application must all agree. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Distributed failure; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --graph --oneline --all` plus recent events/changes, then correlate the service-specific SLI. timeout does not reveal whether a remote side effect occurred, so idempotency and reconciliation matter. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MP-04

- [ ] **Question:** Production is degraded around Git delivery; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker inspect CONTAINER` plus recent events/changes, then correlate the service-specific SLI. reviewed source must bind to immutable artifact, provenance, environment and rollback evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Container isolation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `uptime; vmstat 1; iostat -xz 1` plus recent events/changes, then correlate the service-specific SLI. namespaces, cgroups, capabilities, seccomp and mounts constrain ordinary host processes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MP-06

- [ ] **Question:** Production is degraded around CI/CD security; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip route; ss -lntp; dig NAME; curl -v URL` plus recent events/changes, then correlate the service-specific SLI. untrusted code near runner credentials requires isolation, pinning and short-lived identity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Observability; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --graph --oneline --all` plus recent events/changes, then correlate the service-specific SLI. metrics, logs, traces and profiles answer distinct questions under cardinality/privacy/cost limits. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MP-08

- [ ] **Question:** Production is degraded around SLO/error budget; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker inspect CONTAINER` plus recent events/changes, then correlate the service-specific SLI. user outcome target and burn rate guide paging and risk decisions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Incident response; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `uptime; vmstat 1; iostat -xz 1` plus recent events/changes, then correlate the service-specific SLI. command, containment, evidence, reversible mitigation, verification and prevention form the lifecycle. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-MP-10

- [ ] **Question:** Production is degraded around Disaster recovery; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip route; ss -lntp; dig NAME; curl -v URL` plus recent events/changes, then correlate the service-specific SLI. protected backup plus timed application restore/failover proves RPO and RTO. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SN-01

- [ ] **Question:** Design a production General DevOps foundations capability where Linux resource path, Git delivery and Observability are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: CPU, memory, disk, descriptors, processes, cgroups and kernel evidence explain application symptoms. reviewed source must bind to immutable artifact, provenance, environment and rollback evidence. metrics, logs, traces and profiles answer distinct questions under cardinality/privacy/cost limits. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production General DevOps foundations capability where Network request path, Container isolation and SLO/error budget are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: DNS, route, firewall/NAT, transport, TLS, proxy/load balancer and application must all agree. namespaces, cgroups, capabilities, seccomp and mounts constrain ordinary host processes. user outcome target and burn rate guide paging and risk decisions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SN-03

- [ ] **Question:** Design a production General DevOps foundations capability where Distributed failure, CI/CD security and Incident response are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: timeout does not reveal whether a remote side effect occurred, so idempotency and reconciliation matter. untrusted code near runner credentials requires isolation, pinning and short-lived identity. command, containment, evidence, reversible mitigation, verification and prevention form the lifecycle. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production General DevOps foundations capability where Git delivery, Observability and Disaster recovery are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reviewed source must bind to immutable artifact, provenance, environment and rollback evidence. metrics, logs, traces and profiles answer distinct questions under cardinality/privacy/cost limits. protected backup plus timed application restore/failover proves RPO and RTO. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SN-05

- [ ] **Question:** Design a production General DevOps foundations capability where Container isolation, SLO/error budget and Linux resource path are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: namespaces, cgroups, capabilities, seccomp and mounts constrain ordinary host processes. user outcome target and burn rate guide paging and risk decisions. CPU, memory, disk, descriptors, processes, cgroups and kernel evidence explain application symptoms. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production General DevOps foundations capability where CI/CD security, Incident response and Network request path are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: untrusted code near runner credentials requires isolation, pinning and short-lived identity. command, containment, evidence, reversible mitigation, verification and prevention form the lifecycle. DNS, route, firewall/NAT, transport, TLS, proxy/load balancer and application must all agree. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SN-07

- [ ] **Question:** Design a production General DevOps foundations capability where Observability, Disaster recovery and Distributed failure are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: metrics, logs, traces and profiles answer distinct questions under cardinality/privacy/cost limits. protected backup plus timed application restore/failover proves RPO and RTO. timeout does not reveal whether a remote side effect occurred, so idempotency and reconciliation matter. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production General DevOps foundations capability where SLO/error budget, Linux resource path and Git delivery are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: user outcome target and burn rate guide paging and risk decisions. CPU, memory, disk, descriptors, processes, cgroups and kernel evidence explain application symptoms. reviewed source must bind to immutable artifact, provenance, environment and rollback evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SN-09

- [ ] **Question:** Design a production General DevOps foundations capability where Incident response, Network request path and Container isolation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: command, containment, evidence, reversible mitigation, verification and prevention form the lifecycle. DNS, route, firewall/NAT, transport, TLS, proxy/load balancer and application must all agree. namespaces, cgroups, capabilities, seccomp and mounts constrain ordinary host processes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production General DevOps foundations capability where Disaster recovery, Distributed failure and CI/CD security are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: protected backup plus timed application restore/failover proves RPO and RTO. timeout does not reveal whether a remote side effect occurred, so idempotency and reconciliation matter. untrusted code near runner credentials requires isolation, pinning and short-lived identity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Linux resource path. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `uptime; vmstat 1; iostat -xz 1` as one read-only checkpoint, not the whole diagnosis. CPU, memory, disk, descriptors, processes, cgroups and kernel evidence explain application symptoms. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Network request path. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip route; ss -lntp; dig NAME; curl -v URL` as one read-only checkpoint, not the whole diagnosis. DNS, route, firewall/NAT, transport, TLS, proxy/load balancer and application must all agree. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Distributed failure. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --graph --oneline --all` as one read-only checkpoint, not the whole diagnosis. timeout does not reveal whether a remote side effect occurred, so idempotency and reconciliation matter. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Git delivery. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker inspect CONTAINER` as one read-only checkpoint, not the whole diagnosis. reviewed source must bind to immutable artifact, provenance, environment and rollback evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Container isolation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `uptime; vmstat 1; iostat -xz 1` as one read-only checkpoint, not the whole diagnosis. namespaces, cgroups, capabilities, seccomp and mounts constrain ordinary host processes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CI/CD security. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip route; ss -lntp; dig NAME; curl -v URL` as one read-only checkpoint, not the whole diagnosis. untrusted code near runner credentials requires isolation, pinning and short-lived identity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Observability. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --graph --oneline --all` as one read-only checkpoint, not the whole diagnosis. metrics, logs, traces and profiles answer distinct questions under cardinality/privacy/cost limits. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SLO/error budget. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker inspect CONTAINER` as one read-only checkpoint, not the whole diagnosis. user outcome target and burn rate guide paging and risk decisions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Incident response. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `uptime; vmstat 1; iostat -xz 1` as one read-only checkpoint, not the whole diagnosis. command, containment, evidence, reversible mitigation, verification and prevention form the lifecycle. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GENERAL-DEVOPS-FOUNDATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Disaster recovery. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip route; ss -lntp; dig NAME; curl -v URL` as one read-only checkpoint, not the whole diagnosis. protected backup plus timed application restore/failover proves RPO and RTO. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

# Cloud, Kubernetes and Infrastructure as Code — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JN-01

- [ ] **Question:** What is Cloud account/project, and why does it matter in Cloud, Kubernetes and Infrastructure as Code?

**Answer:** ownership, quota, billing and policy boundary reduces blast radius. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JN-02

- [ ] **Question:** What is Workload identity, and why does it matter in Cloud, Kubernetes and Infrastructure as Code?

**Answer:** short-lived federated runtime credentials replace static cloud keys. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JN-03

- [ ] **Question:** What is Kubernetes reconciliation, and why does it matter in Cloud, Kubernetes and Infrastructure as Code?

**Answer:** API/controllers/scheduler/kubelet converge desired state through plugins/runtime. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JN-04

- [ ] **Question:** What is Kubernetes networking, and why does it matter in Cloud, Kubernetes and Infrastructure as Code?

**Answer:** Service/EndpointSlice/CNI/DNS/policy/load balancer form the request path. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JN-05

- [ ] **Question:** What is Kubernetes storage, and why does it matter in Cloud, Kubernetes and Infrastructure as Code?

**Answer:** PVC/StorageClass/CSI/topology/snapshot bind state to workloads. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JN-06

- [ ] **Question:** What is Autoscaling, and why does it matter in Cloud, Kubernetes and Infrastructure as Code?

**Answer:** demand metric scales replicas and unschedulable requests scale infrastructure after cold delay. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JN-07

- [ ] **Question:** What is Terraform state, and why does it matter in Cloud, Kubernetes and Infrastructure as Code?

**Answer:** sensitive mapping from addresses to remote identities makes safe plan/refactor possible. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JN-08

- [ ] **Code:** **Question:** What does `aws sts get-caller-identity` help you verify for Cloud, Kubernetes and Infrastructure as Code?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: asynchronous dependency/secret values must stay inside engine-aware transformations.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JN-09

- [ ] **Code:** **Question:** What does `kubectl get pods,nodes -A -o wide` help you verify for Cloud, Kubernetes and Infrastructure as Code?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: pull reconciliation audits and repairs drift but can amplify bad desired state.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JN-10

- [ ] **Code:** **Question:** What does `terraform plan -out=tfplan` help you verify for Cloud, Kubernetes and Infrastructure as Code?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: fixed capacity, work units, storage, network and telemetry combine into unit cost.

## Junior — procedural and command questions

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JP-01

- [ ] **Code:** **Question:** A basic Cloud account/project check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods,nodes -A -o wide` and capture exact status/reason/request ID. ownership, quota, billing and policy boundary reduces blast radius. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JP-02

- [ ] **Question:** A basic Workload identity check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan -out=tfplan` and capture exact status/reason/request ID. short-lived federated runtime credentials replace static cloud keys. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JP-03

- [ ] **Question:** A basic Kubernetes reconciliation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. API/controllers/scheduler/kubelet converge desired state through plugins/runtime. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JP-04

- [ ] **Code:** **Question:** A basic Kubernetes networking check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts get-caller-identity` and capture exact status/reason/request ID. Service/EndpointSlice/CNI/DNS/policy/load balancer form the request path. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JP-05

- [ ] **Question:** A basic Kubernetes storage check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods,nodes -A -o wide` and capture exact status/reason/request ID. PVC/StorageClass/CSI/topology/snapshot bind state to workloads. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JP-06

- [ ] **Question:** A basic Autoscaling check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan -out=tfplan` and capture exact status/reason/request ID. demand metric scales replicas and unschedulable requests scale infrastructure after cold delay. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JP-07

- [ ] **Code:** **Question:** A basic Terraform state check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. sensitive mapping from addresses to remote identities makes safe plan/refactor possible. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JP-08

- [ ] **Question:** A basic Pulumi Outputs check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts get-caller-identity` and capture exact status/reason/request ID. asynchronous dependency/secret values must stay inside engine-aware transformations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JP-09

- [ ] **Question:** A basic GitOps check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods,nodes -A -o wide` and capture exact status/reason/request ID. pull reconciliation audits and repairs drift but can amplify bad desired state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-JP-10

- [ ] **Code:** **Question:** A basic Cloud economics check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan -out=tfplan` and capture exact status/reason/request ID. fixed capacity, work units, storage, network and telemetry combine into unit cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MN-01

- [ ] **Question:** Compare Cloud account/project with Workload identity. When would each change your design?

**Answer:** Cloud account/project: ownership, quota, billing and policy boundary reduces blast radius. Workload identity: short-lived federated runtime credentials replace static cloud keys. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MN-02

- [ ] **Question:** Compare Workload identity with Kubernetes reconciliation. When would each change your design?

**Answer:** Workload identity: short-lived federated runtime credentials replace static cloud keys. Kubernetes reconciliation: API/controllers/scheduler/kubelet converge desired state through plugins/runtime. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MN-03

- [ ] **Question:** Compare Kubernetes reconciliation with Kubernetes networking. When would each change your design?

**Answer:** Kubernetes reconciliation: API/controllers/scheduler/kubelet converge desired state through plugins/runtime. Kubernetes networking: Service/EndpointSlice/CNI/DNS/policy/load balancer form the request path. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MN-04

- [ ] **Configuration review:** **Question:** Compare Kubernetes networking with Kubernetes storage. When would each change your design?

**Answer:** Kubernetes networking: Service/EndpointSlice/CNI/DNS/policy/load balancer form the request path. Kubernetes storage: PVC/StorageClass/CSI/topology/snapshot bind state to workloads. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MN-05

- [ ] **Question:** Compare Kubernetes storage with Autoscaling. When would each change your design?

**Answer:** Kubernetes storage: PVC/StorageClass/CSI/topology/snapshot bind state to workloads. Autoscaling: demand metric scales replicas and unschedulable requests scale infrastructure after cold delay. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MN-06

- [ ] **Question:** Compare Autoscaling with Terraform state. When would each change your design?

**Answer:** Autoscaling: demand metric scales replicas and unschedulable requests scale infrastructure after cold delay. Terraform state: sensitive mapping from addresses to remote identities makes safe plan/refactor possible. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MN-07

- [ ] **Configuration review:** **Question:** Compare Terraform state with Pulumi Outputs. When would each change your design?

**Answer:** Terraform state: sensitive mapping from addresses to remote identities makes safe plan/refactor possible. Pulumi Outputs: asynchronous dependency/secret values must stay inside engine-aware transformations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MN-08

- [ ] **Question:** Compare Pulumi Outputs with GitOps. When would each change your design?

**Answer:** Pulumi Outputs: asynchronous dependency/secret values must stay inside engine-aware transformations. GitOps: pull reconciliation audits and repairs drift but can amplify bad desired state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MN-09

- [ ] **Question:** Compare GitOps with Cloud economics. When would each change your design?

**Answer:** GitOps: pull reconciliation audits and repairs drift but can amplify bad desired state. Cloud economics: fixed capacity, work units, storage, network and telemetry combine into unit cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MN-10

- [ ] **Configuration review:** **Question:** Compare Cloud economics with Cloud account/project. When would each change your design?

**Answer:** Cloud economics: fixed capacity, work units, storage, network and telemetry combine into unit cost. Cloud account/project: ownership, quota, billing and policy boundary reduces blast radius. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cloud account/project; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods,nodes -A -o wide` plus recent events/changes, then correlate the service-specific SLI. ownership, quota, billing and policy boundary reduces blast radius. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MP-02

- [ ] **Question:** Production is degraded around Workload identity; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan -out=tfplan` plus recent events/changes, then correlate the service-specific SLI. short-lived federated runtime credentials replace static cloud keys. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Kubernetes reconciliation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. API/controllers/scheduler/kubelet converge desired state through plugins/runtime. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MP-04

- [ ] **Question:** Production is degraded around Kubernetes networking; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts get-caller-identity` plus recent events/changes, then correlate the service-specific SLI. Service/EndpointSlice/CNI/DNS/policy/load balancer form the request path. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Kubernetes storage; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods,nodes -A -o wide` plus recent events/changes, then correlate the service-specific SLI. PVC/StorageClass/CSI/topology/snapshot bind state to workloads. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MP-06

- [ ] **Question:** Production is degraded around Autoscaling; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan -out=tfplan` plus recent events/changes, then correlate the service-specific SLI. demand metric scales replicas and unschedulable requests scale infrastructure after cold delay. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Terraform state; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. sensitive mapping from addresses to remote identities makes safe plan/refactor possible. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MP-08

- [ ] **Question:** Production is degraded around Pulumi Outputs; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts get-caller-identity` plus recent events/changes, then correlate the service-specific SLI. asynchronous dependency/secret values must stay inside engine-aware transformations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around GitOps; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods,nodes -A -o wide` plus recent events/changes, then correlate the service-specific SLI. pull reconciliation audits and repairs drift but can amplify bad desired state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-MP-10

- [ ] **Question:** Production is degraded around Cloud economics; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan -out=tfplan` plus recent events/changes, then correlate the service-specific SLI. fixed capacity, work units, storage, network and telemetry combine into unit cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SN-01

- [ ] **Question:** Design a production Cloud, Kubernetes and Infrastructure as Code capability where Cloud account/project, Kubernetes networking and Terraform state are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ownership, quota, billing and policy boundary reduces blast radius. Service/EndpointSlice/CNI/DNS/policy/load balancer form the request path. sensitive mapping from addresses to remote identities makes safe plan/refactor possible. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Cloud, Kubernetes and Infrastructure as Code capability where Workload identity, Kubernetes storage and Pulumi Outputs are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: short-lived federated runtime credentials replace static cloud keys. PVC/StorageClass/CSI/topology/snapshot bind state to workloads. asynchronous dependency/secret values must stay inside engine-aware transformations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SN-03

- [ ] **Question:** Design a production Cloud, Kubernetes and Infrastructure as Code capability where Kubernetes reconciliation, Autoscaling and GitOps are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: API/controllers/scheduler/kubelet converge desired state through plugins/runtime. demand metric scales replicas and unschedulable requests scale infrastructure after cold delay. pull reconciliation audits and repairs drift but can amplify bad desired state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Cloud, Kubernetes and Infrastructure as Code capability where Kubernetes networking, Terraform state and Cloud economics are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Service/EndpointSlice/CNI/DNS/policy/load balancer form the request path. sensitive mapping from addresses to remote identities makes safe plan/refactor possible. fixed capacity, work units, storage, network and telemetry combine into unit cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SN-05

- [ ] **Question:** Design a production Cloud, Kubernetes and Infrastructure as Code capability where Kubernetes storage, Pulumi Outputs and Cloud account/project are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: PVC/StorageClass/CSI/topology/snapshot bind state to workloads. asynchronous dependency/secret values must stay inside engine-aware transformations. ownership, quota, billing and policy boundary reduces blast radius. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Cloud, Kubernetes and Infrastructure as Code capability where Autoscaling, GitOps and Workload identity are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: demand metric scales replicas and unschedulable requests scale infrastructure after cold delay. pull reconciliation audits and repairs drift but can amplify bad desired state. short-lived federated runtime credentials replace static cloud keys. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SN-07

- [ ] **Question:** Design a production Cloud, Kubernetes and Infrastructure as Code capability where Terraform state, Cloud economics and Kubernetes reconciliation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: sensitive mapping from addresses to remote identities makes safe plan/refactor possible. fixed capacity, work units, storage, network and telemetry combine into unit cost. API/controllers/scheduler/kubelet converge desired state through plugins/runtime. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Cloud, Kubernetes and Infrastructure as Code capability where Pulumi Outputs, Cloud account/project and Kubernetes networking are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: asynchronous dependency/secret values must stay inside engine-aware transformations. ownership, quota, billing and policy boundary reduces blast radius. Service/EndpointSlice/CNI/DNS/policy/load balancer form the request path. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SN-09

- [ ] **Question:** Design a production Cloud, Kubernetes and Infrastructure as Code capability where GitOps, Workload identity and Kubernetes storage are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pull reconciliation audits and repairs drift but can amplify bad desired state. short-lived federated runtime credentials replace static cloud keys. PVC/StorageClass/CSI/topology/snapshot bind state to workloads. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Cloud, Kubernetes and Infrastructure as Code capability where Cloud economics, Kubernetes reconciliation and Autoscaling are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: fixed capacity, work units, storage, network and telemetry combine into unit cost. API/controllers/scheduler/kubelet converge desired state through plugins/runtime. demand metric scales replicas and unschedulable requests scale infrastructure after cold delay. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cloud account/project. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods,nodes -A -o wide` as one read-only checkpoint, not the whole diagnosis. ownership, quota, billing and policy boundary reduces blast radius. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Workload identity. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan -out=tfplan` as one read-only checkpoint, not the whole diagnosis. short-lived federated runtime credentials replace static cloud keys. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Kubernetes reconciliation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. API/controllers/scheduler/kubelet converge desired state through plugins/runtime. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Kubernetes networking. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts get-caller-identity` as one read-only checkpoint, not the whole diagnosis. Service/EndpointSlice/CNI/DNS/policy/load balancer form the request path. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Kubernetes storage. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods,nodes -A -o wide` as one read-only checkpoint, not the whole diagnosis. PVC/StorageClass/CSI/topology/snapshot bind state to workloads. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Autoscaling. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan -out=tfplan` as one read-only checkpoint, not the whole diagnosis. demand metric scales replicas and unschedulable requests scale infrastructure after cold delay. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Terraform state. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. sensitive mapping from addresses to remote identities makes safe plan/refactor possible. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pulumi Outputs. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts get-caller-identity` as one read-only checkpoint, not the whole diagnosis. asynchronous dependency/secret values must stay inside engine-aware transformations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GitOps. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods,nodes -A -o wide` as one read-only checkpoint, not the whole diagnosis. pull reconciliation audits and repairs drift but can amplify bad desired state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CLOUD-KUBERNETES-AND-INFRASTRUCTURE-AS-CO-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cloud economics. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan -out=tfplan` as one read-only checkpoint, not the whole diagnosis. fixed capacity, work units, storage, network and telemetry combine into unit cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

# Senior AI platform engineering — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JN-01

- [ ] **Question:** What is GPU compatibility chain, and why does it matter in Senior AI platform engineering?

**Answer:** hardware, driver, runtime, device allocation, framework and model must be qualified together. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JN-02

- [ ] **Question:** What is Inference queue, and why does it matter in Senior AI platform engineering?

**Answer:** token work, KV memory, TTFT and goodput govern admission/batching/autoscaling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JN-03

- [ ] **Question:** What is Model release, and why does it matter in Senior AI platform engineering?

**Answer:** weights, tokenizer, prompt, adapters, runtime, hardware, data/index and evaluator form one lineage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JN-04

- [ ] **Question:** What is LLM gateway, and why does it matter in Senior AI platform engineering?

**Answer:** identity, policy, quota, routing, streaming, fallback, metering and audit normalize governed access. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JN-05

- [ ] **Question:** What is RAG authorization, and why does it matter in Senior AI platform engineering?

**Answer:** retrieval must enforce source and tenant access before context reaches a model. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JN-06

- [ ] **Question:** What is Evaluation, and why does it matter in Senior AI platform engineering?

**Answer:** versioned datasets and calibrated human/automated judges gate quality/safety regressions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JN-07

- [ ] **Question:** What is Agent tool security, and why does it matter in Senior AI platform engineering?

**Answer:** model output proposes actions; deterministic policy, least privilege and approval authorize them. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JN-08

- [ ] **Code:** **Question:** What does `python -m evals.run --manifest release.yaml` help you verify for Senior AI platform engineering?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: inventory, ownership, risk, data/model/prompt lineage, audit and retirement make controls operable.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JN-09

- [ ] **Code:** **Question:** What does `nvidia-smi topo -m` help you verify for Senior AI platform engineering?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: optimize cost per successful quality-controlled task rather than raw token or GPU hour.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JN-10

- [ ] **Code:** **Question:** What does `kubectl get inferenceservice -A` help you verify for Senior AI platform engineering?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: SaaS, customer cloud, on-prem and air gap require explicit packaging, identity, upgrades and support contracts.

## Junior — procedural and command questions

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JP-01

- [ ] **Code:** **Question:** A basic GPU compatibility chain check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi topo -m` and capture exact status/reason/request ID. hardware, driver, runtime, device allocation, framework and model must be qualified together. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JP-02

- [ ] **Question:** A basic Inference queue check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get inferenceservice -A` and capture exact status/reason/request ID. token work, KV memory, TTFT and goodput govern admission/batching/autoscaling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JP-03

- [ ] **Question:** A basic Model release check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. weights, tokenizer, prompt, adapters, runtime, hardware, data/index and evaluator form one lineage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JP-04

- [ ] **Code:** **Question:** A basic LLM gateway check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml` and capture exact status/reason/request ID. identity, policy, quota, routing, streaming, fallback, metering and audit normalize governed access. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JP-05

- [ ] **Question:** A basic RAG authorization check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi topo -m` and capture exact status/reason/request ID. retrieval must enforce source and tenant access before context reaches a model. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JP-06

- [ ] **Question:** A basic Evaluation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get inferenceservice -A` and capture exact status/reason/request ID. versioned datasets and calibrated human/automated judges gate quality/safety regressions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JP-07

- [ ] **Code:** **Question:** A basic Agent tool security check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. model output proposes actions; deterministic policy, least privilege and approval authorize them. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JP-08

- [ ] **Question:** A basic AI governance check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml` and capture exact status/reason/request ID. inventory, ownership, risk, data/model/prompt lineage, audit and retirement make controls operable. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JP-09

- [ ] **Question:** A basic AI FinOps check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi topo -m` and capture exact status/reason/request ID. optimize cost per successful quality-controlled task rather than raw token or GPU hour. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-JP-10

- [ ] **Code:** **Question:** A basic Deployment portability check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get inferenceservice -A` and capture exact status/reason/request ID. SaaS, customer cloud, on-prem and air gap require explicit packaging, identity, upgrades and support contracts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MN-01

- [ ] **Question:** Compare GPU compatibility chain with Inference queue. When would each change your design?

**Answer:** GPU compatibility chain: hardware, driver, runtime, device allocation, framework and model must be qualified together. Inference queue: token work, KV memory, TTFT and goodput govern admission/batching/autoscaling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MN-02

- [ ] **Question:** Compare Inference queue with Model release. When would each change your design?

**Answer:** Inference queue: token work, KV memory, TTFT and goodput govern admission/batching/autoscaling. Model release: weights, tokenizer, prompt, adapters, runtime, hardware, data/index and evaluator form one lineage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MN-03

- [ ] **Question:** Compare Model release with LLM gateway. When would each change your design?

**Answer:** Model release: weights, tokenizer, prompt, adapters, runtime, hardware, data/index and evaluator form one lineage. LLM gateway: identity, policy, quota, routing, streaming, fallback, metering and audit normalize governed access. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MN-04

- [ ] **Configuration review:** **Question:** Compare LLM gateway with RAG authorization. When would each change your design?

**Answer:** LLM gateway: identity, policy, quota, routing, streaming, fallback, metering and audit normalize governed access. RAG authorization: retrieval must enforce source and tenant access before context reaches a model. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MN-05

- [ ] **Question:** Compare RAG authorization with Evaluation. When would each change your design?

**Answer:** RAG authorization: retrieval must enforce source and tenant access before context reaches a model. Evaluation: versioned datasets and calibrated human/automated judges gate quality/safety regressions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MN-06

- [ ] **Question:** Compare Evaluation with Agent tool security. When would each change your design?

**Answer:** Evaluation: versioned datasets and calibrated human/automated judges gate quality/safety regressions. Agent tool security: model output proposes actions; deterministic policy, least privilege and approval authorize them. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MN-07

- [ ] **Configuration review:** **Question:** Compare Agent tool security with AI governance. When would each change your design?

**Answer:** Agent tool security: model output proposes actions; deterministic policy, least privilege and approval authorize them. AI governance: inventory, ownership, risk, data/model/prompt lineage, audit and retirement make controls operable. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MN-08

- [ ] **Question:** Compare AI governance with AI FinOps. When would each change your design?

**Answer:** AI governance: inventory, ownership, risk, data/model/prompt lineage, audit and retirement make controls operable. AI FinOps: optimize cost per successful quality-controlled task rather than raw token or GPU hour. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MN-09

- [ ] **Question:** Compare AI FinOps with Deployment portability. When would each change your design?

**Answer:** AI FinOps: optimize cost per successful quality-controlled task rather than raw token or GPU hour. Deployment portability: SaaS, customer cloud, on-prem and air gap require explicit packaging, identity, upgrades and support contracts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MN-10

- [ ] **Configuration review:** **Question:** Compare Deployment portability with GPU compatibility chain. When would each change your design?

**Answer:** Deployment portability: SaaS, customer cloud, on-prem and air gap require explicit packaging, identity, upgrades and support contracts. GPU compatibility chain: hardware, driver, runtime, device allocation, framework and model must be qualified together. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around GPU compatibility chain; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi topo -m` plus recent events/changes, then correlate the service-specific SLI. hardware, driver, runtime, device allocation, framework and model must be qualified together. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MP-02

- [ ] **Question:** Production is degraded around Inference queue; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get inferenceservice -A` plus recent events/changes, then correlate the service-specific SLI. token work, KV memory, TTFT and goodput govern admission/batching/autoscaling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model release; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. weights, tokenizer, prompt, adapters, runtime, hardware, data/index and evaluator form one lineage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MP-04

- [ ] **Question:** Production is degraded around LLM gateway; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml` plus recent events/changes, then correlate the service-specific SLI. identity, policy, quota, routing, streaming, fallback, metering and audit normalize governed access. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around RAG authorization; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi topo -m` plus recent events/changes, then correlate the service-specific SLI. retrieval must enforce source and tenant access before context reaches a model. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MP-06

- [ ] **Question:** Production is degraded around Evaluation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get inferenceservice -A` plus recent events/changes, then correlate the service-specific SLI. versioned datasets and calibrated human/automated judges gate quality/safety regressions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Agent tool security; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. model output proposes actions; deterministic policy, least privilege and approval authorize them. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MP-08

- [ ] **Question:** Production is degraded around AI governance; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml` plus recent events/changes, then correlate the service-specific SLI. inventory, ownership, risk, data/model/prompt lineage, audit and retirement make controls operable. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around AI FinOps; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi topo -m` plus recent events/changes, then correlate the service-specific SLI. optimize cost per successful quality-controlled task rather than raw token or GPU hour. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-MP-10

- [ ] **Question:** Production is degraded around Deployment portability; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get inferenceservice -A` plus recent events/changes, then correlate the service-specific SLI. SaaS, customer cloud, on-prem and air gap require explicit packaging, identity, upgrades and support contracts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SN-01

- [ ] **Question:** Design a production Senior AI platform engineering capability where GPU compatibility chain, LLM gateway and Agent tool security are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: hardware, driver, runtime, device allocation, framework and model must be qualified together. identity, policy, quota, routing, streaming, fallback, metering and audit normalize governed access. model output proposes actions; deterministic policy, least privilege and approval authorize them. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Senior AI platform engineering capability where Inference queue, RAG authorization and AI governance are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: token work, KV memory, TTFT and goodput govern admission/batching/autoscaling. retrieval must enforce source and tenant access before context reaches a model. inventory, ownership, risk, data/model/prompt lineage, audit and retirement make controls operable. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SN-03

- [ ] **Question:** Design a production Senior AI platform engineering capability where Model release, Evaluation and AI FinOps are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: weights, tokenizer, prompt, adapters, runtime, hardware, data/index and evaluator form one lineage. versioned datasets and calibrated human/automated judges gate quality/safety regressions. optimize cost per successful quality-controlled task rather than raw token or GPU hour. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Senior AI platform engineering capability where LLM gateway, Agent tool security and Deployment portability are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: identity, policy, quota, routing, streaming, fallback, metering and audit normalize governed access. model output proposes actions; deterministic policy, least privilege and approval authorize them. SaaS, customer cloud, on-prem and air gap require explicit packaging, identity, upgrades and support contracts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SN-05

- [ ] **Question:** Design a production Senior AI platform engineering capability where RAG authorization, AI governance and GPU compatibility chain are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retrieval must enforce source and tenant access before context reaches a model. inventory, ownership, risk, data/model/prompt lineage, audit and retirement make controls operable. hardware, driver, runtime, device allocation, framework and model must be qualified together. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Senior AI platform engineering capability where Evaluation, AI FinOps and Inference queue are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versioned datasets and calibrated human/automated judges gate quality/safety regressions. optimize cost per successful quality-controlled task rather than raw token or GPU hour. token work, KV memory, TTFT and goodput govern admission/batching/autoscaling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SN-07

- [ ] **Question:** Design a production Senior AI platform engineering capability where Agent tool security, Deployment portability and Model release are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model output proposes actions; deterministic policy, least privilege and approval authorize them. SaaS, customer cloud, on-prem and air gap require explicit packaging, identity, upgrades and support contracts. weights, tokenizer, prompt, adapters, runtime, hardware, data/index and evaluator form one lineage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Senior AI platform engineering capability where AI governance, GPU compatibility chain and LLM gateway are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: inventory, ownership, risk, data/model/prompt lineage, audit and retirement make controls operable. hardware, driver, runtime, device allocation, framework and model must be qualified together. identity, policy, quota, routing, streaming, fallback, metering and audit normalize governed access. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SN-09

- [ ] **Question:** Design a production Senior AI platform engineering capability where AI FinOps, Inference queue and RAG authorization are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: optimize cost per successful quality-controlled task rather than raw token or GPU hour. token work, KV memory, TTFT and goodput govern admission/batching/autoscaling. retrieval must enforce source and tenant access before context reaches a model. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Senior AI platform engineering capability where Deployment portability, Model release and Evaluation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: SaaS, customer cloud, on-prem and air gap require explicit packaging, identity, upgrades and support contracts. weights, tokenizer, prompt, adapters, runtime, hardware, data/index and evaluator form one lineage. versioned datasets and calibrated human/automated judges gate quality/safety regressions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU compatibility chain. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi topo -m` as one read-only checkpoint, not the whole diagnosis. hardware, driver, runtime, device allocation, framework and model must be qualified together. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Inference queue. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get inferenceservice -A` as one read-only checkpoint, not the whole diagnosis. token work, KV memory, TTFT and goodput govern admission/batching/autoscaling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model release. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. weights, tokenizer, prompt, adapters, runtime, hardware, data/index and evaluator form one lineage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving LLM gateway. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml` as one read-only checkpoint, not the whole diagnosis. identity, policy, quota, routing, streaming, fallback, metering and audit normalize governed access. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RAG authorization. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi topo -m` as one read-only checkpoint, not the whole diagnosis. retrieval must enforce source and tenant access before context reaches a model. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Evaluation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get inferenceservice -A` as one read-only checkpoint, not the whole diagnosis. versioned datasets and calibrated human/automated judges gate quality/safety regressions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Agent tool security. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. model output proposes actions; deterministic policy, least privilege and approval authorize them. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AI governance. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml` as one read-only checkpoint, not the whole diagnosis. inventory, ownership, risk, data/model/prompt lineage, audit and retirement make controls operable. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AI FinOps. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi topo -m` as one read-only checkpoint, not the whole diagnosis. optimize cost per successful quality-controlled task rather than raw token or GPU hour. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SENIOR-AI-PLATFORM-ENGINEERING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deployment portability. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get inferenceservice -A` as one read-only checkpoint, not the whole diagnosis. SaaS, customer cloud, on-prem and air gap require explicit packaging, identity, upgrades and support contracts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
