# Model validation and release gates — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### MODEL-VALIDATION-AND-RELEASE-GATES-JN-01

- [ ] **Question:** What is Candidate manifest, and why does it matter in Model validation and release gates?

**Answer:** exact release identity prevents evaluation result being attached to different bytes/config. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-VALIDATION-AND-RELEASE-GATES-JN-02

- [ ] **Question:** What is Baseline, and why does it matter in Model validation and release gates?

**Answer:** compare with current champion and explicit acceptance bands instead of an isolated candidate score. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-VALIDATION-AND-RELEASE-GATES-JN-03

- [ ] **Question:** What is Slice tests, and why does it matter in Model validation and release gates?

**Answer:** tenant/language/region/demographic/edge/adversarial slices reveal regressions hidden by averages. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-VALIDATION-AND-RELEASE-GATES-JN-04

- [ ] **Question:** What is Statistical test, and why does it matter in Model validation and release gates?

**Answer:** uncertainty, sample size, multiple comparisons and practical effect size bound decisions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-VALIDATION-AND-RELEASE-GATES-JN-05

- [ ] **Question:** What is Safety evaluation, and why does it matter in Model validation and release gates?

**Answer:** harmful content, privacy leakage, jailbreak and tool behavior require task-specific tests. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-VALIDATION-AND-RELEASE-GATES-JN-06

- [ ] **Question:** What is Performance qualification, and why does it matter in Model validation and release gates?

**Answer:** latency/throughput/memory under target hardware and workload distribution is part of validation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-VALIDATION-AND-RELEASE-GATES-JN-07

- [ ] **Question:** What is Security scan, and why does it matter in Model validation and release gates?

**Answer:** dependencies, unsafe artifact formats, signatures, licenses and model-source trust are checked. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-VALIDATION-AND-RELEASE-GATES-JN-08

- [ ] **Code:** **Question:** What does `opa eval --data policy --input release-evidence.json 'data.release.allow'` help you verify for Model validation and release gates?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: machine-readable pass/fail/warn with evidence links still has risk owner and exception process.

### MODEL-VALIDATION-AND-RELEASE-GATES-JN-09

- [ ] **Code:** **Question:** What does `python -m pytest tests/model_validation -q` help you verify for Model validation and release gates?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: actor, reason, evidence set, target scope, time/expiry and rollback authority are recorded.

### MODEL-VALIDATION-AND-RELEASE-GATES-JN-10

- [ ] **Code:** **Question:** What does `python -m evals.run --manifest release.yaml --dataset golden.jsonl` help you verify for Model validation and release gates?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: gate result must bind exact commit/artifact and expire if dependencies or target policy change.

## Junior — procedural and command questions

### MODEL-VALIDATION-AND-RELEASE-GATES-JP-01

- [ ] **Code:** **Question:** A basic Candidate manifest check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/model_validation -q` and capture exact status/reason/request ID. exact release identity prevents evaluation result being attached to different bytes/config. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-VALIDATION-AND-RELEASE-GATES-JP-02

- [ ] **Question:** A basic Baseline check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml --dataset golden.jsonl` and capture exact status/reason/request ID. compare with current champion and explicit acceptance bands instead of an isolated candidate score. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-VALIDATION-AND-RELEASE-GATES-JP-03

- [ ] **Question:** A basic Slice tests check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cosign verify MODEL_REF` and capture exact status/reason/request ID. tenant/language/region/demographic/edge/adversarial slices reveal regressions hidden by averages. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-VALIDATION-AND-RELEASE-GATES-JP-04

- [ ] **Code:** **Question:** A basic Statistical test check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `opa eval --data policy --input release-evidence.json 'data.release.allow'` and capture exact status/reason/request ID. uncertainty, sample size, multiple comparisons and practical effect size bound decisions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-VALIDATION-AND-RELEASE-GATES-JP-05

- [ ] **Question:** A basic Safety evaluation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/model_validation -q` and capture exact status/reason/request ID. harmful content, privacy leakage, jailbreak and tool behavior require task-specific tests. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-VALIDATION-AND-RELEASE-GATES-JP-06

- [ ] **Question:** A basic Performance qualification check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml --dataset golden.jsonl` and capture exact status/reason/request ID. latency/throughput/memory under target hardware and workload distribution is part of validation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-VALIDATION-AND-RELEASE-GATES-JP-07

- [ ] **Code:** **Question:** A basic Security scan check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cosign verify MODEL_REF` and capture exact status/reason/request ID. dependencies, unsafe artifact formats, signatures, licenses and model-source trust are checked. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-VALIDATION-AND-RELEASE-GATES-JP-08

- [ ] **Question:** A basic Policy decision check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `opa eval --data policy --input release-evidence.json 'data.release.allow'` and capture exact status/reason/request ID. machine-readable pass/fail/warn with evidence links still has risk owner and exception process. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-VALIDATION-AND-RELEASE-GATES-JP-09

- [ ] **Question:** A basic Approval check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/model_validation -q` and capture exact status/reason/request ID. actor, reason, evidence set, target scope, time/expiry and rollback authority are recorded. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-VALIDATION-AND-RELEASE-GATES-JP-10

- [ ] **Code:** **Question:** A basic Promotion race check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml --dataset golden.jsonl` and capture exact status/reason/request ID. gate result must bind exact commit/artifact and expire if dependencies or target policy change. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### MODEL-VALIDATION-AND-RELEASE-GATES-MN-01

- [ ] **Question:** Compare Candidate manifest with Baseline. When would each change your design?

**Answer:** Candidate manifest: exact release identity prevents evaluation result being attached to different bytes/config. Baseline: compare with current champion and explicit acceptance bands instead of an isolated candidate score. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-VALIDATION-AND-RELEASE-GATES-MN-02

- [ ] **Question:** Compare Baseline with Slice tests. When would each change your design?

**Answer:** Baseline: compare with current champion and explicit acceptance bands instead of an isolated candidate score. Slice tests: tenant/language/region/demographic/edge/adversarial slices reveal regressions hidden by averages. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-VALIDATION-AND-RELEASE-GATES-MN-03

- [ ] **Question:** Compare Slice tests with Statistical test. When would each change your design?

**Answer:** Slice tests: tenant/language/region/demographic/edge/adversarial slices reveal regressions hidden by averages. Statistical test: uncertainty, sample size, multiple comparisons and practical effect size bound decisions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-VALIDATION-AND-RELEASE-GATES-MN-04

- [ ] **Configuration review:** **Question:** Compare Statistical test with Safety evaluation. When would each change your design?

**Answer:** Statistical test: uncertainty, sample size, multiple comparisons and practical effect size bound decisions. Safety evaluation: harmful content, privacy leakage, jailbreak and tool behavior require task-specific tests. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-VALIDATION-AND-RELEASE-GATES-MN-05

- [ ] **Question:** Compare Safety evaluation with Performance qualification. When would each change your design?

**Answer:** Safety evaluation: harmful content, privacy leakage, jailbreak and tool behavior require task-specific tests. Performance qualification: latency/throughput/memory under target hardware and workload distribution is part of validation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-VALIDATION-AND-RELEASE-GATES-MN-06

- [ ] **Question:** Compare Performance qualification with Security scan. When would each change your design?

**Answer:** Performance qualification: latency/throughput/memory under target hardware and workload distribution is part of validation. Security scan: dependencies, unsafe artifact formats, signatures, licenses and model-source trust are checked. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-VALIDATION-AND-RELEASE-GATES-MN-07

- [ ] **Configuration review:** **Question:** Compare Security scan with Policy decision. When would each change your design?

**Answer:** Security scan: dependencies, unsafe artifact formats, signatures, licenses and model-source trust are checked. Policy decision: machine-readable pass/fail/warn with evidence links still has risk owner and exception process. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-VALIDATION-AND-RELEASE-GATES-MN-08

- [ ] **Question:** Compare Policy decision with Approval. When would each change your design?

**Answer:** Policy decision: machine-readable pass/fail/warn with evidence links still has risk owner and exception process. Approval: actor, reason, evidence set, target scope, time/expiry and rollback authority are recorded. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-VALIDATION-AND-RELEASE-GATES-MN-09

- [ ] **Question:** Compare Approval with Promotion race. When would each change your design?

**Answer:** Approval: actor, reason, evidence set, target scope, time/expiry and rollback authority are recorded. Promotion race: gate result must bind exact commit/artifact and expire if dependencies or target policy change. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-VALIDATION-AND-RELEASE-GATES-MN-10

- [ ] **Configuration review:** **Question:** Compare Promotion race with Candidate manifest. When would each change your design?

**Answer:** Promotion race: gate result must bind exact commit/artifact and expire if dependencies or target policy change. Candidate manifest: exact release identity prevents evaluation result being attached to different bytes/config. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### MODEL-VALIDATION-AND-RELEASE-GATES-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Candidate manifest; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/model_validation -q` plus recent events/changes, then correlate the service-specific SLI. exact release identity prevents evaluation result being attached to different bytes/config. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-VALIDATION-AND-RELEASE-GATES-MP-02

- [ ] **Question:** Production is degraded around Baseline; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml --dataset golden.jsonl` plus recent events/changes, then correlate the service-specific SLI. compare with current champion and explicit acceptance bands instead of an isolated candidate score. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-VALIDATION-AND-RELEASE-GATES-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Slice tests; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cosign verify MODEL_REF` plus recent events/changes, then correlate the service-specific SLI. tenant/language/region/demographic/edge/adversarial slices reveal regressions hidden by averages. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-VALIDATION-AND-RELEASE-GATES-MP-04

- [ ] **Question:** Production is degraded around Statistical test; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `opa eval --data policy --input release-evidence.json 'data.release.allow'` plus recent events/changes, then correlate the service-specific SLI. uncertainty, sample size, multiple comparisons and practical effect size bound decisions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-VALIDATION-AND-RELEASE-GATES-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Safety evaluation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/model_validation -q` plus recent events/changes, then correlate the service-specific SLI. harmful content, privacy leakage, jailbreak and tool behavior require task-specific tests. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-VALIDATION-AND-RELEASE-GATES-MP-06

- [ ] **Question:** Production is degraded around Performance qualification; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml --dataset golden.jsonl` plus recent events/changes, then correlate the service-specific SLI. latency/throughput/memory under target hardware and workload distribution is part of validation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-VALIDATION-AND-RELEASE-GATES-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Security scan; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cosign verify MODEL_REF` plus recent events/changes, then correlate the service-specific SLI. dependencies, unsafe artifact formats, signatures, licenses and model-source trust are checked. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-VALIDATION-AND-RELEASE-GATES-MP-08

- [ ] **Question:** Production is degraded around Policy decision; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `opa eval --data policy --input release-evidence.json 'data.release.allow'` plus recent events/changes, then correlate the service-specific SLI. machine-readable pass/fail/warn with evidence links still has risk owner and exception process. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-VALIDATION-AND-RELEASE-GATES-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Approval; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/model_validation -q` plus recent events/changes, then correlate the service-specific SLI. actor, reason, evidence set, target scope, time/expiry and rollback authority are recorded. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-VALIDATION-AND-RELEASE-GATES-MP-10

- [ ] **Question:** Production is degraded around Promotion race; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml --dataset golden.jsonl` plus recent events/changes, then correlate the service-specific SLI. gate result must bind exact commit/artifact and expire if dependencies or target policy change. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### MODEL-VALIDATION-AND-RELEASE-GATES-SN-01

- [ ] **Question:** Design a production Model validation and release gates capability where Candidate manifest, Statistical test and Security scan are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exact release identity prevents evaluation result being attached to different bytes/config. uncertainty, sample size, multiple comparisons and practical effect size bound decisions. dependencies, unsafe artifact formats, signatures, licenses and model-source trust are checked. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-VALIDATION-AND-RELEASE-GATES-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Model validation and release gates capability where Baseline, Safety evaluation and Policy decision are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: compare with current champion and explicit acceptance bands instead of an isolated candidate score. harmful content, privacy leakage, jailbreak and tool behavior require task-specific tests. machine-readable pass/fail/warn with evidence links still has risk owner and exception process. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-VALIDATION-AND-RELEASE-GATES-SN-03

- [ ] **Question:** Design a production Model validation and release gates capability where Slice tests, Performance qualification and Approval are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tenant/language/region/demographic/edge/adversarial slices reveal regressions hidden by averages. latency/throughput/memory under target hardware and workload distribution is part of validation. actor, reason, evidence set, target scope, time/expiry and rollback authority are recorded. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-VALIDATION-AND-RELEASE-GATES-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Model validation and release gates capability where Statistical test, Security scan and Promotion race are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: uncertainty, sample size, multiple comparisons and practical effect size bound decisions. dependencies, unsafe artifact formats, signatures, licenses and model-source trust are checked. gate result must bind exact commit/artifact and expire if dependencies or target policy change. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-VALIDATION-AND-RELEASE-GATES-SN-05

- [ ] **Question:** Design a production Model validation and release gates capability where Safety evaluation, Policy decision and Candidate manifest are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: harmful content, privacy leakage, jailbreak and tool behavior require task-specific tests. machine-readable pass/fail/warn with evidence links still has risk owner and exception process. exact release identity prevents evaluation result being attached to different bytes/config. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-VALIDATION-AND-RELEASE-GATES-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Model validation and release gates capability where Performance qualification, Approval and Baseline are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: latency/throughput/memory under target hardware and workload distribution is part of validation. actor, reason, evidence set, target scope, time/expiry and rollback authority are recorded. compare with current champion and explicit acceptance bands instead of an isolated candidate score. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-VALIDATION-AND-RELEASE-GATES-SN-07

- [ ] **Question:** Design a production Model validation and release gates capability where Security scan, Promotion race and Slice tests are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: dependencies, unsafe artifact formats, signatures, licenses and model-source trust are checked. gate result must bind exact commit/artifact and expire if dependencies or target policy change. tenant/language/region/demographic/edge/adversarial slices reveal regressions hidden by averages. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-VALIDATION-AND-RELEASE-GATES-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Model validation and release gates capability where Policy decision, Candidate manifest and Statistical test are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: machine-readable pass/fail/warn with evidence links still has risk owner and exception process. exact release identity prevents evaluation result being attached to different bytes/config. uncertainty, sample size, multiple comparisons and practical effect size bound decisions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-VALIDATION-AND-RELEASE-GATES-SN-09

- [ ] **Question:** Design a production Model validation and release gates capability where Approval, Baseline and Safety evaluation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: actor, reason, evidence set, target scope, time/expiry and rollback authority are recorded. compare with current champion and explicit acceptance bands instead of an isolated candidate score. harmful content, privacy leakage, jailbreak and tool behavior require task-specific tests. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-VALIDATION-AND-RELEASE-GATES-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Model validation and release gates capability where Promotion race, Slice tests and Performance qualification are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: gate result must bind exact commit/artifact and expire if dependencies or target policy change. tenant/language/region/demographic/edge/adversarial slices reveal regressions hidden by averages. latency/throughput/memory under target hardware and workload distribution is part of validation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### MODEL-VALIDATION-AND-RELEASE-GATES-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Candidate manifest. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/model_validation -q` as one read-only checkpoint, not the whole diagnosis. exact release identity prevents evaluation result being attached to different bytes/config. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-VALIDATION-AND-RELEASE-GATES-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Baseline. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml --dataset golden.jsonl` as one read-only checkpoint, not the whole diagnosis. compare with current champion and explicit acceptance bands instead of an isolated candidate score. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-VALIDATION-AND-RELEASE-GATES-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Slice tests. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cosign verify MODEL_REF` as one read-only checkpoint, not the whole diagnosis. tenant/language/region/demographic/edge/adversarial slices reveal regressions hidden by averages. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-VALIDATION-AND-RELEASE-GATES-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Statistical test. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `opa eval --data policy --input release-evidence.json 'data.release.allow'` as one read-only checkpoint, not the whole diagnosis. uncertainty, sample size, multiple comparisons and practical effect size bound decisions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-VALIDATION-AND-RELEASE-GATES-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Safety evaluation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/model_validation -q` as one read-only checkpoint, not the whole diagnosis. harmful content, privacy leakage, jailbreak and tool behavior require task-specific tests. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-VALIDATION-AND-RELEASE-GATES-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Performance qualification. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml --dataset golden.jsonl` as one read-only checkpoint, not the whole diagnosis. latency/throughput/memory under target hardware and workload distribution is part of validation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-VALIDATION-AND-RELEASE-GATES-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Security scan. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cosign verify MODEL_REF` as one read-only checkpoint, not the whole diagnosis. dependencies, unsafe artifact formats, signatures, licenses and model-source trust are checked. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-VALIDATION-AND-RELEASE-GATES-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Policy decision. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `opa eval --data policy --input release-evidence.json 'data.release.allow'` as one read-only checkpoint, not the whole diagnosis. machine-readable pass/fail/warn with evidence links still has risk owner and exception process. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-VALIDATION-AND-RELEASE-GATES-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Approval. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/model_validation -q` as one read-only checkpoint, not the whole diagnosis. actor, reason, evidence set, target scope, time/expiry and rollback authority are recorded. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-VALIDATION-AND-RELEASE-GATES-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Promotion race. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml --dataset golden.jsonl` as one read-only checkpoint, not the whole diagnosis. gate result must bind exact commit/artifact and expire if dependencies or target policy change. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
