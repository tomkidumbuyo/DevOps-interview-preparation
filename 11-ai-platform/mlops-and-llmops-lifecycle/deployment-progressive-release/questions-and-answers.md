# ML/LLM deployment and progressive release — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JN-01

- [ ] **Question:** What is Release manifest, and why does it matter in ML/LLM deployment and progressive release?

**Answer:** model, tokenizer, prompt, adapter, runtime, hardware, index, policy and evaluator versions form one deployable contract. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JN-02

- [ ] **Question:** What is Shadow, and why does it matter in ML/LLM deployment and progressive release?

**Answer:** copies production inputs without user-visible output and requires privacy, side-effect and cost controls. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JN-03

- [ ] **Question:** What is Canary, and why does it matter in ML/LLM deployment and progressive release?

**Answer:** routes bounded real traffic with automatic infrastructure and task-quality abort thresholds. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JN-04

- [ ] **Question:** What is Champion/challenger, and why does it matter in ML/LLM deployment and progressive release?

**Answer:** retains incumbent and candidate comparison under explicit promotion authority. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JN-05

- [ ] **Question:** What is Traffic unit, and why does it matter in ML/LLM deployment and progressive release?

**Answer:** request/user/session/tenant assignment and stickiness determine unbiased consistent comparison. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JN-06

- [ ] **Question:** What is Warmup, and why does it matter in ML/LLM deployment and progressive release?

**Answer:** model download/load/compile/cache and representative request warmup occur before traffic readiness. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JN-07

- [ ] **Question:** What is Compatibility, and why does it matter in ML/LLM deployment and progressive release?

**Answer:** schema, client, cache, feature/index and persisted state must work during mixed-version rollout. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JN-08

- [ ] **Code:** **Question:** What does `curl -s http://MODEL/metrics | rg 'request|token|latency|error'` help you verify for ML/LLM deployment and progressive release?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: prior bytes/config/index/policy/capacity remain available and correctness is reverified after reversal.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JN-09

- [ ] **Code:** **Question:** What does `kubectl rollout status deployment/MODEL -n inference` help you verify for ML/LLM deployment and progressive release?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: rare quality/safety failures may require longer/sample-aware gates than latency/error metrics.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JN-10

- [ ] **Code:** **Question:** What does `kubectl rollout history deployment/MODEL -n inference` help you verify for ML/LLM deployment and progressive release?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: release actor, evidence, traffic changes, exceptions, incidents and final deployed digest remain linked.

## Junior — procedural and command questions

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JP-01

- [ ] **Code:** **Question:** A basic Release manifest check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status deployment/MODEL -n inference` and capture exact status/reason/request ID. model, tokenizer, prompt, adapter, runtime, hardware, index, policy and evaluator versions form one deployable contract. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JP-02

- [ ] **Question:** A basic Shadow check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout history deployment/MODEL -n inference` and capture exact status/reason/request ID. copies production inputs without user-visible output and requires privacy, side-effect and cost controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JP-03

- [ ] **Question:** A basic Canary check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get inferenceservice MODEL -n inference -o yaml` and capture exact status/reason/request ID. routes bounded real traffic with automatic infrastructure and task-quality abort thresholds. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JP-04

- [ ] **Code:** **Question:** A basic Champion/challenger check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics | rg 'request|token|latency|error'` and capture exact status/reason/request ID. retains incumbent and candidate comparison under explicit promotion authority. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JP-05

- [ ] **Question:** A basic Traffic unit check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status deployment/MODEL -n inference` and capture exact status/reason/request ID. request/user/session/tenant assignment and stickiness determine unbiased consistent comparison. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JP-06

- [ ] **Question:** A basic Warmup check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout history deployment/MODEL -n inference` and capture exact status/reason/request ID. model download/load/compile/cache and representative request warmup occur before traffic readiness. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JP-07

- [ ] **Code:** **Question:** A basic Compatibility check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get inferenceservice MODEL -n inference -o yaml` and capture exact status/reason/request ID. schema, client, cache, feature/index and persisted state must work during mixed-version rollout. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JP-08

- [ ] **Question:** A basic Rollback check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics | rg 'request|token|latency|error'` and capture exact status/reason/request ID. prior bytes/config/index/policy/capacity remain available and correctness is reverified after reversal. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JP-09

- [ ] **Question:** A basic Evidence window check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status deployment/MODEL -n inference` and capture exact status/reason/request ID. rare quality/safety failures may require longer/sample-aware gates than latency/error metrics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-JP-10

- [ ] **Code:** **Question:** A basic Audit check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout history deployment/MODEL -n inference` and capture exact status/reason/request ID. release actor, evidence, traffic changes, exceptions, incidents and final deployed digest remain linked. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MN-01

- [ ] **Question:** Compare Release manifest with Shadow. When would each change your design?

**Answer:** Release manifest: model, tokenizer, prompt, adapter, runtime, hardware, index, policy and evaluator versions form one deployable contract. Shadow: copies production inputs without user-visible output and requires privacy, side-effect and cost controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MN-02

- [ ] **Question:** Compare Shadow with Canary. When would each change your design?

**Answer:** Shadow: copies production inputs without user-visible output and requires privacy, side-effect and cost controls. Canary: routes bounded real traffic with automatic infrastructure and task-quality abort thresholds. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MN-03

- [ ] **Question:** Compare Canary with Champion/challenger. When would each change your design?

**Answer:** Canary: routes bounded real traffic with automatic infrastructure and task-quality abort thresholds. Champion/challenger: retains incumbent and candidate comparison under explicit promotion authority. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MN-04

- [ ] **Configuration review:** **Question:** Compare Champion/challenger with Traffic unit. When would each change your design?

**Answer:** Champion/challenger: retains incumbent and candidate comparison under explicit promotion authority. Traffic unit: request/user/session/tenant assignment and stickiness determine unbiased consistent comparison. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MN-05

- [ ] **Question:** Compare Traffic unit with Warmup. When would each change your design?

**Answer:** Traffic unit: request/user/session/tenant assignment and stickiness determine unbiased consistent comparison. Warmup: model download/load/compile/cache and representative request warmup occur before traffic readiness. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MN-06

- [ ] **Question:** Compare Warmup with Compatibility. When would each change your design?

**Answer:** Warmup: model download/load/compile/cache and representative request warmup occur before traffic readiness. Compatibility: schema, client, cache, feature/index and persisted state must work during mixed-version rollout. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MN-07

- [ ] **Configuration review:** **Question:** Compare Compatibility with Rollback. When would each change your design?

**Answer:** Compatibility: schema, client, cache, feature/index and persisted state must work during mixed-version rollout. Rollback: prior bytes/config/index/policy/capacity remain available and correctness is reverified after reversal. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MN-08

- [ ] **Question:** Compare Rollback with Evidence window. When would each change your design?

**Answer:** Rollback: prior bytes/config/index/policy/capacity remain available and correctness is reverified after reversal. Evidence window: rare quality/safety failures may require longer/sample-aware gates than latency/error metrics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MN-09

- [ ] **Question:** Compare Evidence window with Audit. When would each change your design?

**Answer:** Evidence window: rare quality/safety failures may require longer/sample-aware gates than latency/error metrics. Audit: release actor, evidence, traffic changes, exceptions, incidents and final deployed digest remain linked. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MN-10

- [ ] **Configuration review:** **Question:** Compare Audit with Release manifest. When would each change your design?

**Answer:** Audit: release actor, evidence, traffic changes, exceptions, incidents and final deployed digest remain linked. Release manifest: model, tokenizer, prompt, adapter, runtime, hardware, index, policy and evaluator versions form one deployable contract. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Release manifest; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status deployment/MODEL -n inference` plus recent events/changes, then correlate the service-specific SLI. model, tokenizer, prompt, adapter, runtime, hardware, index, policy and evaluator versions form one deployable contract. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MP-02

- [ ] **Question:** Production is degraded around Shadow; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout history deployment/MODEL -n inference` plus recent events/changes, then correlate the service-specific SLI. copies production inputs without user-visible output and requires privacy, side-effect and cost controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Canary; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get inferenceservice MODEL -n inference -o yaml` plus recent events/changes, then correlate the service-specific SLI. routes bounded real traffic with automatic infrastructure and task-quality abort thresholds. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MP-04

- [ ] **Question:** Production is degraded around Champion/challenger; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics | rg 'request|token|latency|error'` plus recent events/changes, then correlate the service-specific SLI. retains incumbent and candidate comparison under explicit promotion authority. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Traffic unit; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status deployment/MODEL -n inference` plus recent events/changes, then correlate the service-specific SLI. request/user/session/tenant assignment and stickiness determine unbiased consistent comparison. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MP-06

- [ ] **Question:** Production is degraded around Warmup; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout history deployment/MODEL -n inference` plus recent events/changes, then correlate the service-specific SLI. model download/load/compile/cache and representative request warmup occur before traffic readiness. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Compatibility; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get inferenceservice MODEL -n inference -o yaml` plus recent events/changes, then correlate the service-specific SLI. schema, client, cache, feature/index and persisted state must work during mixed-version rollout. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MP-08

- [ ] **Question:** Production is degraded around Rollback; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics | rg 'request|token|latency|error'` plus recent events/changes, then correlate the service-specific SLI. prior bytes/config/index/policy/capacity remain available and correctness is reverified after reversal. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Evidence window; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status deployment/MODEL -n inference` plus recent events/changes, then correlate the service-specific SLI. rare quality/safety failures may require longer/sample-aware gates than latency/error metrics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-MP-10

- [ ] **Question:** Production is degraded around Audit; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout history deployment/MODEL -n inference` plus recent events/changes, then correlate the service-specific SLI. release actor, evidence, traffic changes, exceptions, incidents and final deployed digest remain linked. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SN-01

- [ ] **Question:** Design a production ML/LLM deployment and progressive release capability where Release manifest, Champion/challenger and Compatibility are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model, tokenizer, prompt, adapter, runtime, hardware, index, policy and evaluator versions form one deployable contract. retains incumbent and candidate comparison under explicit promotion authority. schema, client, cache, feature/index and persisted state must work during mixed-version rollout. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production ML/LLM deployment and progressive release capability where Shadow, Traffic unit and Rollback are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: copies production inputs without user-visible output and requires privacy, side-effect and cost controls. request/user/session/tenant assignment and stickiness determine unbiased consistent comparison. prior bytes/config/index/policy/capacity remain available and correctness is reverified after reversal. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SN-03

- [ ] **Question:** Design a production ML/LLM deployment and progressive release capability where Canary, Warmup and Evidence window are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: routes bounded real traffic with automatic infrastructure and task-quality abort thresholds. model download/load/compile/cache and representative request warmup occur before traffic readiness. rare quality/safety failures may require longer/sample-aware gates than latency/error metrics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production ML/LLM deployment and progressive release capability where Champion/challenger, Compatibility and Audit are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retains incumbent and candidate comparison under explicit promotion authority. schema, client, cache, feature/index and persisted state must work during mixed-version rollout. release actor, evidence, traffic changes, exceptions, incidents and final deployed digest remain linked. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SN-05

- [ ] **Question:** Design a production ML/LLM deployment and progressive release capability where Traffic unit, Rollback and Release manifest are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: request/user/session/tenant assignment and stickiness determine unbiased consistent comparison. prior bytes/config/index/policy/capacity remain available and correctness is reverified after reversal. model, tokenizer, prompt, adapter, runtime, hardware, index, policy and evaluator versions form one deployable contract. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production ML/LLM deployment and progressive release capability where Warmup, Evidence window and Shadow are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model download/load/compile/cache and representative request warmup occur before traffic readiness. rare quality/safety failures may require longer/sample-aware gates than latency/error metrics. copies production inputs without user-visible output and requires privacy, side-effect and cost controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SN-07

- [ ] **Question:** Design a production ML/LLM deployment and progressive release capability where Compatibility, Audit and Canary are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: schema, client, cache, feature/index and persisted state must work during mixed-version rollout. release actor, evidence, traffic changes, exceptions, incidents and final deployed digest remain linked. routes bounded real traffic with automatic infrastructure and task-quality abort thresholds. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production ML/LLM deployment and progressive release capability where Rollback, Release manifest and Champion/challenger are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prior bytes/config/index/policy/capacity remain available and correctness is reverified after reversal. model, tokenizer, prompt, adapter, runtime, hardware, index, policy and evaluator versions form one deployable contract. retains incumbent and candidate comparison under explicit promotion authority. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SN-09

- [ ] **Question:** Design a production ML/LLM deployment and progressive release capability where Evidence window, Shadow and Traffic unit are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: rare quality/safety failures may require longer/sample-aware gates than latency/error metrics. copies production inputs without user-visible output and requires privacy, side-effect and cost controls. request/user/session/tenant assignment and stickiness determine unbiased consistent comparison. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production ML/LLM deployment and progressive release capability where Audit, Canary and Warmup are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: release actor, evidence, traffic changes, exceptions, incidents and final deployed digest remain linked. routes bounded real traffic with automatic infrastructure and task-quality abort thresholds. model download/load/compile/cache and representative request warmup occur before traffic readiness. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Release manifest. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status deployment/MODEL -n inference` as one read-only checkpoint, not the whole diagnosis. model, tokenizer, prompt, adapter, runtime, hardware, index, policy and evaluator versions form one deployable contract. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Shadow. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout history deployment/MODEL -n inference` as one read-only checkpoint, not the whole diagnosis. copies production inputs without user-visible output and requires privacy, side-effect and cost controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Canary. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get inferenceservice MODEL -n inference -o yaml` as one read-only checkpoint, not the whole diagnosis. routes bounded real traffic with automatic infrastructure and task-quality abort thresholds. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Champion/challenger. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics | rg 'request|token|latency|error'` as one read-only checkpoint, not the whole diagnosis. retains incumbent and candidate comparison under explicit promotion authority. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Traffic unit. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status deployment/MODEL -n inference` as one read-only checkpoint, not the whole diagnosis. request/user/session/tenant assignment and stickiness determine unbiased consistent comparison. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Warmup. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout history deployment/MODEL -n inference` as one read-only checkpoint, not the whole diagnosis. model download/load/compile/cache and representative request warmup occur before traffic readiness. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Compatibility. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get inferenceservice MODEL -n inference -o yaml` as one read-only checkpoint, not the whole diagnosis. schema, client, cache, feature/index and persisted state must work during mixed-version rollout. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rollback. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics | rg 'request|token|latency|error'` as one read-only checkpoint, not the whole diagnosis. prior bytes/config/index/policy/capacity remain available and correctness is reverified after reversal. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Evidence window. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status deployment/MODEL -n inference` as one read-only checkpoint, not the whole diagnosis. rare quality/safety failures may require longer/sample-aware gates than latency/error metrics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-LLM-DEPLOYMENT-AND-PROGRESSIVE-RELEASE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Audit. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout history deployment/MODEL -n inference` as one read-only checkpoint, not the whole diagnosis. release actor, evidence, traffic changes, exceptions, incidents and final deployed digest remain linked. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
