# AgentOps and tool-using system operations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JN-01

- [ ] **Question:** What is Run state machine, and why does it matter in AgentOps and tool-using system operations?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** queued/running/waiting-approval/succeeded/failed/canceled/compensating states survive worker restart. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JN-02

- [ ] **Question:** What is Tool contract, and why does it matter in AgentOps and tool-using system operations?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** typed input/output/error/idempotency/timeout and side-effect classification are versioned. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JN-03

- [ ] **Question:** What is Authorization, and why does it matter in AgentOps and tool-using system operations?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** user and workload identity plus current resource context authorize every call at execution time. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JN-04

- [ ] **Question:** What is Capability, and why does it matter in AgentOps and tool-using system operations?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** agent receives narrow short-lived tool/resource scope rather than ambient broad credentials. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JN-05

- [ ] **Question:** What is Idempotency, and why does it matter in AgentOps and tool-using system operations?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** stable operation key and result lookup handle timeout with unknown side effect. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JN-06

- [ ] **Question:** What is Approval, and why does it matter in AgentOps and tool-using system operations?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** high-risk proposed action includes diff/target/effect/evidence/expiry and revalidates after approval. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JN-07

- [ ] **Question:** What is Budgets, and why does it matter in AgentOps and tool-using system operations?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** steps, wall time, tokens, spend, retries and external calls bound loops and denial-of-wallet. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JN-08

- [ ] **Code:** **Question:** What does `opa eval --data policy --input proposed-tool-call.json 'data.tools.allow'` help you verify for AgentOps and tool-using system operations?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: generated code/browser/file/network operations run in isolated constrained environments.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JN-09

- [ ] **Code:** **Question:** What does `python -m pytest tests/agent_tools -q` help you verify for AgentOps and tool-using system operations?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: model/tool/policy/approval state transitions and safe arguments/results support replay and evaluation.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JN-10

- [ ] **Code:** **Question:** What does `python run_agent.py --fixture tests/task.json --max-steps 8 --dry-run` help you verify for AgentOps and tool-using system operations?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: task success, policy compliance, tool correctness, recovery, cost and adversarial behavior are release gates.

## Junior — procedural and command questions

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JP-01

- [ ] **Code:** **Question:** A basic Run state machine check fails. What would you do first using the CLI?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/agent_tools -q` and capture exact status/reason/request ID. queued/running/waiting-approval/succeeded/failed/canceled/compensating states survive worker restart. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JP-02

- [ ] **Question:** A basic Tool contract check fails. What would you do first?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python run_agent.py --fixture tests/task.json --max-steps 8 --dry-run` and capture exact status/reason/request ID. typed input/output/error/idempotency/timeout and side-effect classification are versioned. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JP-03

- [ ] **Question:** A basic Authorization check fails. What would you do first?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s AGENT_API/runs/RUN_ID | jq` and capture exact status/reason/request ID. user and workload identity plus current resource context authorize every call at execution time. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JP-04

- [ ] **Code:** **Question:** A basic Capability check fails. What would you do first using the CLI?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `opa eval --data policy --input proposed-tool-call.json 'data.tools.allow'` and capture exact status/reason/request ID. agent receives narrow short-lived tool/resource scope rather than ambient broad credentials. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JP-05

- [ ] **Question:** A basic Idempotency check fails. What would you do first?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/agent_tools -q` and capture exact status/reason/request ID. stable operation key and result lookup handle timeout with unknown side effect. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JP-06

- [ ] **Question:** A basic Approval check fails. What would you do first?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python run_agent.py --fixture tests/task.json --max-steps 8 --dry-run` and capture exact status/reason/request ID. high-risk proposed action includes diff/target/effect/evidence/expiry and revalidates after approval. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JP-07

- [ ] **Code:** **Question:** A basic Budgets check fails. What would you do first using the CLI?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s AGENT_API/runs/RUN_ID | jq` and capture exact status/reason/request ID. steps, wall time, tokens, spend, retries and external calls bound loops and denial-of-wallet. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JP-08

- [ ] **Question:** A basic Sandbox check fails. What would you do first?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `opa eval --data policy --input proposed-tool-call.json 'data.tools.allow'` and capture exact status/reason/request ID. generated code/browser/file/network operations run in isolated constrained environments. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JP-09

- [ ] **Question:** A basic Trace check fails. What would you do first?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/agent_tools -q` and capture exact status/reason/request ID. model/tool/policy/approval state transitions and safe arguments/results support replay and evaluation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-JP-10

- [ ] **Code:** **Question:** A basic Evaluation check fails. What would you do first using the CLI?
> **Covered in:** [AgentOps and tool-using system operations — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python run_agent.py --fixture tests/task.json --max-steps 8 --dry-run` and capture exact status/reason/request ID. task success, policy compliance, tool correctness, recovery, cost and adversarial behavior are release gates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MN-01

- [ ] **Question:** Compare Run state machine with Tool contract. When would each change your design?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Run state machine: queued/running/waiting-approval/succeeded/failed/canceled/compensating states survive worker restart. Tool contract: typed input/output/error/idempotency/timeout and side-effect classification are versioned. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MN-02

- [ ] **Question:** Compare Tool contract with Authorization. When would each change your design?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Tool contract: typed input/output/error/idempotency/timeout and side-effect classification are versioned. Authorization: user and workload identity plus current resource context authorize every call at execution time. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MN-03

- [ ] **Question:** Compare Authorization with Capability. When would each change your design?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Authorization: user and workload identity plus current resource context authorize every call at execution time. Capability: agent receives narrow short-lived tool/resource scope rather than ambient broad credentials. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Capability with Idempotency. When would each change your design?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Capability: agent receives narrow short-lived tool/resource scope rather than ambient broad credentials. Idempotency: stable operation key and result lookup handle timeout with unknown side effect. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MN-05

- [ ] **Question:** Compare Idempotency with Approval. When would each change your design?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Idempotency: stable operation key and result lookup handle timeout with unknown side effect. Approval: high-risk proposed action includes diff/target/effect/evidence/expiry and revalidates after approval. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MN-06

- [ ] **Question:** Compare Approval with Budgets. When would each change your design?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Approval: high-risk proposed action includes diff/target/effect/evidence/expiry and revalidates after approval. Budgets: steps, wall time, tokens, spend, retries and external calls bound loops and denial-of-wallet. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Budgets with Sandbox. When would each change your design?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Budgets: steps, wall time, tokens, spend, retries and external calls bound loops and denial-of-wallet. Sandbox: generated code/browser/file/network operations run in isolated constrained environments. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MN-08

- [ ] **Question:** Compare Sandbox with Trace. When would each change your design?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Sandbox: generated code/browser/file/network operations run in isolated constrained environments. Trace: model/tool/policy/approval state transitions and safe arguments/results support replay and evaluation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MN-09

- [ ] **Question:** Compare Trace with Evaluation. When would each change your design?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Trace: model/tool/policy/approval state transitions and safe arguments/results support replay and evaluation. Evaluation: task success, policy compliance, tool correctness, recovery, cost and adversarial behavior are release gates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Evaluation with Run state machine. When would each change your design?
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Evaluation: task success, policy compliance, tool correctness, recovery, cost and adversarial behavior are release gates. Run state machine: queued/running/waiting-approval/succeeded/failed/canceled/compensating states survive worker restart. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Run state machine; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/agent_tools -q` plus recent events/changes, then correlate the service-specific SLI. queued/running/waiting-approval/succeeded/failed/canceled/compensating states survive worker restart. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MP-02

- [ ] **Question:** Production is degraded around Tool contract; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python run_agent.py --fixture tests/task.json --max-steps 8 --dry-run` plus recent events/changes, then correlate the service-specific SLI. typed input/output/error/idempotency/timeout and side-effect classification are versioned. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Authorization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s AGENT_API/runs/RUN_ID | jq` plus recent events/changes, then correlate the service-specific SLI. user and workload identity plus current resource context authorize every call at execution time. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MP-04

- [ ] **Question:** Production is degraded around Capability; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `opa eval --data policy --input proposed-tool-call.json 'data.tools.allow'` plus recent events/changes, then correlate the service-specific SLI. agent receives narrow short-lived tool/resource scope rather than ambient broad credentials. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Idempotency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/agent_tools -q` plus recent events/changes, then correlate the service-specific SLI. stable operation key and result lookup handle timeout with unknown side effect. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MP-06

- [ ] **Question:** Production is degraded around Approval; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python run_agent.py --fixture tests/task.json --max-steps 8 --dry-run` plus recent events/changes, then correlate the service-specific SLI. high-risk proposed action includes diff/target/effect/evidence/expiry and revalidates after approval. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Budgets; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s AGENT_API/runs/RUN_ID | jq` plus recent events/changes, then correlate the service-specific SLI. steps, wall time, tokens, spend, retries and external calls bound loops and denial-of-wallet. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MP-08

- [ ] **Question:** Production is degraded around Sandbox; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `opa eval --data policy --input proposed-tool-call.json 'data.tools.allow'` plus recent events/changes, then correlate the service-specific SLI. generated code/browser/file/network operations run in isolated constrained environments. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Trace; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/agent_tools -q` plus recent events/changes, then correlate the service-specific SLI. model/tool/policy/approval state transitions and safe arguments/results support replay and evaluation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-MP-10

- [ ] **Question:** Production is degraded around Evaluation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python run_agent.py --fixture tests/task.json --max-steps 8 --dry-run` plus recent events/changes, then correlate the service-specific SLI. task success, policy compliance, tool correctness, recovery, cost and adversarial behavior are release gates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SN-01

- [ ] **Question:** Design a production AgentOps and tool-using system operations capability where Run state machine, Capability and Budgets are first-class requirements.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: queued/running/waiting-approval/succeeded/failed/canceled/compensating states survive worker restart. agent receives narrow short-lived tool/resource scope rather than ambient broad credentials. steps, wall time, tokens, spend, retries and external calls bound loops and denial-of-wallet. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AgentOps and tool-using system operations capability where Tool contract, Idempotency and Sandbox are first-class requirements.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: typed input/output/error/idempotency/timeout and side-effect classification are versioned. stable operation key and result lookup handle timeout with unknown side effect. generated code/browser/file/network operations run in isolated constrained environments. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SN-03

- [ ] **Question:** Design a production AgentOps and tool-using system operations capability where Authorization, Approval and Trace are first-class requirements.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: user and workload identity plus current resource context authorize every call at execution time. high-risk proposed action includes diff/target/effect/evidence/expiry and revalidates after approval. model/tool/policy/approval state transitions and safe arguments/results support replay and evaluation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AgentOps and tool-using system operations capability where Capability, Budgets and Evaluation are first-class requirements.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: agent receives narrow short-lived tool/resource scope rather than ambient broad credentials. steps, wall time, tokens, spend, retries and external calls bound loops and denial-of-wallet. task success, policy compliance, tool correctness, recovery, cost and adversarial behavior are release gates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SN-05

- [ ] **Question:** Design a production AgentOps and tool-using system operations capability where Idempotency, Sandbox and Run state machine are first-class requirements.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stable operation key and result lookup handle timeout with unknown side effect. generated code/browser/file/network operations run in isolated constrained environments. queued/running/waiting-approval/succeeded/failed/canceled/compensating states survive worker restart. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AgentOps and tool-using system operations capability where Approval, Trace and Tool contract are first-class requirements.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: high-risk proposed action includes diff/target/effect/evidence/expiry and revalidates after approval. model/tool/policy/approval state transitions and safe arguments/results support replay and evaluation. typed input/output/error/idempotency/timeout and side-effect classification are versioned. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SN-07

- [ ] **Question:** Design a production AgentOps and tool-using system operations capability where Budgets, Evaluation and Authorization are first-class requirements.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: steps, wall time, tokens, spend, retries and external calls bound loops and denial-of-wallet. task success, policy compliance, tool correctness, recovery, cost and adversarial behavior are release gates. user and workload identity plus current resource context authorize every call at execution time. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AgentOps and tool-using system operations capability where Sandbox, Run state machine and Capability are first-class requirements.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: generated code/browser/file/network operations run in isolated constrained environments. queued/running/waiting-approval/succeeded/failed/canceled/compensating states survive worker restart. agent receives narrow short-lived tool/resource scope rather than ambient broad credentials. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SN-09

- [ ] **Question:** Design a production AgentOps and tool-using system operations capability where Trace, Tool contract and Idempotency are first-class requirements.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model/tool/policy/approval state transitions and safe arguments/results support replay and evaluation. typed input/output/error/idempotency/timeout and side-effect classification are versioned. stable operation key and result lookup handle timeout with unknown side effect. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AgentOps and tool-using system operations capability where Evaluation, Authorization and Approval are first-class requirements.
> **Covered in:** [AgentOps and tool-using system operations — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: task success, policy compliance, tool correctness, recovery, cost and adversarial behavior are release gates. user and workload identity plus current resource context authorize every call at execution time. high-risk proposed action includes diff/target/effect/evidence/expiry and revalidates after approval. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Run state machine. How do you lead it end to end?
> **Covered in:** [AgentOps and tool-using system operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/agent_tools -q` as one read-only checkpoint, not the whole diagnosis. queued/running/waiting-approval/succeeded/failed/canceled/compensating states survive worker restart. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tool contract. How do you lead it end to end?
> **Covered in:** [AgentOps and tool-using system operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python run_agent.py --fixture tests/task.json --max-steps 8 --dry-run` as one read-only checkpoint, not the whole diagnosis. typed input/output/error/idempotency/timeout and side-effect classification are versioned. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authorization. How do you lead it end to end?
> **Covered in:** [AgentOps and tool-using system operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s AGENT_API/runs/RUN_ID | jq` as one read-only checkpoint, not the whole diagnosis. user and workload identity plus current resource context authorize every call at execution time. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Capability. How do you lead it end to end?
> **Covered in:** [AgentOps and tool-using system operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `opa eval --data policy --input proposed-tool-call.json 'data.tools.allow'` as one read-only checkpoint, not the whole diagnosis. agent receives narrow short-lived tool/resource scope rather than ambient broad credentials. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Idempotency. How do you lead it end to end?
> **Covered in:** [AgentOps and tool-using system operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/agent_tools -q` as one read-only checkpoint, not the whole diagnosis. stable operation key and result lookup handle timeout with unknown side effect. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Approval. How do you lead it end to end?
> **Covered in:** [AgentOps and tool-using system operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python run_agent.py --fixture tests/task.json --max-steps 8 --dry-run` as one read-only checkpoint, not the whole diagnosis. high-risk proposed action includes diff/target/effect/evidence/expiry and revalidates after approval. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Budgets. How do you lead it end to end?
> **Covered in:** [AgentOps and tool-using system operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s AGENT_API/runs/RUN_ID | jq` as one read-only checkpoint, not the whole diagnosis. steps, wall time, tokens, spend, retries and external calls bound loops and denial-of-wallet. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Sandbox. How do you lead it end to end?
> **Covered in:** [AgentOps and tool-using system operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `opa eval --data policy --input proposed-tool-call.json 'data.tools.allow'` as one read-only checkpoint, not the whole diagnosis. generated code/browser/file/network operations run in isolated constrained environments. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Trace. How do you lead it end to end?
> **Covered in:** [AgentOps and tool-using system operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/agent_tools -q` as one read-only checkpoint, not the whole diagnosis. model/tool/policy/approval state transitions and safe arguments/results support replay and evaluation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AGENTOPS-AND-TOOL-USING-SYSTEM-OPERATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Evaluation. How do you lead it end to end?
> **Covered in:** [AgentOps and tool-using system operations — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python run_agent.py --fixture tests/task.json --max-steps 8 --dry-run` as one read-only checkpoint, not the whole diagnosis. task success, policy compliance, tool correctness, recovery, cost and adversarial behavior are release gates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: LLM gateway and ProviderOps](../20-gateway-providerops/README.md) · [Study note](README.md) · [Next: LLM observability and quality telemetry →](../22-llm-observability/README.md)

<!-- reading-navigation:end -->
