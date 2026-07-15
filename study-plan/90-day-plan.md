# 90-day Senior AI Platform Engineer interview plan

> If the interview is sooner, use the 14-day sprint first. Track question progress by changing `- [ ]` to `- [x]`; track labs by committing evidence that contains no credentials or customer data.

## Daily loop (2–4 focused hours)

1. **Learn, 45–60 min:** read one README and redraw its lifecycle/request path from memory.
2. **Practise, 45–90 min:** run the commands or lab in a disposable environment; capture healthy evidence, one controlled failure, recovery and cleanup.
3. **Speak, 30–45 min:** answer five normal and five procedural questions without notes. Use a 2–4 minute timer.
4. **Code/review, 30–60 min:** write or review one shell/Python/Go, Kubernetes, Terraform/Pulumi or CI workflow change.
5. **Recall, 15 min:** write five facts, two trade-offs, two failure modes and one design decision from memory.

## 14-day interview sprint

| Day | Focus | Required practical proof |
|---:|---|---|
| 1 | Role ownership, distributed systems, Linux process/resource model | Diagnose CPU/memory/I/O evidence in a disposable Linux system; deliver a 30/60/90-day ownership answer. |
| 2 | Networking, DNS, HTTP/TLS, proxies and load balancing | Trace DNS→route→TCP→TLS→HTTP using `dig/getent`, `ip`, `ss`, `curl`, `openssl` and `tcpdump`. |
| 3 | Containers and software supply chain | Build/inspect a non-root limited container; explain digest, layers, SBOM/signature and runtime isolation. |
| 4 | Kubernetes architecture, API, workloads and `kubectl` | Deploy, break and recover a workload; trace API/controller/scheduler/kubelet and rollout state. |
| 5 | Kubernetes network, storage, security and autoscaling | Diagnose Service/endpoints/DNS/policy and PVC; review RBAC/Pod Security/HPA/PDB YAML. |
| 6 | GPU Kubernetes | Trace hardware→driver→runtime→plugin/DRA→framework; diagnose one Pending or compatibility scenario. |
| 7 | AWS IAM/VPC/EC2/ELB/S3/EKS | Draw a production request path and troubleshoot IAM/policy, route/SG/NACL, target health and EKS identity. |
| 8 | GCP and multi-cloud | Compare AWS/GCP identity, network, GKE/EKS, Vertex/SageMaker and data-residency/failover contracts. |
| 9 | Terraform and Pulumi | Run format/validate/test/plan or preview; explain state, locking, refactor/import, Outputs, components and policy. |
| 10 | GitHub Actions and CircleCI | Build a PR validation workflow, artifact handoff, environment/approval and OIDC trust; review an unsafe pipeline. |
| 11 | Observability, SRE, incident response and DR | Define an SLO/burn alert, trace one failure, and explain a tested application restore with RPO/RTO. |
| 12 | Model serving, LLM gateway and GPU capacity | Explain queue/prefill/decode/KV, TTFT/goodput, batching/autoscaling, streaming retry and provider fallback. |
| 13 | MLOps/LLMOps, RAG, EvalOps, AgentOps, security/governance/FinOps | Build a release manifest and tiny golden evaluation; explain lineage, ACL retrieval, tool auth and cost/quality gate. |
| 14 | Full Andela simulation | 60–90 minutes: system design, coding/config, code review and incident scenario; record and grade communication. |

## Weeks 1–2: core operational fluency

- Complete Linux, networking, Git and container child notes and at least 120 questions.
- Practise evidence-first diagnosis rather than command memorization.
- Write safe shell with quoting, traps, idempotency, timeouts and secret-safe logs.
- Deliver two timed incidents from the cross-domain bank and one architecture exercise.

Exit proof: given “the service is slow,” produce a layered diagnostic tree, state what each command proves, mitigate reversibly and verify the user path.

## Weeks 3–4: Kubernetes and accelerators

- Complete Kubernetes architecture, workloads, networking, storage, security, autoscaling, packaging and operations.
- Write manifests from memory: Deployment/Service/ConfigMap/Secret reference, probes/resources/security context, NetworkPolicy, HPA and PDB.
- Complete GPU Operator/DRA, sharing, topology, queueing, model distribution, inference autoscaling and GPU failures.
- Rehearse upgrades, API deprecation, etcd/application backup and recovery.

Exit proof: build a small cluster lab, deploy a service, inject config/readiness/DNS/policy/resource failures, diagnose and clean up. Explain the equivalent GPU path even if no local GPU is available.

## Weeks 5–6: AWS, GCP and deployment models

- Complete AWS branches and service leaves in P0 order, then GCP.
- Draw account/project hierarchy, identity/federation, network and private service paths.
- Compare ALB/NLB/GWLB/Global Accelerator; EKS/ECS; S3/EBS/EFS; RDS/Aurora/DynamoDB; Bedrock/SageMaker/EKS AI.
- Design SaaS, customer cloud, on-prem, hybrid and air-gapped installation/update/support contracts.

Exit proof: deliver a 45-minute multi-tenant AI platform design with two alternatives, rough capacity/cost, trust/failure boundaries, migration, rollback and DR.

## Weeks 7–8: IaC, CI/CD and platform security

- Complete Terraform and Pulumi child notes; perform import/refactor without replacement in a sandbox.
- Build GitHub Actions and CircleCI validation/deployment examples using short-lived identity.
- Review untrusted-runner, action/orb pinning, artifact provenance, environment approval and GitOps reconciliation risks.
- Practise policy/test/preview/apply/verify/rollback and drift handling.

Exit proof: review a deliberately unsafe IaC/pipeline diff and identify correctness, destruction, identity, secrets, supply-chain, concurrency, rollback and cost problems with a corrected sample.

## Weeks 9–10: AI serving and MLOps/LLMOps

- Complete model-serving, gateway, RAG and all MLOps/LLMOps child notes.
- Build a small versioned dataset/run/model/prompt/evaluation release and trace its lineage.
- Measure TTFT, inter-token latency, throughput, errors, token work, quality and unit cost.
- Practise model/prompt/index/runtime canary and rollback; calibrate at least one automated evaluation against human labels.

Exit proof: present a release manifest, evaluation report and deployment evidence; explain exactly which change caused a regression and how it rolls back.

## Week 11: security, governance, FinOps and leadership

- Threat-model prompt/RAG/tool/provider/supply-chain paths.
- Implement or review deterministic tool authorization and an expired approval/exception path.
- Explain NIST AI RMF, EU/GDPR operational implications without pretending to give legal advice.
- Calculate cost per successful quality-controlled request and propose a 30% saving with protected SLO/quality thresholds.
- Prepare STAR stories: incident, disagreement, ambiguity, migration, technical debt, mentoring, failure and cost reduction.

## Week 12: simulations and weak-area repair

- Run four practical work simulations: system design, coding/configuration, code review and incident response.
- Use [Andela readiness](andela-readiness.md) for the expected format and scoring rubric.
- Sample unseen checkbox questions; do not reread only familiar notes.
- Re-run failed labs, shorten explanations and make assumptions explicit.
- Prepare environment: editor, terminal, diagram surface, camera/audio/network, timezone and BYOD security.

## Self-scoring rubric (0–2 each)

- Clarifies requirements and states assumptions.
- Explains the mechanism rather than listing products.
- Uses safe concrete commands/config/code and interprets output.
- Covers trust and failure boundaries, SLO/RPO/RTO and capacity/cost.
- Separates mitigation, source repair, verification and prevention.
- Communicates trade-offs, decision and evidence concisely.

Target at least 10/12 before the final week. A low category determines the next lab; question volume alone is not readiness.
