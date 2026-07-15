# LLM observability and quality telemetry — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JN-01

- [ ] **Question:** What is End-to-end trace, and why does it matter in LLM observability and quality telemetry?

**Answer:** gateway→retrieval→rerank→model→tool spans share safe request/release/tenant identifiers. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JN-02

- [ ] **Question:** What is TTFT, and why does it matter in LLM observability and quality telemetry?

**Answer:** time to first token separates admission/queue/prefill from ongoing decode latency. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JN-03

- [ ] **Question:** What is Inter-token latency, and why does it matter in LLM observability and quality telemetry?

**Answer:** streaming cadence reveals decode/runtime/network behavior hidden by total duration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JN-04

- [ ] **Question:** What is Token work, and why does it matter in LLM observability and quality telemetry?

**Answer:** input/output/cache/tool/image work supports quota, capacity and cost attribution under tokenizer uncertainty. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JN-05

- [ ] **Question:** What is Goodput, and why does it matter in LLM observability and quality telemetry?

**Answer:** requests/tokens satisfying latency, quality and safety are more meaningful than raw GPU utilization. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JN-06

- [ ] **Question:** What is Quality signal, and why does it matter in LLM observability and quality telemetry?

**Answer:** online deterministic checks, feedback and sampled evaluations connect infrastructure to user outcome. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JN-07

- [ ] **Question:** What is Privacy, and why does it matter in LLM observability and quality telemetry?

**Answer:** prompts/responses/retrieved text/tool arguments default to excluded or redacted with controlled sampling/access/retention. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JN-08

- [ ] **Code:** **Question:** What does `python scripts/trace_release.py --release RELEASE_ID` help you verify for LLM observability and quality telemetry?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: model/release/route/status are bounded metric labels; request/user/document IDs belong in traces/logs.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JN-09

- [ ] **Code:** **Question:** What does `curl -s http://LLM_GATEWAY/metrics | rg 'token|ttft|latency|cost|error'` help you verify for LLM observability and quality telemetry?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: provider charges and allocated accelerator time join tenant/project/release without exposing content.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JN-10

- [ ] **Code:** **Question:** What does `otelcol validate --config otel-collector.yaml` help you verify for LLM observability and quality telemetry?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: collector/exporter backlog, drops, sampling and schema/version changes are monitored.

## Junior — procedural and command questions

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JP-01

- [ ] **Code:** **Question:** A basic End-to-end trace check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://LLM_GATEWAY/metrics | rg 'token|ttft|latency|cost|error'` and capture exact status/reason/request ID. gateway→retrieval→rerank→model→tool spans share safe request/release/tenant identifiers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JP-02

- [ ] **Question:** A basic TTFT check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `otelcol validate --config otel-collector.yaml` and capture exact status/reason/request ID. time to first token separates admission/queue/prefill from ongoing decode latency. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JP-03

- [ ] **Question:** A basic Inter-token latency check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n observability deploy/otel-collector --since=30m` and capture exact status/reason/request ID. streaming cadence reveals decode/runtime/network behavior hidden by total duration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JP-04

- [ ] **Code:** **Question:** A basic Token work check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/trace_release.py --release RELEASE_ID` and capture exact status/reason/request ID. input/output/cache/tool/image work supports quota, capacity and cost attribution under tokenizer uncertainty. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JP-05

- [ ] **Question:** A basic Goodput check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://LLM_GATEWAY/metrics | rg 'token|ttft|latency|cost|error'` and capture exact status/reason/request ID. requests/tokens satisfying latency, quality and safety are more meaningful than raw GPU utilization. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JP-06

- [ ] **Question:** A basic Quality signal check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `otelcol validate --config otel-collector.yaml` and capture exact status/reason/request ID. online deterministic checks, feedback and sampled evaluations connect infrastructure to user outcome. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JP-07

- [ ] **Code:** **Question:** A basic Privacy check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n observability deploy/otel-collector --since=30m` and capture exact status/reason/request ID. prompts/responses/retrieved text/tool arguments default to excluded or redacted with controlled sampling/access/retention. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JP-08

- [ ] **Question:** A basic Cardinality check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/trace_release.py --release RELEASE_ID` and capture exact status/reason/request ID. model/release/route/status are bounded metric labels; request/user/document IDs belong in traces/logs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JP-09

- [ ] **Question:** A basic Cost check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://LLM_GATEWAY/metrics | rg 'token|ttft|latency|cost|error'` and capture exact status/reason/request ID. provider charges and allocated accelerator time join tenant/project/release without exposing content. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-JP-10

- [ ] **Code:** **Question:** A basic Telemetry reliability check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `otelcol validate --config otel-collector.yaml` and capture exact status/reason/request ID. collector/exporter backlog, drops, sampling and schema/version changes are monitored. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MN-01

- [ ] **Question:** Compare End-to-end trace with TTFT. When would each change your design?

**Answer:** End-to-end trace: gateway→retrieval→rerank→model→tool spans share safe request/release/tenant identifiers. TTFT: time to first token separates admission/queue/prefill from ongoing decode latency. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MN-02

- [ ] **Question:** Compare TTFT with Inter-token latency. When would each change your design?

**Answer:** TTFT: time to first token separates admission/queue/prefill from ongoing decode latency. Inter-token latency: streaming cadence reveals decode/runtime/network behavior hidden by total duration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MN-03

- [ ] **Question:** Compare Inter-token latency with Token work. When would each change your design?

**Answer:** Inter-token latency: streaming cadence reveals decode/runtime/network behavior hidden by total duration. Token work: input/output/cache/tool/image work supports quota, capacity and cost attribution under tokenizer uncertainty. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MN-04

- [ ] **Configuration review:** **Question:** Compare Token work with Goodput. When would each change your design?

**Answer:** Token work: input/output/cache/tool/image work supports quota, capacity and cost attribution under tokenizer uncertainty. Goodput: requests/tokens satisfying latency, quality and safety are more meaningful than raw GPU utilization. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MN-05

- [ ] **Question:** Compare Goodput with Quality signal. When would each change your design?

**Answer:** Goodput: requests/tokens satisfying latency, quality and safety are more meaningful than raw GPU utilization. Quality signal: online deterministic checks, feedback and sampled evaluations connect infrastructure to user outcome. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MN-06

- [ ] **Question:** Compare Quality signal with Privacy. When would each change your design?

**Answer:** Quality signal: online deterministic checks, feedback and sampled evaluations connect infrastructure to user outcome. Privacy: prompts/responses/retrieved text/tool arguments default to excluded or redacted with controlled sampling/access/retention. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MN-07

- [ ] **Configuration review:** **Question:** Compare Privacy with Cardinality. When would each change your design?

**Answer:** Privacy: prompts/responses/retrieved text/tool arguments default to excluded or redacted with controlled sampling/access/retention. Cardinality: model/release/route/status are bounded metric labels; request/user/document IDs belong in traces/logs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MN-08

- [ ] **Question:** Compare Cardinality with Cost. When would each change your design?

**Answer:** Cardinality: model/release/route/status are bounded metric labels; request/user/document IDs belong in traces/logs. Cost: provider charges and allocated accelerator time join tenant/project/release without exposing content. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MN-09

- [ ] **Question:** Compare Cost with Telemetry reliability. When would each change your design?

**Answer:** Cost: provider charges and allocated accelerator time join tenant/project/release without exposing content. Telemetry reliability: collector/exporter backlog, drops, sampling and schema/version changes are monitored. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MN-10

- [ ] **Configuration review:** **Question:** Compare Telemetry reliability with End-to-end trace. When would each change your design?

**Answer:** Telemetry reliability: collector/exporter backlog, drops, sampling and schema/version changes are monitored. End-to-end trace: gateway→retrieval→rerank→model→tool spans share safe request/release/tenant identifiers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around End-to-end trace; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://LLM_GATEWAY/metrics | rg 'token|ttft|latency|cost|error'` plus recent events/changes, then correlate the service-specific SLI. gateway→retrieval→rerank→model→tool spans share safe request/release/tenant identifiers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MP-02

- [ ] **Question:** Production is degraded around TTFT; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `otelcol validate --config otel-collector.yaml` plus recent events/changes, then correlate the service-specific SLI. time to first token separates admission/queue/prefill from ongoing decode latency. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Inter-token latency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n observability deploy/otel-collector --since=30m` plus recent events/changes, then correlate the service-specific SLI. streaming cadence reveals decode/runtime/network behavior hidden by total duration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MP-04

- [ ] **Question:** Production is degraded around Token work; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/trace_release.py --release RELEASE_ID` plus recent events/changes, then correlate the service-specific SLI. input/output/cache/tool/image work supports quota, capacity and cost attribution under tokenizer uncertainty. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Goodput; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://LLM_GATEWAY/metrics | rg 'token|ttft|latency|cost|error'` plus recent events/changes, then correlate the service-specific SLI. requests/tokens satisfying latency, quality and safety are more meaningful than raw GPU utilization. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MP-06

- [ ] **Question:** Production is degraded around Quality signal; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `otelcol validate --config otel-collector.yaml` plus recent events/changes, then correlate the service-specific SLI. online deterministic checks, feedback and sampled evaluations connect infrastructure to user outcome. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Privacy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n observability deploy/otel-collector --since=30m` plus recent events/changes, then correlate the service-specific SLI. prompts/responses/retrieved text/tool arguments default to excluded or redacted with controlled sampling/access/retention. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MP-08

- [ ] **Question:** Production is degraded around Cardinality; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/trace_release.py --release RELEASE_ID` plus recent events/changes, then correlate the service-specific SLI. model/release/route/status are bounded metric labels; request/user/document IDs belong in traces/logs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cost; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://LLM_GATEWAY/metrics | rg 'token|ttft|latency|cost|error'` plus recent events/changes, then correlate the service-specific SLI. provider charges and allocated accelerator time join tenant/project/release without exposing content. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-MP-10

- [ ] **Question:** Production is degraded around Telemetry reliability; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `otelcol validate --config otel-collector.yaml` plus recent events/changes, then correlate the service-specific SLI. collector/exporter backlog, drops, sampling and schema/version changes are monitored. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SN-01

- [ ] **Question:** Design a production LLM observability and quality telemetry capability where End-to-end trace, Token work and Privacy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: gateway→retrieval→rerank→model→tool spans share safe request/release/tenant identifiers. input/output/cache/tool/image work supports quota, capacity and cost attribution under tokenizer uncertainty. prompts/responses/retrieved text/tool arguments default to excluded or redacted with controlled sampling/access/retention. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production LLM observability and quality telemetry capability where TTFT, Goodput and Cardinality are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: time to first token separates admission/queue/prefill from ongoing decode latency. requests/tokens satisfying latency, quality and safety are more meaningful than raw GPU utilization. model/release/route/status are bounded metric labels; request/user/document IDs belong in traces/logs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SN-03

- [ ] **Question:** Design a production LLM observability and quality telemetry capability where Inter-token latency, Quality signal and Cost are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: streaming cadence reveals decode/runtime/network behavior hidden by total duration. online deterministic checks, feedback and sampled evaluations connect infrastructure to user outcome. provider charges and allocated accelerator time join tenant/project/release without exposing content. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production LLM observability and quality telemetry capability where Token work, Privacy and Telemetry reliability are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: input/output/cache/tool/image work supports quota, capacity and cost attribution under tokenizer uncertainty. prompts/responses/retrieved text/tool arguments default to excluded or redacted with controlled sampling/access/retention. collector/exporter backlog, drops, sampling and schema/version changes are monitored. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SN-05

- [ ] **Question:** Design a production LLM observability and quality telemetry capability where Goodput, Cardinality and End-to-end trace are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: requests/tokens satisfying latency, quality and safety are more meaningful than raw GPU utilization. model/release/route/status are bounded metric labels; request/user/document IDs belong in traces/logs. gateway→retrieval→rerank→model→tool spans share safe request/release/tenant identifiers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production LLM observability and quality telemetry capability where Quality signal, Cost and TTFT are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: online deterministic checks, feedback and sampled evaluations connect infrastructure to user outcome. provider charges and allocated accelerator time join tenant/project/release without exposing content. time to first token separates admission/queue/prefill from ongoing decode latency. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SN-07

- [ ] **Question:** Design a production LLM observability and quality telemetry capability where Privacy, Telemetry reliability and Inter-token latency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prompts/responses/retrieved text/tool arguments default to excluded or redacted with controlled sampling/access/retention. collector/exporter backlog, drops, sampling and schema/version changes are monitored. streaming cadence reveals decode/runtime/network behavior hidden by total duration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production LLM observability and quality telemetry capability where Cardinality, End-to-end trace and Token work are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model/release/route/status are bounded metric labels; request/user/document IDs belong in traces/logs. gateway→retrieval→rerank→model→tool spans share safe request/release/tenant identifiers. input/output/cache/tool/image work supports quota, capacity and cost attribution under tokenizer uncertainty. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SN-09

- [ ] **Question:** Design a production LLM observability and quality telemetry capability where Cost, TTFT and Goodput are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: provider charges and allocated accelerator time join tenant/project/release without exposing content. time to first token separates admission/queue/prefill from ongoing decode latency. requests/tokens satisfying latency, quality and safety are more meaningful than raw GPU utilization. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production LLM observability and quality telemetry capability where Telemetry reliability, Inter-token latency and Quality signal are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: collector/exporter backlog, drops, sampling and schema/version changes are monitored. streaming cadence reveals decode/runtime/network behavior hidden by total duration. online deterministic checks, feedback and sampled evaluations connect infrastructure to user outcome. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving End-to-end trace. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://LLM_GATEWAY/metrics | rg 'token|ttft|latency|cost|error'` as one read-only checkpoint, not the whole diagnosis. gateway→retrieval→rerank→model→tool spans share safe request/release/tenant identifiers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TTFT. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `otelcol validate --config otel-collector.yaml` as one read-only checkpoint, not the whole diagnosis. time to first token separates admission/queue/prefill from ongoing decode latency. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Inter-token latency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n observability deploy/otel-collector --since=30m` as one read-only checkpoint, not the whole diagnosis. streaming cadence reveals decode/runtime/network behavior hidden by total duration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Token work. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/trace_release.py --release RELEASE_ID` as one read-only checkpoint, not the whole diagnosis. input/output/cache/tool/image work supports quota, capacity and cost attribution under tokenizer uncertainty. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Goodput. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://LLM_GATEWAY/metrics | rg 'token|ttft|latency|cost|error'` as one read-only checkpoint, not the whole diagnosis. requests/tokens satisfying latency, quality and safety are more meaningful than raw GPU utilization. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Quality signal. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `otelcol validate --config otel-collector.yaml` as one read-only checkpoint, not the whole diagnosis. online deterministic checks, feedback and sampled evaluations connect infrastructure to user outcome. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Privacy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n observability deploy/otel-collector --since=30m` as one read-only checkpoint, not the whole diagnosis. prompts/responses/retrieved text/tool arguments default to excluded or redacted with controlled sampling/access/retention. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cardinality. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/trace_release.py --release RELEASE_ID` as one read-only checkpoint, not the whole diagnosis. model/release/route/status are bounded metric labels; request/user/document IDs belong in traces/logs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cost. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://LLM_GATEWAY/metrics | rg 'token|ttft|latency|cost|error'` as one read-only checkpoint, not the whole diagnosis. provider charges and allocated accelerator time join tenant/project/release without exposing content. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-OBSERVABILITY-AND-QUALITY-TELEMETRY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Telemetry reliability. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `otelcol validate --config otel-collector.yaml` as one read-only checkpoint, not the whole diagnosis. collector/exporter backlog, drops, sampling and schema/version changes are monitored. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
