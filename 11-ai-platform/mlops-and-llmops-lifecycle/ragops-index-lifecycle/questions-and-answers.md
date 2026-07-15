# RAGOps and index lifecycle — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### RAGOPS-AND-INDEX-LIFECYCLE-JN-01

- [ ] **Question:** What is Source inventory, and why does it matter in RAGOps and index lifecycle?

**Answer:** owner, connector, classification, ACL, residency, update/delete semantics and watermark are explicit. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAGOPS-AND-INDEX-LIFECYCLE-JN-02

- [ ] **Question:** What is Ingestion idempotency, and why does it matter in RAGOps and index lifecycle?

**Answer:** stable source/version IDs and checkpoints prevent duplicate or skipped documents. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAGOPS-AND-INDEX-LIFECYCLE-JN-03

- [ ] **Question:** What is Parser/chunker version, and why does it matter in RAGOps and index lifecycle?

**Answer:** content extraction, tables/images and chunk boundaries change retrieval and require lineage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAGOPS-AND-INDEX-LIFECYCLE-JN-04

- [ ] **Question:** What is Embedding release, and why does it matter in RAGOps and index lifecycle?

**Answer:** model/tokenizer/dimension/normalization and batching are immutable index dependencies. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAGOPS-AND-INDEX-LIFECYCLE-JN-05

- [ ] **Question:** What is Index build, and why does it matter in RAGOps and index lifecycle?

**Answer:** staging index is populated and validated before atomic alias/pointer promotion. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAGOPS-AND-INDEX-LIFECYCLE-JN-06

- [ ] **Question:** What is Authorization, and why does it matter in RAGOps and index lifecycle?

**Answer:** tenant and source ACL filters apply before context is returned; application post-filtering is too late. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAGOPS-AND-INDEX-LIFECYCLE-JN-07

- [ ] **Question:** What is Freshness SLI, and why does it matter in RAGOps and index lifecycle?

**Answer:** source update→ingest→embed→index→query visibility latency is measured by stage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAGOPS-AND-INDEX-LIFECYCLE-JN-08

- [ ] **Code:** **Question:** What does `curl -s VECTOR_DB/health` help you verify for RAGOps and index lifecycle?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: tombstone and hard-delete reconcile chunks, vector/sparse indexes, caches, evaluations and backups under policy.

### RAGOPS-AND-INDEX-LIFECYCLE-JN-09

- [ ] **Code:** **Question:** What does `python ingest.py --source fixtures/docs --dry-run` help you verify for RAGOps and index lifecycle?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: retrieval recall/precision/MRR/nDCG and answer faithfulness/citation/quality are separated by slices.

### RAGOPS-AND-INDEX-LIFECYCLE-JN-10

- [ ] **Code:** **Question:** What does `python build_index.py --manifest corpus-v12.json --target staging-v12` help you verify for RAGOps and index lifecycle?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: retain compatible prior index and query code; alias reversal must not reintroduce deleted/unauthorized content.

## Junior — procedural and command questions

### RAGOPS-AND-INDEX-LIFECYCLE-JP-01

- [ ] **Code:** **Question:** A basic Source inventory check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python ingest.py --source fixtures/docs --dry-run` and capture exact status/reason/request ID. owner, connector, classification, ACL, residency, update/delete semantics and watermark are explicit. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAGOPS-AND-INDEX-LIFECYCLE-JP-02

- [ ] **Question:** A basic Ingestion idempotency check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python build_index.py --manifest corpus-v12.json --target staging-v12` and capture exact status/reason/request ID. stable source/version IDs and checkpoints prevent duplicate or skipped documents. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAGOPS-AND-INDEX-LIFECYCLE-JP-03

- [ ] **Question:** A basic Parser/chunker version check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python evaluate_rag.py --dataset eval/rag-golden.jsonl` and capture exact status/reason/request ID. content extraction, tables/images and chunk boundaries change retrieval and require lineage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAGOPS-AND-INDEX-LIFECYCLE-JP-04

- [ ] **Code:** **Question:** A basic Embedding release check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s VECTOR_DB/health` and capture exact status/reason/request ID. model/tokenizer/dimension/normalization and batching are immutable index dependencies. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAGOPS-AND-INDEX-LIFECYCLE-JP-05

- [ ] **Question:** A basic Index build check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python ingest.py --source fixtures/docs --dry-run` and capture exact status/reason/request ID. staging index is populated and validated before atomic alias/pointer promotion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAGOPS-AND-INDEX-LIFECYCLE-JP-06

- [ ] **Question:** A basic Authorization check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python build_index.py --manifest corpus-v12.json --target staging-v12` and capture exact status/reason/request ID. tenant and source ACL filters apply before context is returned; application post-filtering is too late. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAGOPS-AND-INDEX-LIFECYCLE-JP-07

- [ ] **Code:** **Question:** A basic Freshness SLI check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python evaluate_rag.py --dataset eval/rag-golden.jsonl` and capture exact status/reason/request ID. source update→ingest→embed→index→query visibility latency is measured by stage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAGOPS-AND-INDEX-LIFECYCLE-JP-08

- [ ] **Question:** A basic Deletion check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s VECTOR_DB/health` and capture exact status/reason/request ID. tombstone and hard-delete reconcile chunks, vector/sparse indexes, caches, evaluations and backups under policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAGOPS-AND-INDEX-LIFECYCLE-JP-09

- [ ] **Question:** A basic Evaluation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python ingest.py --source fixtures/docs --dry-run` and capture exact status/reason/request ID. retrieval recall/precision/MRR/nDCG and answer faithfulness/citation/quality are separated by slices. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAGOPS-AND-INDEX-LIFECYCLE-JP-10

- [ ] **Code:** **Question:** A basic Rollback check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python build_index.py --manifest corpus-v12.json --target staging-v12` and capture exact status/reason/request ID. retain compatible prior index and query code; alias reversal must not reintroduce deleted/unauthorized content. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### RAGOPS-AND-INDEX-LIFECYCLE-MN-01

- [ ] **Question:** Compare Source inventory with Ingestion idempotency. When would each change your design?

**Answer:** Source inventory: owner, connector, classification, ACL, residency, update/delete semantics and watermark are explicit. Ingestion idempotency: stable source/version IDs and checkpoints prevent duplicate or skipped documents. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAGOPS-AND-INDEX-LIFECYCLE-MN-02

- [ ] **Question:** Compare Ingestion idempotency with Parser/chunker version. When would each change your design?

**Answer:** Ingestion idempotency: stable source/version IDs and checkpoints prevent duplicate or skipped documents. Parser/chunker version: content extraction, tables/images and chunk boundaries change retrieval and require lineage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAGOPS-AND-INDEX-LIFECYCLE-MN-03

- [ ] **Question:** Compare Parser/chunker version with Embedding release. When would each change your design?

**Answer:** Parser/chunker version: content extraction, tables/images and chunk boundaries change retrieval and require lineage. Embedding release: model/tokenizer/dimension/normalization and batching are immutable index dependencies. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAGOPS-AND-INDEX-LIFECYCLE-MN-04

- [ ] **Configuration review:** **Question:** Compare Embedding release with Index build. When would each change your design?

**Answer:** Embedding release: model/tokenizer/dimension/normalization and batching are immutable index dependencies. Index build: staging index is populated and validated before atomic alias/pointer promotion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAGOPS-AND-INDEX-LIFECYCLE-MN-05

- [ ] **Question:** Compare Index build with Authorization. When would each change your design?

**Answer:** Index build: staging index is populated and validated before atomic alias/pointer promotion. Authorization: tenant and source ACL filters apply before context is returned; application post-filtering is too late. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAGOPS-AND-INDEX-LIFECYCLE-MN-06

- [ ] **Question:** Compare Authorization with Freshness SLI. When would each change your design?

**Answer:** Authorization: tenant and source ACL filters apply before context is returned; application post-filtering is too late. Freshness SLI: source update→ingest→embed→index→query visibility latency is measured by stage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAGOPS-AND-INDEX-LIFECYCLE-MN-07

- [ ] **Configuration review:** **Question:** Compare Freshness SLI with Deletion. When would each change your design?

**Answer:** Freshness SLI: source update→ingest→embed→index→query visibility latency is measured by stage. Deletion: tombstone and hard-delete reconcile chunks, vector/sparse indexes, caches, evaluations and backups under policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAGOPS-AND-INDEX-LIFECYCLE-MN-08

- [ ] **Question:** Compare Deletion with Evaluation. When would each change your design?

**Answer:** Deletion: tombstone and hard-delete reconcile chunks, vector/sparse indexes, caches, evaluations and backups under policy. Evaluation: retrieval recall/precision/MRR/nDCG and answer faithfulness/citation/quality are separated by slices. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAGOPS-AND-INDEX-LIFECYCLE-MN-09

- [ ] **Question:** Compare Evaluation with Rollback. When would each change your design?

**Answer:** Evaluation: retrieval recall/precision/MRR/nDCG and answer faithfulness/citation/quality are separated by slices. Rollback: retain compatible prior index and query code; alias reversal must not reintroduce deleted/unauthorized content. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAGOPS-AND-INDEX-LIFECYCLE-MN-10

- [ ] **Configuration review:** **Question:** Compare Rollback with Source inventory. When would each change your design?

**Answer:** Rollback: retain compatible prior index and query code; alias reversal must not reintroduce deleted/unauthorized content. Source inventory: owner, connector, classification, ACL, residency, update/delete semantics and watermark are explicit. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### RAGOPS-AND-INDEX-LIFECYCLE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Source inventory; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python ingest.py --source fixtures/docs --dry-run` plus recent events/changes, then correlate the service-specific SLI. owner, connector, classification, ACL, residency, update/delete semantics and watermark are explicit. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAGOPS-AND-INDEX-LIFECYCLE-MP-02

- [ ] **Question:** Production is degraded around Ingestion idempotency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python build_index.py --manifest corpus-v12.json --target staging-v12` plus recent events/changes, then correlate the service-specific SLI. stable source/version IDs and checkpoints prevent duplicate or skipped documents. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAGOPS-AND-INDEX-LIFECYCLE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Parser/chunker version; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python evaluate_rag.py --dataset eval/rag-golden.jsonl` plus recent events/changes, then correlate the service-specific SLI. content extraction, tables/images and chunk boundaries change retrieval and require lineage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAGOPS-AND-INDEX-LIFECYCLE-MP-04

- [ ] **Question:** Production is degraded around Embedding release; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s VECTOR_DB/health` plus recent events/changes, then correlate the service-specific SLI. model/tokenizer/dimension/normalization and batching are immutable index dependencies. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAGOPS-AND-INDEX-LIFECYCLE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Index build; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python ingest.py --source fixtures/docs --dry-run` plus recent events/changes, then correlate the service-specific SLI. staging index is populated and validated before atomic alias/pointer promotion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAGOPS-AND-INDEX-LIFECYCLE-MP-06

- [ ] **Question:** Production is degraded around Authorization; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python build_index.py --manifest corpus-v12.json --target staging-v12` plus recent events/changes, then correlate the service-specific SLI. tenant and source ACL filters apply before context is returned; application post-filtering is too late. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAGOPS-AND-INDEX-LIFECYCLE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Freshness SLI; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python evaluate_rag.py --dataset eval/rag-golden.jsonl` plus recent events/changes, then correlate the service-specific SLI. source update→ingest→embed→index→query visibility latency is measured by stage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAGOPS-AND-INDEX-LIFECYCLE-MP-08

- [ ] **Question:** Production is degraded around Deletion; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s VECTOR_DB/health` plus recent events/changes, then correlate the service-specific SLI. tombstone and hard-delete reconcile chunks, vector/sparse indexes, caches, evaluations and backups under policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAGOPS-AND-INDEX-LIFECYCLE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Evaluation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python ingest.py --source fixtures/docs --dry-run` plus recent events/changes, then correlate the service-specific SLI. retrieval recall/precision/MRR/nDCG and answer faithfulness/citation/quality are separated by slices. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAGOPS-AND-INDEX-LIFECYCLE-MP-10

- [ ] **Question:** Production is degraded around Rollback; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python build_index.py --manifest corpus-v12.json --target staging-v12` plus recent events/changes, then correlate the service-specific SLI. retain compatible prior index and query code; alias reversal must not reintroduce deleted/unauthorized content. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### RAGOPS-AND-INDEX-LIFECYCLE-SN-01

- [ ] **Question:** Design a production RAGOps and index lifecycle capability where Source inventory, Embedding release and Freshness SLI are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: owner, connector, classification, ACL, residency, update/delete semantics and watermark are explicit. model/tokenizer/dimension/normalization and batching are immutable index dependencies. source update→ingest→embed→index→query visibility latency is measured by stage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAGOPS-AND-INDEX-LIFECYCLE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production RAGOps and index lifecycle capability where Ingestion idempotency, Index build and Deletion are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stable source/version IDs and checkpoints prevent duplicate or skipped documents. staging index is populated and validated before atomic alias/pointer promotion. tombstone and hard-delete reconcile chunks, vector/sparse indexes, caches, evaluations and backups under policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAGOPS-AND-INDEX-LIFECYCLE-SN-03

- [ ] **Question:** Design a production RAGOps and index lifecycle capability where Parser/chunker version, Authorization and Evaluation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: content extraction, tables/images and chunk boundaries change retrieval and require lineage. tenant and source ACL filters apply before context is returned; application post-filtering is too late. retrieval recall/precision/MRR/nDCG and answer faithfulness/citation/quality are separated by slices. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAGOPS-AND-INDEX-LIFECYCLE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production RAGOps and index lifecycle capability where Embedding release, Freshness SLI and Rollback are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model/tokenizer/dimension/normalization and batching are immutable index dependencies. source update→ingest→embed→index→query visibility latency is measured by stage. retain compatible prior index and query code; alias reversal must not reintroduce deleted/unauthorized content. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAGOPS-AND-INDEX-LIFECYCLE-SN-05

- [ ] **Question:** Design a production RAGOps and index lifecycle capability where Index build, Deletion and Source inventory are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: staging index is populated and validated before atomic alias/pointer promotion. tombstone and hard-delete reconcile chunks, vector/sparse indexes, caches, evaluations and backups under policy. owner, connector, classification, ACL, residency, update/delete semantics and watermark are explicit. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAGOPS-AND-INDEX-LIFECYCLE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production RAGOps and index lifecycle capability where Authorization, Evaluation and Ingestion idempotency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tenant and source ACL filters apply before context is returned; application post-filtering is too late. retrieval recall/precision/MRR/nDCG and answer faithfulness/citation/quality are separated by slices. stable source/version IDs and checkpoints prevent duplicate or skipped documents. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAGOPS-AND-INDEX-LIFECYCLE-SN-07

- [ ] **Question:** Design a production RAGOps and index lifecycle capability where Freshness SLI, Rollback and Parser/chunker version are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: source update→ingest→embed→index→query visibility latency is measured by stage. retain compatible prior index and query code; alias reversal must not reintroduce deleted/unauthorized content. content extraction, tables/images and chunk boundaries change retrieval and require lineage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAGOPS-AND-INDEX-LIFECYCLE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production RAGOps and index lifecycle capability where Deletion, Source inventory and Embedding release are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tombstone and hard-delete reconcile chunks, vector/sparse indexes, caches, evaluations and backups under policy. owner, connector, classification, ACL, residency, update/delete semantics and watermark are explicit. model/tokenizer/dimension/normalization and batching are immutable index dependencies. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAGOPS-AND-INDEX-LIFECYCLE-SN-09

- [ ] **Question:** Design a production RAGOps and index lifecycle capability where Evaluation, Ingestion idempotency and Index build are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retrieval recall/precision/MRR/nDCG and answer faithfulness/citation/quality are separated by slices. stable source/version IDs and checkpoints prevent duplicate or skipped documents. staging index is populated and validated before atomic alias/pointer promotion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAGOPS-AND-INDEX-LIFECYCLE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production RAGOps and index lifecycle capability where Rollback, Parser/chunker version and Authorization are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retain compatible prior index and query code; alias reversal must not reintroduce deleted/unauthorized content. content extraction, tables/images and chunk boundaries change retrieval and require lineage. tenant and source ACL filters apply before context is returned; application post-filtering is too late. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### RAGOPS-AND-INDEX-LIFECYCLE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Source inventory. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python ingest.py --source fixtures/docs --dry-run` as one read-only checkpoint, not the whole diagnosis. owner, connector, classification, ACL, residency, update/delete semantics and watermark are explicit. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAGOPS-AND-INDEX-LIFECYCLE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ingestion idempotency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python build_index.py --manifest corpus-v12.json --target staging-v12` as one read-only checkpoint, not the whole diagnosis. stable source/version IDs and checkpoints prevent duplicate or skipped documents. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAGOPS-AND-INDEX-LIFECYCLE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Parser/chunker version. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python evaluate_rag.py --dataset eval/rag-golden.jsonl` as one read-only checkpoint, not the whole diagnosis. content extraction, tables/images and chunk boundaries change retrieval and require lineage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAGOPS-AND-INDEX-LIFECYCLE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Embedding release. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s VECTOR_DB/health` as one read-only checkpoint, not the whole diagnosis. model/tokenizer/dimension/normalization and batching are immutable index dependencies. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAGOPS-AND-INDEX-LIFECYCLE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Index build. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python ingest.py --source fixtures/docs --dry-run` as one read-only checkpoint, not the whole diagnosis. staging index is populated and validated before atomic alias/pointer promotion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAGOPS-AND-INDEX-LIFECYCLE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authorization. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python build_index.py --manifest corpus-v12.json --target staging-v12` as one read-only checkpoint, not the whole diagnosis. tenant and source ACL filters apply before context is returned; application post-filtering is too late. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAGOPS-AND-INDEX-LIFECYCLE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Freshness SLI. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python evaluate_rag.py --dataset eval/rag-golden.jsonl` as one read-only checkpoint, not the whole diagnosis. source update→ingest→embed→index→query visibility latency is measured by stage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAGOPS-AND-INDEX-LIFECYCLE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deletion. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s VECTOR_DB/health` as one read-only checkpoint, not the whole diagnosis. tombstone and hard-delete reconcile chunks, vector/sparse indexes, caches, evaluations and backups under policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAGOPS-AND-INDEX-LIFECYCLE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Evaluation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python ingest.py --source fixtures/docs --dry-run` as one read-only checkpoint, not the whole diagnosis. retrieval recall/precision/MRR/nDCG and answer faithfulness/citation/quality are separated by slices. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAGOPS-AND-INDEX-LIFECYCLE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rollback. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python build_index.py --manifest corpus-v12.json --target staging-v12` as one read-only checkpoint, not the whole diagnosis. retain compatible prior index and query code; alias reversal must not reintroduce deleted/unauthorized content. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
