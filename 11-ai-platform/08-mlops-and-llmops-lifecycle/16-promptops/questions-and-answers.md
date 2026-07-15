# PromptOps: prompt, template and policy lifecycle — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JN-01

- [ ] **Question:** What is Prompt asset, and why does it matter in PromptOps: prompt, template and policy lifecycle?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** system/developer/user templates, variables, examples and output schema are versioned independently from application code when needed. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JN-02

- [ ] **Question:** What is Rendering, and why does it matter in PromptOps: prompt, template and policy lifecycle?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** typed variables, escaping, length limits and deterministic template engine prevent malformed or injected structure. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JN-03

- [ ] **Question:** What is Model coupling, and why does it matter in PromptOps: prompt, template and policy lifecycle?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** a prompt version is qualified against specific model/tokenizer/provider capabilities and settings. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JN-04

- [ ] **Question:** What is Prompt dataset, and why does it matter in PromptOps: prompt, template and policy lifecycle?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** expected tasks, edge cases, adversarial inputs and owner define regression evidence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JN-05

- [ ] **Question:** What is Change review, and why does it matter in PromptOps: prompt, template and policy lifecycle?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** semantic diff explains instruction/order/example/policy changes beyond line-level text. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JN-06

- [ ] **Question:** What is Release, and why does it matter in PromptOps: prompt, template and policy lifecycle?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** immutable prompt digest/alias follows shadow/canary and quality/safety/latency/cost gates. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JN-07

- [ ] **Question:** What is Caching, and why does it matter in PromptOps: prompt, template and policy lifecycle?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** cache keys include prompt/model/policy/tenant semantics and never cross authorization boundaries. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JN-08

- [ ] **Code:** **Question:** What does `sha256sum prompts/support.yaml` help you verify for PromptOps: prompt, template and policy lifecycle?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: prompt version, safe template ID, tokens, latency, route and evaluation join without logging sensitive rendered content.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JN-09

- [ ] **Code:** **Question:** What does `git diff -- prompts/` help you verify for PromptOps: prompt, template and policy lifecycle?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: previous prompt and compatible model/tool schema remain deployable with fast traffic reversal.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JN-10

- [ ] **Code:** **Question:** What does `python scripts/render_prompt.py --template prompts/support.yaml --fixture tests/fixture.json` help you verify for PromptOps: prompt, template and policy lifecycle?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: owner, intended use, prohibited data/actions, approval, exception and retirement are auditable.

## Junior — procedural and command questions

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JP-01

- [ ] **Code:** **Question:** A basic Prompt asset check fails. What would you do first using the CLI?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff -- prompts/` and capture exact status/reason/request ID. system/developer/user templates, variables, examples and output schema are versioned independently from application code when needed. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JP-02

- [ ] **Question:** A basic Rendering check fails. What would you do first?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/render_prompt.py --template prompts/support.yaml --fixture tests/fixture.json` and capture exact status/reason/request ID. typed variables, escaping, length limits and deterministic template engine prevent malformed or injected structure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JP-03

- [ ] **Question:** A basic Model coupling check fails. What would you do first?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Security model](README.md#security-model)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml --dataset prompt-regression.jsonl` and capture exact status/reason/request ID. a prompt version is qualified against specific model/tokenizer/provider capabilities and settings. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JP-04

- [ ] **Code:** **Question:** A basic Prompt dataset check fails. What would you do first using the CLI?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `sha256sum prompts/support.yaml` and capture exact status/reason/request ID. expected tasks, edge cases, adversarial inputs and owner define regression evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JP-05

- [ ] **Question:** A basic Change review check fails. What would you do first?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff -- prompts/` and capture exact status/reason/request ID. semantic diff explains instruction/order/example/policy changes beyond line-level text. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JP-06

- [ ] **Question:** A basic Release check fails. What would you do first?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/render_prompt.py --template prompts/support.yaml --fixture tests/fixture.json` and capture exact status/reason/request ID. immutable prompt digest/alias follows shadow/canary and quality/safety/latency/cost gates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JP-07

- [ ] **Code:** **Question:** A basic Caching check fails. What would you do first using the CLI?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml --dataset prompt-regression.jsonl` and capture exact status/reason/request ID. cache keys include prompt/model/policy/tenant semantics and never cross authorization boundaries. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JP-08

- [ ] **Question:** A basic Observability check fails. What would you do first?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `sha256sum prompts/support.yaml` and capture exact status/reason/request ID. prompt version, safe template ID, tokens, latency, route and evaluation join without logging sensitive rendered content. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JP-09

- [ ] **Question:** A basic Rollback check fails. What would you do first?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff -- prompts/` and capture exact status/reason/request ID. previous prompt and compatible model/tool schema remain deployable with fast traffic reversal. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-JP-10

- [ ] **Code:** **Question:** A basic Governance check fails. What would you do first using the CLI?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/render_prompt.py --template prompts/support.yaml --fixture tests/fixture.json` and capture exact status/reason/request ID. owner, intended use, prohibited data/actions, approval, exception and retirement are auditable. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MN-01

- [ ] **Question:** Compare Prompt asset with Rendering. When would each change your design?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Prompt asset: system/developer/user templates, variables, examples and output schema are versioned independently from application code when needed. Rendering: typed variables, escaping, length limits and deterministic template engine prevent malformed or injected structure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MN-02

- [ ] **Question:** Compare Rendering with Model coupling. When would each change your design?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Rendering: typed variables, escaping, length limits and deterministic template engine prevent malformed or injected structure. Model coupling: a prompt version is qualified against specific model/tokenizer/provider capabilities and settings. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MN-03

- [ ] **Question:** Compare Model coupling with Prompt dataset. When would each change your design?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Model coupling: a prompt version is qualified against specific model/tokenizer/provider capabilities and settings. Prompt dataset: expected tasks, edge cases, adversarial inputs and owner define regression evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MN-04

- [ ] **Configuration review:** **Question:** Compare Prompt dataset with Change review. When would each change your design?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Prompt dataset: expected tasks, edge cases, adversarial inputs and owner define regression evidence. Change review: semantic diff explains instruction/order/example/policy changes beyond line-level text. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MN-05

- [ ] **Question:** Compare Change review with Release. When would each change your design?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Change review: semantic diff explains instruction/order/example/policy changes beyond line-level text. Release: immutable prompt digest/alias follows shadow/canary and quality/safety/latency/cost gates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MN-06

- [ ] **Question:** Compare Release with Caching. When would each change your design?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Release: immutable prompt digest/alias follows shadow/canary and quality/safety/latency/cost gates. Caching: cache keys include prompt/model/policy/tenant semantics and never cross authorization boundaries. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MN-07

- [ ] **Configuration review:** **Question:** Compare Caching with Observability. When would each change your design?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Caching: cache keys include prompt/model/policy/tenant semantics and never cross authorization boundaries. Observability: prompt version, safe template ID, tokens, latency, route and evaluation join without logging sensitive rendered content. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MN-08

- [ ] **Question:** Compare Observability with Rollback. When would each change your design?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Observability: prompt version, safe template ID, tokens, latency, route and evaluation join without logging sensitive rendered content. Rollback: previous prompt and compatible model/tool schema remain deployable with fast traffic reversal. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MN-09

- [ ] **Question:** Compare Rollback with Governance. When would each change your design?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Rollback: previous prompt and compatible model/tool schema remain deployable with fast traffic reversal. Governance: owner, intended use, prohibited data/actions, approval, exception and retirement are auditable. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MN-10

- [ ] **Configuration review:** **Question:** Compare Governance with Prompt asset. When would each change your design?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Governance: owner, intended use, prohibited data/actions, approval, exception and retirement are auditable. Prompt asset: system/developer/user templates, variables, examples and output schema are versioned independently from application code when needed. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Prompt asset; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff -- prompts/` plus recent events/changes, then correlate the service-specific SLI. system/developer/user templates, variables, examples and output schema are versioned independently from application code when needed. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MP-02

- [ ] **Question:** Production is degraded around Rendering; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/render_prompt.py --template prompts/support.yaml --fixture tests/fixture.json` plus recent events/changes, then correlate the service-specific SLI. typed variables, escaping, length limits and deterministic template engine prevent malformed or injected structure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model coupling; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml --dataset prompt-regression.jsonl` plus recent events/changes, then correlate the service-specific SLI. a prompt version is qualified against specific model/tokenizer/provider capabilities and settings. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MP-04

- [ ] **Question:** Production is degraded around Prompt dataset; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `sha256sum prompts/support.yaml` plus recent events/changes, then correlate the service-specific SLI. expected tasks, edge cases, adversarial inputs and owner define regression evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Change review; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff -- prompts/` plus recent events/changes, then correlate the service-specific SLI. semantic diff explains instruction/order/example/policy changes beyond line-level text. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MP-06

- [ ] **Question:** Production is degraded around Release; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/render_prompt.py --template prompts/support.yaml --fixture tests/fixture.json` plus recent events/changes, then correlate the service-specific SLI. immutable prompt digest/alias follows shadow/canary and quality/safety/latency/cost gates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Caching; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml --dataset prompt-regression.jsonl` plus recent events/changes, then correlate the service-specific SLI. cache keys include prompt/model/policy/tenant semantics and never cross authorization boundaries. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MP-08

- [ ] **Question:** Production is degraded around Observability; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Observability](README.md#observability)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `sha256sum prompts/support.yaml` plus recent events/changes, then correlate the service-specific SLI. prompt version, safe template ID, tokens, latency, route and evaluation join without logging sensitive rendered content. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Rollback; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff -- prompts/` plus recent events/changes, then correlate the service-specific SLI. previous prompt and compatible model/tool schema remain deployable with fast traffic reversal. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-MP-10

- [ ] **Question:** Production is degraded around Governance; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/render_prompt.py --template prompts/support.yaml --fixture tests/fixture.json` plus recent events/changes, then correlate the service-specific SLI. owner, intended use, prohibited data/actions, approval, exception and retirement are auditable. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SN-01

- [ ] **Question:** Design a production PromptOps: prompt, template and policy lifecycle capability where Prompt asset, Prompt dataset and Caching are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: system/developer/user templates, variables, examples and output schema are versioned independently from application code when needed. expected tasks, edge cases, adversarial inputs and owner define regression evidence. cache keys include prompt/model/policy/tenant semantics and never cross authorization boundaries. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production PromptOps: prompt, template and policy lifecycle capability where Rendering, Change review and Observability are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: typed variables, escaping, length limits and deterministic template engine prevent malformed or injected structure. semantic diff explains instruction/order/example/policy changes beyond line-level text. prompt version, safe template ID, tokens, latency, route and evaluation join without logging sensitive rendered content. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SN-03

- [ ] **Question:** Design a production PromptOps: prompt, template and policy lifecycle capability where Model coupling, Release and Rollback are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: a prompt version is qualified against specific model/tokenizer/provider capabilities and settings. immutable prompt digest/alias follows shadow/canary and quality/safety/latency/cost gates. previous prompt and compatible model/tool schema remain deployable with fast traffic reversal. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production PromptOps: prompt, template and policy lifecycle capability where Prompt dataset, Caching and Governance are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: expected tasks, edge cases, adversarial inputs and owner define regression evidence. cache keys include prompt/model/policy/tenant semantics and never cross authorization boundaries. owner, intended use, prohibited data/actions, approval, exception and retirement are auditable. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SN-05

- [ ] **Question:** Design a production PromptOps: prompt, template and policy lifecycle capability where Change review, Observability and Prompt asset are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: semantic diff explains instruction/order/example/policy changes beyond line-level text. prompt version, safe template ID, tokens, latency, route and evaluation join without logging sensitive rendered content. system/developer/user templates, variables, examples and output schema are versioned independently from application code when needed. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production PromptOps: prompt, template and policy lifecycle capability where Release, Rollback and Rendering are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable prompt digest/alias follows shadow/canary and quality/safety/latency/cost gates. previous prompt and compatible model/tool schema remain deployable with fast traffic reversal. typed variables, escaping, length limits and deterministic template engine prevent malformed or injected structure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SN-07

- [ ] **Question:** Design a production PromptOps: prompt, template and policy lifecycle capability where Caching, Governance and Model coupling are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cache keys include prompt/model/policy/tenant semantics and never cross authorization boundaries. owner, intended use, prohibited data/actions, approval, exception and retirement are auditable. a prompt version is qualified against specific model/tokenizer/provider capabilities and settings. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production PromptOps: prompt, template and policy lifecycle capability where Observability, Prompt asset and Prompt dataset are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prompt version, safe template ID, tokens, latency, route and evaluation join without logging sensitive rendered content. system/developer/user templates, variables, examples and output schema are versioned independently from application code when needed. expected tasks, edge cases, adversarial inputs and owner define regression evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SN-09

- [ ] **Question:** Design a production PromptOps: prompt, template and policy lifecycle capability where Rollback, Rendering and Change review are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: previous prompt and compatible model/tool schema remain deployable with fast traffic reversal. typed variables, escaping, length limits and deterministic template engine prevent malformed or injected structure. semantic diff explains instruction/order/example/policy changes beyond line-level text. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production PromptOps: prompt, template and policy lifecycle capability where Governance, Model coupling and Release are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: owner, intended use, prohibited data/actions, approval, exception and retirement are auditable. a prompt version is qualified against specific model/tokenizer/provider capabilities and settings. immutable prompt digest/alias follows shadow/canary and quality/safety/latency/cost gates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt asset. How do you lead it end to end?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff -- prompts/` as one read-only checkpoint, not the whole diagnosis. system/developer/user templates, variables, examples and output schema are versioned independently from application code when needed. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rendering. How do you lead it end to end?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/render_prompt.py --template prompts/support.yaml --fixture tests/fixture.json` as one read-only checkpoint, not the whole diagnosis. typed variables, escaping, length limits and deterministic template engine prevent malformed or injected structure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model coupling. How do you lead it end to end?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml --dataset prompt-regression.jsonl` as one read-only checkpoint, not the whole diagnosis. a prompt version is qualified against specific model/tokenizer/provider capabilities and settings. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt dataset. How do you lead it end to end?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `sha256sum prompts/support.yaml` as one read-only checkpoint, not the whole diagnosis. expected tasks, edge cases, adversarial inputs and owner define regression evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Change review. How do you lead it end to end?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff -- prompts/` as one read-only checkpoint, not the whole diagnosis. semantic diff explains instruction/order/example/policy changes beyond line-level text. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Release. How do you lead it end to end?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/render_prompt.py --template prompts/support.yaml --fixture tests/fixture.json` as one read-only checkpoint, not the whole diagnosis. immutable prompt digest/alias follows shadow/canary and quality/safety/latency/cost gates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Caching. How do you lead it end to end?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml --dataset prompt-regression.jsonl` as one read-only checkpoint, not the whole diagnosis. cache keys include prompt/model/policy/tenant semantics and never cross authorization boundaries. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Observability. How do you lead it end to end?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `sha256sum prompts/support.yaml` as one read-only checkpoint, not the whole diagnosis. prompt version, safe template ID, tokens, latency, route and evaluation join without logging sensitive rendered content. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rollback. How do you lead it end to end?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff -- prompts/` as one read-only checkpoint, not the whole diagnosis. previous prompt and compatible model/tool schema remain deployable with fast traffic reversal. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPTOPS-PROMPT-TEMPLATE-AND-POLICY-LIFECYCLE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Governance. How do you lead it end to end?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/render_prompt.py --template prompts/support.yaml --fixture tests/fixture.json` as one read-only checkpoint, not the whole diagnosis. owner, intended use, prohibited data/actions, approval, exception and retirement are auditable. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Retraining and feedback loops](../15-retraining-feedback-loops/README.md) · [Study note](README.md) · [Next: LLM fine-tuning, PEFT and adapter operations →](../17-llm-finetuning-peft/README.md)

<!-- reading-navigation:end -->
