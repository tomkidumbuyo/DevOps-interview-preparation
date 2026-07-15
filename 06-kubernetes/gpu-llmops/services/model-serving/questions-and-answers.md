# KServe, vLLM and Triton on Kubernetes — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JN-01

- [ ] **Question:** What is InferenceService, and why does it matter in KServe, vLLM and Triton on Kubernetes?

**Answer:** KServe resource declares predictor/runtime/storage/traffic under deployment mode. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JN-02

- [ ] **Question:** What is ServingRuntime, and why does it matter in KServe, vLLM and Triton on Kubernetes?

**Answer:** reusable supported model format/container/protocol contract. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JN-03

- [ ] **Question:** What is vLLM continuous batching, and why does it matter in KServe, vLLM and Triton on Kubernetes?

**Answer:** dynamically combines active sequences for throughput. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JN-04

- [ ] **Question:** What is PagedAttention/KV cache, and why does it matter in KServe, vLLM and Triton on Kubernetes?

**Answer:** manages noncontiguous KV blocks and capacity/eviction. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JN-05

- [ ] **Question:** What is Triton model repository, and why does it matter in KServe, vLLM and Triton on Kubernetes?

**Answer:** versioned model/config layout controls loading and backend. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JN-06

- [ ] **Question:** What is Dynamic batching, and why does it matter in KServe, vLLM and Triton on Kubernetes?

**Answer:** waits briefly to combine requests under latency/shape limits. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JN-07

- [ ] **Question:** What is Model readiness, and why does it matter in KServe, vLLM and Triton on Kubernetes?

**Answer:** exact weights/tokenizer/config loaded, warmed and able to respond. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JN-08

- [ ] **Code:** **Question:** What does `curl -s http://ENDPOINT/metrics | rg 'queue|token|cache|request'` help you verify for KServe, vLLM and Triton on Kubernetes?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: northbound schema compatibility does not guarantee semantic feature parity.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JN-09

- [ ] **Code:** **Question:** What does `kubectl get inferenceservice,servingruntime -A` help you verify for KServe, vLLM and Triton on Kubernetes?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: verified shared/local artifacts reduce cold start but need version/tenant/disk lifecycle.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe inferenceservice NAME -n NS` help you verify for KServe, vLLM and Triton on Kubernetes?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: route controlled traffic and gate latency/error/quality/cost before promotion.

## Junior — procedural and command questions

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JP-01

- [ ] **Code:** **Question:** A basic InferenceService check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get inferenceservice,servingruntime -A` and capture exact status/reason/request ID. KServe resource declares predictor/runtime/storage/traffic under deployment mode. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JP-02

- [ ] **Question:** A basic ServingRuntime check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe inferenceservice NAME -n NS` and capture exact status/reason/request ID. reusable supported model format/container/protocol contract. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JP-03

- [ ] **Question:** A basic vLLM continuous batching check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n NS POD --all-containers` and capture exact status/reason/request ID. dynamically combines active sequences for throughput. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JP-04

- [ ] **Code:** **Question:** A basic PagedAttention/KV cache check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://ENDPOINT/metrics | rg 'queue|token|cache|request'` and capture exact status/reason/request ID. manages noncontiguous KV blocks and capacity/eviction. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JP-05

- [ ] **Question:** A basic Triton model repository check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get inferenceservice,servingruntime -A` and capture exact status/reason/request ID. versioned model/config layout controls loading and backend. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JP-06

- [ ] **Question:** A basic Dynamic batching check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe inferenceservice NAME -n NS` and capture exact status/reason/request ID. waits briefly to combine requests under latency/shape limits. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JP-07

- [ ] **Code:** **Question:** A basic Model readiness check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n NS POD --all-containers` and capture exact status/reason/request ID. exact weights/tokenizer/config loaded, warmed and able to respond. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JP-08

- [ ] **Question:** A basic OpenAI/V2 protocol check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://ENDPOINT/metrics | rg 'queue|token|cache|request'` and capture exact status/reason/request ID. northbound schema compatibility does not guarantee semantic feature parity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JP-09

- [ ] **Question:** A basic Model cache check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get inferenceservice,servingruntime -A` and capture exact status/reason/request ID. verified shared/local artifacts reduce cold start but need version/tenant/disk lifecycle. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-JP-10

- [ ] **Code:** **Question:** A basic Canary/shadow check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe inferenceservice NAME -n NS` and capture exact status/reason/request ID. route controlled traffic and gate latency/error/quality/cost before promotion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MN-01

- [ ] **Question:** Compare InferenceService with ServingRuntime. When would each change your design?

**Answer:** InferenceService: KServe resource declares predictor/runtime/storage/traffic under deployment mode. ServingRuntime: reusable supported model format/container/protocol contract. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MN-02

- [ ] **Question:** Compare ServingRuntime with vLLM continuous batching. When would each change your design?

**Answer:** ServingRuntime: reusable supported model format/container/protocol contract. vLLM continuous batching: dynamically combines active sequences for throughput. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MN-03

- [ ] **Question:** Compare vLLM continuous batching with PagedAttention/KV cache. When would each change your design?

**Answer:** vLLM continuous batching: dynamically combines active sequences for throughput. PagedAttention/KV cache: manages noncontiguous KV blocks and capacity/eviction. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MN-04

- [ ] **Configuration review:** **Question:** Compare PagedAttention/KV cache with Triton model repository. When would each change your design?

**Answer:** PagedAttention/KV cache: manages noncontiguous KV blocks and capacity/eviction. Triton model repository: versioned model/config layout controls loading and backend. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MN-05

- [ ] **Question:** Compare Triton model repository with Dynamic batching. When would each change your design?

**Answer:** Triton model repository: versioned model/config layout controls loading and backend. Dynamic batching: waits briefly to combine requests under latency/shape limits. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MN-06

- [ ] **Question:** Compare Dynamic batching with Model readiness. When would each change your design?

**Answer:** Dynamic batching: waits briefly to combine requests under latency/shape limits. Model readiness: exact weights/tokenizer/config loaded, warmed and able to respond. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MN-07

- [ ] **Configuration review:** **Question:** Compare Model readiness with OpenAI/V2 protocol. When would each change your design?

**Answer:** Model readiness: exact weights/tokenizer/config loaded, warmed and able to respond. OpenAI/V2 protocol: northbound schema compatibility does not guarantee semantic feature parity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MN-08

- [ ] **Question:** Compare OpenAI/V2 protocol with Model cache. When would each change your design?

**Answer:** OpenAI/V2 protocol: northbound schema compatibility does not guarantee semantic feature parity. Model cache: verified shared/local artifacts reduce cold start but need version/tenant/disk lifecycle. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MN-09

- [ ] **Question:** Compare Model cache with Canary/shadow. When would each change your design?

**Answer:** Model cache: verified shared/local artifacts reduce cold start but need version/tenant/disk lifecycle. Canary/shadow: route controlled traffic and gate latency/error/quality/cost before promotion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MN-10

- [ ] **Configuration review:** **Question:** Compare Canary/shadow with InferenceService. When would each change your design?

**Answer:** Canary/shadow: route controlled traffic and gate latency/error/quality/cost before promotion. InferenceService: KServe resource declares predictor/runtime/storage/traffic under deployment mode. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around InferenceService; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get inferenceservice,servingruntime -A` plus recent events/changes, then correlate the service-specific SLI. KServe resource declares predictor/runtime/storage/traffic under deployment mode. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MP-02

- [ ] **Question:** Production is degraded around ServingRuntime; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe inferenceservice NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. reusable supported model format/container/protocol contract. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around vLLM continuous batching; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n NS POD --all-containers` plus recent events/changes, then correlate the service-specific SLI. dynamically combines active sequences for throughput. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MP-04

- [ ] **Question:** Production is degraded around PagedAttention/KV cache; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://ENDPOINT/metrics | rg 'queue|token|cache|request'` plus recent events/changes, then correlate the service-specific SLI. manages noncontiguous KV blocks and capacity/eviction. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Triton model repository; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get inferenceservice,servingruntime -A` plus recent events/changes, then correlate the service-specific SLI. versioned model/config layout controls loading and backend. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MP-06

- [ ] **Question:** Production is degraded around Dynamic batching; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe inferenceservice NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. waits briefly to combine requests under latency/shape limits. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model readiness; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n NS POD --all-containers` plus recent events/changes, then correlate the service-specific SLI. exact weights/tokenizer/config loaded, warmed and able to respond. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MP-08

- [ ] **Question:** Production is degraded around OpenAI/V2 protocol; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://ENDPOINT/metrics | rg 'queue|token|cache|request'` plus recent events/changes, then correlate the service-specific SLI. northbound schema compatibility does not guarantee semantic feature parity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model cache; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get inferenceservice,servingruntime -A` plus recent events/changes, then correlate the service-specific SLI. verified shared/local artifacts reduce cold start but need version/tenant/disk lifecycle. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-MP-10

- [ ] **Question:** Production is degraded around Canary/shadow; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe inferenceservice NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. route controlled traffic and gate latency/error/quality/cost before promotion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SN-01

- [ ] **Question:** Design a production KServe, vLLM and Triton on Kubernetes capability where InferenceService, PagedAttention/KV cache and Model readiness are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: KServe resource declares predictor/runtime/storage/traffic under deployment mode. manages noncontiguous KV blocks and capacity/eviction. exact weights/tokenizer/config loaded, warmed and able to respond. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production KServe, vLLM and Triton on Kubernetes capability where ServingRuntime, Triton model repository and OpenAI/V2 protocol are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reusable supported model format/container/protocol contract. versioned model/config layout controls loading and backend. northbound schema compatibility does not guarantee semantic feature parity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SN-03

- [ ] **Question:** Design a production KServe, vLLM and Triton on Kubernetes capability where vLLM continuous batching, Dynamic batching and Model cache are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: dynamically combines active sequences for throughput. waits briefly to combine requests under latency/shape limits. verified shared/local artifacts reduce cold start but need version/tenant/disk lifecycle. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production KServe, vLLM and Triton on Kubernetes capability where PagedAttention/KV cache, Model readiness and Canary/shadow are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: manages noncontiguous KV blocks and capacity/eviction. exact weights/tokenizer/config loaded, warmed and able to respond. route controlled traffic and gate latency/error/quality/cost before promotion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SN-05

- [ ] **Question:** Design a production KServe, vLLM and Triton on Kubernetes capability where Triton model repository, OpenAI/V2 protocol and InferenceService are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versioned model/config layout controls loading and backend. northbound schema compatibility does not guarantee semantic feature parity. KServe resource declares predictor/runtime/storage/traffic under deployment mode. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production KServe, vLLM and Triton on Kubernetes capability where Dynamic batching, Model cache and ServingRuntime are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: waits briefly to combine requests under latency/shape limits. verified shared/local artifacts reduce cold start but need version/tenant/disk lifecycle. reusable supported model format/container/protocol contract. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SN-07

- [ ] **Question:** Design a production KServe, vLLM and Triton on Kubernetes capability where Model readiness, Canary/shadow and vLLM continuous batching are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exact weights/tokenizer/config loaded, warmed and able to respond. route controlled traffic and gate latency/error/quality/cost before promotion. dynamically combines active sequences for throughput. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production KServe, vLLM and Triton on Kubernetes capability where OpenAI/V2 protocol, InferenceService and PagedAttention/KV cache are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: northbound schema compatibility does not guarantee semantic feature parity. KServe resource declares predictor/runtime/storage/traffic under deployment mode. manages noncontiguous KV blocks and capacity/eviction. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SN-09

- [ ] **Question:** Design a production KServe, vLLM and Triton on Kubernetes capability where Model cache, ServingRuntime and Triton model repository are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: verified shared/local artifacts reduce cold start but need version/tenant/disk lifecycle. reusable supported model format/container/protocol contract. versioned model/config layout controls loading and backend. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production KServe, vLLM and Triton on Kubernetes capability where Canary/shadow, vLLM continuous batching and Dynamic batching are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: route controlled traffic and gate latency/error/quality/cost before promotion. dynamically combines active sequences for throughput. waits briefly to combine requests under latency/shape limits. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving InferenceService. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get inferenceservice,servingruntime -A` as one read-only checkpoint, not the whole diagnosis. KServe resource declares predictor/runtime/storage/traffic under deployment mode. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ServingRuntime. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe inferenceservice NAME -n NS` as one read-only checkpoint, not the whole diagnosis. reusable supported model format/container/protocol contract. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving vLLM continuous batching. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n NS POD --all-containers` as one read-only checkpoint, not the whole diagnosis. dynamically combines active sequences for throughput. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving PagedAttention/KV cache. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://ENDPOINT/metrics | rg 'queue|token|cache|request'` as one read-only checkpoint, not the whole diagnosis. manages noncontiguous KV blocks and capacity/eviction. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Triton model repository. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get inferenceservice,servingruntime -A` as one read-only checkpoint, not the whole diagnosis. versioned model/config layout controls loading and backend. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dynamic batching. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe inferenceservice NAME -n NS` as one read-only checkpoint, not the whole diagnosis. waits briefly to combine requests under latency/shape limits. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model readiness. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n NS POD --all-containers` as one read-only checkpoint, not the whole diagnosis. exact weights/tokenizer/config loaded, warmed and able to respond. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving OpenAI/V2 protocol. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://ENDPOINT/metrics | rg 'queue|token|cache|request'` as one read-only checkpoint, not the whole diagnosis. northbound schema compatibility does not guarantee semantic feature parity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model cache. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get inferenceservice,servingruntime -A` as one read-only checkpoint, not the whole diagnosis. verified shared/local artifacts reduce cold start but need version/tenant/disk lifecycle. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KSERVE-VLLM-AND-TRITON-ON-KUBERNETES-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Canary/shadow. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe inferenceservice NAME -n NS` as one read-only checkpoint, not the whole diagnosis. route controlled traffic and gate latency/error/quality/cost before promotion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
