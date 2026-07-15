# LLM release manifests and compatibility — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JN-01

- [ ] **Question:** What is Weights digest, and why does it matter in LLM release manifests and compatibility?

**Answer:** base and fine-tuned model byte identity is stronger than a mutable repository revision name. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JN-02

- [ ] **Question:** What is Tokenizer, and why does it matter in LLM release manifests and compatibility?

**Answer:** files, normalization, vocabulary, special tokens and chat template are release-critical. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JN-03

- [ ] **Question:** What is Adapter, and why does it matter in LLM release manifests and compatibility?

**Answer:** base compatibility, target modules, rank/alpha and merge state prevent wrong attachment. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JN-04

- [ ] **Question:** What is Runtime, and why does it matter in LLM release manifests and compatibility?

**Answer:** image digest, server version, engine flags, kernels and quantization affect semantics/performance. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JN-05

- [ ] **Question:** What is Hardware, and why does it matter in LLM release manifests and compatibility?

**Answer:** accelerator/driver/CUDA topology qualification and memory profile bound supported deployment. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JN-06

- [ ] **Question:** What is Prompt/tool schema, and why does it matter in LLM release manifests and compatibility?

**Answer:** template/policy/function contracts and structured-output schema are versioned. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JN-07

- [ ] **Question:** What is RAG index, and why does it matter in LLM release manifests and compatibility?

**Answer:** embedding/chunker/corpus/snapshot/ACL policy and index digest affect every answer. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JN-08

- [ ] **Code:** **Question:** What does `kubectl get deployment MODEL -n inference -o jsonpath='{.spec.template.spec.containers[0].image}'` help you verify for LLM release manifests and compatibility?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: dataset/judge/prompt/rubric/calibration and pass thresholds explain approval.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JN-09

- [ ] **Code:** **Question:** What does `python scripts/validate_release_manifest.py release.yaml` help you verify for LLM release manifests and compatibility?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: owner, risk class, licenses, data residency, approval/exception and expiry travel with release.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JN-10

- [ ] **Code:** **Question:** What does `sha256sum model/* tokenizer/*` help you verify for LLM release manifests and compatibility?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: prior compatible release and capacity, database/index schemas and cache invalidation steps are retained.

## Junior — procedural and command questions

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JP-01

- [ ] **Code:** **Question:** A basic Weights digest check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/validate_release_manifest.py release.yaml` and capture exact status/reason/request ID. base and fine-tuned model byte identity is stronger than a mutable repository revision name. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JP-02

- [ ] **Question:** A basic Tokenizer check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `sha256sum model/* tokenizer/*` and capture exact status/reason/request ID. files, normalization, vocabulary, special tokens and chat template are release-critical. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JP-03

- [ ] **Question:** A basic Adapter check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cosign verify-blob --signature release.sig release.yaml` and capture exact status/reason/request ID. base compatibility, target modules, rank/alpha and merge state prevent wrong attachment. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JP-04

- [ ] **Code:** **Question:** A basic Runtime check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get deployment MODEL -n inference -o jsonpath='{.spec.template.spec.containers[0].image}'` and capture exact status/reason/request ID. image digest, server version, engine flags, kernels and quantization affect semantics/performance. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JP-05

- [ ] **Question:** A basic Hardware check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/validate_release_manifest.py release.yaml` and capture exact status/reason/request ID. accelerator/driver/CUDA topology qualification and memory profile bound supported deployment. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JP-06

- [ ] **Question:** A basic Prompt/tool schema check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `sha256sum model/* tokenizer/*` and capture exact status/reason/request ID. template/policy/function contracts and structured-output schema are versioned. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JP-07

- [ ] **Code:** **Question:** A basic RAG index check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cosign verify-blob --signature release.sig release.yaml` and capture exact status/reason/request ID. embedding/chunker/corpus/snapshot/ACL policy and index digest affect every answer. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JP-08

- [ ] **Question:** A basic Evaluator check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get deployment MODEL -n inference -o jsonpath='{.spec.template.spec.containers[0].image}'` and capture exact status/reason/request ID. dataset/judge/prompt/rubric/calibration and pass thresholds explain approval. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JP-09

- [ ] **Question:** A basic Governance check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/validate_release_manifest.py release.yaml` and capture exact status/reason/request ID. owner, risk class, licenses, data residency, approval/exception and expiry travel with release. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-JP-10

- [ ] **Code:** **Question:** A basic Rollback set check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `sha256sum model/* tokenizer/*` and capture exact status/reason/request ID. prior compatible release and capacity, database/index schemas and cache invalidation steps are retained. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MN-01

- [ ] **Question:** Compare Weights digest with Tokenizer. When would each change your design?

**Answer:** Weights digest: base and fine-tuned model byte identity is stronger than a mutable repository revision name. Tokenizer: files, normalization, vocabulary, special tokens and chat template are release-critical. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MN-02

- [ ] **Question:** Compare Tokenizer with Adapter. When would each change your design?

**Answer:** Tokenizer: files, normalization, vocabulary, special tokens and chat template are release-critical. Adapter: base compatibility, target modules, rank/alpha and merge state prevent wrong attachment. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MN-03

- [ ] **Question:** Compare Adapter with Runtime. When would each change your design?

**Answer:** Adapter: base compatibility, target modules, rank/alpha and merge state prevent wrong attachment. Runtime: image digest, server version, engine flags, kernels and quantization affect semantics/performance. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MN-04

- [ ] **Configuration review:** **Question:** Compare Runtime with Hardware. When would each change your design?

**Answer:** Runtime: image digest, server version, engine flags, kernels and quantization affect semantics/performance. Hardware: accelerator/driver/CUDA topology qualification and memory profile bound supported deployment. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MN-05

- [ ] **Question:** Compare Hardware with Prompt/tool schema. When would each change your design?

**Answer:** Hardware: accelerator/driver/CUDA topology qualification and memory profile bound supported deployment. Prompt/tool schema: template/policy/function contracts and structured-output schema are versioned. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MN-06

- [ ] **Question:** Compare Prompt/tool schema with RAG index. When would each change your design?

**Answer:** Prompt/tool schema: template/policy/function contracts and structured-output schema are versioned. RAG index: embedding/chunker/corpus/snapshot/ACL policy and index digest affect every answer. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MN-07

- [ ] **Configuration review:** **Question:** Compare RAG index with Evaluator. When would each change your design?

**Answer:** RAG index: embedding/chunker/corpus/snapshot/ACL policy and index digest affect every answer. Evaluator: dataset/judge/prompt/rubric/calibration and pass thresholds explain approval. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MN-08

- [ ] **Question:** Compare Evaluator with Governance. When would each change your design?

**Answer:** Evaluator: dataset/judge/prompt/rubric/calibration and pass thresholds explain approval. Governance: owner, risk class, licenses, data residency, approval/exception and expiry travel with release. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MN-09

- [ ] **Question:** Compare Governance with Rollback set. When would each change your design?

**Answer:** Governance: owner, risk class, licenses, data residency, approval/exception and expiry travel with release. Rollback set: prior compatible release and capacity, database/index schemas and cache invalidation steps are retained. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MN-10

- [ ] **Configuration review:** **Question:** Compare Rollback set with Weights digest. When would each change your design?

**Answer:** Rollback set: prior compatible release and capacity, database/index schemas and cache invalidation steps are retained. Weights digest: base and fine-tuned model byte identity is stronger than a mutable repository revision name. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Weights digest; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/validate_release_manifest.py release.yaml` plus recent events/changes, then correlate the service-specific SLI. base and fine-tuned model byte identity is stronger than a mutable repository revision name. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MP-02

- [ ] **Question:** Production is degraded around Tokenizer; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `sha256sum model/* tokenizer/*` plus recent events/changes, then correlate the service-specific SLI. files, normalization, vocabulary, special tokens and chat template are release-critical. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Adapter; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cosign verify-blob --signature release.sig release.yaml` plus recent events/changes, then correlate the service-specific SLI. base compatibility, target modules, rank/alpha and merge state prevent wrong attachment. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MP-04

- [ ] **Question:** Production is degraded around Runtime; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get deployment MODEL -n inference -o jsonpath='{.spec.template.spec.containers[0].image}'` plus recent events/changes, then correlate the service-specific SLI. image digest, server version, engine flags, kernels and quantization affect semantics/performance. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Hardware; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/validate_release_manifest.py release.yaml` plus recent events/changes, then correlate the service-specific SLI. accelerator/driver/CUDA topology qualification and memory profile bound supported deployment. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MP-06

- [ ] **Question:** Production is degraded around Prompt/tool schema; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `sha256sum model/* tokenizer/*` plus recent events/changes, then correlate the service-specific SLI. template/policy/function contracts and structured-output schema are versioned. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around RAG index; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cosign verify-blob --signature release.sig release.yaml` plus recent events/changes, then correlate the service-specific SLI. embedding/chunker/corpus/snapshot/ACL policy and index digest affect every answer. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MP-08

- [ ] **Question:** Production is degraded around Evaluator; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get deployment MODEL -n inference -o jsonpath='{.spec.template.spec.containers[0].image}'` plus recent events/changes, then correlate the service-specific SLI. dataset/judge/prompt/rubric/calibration and pass thresholds explain approval. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Governance; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/validate_release_manifest.py release.yaml` plus recent events/changes, then correlate the service-specific SLI. owner, risk class, licenses, data residency, approval/exception and expiry travel with release. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-MP-10

- [ ] **Question:** Production is degraded around Rollback set; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `sha256sum model/* tokenizer/*` plus recent events/changes, then correlate the service-specific SLI. prior compatible release and capacity, database/index schemas and cache invalidation steps are retained. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SN-01

- [ ] **Question:** Design a production LLM release manifests and compatibility capability where Weights digest, Runtime and RAG index are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: base and fine-tuned model byte identity is stronger than a mutable repository revision name. image digest, server version, engine flags, kernels and quantization affect semantics/performance. embedding/chunker/corpus/snapshot/ACL policy and index digest affect every answer. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production LLM release manifests and compatibility capability where Tokenizer, Hardware and Evaluator are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: files, normalization, vocabulary, special tokens and chat template are release-critical. accelerator/driver/CUDA topology qualification and memory profile bound supported deployment. dataset/judge/prompt/rubric/calibration and pass thresholds explain approval. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SN-03

- [ ] **Question:** Design a production LLM release manifests and compatibility capability where Adapter, Prompt/tool schema and Governance are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: base compatibility, target modules, rank/alpha and merge state prevent wrong attachment. template/policy/function contracts and structured-output schema are versioned. owner, risk class, licenses, data residency, approval/exception and expiry travel with release. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production LLM release manifests and compatibility capability where Runtime, RAG index and Rollback set are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: image digest, server version, engine flags, kernels and quantization affect semantics/performance. embedding/chunker/corpus/snapshot/ACL policy and index digest affect every answer. prior compatible release and capacity, database/index schemas and cache invalidation steps are retained. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SN-05

- [ ] **Question:** Design a production LLM release manifests and compatibility capability where Hardware, Evaluator and Weights digest are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: accelerator/driver/CUDA topology qualification and memory profile bound supported deployment. dataset/judge/prompt/rubric/calibration and pass thresholds explain approval. base and fine-tuned model byte identity is stronger than a mutable repository revision name. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production LLM release manifests and compatibility capability where Prompt/tool schema, Governance and Tokenizer are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: template/policy/function contracts and structured-output schema are versioned. owner, risk class, licenses, data residency, approval/exception and expiry travel with release. files, normalization, vocabulary, special tokens and chat template are release-critical. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SN-07

- [ ] **Question:** Design a production LLM release manifests and compatibility capability where RAG index, Rollback set and Adapter are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: embedding/chunker/corpus/snapshot/ACL policy and index digest affect every answer. prior compatible release and capacity, database/index schemas and cache invalidation steps are retained. base compatibility, target modules, rank/alpha and merge state prevent wrong attachment. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production LLM release manifests and compatibility capability where Evaluator, Weights digest and Runtime are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: dataset/judge/prompt/rubric/calibration and pass thresholds explain approval. base and fine-tuned model byte identity is stronger than a mutable repository revision name. image digest, server version, engine flags, kernels and quantization affect semantics/performance. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SN-09

- [ ] **Question:** Design a production LLM release manifests and compatibility capability where Governance, Tokenizer and Hardware are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: owner, risk class, licenses, data residency, approval/exception and expiry travel with release. files, normalization, vocabulary, special tokens and chat template are release-critical. accelerator/driver/CUDA topology qualification and memory profile bound supported deployment. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production LLM release manifests and compatibility capability where Rollback set, Adapter and Prompt/tool schema are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prior compatible release and capacity, database/index schemas and cache invalidation steps are retained. base compatibility, target modules, rank/alpha and merge state prevent wrong attachment. template/policy/function contracts and structured-output schema are versioned. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Weights digest. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/validate_release_manifest.py release.yaml` as one read-only checkpoint, not the whole diagnosis. base and fine-tuned model byte identity is stronger than a mutable repository revision name. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tokenizer. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `sha256sum model/* tokenizer/*` as one read-only checkpoint, not the whole diagnosis. files, normalization, vocabulary, special tokens and chat template are release-critical. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Adapter. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cosign verify-blob --signature release.sig release.yaml` as one read-only checkpoint, not the whole diagnosis. base compatibility, target modules, rank/alpha and merge state prevent wrong attachment. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Runtime. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get deployment MODEL -n inference -o jsonpath='{.spec.template.spec.containers[0].image}'` as one read-only checkpoint, not the whole diagnosis. image digest, server version, engine flags, kernels and quantization affect semantics/performance. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hardware. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/validate_release_manifest.py release.yaml` as one read-only checkpoint, not the whole diagnosis. accelerator/driver/CUDA topology qualification and memory profile bound supported deployment. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt/tool schema. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `sha256sum model/* tokenizer/*` as one read-only checkpoint, not the whole diagnosis. template/policy/function contracts and structured-output schema are versioned. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RAG index. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cosign verify-blob --signature release.sig release.yaml` as one read-only checkpoint, not the whole diagnosis. embedding/chunker/corpus/snapshot/ACL policy and index digest affect every answer. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Evaluator. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get deployment MODEL -n inference -o jsonpath='{.spec.template.spec.containers[0].image}'` as one read-only checkpoint, not the whole diagnosis. dataset/judge/prompt/rubric/calibration and pass thresholds explain approval. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Governance. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/validate_release_manifest.py release.yaml` as one read-only checkpoint, not the whole diagnosis. owner, risk class, licenses, data residency, approval/exception and expiry travel with release. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-RELEASE-MANIFESTS-AND-COMPATIBILITY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rollback set. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `sha256sum model/* tokenizer/*` as one read-only checkpoint, not the whole diagnosis. prior compatible release and capacity, database/index schemas and cache invalidation steps are retained. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
