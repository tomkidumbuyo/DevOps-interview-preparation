# LLM fine-tuning, PEFT and adapter operations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JN-01

- [ ] **Question:** What is Objective, and why does it matter in LLM fine-tuning, PEFT and adapter operations?

**Answer:** continued pretraining, SFT, reward modeling and preference optimization solve different problems/data contracts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JN-02

- [ ] **Question:** What is Tokenizer/template, and why does it matter in LLM fine-tuning, PEFT and adapter operations?

**Answer:** chat format and special tokens must match training and serving or quality silently collapses. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JN-03

- [ ] **Question:** What is PEFT/LoRA, and why does it matter in LLM fine-tuning, PEFT and adapter operations?

**Answer:** low-rank adapter parameters reduce trainable state but introduce base-model/rank/target-module compatibility. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JN-04

- [ ] **Question:** What is QLoRA, and why does it matter in LLM fine-tuning, PEFT and adapter operations?

**Answer:** quantized base weights save memory while compute dtype, quantization config and optimizer affect stability. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JN-05

- [ ] **Question:** What is Dataset formatting, and why does it matter in LLM fine-tuning, PEFT and adapter operations?

**Answer:** prompt/completion boundaries, masks, truncation, deduplication and contamination define learning signal. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JN-06

- [ ] **Question:** What is Packing, and why does it matter in LLM fine-tuning, PEFT and adapter operations?

**Answer:** combines short examples efficiently but requires correct loss masks and sequence-boundary handling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JN-07

- [ ] **Question:** What is Checkpoint, and why does it matter in LLM fine-tuning, PEFT and adapter operations?

**Answer:** adapter, optimizer, scheduler, RNG, trainer/data progress and config support restart/reproduction. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JN-08

- [ ] **Code:** **Question:** What does `python eval_adapter.py --base BASE_MODEL --adapter output/adapter` help you verify for LLM fine-tuning, PEFT and adapter operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: merged weights simplify serving while dynamic adapters improve reuse at isolation/cache complexity.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JN-09

- [ ] **Code:** **Question:** What does `python -m pip show peft transformers accelerate` help you verify for LLM fine-tuning, PEFT and adapter operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: task/safety/memorization and base-capability regression compare adapter with base/champion.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JN-10

- [ ] **Code:** **Question:** What does `accelerate config` help you verify for LLM fine-tuning, PEFT and adapter operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: base model/data/adapter licenses, consent, provenance and intended-use constraints travel with release.

## Junior — procedural and command questions

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JP-01

- [ ] **Code:** **Question:** A basic Objective check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pip show peft transformers accelerate` and capture exact status/reason/request ID. continued pretraining, SFT, reward modeling and preference optimization solve different problems/data contracts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JP-02

- [ ] **Question:** A basic Tokenizer/template check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `accelerate config` and capture exact status/reason/request ID. chat format and special tokens must match training and serving or quality silently collapses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JP-03

- [ ] **Question:** A basic PEFT/LoRA check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python train_lora.py --config configs/smoke.yaml` and capture exact status/reason/request ID. low-rank adapter parameters reduce trainable state but introduce base-model/rank/target-module compatibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JP-04

- [ ] **Code:** **Question:** A basic QLoRA check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python eval_adapter.py --base BASE_MODEL --adapter output/adapter` and capture exact status/reason/request ID. quantized base weights save memory while compute dtype, quantization config and optimizer affect stability. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JP-05

- [ ] **Question:** A basic Dataset formatting check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pip show peft transformers accelerate` and capture exact status/reason/request ID. prompt/completion boundaries, masks, truncation, deduplication and contamination define learning signal. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JP-06

- [ ] **Question:** A basic Packing check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `accelerate config` and capture exact status/reason/request ID. combines short examples efficiently but requires correct loss masks and sequence-boundary handling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JP-07

- [ ] **Code:** **Question:** A basic Checkpoint check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python train_lora.py --config configs/smoke.yaml` and capture exact status/reason/request ID. adapter, optimizer, scheduler, RNG, trainer/data progress and config support restart/reproduction. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JP-08

- [ ] **Question:** A basic Merge versus dynamic adapter check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python eval_adapter.py --base BASE_MODEL --adapter output/adapter` and capture exact status/reason/request ID. merged weights simplify serving while dynamic adapters improve reuse at isolation/cache complexity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JP-09

- [ ] **Question:** A basic Evaluation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pip show peft transformers accelerate` and capture exact status/reason/request ID. task/safety/memorization and base-capability regression compare adapter with base/champion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-JP-10

- [ ] **Code:** **Question:** A basic Lineage/license check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `accelerate config` and capture exact status/reason/request ID. base model/data/adapter licenses, consent, provenance and intended-use constraints travel with release. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MN-01

- [ ] **Question:** Compare Objective with Tokenizer/template. When would each change your design?

**Answer:** Objective: continued pretraining, SFT, reward modeling and preference optimization solve different problems/data contracts. Tokenizer/template: chat format and special tokens must match training and serving or quality silently collapses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MN-02

- [ ] **Question:** Compare Tokenizer/template with PEFT/LoRA. When would each change your design?

**Answer:** Tokenizer/template: chat format and special tokens must match training and serving or quality silently collapses. PEFT/LoRA: low-rank adapter parameters reduce trainable state but introduce base-model/rank/target-module compatibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MN-03

- [ ] **Question:** Compare PEFT/LoRA with QLoRA. When would each change your design?

**Answer:** PEFT/LoRA: low-rank adapter parameters reduce trainable state but introduce base-model/rank/target-module compatibility. QLoRA: quantized base weights save memory while compute dtype, quantization config and optimizer affect stability. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare QLoRA with Dataset formatting. When would each change your design?

**Answer:** QLoRA: quantized base weights save memory while compute dtype, quantization config and optimizer affect stability. Dataset formatting: prompt/completion boundaries, masks, truncation, deduplication and contamination define learning signal. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MN-05

- [ ] **Question:** Compare Dataset formatting with Packing. When would each change your design?

**Answer:** Dataset formatting: prompt/completion boundaries, masks, truncation, deduplication and contamination define learning signal. Packing: combines short examples efficiently but requires correct loss masks and sequence-boundary handling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MN-06

- [ ] **Question:** Compare Packing with Checkpoint. When would each change your design?

**Answer:** Packing: combines short examples efficiently but requires correct loss masks and sequence-boundary handling. Checkpoint: adapter, optimizer, scheduler, RNG, trainer/data progress and config support restart/reproduction. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Checkpoint with Merge versus dynamic adapter. When would each change your design?

**Answer:** Checkpoint: adapter, optimizer, scheduler, RNG, trainer/data progress and config support restart/reproduction. Merge versus dynamic adapter: merged weights simplify serving while dynamic adapters improve reuse at isolation/cache complexity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MN-08

- [ ] **Question:** Compare Merge versus dynamic adapter with Evaluation. When would each change your design?

**Answer:** Merge versus dynamic adapter: merged weights simplify serving while dynamic adapters improve reuse at isolation/cache complexity. Evaluation: task/safety/memorization and base-capability regression compare adapter with base/champion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MN-09

- [ ] **Question:** Compare Evaluation with Lineage/license. When would each change your design?

**Answer:** Evaluation: task/safety/memorization and base-capability regression compare adapter with base/champion. Lineage/license: base model/data/adapter licenses, consent, provenance and intended-use constraints travel with release. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Lineage/license with Objective. When would each change your design?

**Answer:** Lineage/license: base model/data/adapter licenses, consent, provenance and intended-use constraints travel with release. Objective: continued pretraining, SFT, reward modeling and preference optimization solve different problems/data contracts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Objective; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pip show peft transformers accelerate` plus recent events/changes, then correlate the service-specific SLI. continued pretraining, SFT, reward modeling and preference optimization solve different problems/data contracts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MP-02

- [ ] **Question:** Production is degraded around Tokenizer/template; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `accelerate config` plus recent events/changes, then correlate the service-specific SLI. chat format and special tokens must match training and serving or quality silently collapses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around PEFT/LoRA; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python train_lora.py --config configs/smoke.yaml` plus recent events/changes, then correlate the service-specific SLI. low-rank adapter parameters reduce trainable state but introduce base-model/rank/target-module compatibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MP-04

- [ ] **Question:** Production is degraded around QLoRA; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python eval_adapter.py --base BASE_MODEL --adapter output/adapter` plus recent events/changes, then correlate the service-specific SLI. quantized base weights save memory while compute dtype, quantization config and optimizer affect stability. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Dataset formatting; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pip show peft transformers accelerate` plus recent events/changes, then correlate the service-specific SLI. prompt/completion boundaries, masks, truncation, deduplication and contamination define learning signal. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MP-06

- [ ] **Question:** Production is degraded around Packing; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `accelerate config` plus recent events/changes, then correlate the service-specific SLI. combines short examples efficiently but requires correct loss masks and sequence-boundary handling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Checkpoint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python train_lora.py --config configs/smoke.yaml` plus recent events/changes, then correlate the service-specific SLI. adapter, optimizer, scheduler, RNG, trainer/data progress and config support restart/reproduction. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MP-08

- [ ] **Question:** Production is degraded around Merge versus dynamic adapter; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python eval_adapter.py --base BASE_MODEL --adapter output/adapter` plus recent events/changes, then correlate the service-specific SLI. merged weights simplify serving while dynamic adapters improve reuse at isolation/cache complexity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Evaluation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pip show peft transformers accelerate` plus recent events/changes, then correlate the service-specific SLI. task/safety/memorization and base-capability regression compare adapter with base/champion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-MP-10

- [ ] **Question:** Production is degraded around Lineage/license; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `accelerate config` plus recent events/changes, then correlate the service-specific SLI. base model/data/adapter licenses, consent, provenance and intended-use constraints travel with release. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SN-01

- [ ] **Question:** Design a production LLM fine-tuning, PEFT and adapter operations capability where Objective, QLoRA and Checkpoint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: continued pretraining, SFT, reward modeling and preference optimization solve different problems/data contracts. quantized base weights save memory while compute dtype, quantization config and optimizer affect stability. adapter, optimizer, scheduler, RNG, trainer/data progress and config support restart/reproduction. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production LLM fine-tuning, PEFT and adapter operations capability where Tokenizer/template, Dataset formatting and Merge versus dynamic adapter are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: chat format and special tokens must match training and serving or quality silently collapses. prompt/completion boundaries, masks, truncation, deduplication and contamination define learning signal. merged weights simplify serving while dynamic adapters improve reuse at isolation/cache complexity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SN-03

- [ ] **Question:** Design a production LLM fine-tuning, PEFT and adapter operations capability where PEFT/LoRA, Packing and Evaluation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: low-rank adapter parameters reduce trainable state but introduce base-model/rank/target-module compatibility. combines short examples efficiently but requires correct loss masks and sequence-boundary handling. task/safety/memorization and base-capability regression compare adapter with base/champion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production LLM fine-tuning, PEFT and adapter operations capability where QLoRA, Checkpoint and Lineage/license are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: quantized base weights save memory while compute dtype, quantization config and optimizer affect stability. adapter, optimizer, scheduler, RNG, trainer/data progress and config support restart/reproduction. base model/data/adapter licenses, consent, provenance and intended-use constraints travel with release. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SN-05

- [ ] **Question:** Design a production LLM fine-tuning, PEFT and adapter operations capability where Dataset formatting, Merge versus dynamic adapter and Objective are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prompt/completion boundaries, masks, truncation, deduplication and contamination define learning signal. merged weights simplify serving while dynamic adapters improve reuse at isolation/cache complexity. continued pretraining, SFT, reward modeling and preference optimization solve different problems/data contracts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production LLM fine-tuning, PEFT and adapter operations capability where Packing, Evaluation and Tokenizer/template are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: combines short examples efficiently but requires correct loss masks and sequence-boundary handling. task/safety/memorization and base-capability regression compare adapter with base/champion. chat format and special tokens must match training and serving or quality silently collapses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SN-07

- [ ] **Question:** Design a production LLM fine-tuning, PEFT and adapter operations capability where Checkpoint, Lineage/license and PEFT/LoRA are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: adapter, optimizer, scheduler, RNG, trainer/data progress and config support restart/reproduction. base model/data/adapter licenses, consent, provenance and intended-use constraints travel with release. low-rank adapter parameters reduce trainable state but introduce base-model/rank/target-module compatibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production LLM fine-tuning, PEFT and adapter operations capability where Merge versus dynamic adapter, Objective and QLoRA are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: merged weights simplify serving while dynamic adapters improve reuse at isolation/cache complexity. continued pretraining, SFT, reward modeling and preference optimization solve different problems/data contracts. quantized base weights save memory while compute dtype, quantization config and optimizer affect stability. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SN-09

- [ ] **Question:** Design a production LLM fine-tuning, PEFT and adapter operations capability where Evaluation, Tokenizer/template and Dataset formatting are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: task/safety/memorization and base-capability regression compare adapter with base/champion. chat format and special tokens must match training and serving or quality silently collapses. prompt/completion boundaries, masks, truncation, deduplication and contamination define learning signal. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production LLM fine-tuning, PEFT and adapter operations capability where Lineage/license, PEFT/LoRA and Packing are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: base model/data/adapter licenses, consent, provenance and intended-use constraints travel with release. low-rank adapter parameters reduce trainable state but introduce base-model/rank/target-module compatibility. combines short examples efficiently but requires correct loss masks and sequence-boundary handling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Objective. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pip show peft transformers accelerate` as one read-only checkpoint, not the whole diagnosis. continued pretraining, SFT, reward modeling and preference optimization solve different problems/data contracts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tokenizer/template. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `accelerate config` as one read-only checkpoint, not the whole diagnosis. chat format and special tokens must match training and serving or quality silently collapses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving PEFT/LoRA. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python train_lora.py --config configs/smoke.yaml` as one read-only checkpoint, not the whole diagnosis. low-rank adapter parameters reduce trainable state but introduce base-model/rank/target-module compatibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving QLoRA. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python eval_adapter.py --base BASE_MODEL --adapter output/adapter` as one read-only checkpoint, not the whole diagnosis. quantized base weights save memory while compute dtype, quantization config and optimizer affect stability. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dataset formatting. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pip show peft transformers accelerate` as one read-only checkpoint, not the whole diagnosis. prompt/completion boundaries, masks, truncation, deduplication and contamination define learning signal. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Packing. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `accelerate config` as one read-only checkpoint, not the whole diagnosis. combines short examples efficiently but requires correct loss masks and sequence-boundary handling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Checkpoint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python train_lora.py --config configs/smoke.yaml` as one read-only checkpoint, not the whole diagnosis. adapter, optimizer, scheduler, RNG, trainer/data progress and config support restart/reproduction. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Merge versus dynamic adapter. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python eval_adapter.py --base BASE_MODEL --adapter output/adapter` as one read-only checkpoint, not the whole diagnosis. merged weights simplify serving while dynamic adapters improve reuse at isolation/cache complexity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Evaluation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pip show peft transformers accelerate` as one read-only checkpoint, not the whole diagnosis. task/safety/memorization and base-capability regression compare adapter with base/champion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLM-FINE-TUNING-PEFT-AND-ADAPTER-OPERATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lineage/license. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `accelerate config` as one read-only checkpoint, not the whole diagnosis. base model/data/adapter licenses, consent, provenance and intended-use constraints travel with release. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
