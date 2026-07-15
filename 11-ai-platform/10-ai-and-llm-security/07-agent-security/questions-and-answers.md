# Agent security — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AGENT-SECURITY-JN-01

- [ ] **Question:** What is Excessive agency, and why does it matter in Agent security?
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENT-SECURITY-JN-02

- [ ] **Question:** What is Tool misuse, and why does it matter in Agent security?
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENT-SECURITY-JN-03

- [ ] **Question:** What is Credential misuse, and why does it matter in Agent security?
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENT-SECURITY-JN-04

- [ ] **Question:** What is Recursive actions, and why does it matter in Agent security?
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENT-SECURITY-JN-05

- [ ] **Question:** What is Resource exhaustion, and why does it matter in Agent security?
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENT-SECURITY-JN-06

- [ ] **Question:** What is Human-in-the-loop controls, and why does it matter in Agent security?
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENT-SECURITY-JN-07

- [ ] **Question:** What is Action allowlists, and why does it matter in Agent security?
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENT-SECURITY-JN-08

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for Agent security?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### AGENT-SECURITY-JN-09

- [ ] **Code:** **Question:** What does `nvidia-smi` help you verify for Agent security?
> **Covered in:** [Agent security — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### AGENT-SECURITY-JN-10

- [ ] **Code:** **Question:** What does `kubectl get pods -A -o wide` help you verify for Agent security?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### AGENT-SECURITY-JP-01

- [ ] **Code:** **Question:** A basic Excessive agency check fails. What would you do first using the CLI?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENT-SECURITY-JP-02

- [ ] **Question:** A basic Tool misuse check fails. What would you do first?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENT-SECURITY-JP-03

- [ ] **Question:** A basic Credential misuse check fails. What would you do first?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENT-SECURITY-JP-04

- [ ] **Code:** **Question:** A basic Recursive actions check fails. What would you do first using the CLI?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENT-SECURITY-JP-05

- [ ] **Question:** A basic Resource exhaustion check fails. What would you do first?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENT-SECURITY-JP-06

- [ ] **Question:** A basic Human-in-the-loop controls check fails. What would you do first?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENT-SECURITY-JP-07

- [ ] **Code:** **Question:** A basic Action allowlists check fails. What would you do first using the CLI?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENT-SECURITY-JP-08

- [ ] **Question:** A basic Excessive agency check fails. What would you do first?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENT-SECURITY-JP-09

- [ ] **Question:** A basic Tool misuse check fails. What would you do first?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENT-SECURITY-JP-10

- [ ] **Code:** **Question:** A basic Credential misuse check fails. What would you do first using the CLI?
> **Covered in:** [Agent security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AGENT-SECURITY-MN-01

- [ ] **Question:** Compare Excessive agency with Tool misuse. When would each change your design?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Excessive agency: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Tool misuse: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENT-SECURITY-MN-02

- [ ] **Question:** Compare Tool misuse with Credential misuse. When would each change your design?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Tool misuse: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Credential misuse: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENT-SECURITY-MN-03

- [ ] **Question:** Compare Credential misuse with Recursive actions. When would each change your design?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Credential misuse: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Recursive actions: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENT-SECURITY-MN-04

- [ ] **Configuration review:** **Question:** Compare Recursive actions with Resource exhaustion. When would each change your design?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Recursive actions: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Resource exhaustion: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENT-SECURITY-MN-05

- [ ] **Question:** Compare Resource exhaustion with Human-in-the-loop controls. When would each change your design?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Resource exhaustion: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Human-in-the-loop controls: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENT-SECURITY-MN-06

- [ ] **Question:** Compare Human-in-the-loop controls with Action allowlists. When would each change your design?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Human-in-the-loop controls: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Action allowlists: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENT-SECURITY-MN-07

- [ ] **Configuration review:** **Question:** Compare Action allowlists with Excessive agency. When would each change your design?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Action allowlists: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Excessive agency: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENT-SECURITY-MN-08

- [ ] **Question:** Compare Excessive agency with Tool misuse. When would each change your design?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Excessive agency: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Tool misuse: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENT-SECURITY-MN-09

- [ ] **Question:** Compare Tool misuse with Credential misuse. When would each change your design?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Tool misuse: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Credential misuse: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENT-SECURITY-MN-10

- [ ] **Configuration review:** **Question:** Compare Credential misuse with Excessive agency. When would each change your design?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Credential misuse: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Excessive agency: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AGENT-SECURITY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Excessive agency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENT-SECURITY-MP-02

- [ ] **Question:** Production is degraded around Tool misuse; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENT-SECURITY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Credential misuse; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENT-SECURITY-MP-04

- [ ] **Question:** Production is degraded around Recursive actions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENT-SECURITY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Resource exhaustion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENT-SECURITY-MP-06

- [ ] **Question:** Production is degraded around Human-in-the-loop controls; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENT-SECURITY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Action allowlists; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENT-SECURITY-MP-08

- [ ] **Question:** Production is degraded around Excessive agency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENT-SECURITY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Tool misuse; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENT-SECURITY-MP-10

- [ ] **Question:** Production is degraded around Credential misuse; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AGENT-SECURITY-SN-01

- [ ] **Question:** Design a production Agent security capability where Excessive agency, Recursive actions and Action allowlists are first-class requirements.
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENT-SECURITY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Agent security capability where Tool misuse, Resource exhaustion and Excessive agency are first-class requirements.
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENT-SECURITY-SN-03

- [ ] **Question:** Design a production Agent security capability where Credential misuse, Human-in-the-loop controls and Tool misuse are first-class requirements.
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENT-SECURITY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Agent security capability where Recursive actions, Action allowlists and Credential misuse are first-class requirements.
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENT-SECURITY-SN-05

- [ ] **Question:** Design a production Agent security capability where Resource exhaustion, Excessive agency and Excessive agency are first-class requirements.
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENT-SECURITY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Agent security capability where Human-in-the-loop controls, Tool misuse and Tool misuse are first-class requirements.
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENT-SECURITY-SN-07

- [ ] **Question:** Design a production Agent security capability where Action allowlists, Credential misuse and Credential misuse are first-class requirements.
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENT-SECURITY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Agent security capability where Excessive agency, Excessive agency and Recursive actions are first-class requirements.
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENT-SECURITY-SN-09

- [ ] **Question:** Design a production Agent security capability where Tool misuse, Tool misuse and Resource exhaustion are first-class requirements.
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENT-SECURITY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Agent security capability where Credential misuse, Credential misuse and Human-in-the-loop controls are first-class requirements.
> **Covered in:** [Agent security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AGENT-SECURITY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Excessive agency. How do you lead it end to end?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENT-SECURITY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tool misuse. How do you lead it end to end?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENT-SECURITY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Credential misuse. How do you lead it end to end?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENT-SECURITY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Recursive actions. How do you lead it end to end?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENT-SECURITY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource exhaustion. How do you lead it end to end?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENT-SECURITY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Human-in-the-loop controls. How do you lead it end to end?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENT-SECURITY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Action allowlists. How do you lead it end to end?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENT-SECURITY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Excessive agency. How do you lead it end to end?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENT-SECURITY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tool misuse. How do you lead it end to end?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENT-SECURITY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Credential misuse. How do you lead it end to end?
> **Covered in:** [Agent security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Agent security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: RAG security](../06-rag-security/README.md) · [Study note](README.md) · [Next: AI supply chain →](../08-ai-supply-chain/README.md)

<!-- reading-navigation:end -->
