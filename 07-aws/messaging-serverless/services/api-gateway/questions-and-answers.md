# Amazon API Gateway — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-API-GATEWAY-JN-01

- [ ] **Question:** What is REST vs HTTP API, and why does it matter in Amazon API Gateway?

**Answer:** feature/integration/authorization/transformation and price differ. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-API-GATEWAY-JN-02

- [ ] **Question:** What is WebSocket API, and why does it matter in Amazon API Gateway?

**Answer:** connection routes and state/callback management support bidirectional messaging. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-API-GATEWAY-JN-03

- [ ] **Question:** What is Route/resource-method, and why does it matter in Amazon API Gateway?

**Answer:** matches request and invokes an integration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-API-GATEWAY-JN-04

- [ ] **Question:** What is Lambda proxy integration, and why does it matter in Amazon API Gateway?

**Answer:** passes normalized request/event and expects defined response shape. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-API-GATEWAY-JN-05

- [ ] **Question:** What is Authorizer, and why does it matter in Amazon API Gateway?

**Answer:** IAM/JWT/Lambda identity decision with cache and failure implications. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-API-GATEWAY-JN-06

- [ ] **Question:** What is Usage plan/API key, and why does it matter in Amazon API Gateway?

**Answer:** metering/throttle association is not user authentication by itself. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-API-GATEWAY-JN-07

- [ ] **Question:** What is Stage/deployment, and why does it matter in Amazon API Gateway?

**Answer:** immutable API snapshot and stage settings/canary/logging form release unit. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-API-GATEWAY-JN-08

- [ ] **Code:** **Question:** What does `aws apigatewayv2 get-integrations --api-id API_ID` help you verify for Amazon API Gateway?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: account/stage/route limits protect gateway/downstream and return retryable errors.

### AMAZON-API-GATEWAY-JN-09

- [ ] **Code:** **Question:** What does `aws apigateway get-rest-apis` help you verify for Amazon API Gateway?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: certificate, endpoint type, API mapping and DNS compose the public endpoint.

### AMAZON-API-GATEWAY-JN-10

- [ ] **Code:** **Question:** What does `aws apigatewayv2 get-apis` help you verify for Amazon API Gateway?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: request IDs, integration latency/status and safe fields support diagnosis.

## Junior — procedural and command questions

### AMAZON-API-GATEWAY-JP-01

- [ ] **Code:** **Question:** A basic REST vs HTTP API check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws apigateway get-rest-apis` and capture exact status/reason/request ID. feature/integration/authorization/transformation and price differ. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-API-GATEWAY-JP-02

- [ ] **Question:** A basic WebSocket API check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws apigatewayv2 get-apis` and capture exact status/reason/request ID. connection routes and state/callback management support bidirectional messaging. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-API-GATEWAY-JP-03

- [ ] **Question:** A basic Route/resource-method check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws apigateway get-stages --rest-api-id API_ID` and capture exact status/reason/request ID. matches request and invokes an integration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-API-GATEWAY-JP-04

- [ ] **Code:** **Question:** A basic Lambda proxy integration check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws apigatewayv2 get-integrations --api-id API_ID` and capture exact status/reason/request ID. passes normalized request/event and expects defined response shape. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-API-GATEWAY-JP-05

- [ ] **Question:** A basic Authorizer check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws apigateway get-rest-apis` and capture exact status/reason/request ID. IAM/JWT/Lambda identity decision with cache and failure implications. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-API-GATEWAY-JP-06

- [ ] **Question:** A basic Usage plan/API key check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws apigatewayv2 get-apis` and capture exact status/reason/request ID. metering/throttle association is not user authentication by itself. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-API-GATEWAY-JP-07

- [ ] **Code:** **Question:** A basic Stage/deployment check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws apigateway get-stages --rest-api-id API_ID` and capture exact status/reason/request ID. immutable API snapshot and stage settings/canary/logging form release unit. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-API-GATEWAY-JP-08

- [ ] **Question:** A basic Throttling check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws apigatewayv2 get-integrations --api-id API_ID` and capture exact status/reason/request ID. account/stage/route limits protect gateway/downstream and return retryable errors. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-API-GATEWAY-JP-09

- [ ] **Question:** A basic Custom domain check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws apigateway get-rest-apis` and capture exact status/reason/request ID. certificate, endpoint type, API mapping and DNS compose the public endpoint. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-API-GATEWAY-JP-10

- [ ] **Code:** **Question:** A basic Access/execution logs check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws apigatewayv2 get-apis` and capture exact status/reason/request ID. request IDs, integration latency/status and safe fields support diagnosis. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-API-GATEWAY-MN-01

- [ ] **Question:** Compare REST vs HTTP API with WebSocket API. When would each change your design?

**Answer:** REST vs HTTP API: feature/integration/authorization/transformation and price differ. WebSocket API: connection routes and state/callback management support bidirectional messaging. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-API-GATEWAY-MN-02

- [ ] **Question:** Compare WebSocket API with Route/resource-method. When would each change your design?

**Answer:** WebSocket API: connection routes and state/callback management support bidirectional messaging. Route/resource-method: matches request and invokes an integration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-API-GATEWAY-MN-03

- [ ] **Question:** Compare Route/resource-method with Lambda proxy integration. When would each change your design?

**Answer:** Route/resource-method: matches request and invokes an integration. Lambda proxy integration: passes normalized request/event and expects defined response shape. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-API-GATEWAY-MN-04

- [ ] **Configuration review:** **Question:** Compare Lambda proxy integration with Authorizer. When would each change your design?

**Answer:** Lambda proxy integration: passes normalized request/event and expects defined response shape. Authorizer: IAM/JWT/Lambda identity decision with cache and failure implications. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-API-GATEWAY-MN-05

- [ ] **Question:** Compare Authorizer with Usage plan/API key. When would each change your design?

**Answer:** Authorizer: IAM/JWT/Lambda identity decision with cache and failure implications. Usage plan/API key: metering/throttle association is not user authentication by itself. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-API-GATEWAY-MN-06

- [ ] **Question:** Compare Usage plan/API key with Stage/deployment. When would each change your design?

**Answer:** Usage plan/API key: metering/throttle association is not user authentication by itself. Stage/deployment: immutable API snapshot and stage settings/canary/logging form release unit. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-API-GATEWAY-MN-07

- [ ] **Configuration review:** **Question:** Compare Stage/deployment with Throttling. When would each change your design?

**Answer:** Stage/deployment: immutable API snapshot and stage settings/canary/logging form release unit. Throttling: account/stage/route limits protect gateway/downstream and return retryable errors. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-API-GATEWAY-MN-08

- [ ] **Question:** Compare Throttling with Custom domain. When would each change your design?

**Answer:** Throttling: account/stage/route limits protect gateway/downstream and return retryable errors. Custom domain: certificate, endpoint type, API mapping and DNS compose the public endpoint. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-API-GATEWAY-MN-09

- [ ] **Question:** Compare Custom domain with Access/execution logs. When would each change your design?

**Answer:** Custom domain: certificate, endpoint type, API mapping and DNS compose the public endpoint. Access/execution logs: request IDs, integration latency/status and safe fields support diagnosis. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-API-GATEWAY-MN-10

- [ ] **Configuration review:** **Question:** Compare Access/execution logs with REST vs HTTP API. When would each change your design?

**Answer:** Access/execution logs: request IDs, integration latency/status and safe fields support diagnosis. REST vs HTTP API: feature/integration/authorization/transformation and price differ. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-API-GATEWAY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around REST vs HTTP API; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws apigateway get-rest-apis` plus recent events/changes, then correlate the service-specific SLI. feature/integration/authorization/transformation and price differ. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-API-GATEWAY-MP-02

- [ ] **Question:** Production is degraded around WebSocket API; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws apigatewayv2 get-apis` plus recent events/changes, then correlate the service-specific SLI. connection routes and state/callback management support bidirectional messaging. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-API-GATEWAY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Route/resource-method; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws apigateway get-stages --rest-api-id API_ID` plus recent events/changes, then correlate the service-specific SLI. matches request and invokes an integration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-API-GATEWAY-MP-04

- [ ] **Question:** Production is degraded around Lambda proxy integration; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws apigatewayv2 get-integrations --api-id API_ID` plus recent events/changes, then correlate the service-specific SLI. passes normalized request/event and expects defined response shape. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-API-GATEWAY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Authorizer; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws apigateway get-rest-apis` plus recent events/changes, then correlate the service-specific SLI. IAM/JWT/Lambda identity decision with cache and failure implications. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-API-GATEWAY-MP-06

- [ ] **Question:** Production is degraded around Usage plan/API key; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws apigatewayv2 get-apis` plus recent events/changes, then correlate the service-specific SLI. metering/throttle association is not user authentication by itself. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-API-GATEWAY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Stage/deployment; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws apigateway get-stages --rest-api-id API_ID` plus recent events/changes, then correlate the service-specific SLI. immutable API snapshot and stage settings/canary/logging form release unit. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-API-GATEWAY-MP-08

- [ ] **Question:** Production is degraded around Throttling; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws apigatewayv2 get-integrations --api-id API_ID` plus recent events/changes, then correlate the service-specific SLI. account/stage/route limits protect gateway/downstream and return retryable errors. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-API-GATEWAY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Custom domain; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws apigateway get-rest-apis` plus recent events/changes, then correlate the service-specific SLI. certificate, endpoint type, API mapping and DNS compose the public endpoint. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-API-GATEWAY-MP-10

- [ ] **Question:** Production is degraded around Access/execution logs; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws apigatewayv2 get-apis` plus recent events/changes, then correlate the service-specific SLI. request IDs, integration latency/status and safe fields support diagnosis. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-API-GATEWAY-SN-01

- [ ] **Question:** Design a production Amazon API Gateway capability where REST vs HTTP API, Lambda proxy integration and Stage/deployment are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: feature/integration/authorization/transformation and price differ. passes normalized request/event and expects defined response shape. immutable API snapshot and stage settings/canary/logging form release unit. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-API-GATEWAY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon API Gateway capability where WebSocket API, Authorizer and Throttling are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: connection routes and state/callback management support bidirectional messaging. IAM/JWT/Lambda identity decision with cache and failure implications. account/stage/route limits protect gateway/downstream and return retryable errors. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-API-GATEWAY-SN-03

- [ ] **Question:** Design a production Amazon API Gateway capability where Route/resource-method, Usage plan/API key and Custom domain are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: matches request and invokes an integration. metering/throttle association is not user authentication by itself. certificate, endpoint type, API mapping and DNS compose the public endpoint. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-API-GATEWAY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon API Gateway capability where Lambda proxy integration, Stage/deployment and Access/execution logs are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: passes normalized request/event and expects defined response shape. immutable API snapshot and stage settings/canary/logging form release unit. request IDs, integration latency/status and safe fields support diagnosis. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-API-GATEWAY-SN-05

- [ ] **Question:** Design a production Amazon API Gateway capability where Authorizer, Throttling and REST vs HTTP API are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: IAM/JWT/Lambda identity decision with cache and failure implications. account/stage/route limits protect gateway/downstream and return retryable errors. feature/integration/authorization/transformation and price differ. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-API-GATEWAY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon API Gateway capability where Usage plan/API key, Custom domain and WebSocket API are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: metering/throttle association is not user authentication by itself. certificate, endpoint type, API mapping and DNS compose the public endpoint. connection routes and state/callback management support bidirectional messaging. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-API-GATEWAY-SN-07

- [ ] **Question:** Design a production Amazon API Gateway capability where Stage/deployment, Access/execution logs and Route/resource-method are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable API snapshot and stage settings/canary/logging form release unit. request IDs, integration latency/status and safe fields support diagnosis. matches request and invokes an integration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-API-GATEWAY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon API Gateway capability where Throttling, REST vs HTTP API and Lambda proxy integration are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: account/stage/route limits protect gateway/downstream and return retryable errors. feature/integration/authorization/transformation and price differ. passes normalized request/event and expects defined response shape. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-API-GATEWAY-SN-09

- [ ] **Question:** Design a production Amazon API Gateway capability where Custom domain, WebSocket API and Authorizer are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: certificate, endpoint type, API mapping and DNS compose the public endpoint. connection routes and state/callback management support bidirectional messaging. IAM/JWT/Lambda identity decision with cache and failure implications. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-API-GATEWAY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon API Gateway capability where Access/execution logs, Route/resource-method and Usage plan/API key are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: request IDs, integration latency/status and safe fields support diagnosis. matches request and invokes an integration. metering/throttle association is not user authentication by itself. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-API-GATEWAY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving REST vs HTTP API. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws apigateway get-rest-apis` as one read-only checkpoint, not the whole diagnosis. feature/integration/authorization/transformation and price differ. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-API-GATEWAY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving WebSocket API. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws apigatewayv2 get-apis` as one read-only checkpoint, not the whole diagnosis. connection routes and state/callback management support bidirectional messaging. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-API-GATEWAY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Route/resource-method. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws apigateway get-stages --rest-api-id API_ID` as one read-only checkpoint, not the whole diagnosis. matches request and invokes an integration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-API-GATEWAY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lambda proxy integration. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws apigatewayv2 get-integrations --api-id API_ID` as one read-only checkpoint, not the whole diagnosis. passes normalized request/event and expects defined response shape. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-API-GATEWAY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authorizer. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws apigateway get-rest-apis` as one read-only checkpoint, not the whole diagnosis. IAM/JWT/Lambda identity decision with cache and failure implications. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-API-GATEWAY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Usage plan/API key. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws apigatewayv2 get-apis` as one read-only checkpoint, not the whole diagnosis. metering/throttle association is not user authentication by itself. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-API-GATEWAY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stage/deployment. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws apigateway get-stages --rest-api-id API_ID` as one read-only checkpoint, not the whole diagnosis. immutable API snapshot and stage settings/canary/logging form release unit. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-API-GATEWAY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Throttling. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws apigatewayv2 get-integrations --api-id API_ID` as one read-only checkpoint, not the whole diagnosis. account/stage/route limits protect gateway/downstream and return retryable errors. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-API-GATEWAY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Custom domain. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws apigateway get-rest-apis` as one read-only checkpoint, not the whole diagnosis. certificate, endpoint type, API mapping and DNS compose the public endpoint. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-API-GATEWAY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Access/execution logs. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws apigatewayv2 get-apis` as one read-only checkpoint, not the whole diagnosis. request IDs, integration latency/status and safe fields support diagnosis. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
