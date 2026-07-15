# Amazon Bedrock — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-BEDROCK-JN-01

- [ ] **Question:** What is Foundation model access, and why does it matter in Amazon Bedrock?
> **Covered in:** [Amazon Bedrock — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** model/provider/Region/API capability and terms must be approved. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-BEDROCK-JN-02

- [ ] **Question:** What is Converse/Invoke API, and why does it matter in Amazon Bedrock?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** normalized/model APIs differ in streaming, tools and request schema. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-BEDROCK-JN-03

- [ ] **Question:** What is Inference profile, and why does it matter in Amazon Bedrock?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** routes/model invocation capacity across supported Regions or application profiles. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-BEDROCK-JN-04

- [ ] **Question:** What is Provisioned throughput, and why does it matter in Amazon Bedrock?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** reserves model units/capacity for predictable demand at commitment cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-BEDROCK-JN-05

- [ ] **Question:** What is Guardrail, and why does it matter in Amazon Bedrock?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** evaluates input/output policies but is one layer rather than proof of safety. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-BEDROCK-JN-06

- [ ] **Question:** What is Knowledge Base, and why does it matter in Amazon Bedrock?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** managed ingestion/retrieval still needs source authorization, tenancy and freshness. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-BEDROCK-JN-07

- [ ] **Question:** What is Agent, and why does it matter in Amazon Bedrock?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** orchestrates models/actions/knowledge with least-privilege tools and human approval. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-BEDROCK-JN-08

- [ ] **Code:** **Question:** What does `aws bedrock list-inference-profiles` help you verify for Amazon Bedrock?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: datasets/metrics/judges compare candidates but need calibration/versioning.

### AMAZON-BEDROCK-JN-09

- [ ] **Code:** **Question:** What does `aws bedrock list-foundation-models` help you verify for Amazon Bedrock?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: improves capacity while changing data path/residency analysis.

### AMAZON-BEDROCK-JN-10

- [ ] **Code:** **Question:** What does `aws bedrock-runtime converse --model-id MODEL --messages file://messages.json` help you verify for Amazon Bedrock?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: input/output/cache/model/region usage supports budget and chargeback.

## Junior — procedural and command questions

### AMAZON-BEDROCK-JP-01

- [ ] **Code:** **Question:** A basic Foundation model access check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock list-foundation-models` and capture exact status/reason/request ID. model/provider/Region/API capability and terms must be approved. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-BEDROCK-JP-02

- [ ] **Question:** A basic Converse/Invoke API check fails. What would you do first?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock-runtime converse --model-id MODEL --messages file://messages.json` and capture exact status/reason/request ID. normalized/model APIs differ in streaming, tools and request schema. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-BEDROCK-JP-03

- [ ] **Question:** A basic Inference profile check fails. What would you do first?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock list-guardrails` and capture exact status/reason/request ID. routes/model invocation capacity across supported Regions or application profiles. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-BEDROCK-JP-04

- [ ] **Code:** **Question:** A basic Provisioned throughput check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock list-inference-profiles` and capture exact status/reason/request ID. reserves model units/capacity for predictable demand at commitment cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-BEDROCK-JP-05

- [ ] **Question:** A basic Guardrail check fails. What would you do first?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock list-foundation-models` and capture exact status/reason/request ID. evaluates input/output policies but is one layer rather than proof of safety. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-BEDROCK-JP-06

- [ ] **Question:** A basic Knowledge Base check fails. What would you do first?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock-runtime converse --model-id MODEL --messages file://messages.json` and capture exact status/reason/request ID. managed ingestion/retrieval still needs source authorization, tenancy and freshness. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-BEDROCK-JP-07

- [ ] **Code:** **Question:** A basic Agent check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock list-guardrails` and capture exact status/reason/request ID. orchestrates models/actions/knowledge with least-privilege tools and human approval. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-BEDROCK-JP-08

- [ ] **Question:** A basic Model evaluation check fails. What would you do first?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock list-inference-profiles` and capture exact status/reason/request ID. datasets/metrics/judges compare candidates but need calibration/versioning. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-BEDROCK-JP-09

- [ ] **Question:** A basic Cross-Region inference check fails. What would you do first?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock list-foundation-models` and capture exact status/reason/request ID. improves capacity while changing data path/residency analysis. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-BEDROCK-JP-10

- [ ] **Code:** **Question:** A basic Token metering check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Bedrock — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock-runtime converse --model-id MODEL --messages file://messages.json` and capture exact status/reason/request ID. input/output/cache/model/region usage supports budget and chargeback. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-BEDROCK-MN-01

- [ ] **Question:** Compare Foundation model access with Converse/Invoke API. When would each change your design?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Foundation model access: model/provider/Region/API capability and terms must be approved. Converse/Invoke API: normalized/model APIs differ in streaming, tools and request schema. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-BEDROCK-MN-02

- [ ] **Question:** Compare Converse/Invoke API with Inference profile. When would each change your design?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Converse/Invoke API: normalized/model APIs differ in streaming, tools and request schema. Inference profile: routes/model invocation capacity across supported Regions or application profiles. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-BEDROCK-MN-03

- [ ] **Question:** Compare Inference profile with Provisioned throughput. When would each change your design?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Inference profile: routes/model invocation capacity across supported Regions or application profiles. Provisioned throughput: reserves model units/capacity for predictable demand at commitment cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-BEDROCK-MN-04

- [ ] **Configuration review:** **Question:** Compare Provisioned throughput with Guardrail. When would each change your design?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Provisioned throughput: reserves model units/capacity for predictable demand at commitment cost. Guardrail: evaluates input/output policies but is one layer rather than proof of safety. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-BEDROCK-MN-05

- [ ] **Question:** Compare Guardrail with Knowledge Base. When would each change your design?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Guardrail: evaluates input/output policies but is one layer rather than proof of safety. Knowledge Base: managed ingestion/retrieval still needs source authorization, tenancy and freshness. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-BEDROCK-MN-06

- [ ] **Question:** Compare Knowledge Base with Agent. When would each change your design?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Knowledge Base: managed ingestion/retrieval still needs source authorization, tenancy and freshness. Agent: orchestrates models/actions/knowledge with least-privilege tools and human approval. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-BEDROCK-MN-07

- [ ] **Configuration review:** **Question:** Compare Agent with Model evaluation. When would each change your design?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Agent: orchestrates models/actions/knowledge with least-privilege tools and human approval. Model evaluation: datasets/metrics/judges compare candidates but need calibration/versioning. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-BEDROCK-MN-08

- [ ] **Question:** Compare Model evaluation with Cross-Region inference. When would each change your design?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Model evaluation: datasets/metrics/judges compare candidates but need calibration/versioning. Cross-Region inference: improves capacity while changing data path/residency analysis. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-BEDROCK-MN-09

- [ ] **Question:** Compare Cross-Region inference with Token metering. When would each change your design?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Cross-Region inference: improves capacity while changing data path/residency analysis. Token metering: input/output/cache/model/region usage supports budget and chargeback. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-BEDROCK-MN-10

- [ ] **Configuration review:** **Question:** Compare Token metering with Foundation model access. When would each change your design?
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Token metering: input/output/cache/model/region usage supports budget and chargeback. Foundation model access: model/provider/Region/API capability and terms must be approved. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-BEDROCK-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Foundation model access; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock list-foundation-models` plus recent events/changes, then correlate the service-specific SLI. model/provider/Region/API capability and terms must be approved. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-BEDROCK-MP-02

- [ ] **Question:** Production is degraded around Converse/Invoke API; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock-runtime converse --model-id MODEL --messages file://messages.json` plus recent events/changes, then correlate the service-specific SLI. normalized/model APIs differ in streaming, tools and request schema. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-BEDROCK-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Inference profile; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock list-guardrails` plus recent events/changes, then correlate the service-specific SLI. routes/model invocation capacity across supported Regions or application profiles. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-BEDROCK-MP-04

- [ ] **Question:** Production is degraded around Provisioned throughput; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock list-inference-profiles` plus recent events/changes, then correlate the service-specific SLI. reserves model units/capacity for predictable demand at commitment cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-BEDROCK-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Guardrail; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock list-foundation-models` plus recent events/changes, then correlate the service-specific SLI. evaluates input/output policies but is one layer rather than proof of safety. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-BEDROCK-MP-06

- [ ] **Question:** Production is degraded around Knowledge Base; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock-runtime converse --model-id MODEL --messages file://messages.json` plus recent events/changes, then correlate the service-specific SLI. managed ingestion/retrieval still needs source authorization, tenancy and freshness. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-BEDROCK-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Agent; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock list-guardrails` plus recent events/changes, then correlate the service-specific SLI. orchestrates models/actions/knowledge with least-privilege tools and human approval. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-BEDROCK-MP-08

- [ ] **Question:** Production is degraded around Model evaluation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Bedrock — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock list-inference-profiles` plus recent events/changes, then correlate the service-specific SLI. datasets/metrics/judges compare candidates but need calibration/versioning. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-BEDROCK-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cross-Region inference; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock list-foundation-models` plus recent events/changes, then correlate the service-specific SLI. improves capacity while changing data path/residency analysis. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-BEDROCK-MP-10

- [ ] **Question:** Production is degraded around Token metering; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock-runtime converse --model-id MODEL --messages file://messages.json` plus recent events/changes, then correlate the service-specific SLI. input/output/cache/model/region usage supports budget and chargeback. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-BEDROCK-SN-01

- [ ] **Question:** Design a production Amazon Bedrock capability where Foundation model access, Provisioned throughput and Agent are first-class requirements.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model/provider/Region/API capability and terms must be approved. reserves model units/capacity for predictable demand at commitment cost. orchestrates models/actions/knowledge with least-privilege tools and human approval. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-BEDROCK-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Bedrock capability where Converse/Invoke API, Guardrail and Model evaluation are first-class requirements.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: normalized/model APIs differ in streaming, tools and request schema. evaluates input/output policies but is one layer rather than proof of safety. datasets/metrics/judges compare candidates but need calibration/versioning. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-BEDROCK-SN-03

- [ ] **Question:** Design a production Amazon Bedrock capability where Inference profile, Knowledge Base and Cross-Region inference are first-class requirements.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: routes/model invocation capacity across supported Regions or application profiles. managed ingestion/retrieval still needs source authorization, tenancy and freshness. improves capacity while changing data path/residency analysis. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-BEDROCK-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Bedrock capability where Provisioned throughput, Agent and Token metering are first-class requirements.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reserves model units/capacity for predictable demand at commitment cost. orchestrates models/actions/knowledge with least-privilege tools and human approval. input/output/cache/model/region usage supports budget and chargeback. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-BEDROCK-SN-05

- [ ] **Question:** Design a production Amazon Bedrock capability where Guardrail, Model evaluation and Foundation model access are first-class requirements.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: evaluates input/output policies but is one layer rather than proof of safety. datasets/metrics/judges compare candidates but need calibration/versioning. model/provider/Region/API capability and terms must be approved. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-BEDROCK-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Bedrock capability where Knowledge Base, Cross-Region inference and Converse/Invoke API are first-class requirements.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed ingestion/retrieval still needs source authorization, tenancy and freshness. improves capacity while changing data path/residency analysis. normalized/model APIs differ in streaming, tools and request schema. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-BEDROCK-SN-07

- [ ] **Question:** Design a production Amazon Bedrock capability where Agent, Token metering and Inference profile are first-class requirements.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: orchestrates models/actions/knowledge with least-privilege tools and human approval. input/output/cache/model/region usage supports budget and chargeback. routes/model invocation capacity across supported Regions or application profiles. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-BEDROCK-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Bedrock capability where Model evaluation, Foundation model access and Provisioned throughput are first-class requirements.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: datasets/metrics/judges compare candidates but need calibration/versioning. model/provider/Region/API capability and terms must be approved. reserves model units/capacity for predictable demand at commitment cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-BEDROCK-SN-09

- [ ] **Question:** Design a production Amazon Bedrock capability where Cross-Region inference, Converse/Invoke API and Guardrail are first-class requirements.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: improves capacity while changing data path/residency analysis. normalized/model APIs differ in streaming, tools and request schema. evaluates input/output policies but is one layer rather than proof of safety. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-BEDROCK-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Bedrock capability where Token metering, Inference profile and Knowledge Base are first-class requirements.
> **Covered in:** [Amazon Bedrock — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: input/output/cache/model/region usage supports budget and chargeback. routes/model invocation capacity across supported Regions or application profiles. managed ingestion/retrieval still needs source authorization, tenancy and freshness. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-BEDROCK-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Foundation model access. How do you lead it end to end?
> **Covered in:** [Amazon Bedrock — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock list-foundation-models` as one read-only checkpoint, not the whole diagnosis. model/provider/Region/API capability and terms must be approved. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-BEDROCK-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Converse/Invoke API. How do you lead it end to end?
> **Covered in:** [Amazon Bedrock — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock-runtime converse --model-id MODEL --messages file://messages.json` as one read-only checkpoint, not the whole diagnosis. normalized/model APIs differ in streaming, tools and request schema. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-BEDROCK-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Inference profile. How do you lead it end to end?
> **Covered in:** [Amazon Bedrock — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock list-guardrails` as one read-only checkpoint, not the whole diagnosis. routes/model invocation capacity across supported Regions or application profiles. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-BEDROCK-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Provisioned throughput. How do you lead it end to end?
> **Covered in:** [Amazon Bedrock — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock list-inference-profiles` as one read-only checkpoint, not the whole diagnosis. reserves model units/capacity for predictable demand at commitment cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-BEDROCK-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Guardrail. How do you lead it end to end?
> **Covered in:** [Amazon Bedrock — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock list-foundation-models` as one read-only checkpoint, not the whole diagnosis. evaluates input/output policies but is one layer rather than proof of safety. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-BEDROCK-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Knowledge Base. How do you lead it end to end?
> **Covered in:** [Amazon Bedrock — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock-runtime converse --model-id MODEL --messages file://messages.json` as one read-only checkpoint, not the whole diagnosis. managed ingestion/retrieval still needs source authorization, tenancy and freshness. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-BEDROCK-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Agent. How do you lead it end to end?
> **Covered in:** [Amazon Bedrock — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock list-guardrails` as one read-only checkpoint, not the whole diagnosis. orchestrates models/actions/knowledge with least-privilege tools and human approval. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-BEDROCK-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model evaluation. How do you lead it end to end?
> **Covered in:** [Amazon Bedrock — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock list-inference-profiles` as one read-only checkpoint, not the whole diagnosis. datasets/metrics/judges compare candidates but need calibration/versioning. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-BEDROCK-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cross-Region inference. How do you lead it end to end?
> **Covered in:** [Amazon Bedrock — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock list-foundation-models` as one read-only checkpoint, not the whole diagnosis. improves capacity while changing data path/residency analysis. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-BEDROCK-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Token metering. How do you lead it end to end?
> **Covered in:** [Amazon Bedrock — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock-runtime converse --model-id MODEL --messages file://messages.json` as one read-only checkpoint, not the whole diagnosis. input/output/cache/model/region usage supports budget and chargeback. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Ai Platform](../README.md) · [Study note](README.md) · [Next: Amazon SageMaker AI →](../02-sagemaker-ai/README.md)

<!-- reading-navigation:end -->
