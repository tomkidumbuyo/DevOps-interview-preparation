# Additions from the role and current platform landscape

The supplied curriculum is preserved in full. These are additive study leaves discovered while mapping it to the role and current platform practice.

## Delivery tooling added during handbook development

- CircleCI is a first-class CI/CD topic: version 2.1 configuration, pipelines/workflows/jobs/steps, executors, reusable commands/orbs, dynamic configuration, contexts, OIDC, approvals, serial groups, workspaces, caches, artifacts, test results, CLI operations and runner security.
- GitHub Actions coverage includes the full workflow/action file format, reusable workflows and custom actions, GitHub-hosted/self-hosted runners, event trust boundaries, OIDC and software-supply-chain controls.
- Pulumi coverage includes exact `Pulumi.yaml`, `Pulumi.<stack>.yaml`, program/component, provider/backend/secrets-provider and policy project structures.

## Expanded MLOps and LLMOps operations

- The lifecycle branch now separates experiment tracking, dataset/feature operations, pipeline and training platforms, distributed training, tuning, registries, reproducibility, model validation, progressive releases, drift/retraining, PromptOps, fine-tuning/PEFT, release manifests, RAGOps, EvalOps, LLM observability, ProviderOps, safety/red teaming, AgentOps, AI supply chain, governance evidence and AI FinOps.

## AI inference architecture

- Disaggregated prefill/decode, KV-cache transfer/offload, prefix-aware routing, cache locality, and failure handling.
- Speculative decoding, chunked prefill, continuous batching, admission control by predicted token work, and goodput rather than raw requests/second.
- SGLang, NVIDIA NIM/TensorRT-LLM, and inference gateway/scheduler interoperability as comparison points alongside vLLM, TGI, Triton, KServe, and Ray Serve.
- Multi-LoRA/adapters, model composition, tokenizer/chat-template compatibility, structured-output constraints, and safe remote model code.
- Benchmark methodology: warm/cold runs, arrival distributions, prompt/output length distributions, concurrency, percentile TTFT/inter-token latency, throughput, errors, and quality.

## Kubernetes and accelerator operations

- Kubernetes Dynamic Resource Allocation feature/version states, ResourceClaims/DeviceClasses/ResourceSlices, device health, and migration from extended resources.
- Queueing and gang scheduling with Kueue/Volcano-style concepts, fair sharing, topology-aware scheduling, and preemption limits for accelerators.
- GPU firmware/driver/CUDA/runtime compatibility matrices, node-image qualification, canary node pools, drain/reboot behavior, and XID/ECC quarantine automation.
- NUMA/PCIe/NVLink/NVSwitch/RDMA topology, GPUDirect, NCCL tests, EFA, and topology-aware placement.
- GPU utilization blind spots: time-slicing attribution, SM versus memory-bound workloads, KV-cache pressure, fragmentation, and workload goodput.

## LLM gateway and agent platform

- Model Context Protocol (MCP) and other tool contracts: capability discovery, schema validation, identity propagation, consent, timeouts, idempotency, audit, and revocation.
- Per-request policy context, regional/provider/model allowlists, data-use/retention attributes, residency routing, and cryptographically useful audit records.
- Backpressure and fair queueing by predicted token work; retry budgets and streaming-aware retries; cancellation propagation and client disconnects.
- Evals and policy-as-code at gateway, prompt, model, RAG-index, and tool-release boundaries.
- Agent durable execution, checkpointing, replay, compensation, budget/loop limits, least-privilege delegated credentials, and human approval freshness.

## Governance and operational maturity

- NIST AI RMF/Generative AI Profile as a practical complement to the EU AI Act and GDPR.
- AI bills of materials: base model, adapters, tokenizer, prompts, evaluators, datasets/indexes, runtime, container/SBOM, license, provenance, and approval.
- Evidence retention with privacy controls; prompt/response and trace minimization; deletion propagation into indexes, caches, backups, and evaluation sets.
- Customer deployment compatibility matrices, preflight checks, signed offline bundles, reproducible installs, support bundles, upgrade channels, and end-of-life policy.
- Platform product metrics: time-to-first-safe-deployment, paved-road adoption, deployment success, recovery time, support burden, cost/quality per successful task.

## Conventional DevOps gaps worth retaining

- Ansible/configuration management, CDN and edge caching, database migration safety, package repositories, certificate automation, and service-mesh operations.
- FinOps commitments and capacity reservations, egress/NAT/telemetry costs, unit economics, budget policy, and anomaly response.
- Business continuity beyond infrastructure: provider/model/license deprecation, customer-managed dependencies, support access, staffing and key-person risk.
