# MLOps and LLMOps lifecycle

<!-- child-topic-toc:start -->
## Table of contents and deeper notes

This parent note explains how the child topics work together. Follow each child link for the deeper mechanism, real commands/configuration, hands-on practice, authoritative documentation, and its local interview bank.

- [AgentOps and tool-using system operations](agentops/README.md) — [questions and answers](agentops/questions-and-answers.md)
- [MLOps/LLMOps FinOps and capacity](ai-finops-capacity/README.md) — [questions and answers](ai-finops-capacity/questions-and-answers.md)
- [AI supply chain, signing and provenance](ai-supply-chain/README.md) — [questions and answers](ai-supply-chain/questions-and-answers.md)
- [Data versioning, quality and lineage](data-versioning-quality-lineage/README.md) — [questions and answers](data-versioning-quality-lineage/questions-and-answers.md)
- [ML/LLM deployment and progressive release](deployment-progressive-release/README.md) — [questions and answers](deployment-progressive-release/questions-and-answers.md)
- [Distributed training and checkpoint recovery](distributed-training/README.md) — [questions and answers](distributed-training/questions-and-answers.md)
- [EvalOps: continuous AI evaluation infrastructure](evalops/README.md) — [questions and answers](evalops/questions-and-answers.md)
- [Experiment tracking and comparison](experiment-tracking/README.md) — [questions and answers](experiment-tracking/questions-and-answers.md)
- [Feature stores and training-serving consistency](feature-store-training-serving/README.md) — [questions and answers](feature-store-training-serving/questions-and-answers.md)
- [LLM gateway and ProviderOps](gateway-providerops/README.md) — [questions and answers](gateway-providerops/questions-and-answers.md)
- [AI governance, approval and evidence automation](governance-approval-evidence/README.md) — [questions and answers](governance-approval-evidence/questions-and-answers.md)
- [Hyperparameter tuning and experiment search](hyperparameter-tuning/README.md) — [questions and answers](hyperparameter-tuning/questions-and-answers.md)
- [MLOps/LLMOps platform architecture](lifecycle-platform-architecture/README.md) — [questions and answers](lifecycle-platform-architecture/questions-and-answers.md)
- [LLM fine-tuning, PEFT and adapter operations](llm-finetuning-peft/README.md) — [questions and answers](llm-finetuning-peft/questions-and-answers.md)
- [LLM observability and quality telemetry](llm-observability/README.md) — [questions and answers](llm-observability/questions-and-answers.md)
- [LLM release manifests and compatibility](llm-release-manifest/README.md) — [questions and answers](llm-release-manifest/questions-and-answers.md)
- [Model registry, artifacts and lineage](model-registry-artifact-lineage/README.md) — [questions and answers](model-registry-artifact-lineage/questions-and-answers.md)
- [Model validation and release gates](model-validation-release-gates/README.md) — [questions and answers](model-validation-release-gates/questions-and-answers.md)
- [ML monitoring, drift and data quality](monitoring-drift/README.md) — [questions and answers](monitoring-drift/questions-and-answers.md)
- [ML pipeline orchestration](pipeline-orchestration/README.md) — [questions and answers](pipeline-orchestration/questions-and-answers.md)
- [PromptOps: prompt, template and policy lifecycle](promptops/README.md) — [questions and answers](promptops/questions-and-answers.md)
- [RAGOps and index lifecycle](ragops-index-lifecycle/README.md) — [questions and answers](ragops-index-lifecycle/questions-and-answers.md)
- [Reproducibility and environment capture](reproducibility-environments/README.md) — [questions and answers](reproducibility-environments/questions-and-answers.md)
- [Retraining and feedback loops](retraining-feedback-loops/README.md) — [questions and answers](retraining-feedback-loops/questions-and-answers.md)
- [LLM safety, red teaming and guardrail operations](safety-redteam-guardrails/README.md) — [questions and answers](safety-redteam-guardrails/questions-and-answers.md)
- [Training platform operations](training-platform/README.md) — [questions and answers](training-platform/questions-and-answers.md)
<!-- child-topic-toc:end -->
> [Interview questions and answers](questions-and-answers.md) · [Master curriculum](../../curriculum/master-curriculum.txt) · Official starting point: <https://ml-ops.org/>

## Easy mode: mental model

Integrate every part of MLOps and LLMOps lifecycle into one secure, reliable, observable, supportable and cost-aware production capability.

Learn this topic in layers: name the object or mechanism, trace its lifecycle/data path, configure it safely, observe a healthy and failed state, recover it, and then design it across failure domains and team boundaries.

```mermaid
flowchart LR
  R[requirement or symptom] --> M[MLOps and LLMOps lifecycle mechanism]
  M --> S[state and dependencies]
  S --> O[commands metrics logs traces audit]
  O --> D[decision mitigation or design]
  D --> V[user-facing verification]
```

## Complete curriculum checklist

| # | Topic | What you must understand and demonstrate |
|---:|---|---|
| 1 | **Experiment tracking** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 2 | **Dataset versioning** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 3 | **Prompt versioning** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 4 | **Model versioning** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 5 | **Feature and embedding versioning** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 6 | **Model registry** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 7 | **Artifact registry** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 8 | **Lineage** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 9 | **Reproducibility** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 10 | **Training pipelines** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 11 | **Evaluation pipelines** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 12 | **Deployment pipelines** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 13 | **Approval workflows** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 14 | **Model monitoring** | turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. |
| 15 | **Data drift** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 16 | **Concept drift** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 17 | **Quality drift** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 18 | **Retraining** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 19 | **Rollback** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 20 | **Deprecation** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 21 | **Model retirement** | is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |

## Beginner → mid-level → senior learning path

1. **Beginner:** define every term; identify the relevant file, object, protocol, API, or command; explain one normal use.
2. **Mid-level:** configure it from source control, inspect effective runtime state, diagnose two failure modes, automate a safe change, and explain one trade-off.
3. **Senior:** clarify ambiguous requirements, map trust and failure domains, quantify capacity/SLO/RPO/RTO/cost, compare alternatives, plan migration/rollback, and assign ownership.

## Command and configuration lab

Run read-only checks first in a sandbox. For each command, predict healthy output, one failing result, the next discriminating check, and the safe rollback for any later mutation.

```bash
nvidia-smi
kubectl get pods -A -o wide
curl -s http://MODEL/metrics
python -m pytest -q
```

## Hands-on practice: setup → failure → verification → cleanup

Use a tiny local model or approved sandbox endpoint and a versioned JSONL dataset. Record model/tokenizer/prompt/runtime/hardware and baseline latency, token and quality metrics; change one bounded variable; rerun; compare; then simulate an unavailable route or rejected request and verify safe fallback/denial. Cleanup artifacts, endpoint and cached test data according to their classification and retention policy.

Expected result: you can show the healthy evidence, reproduce a safe failure, explain why each command distinguishes one layer from another, restore the baseline, and prove cleanup. Hard extension: automate the lab from source control, add a test or alert for the injected failure, and write a five-step runbook another engineer can execute.

For code/configuration, be ready to review an intentionally unsafe diff and improve idempotency, secret handling, timeouts, validation, logging, tests, and rollback.

## Senior design checklist

State assumptions for tenants, traffic/work units, latency and availability targets, data classification/residency, recovery, team skills and budget. Draw control/data planes and synchronous/asynchronous dependencies. Cover identity, policy, encryption/key lifecycle, delivery provenance, observability, capacity, unit cost, operational ownership, migration and exit criteria. Name the evidence that would cause you to revise the design.

## Revision and practice

Complete the separate [checkbox interview bank](questions-and-answers.md). Do not memorize wording: speak in the order **definition → mechanism → evidence/configuration → failure/trade-off → production example**. For procedures use **stabilize → scope → inspect → hypothesize → test → mitigate → verify → prevent**.
