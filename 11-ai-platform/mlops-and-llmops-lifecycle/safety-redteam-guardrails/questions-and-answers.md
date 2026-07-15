# LLM safety, red teaming and guardrail operations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JN-01

- [ ] **Question:** What is Threat model, and why does it matter in LLM safety, red teaming and guardrail operations?

**Answer:** assets, actors, trust boundaries and abuse cases span prompt, retrieval, model, tool, provider and operators. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JN-02

- [ ] **Question:** What is Policy taxonomy, and why does it matter in LLM safety, red teaming and guardrail operations?

**Answer:** harmful content, privacy, authorization, regulated advice and customer-specific rules need owned definitions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JN-03

- [ ] **Question:** What is Pre-input control, and why does it matter in LLM safety, red teaming and guardrail operations?

**Answer:** size/schema/malware/PII and policy checks bound input but cannot prove downstream safety. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JN-04

- [ ] **Question:** What is Prompt injection, and why does it matter in LLM safety, red teaming and guardrail operations?

**Answer:** untrusted user/retrieved/tool content cannot grant system or tool authority. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JN-05

- [ ] **Question:** What is Output control, and why does it matter in LLM safety, red teaming and guardrail operations?

**Answer:** validate structured data, content policy, citations and destinations before display or execution. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JN-06

- [ ] **Question:** What is Tool guardrail, and why does it matter in LLM safety, red teaming and guardrail operations?

**Answer:** deterministic authorization, schema/range checks, idempotency and approval mediate model-proposed actions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JN-07

- [ ] **Question:** What is Red-team corpus, and why does it matter in LLM safety, red teaming and guardrail operations?

**Answer:** versioned attack/edge cases record threat, expected behavior, severity and regression owner. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JN-08

- [ ] **Code:** **Question:** What does `kubectl logs -n ai-platform deploy/policy-engine --since=30m` help you verify for LLM safety, red teaming and guardrail operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: mutation/multiturn/encoding/tool/retrieval attacks explore beyond static known strings.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JN-09

- [ ] **Code:** **Question:** What does `python -m pytest tests/guardrails -q` help you verify for LLM safety, red teaming and guardrail operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: false positive/negative, override/appeal, latency, availability and policy-version metrics have SLO/owners.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JN-10

- [ ] **Code:** **Question:** What does `python redteam.py --manifest release.yaml --suite suites/prompt-injection.yaml` help you verify for LLM safety, red teaming and guardrail operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: preserve safe evidence, contain routes/tools/data, add regression cases and verify control changes.

## Junior — procedural and command questions

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JP-01

- [ ] **Code:** **Question:** A basic Threat model check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/guardrails -q` and capture exact status/reason/request ID. assets, actors, trust boundaries and abuse cases span prompt, retrieval, model, tool, provider and operators. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JP-02

- [ ] **Question:** A basic Policy taxonomy check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python redteam.py --manifest release.yaml --suite suites/prompt-injection.yaml` and capture exact status/reason/request ID. harmful content, privacy, authorization, regulated advice and customer-specific rules need owned definitions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JP-03

- [ ] **Question:** A basic Pre-input control check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `opa test policy/` and capture exact status/reason/request ID. size/schema/malware/PII and policy checks bound input but cannot prove downstream safety. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JP-04

- [ ] **Code:** **Question:** A basic Prompt injection check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n ai-platform deploy/policy-engine --since=30m` and capture exact status/reason/request ID. untrusted user/retrieved/tool content cannot grant system or tool authority. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JP-05

- [ ] **Question:** A basic Output control check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/guardrails -q` and capture exact status/reason/request ID. validate structured data, content policy, citations and destinations before display or execution. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JP-06

- [ ] **Question:** A basic Tool guardrail check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python redteam.py --manifest release.yaml --suite suites/prompt-injection.yaml` and capture exact status/reason/request ID. deterministic authorization, schema/range checks, idempotency and approval mediate model-proposed actions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JP-07

- [ ] **Code:** **Question:** A basic Red-team corpus check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `opa test policy/` and capture exact status/reason/request ID. versioned attack/edge cases record threat, expected behavior, severity and regression owner. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JP-08

- [ ] **Question:** A basic Adaptive testing check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n ai-platform deploy/policy-engine --since=30m` and capture exact status/reason/request ID. mutation/multiturn/encoding/tool/retrieval attacks explore beyond static known strings. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JP-09

- [ ] **Question:** A basic Operations check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/guardrails -q` and capture exact status/reason/request ID. false positive/negative, override/appeal, latency, availability and policy-version metrics have SLO/owners. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-JP-10

- [ ] **Code:** **Question:** A basic Incident learning check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python redteam.py --manifest release.yaml --suite suites/prompt-injection.yaml` and capture exact status/reason/request ID. preserve safe evidence, contain routes/tools/data, add regression cases and verify control changes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MN-01

- [ ] **Question:** Compare Threat model with Policy taxonomy. When would each change your design?

**Answer:** Threat model: assets, actors, trust boundaries and abuse cases span prompt, retrieval, model, tool, provider and operators. Policy taxonomy: harmful content, privacy, authorization, regulated advice and customer-specific rules need owned definitions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MN-02

- [ ] **Question:** Compare Policy taxonomy with Pre-input control. When would each change your design?

**Answer:** Policy taxonomy: harmful content, privacy, authorization, regulated advice and customer-specific rules need owned definitions. Pre-input control: size/schema/malware/PII and policy checks bound input but cannot prove downstream safety. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MN-03

- [ ] **Question:** Compare Pre-input control with Prompt injection. When would each change your design?

**Answer:** Pre-input control: size/schema/malware/PII and policy checks bound input but cannot prove downstream safety. Prompt injection: untrusted user/retrieved/tool content cannot grant system or tool authority. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Prompt injection with Output control. When would each change your design?

**Answer:** Prompt injection: untrusted user/retrieved/tool content cannot grant system or tool authority. Output control: validate structured data, content policy, citations and destinations before display or execution. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MN-05

- [ ] **Question:** Compare Output control with Tool guardrail. When would each change your design?

**Answer:** Output control: validate structured data, content policy, citations and destinations before display or execution. Tool guardrail: deterministic authorization, schema/range checks, idempotency and approval mediate model-proposed actions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MN-06

- [ ] **Question:** Compare Tool guardrail with Red-team corpus. When would each change your design?

**Answer:** Tool guardrail: deterministic authorization, schema/range checks, idempotency and approval mediate model-proposed actions. Red-team corpus: versioned attack/edge cases record threat, expected behavior, severity and regression owner. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Red-team corpus with Adaptive testing. When would each change your design?

**Answer:** Red-team corpus: versioned attack/edge cases record threat, expected behavior, severity and regression owner. Adaptive testing: mutation/multiturn/encoding/tool/retrieval attacks explore beyond static known strings. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MN-08

- [ ] **Question:** Compare Adaptive testing with Operations. When would each change your design?

**Answer:** Adaptive testing: mutation/multiturn/encoding/tool/retrieval attacks explore beyond static known strings. Operations: false positive/negative, override/appeal, latency, availability and policy-version metrics have SLO/owners. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MN-09

- [ ] **Question:** Compare Operations with Incident learning. When would each change your design?

**Answer:** Operations: false positive/negative, override/appeal, latency, availability and policy-version metrics have SLO/owners. Incident learning: preserve safe evidence, contain routes/tools/data, add regression cases and verify control changes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Incident learning with Threat model. When would each change your design?

**Answer:** Incident learning: preserve safe evidence, contain routes/tools/data, add regression cases and verify control changes. Threat model: assets, actors, trust boundaries and abuse cases span prompt, retrieval, model, tool, provider and operators. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Threat model; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/guardrails -q` plus recent events/changes, then correlate the service-specific SLI. assets, actors, trust boundaries and abuse cases span prompt, retrieval, model, tool, provider and operators. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MP-02

- [ ] **Question:** Production is degraded around Policy taxonomy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python redteam.py --manifest release.yaml --suite suites/prompt-injection.yaml` plus recent events/changes, then correlate the service-specific SLI. harmful content, privacy, authorization, regulated advice and customer-specific rules need owned definitions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pre-input control; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `opa test policy/` plus recent events/changes, then correlate the service-specific SLI. size/schema/malware/PII and policy checks bound input but cannot prove downstream safety. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MP-04

- [ ] **Question:** Production is degraded around Prompt injection; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n ai-platform deploy/policy-engine --since=30m` plus recent events/changes, then correlate the service-specific SLI. untrusted user/retrieved/tool content cannot grant system or tool authority. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Output control; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/guardrails -q` plus recent events/changes, then correlate the service-specific SLI. validate structured data, content policy, citations and destinations before display or execution. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MP-06

- [ ] **Question:** Production is degraded around Tool guardrail; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python redteam.py --manifest release.yaml --suite suites/prompt-injection.yaml` plus recent events/changes, then correlate the service-specific SLI. deterministic authorization, schema/range checks, idempotency and approval mediate model-proposed actions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Red-team corpus; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `opa test policy/` plus recent events/changes, then correlate the service-specific SLI. versioned attack/edge cases record threat, expected behavior, severity and regression owner. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MP-08

- [ ] **Question:** Production is degraded around Adaptive testing; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n ai-platform deploy/policy-engine --since=30m` plus recent events/changes, then correlate the service-specific SLI. mutation/multiturn/encoding/tool/retrieval attacks explore beyond static known strings. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Operations; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/guardrails -q` plus recent events/changes, then correlate the service-specific SLI. false positive/negative, override/appeal, latency, availability and policy-version metrics have SLO/owners. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-MP-10

- [ ] **Question:** Production is degraded around Incident learning; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python redteam.py --manifest release.yaml --suite suites/prompt-injection.yaml` plus recent events/changes, then correlate the service-specific SLI. preserve safe evidence, contain routes/tools/data, add regression cases and verify control changes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SN-01

- [ ] **Question:** Design a production LLM safety, red teaming and guardrail operations capability where Threat model, Prompt injection and Red-team corpus are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: assets, actors, trust boundaries and abuse cases span prompt, retrieval, model, tool, provider and operators. untrusted user/retrieved/tool content cannot grant system or tool authority. versioned attack/edge cases record threat, expected behavior, severity and regression owner. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production LLM safety, red teaming and guardrail operations capability where Policy taxonomy, Output control and Adaptive testing are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: harmful content, privacy, authorization, regulated advice and customer-specific rules need owned definitions. validate structured data, content policy, citations and destinations before display or execution. mutation/multiturn/encoding/tool/retrieval attacks explore beyond static known strings. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SN-03

- [ ] **Question:** Design a production LLM safety, red teaming and guardrail operations capability where Pre-input control, Tool guardrail and Operations are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: size/schema/malware/PII and policy checks bound input but cannot prove downstream safety. deterministic authorization, schema/range checks, idempotency and approval mediate model-proposed actions. false positive/negative, override/appeal, latency, availability and policy-version metrics have SLO/owners. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production LLM safety, red teaming and guardrail operations capability where Prompt injection, Red-team corpus and Incident learning are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: untrusted user/retrieved/tool content cannot grant system or tool authority. versioned attack/edge cases record threat, expected behavior, severity and regression owner. preserve safe evidence, contain routes/tools/data, add regression cases and verify control changes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SN-05

- [ ] **Question:** Design a production LLM safety, red teaming and guardrail operations capability where Output control, Adaptive testing and Threat model are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: validate structured data, content policy, citations and destinations before display or execution. mutation/multiturn/encoding/tool/retrieval attacks explore beyond static known strings. assets, actors, trust boundaries and abuse cases span prompt, retrieval, model, tool, provider and operators. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production LLM safety, red teaming and guardrail operations capability where Tool guardrail, Operations and Policy taxonomy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: deterministic authorization, schema/range checks, idempotency and approval mediate model-proposed actions. false positive/negative, override/appeal, latency, availability and policy-version metrics have SLO/owners. harmful content, privacy, authorization, regulated advice and customer-specific rules need owned definitions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SN-07

- [ ] **Question:** Design a production LLM safety, red teaming and guardrail operations capability where Red-team corpus, Incident learning and Pre-input control are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versioned attack/edge cases record threat, expected behavior, severity and regression owner. preserve safe evidence, contain routes/tools/data, add regression cases and verify control changes. size/schema/malware/PII and policy checks bound input but cannot prove downstream safety. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production LLM safety, red teaming and guardrail operations capability where Adaptive testing, Threat model and Prompt injection are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: mutation/multiturn/encoding/tool/retrieval attacks explore beyond static known strings. assets, actors, trust boundaries and abuse cases span prompt, retrieval, model, tool, provider and operators. untrusted user/retrieved/tool content cannot grant system or tool authority. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SN-09

- [ ] **Question:** Design a production LLM safety, red teaming and guardrail operations capability where Operations, Policy taxonomy and Output control are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: false positive/negative, override/appeal, latency, availability and policy-version metrics have SLO/owners. harmful content, privacy, authorization, regulated advice and customer-specific rules need owned definitions. validate structured data, content policy, citations and destinations before display or execution. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production LLM safety, red teaming and guardrail operations capability where Incident learning, Pre-input control and Tool guardrail are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: preserve safe evidence, contain routes/tools/data, add regression cases and verify control changes. size/schema/malware/PII and policy checks bound input but cannot prove downstream safety. deterministic authorization, schema/range checks, idempotency and approval mediate model-proposed actions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Threat model. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/guardrails -q` as one read-only checkpoint, not the whole diagnosis. assets, actors, trust boundaries and abuse cases span prompt, retrieval, model, tool, provider and operators. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Policy taxonomy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python redteam.py --manifest release.yaml --suite suites/prompt-injection.yaml` as one read-only checkpoint, not the whole diagnosis. harmful content, privacy, authorization, regulated advice and customer-specific rules need owned definitions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pre-input control. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `opa test policy/` as one read-only checkpoint, not the whole diagnosis. size/schema/malware/PII and policy checks bound input but cannot prove downstream safety. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt injection. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n ai-platform deploy/policy-engine --since=30m` as one read-only checkpoint, not the whole diagnosis. untrusted user/retrieved/tool content cannot grant system or tool authority. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Output control. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/guardrails -q` as one read-only checkpoint, not the whole diagnosis. validate structured data, content policy, citations and destinations before display or execution. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tool guardrail. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python redteam.py --manifest release.yaml --suite suites/prompt-injection.yaml` as one read-only checkpoint, not the whole diagnosis. deterministic authorization, schema/range checks, idempotency and approval mediate model-proposed actions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Red-team corpus. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `opa test policy/` as one read-only checkpoint, not the whole diagnosis. versioned attack/edge cases record threat, expected behavior, severity and regression owner. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Adaptive testing. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n ai-platform deploy/policy-engine --since=30m` as one read-only checkpoint, not the whole diagnosis. mutation/multiturn/encoding/tool/retrieval attacks explore beyond static known strings. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Operations. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/guardrails -q` as one read-only checkpoint, not the whole diagnosis. false positive/negative, override/appeal, latency, availability and policy-version metrics have SLO/owners. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-SAFETY-RED-TEAMING-AND-GUARDRAIL-OPERATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Incident learning. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python redteam.py --manifest release.yaml --suite suites/prompt-injection.yaml` as one read-only checkpoint, not the whole diagnosis. preserve safe evidence, contain routes/tools/data, add regression cases and verify control changes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
