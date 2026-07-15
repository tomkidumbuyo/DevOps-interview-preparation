# LLM gateway and RAG on Kubernetes — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JN-01

- [ ] **Question:** What is Gateway identity, and why does it matter in LLM gateway and RAG on Kubernetes?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** authenticates workload/user and derives tenant/project/policy context. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JN-02

- [ ] **Question:** What is Model route, and why does it matter in LLM gateway and RAG on Kubernetes?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** alias selects approved provider/model/region/capability under health and budget. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JN-03

- [ ] **Question:** What is Token quota, and why does it matter in LLM gateway and RAG on Kubernetes?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** rate/concurrency/queued work protects fairness/provider/GPU capacity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JN-04

- [ ] **Question:** What is Streaming retry, and why does it matter in LLM gateway and RAG on Kubernetes?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** after output starts, transparent retry can duplicate content/effect/billing. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JN-05

- [ ] **Question:** What is Ingestion pipeline, and why does it matter in LLM gateway and RAG on Kubernetes?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** parses/chunks/embeds/indexes source documents idempotently with lineage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JN-06

- [ ] **Question:** What is Authorization filter, and why does it matter in LLM gateway and RAG on Kubernetes?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** retrieval applies source ACL/tenant constraints before returning context. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JN-07

- [ ] **Question:** What is Hybrid retrieval/rerank, and why does it matter in LLM gateway and RAG on Kubernetes?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** dense/sparse candidates plus reranker trade recall/latency/cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JN-08

- [ ] **Code:** **Question:** What does `curl -N https://gateway.example/v1/chat/completions -H 'Authorization: Bearer TOKEN' -d @request.json` help you verify for LLM gateway and RAG on Kubernetes?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: retrieved content is untrusted data and cannot grant tool/system authority.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JN-09

- [ ] **Code:** **Question:** What does `kubectl get gateway,httproute,networkpolicy -A` help you verify for LLM gateway and RAG on Kubernetes?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: source changes, right-to-delete, re-embedding and cache/index versions reconcile.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JN-10

- [ ] **Code:** **Question:** What does `kubectl top pod -n ai-platform --containers` help you verify for LLM gateway and RAG on Kubernetes?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: gateway→retrieval→rerank→model→tool spans include safe IDs/tokens/latency/cost/eval.

## Junior — procedural and command questions

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JP-01

- [ ] **Code:** **Question:** A basic Gateway identity check fails. What would you do first using the CLI?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get gateway,httproute,networkpolicy -A` and capture exact status/reason/request ID. authenticates workload/user and derives tenant/project/policy context. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JP-02

- [ ] **Question:** A basic Model route check fails. What would you do first?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -n ai-platform --containers` and capture exact status/reason/request ID. alias selects approved provider/model/region/capability under health and budget. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JP-03

- [ ] **Question:** A basic Token quota check fails. What would you do first?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` and capture exact status/reason/request ID. rate/concurrency/queued work protects fairness/provider/GPU capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JP-04

- [ ] **Code:** **Question:** A basic Streaming retry check fails. What would you do first using the CLI?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -N https://gateway.example/v1/chat/completions -H 'Authorization: Bearer TOKEN' -d @request.json` and capture exact status/reason/request ID. after output starts, transparent retry can duplicate content/effect/billing. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JP-05

- [ ] **Question:** A basic Ingestion pipeline check fails. What would you do first?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get gateway,httproute,networkpolicy -A` and capture exact status/reason/request ID. parses/chunks/embeds/indexes source documents idempotently with lineage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JP-06

- [ ] **Question:** A basic Authorization filter check fails. What would you do first?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -n ai-platform --containers` and capture exact status/reason/request ID. retrieval applies source ACL/tenant constraints before returning context. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JP-07

- [ ] **Code:** **Question:** A basic Hybrid retrieval/rerank check fails. What would you do first using the CLI?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` and capture exact status/reason/request ID. dense/sparse candidates plus reranker trade recall/latency/cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JP-08

- [ ] **Question:** A basic Prompt injection check fails. What would you do first?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -N https://gateway.example/v1/chat/completions -H 'Authorization: Bearer TOKEN' -d @request.json` and capture exact status/reason/request ID. retrieved content is untrusted data and cannot grant tool/system authority. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JP-09

- [ ] **Question:** A basic Freshness/deletion check fails. What would you do first?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get gateway,httproute,networkpolicy -A` and capture exact status/reason/request ID. source changes, right-to-delete, re-embedding and cache/index versions reconcile. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-JP-10

- [ ] **Code:** **Question:** A basic End-to-end trace check fails. What would you do first using the CLI?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -n ai-platform --containers` and capture exact status/reason/request ID. gateway→retrieval→rerank→model→tool spans include safe IDs/tokens/latency/cost/eval. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MN-01

- [ ] **Question:** Compare Gateway identity with Model route. When would each change your design?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Gateway identity: authenticates workload/user and derives tenant/project/policy context. Model route: alias selects approved provider/model/region/capability under health and budget. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MN-02

- [ ] **Question:** Compare Model route with Token quota. When would each change your design?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Model route: alias selects approved provider/model/region/capability under health and budget. Token quota: rate/concurrency/queued work protects fairness/provider/GPU capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MN-03

- [ ] **Question:** Compare Token quota with Streaming retry. When would each change your design?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Token quota: rate/concurrency/queued work protects fairness/provider/GPU capacity. Streaming retry: after output starts, transparent retry can duplicate content/effect/billing. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MN-04

- [ ] **Configuration review:** **Question:** Compare Streaming retry with Ingestion pipeline. When would each change your design?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Streaming retry: after output starts, transparent retry can duplicate content/effect/billing. Ingestion pipeline: parses/chunks/embeds/indexes source documents idempotently with lineage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MN-05

- [ ] **Question:** Compare Ingestion pipeline with Authorization filter. When would each change your design?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Ingestion pipeline: parses/chunks/embeds/indexes source documents idempotently with lineage. Authorization filter: retrieval applies source ACL/tenant constraints before returning context. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MN-06

- [ ] **Question:** Compare Authorization filter with Hybrid retrieval/rerank. When would each change your design?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Authorization filter: retrieval applies source ACL/tenant constraints before returning context. Hybrid retrieval/rerank: dense/sparse candidates plus reranker trade recall/latency/cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MN-07

- [ ] **Configuration review:** **Question:** Compare Hybrid retrieval/rerank with Prompt injection. When would each change your design?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Hybrid retrieval/rerank: dense/sparse candidates plus reranker trade recall/latency/cost. Prompt injection: retrieved content is untrusted data and cannot grant tool/system authority. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MN-08

- [ ] **Question:** Compare Prompt injection with Freshness/deletion. When would each change your design?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Prompt injection: retrieved content is untrusted data and cannot grant tool/system authority. Freshness/deletion: source changes, right-to-delete, re-embedding and cache/index versions reconcile. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MN-09

- [ ] **Question:** Compare Freshness/deletion with End-to-end trace. When would each change your design?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Freshness/deletion: source changes, right-to-delete, re-embedding and cache/index versions reconcile. End-to-end trace: gateway→retrieval→rerank→model→tool spans include safe IDs/tokens/latency/cost/eval. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MN-10

- [ ] **Configuration review:** **Question:** Compare End-to-end trace with Gateway identity. When would each change your design?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** End-to-end trace: gateway→retrieval→rerank→model→tool spans include safe IDs/tokens/latency/cost/eval. Gateway identity: authenticates workload/user and derives tenant/project/policy context. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Gateway identity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get gateway,httproute,networkpolicy -A` plus recent events/changes, then correlate the service-specific SLI. authenticates workload/user and derives tenant/project/policy context. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MP-02

- [ ] **Question:** Production is degraded around Model route; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -n ai-platform --containers` plus recent events/changes, then correlate the service-specific SLI. alias selects approved provider/model/region/capability under health and budget. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Token quota; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` plus recent events/changes, then correlate the service-specific SLI. rate/concurrency/queued work protects fairness/provider/GPU capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MP-04

- [ ] **Question:** Production is degraded around Streaming retry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -N https://gateway.example/v1/chat/completions -H 'Authorization: Bearer TOKEN' -d @request.json` plus recent events/changes, then correlate the service-specific SLI. after output starts, transparent retry can duplicate content/effect/billing. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Ingestion pipeline; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get gateway,httproute,networkpolicy -A` plus recent events/changes, then correlate the service-specific SLI. parses/chunks/embeds/indexes source documents idempotently with lineage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MP-06

- [ ] **Question:** Production is degraded around Authorization filter; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -n ai-platform --containers` plus recent events/changes, then correlate the service-specific SLI. retrieval applies source ACL/tenant constraints before returning context. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Hybrid retrieval/rerank; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` plus recent events/changes, then correlate the service-specific SLI. dense/sparse candidates plus reranker trade recall/latency/cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MP-08

- [ ] **Question:** Production is degraded around Prompt injection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -N https://gateway.example/v1/chat/completions -H 'Authorization: Bearer TOKEN' -d @request.json` plus recent events/changes, then correlate the service-specific SLI. retrieved content is untrusted data and cannot grant tool/system authority. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Freshness/deletion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get gateway,httproute,networkpolicy -A` plus recent events/changes, then correlate the service-specific SLI. source changes, right-to-delete, re-embedding and cache/index versions reconcile. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-MP-10

- [ ] **Question:** Production is degraded around End-to-end trace; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -n ai-platform --containers` plus recent events/changes, then correlate the service-specific SLI. gateway→retrieval→rerank→model→tool spans include safe IDs/tokens/latency/cost/eval. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SN-01

- [ ] **Question:** Design a production LLM gateway and RAG on Kubernetes capability where Gateway identity, Streaming retry and Hybrid retrieval/rerank are first-class requirements.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: authenticates workload/user and derives tenant/project/policy context. after output starts, transparent retry can duplicate content/effect/billing. dense/sparse candidates plus reranker trade recall/latency/cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production LLM gateway and RAG on Kubernetes capability where Model route, Ingestion pipeline and Prompt injection are first-class requirements.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: alias selects approved provider/model/region/capability under health and budget. parses/chunks/embeds/indexes source documents idempotently with lineage. retrieved content is untrusted data and cannot grant tool/system authority. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SN-03

- [ ] **Question:** Design a production LLM gateway and RAG on Kubernetes capability where Token quota, Authorization filter and Freshness/deletion are first-class requirements.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: rate/concurrency/queued work protects fairness/provider/GPU capacity. retrieval applies source ACL/tenant constraints before returning context. source changes, right-to-delete, re-embedding and cache/index versions reconcile. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production LLM gateway and RAG on Kubernetes capability where Streaming retry, Hybrid retrieval/rerank and End-to-end trace are first-class requirements.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: after output starts, transparent retry can duplicate content/effect/billing. dense/sparse candidates plus reranker trade recall/latency/cost. gateway→retrieval→rerank→model→tool spans include safe IDs/tokens/latency/cost/eval. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SN-05

- [ ] **Question:** Design a production LLM gateway and RAG on Kubernetes capability where Ingestion pipeline, Prompt injection and Gateway identity are first-class requirements.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: parses/chunks/embeds/indexes source documents idempotently with lineage. retrieved content is untrusted data and cannot grant tool/system authority. authenticates workload/user and derives tenant/project/policy context. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production LLM gateway and RAG on Kubernetes capability where Authorization filter, Freshness/deletion and Model route are first-class requirements.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retrieval applies source ACL/tenant constraints before returning context. source changes, right-to-delete, re-embedding and cache/index versions reconcile. alias selects approved provider/model/region/capability under health and budget. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SN-07

- [ ] **Question:** Design a production LLM gateway and RAG on Kubernetes capability where Hybrid retrieval/rerank, End-to-end trace and Token quota are first-class requirements.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: dense/sparse candidates plus reranker trade recall/latency/cost. gateway→retrieval→rerank→model→tool spans include safe IDs/tokens/latency/cost/eval. rate/concurrency/queued work protects fairness/provider/GPU capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production LLM gateway and RAG on Kubernetes capability where Prompt injection, Gateway identity and Streaming retry are first-class requirements.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retrieved content is untrusted data and cannot grant tool/system authority. authenticates workload/user and derives tenant/project/policy context. after output starts, transparent retry can duplicate content/effect/billing. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SN-09

- [ ] **Question:** Design a production LLM gateway and RAG on Kubernetes capability where Freshness/deletion, Model route and Ingestion pipeline are first-class requirements.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: source changes, right-to-delete, re-embedding and cache/index versions reconcile. alias selects approved provider/model/region/capability under health and budget. parses/chunks/embeds/indexes source documents idempotently with lineage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production LLM gateway and RAG on Kubernetes capability where End-to-end trace, Token quota and Authorization filter are first-class requirements.
> **Covered in:** [LLM gateway and RAG on Kubernetes — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: gateway→retrieval→rerank→model→tool spans include safe IDs/tokens/latency/cost/eval. rate/concurrency/queued work protects fairness/provider/GPU capacity. retrieval applies source ACL/tenant constraints before returning context. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Gateway identity. How do you lead it end to end?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get gateway,httproute,networkpolicy -A` as one read-only checkpoint, not the whole diagnosis. authenticates workload/user and derives tenant/project/policy context. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model route. How do you lead it end to end?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -n ai-platform --containers` as one read-only checkpoint, not the whole diagnosis. alias selects approved provider/model/region/capability under health and budget. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Token quota. How do you lead it end to end?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` as one read-only checkpoint, not the whole diagnosis. rate/concurrency/queued work protects fairness/provider/GPU capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Streaming retry. How do you lead it end to end?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -N https://gateway.example/v1/chat/completions -H 'Authorization: Bearer TOKEN' -d @request.json` as one read-only checkpoint, not the whole diagnosis. after output starts, transparent retry can duplicate content/effect/billing. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ingestion pipeline. How do you lead it end to end?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get gateway,httproute,networkpolicy -A` as one read-only checkpoint, not the whole diagnosis. parses/chunks/embeds/indexes source documents idempotently with lineage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authorization filter. How do you lead it end to end?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -n ai-platform --containers` as one read-only checkpoint, not the whole diagnosis. retrieval applies source ACL/tenant constraints before returning context. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hybrid retrieval/rerank. How do you lead it end to end?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n ai-platform deploy/llm-gateway --since=30m` as one read-only checkpoint, not the whole diagnosis. dense/sparse candidates plus reranker trade recall/latency/cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt injection. How do you lead it end to end?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -N https://gateway.example/v1/chat/completions -H 'Authorization: Bearer TOKEN' -d @request.json` as one read-only checkpoint, not the whole diagnosis. retrieved content is untrusted data and cannot grant tool/system authority. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Freshness/deletion. How do you lead it end to end?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get gateway,httproute,networkpolicy -A` as one read-only checkpoint, not the whole diagnosis. source changes, right-to-delete, re-embedding and cache/index versions reconcile. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-GATEWAY-AND-RAG-ON-KUBERNETES-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving End-to-end trace. How do you lead it end to end?
> **Covered in:** [LLM gateway and RAG on Kubernetes — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -n ai-platform --containers` as one read-only checkpoint, not the whole diagnosis. gateway→retrieval→rerank→model→tool spans include safe IDs/tokens/latency/cost/eval. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: LLMOps release and evaluation on Kubernetes](../05-llmops-release-evaluation/README.md) · [Study note](README.md) · [Next: AWS interview curriculum tree →](../../../07-aws/README.md)

<!-- reading-navigation:end -->
