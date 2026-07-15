# Gateway observability — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### GATEWAY-OBSERVABILITY-JN-01

- [ ] **Question:** What is Request count, and why does it matter in Gateway observability?
> **Covered in:** [Gateway observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-OBSERVABILITY-JN-02

- [ ] **Question:** What is Provider, and why does it matter in Gateway observability?
> **Covered in:** [Gateway observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-OBSERVABILITY-JN-03

- [ ] **Question:** What is Model, and why does it matter in Gateway observability?
> **Covered in:** [Gateway observability — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-OBSERVABILITY-JN-04

- [ ] **Question:** What is Tokens, and why does it matter in Gateway observability?
> **Covered in:** [Gateway observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-OBSERVABILITY-JN-05

- [ ] **Question:** What is Latency, and why does it matter in Gateway observability?
> **Covered in:** [Gateway observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-OBSERVABILITY-JN-06

- [ ] **Question:** What is Time to first token, and why does it matter in Gateway observability?
> **Covered in:** [Gateway observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-OBSERVABILITY-JN-07

- [ ] **Question:** What is Errors, and why does it matter in Gateway observability?
> **Covered in:** [Gateway observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-OBSERVABILITY-JN-08

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for Gateway observability?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms.

### GATEWAY-OBSERVABILITY-JN-09

- [ ] **Code:** **Question:** What does `nvidia-smi` help you verify for Gateway observability?
> **Covered in:** [Gateway observability — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### GATEWAY-OBSERVABILITY-JN-10

- [ ] **Code:** **Question:** What does `kubectl get pods -A -o wide` help you verify for Gateway observability?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### GATEWAY-OBSERVABILITY-JP-01

- [ ] **Code:** **Question:** A basic Request count check fails. What would you do first using the CLI?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-OBSERVABILITY-JP-02

- [ ] **Question:** A basic Provider check fails. What would you do first?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-OBSERVABILITY-JP-03

- [ ] **Question:** A basic Model check fails. What would you do first?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-OBSERVABILITY-JP-04

- [ ] **Code:** **Question:** A basic Tokens check fails. What would you do first using the CLI?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-OBSERVABILITY-JP-05

- [ ] **Question:** A basic Latency check fails. What would you do first?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-OBSERVABILITY-JP-06

- [ ] **Question:** A basic Time to first token check fails. What would you do first?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-OBSERVABILITY-JP-07

- [ ] **Code:** **Question:** A basic Errors check fails. What would you do first using the CLI?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-OBSERVABILITY-JP-08

- [ ] **Question:** A basic Retries check fails. What would you do first?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-OBSERVABILITY-JP-09

- [ ] **Question:** A basic Fallbacks check fails. What would you do first?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-OBSERVABILITY-JP-10

- [ ] **Code:** **Question:** A basic Cache hits check fails. What would you do first using the CLI?
> **Covered in:** [Gateway observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### GATEWAY-OBSERVABILITY-MN-01

- [ ] **Question:** Compare Request count with Provider. When would each change your design?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Request count: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Provider: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-OBSERVABILITY-MN-02

- [ ] **Question:** Compare Provider with Model. When would each change your design?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Provider: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Model: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-OBSERVABILITY-MN-03

- [ ] **Question:** Compare Model with Tokens. When would each change your design?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Model: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Tokens: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-OBSERVABILITY-MN-04

- [ ] **Configuration review:** **Question:** Compare Tokens with Latency. When would each change your design?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Tokens: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Latency: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-OBSERVABILITY-MN-05

- [ ] **Question:** Compare Latency with Time to first token. When would each change your design?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Latency: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Time to first token: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-OBSERVABILITY-MN-06

- [ ] **Question:** Compare Time to first token with Errors. When would each change your design?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Time to first token: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Errors: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-OBSERVABILITY-MN-07

- [ ] **Configuration review:** **Question:** Compare Errors with Retries. When would each change your design?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Errors: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Retries: repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-OBSERVABILITY-MN-08

- [ ] **Question:** Compare Retries with Fallbacks. When would each change your design?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Retries: repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Fallbacks: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-OBSERVABILITY-MN-09

- [ ] **Question:** Compare Fallbacks with Cache hits. When would each change your design?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Fallbacks: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Cache hits: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-OBSERVABILITY-MN-10

- [ ] **Configuration review:** **Question:** Compare Cache hits with Request count. When would each change your design?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Cache hits: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Request count: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### GATEWAY-OBSERVABILITY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Request count; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-OBSERVABILITY-MP-02

- [ ] **Question:** Production is degraded around Provider; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-OBSERVABILITY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway observability — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-OBSERVABILITY-MP-04

- [ ] **Question:** Production is degraded around Tokens; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-OBSERVABILITY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Latency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-OBSERVABILITY-MP-06

- [ ] **Question:** Production is degraded around Time to first token; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-OBSERVABILITY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Errors; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-OBSERVABILITY-MP-08

- [ ] **Question:** Production is degraded around Retries; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-OBSERVABILITY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Fallbacks; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-OBSERVABILITY-MP-10

- [ ] **Question:** Production is degraded around Cache hits; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### GATEWAY-OBSERVABILITY-SN-01

- [ ] **Question:** Design a production Gateway observability capability where Request count, Tokens and Errors are first-class requirements.
> **Covered in:** [Gateway observability — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-OBSERVABILITY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Gateway observability capability where Provider, Latency and Retries are first-class requirements.
> **Covered in:** [Gateway observability — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-OBSERVABILITY-SN-03

- [ ] **Question:** Design a production Gateway observability capability where Model, Time to first token and Fallbacks are first-class requirements.
> **Covered in:** [Gateway observability — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-OBSERVABILITY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Gateway observability capability where Tokens, Errors and Cache hits are first-class requirements.
> **Covered in:** [Gateway observability — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-OBSERVABILITY-SN-05

- [ ] **Question:** Design a production Gateway observability capability where Latency, Retries and Request count are first-class requirements.
> **Covered in:** [Gateway observability — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-OBSERVABILITY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Gateway observability capability where Time to first token, Fallbacks and Provider are first-class requirements.
> **Covered in:** [Gateway observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-OBSERVABILITY-SN-07

- [ ] **Question:** Design a production Gateway observability capability where Errors, Cache hits and Model are first-class requirements.
> **Covered in:** [Gateway observability — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-OBSERVABILITY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Gateway observability capability where Retries, Request count and Tokens are first-class requirements.
> **Covered in:** [Gateway observability — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-OBSERVABILITY-SN-09

- [ ] **Question:** Design a production Gateway observability capability where Fallbacks, Provider and Latency are first-class requirements.
> **Covered in:** [Gateway observability — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-OBSERVABILITY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Gateway observability capability where Cache hits, Model and Time to first token are first-class requirements.
> **Covered in:** [Gateway observability — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### GATEWAY-OBSERVABILITY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Request count. How do you lead it end to end?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-OBSERVABILITY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Provider. How do you lead it end to end?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-OBSERVABILITY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model. How do you lead it end to end?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-OBSERVABILITY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tokens. How do you lead it end to end?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-OBSERVABILITY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Latency. How do you lead it end to end?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-OBSERVABILITY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Time to first token. How do you lead it end to end?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-OBSERVABILITY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Errors. How do you lead it end to end?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-OBSERVABILITY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retries. How do you lead it end to end?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-OBSERVABILITY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Fallbacks. How do you lead it end to end?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-OBSERVABILITY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cache hits. How do you lead it end to end?
> **Covered in:** [Gateway observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Gateway observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Cost management](../09-cost-management/README.md) · [Study note](README.md) · [Next: Gateway technologies →](../11-gateway-technologies/README.md)

<!-- reading-navigation:end -->
