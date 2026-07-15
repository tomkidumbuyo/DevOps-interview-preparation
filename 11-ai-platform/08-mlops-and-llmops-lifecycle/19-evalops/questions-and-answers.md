# EvalOps: continuous AI evaluation infrastructure — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JN-01

- [ ] **Question:** What is Evaluation contract, and why does it matter in EvalOps: continuous AI evaluation infrastructure?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** task, population, dataset, metric, evaluator, threshold and decision owner define what a score means. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JN-02

- [ ] **Question:** What is Golden dataset, and why does it matter in EvalOps: continuous AI evaluation infrastructure?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** versioned representative, edge, adversarial and previously failed cases have provenance and maintenance owners. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JN-03

- [ ] **Question:** What is Deterministic checks, and why does it matter in EvalOps: continuous AI evaluation infrastructure?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** schema, exact facts, executable tests, citations and policy assertions are preferred where possible. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JN-04

- [ ] **Question:** What is Model-as-judge, and why does it matter in EvalOps: continuous AI evaluation infrastructure?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** prompt/model/temperature/rubric/order bias and nondeterminism require calibration against human labels. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JN-05

- [ ] **Question:** What is Human evaluation, and why does it matter in EvalOps: continuous AI evaluation infrastructure?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** rubric, blinded/randomized assignment, agreement, adjudication and reviewer safety create evidence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JN-06

- [ ] **Question:** What is RAG decomposition, and why does it matter in EvalOps: continuous AI evaluation infrastructure?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** retrieval relevance/recall and answer faithfulness/quality are measured separately. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JN-07

- [ ] **Question:** What is Statistical comparison, and why does it matter in EvalOps: continuous AI evaluation infrastructure?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** uncertainty, paired tests, multiple slices and minimum practical effect prevent leaderboard overreaction. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JN-08

- [ ] **Code:** **Question:** What does `python scripts/compare_releases.py baseline.json candidate.json --paired` help you verify for EvalOps: continuous AI evaluation infrastructure?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: exact candidate/baseline evidence produces pass/fail/exception bound to immutable release.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JN-09

- [ ] **Code:** **Question:** What does `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` help you verify for EvalOps: continuous AI evaluation infrastructure?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: privacy-safe stratified traces and delayed outcomes detect realism gaps without uncontrolled retention.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JN-10

- [ ] **Code:** **Question:** What does `python -m pytest tests/evaluators -q` help you verify for EvalOps: continuous AI evaluation infrastructure?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: drift, judge/provider changes, cost/latency and disagreement are themselves observed.

## Junior — procedural and command questions

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JP-01

- [ ] **Code:** **Question:** A basic Evaluation contract check fails. What would you do first using the CLI?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` and capture exact status/reason/request ID. task, population, dataset, metric, evaluator, threshold and decision owner define what a score means. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JP-02

- [ ] **Question:** A basic Golden dataset check fails. What would you do first?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/evaluators -q` and capture exact status/reason/request ID. versioned representative, edge, adversarial and previously failed cases have provenance and maintenance owners. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JP-03

- [ ] **Question:** A basic Deterministic checks check fails. What would you do first?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/calibrate_judge.py --human labels.jsonl --judge results.jsonl` and capture exact status/reason/request ID. schema, exact facts, executable tests, citations and policy assertions are preferred where possible. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JP-04

- [ ] **Code:** **Question:** A basic Model-as-judge check fails. What would you do first using the CLI?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/compare_releases.py baseline.json candidate.json --paired` and capture exact status/reason/request ID. prompt/model/temperature/rubric/order bias and nondeterminism require calibration against human labels. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JP-05

- [ ] **Question:** A basic Human evaluation check fails. What would you do first?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` and capture exact status/reason/request ID. rubric, blinded/randomized assignment, agreement, adjudication and reviewer safety create evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JP-06

- [ ] **Question:** A basic RAG decomposition check fails. What would you do first?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/evaluators -q` and capture exact status/reason/request ID. retrieval relevance/recall and answer faithfulness/quality are measured separately. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JP-07

- [ ] **Code:** **Question:** A basic Statistical comparison check fails. What would you do first using the CLI?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/calibrate_judge.py --human labels.jsonl --judge results.jsonl` and capture exact status/reason/request ID. uncertainty, paired tests, multiple slices and minimum practical effect prevent leaderboard overreaction. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JP-08

- [ ] **Question:** A basic Release gate check fails. What would you do first?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/compare_releases.py baseline.json candidate.json --paired` and capture exact status/reason/request ID. exact candidate/baseline evidence produces pass/fail/exception bound to immutable release. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JP-09

- [ ] **Question:** A basic Production sampling check fails. What would you do first?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` and capture exact status/reason/request ID. privacy-safe stratified traces and delayed outcomes detect realism gaps without uncontrolled retention. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-JP-10

- [ ] **Code:** **Question:** A basic Evaluator monitoring check fails. What would you do first using the CLI?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/evaluators -q` and capture exact status/reason/request ID. drift, judge/provider changes, cost/latency and disagreement are themselves observed. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MN-01

- [ ] **Question:** Compare Evaluation contract with Golden dataset. When would each change your design?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Evaluation contract: task, population, dataset, metric, evaluator, threshold and decision owner define what a score means. Golden dataset: versioned representative, edge, adversarial and previously failed cases have provenance and maintenance owners. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MN-02

- [ ] **Question:** Compare Golden dataset with Deterministic checks. When would each change your design?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Golden dataset: versioned representative, edge, adversarial and previously failed cases have provenance and maintenance owners. Deterministic checks: schema, exact facts, executable tests, citations and policy assertions are preferred where possible. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MN-03

- [ ] **Question:** Compare Deterministic checks with Model-as-judge. When would each change your design?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Deterministic checks: schema, exact facts, executable tests, citations and policy assertions are preferred where possible. Model-as-judge: prompt/model/temperature/rubric/order bias and nondeterminism require calibration against human labels. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MN-04

- [ ] **Configuration review:** **Question:** Compare Model-as-judge with Human evaluation. When would each change your design?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Model-as-judge: prompt/model/temperature/rubric/order bias and nondeterminism require calibration against human labels. Human evaluation: rubric, blinded/randomized assignment, agreement, adjudication and reviewer safety create evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MN-05

- [ ] **Question:** Compare Human evaluation with RAG decomposition. When would each change your design?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Human evaluation: rubric, blinded/randomized assignment, agreement, adjudication and reviewer safety create evidence. RAG decomposition: retrieval relevance/recall and answer faithfulness/quality are measured separately. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MN-06

- [ ] **Question:** Compare RAG decomposition with Statistical comparison. When would each change your design?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** RAG decomposition: retrieval relevance/recall and answer faithfulness/quality are measured separately. Statistical comparison: uncertainty, paired tests, multiple slices and minimum practical effect prevent leaderboard overreaction. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MN-07

- [ ] **Configuration review:** **Question:** Compare Statistical comparison with Release gate. When would each change your design?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Statistical comparison: uncertainty, paired tests, multiple slices and minimum practical effect prevent leaderboard overreaction. Release gate: exact candidate/baseline evidence produces pass/fail/exception bound to immutable release. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MN-08

- [ ] **Question:** Compare Release gate with Production sampling. When would each change your design?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Release gate: exact candidate/baseline evidence produces pass/fail/exception bound to immutable release. Production sampling: privacy-safe stratified traces and delayed outcomes detect realism gaps without uncontrolled retention. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MN-09

- [ ] **Question:** Compare Production sampling with Evaluator monitoring. When would each change your design?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Production sampling: privacy-safe stratified traces and delayed outcomes detect realism gaps without uncontrolled retention. Evaluator monitoring: drift, judge/provider changes, cost/latency and disagreement are themselves observed. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MN-10

- [ ] **Configuration review:** **Question:** Compare Evaluator monitoring with Evaluation contract. When would each change your design?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Evaluator monitoring: drift, judge/provider changes, cost/latency and disagreement are themselves observed. Evaluation contract: task, population, dataset, metric, evaluator, threshold and decision owner define what a score means. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Evaluation contract; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` plus recent events/changes, then correlate the service-specific SLI. task, population, dataset, metric, evaluator, threshold and decision owner define what a score means. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MP-02

- [ ] **Question:** Production is degraded around Golden dataset; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/evaluators -q` plus recent events/changes, then correlate the service-specific SLI. versioned representative, edge, adversarial and previously failed cases have provenance and maintenance owners. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Deterministic checks; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/calibrate_judge.py --human labels.jsonl --judge results.jsonl` plus recent events/changes, then correlate the service-specific SLI. schema, exact facts, executable tests, citations and policy assertions are preferred where possible. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MP-04

- [ ] **Question:** Production is degraded around Model-as-judge; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/compare_releases.py baseline.json candidate.json --paired` plus recent events/changes, then correlate the service-specific SLI. prompt/model/temperature/rubric/order bias and nondeterminism require calibration against human labels. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Human evaluation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` plus recent events/changes, then correlate the service-specific SLI. rubric, blinded/randomized assignment, agreement, adjudication and reviewer safety create evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MP-06

- [ ] **Question:** Production is degraded around RAG decomposition; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/evaluators -q` plus recent events/changes, then correlate the service-specific SLI. retrieval relevance/recall and answer faithfulness/quality are measured separately. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Statistical comparison; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/calibrate_judge.py --human labels.jsonl --judge results.jsonl` plus recent events/changes, then correlate the service-specific SLI. uncertainty, paired tests, multiple slices and minimum practical effect prevent leaderboard overreaction. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MP-08

- [ ] **Question:** Production is degraded around Release gate; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/compare_releases.py baseline.json candidate.json --paired` plus recent events/changes, then correlate the service-specific SLI. exact candidate/baseline evidence produces pass/fail/exception bound to immutable release. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Production sampling; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` plus recent events/changes, then correlate the service-specific SLI. privacy-safe stratified traces and delayed outcomes detect realism gaps without uncontrolled retention. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-MP-10

- [ ] **Question:** Production is degraded around Evaluator monitoring; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/evaluators -q` plus recent events/changes, then correlate the service-specific SLI. drift, judge/provider changes, cost/latency and disagreement are themselves observed. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SN-01

- [ ] **Question:** Design a production EvalOps: continuous AI evaluation infrastructure capability where Evaluation contract, Model-as-judge and Statistical comparison are first-class requirements.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: task, population, dataset, metric, evaluator, threshold and decision owner define what a score means. prompt/model/temperature/rubric/order bias and nondeterminism require calibration against human labels. uncertainty, paired tests, multiple slices and minimum practical effect prevent leaderboard overreaction. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production EvalOps: continuous AI evaluation infrastructure capability where Golden dataset, Human evaluation and Release gate are first-class requirements.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versioned representative, edge, adversarial and previously failed cases have provenance and maintenance owners. rubric, blinded/randomized assignment, agreement, adjudication and reviewer safety create evidence. exact candidate/baseline evidence produces pass/fail/exception bound to immutable release. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SN-03

- [ ] **Question:** Design a production EvalOps: continuous AI evaluation infrastructure capability where Deterministic checks, RAG decomposition and Production sampling are first-class requirements.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: schema, exact facts, executable tests, citations and policy assertions are preferred where possible. retrieval relevance/recall and answer faithfulness/quality are measured separately. privacy-safe stratified traces and delayed outcomes detect realism gaps without uncontrolled retention. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production EvalOps: continuous AI evaluation infrastructure capability where Model-as-judge, Statistical comparison and Evaluator monitoring are first-class requirements.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prompt/model/temperature/rubric/order bias and nondeterminism require calibration against human labels. uncertainty, paired tests, multiple slices and minimum practical effect prevent leaderboard overreaction. drift, judge/provider changes, cost/latency and disagreement are themselves observed. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SN-05

- [ ] **Question:** Design a production EvalOps: continuous AI evaluation infrastructure capability where Human evaluation, Release gate and Evaluation contract are first-class requirements.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: rubric, blinded/randomized assignment, agreement, adjudication and reviewer safety create evidence. exact candidate/baseline evidence produces pass/fail/exception bound to immutable release. task, population, dataset, metric, evaluator, threshold and decision owner define what a score means. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production EvalOps: continuous AI evaluation infrastructure capability where RAG decomposition, Production sampling and Golden dataset are first-class requirements.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retrieval relevance/recall and answer faithfulness/quality are measured separately. privacy-safe stratified traces and delayed outcomes detect realism gaps without uncontrolled retention. versioned representative, edge, adversarial and previously failed cases have provenance and maintenance owners. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SN-07

- [ ] **Question:** Design a production EvalOps: continuous AI evaluation infrastructure capability where Statistical comparison, Evaluator monitoring and Deterministic checks are first-class requirements.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: uncertainty, paired tests, multiple slices and minimum practical effect prevent leaderboard overreaction. drift, judge/provider changes, cost/latency and disagreement are themselves observed. schema, exact facts, executable tests, citations and policy assertions are preferred where possible. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production EvalOps: continuous AI evaluation infrastructure capability where Release gate, Evaluation contract and Model-as-judge are first-class requirements.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exact candidate/baseline evidence produces pass/fail/exception bound to immutable release. task, population, dataset, metric, evaluator, threshold and decision owner define what a score means. prompt/model/temperature/rubric/order bias and nondeterminism require calibration against human labels. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SN-09

- [ ] **Question:** Design a production EvalOps: continuous AI evaluation infrastructure capability where Production sampling, Golden dataset and Human evaluation are first-class requirements.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: privacy-safe stratified traces and delayed outcomes detect realism gaps without uncontrolled retention. versioned representative, edge, adversarial and previously failed cases have provenance and maintenance owners. rubric, blinded/randomized assignment, agreement, adjudication and reviewer safety create evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production EvalOps: continuous AI evaluation infrastructure capability where Evaluator monitoring, Deterministic checks and RAG decomposition are first-class requirements.
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: drift, judge/provider changes, cost/latency and disagreement are themselves observed. schema, exact facts, executable tests, citations and policy assertions are preferred where possible. retrieval relevance/recall and answer faithfulness/quality are measured separately. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Evaluation contract. How do you lead it end to end?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` as one read-only checkpoint, not the whole diagnosis. task, population, dataset, metric, evaluator, threshold and decision owner define what a score means. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Golden dataset. How do you lead it end to end?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/evaluators -q` as one read-only checkpoint, not the whole diagnosis. versioned representative, edge, adversarial and previously failed cases have provenance and maintenance owners. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deterministic checks. How do you lead it end to end?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/calibrate_judge.py --human labels.jsonl --judge results.jsonl` as one read-only checkpoint, not the whole diagnosis. schema, exact facts, executable tests, citations and policy assertions are preferred where possible. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model-as-judge. How do you lead it end to end?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/compare_releases.py baseline.json candidate.json --paired` as one read-only checkpoint, not the whole diagnosis. prompt/model/temperature/rubric/order bias and nondeterminism require calibration against human labels. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Human evaluation. How do you lead it end to end?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` as one read-only checkpoint, not the whole diagnosis. rubric, blinded/randomized assignment, agreement, adjudication and reviewer safety create evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RAG decomposition. How do you lead it end to end?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/evaluators -q` as one read-only checkpoint, not the whole diagnosis. retrieval relevance/recall and answer faithfulness/quality are measured separately. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Statistical comparison. How do you lead it end to end?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/calibrate_judge.py --human labels.jsonl --judge results.jsonl` as one read-only checkpoint, not the whole diagnosis. uncertainty, paired tests, multiple slices and minimum practical effect prevent leaderboard overreaction. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Release gate. How do you lead it end to end?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/compare_releases.py baseline.json candidate.json --paired` as one read-only checkpoint, not the whole diagnosis. exact candidate/baseline evidence produces pass/fail/exception bound to immutable release. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Production sampling. How do you lead it end to end?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` as one read-only checkpoint, not the whole diagnosis. privacy-safe stratified traces and delayed outcomes detect realism gaps without uncontrolled retention. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EVALOPS-CONTINUOUS-AI-EVALUATION-INFRASTRUCTURE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Evaluator monitoring. How do you lead it end to end?
> **Covered in:** [EvalOps: continuous AI evaluation infrastructure — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/evaluators -q` as one read-only checkpoint, not the whole diagnosis. drift, judge/provider changes, cost/latency and disagreement are themselves observed. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: RAGOps and index lifecycle](../18-ragops-index-lifecycle/README.md) · [Study note](README.md) · [Next: LLM gateway and ProviderOps →](../20-gateway-providerops/README.md)

<!-- reading-navigation:end -->
