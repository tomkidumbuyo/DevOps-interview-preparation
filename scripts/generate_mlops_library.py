#!/usr/bin/env python3
"""Generate deep MLOps and LLMOps leaves with practical notes and Q&A."""

from pathlib import Path

from generate_leaf_library import C, Leaf, notes, qna, write


ROOT = Path(__file__).resolve().parents[1]
AREA = "11-ai-platform"
BRANCH = "mlops-and-llmops-lifecycle"


LEAVES = [
    Leaf(AREA, BRANCH, "lifecycle-platform-architecture", "MLOps/LLMOps platform architecture", "Design the complete path from governed data and experiments to reproducible releases, serving, monitoring, feedback and retirement.", C(
        "Lifecycle state machine — idea, experiment, candidate, validated, approved, deployed, monitored, deprecated and retired need explicit transitions",
        "Control plane — metadata, orchestration, policy, registry, approval and reconciliation coordinate work without carrying every inference payload",
        "Data plane — training, batch, retrieval and serving compute move protected data and model work under tenant boundaries",
        "Release unit — data/code/config/model/runtime/evaluator/policy identity must travel together instead of calling a weights file the release",
        "Metadata spine — stable run, dataset, model, release, deployment and request identifiers join otherwise separate systems",
        "Environment promotion — promote immutable evidence/artifacts while configuration and credentials remain target-specific",
        "Human decision — risk-based approvals and exceptions retain actor, evidence, reason, expiry and rollback authority",
        "Reconciliation — controllers compare desired release with observed deployment/index/evaluation state and retry idempotently",
        "Multi-tenancy — identity, quota, compute, metadata, artifacts, networks and cost allocation require explicit isolation",
        "Exit and retirement — revoke endpoints/credentials, preserve required evidence, delete protected data/artifacts and update inventories",
    ), ("mlflow experiments search", "kubectl get workflows,pipelines,trainingjobs,inferenceservices -A", "git log --graph --oneline --all", "curl -s http://metadata-api/health"), "https://ml-ops.org/"),

    Leaf(AREA, BRANCH, "data-versioning-quality-lineage", "Data versioning, quality and lineage", "Make training/evaluation data reproducible, authorized, testable and deletable across snapshots and transformations.", C(
        "Logical dataset version — immutable manifest identifies source snapshot/partitions/files and schema rather than relying on a mutable path",
        "Content digest — hashes prove byte identity but require canonical manifests and cannot prove authorization or semantic quality",
        "Schema contract — names/types/nullability/ranges/keys and evolution compatibility fail early before expensive training",
        "Statistical validation — distribution, missingness, duplicates, label balance and leakage tests compare against owned baselines",
        "Point-in-time correctness — feature joins must use only information available at prediction time to prevent future leakage",
        "Lineage graph — source→transform code/config→dataset→run→model→release supports impact and deletion analysis",
        "Sensitive data — classification, purpose, consent, residency, minimization and access policy follow derived datasets",
        "Deletion propagation — source deletion must reconcile caches, snapshots, embeddings, indexes and retained models under policy",
        "Data drift — changed production input is a signal for investigation/evaluation, not automatic proof that retraining helps",
        "Reproducible split — versioned entity/time-aware train/validation/test assignment avoids overlap and evaluation contamination",
    ), ("dvc status; dvc dag; dvc repro", "dvc data status --json", "great_expectations checkpoint run CHECKPOINT", "python scripts/verify_dataset_manifest.py data/manifest.json"), "https://dvc.org/doc"),

    Leaf(AREA, BRANCH, "feature-store-training-serving", "Feature stores and training-serving consistency", "Operate reusable offline/online features without leakage, stale values or mismatched transformations.", C(
        "Feature definition — owner, entity key, schema, source, transformation, freshness and documentation form a versioned contract",
        "Offline store — historical values support point-in-time training datasets and batch retrieval",
        "Online store — low-latency current values trade history and consistency for serving needs",
        "Registry — versioned metadata connects feature views, entities, sources and ownership but is not necessarily the data store",
        "Materialization — loads computed feature values into online storage with retry, watermark and freshness evidence",
        "Point-in-time join — retrieves each entity's latest valid feature before the event timestamp to prevent leakage",
        "Training-serving skew — code/schema/default/freshness differences between training and inference change behavior",
        "Freshness SLI — event/source/materialization/serve ages distinguish pipeline delay from missing values",
        "Access control — sensitive feature values need entity/tenant authorization and purpose-aware audit",
        "Backfill — historical recomputation needs immutable transformation versions, capacity control and comparison before promotion",
    ), ("feast apply", "feast feature-views list", "feast materialize-incremental $(date -u +%Y-%m-%dT%H:%M:%S)", "feast get-historical-features --help"), "https://docs.feast.dev/"),

    Leaf(AREA, BRANCH, "experiment-tracking", "Experiment tracking and comparison", "Record enough immutable context and evidence to compare runs, reproduce candidates and avoid selecting on noisy metrics.", C(
        "Experiment — groups runs around one owned objective while avoiding an endless unstructured namespace",
        "Run — one execution records code revision, parameters, environment, data identity, metrics, artifacts, status and actor",
        "Parameter — intended input/configuration is logged before execution and is distinct from observed metric",
        "Metric — value plus step/time/dataset/slice semantics prevents misleading comparison",
        "Artifact — model/checkpoint/plot/log/evaluation output needs digest, media type, size and storage policy",
        "Nested runs — organize trials/folds/stages without losing independent failure/evidence",
        "Tags — owner, purpose, tenant/data class, hardware and ticket improve search/governance without encoding secrets",
        "Comparison — confidence intervals, repeated seeds and slice results matter beyond the best scalar score",
        "Tracking server — authentication, artifact credentials, database availability, backup and tenancy are production concerns",
        "Candidate selection — promotion creates a reviewed lineage record rather than treating a dashboard click as deployment",
    ), ("mlflow experiments search", "mlflow runs list --experiment-id EXPERIMENT_ID", "mlflow artifacts list --run-id RUN_ID", "mlflow server --host 127.0.0.1 --port 5000"), "https://mlflow.org/docs/latest/ml/tracking/"),

    Leaf(AREA, BRANCH, "pipeline-orchestration", "ML pipeline orchestration", "Build typed, cache-aware, retry-safe DAGs for data, training, evaluation, registration and release.", C(
        "Component contract — container/code, typed parameters, artifact inputs/outputs, resources and retry behavior are versioned",
        "DAG — data/control dependencies define concurrency and critical path; hidden external state breaks reproducibility",
        "Artifact passing — object references/digests scale better than large values and preserve lineage",
        "Caching — cache key includes all semantic inputs and environment; unsafe caching can promote stale artifacts",
        "Retry — only transient idempotent stages retry automatically; remote side effects need operation keys/reconciliation",
        "Conditional gate — evaluation/policy decision consumes explicit evidence and records why a branch executed",
        "Backfill — bounded partition ranges, concurrency and checkpoints prevent normal workloads from being overwhelmed",
        "Secrets/identity — each component receives short-lived least-privileged identity instead of pipeline-wide static keys",
        "Observability — pipeline/run/task/artifact IDs correlate status, logs, resource use, cost and downstream release",
        "Compiler/version skew — pipeline SDK, compiled spec, orchestrator and component images require compatibility testing",
    ), ("kfp dsl compile --py pipeline.py --output pipeline.yaml", "argo lint workflow.yaml", "kubectl get workflows -A", "kubectl describe workflow RUN -n NS"), "https://www.kubeflow.org/docs/components/pipelines/"),

    Leaf(AREA, BRANCH, "training-platform", "Training platform operations", "Schedule reproducible CPU/GPU training jobs with secure data access, checkpoints, quotas, observability and cleanup.", C(
        "Training job spec — image/digest, command, data, config, resources, topology, identity, timeout and outputs are immutable inputs",
        "Workspace — ephemeral code/scratch is separated from durable datasets/checkpoints/artifacts",
        "Queue/admission — cohort quota, priority, fairness and flavor/topology assignment control scarce accelerators",
        "Node compatibility — GPU/driver/runtime/framework/network/storage versions are qualified together",
        "Checkpoint — atomic versioned state includes model/optimizer/scheduler/RNG/progress and is tested for resume",
        "Spot/preemption — checkpoint interval and restart overhead determine whether discounted capacity saves money",
        "Data loading — sharding, prefetch, cache and worker counts can bottleneck GPUs or overload shared storage",
        "Isolation — untrusted training code, dataset credentials, host devices and outbound network form a high-risk boundary",
        "Training telemetry — loss/quality plus step time, samples/tokens per second, GPU, network, I/O and cost reveal goodput",
        "Cleanup — successful/failed/canceled jobs reconcile pods, disks, IPs, checkpoints, logs and retained evidence",
    ), ("kubectl get trainingjobs,jobs,pods -A -o wide", "kubectl describe pod POD -n NS", "kubectl logs POD -n NS --all-containers --since=30m", "nvidia-smi dmon -s pucvmet"), "https://www.kubeflow.org/docs/components/trainer/"),

    Leaf(AREA, BRANCH, "distributed-training", "Distributed training and checkpoint recovery", "Operate DDP/FSDP/tensor/pipeline parallel training across failure-prone GPU networks and storage.", C(
        "Data parallel — replicas process different batches and synchronize gradients; global batch and optimizer behavior change with world size",
        "DDP — one process per GPU and collective gradient reduction require rank/world/rendezvous correctness",
        "FSDP/ZeRO — shard parameters, gradients and optimizer state to trade communication/complexity for memory scale",
        "Tensor parallel — partitions matrix operations within a layer and benefits from high-bandwidth low-latency topology",
        "Pipeline parallel — partitions layers into stages with microbatches, bubbles and failure coordination",
        "NCCL collectives — ring/tree algorithms depend on rank, interface, RDMA/EFA, topology and version compatibility",
        "Elasticity — worker loss/restart changes membership only when algorithm/checkpoint semantics support it",
        "Distributed checkpoint — sharded state needs a committed manifest and compatible reshard/load procedure",
        "Straggler — one slow GPU/network/data worker holds synchronous progress and can hide behind average utilization",
        "Reproducibility — seeds alone do not eliminate nondeterministic kernels, asynchronous order or topology differences",
    ), ("torchrun --standalone --nproc-per-node=2 train.py --smoke-test", "nvidia-smi topo -m", "NCCL_DEBUG=INFO torchrun --nproc-per-node=2 diagnose.py", "kubectl logs -n NS -l job-name=TRAINING_JOB --prefix"), "https://docs.pytorch.org/tutorials/distributed.html"),

    Leaf(AREA, BRANCH, "hyperparameter-tuning", "Hyperparameter tuning and experiment search", "Run bounded, reproducible searches without leakage, runaway spend or selecting noise.", C(
        "Search space — type/range/scale/conditional relationships encode valid candidate configurations",
        "Random/grid/Bayesian — exploration strategy trades coverage, parallelism and sample efficiency",
        "Objective — metric/dataset/slice/direction/aggregation must represent the production goal",
        "Multi-objective — quality, latency, memory and cost create a Pareto frontier rather than one magic scalar",
        "Early stopping — prunes poor trials only when partial metrics are comparable and not systematically biased",
        "Trial isolation — data split, seed, resources and artifact paths cannot collide across parallel trials",
        "Budget — maximum trials/time/GPU-hours and concurrency prevent search from starving production",
        "Scheduler — ASHA/HyperBand-style resource allocation needs fair checkpoints and monotonic resource semantics",
        "Selection bias — repeated tuning against one validation set overfits the evaluation process",
        "Promotion — rerun finalist with locked config/seeds and independent evaluation before registry approval",
    ), ("kubectl get experiments,trials -A", "kubectl describe experiment NAME -n NS", "python tune.py --smoke-test --max-trials 4", "mlflow runs list --experiment-id EXPERIMENT_ID"), "https://www.kubeflow.org/docs/components/katib/"),

    Leaf(AREA, BRANCH, "model-registry-artifact-lineage", "Model registry, artifacts and lineage", "Bind immutable model bytes to formats, dependencies, evidence, ownership, approvals and deployments.", C(
        "Registered model — logical product/capability groups versions without conflating mutable alias with byte identity",
        "Model version — immutable digest plus source run/data/code/config defines one candidate",
        "Alias — Champion/Challenger/production is a mutable pointer changed through authorized auditable promotion",
        "Artifact format — framework-native, safetensors, ONNX or MLflow flavor determines loader/runtime compatibility and attack surface",
        "Signature/schema — input/output names/types/shapes and preprocessing contract prevent silent integration mismatch",
        "Lineage — dataset/run/checkpoint/evaluation/license/approval links support reproduction and impact analysis",
        "Model card — intended use, limitations, training/evaluation data summary and risk evidence inform consumers",
        "Storage — encryption, immutable retention, replication, malware/unsafe-deserialization controls and restore tests protect artifacts",
        "Access — separate discover/download/promote/delete privileges and audit sensitive model exfiltration",
        "Deployment binding — deployed endpoint records exact model/runtime/prompt/index/policy revision rather than only an alias",
    ), ("mlflow models search -f 'name = MODEL_NAME'", "mlflow artifacts download --run-id RUN_ID --artifact-path model", "sha256sum MODEL_ARTIFACT", "oras manifest fetch REGISTRY/REPOSITORY@sha256:DIGEST"), "https://www.kubeflow.org/docs/components/hub/overview/"),

    Leaf(AREA, BRANCH, "reproducibility-environments", "Reproducibility and environment capture", "Reconstruct data, code, dependencies, hardware and configuration well enough to explain or rerun a release.", C(
        "Code revision — clean commit plus reviewed patch/submodule identity is stronger than an uncommitted notebook snapshot",
        "Dependency lock — resolved package names/versions/hashes and index source prevent floating environments",
        "Container digest — captures userspace bytes but not host kernel, driver, devices, external services or mutable downloads",
        "Dataset manifest — immutable snapshot/transform/split identity is required in addition to a storage URI",
        "Randomness — seeds and RNG states across libraries/workers are recorded while nondeterminism is measured",
        "Hardware/software fingerprint — accelerator, driver, CUDA/ROCm, library and topology can change numerics/performance",
        "Configuration — effective validated config is stored after defaults/overrides without secrets",
        "External dependency — foundation APIs, base models, feature services and remote code need version/contract evidence",
        "Reproduction tolerance — bitwise, numerical or metric-range criteria depend on workload and kernel behavior",
        "Hermetic rebuild — isolated build with pinned sources proves more than retaining an old mutable worker",
    ), ("git status --short; git rev-parse HEAD", "python -m pip freeze; python -m pip check", "docker image inspect IMAGE --format '{{json .RepoDigests}}'", "nvidia-smi --query-gpu=name,driver_version --format=csv"), "https://reproducible-builds.org/docs/"),

    Leaf(AREA, BRANCH, "model-validation-release-gates", "Model validation and release gates", "Combine schema, quality, safety, robustness, performance, security and approval evidence into an auditable decision.", C(
        "Candidate manifest — exact release identity prevents evaluation result being attached to different bytes/config",
        "Baseline — compare with current champion and explicit acceptance bands instead of an isolated candidate score",
        "Slice tests — tenant/language/region/demographic/edge/adversarial slices reveal regressions hidden by averages",
        "Statistical test — uncertainty, sample size, multiple comparisons and practical effect size bound decisions",
        "Safety evaluation — harmful content, privacy leakage, jailbreak and tool behavior require task-specific tests",
        "Performance qualification — latency/throughput/memory under target hardware and workload distribution is part of validation",
        "Security scan — dependencies, unsafe artifact formats, signatures, licenses and model-source trust are checked",
        "Policy decision — machine-readable pass/fail/warn with evidence links still has risk owner and exception process",
        "Approval — actor, reason, evidence set, target scope, time/expiry and rollback authority are recorded",
        "Promotion race — gate result must bind exact commit/artifact and expire if dependencies or target policy change",
    ), ("python -m pytest tests/model_validation -q", "python -m evals.run --manifest release.yaml --dataset golden.jsonl", "cosign verify MODEL_REF", "opa eval --data policy --input release-evidence.json 'data.release.allow'"), "https://mlflow.org/docs/latest/ml/evaluation/"),

    Leaf(AREA, BRANCH, "deployment-progressive-release", "ML/LLM deployment and progressive release", "Promote immutable releases through shadow, canary, champion/challenger and rollback with infrastructure and quality gates.", C(
        "Release manifest — model, tokenizer, prompt, adapter, runtime, hardware, index, policy and evaluator versions form one deployable contract",
        "Shadow — copies production inputs without user-visible output and requires privacy, side-effect and cost controls",
        "Canary — routes bounded real traffic with automatic infrastructure and task-quality abort thresholds",
        "Champion/challenger — retains incumbent and candidate comparison under explicit promotion authority",
        "Traffic unit — request/user/session/tenant assignment and stickiness determine unbiased consistent comparison",
        "Warmup — model download/load/compile/cache and representative request warmup occur before traffic readiness",
        "Compatibility — schema, client, cache, feature/index and persisted state must work during mixed-version rollout",
        "Rollback — prior bytes/config/index/policy/capacity remain available and correctness is reverified after reversal",
        "Evidence window — rare quality/safety failures may require longer/sample-aware gates than latency/error metrics",
        "Audit — release actor, evidence, traffic changes, exceptions, incidents and final deployed digest remain linked",
    ), ("kubectl rollout status deployment/MODEL -n inference", "kubectl rollout history deployment/MODEL -n inference", "kubectl get inferenceservice MODEL -n inference -o yaml", "curl -s http://MODEL/metrics | rg 'request|token|latency|error'"), "https://kserve.github.io/website/docs/model-serving/predictive-inference/rollout-strategies/canary-examples"),

    Leaf(AREA, BRANCH, "monitoring-drift", "ML monitoring, drift and data quality", "Detect actionable changes in inputs, predictions, labels, quality and system behavior without confusing drift with root cause.", C(
        "Input quality — schema, missingness, ranges, categories and parse failures catch broken pipelines before abstract drift scores",
        "Covariate drift — production input distribution differs from reference but does not alone prove quality degradation",
        "Prediction drift — output distribution changes and can arise from traffic, model, policy or upstream shifts",
        "Concept drift — relationship between input and desired output changes and requires trustworthy delayed labels",
        "Label delay — monitoring architecture reconciles predictions with outcomes later using stable privacy-safe IDs",
        "Slice monitoring — aggregate stability can hide one tenant/language/segment regression",
        "Threshold — expected seasonality/sample size/uncertainty and business impact determine alerting rather than arbitrary distance",
        "Data lineage — identify which source/transform/model deployments explain an observed change",
        "Feedback loop — model decisions can alter future data and create selection or self-reinforcement bias",
        "Response — investigate/evaluate/shadow/retrain/rollback under owned policy; never auto-retrain on one drift metric",
    ), ("python scripts/validate_batch.py --reference reference.parquet --current current.parquet", "curl -s http://MODEL/metrics", "kubectl logs -n inference deploy/MODEL --since=30m", "python -m pytest tests/drift -q"), "https://www.tensorflow.org/tfx/guide/tfdv"),

    Leaf(AREA, BRANCH, "retraining-feedback-loops", "Retraining and feedback loops", "Turn labeled outcomes and approved data changes into bounded retraining without poisoning, bias amplification or uncontrolled promotion.", C(
        "Trigger — schedule, data volume, drift, quality incident or business change proposes retraining under debounce/budget controls",
        "Feedback collection — stable prediction/outcome IDs, consent, provenance and label definition determine trustworthy supervision",
        "Label quality — reviewer agreement, adjudication, sampling and leakage tests are part of training evidence",
        "Sampling bias — observed feedback reflects product exposure and user response rather than the target population automatically",
        "Poisoning — anomalous contributors/content and influence controls protect training/evaluation sets",
        "Replay set — retain representative historical/edge cases so adaptation does not catastrophically forget",
        "Pipeline version — retraining uses immutable data/code/config/environment and produces a new candidate, never silent in-place mutation",
        "Budget/admission — GPU, provider and pipeline quotas prevent feedback automation from starving serving",
        "Validation — candidate must beat champion within owned quality/safety/performance/cost gates",
        "Human promotion — high-risk changes retain approval, exception and rollback rather than automatic drift-to-production",
    ), ("python scripts/build_feedback_dataset.py --dry-run", "dvc repro retrain", "mlflow runs list --experiment-id EXPERIMENT_ID", "python -m evals.run --manifest candidate.yaml --dataset regression.jsonl"), "https://mlflow.org/docs/latest/ml/tracking/"),

    Leaf(AREA, BRANCH, "promptops", "PromptOps: prompt, template and policy lifecycle", "Version, evaluate, approve and observe prompts as executable production configuration.", C(
        "Prompt asset — system/developer/user templates, variables, examples and output schema are versioned independently from application code when needed",
        "Rendering — typed variables, escaping, length limits and deterministic template engine prevent malformed or injected structure",
        "Model coupling — a prompt version is qualified against specific model/tokenizer/provider capabilities and settings",
        "Prompt dataset — expected tasks, edge cases, adversarial inputs and owner define regression evidence",
        "Change review — semantic diff explains instruction/order/example/policy changes beyond line-level text",
        "Release — immutable prompt digest/alias follows shadow/canary and quality/safety/latency/cost gates",
        "Caching — cache keys include prompt/model/policy/tenant semantics and never cross authorization boundaries",
        "Observability — prompt version, safe template ID, tokens, latency, route and evaluation join without logging sensitive rendered content",
        "Rollback — previous prompt and compatible model/tool schema remain deployable with fast traffic reversal",
        "Governance — owner, intended use, prohibited data/actions, approval, exception and retirement are auditable",
    ), ("git diff -- prompts/", "python scripts/render_prompt.py --template prompts/support.yaml --fixture tests/fixture.json", "python -m evals.run --manifest release.yaml --dataset prompt-regression.jsonl", "sha256sum prompts/support.yaml"), "https://opentelemetry.io/docs/specs/semconv/gen-ai/"),

    Leaf(AREA, BRANCH, "llm-finetuning-peft", "LLM fine-tuning, PEFT and adapter operations", "Operate supervised tuning, LoRA/PEFT and preference optimization with reproducible data, checkpoints, evaluation and adapter serving.", C(
        "Objective — continued pretraining, SFT, reward modeling and preference optimization solve different problems/data contracts",
        "Tokenizer/template — chat format and special tokens must match training and serving or quality silently collapses",
        "PEFT/LoRA — low-rank adapter parameters reduce trainable state but introduce base-model/rank/target-module compatibility",
        "QLoRA — quantized base weights save memory while compute dtype, quantization config and optimizer affect stability",
        "Dataset formatting — prompt/completion boundaries, masks, truncation, deduplication and contamination define learning signal",
        "Packing — combines short examples efficiently but requires correct loss masks and sequence-boundary handling",
        "Checkpoint — adapter, optimizer, scheduler, RNG, trainer/data progress and config support restart/reproduction",
        "Merge versus dynamic adapter — merged weights simplify serving while dynamic adapters improve reuse at isolation/cache complexity",
        "Evaluation — task/safety/memorization and base-capability regression compare adapter with base/champion",
        "Lineage/license — base model/data/adapter licenses, consent, provenance and intended-use constraints travel with release",
    ), ("python -m pip show peft transformers accelerate", "accelerate config", "python train_lora.py --config configs/smoke.yaml", "python eval_adapter.py --base BASE_MODEL --adapter output/adapter"), "https://huggingface.co/docs/peft/index"),

    Leaf(AREA, BRANCH, "llm-release-manifest", "LLM release manifests and compatibility", "Bind every LLM system component into an immutable, verifiable and rollback-ready release identity.", C(
        "Weights digest — base and fine-tuned model byte identity is stronger than a mutable repository revision name",
        "Tokenizer — files, normalization, vocabulary, special tokens and chat template are release-critical",
        "Adapter — base compatibility, target modules, rank/alpha and merge state prevent wrong attachment",
        "Runtime — image digest, server version, engine flags, kernels and quantization affect semantics/performance",
        "Hardware — accelerator/driver/CUDA topology qualification and memory profile bound supported deployment",
        "Prompt/tool schema — template/policy/function contracts and structured-output schema are versioned",
        "RAG index — embedding/chunker/corpus/snapshot/ACL policy and index digest affect every answer",
        "Evaluator — dataset/judge/prompt/rubric/calibration and pass thresholds explain approval",
        "Governance — owner, risk class, licenses, data residency, approval/exception and expiry travel with release",
        "Rollback set — prior compatible release and capacity, database/index schemas and cache invalidation steps are retained",
    ), ("python scripts/validate_release_manifest.py release.yaml", "sha256sum model/* tokenizer/*", "cosign verify-blob --signature release.sig release.yaml", "kubectl get deployment MODEL -n inference -o jsonpath='{.spec.template.spec.containers[0].image}'"), "https://slsa.dev/spec/v1.0/"),

    Leaf(AREA, BRANCH, "ragops-index-lifecycle", "RAGOps and index lifecycle", "Reconcile source permissions and changes through parse, chunk, embed, index, retrieval, evaluation, deletion and rollback.", C(
        "Source inventory — owner, connector, classification, ACL, residency, update/delete semantics and watermark are explicit",
        "Ingestion idempotency — stable source/version IDs and checkpoints prevent duplicate or skipped documents",
        "Parser/chunker version — content extraction, tables/images and chunk boundaries change retrieval and require lineage",
        "Embedding release — model/tokenizer/dimension/normalization and batching are immutable index dependencies",
        "Index build — staging index is populated and validated before atomic alias/pointer promotion",
        "Authorization — tenant and source ACL filters apply before context is returned; application post-filtering is too late",
        "Freshness SLI — source update→ingest→embed→index→query visibility latency is measured by stage",
        "Deletion — tombstone and hard-delete reconcile chunks, vector/sparse indexes, caches, evaluations and backups under policy",
        "Evaluation — retrieval recall/precision/MRR/nDCG and answer faithfulness/citation/quality are separated by slices",
        "Rollback — retain compatible prior index and query code; alias reversal must not reintroduce deleted/unauthorized content",
    ), ("python ingest.py --source fixtures/docs --dry-run", "python build_index.py --manifest corpus-v12.json --target staging-v12", "python evaluate_rag.py --dataset eval/rag-golden.jsonl", "curl -s VECTOR_DB/health"), "https://docs.llamaindex.ai/"),

    Leaf(AREA, BRANCH, "evalops", "EvalOps: continuous AI evaluation infrastructure", "Operate versioned datasets, evaluators and release/production evaluation with calibrated uncertainty and actionable ownership.", C(
        "Evaluation contract — task, population, dataset, metric, evaluator, threshold and decision owner define what a score means",
        "Golden dataset — versioned representative, edge, adversarial and previously failed cases have provenance and maintenance owners",
        "Deterministic checks — schema, exact facts, executable tests, citations and policy assertions are preferred where possible",
        "Model-as-judge — prompt/model/temperature/rubric/order bias and nondeterminism require calibration against human labels",
        "Human evaluation — rubric, blinded/randomized assignment, agreement, adjudication and reviewer safety create evidence",
        "RAG decomposition — retrieval relevance/recall and answer faithfulness/quality are measured separately",
        "Statistical comparison — uncertainty, paired tests, multiple slices and minimum practical effect prevent leaderboard overreaction",
        "Release gate — exact candidate/baseline evidence produces pass/fail/exception bound to immutable release",
        "Production sampling — privacy-safe stratified traces and delayed outcomes detect realism gaps without uncontrolled retention",
        "Evaluator monitoring — drift, judge/provider changes, cost/latency and disagreement are themselves observed",
    ), ("python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl", "python -m pytest tests/evaluators -q", "python scripts/calibrate_judge.py --human labels.jsonl --judge results.jsonl", "python scripts/compare_releases.py baseline.json candidate.json --paired"), "https://mlflow.org/docs/latest/ml/evaluation/"),

    Leaf(AREA, BRANCH, "llm-observability", "LLM observability and quality telemetry", "Trace gateway, retrieval, model and tools while protecting prompts, controlling cardinality and joining quality with cost and SLOs.", C(
        "End-to-end trace — gateway→retrieval→rerank→model→tool spans share safe request/release/tenant identifiers",
        "TTFT — time to first token separates admission/queue/prefill from ongoing decode latency",
        "Inter-token latency — streaming cadence reveals decode/runtime/network behavior hidden by total duration",
        "Token work — input/output/cache/tool/image work supports quota, capacity and cost attribution under tokenizer uncertainty",
        "Goodput — requests/tokens satisfying latency, quality and safety are more meaningful than raw GPU utilization",
        "Quality signal — online deterministic checks, feedback and sampled evaluations connect infrastructure to user outcome",
        "Privacy — prompts/responses/retrieved text/tool arguments default to excluded or redacted with controlled sampling/access/retention",
        "Cardinality — model/release/route/status are bounded metric labels; request/user/document IDs belong in traces/logs",
        "Cost — provider charges and allocated accelerator time join tenant/project/release without exposing content",
        "Telemetry reliability — collector/exporter backlog, drops, sampling and schema/version changes are monitored",
    ), ("curl -s http://LLM_GATEWAY/metrics | rg 'token|ttft|latency|cost|error'", "otelcol validate --config otel-collector.yaml", "kubectl logs -n observability deploy/otel-collector --since=30m", "python scripts/trace_release.py --release RELEASE_ID"), "https://opentelemetry.io/docs/specs/semconv/gen-ai/"),

    Leaf(AREA, BRANCH, "gateway-providerops", "LLM gateway and ProviderOps", "Operate normalized model access, quotas, routing, fallbacks, provider changes, metering and incident response.", C(
        "Normalized API — common request/response cannot erase provider differences in tools, streaming, errors, tokens and safety",
        "Model catalog — alias maps to approved provider/model/region/capabilities/context/price under versioned policy",
        "Tenant policy — identity derives allowed models, data routes, quotas, logging, tools and budget",
        "Admission — request/token/concurrency/queued-work controls protect provider and self-hosted capacity fairly",
        "Routing — capability, health, residency, cost and experiment policy choose a route with auditable reason",
        "Retry — bounded backoff honors provider hints and only retries safe stages; streamed output/unknown side effects prevent transparent replay",
        "Fallback — alternate route is prequalified for schema, quality, safety, residency and cost rather than merely available",
        "Provider release — model alias/version/deprecation changes need contract/eval canary and rollback like internal changes",
        "Metering — estimated/actual tokens, cache and tool work reconcile with invoice and tenant allocation",
        "Incident — circuit, shed, queue, failover or degrade under explicit SLO/quality/security trade-offs and communication",
    ), ("curl -N -v GATEWAY/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json", "curl -s GATEWAY/metrics", "kubectl logs -n ai-platform deploy/llm-gateway --since=30m", "python scripts/reconcile_provider_invoice.py --month YYYY-MM"), "https://opentelemetry.io/docs/specs/semconv/gen-ai/"),

    Leaf(AREA, BRANCH, "safety-redteam-guardrails", "LLM safety, red teaming and guardrail operations", "Turn threat models and safety policies into tested release/runtime controls with measurable false positives and bypass handling.", C(
        "Threat model — assets, actors, trust boundaries and abuse cases span prompt, retrieval, model, tool, provider and operators",
        "Policy taxonomy — harmful content, privacy, authorization, regulated advice and customer-specific rules need owned definitions",
        "Pre-input control — size/schema/malware/PII and policy checks bound input but cannot prove downstream safety",
        "Prompt injection — untrusted user/retrieved/tool content cannot grant system or tool authority",
        "Output control — validate structured data, content policy, citations and destinations before display or execution",
        "Tool guardrail — deterministic authorization, schema/range checks, idempotency and approval mediate model-proposed actions",
        "Red-team corpus — versioned attack/edge cases record threat, expected behavior, severity and regression owner",
        "Adaptive testing — mutation/multiturn/encoding/tool/retrieval attacks explore beyond static known strings",
        "Operations — false positive/negative, override/appeal, latency, availability and policy-version metrics have SLO/owners",
        "Incident learning — preserve safe evidence, contain routes/tools/data, add regression cases and verify control changes",
    ), ("python -m pytest tests/guardrails -q", "python redteam.py --manifest release.yaml --suite suites/prompt-injection.yaml", "opa test policy/", "kubectl logs -n ai-platform deploy/policy-engine --since=30m"), "https://genai.owasp.org/"),

    Leaf(AREA, BRANCH, "agentops", "AgentOps and tool-using system operations", "Operate plans, state, tool calls and approvals as durable, authorized workflows rather than trusting generated text.", C(
        "Run state machine — queued/running/waiting-approval/succeeded/failed/canceled/compensating states survive worker restart",
        "Tool contract — typed input/output/error/idempotency/timeout and side-effect classification are versioned",
        "Authorization — user and workload identity plus current resource context authorize every call at execution time",
        "Capability — agent receives narrow short-lived tool/resource scope rather than ambient broad credentials",
        "Idempotency — stable operation key and result lookup handle timeout with unknown side effect",
        "Approval — high-risk proposed action includes diff/target/effect/evidence/expiry and revalidates after approval",
        "Budgets — steps, wall time, tokens, spend, retries and external calls bound loops and denial-of-wallet",
        "Sandbox — generated code/browser/file/network operations run in isolated constrained environments",
        "Trace — model/tool/policy/approval state transitions and safe arguments/results support replay and evaluation",
        "Evaluation — task success, policy compliance, tool correctness, recovery, cost and adversarial behavior are release gates",
    ), ("python -m pytest tests/agent_tools -q", "python run_agent.py --fixture tests/task.json --max-steps 8 --dry-run", "curl -s AGENT_API/runs/RUN_ID | jq", "opa eval --data policy --input proposed-tool-call.json 'data.tools.allow'"), "https://modelcontextprotocol.io/docs/getting-started/intro"),

    Leaf(AREA, BRANCH, "ai-supply-chain", "AI supply chain, signing and provenance", "Verify code, containers, models, tokenizers, adapters, datasets and evaluation evidence from source to deployed release.", C(
        "Source provenance — repository/revision/review and build identity connect declared source to artifact",
        "Dependency lock/SBOM — software names/versions/hashes/licenses/vulnerabilities cover training and serving environments",
        "Model provenance — origin, base, fine-tuning data/process, transforms and digest establish lineage beyond filename",
        "Unsafe serialization — pickle-like formats can execute code; prefer safe formats and isolated inspection for untrusted models",
        "OCI artifact — media types/manifests/subject/referrers store models, SBOMs, signatures and attestations in registries",
        "Signature — verifies signer/keyless identity and bytes under trust policy, not model quality or authorization alone",
        "Attestation — predicate records build/training/evaluation facts with verifiable producer identity and inputs",
        "Registry policy — immutability, retention, replication, vulnerability/malware scanning and access logs protect promotion",
        "Release verification — admission checks exact digest, signature/attestation, policy and environment compatibility",
        "Revocation/response — inventory maps compromised dependency/model to runs, releases and deployments for containment",
    ), ("syft IMAGE -o cyclonedx-json", "oras manifest fetch MODEL_REF", "cosign verify MODEL_REF", "cosign verify-attestation --type slsaprovenance MODEL_REF"), "https://docs.sigstore.dev/"),

    Leaf(AREA, BRANCH, "governance-approval-evidence", "AI governance, approval and evidence automation", "Make inventory, ownership, risk, policy, lineage, approval, exceptions, audit and retirement executable platform workflows.", C(
        "AI inventory — system/model/dataset/prompt/index/tool/evaluator/deployment assets have owners and current lifecycle state",
        "Risk classification — intended use, affected users, autonomy, data and consequence determine control rigor",
        "Control mapping — policy requirement maps to automated/manual control, evidence source, frequency and accountable owner",
        "Approval package — immutable release plus evaluation/safety/security/privacy/operational evidence supports decision",
        "Exception — scoped asset/target, rationale, compensating control, risk owner and expiry prevent permanent invisible bypass",
        "Separation of duties — builder/evaluator/approver/deployer roles reduce unilateral high-risk release",
        "Audit event — actor/action/target/revision/decision/reason/evidence/result/time are tamper-resistant and searchable",
        "Change impact — lineage identifies systems, data subjects and controls affected by model/data/prompt/provider change",
        "Appeal/override — operational process records user/customer contest and policy override without erasing original decision",
        "Retirement — disable routes/tools, revoke access, preserve required evidence and delete data/artifacts under policy",
    ), ("python scripts/inventory_lint.py inventory/*.yaml", "opa test governance/policy", "python scripts/build_approval_package.py --release release.yaml", "python scripts/find_impact.py --asset MODEL_DIGEST"), "https://www.nist.gov/itl/ai-risk-management-framework"),

    Leaf(AREA, BRANCH, "ai-finops-capacity", "MLOps/LLMOps FinOps and capacity", "Allocate and optimize training, serving, retrieval, evaluation and telemetry cost per successful quality-controlled outcome.", C(
        "Cost taxonomy — training GPU, serving capacity/provider tokens, storage, vector/search, network and telemetry are separated",
        "Allocation — tenant/project/model/release/environment/owner identifiers join billing without high-cardinality metric abuse",
        "Unit economics — cost per trained candidate, evaluated case, indexed document and successful quality-controlled request guide decisions",
        "Goodput — paid work meeting latency/quality/safety is distinguished from raw tokens, requests or GPU utilization",
        "Training efficiency — samples/tokens to target quality, GPU goodput, checkpoint waste and experiment pruning control spend",
        "Serving efficiency — batching, KV/cache, quantization, routing, autoscaling and warm capacity trade cost against SLO/quality",
        "Provider reconciliation — gateway estimates compare with provider usage/invoice and flag routing/metering drift",
        "Budget control — forecast, quota, alert, admission and approval stop runaway experiments/agents/evaluations safely",
        "Commitment — reservations/savings plans/capacity contracts match stable floor while burst/interruption strategies cover variance",
        "Optimization gate — every saving proposal states expected amount, SLO/quality/security risk, experiment and rollback threshold",
    ), ("python scripts/cost_per_release.py --release RELEASE_ID", "kubectl top pod -A --containers", "nvidia-smi dmon -s pucvmet", "python scripts/reconcile_usage.py --provider PROVIDER --month YYYY-MM"), "https://www.finops.org/framework/"),
]


PRACTICE = """

## Hands-on proof: easy → hard

Use a disposable local environment, sandbox project/account or isolated Kubernetes namespace. Define all uppercase placeholders before running commands and confirm identity/context, data classification and cost boundary.

1. **Inventory:** run the read-only commands above, capture exact versions/IDs and explain which desired or observed state each proves.
2. **Build:** implement the smallest version-controlled example with an immutable input/artifact manifest and one automated test.
3. **Failure:** inject one bounded invalid input, dependency outage, incompatible revision, quota or stale-state condition; preserve the error and distinguish its layer without restarting blindly.
4. **Release:** generate evidence, compare a candidate with a baseline, make an explicit pass/fail decision and prove the deployed/run revision.
5. **Recover:** roll back or resume from a protected artifact/checkpoint, re-run the original quality and operational verification, and reconcile the source of truth.
6. **Cleanup:** delete only named lab resources and confirm no job, endpoint, volume, artifact, credential or billable accelerator remains. Retain only non-sensitive learning evidence allowed by policy.

Hard extension: put the lab in CI with short-lived identity, policy/evaluation gates, bounded concurrency/cost, an artifact digest, a failure-path test and a five-step runbook.
"""


def main() -> None:
    base = ROOT / AREA / BRANCH
    for leaf in LEAVES:
        path = base / leaf.slug
        write(path / "README.md", notes(leaf) + PRACTICE)
        write(path / "questions-and-answers.md", qna(leaf))
    print(f"generated {len(LEAVES)} practical MLOps/LLMOps leaves")


if __name__ == "__main__":
    main()
