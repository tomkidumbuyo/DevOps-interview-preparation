# Senior AI Platform Engineer (DevOps) Interview Handbook

<!-- child-topic-toc:start -->
## Table of contents and deeper notes

This parent note explains how the child topics work together. Follow each child link for the deeper mechanism, real commands/configuration, hands-on practice, authoritative documentation, and its local interview bank.

- [Interview and role-ownership framework](00-role-ownership/README.md) — [questions and answers](00-role-ownership/questions-and-answers.md)
- [Computer science and distributed-systems foundations](01-foundations/README.md) — [questions and answers](01-foundations/questions-and-answers.md)
- [Linux and operating systems](02-linux/README.md) — [questions and answers](02-linux/questions-and-answers.md)
- [Networking](03-networking/README.md) — [questions and answers](03-networking/questions-and-answers.md)
- [Git and software-delivery fundamentals](04-git-delivery/README.md) — [questions and answers](04-git-delivery/questions-and-answers.md)
- [Container fundamentals](05-containers/README.md) — [questions and answers](05-containers/questions-and-answers.md)
- [Kubernetes core platform](06-kubernetes/README.md) — [questions and answers](06-kubernetes/questions-and-answers.md)
- [AWS interview curriculum tree](07-aws/README.md) — [questions and answers](07-aws/questions-and-answers.md)
- [Google Cloud Platform](08-gcp/README.md) — [questions and answers](08-gcp/questions-and-answers.md)
- [Infrastructure as Code and delivery](09-iac-delivery/README.md) — [questions and answers](09-iac-delivery/questions-and-answers.md)
- [Operations, observability, reliability and security](10-operations/README.md) — [questions and answers](10-operations/questions-and-answers.md)
- [AI/ML platform, LLMOps, security and governance](11-ai-platform/README.md) — [questions and answers](11-ai-platform/questions-and-answers.md)
- [Platform engineering, deployment models, FinOps and coding](12-platform-engineering/README.md) — [questions and answers](12-platform-engineering/questions-and-answers.md)
- [Procedural, architecture and leadership scenarios](scenarios/README.md) — [questions and answers](scenarios/questions-and-answers.md)
<!-- child-topic-toc:end -->
This repository is the study hub for a Senior AI Platform Engineer interview focused on production AI infrastructure: Kubernetes and GPU compute, model serving, an LLM gateway, evaluation and RAG infrastructure, governance, reliability, security, cost control, and deployment across AWS, GCP, SaaS, customer cloud, on-premises, and restricted environments.

The curriculum supplied for this project is preserved without removing any item in [`curriculum/master-curriculum.txt`](curriculum/master-curriculum.txt). This README is the main table of contents. Start with P0 material, practise the scenario bank aloud, then fill gaps using P1 and P2 material.

The root [mega DevOps and AI Platform question bank](questions-and-answers.md) contains 180 answered, checkbox-tracked questions that combine domains; every parent and child topic adds its own 60-question bank.

## How to use this handbook

1. Read a topic's notes before looking at its questions.
2. Answer each question aloud in 2–4 minutes: definition, mechanism, trade-off, failure mode, and a production example.
3. For procedural questions, use the sequence **stabilize → scope → inspect → hypothesize → test → mitigate → verify → prevent**.
4. For senior design questions, clarify requirements first, state assumptions, quantify scale and SLOs, identify failure domains and trust boundaries, compare alternatives, and explain migration/rollback.
5. Track progress in [`curriculum/coverage-matrix.md`](curriculum/coverage-matrix.md) and use [`study-plan/90-day-plan.md`](study-plan/90-day-plan.md).

Difficulty labels:

- **Junior:** accurate fundamentals and safe commands.
- **Mid:** independent implementation, troubleshooting, automation, and production trade-offs.
- **Senior:** ambiguous requirements, architecture, risk ownership, multi-team operation, economics, and failure recovery.

## Master table of contents

### 0. Interview and role ownership — P0

- [`00-role-ownership/README.md`](00-role-ownership/README.md) — role boundaries, platform ownership, 30/60/90 days, operating model, contractor/BYOD readiness, leadership questions.

### Part I — Core systems and DevOps foundations

- [`01-foundations/README.md`](01-foundations/README.md) — computing, concurrency, distributed systems, consistency, resilience, APIs, architecture styles.
- [`02-linux/README.md`](02-linux/README.md) — kernel/boot, filesystems, processes, systemd, memory/CPU/storage/network/security, troubleshooting.
- The Linux README also contains the essential command reference and diagnostic command paths; notes and commands intentionally live together.
- [`03-networking/README.md`](03-networking/README.md) — OSI/TCP-IP, IP/subnetting, routing, TCP/UDP/QUIC, DNS, HTTP/TLS, load balancing, proxies, NAT, packet-path troubleshooting.
- [`04-git-delivery/README.md`](04-git-delivery/README.md) — Git internals, branching, change integration, collaboration, releases, and repository security.

### Part II — Containers and Kubernetes

- [`05-containers/README.md`](05-containers/README.md) — namespaces/cgroups, OCI images, runtimes, networking, storage, registries, and supply-chain/runtime security.
- [`06-kubernetes/README.md`](06-kubernetes/README.md) — control plane, API reconciliation, etcd, workloads, services/networking/storage/security/scheduling, autoscaling, upgrades, DR, troubleshooting.
- [`06-kubernetes/gpu-llmops/README.md`](06-kubernetes/gpu-llmops/README.md) — accelerators, CUDA/NCCL, device plugins and DRA, GPU Operator, MIG/time-slicing, queues, autoscaling, telemetry, model serving and LLMOps.

### Part III — AWS

- [`07-aws/README.md`](07-aws/README.md) — complete AWS interview tree and service-selection map.
- [`07-aws/foundations/README.md`](07-aws/foundations/README.md) — global infrastructure, Organizations, Control Tower, IAM, STS/federation, tagging, quotas, governance.
- [`07-aws/networking/README.md`](07-aws/networking/README.md) — VPC/subnets/routes, SG/NACL, NAT/egress, endpoints, peering/TGW/Cloud WAN, hybrid networking, Route 53, troubleshooting.
- [`07-aws/compute/README.md`](07-aws/compute/README.md) — instance families, lifecycle, AMIs, ENIs, security, purchase/capacity models, Auto Scaling.
- [`07-aws/load-balancing/README.md`](07-aws/load-balancing/README.md) — ALB, NLB, GWLB, Global Accelerator, health and failure diagnosis.
- [`07-aws/storage/services/s3/README.md`](07-aws/storage/services/s3/README.md) — object model, consistency, storage classes, lifecycle, versioning, replication, encryption, authorization, events, performance and recovery.
- [`07-aws/storage/README.md`](07-aws/storage/README.md) — EBS, EFS, FSx, AWS Backup and cross-account/region recovery.
- [`07-aws/containers/README.md`](07-aws/containers/README.md) — ECR, ECS, EKS, identities, networking/storage add-ons, upgrades, Karpenter/Auto Mode and AWS Load Balancer Controller.
- [`07-aws/databases/README.md`](07-aws/databases/README.md) and [`07-aws/messaging-serverless/README.md`](07-aws/messaging-serverless/README.md) — RDS/Aurora/DynamoDB/ElastiCache/OpenSearch, SQS/SNS/EventBridge/Kinesis/MSK, Lambda/API Gateway/Step Functions.
- [`07-aws/security-operations/README.md`](07-aws/security-operations/README.md) — KMS/secrets/ACM/WAF/Shield/detection, CloudWatch/X-Ray/CloudTrail/Config/SSM and incident response.
- [`07-aws/infrastructure-delivery/README.md`](07-aws/infrastructure-delivery/README.md) — CloudFormation/CDK, StackSets/change sets, delivery services, Service Catalog/Proton, drift and rollback.
- [`07-aws/ai-platform/README.md`](07-aws/ai-platform/README.md) — Bedrock, SageMaker AI, EKS inference/training, NVIDIA GPUs, Inferentia/Trainium/Neuron, capacity and cost.

### Part IV — Google Cloud Platform

- [`08-gcp/README.md`](08-gcp/README.md) — resource hierarchy/IAM, networking and load balancing, Compute/GKE/Cloud Run, storage/data/messaging, operations/security/cost.
- [`08-gcp/vertex-ai-and-gcp-ai-platform/README.md`](08-gcp/vertex-ai-and-gcp-ai-platform/README.md) — Vertex AI, GKE AI/ML, GPU/TPU, serving, RAG/vector search, evaluation, pipelines and responsible AI.

### Part V — Infrastructure as Code and delivery

- [`09-iac-delivery/terraform/README.md`](09-iac-delivery/terraform/README.md) — HCL/graph, plan/apply, state, lifecycle, modules, refactoring/import, testing, CI/CD and security.
- [`09-iac-delivery/pulumi/README.md`](09-iac-delivery/pulumi/README.md) — complete project/stack/program/file structure, inputs/outputs, state, components, Automation API, policy, delivery, testing and Terraform comparison/migration.
- [`09-iac-delivery/ci-cd/README.md`](09-iac-delivery/ci-cd/README.md) — CI/CD, GitHub Actions/GitLab/Jenkins/CircleCI, strategies, GitOps, database changes and software-supply-chain security.
- [`09-iac-delivery/ci-cd/github-actions/README.md`](09-iac-delivery/ci-cd/github-actions/README.md) — full workflow YAML anatomy, events, jobs/steps, matrices, services, outputs, artifacts/cache, reusable workflows/actions, runners, OIDC/security, CLI and labs.
- [`09-iac-delivery/ci-cd/circleci/README.md`](09-iac-delivery/ci-cd/circleci/README.md) — full CircleCI 2.1 config structure, executors/commands/jobs/workflows, orbs, dynamic config, contexts/OIDC, workspaces/cache/artifacts, CLI and labs.

### Part VI — Observability, reliability, and platform security

- [`10-operations/observability/README.md`](10-operations/observability/README.md) — metrics/logs/traces/profiles, Prometheus/Grafana/OpenTelemetry, GenAI and GPU telemetry, cardinality/privacy/cost.
- [`10-operations/sre-and-reliability-engineering/README.md`](10-operations/sre-and-reliability-engineering/README.md) — SLIs/SLOs/error budgets, alerting, capacity, incidents/postmortems, DR, chaos/game days.
- [`10-operations/platform-and-cloud-security/README.md`](10-operations/platform-and-cloud-security/README.md) — identity/secrets/network/Kubernetes/supply-chain/vulnerability controls and audit evidence.

### Parts VII–VIII — AI/ML, LLM engineering, security, and governance

- [`11-ai-platform/gpu-compute-architecture/README.md`](11-ai-platform/gpu-compute-architecture/README.md) — ML lifecycle, transformers/LLMs, model artifacts, precision/quantization, memory math and parallelism.
- [`11-ai-platform/model-serving-and-inference-platforms/README.md`](11-ai-platform/model-serving-and-inference-platforms/README.md) — KServe, vLLM, Triton, TGI/Ray Serve, model lifecycle, batching/cache, autoscaling, rollout and failure modes.
- [`11-ai-platform/llm-gateway/README.md`](11-ai-platform/llm-gateway/README.md) — normalized APIs, identity/tenancy, policy/routing/reliability, token limits, caching, observability and cost.
- [`11-ai-platform/rag-engineering/README.md`](11-ai-platform/rag-engineering/README.md) — ingestion/parsing/chunking, embeddings/vector databases, hybrid retrieval/reranking, context, freshness, tenancy, security, operations.
- [`11-ai-platform/ai-evaluation-infrastructure/README.md`](11-ai-platform/ai-evaluation-infrastructure/README.md) and [`11-ai-platform/mlops-and-llmops-lifecycle/README.md`](11-ai-platform/mlops-and-llmops-lifecycle/README.md) — datasets/evaluators, RAG/quality/safety/operational metrics, release gates, lineage, reproducibility, drift and retirement.
- The MLOps/LLMOps lifecycle branch contains 26 deeper practical folders spanning experiment tracking, data/features, orchestration/training, registries, release/monitoring/retraining, PromptOps, fine-tuning/PEFT, RAGOps, EvalOps, ProviderOps, AgentOps, observability, safety, governance, supply chain and FinOps.
- [`11-ai-platform/agents-and-tool-using-ai/README.md`](11-ai-platform/agents-and-tool-using-ai/README.md) — agent/tool architecture, MCP and tool contracts, authorization, sandboxes, human approval, budgets, observability/evaluation.
- [`11-ai-platform/ai-and-llm-security/README.md`](11-ai-platform/ai-and-llm-security/README.md), [`11-ai-platform/ai-governance/README.md`](11-ai-platform/ai-governance/README.md), and [`11-ai-platform/european-ai-and-privacy-regulation/README.md`](11-ai-platform/european-ai-and-privacy-regulation/README.md) — threat modeling, OWASP GenAI risks, red teaming, asset/model/data/prompt governance, NIST AI RMF, EU AI Act and GDPR operations.

### Parts IX–XI — Economics, deployment models, platform engineering, and coding

- [`12-platform-engineering/ai-finops-and-cost-control/README.md`](12-platform-engineering/ai-finops-and-cost-control/README.md) and [`12-platform-engineering/multi-cloud-architecture/README.md`](12-platform-engineering/multi-cloud-architecture/README.md) — inference unit economics, chargeback/budgets and multi-cloud design. The sibling SaaS, customer-cloud, on-prem, hybrid and air-gap folders cover each deployment model separately.
- [`12-platform-engineering/internal-developer-platform-for-ai/README.md`](12-platform-engineering/internal-developer-platform-for-ai/README.md) — users/golden paths, portals/CLIs/APIs/CRDs, reconciliation, configuration, developer experience and platform-product metrics.
- [`12-platform-engineering/python-for-platform-engineering/README.md`](12-platform-engineering/python-for-platform-engineering/README.md), [`12-platform-engineering/go-fundamentals/README.md`](12-platform-engineering/go-fundamentals/README.md), [`12-platform-engineering/shell-scripting/README.md`](12-platform-engineering/shell-scripting/README.md), and [`12-platform-engineering/sql-and-data-querying/README.md`](12-platform-engineering/sql-and-data-querying/README.md) — code, CLI, tests and automation contracts.

### Part XII — Procedural and architecture preparation

- [`scenarios/README.md`](scenarios/README.md) — how to answer procedural questions.
- [`scenarios/120-cross-domain-scenarios.md`](scenarios/120-cross-domain-scenarios.md) — 150 production scenarios with investigation, mitigation, verification, and prevention guidance (the filename is retained from the original 120-scenario plan).
- [`scenarios/architecture-exercises/README.md`](scenarios/architecture-exercises/README.md) — AI platform, LLM gateway, GPU capacity, RAG, evaluation, private/on-prem, multi-region, observability, migration designs.
- [`scenarios/leadership-and-behavioural-questions/README.md`](scenarios/leadership-and-behavioural-questions/README.md) — senior ownership and behavioural questions with STAR/decision-record answer patterns.

### Study governance and sources

- [`curriculum/master-curriculum.txt`](curriculum/master-curriculum.txt) — immutable user-supplied requirements baseline.
- [`curriculum/coverage-matrix.md`](curriculum/coverage-matrix.md) — mapping from all 66 curriculum branches to study notes and question banks.
- [`curriculum/additions-from-role-and-research.md`](curriculum/additions-from-role-and-research.md) — role gaps and fast-moving additions beyond the original tree.
- [`curriculum/question-standard.md`](curriculum/question-standard.md) — minimum counts and answer-quality rubric.
- [`sources/official-sources.md`](sources/official-sources.md) — authoritative, version-sensitive references.
- [`sources/reference-handbook-audit.md`](sources/reference-handbook-audit.md) — what was incorporated from the external DevOps handbook and what it did not cover.
- [`study-plan/90-day-plan.md`](study-plan/90-day-plan.md) — P0-first preparation plan.
- [`study-plan/andela-readiness.md`](study-plan/andela-readiness.md) — official-format-informed system design, coding/configuration, review and incident mock interview.
- [`scripts/validate_content.py`](scripts/validate_content.py) — local link, structure, and question-count checker.

## Interview answer contracts

### Conceptual answer

Use: **what it is → how it works → why/when → trade-off/failure → concrete example**. Avoid a list of product features without explaining the mechanism or decision.

### Procedural answer

Use: **protect people/data → define impact and SLO → preserve evidence → trace the request/resource path → change one variable → mitigate reversibly → verify from the user's perspective → record/prevent**. State commands or metrics you would use and what each possible result means.

### Architecture answer

Begin with requirements: tenants, traffic/tokens, model sizes, GPU types, latency and quality SLOs, regions/residency, RPO/RTO, security/compliance, team skills, and budget. Then cover control/data planes, failure domains, identities/trust boundaries, delivery/rollback, observability, capacity math, cost, and migration.

## Scope note

Cloud products, Kubernetes feature states, serving runtimes, and regulations change. Treat commands and feature availability as version-sensitive, confirm them against the official sources, and say which version/region you assume during an interview. The notes are designed for understanding and rehearsal, not for memorizing vendor marketing claims.
# DevOps-interview-preparation
