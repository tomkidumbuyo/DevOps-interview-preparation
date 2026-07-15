# LLM gateway and ProviderOps — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### LLM-GATEWAY-AND-PROVIDEROPS-JN-01

- [ ] **Question:** What is Normalized API, and why does it matter in LLM gateway and ProviderOps?

**Answer:** common request/response cannot erase provider differences in tools, streaming, errors, tokens and safety. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-PROVIDEROPS-JN-02

- [ ] **Question:** What is Model catalog, and why does it matter in LLM gateway and ProviderOps?

**Answer:** alias maps to approved provider/model/region/capabilities/context/price under versioned policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-PROVIDEROPS-JN-03

- [ ] **Question:** What is Tenant policy, and why does it matter in LLM gateway and ProviderOps?

**Answer:** identity derives allowed models, data routes, quotas, logging, tools and budget. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-PROVIDEROPS-JN-04

- [ ] **Question:** What is Admission, and why does it matter in LLM gateway and ProviderOps?

**Answer:** request/token/concurrency/queued-work controls protect provider and self-hosted capacity fairly. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-PROVIDEROPS-JN-05

- [ ] **Question:** What is Routing, and why does it matter in LLM gateway and ProviderOps?

**Answer:** capability, health, residency, cost and experiment policy choose a route with auditable reason. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-PROVIDEROPS-JN-06

- [ ] **Question:** What is Retry, and why does it matter in LLM gateway and ProviderOps?

**Answer:** bounded backoff honors provider hints and only retries safe stages; streamed output/unknown side effects prevent transparent replay. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-PROVIDEROPS-JN-07

- [ ] **Question:** What is Fallback, and why does it matter in LLM gateway and ProviderOps?

**Answer:** alternate route is prequalified for schema, quality, safety, residency and cost rather than merely available. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-PROVIDEROPS-JN-08

- [ ] **Code:** **Question:** What does `python scripts/reconcile_provider_invoice.py --month YYYY-MM` help you verify for LLM gateway and ProviderOps?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: model alias/version/deprecation changes need contract/eval canary and rollback like internal changes.

### LLM-GATEWAY-AND-PROVIDEROPS-JN-09

- [ ] **Code:** **Question:** What does `curl -N -v GATEWAY/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json` help you verify for LLM gateway and ProviderOps?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: estimated/actual tokens, cache and tool work reconcile with invoice and tenant allocation.

### LLM-GATEWAY-AND-PROVIDEROPS-JN-10

- [ ] **Code:** **Question:** What does `curl -s GATEWAY/metrics` help you verify for LLM gateway and ProviderOps?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: circuit, shed, queue, failover or degrade under explicit SLO/quality/security trade-offs and communication.

## Junior — procedural and command questions

### LLM-GATEWAY-AND-PROVIDEROPS-JP-01

- [ ] **Code:** **Question:** A basic Normalized API check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -N -v GATEWAY/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json` and capture exact status/reason/request ID. common request/response cannot erase provider differences in tools, streaming, errors, tokens and safety. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-PROVIDEROPS-JP-02

- [ ] **Question:** A basic Model catalog check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s GATEWAY/metrics` and capture exact status/reason/request ID. alias maps to approved provider/model/region/capabilities/context/price under versioned policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-PROVIDEROPS-JP-03

- [ ] **Question:** A basic Tenant policy check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` and capture exact status/reason/request ID. identity derives allowed models, data routes, quotas, logging, tools and budget. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-PROVIDEROPS-JP-04

- [ ] **Code:** **Question:** A basic Admission check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/reconcile_provider_invoice.py --month YYYY-MM` and capture exact status/reason/request ID. request/token/concurrency/queued-work controls protect provider and self-hosted capacity fairly. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-PROVIDEROPS-JP-05

- [ ] **Question:** A basic Routing check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -N -v GATEWAY/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json` and capture exact status/reason/request ID. capability, health, residency, cost and experiment policy choose a route with auditable reason. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-PROVIDEROPS-JP-06

- [ ] **Question:** A basic Retry check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s GATEWAY/metrics` and capture exact status/reason/request ID. bounded backoff honors provider hints and only retries safe stages; streamed output/unknown side effects prevent transparent replay. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-PROVIDEROPS-JP-07

- [ ] **Code:** **Question:** A basic Fallback check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` and capture exact status/reason/request ID. alternate route is prequalified for schema, quality, safety, residency and cost rather than merely available. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-PROVIDEROPS-JP-08

- [ ] **Question:** A basic Provider release check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/reconcile_provider_invoice.py --month YYYY-MM` and capture exact status/reason/request ID. model alias/version/deprecation changes need contract/eval canary and rollback like internal changes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-PROVIDEROPS-JP-09

- [ ] **Question:** A basic Metering check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -N -v GATEWAY/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json` and capture exact status/reason/request ID. estimated/actual tokens, cache and tool work reconcile with invoice and tenant allocation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-PROVIDEROPS-JP-10

- [ ] **Code:** **Question:** A basic Incident check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s GATEWAY/metrics` and capture exact status/reason/request ID. circuit, shed, queue, failover or degrade under explicit SLO/quality/security trade-offs and communication. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### LLM-GATEWAY-AND-PROVIDEROPS-MN-01

- [ ] **Question:** Compare Normalized API with Model catalog. When would each change your design?

**Answer:** Normalized API: common request/response cannot erase provider differences in tools, streaming, errors, tokens and safety. Model catalog: alias maps to approved provider/model/region/capabilities/context/price under versioned policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-PROVIDEROPS-MN-02

- [ ] **Question:** Compare Model catalog with Tenant policy. When would each change your design?

**Answer:** Model catalog: alias maps to approved provider/model/region/capabilities/context/price under versioned policy. Tenant policy: identity derives allowed models, data routes, quotas, logging, tools and budget. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-PROVIDEROPS-MN-03

- [ ] **Question:** Compare Tenant policy with Admission. When would each change your design?

**Answer:** Tenant policy: identity derives allowed models, data routes, quotas, logging, tools and budget. Admission: request/token/concurrency/queued-work controls protect provider and self-hosted capacity fairly. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-PROVIDEROPS-MN-04

- [ ] **Configuration review:** **Question:** Compare Admission with Routing. When would each change your design?

**Answer:** Admission: request/token/concurrency/queued-work controls protect provider and self-hosted capacity fairly. Routing: capability, health, residency, cost and experiment policy choose a route with auditable reason. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-PROVIDEROPS-MN-05

- [ ] **Question:** Compare Routing with Retry. When would each change your design?

**Answer:** Routing: capability, health, residency, cost and experiment policy choose a route with auditable reason. Retry: bounded backoff honors provider hints and only retries safe stages; streamed output/unknown side effects prevent transparent replay. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-PROVIDEROPS-MN-06

- [ ] **Question:** Compare Retry with Fallback. When would each change your design?

**Answer:** Retry: bounded backoff honors provider hints and only retries safe stages; streamed output/unknown side effects prevent transparent replay. Fallback: alternate route is prequalified for schema, quality, safety, residency and cost rather than merely available. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-PROVIDEROPS-MN-07

- [ ] **Configuration review:** **Question:** Compare Fallback with Provider release. When would each change your design?

**Answer:** Fallback: alternate route is prequalified for schema, quality, safety, residency and cost rather than merely available. Provider release: model alias/version/deprecation changes need contract/eval canary and rollback like internal changes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-PROVIDEROPS-MN-08

- [ ] **Question:** Compare Provider release with Metering. When would each change your design?

**Answer:** Provider release: model alias/version/deprecation changes need contract/eval canary and rollback like internal changes. Metering: estimated/actual tokens, cache and tool work reconcile with invoice and tenant allocation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-PROVIDEROPS-MN-09

- [ ] **Question:** Compare Metering with Incident. When would each change your design?

**Answer:** Metering: estimated/actual tokens, cache and tool work reconcile with invoice and tenant allocation. Incident: circuit, shed, queue, failover or degrade under explicit SLO/quality/security trade-offs and communication. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-PROVIDEROPS-MN-10

- [ ] **Configuration review:** **Question:** Compare Incident with Normalized API. When would each change your design?

**Answer:** Incident: circuit, shed, queue, failover or degrade under explicit SLO/quality/security trade-offs and communication. Normalized API: common request/response cannot erase provider differences in tools, streaming, errors, tokens and safety. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### LLM-GATEWAY-AND-PROVIDEROPS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Normalized API; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -N -v GATEWAY/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json` plus recent events/changes, then correlate the service-specific SLI. common request/response cannot erase provider differences in tools, streaming, errors, tokens and safety. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-PROVIDEROPS-MP-02

- [ ] **Question:** Production is degraded around Model catalog; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s GATEWAY/metrics` plus recent events/changes, then correlate the service-specific SLI. alias maps to approved provider/model/region/capabilities/context/price under versioned policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-PROVIDEROPS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Tenant policy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` plus recent events/changes, then correlate the service-specific SLI. identity derives allowed models, data routes, quotas, logging, tools and budget. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-PROVIDEROPS-MP-04

- [ ] **Question:** Production is degraded around Admission; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/reconcile_provider_invoice.py --month YYYY-MM` plus recent events/changes, then correlate the service-specific SLI. request/token/concurrency/queued-work controls protect provider and self-hosted capacity fairly. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-PROVIDEROPS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Routing; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -N -v GATEWAY/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json` plus recent events/changes, then correlate the service-specific SLI. capability, health, residency, cost and experiment policy choose a route with auditable reason. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-PROVIDEROPS-MP-06

- [ ] **Question:** Production is degraded around Retry; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s GATEWAY/metrics` plus recent events/changes, then correlate the service-specific SLI. bounded backoff honors provider hints and only retries safe stages; streamed output/unknown side effects prevent transparent replay. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-PROVIDEROPS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Fallback; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` plus recent events/changes, then correlate the service-specific SLI. alternate route is prequalified for schema, quality, safety, residency and cost rather than merely available. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-PROVIDEROPS-MP-08

- [ ] **Question:** Production is degraded around Provider release; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/reconcile_provider_invoice.py --month YYYY-MM` plus recent events/changes, then correlate the service-specific SLI. model alias/version/deprecation changes need contract/eval canary and rollback like internal changes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-PROVIDEROPS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Metering; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -N -v GATEWAY/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json` plus recent events/changes, then correlate the service-specific SLI. estimated/actual tokens, cache and tool work reconcile with invoice and tenant allocation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-PROVIDEROPS-MP-10

- [ ] **Question:** Production is degraded around Incident; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s GATEWAY/metrics` plus recent events/changes, then correlate the service-specific SLI. circuit, shed, queue, failover or degrade under explicit SLO/quality/security trade-offs and communication. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### LLM-GATEWAY-AND-PROVIDEROPS-SN-01

- [ ] **Question:** Design a production LLM gateway and ProviderOps capability where Normalized API, Admission and Fallback are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: common request/response cannot erase provider differences in tools, streaming, errors, tokens and safety. request/token/concurrency/queued-work controls protect provider and self-hosted capacity fairly. alternate route is prequalified for schema, quality, safety, residency and cost rather than merely available. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-PROVIDEROPS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production LLM gateway and ProviderOps capability where Model catalog, Routing and Provider release are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: alias maps to approved provider/model/region/capabilities/context/price under versioned policy. capability, health, residency, cost and experiment policy choose a route with auditable reason. model alias/version/deprecation changes need contract/eval canary and rollback like internal changes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-PROVIDEROPS-SN-03

- [ ] **Question:** Design a production LLM gateway and ProviderOps capability where Tenant policy, Retry and Metering are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: identity derives allowed models, data routes, quotas, logging, tools and budget. bounded backoff honors provider hints and only retries safe stages; streamed output/unknown side effects prevent transparent replay. estimated/actual tokens, cache and tool work reconcile with invoice and tenant allocation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-PROVIDEROPS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production LLM gateway and ProviderOps capability where Admission, Fallback and Incident are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: request/token/concurrency/queued-work controls protect provider and self-hosted capacity fairly. alternate route is prequalified for schema, quality, safety, residency and cost rather than merely available. circuit, shed, queue, failover or degrade under explicit SLO/quality/security trade-offs and communication. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-PROVIDEROPS-SN-05

- [ ] **Question:** Design a production LLM gateway and ProviderOps capability where Routing, Provider release and Normalized API are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: capability, health, residency, cost and experiment policy choose a route with auditable reason. model alias/version/deprecation changes need contract/eval canary and rollback like internal changes. common request/response cannot erase provider differences in tools, streaming, errors, tokens and safety. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-PROVIDEROPS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production LLM gateway and ProviderOps capability where Retry, Metering and Model catalog are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bounded backoff honors provider hints and only retries safe stages; streamed output/unknown side effects prevent transparent replay. estimated/actual tokens, cache and tool work reconcile with invoice and tenant allocation. alias maps to approved provider/model/region/capabilities/context/price under versioned policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-PROVIDEROPS-SN-07

- [ ] **Question:** Design a production LLM gateway and ProviderOps capability where Fallback, Incident and Tenant policy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: alternate route is prequalified for schema, quality, safety, residency and cost rather than merely available. circuit, shed, queue, failover or degrade under explicit SLO/quality/security trade-offs and communication. identity derives allowed models, data routes, quotas, logging, tools and budget. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-PROVIDEROPS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production LLM gateway and ProviderOps capability where Provider release, Normalized API and Admission are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model alias/version/deprecation changes need contract/eval canary and rollback like internal changes. common request/response cannot erase provider differences in tools, streaming, errors, tokens and safety. request/token/concurrency/queued-work controls protect provider and self-hosted capacity fairly. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-PROVIDEROPS-SN-09

- [ ] **Question:** Design a production LLM gateway and ProviderOps capability where Metering, Model catalog and Routing are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: estimated/actual tokens, cache and tool work reconcile with invoice and tenant allocation. alias maps to approved provider/model/region/capabilities/context/price under versioned policy. capability, health, residency, cost and experiment policy choose a route with auditable reason. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-PROVIDEROPS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production LLM gateway and ProviderOps capability where Incident, Tenant policy and Retry are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: circuit, shed, queue, failover or degrade under explicit SLO/quality/security trade-offs and communication. identity derives allowed models, data routes, quotas, logging, tools and budget. bounded backoff honors provider hints and only retries safe stages; streamed output/unknown side effects prevent transparent replay. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### LLM-GATEWAY-AND-PROVIDEROPS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Normalized API. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -N -v GATEWAY/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json` as one read-only checkpoint, not the whole diagnosis. common request/response cannot erase provider differences in tools, streaming, errors, tokens and safety. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-PROVIDEROPS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model catalog. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s GATEWAY/metrics` as one read-only checkpoint, not the whole diagnosis. alias maps to approved provider/model/region/capabilities/context/price under versioned policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-PROVIDEROPS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tenant policy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` as one read-only checkpoint, not the whole diagnosis. identity derives allowed models, data routes, quotas, logging, tools and budget. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-PROVIDEROPS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Admission. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/reconcile_provider_invoice.py --month YYYY-MM` as one read-only checkpoint, not the whole diagnosis. request/token/concurrency/queued-work controls protect provider and self-hosted capacity fairly. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-PROVIDEROPS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Routing. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -N -v GATEWAY/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json` as one read-only checkpoint, not the whole diagnosis. capability, health, residency, cost and experiment policy choose a route with auditable reason. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-PROVIDEROPS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retry. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s GATEWAY/metrics` as one read-only checkpoint, not the whole diagnosis. bounded backoff honors provider hints and only retries safe stages; streamed output/unknown side effects prevent transparent replay. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-PROVIDEROPS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Fallback. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` as one read-only checkpoint, not the whole diagnosis. alternate route is prequalified for schema, quality, safety, residency and cost rather than merely available. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-PROVIDEROPS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Provider release. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/reconcile_provider_invoice.py --month YYYY-MM` as one read-only checkpoint, not the whole diagnosis. model alias/version/deprecation changes need contract/eval canary and rollback like internal changes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-PROVIDEROPS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Metering. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -N -v GATEWAY/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json` as one read-only checkpoint, not the whole diagnosis. estimated/actual tokens, cache and tool work reconcile with invoice and tenant allocation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-PROVIDEROPS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Incident. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s GATEWAY/metrics` as one read-only checkpoint, not the whole diagnosis. circuit, shed, queue, failover or degrade under explicit SLO/quality/security trade-offs and communication. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
