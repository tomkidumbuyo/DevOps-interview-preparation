# AI governance, approval and evidence automation — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JN-01

- [ ] **Question:** What is AI inventory, and why does it matter in AI governance, approval and evidence automation?
> **Covered in:** [AI governance, approval and evidence automation — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** system/model/dataset/prompt/index/tool/evaluator/deployment assets have owners and current lifecycle state. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JN-02

- [ ] **Question:** What is Risk classification, and why does it matter in AI governance, approval and evidence automation?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** intended use, affected users, autonomy, data and consequence determine control rigor. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JN-03

- [ ] **Question:** What is Control mapping, and why does it matter in AI governance, approval and evidence automation?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** policy requirement maps to automated/manual control, evidence source, frequency and accountable owner. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JN-04

- [ ] **Question:** What is Approval package, and why does it matter in AI governance, approval and evidence automation?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** immutable release plus evaluation/safety/security/privacy/operational evidence supports decision. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JN-05

- [ ] **Question:** What is Exception, and why does it matter in AI governance, approval and evidence automation?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** scoped asset/target, rationale, compensating control, risk owner and expiry prevent permanent invisible bypass. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JN-06

- [ ] **Question:** What is Separation of duties, and why does it matter in AI governance, approval and evidence automation?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** builder/evaluator/approver/deployer roles reduce unilateral high-risk release. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JN-07

- [ ] **Question:** What is Audit event, and why does it matter in AI governance, approval and evidence automation?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** actor/action/target/revision/decision/reason/evidence/result/time are tamper-resistant and searchable. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JN-08

- [ ] **Code:** **Question:** What does `python scripts/find_impact.py --asset MODEL_DIGEST` help you verify for AI governance, approval and evidence automation?
> **Covered in:** [AI governance, approval and evidence automation — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: lineage identifies systems, data subjects and controls affected by model/data/prompt/provider change.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JN-09

- [ ] **Code:** **Question:** What does `python scripts/inventory_lint.py inventory/*.yaml` help you verify for AI governance, approval and evidence automation?
> **Covered in:** [AI governance, approval and evidence automation — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: operational process records user/customer contest and policy override without erasing original decision.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JN-10

- [ ] **Code:** **Question:** What does `opa test governance/policy` help you verify for AI governance, approval and evidence automation?
> **Covered in:** [AI governance, approval and evidence automation — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: disable routes/tools, revoke access, preserve required evidence and delete data/artifacts under policy.

## Junior — procedural and command questions

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JP-01

- [ ] **Code:** **Question:** A basic AI inventory check fails. What would you do first using the CLI?
> **Covered in:** [AI governance, approval and evidence automation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/inventory_lint.py inventory/*.yaml` and capture exact status/reason/request ID. system/model/dataset/prompt/index/tool/evaluator/deployment assets have owners and current lifecycle state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JP-02

- [ ] **Question:** A basic Risk classification check fails. What would you do first?
> **Covered in:** [AI governance, approval and evidence automation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `opa test governance/policy` and capture exact status/reason/request ID. intended use, affected users, autonomy, data and consequence determine control rigor. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JP-03

- [ ] **Question:** A basic Control mapping check fails. What would you do first?
> **Covered in:** [AI governance, approval and evidence automation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/build_approval_package.py --release release.yaml` and capture exact status/reason/request ID. policy requirement maps to automated/manual control, evidence source, frequency and accountable owner. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JP-04

- [ ] **Code:** **Question:** A basic Approval package check fails. What would you do first using the CLI?
> **Covered in:** [AI governance, approval and evidence automation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/find_impact.py --asset MODEL_DIGEST` and capture exact status/reason/request ID. immutable release plus evaluation/safety/security/privacy/operational evidence supports decision. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JP-05

- [ ] **Question:** A basic Exception check fails. What would you do first?
> **Covered in:** [AI governance, approval and evidence automation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/inventory_lint.py inventory/*.yaml` and capture exact status/reason/request ID. scoped asset/target, rationale, compensating control, risk owner and expiry prevent permanent invisible bypass. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JP-06

- [ ] **Question:** A basic Separation of duties check fails. What would you do first?
> **Covered in:** [AI governance, approval and evidence automation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `opa test governance/policy` and capture exact status/reason/request ID. builder/evaluator/approver/deployer roles reduce unilateral high-risk release. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JP-07

- [ ] **Code:** **Question:** A basic Audit event check fails. What would you do first using the CLI?
> **Covered in:** [AI governance, approval and evidence automation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/build_approval_package.py --release release.yaml` and capture exact status/reason/request ID. actor/action/target/revision/decision/reason/evidence/result/time are tamper-resistant and searchable. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JP-08

- [ ] **Question:** A basic Change impact check fails. What would you do first?
> **Covered in:** [AI governance, approval and evidence automation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/find_impact.py --asset MODEL_DIGEST` and capture exact status/reason/request ID. lineage identifies systems, data subjects and controls affected by model/data/prompt/provider change. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JP-09

- [ ] **Question:** A basic Appeal/override check fails. What would you do first?
> **Covered in:** [AI governance, approval and evidence automation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/inventory_lint.py inventory/*.yaml` and capture exact status/reason/request ID. operational process records user/customer contest and policy override without erasing original decision. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-JP-10

- [ ] **Code:** **Question:** A basic Retirement check fails. What would you do first using the CLI?
> **Covered in:** [AI governance, approval and evidence automation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `opa test governance/policy` and capture exact status/reason/request ID. disable routes/tools, revoke access, preserve required evidence and delete data/artifacts under policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MN-01

- [ ] **Question:** Compare AI inventory with Risk classification. When would each change your design?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** AI inventory: system/model/dataset/prompt/index/tool/evaluator/deployment assets have owners and current lifecycle state. Risk classification: intended use, affected users, autonomy, data and consequence determine control rigor. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MN-02

- [ ] **Question:** Compare Risk classification with Control mapping. When would each change your design?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Risk classification: intended use, affected users, autonomy, data and consequence determine control rigor. Control mapping: policy requirement maps to automated/manual control, evidence source, frequency and accountable owner. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MN-03

- [ ] **Question:** Compare Control mapping with Approval package. When would each change your design?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Control mapping: policy requirement maps to automated/manual control, evidence source, frequency and accountable owner. Approval package: immutable release plus evaluation/safety/security/privacy/operational evidence supports decision. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MN-04

- [ ] **Configuration review:** **Question:** Compare Approval package with Exception. When would each change your design?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Approval package: immutable release plus evaluation/safety/security/privacy/operational evidence supports decision. Exception: scoped asset/target, rationale, compensating control, risk owner and expiry prevent permanent invisible bypass. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MN-05

- [ ] **Question:** Compare Exception with Separation of duties. When would each change your design?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Exception: scoped asset/target, rationale, compensating control, risk owner and expiry prevent permanent invisible bypass. Separation of duties: builder/evaluator/approver/deployer roles reduce unilateral high-risk release. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MN-06

- [ ] **Question:** Compare Separation of duties with Audit event. When would each change your design?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Separation of duties: builder/evaluator/approver/deployer roles reduce unilateral high-risk release. Audit event: actor/action/target/revision/decision/reason/evidence/result/time are tamper-resistant and searchable. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MN-07

- [ ] **Configuration review:** **Question:** Compare Audit event with Change impact. When would each change your design?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Audit event: actor/action/target/revision/decision/reason/evidence/result/time are tamper-resistant and searchable. Change impact: lineage identifies systems, data subjects and controls affected by model/data/prompt/provider change. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MN-08

- [ ] **Question:** Compare Change impact with Appeal/override. When would each change your design?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Change impact: lineage identifies systems, data subjects and controls affected by model/data/prompt/provider change. Appeal/override: operational process records user/customer contest and policy override without erasing original decision. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MN-09

- [ ] **Question:** Compare Appeal/override with Retirement. When would each change your design?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Appeal/override: operational process records user/customer contest and policy override without erasing original decision. Retirement: disable routes/tools, revoke access, preserve required evidence and delete data/artifacts under policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MN-10

- [ ] **Configuration review:** **Question:** Compare Retirement with AI inventory. When would each change your design?
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Retirement: disable routes/tools, revoke access, preserve required evidence and delete data/artifacts under policy. AI inventory: system/model/dataset/prompt/index/tool/evaluator/deployment assets have owners and current lifecycle state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around AI inventory; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/inventory_lint.py inventory/*.yaml` plus recent events/changes, then correlate the service-specific SLI. system/model/dataset/prompt/index/tool/evaluator/deployment assets have owners and current lifecycle state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MP-02

- [ ] **Question:** Production is degraded around Risk classification; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `opa test governance/policy` plus recent events/changes, then correlate the service-specific SLI. intended use, affected users, autonomy, data and consequence determine control rigor. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Control mapping; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/build_approval_package.py --release release.yaml` plus recent events/changes, then correlate the service-specific SLI. policy requirement maps to automated/manual control, evidence source, frequency and accountable owner. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MP-04

- [ ] **Question:** Production is degraded around Approval package; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/find_impact.py --asset MODEL_DIGEST` plus recent events/changes, then correlate the service-specific SLI. immutable release plus evaluation/safety/security/privacy/operational evidence supports decision. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Exception; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/inventory_lint.py inventory/*.yaml` plus recent events/changes, then correlate the service-specific SLI. scoped asset/target, rationale, compensating control, risk owner and expiry prevent permanent invisible bypass. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MP-06

- [ ] **Question:** Production is degraded around Separation of duties; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `opa test governance/policy` plus recent events/changes, then correlate the service-specific SLI. builder/evaluator/approver/deployer roles reduce unilateral high-risk release. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Audit event; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/build_approval_package.py --release release.yaml` plus recent events/changes, then correlate the service-specific SLI. actor/action/target/revision/decision/reason/evidence/result/time are tamper-resistant and searchable. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MP-08

- [ ] **Question:** Production is degraded around Change impact; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/find_impact.py --asset MODEL_DIGEST` plus recent events/changes, then correlate the service-specific SLI. lineage identifies systems, data subjects and controls affected by model/data/prompt/provider change. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Appeal/override; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/inventory_lint.py inventory/*.yaml` plus recent events/changes, then correlate the service-specific SLI. operational process records user/customer contest and policy override without erasing original decision. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-MP-10

- [ ] **Question:** Production is degraded around Retirement; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `opa test governance/policy` plus recent events/changes, then correlate the service-specific SLI. disable routes/tools, revoke access, preserve required evidence and delete data/artifacts under policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SN-01

- [ ] **Question:** Design a production AI governance, approval and evidence automation capability where AI inventory, Approval package and Audit event are first-class requirements.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: system/model/dataset/prompt/index/tool/evaluator/deployment assets have owners and current lifecycle state. immutable release plus evaluation/safety/security/privacy/operational evidence supports decision. actor/action/target/revision/decision/reason/evidence/result/time are tamper-resistant and searchable. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AI governance, approval and evidence automation capability where Risk classification, Exception and Change impact are first-class requirements.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: intended use, affected users, autonomy, data and consequence determine control rigor. scoped asset/target, rationale, compensating control, risk owner and expiry prevent permanent invisible bypass. lineage identifies systems, data subjects and controls affected by model/data/prompt/provider change. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SN-03

- [ ] **Question:** Design a production AI governance, approval and evidence automation capability where Control mapping, Separation of duties and Appeal/override are first-class requirements.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: policy requirement maps to automated/manual control, evidence source, frequency and accountable owner. builder/evaluator/approver/deployer roles reduce unilateral high-risk release. operational process records user/customer contest and policy override without erasing original decision. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AI governance, approval and evidence automation capability where Approval package, Audit event and Retirement are first-class requirements.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable release plus evaluation/safety/security/privacy/operational evidence supports decision. actor/action/target/revision/decision/reason/evidence/result/time are tamper-resistant and searchable. disable routes/tools, revoke access, preserve required evidence and delete data/artifacts under policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SN-05

- [ ] **Question:** Design a production AI governance, approval and evidence automation capability where Exception, Change impact and AI inventory are first-class requirements.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scoped asset/target, rationale, compensating control, risk owner and expiry prevent permanent invisible bypass. lineage identifies systems, data subjects and controls affected by model/data/prompt/provider change. system/model/dataset/prompt/index/tool/evaluator/deployment assets have owners and current lifecycle state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AI governance, approval and evidence automation capability where Separation of duties, Appeal/override and Risk classification are first-class requirements.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: builder/evaluator/approver/deployer roles reduce unilateral high-risk release. operational process records user/customer contest and policy override without erasing original decision. intended use, affected users, autonomy, data and consequence determine control rigor. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SN-07

- [ ] **Question:** Design a production AI governance, approval and evidence automation capability where Audit event, Retirement and Control mapping are first-class requirements.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: actor/action/target/revision/decision/reason/evidence/result/time are tamper-resistant and searchable. disable routes/tools, revoke access, preserve required evidence and delete data/artifacts under policy. policy requirement maps to automated/manual control, evidence source, frequency and accountable owner. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AI governance, approval and evidence automation capability where Change impact, AI inventory and Approval package are first-class requirements.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: lineage identifies systems, data subjects and controls affected by model/data/prompt/provider change. system/model/dataset/prompt/index/tool/evaluator/deployment assets have owners and current lifecycle state. immutable release plus evaluation/safety/security/privacy/operational evidence supports decision. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SN-09

- [ ] **Question:** Design a production AI governance, approval and evidence automation capability where Appeal/override, Risk classification and Exception are first-class requirements.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: operational process records user/customer contest and policy override without erasing original decision. intended use, affected users, autonomy, data and consequence determine control rigor. scoped asset/target, rationale, compensating control, risk owner and expiry prevent permanent invisible bypass. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AI governance, approval and evidence automation capability where Retirement, Control mapping and Separation of duties are first-class requirements.
> **Covered in:** [AI governance, approval and evidence automation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: disable routes/tools, revoke access, preserve required evidence and delete data/artifacts under policy. policy requirement maps to automated/manual control, evidence source, frequency and accountable owner. builder/evaluator/approver/deployer roles reduce unilateral high-risk release. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AI inventory. How do you lead it end to end?
> **Covered in:** [AI governance, approval and evidence automation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/inventory_lint.py inventory/*.yaml` as one read-only checkpoint, not the whole diagnosis. system/model/dataset/prompt/index/tool/evaluator/deployment assets have owners and current lifecycle state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Risk classification. How do you lead it end to end?
> **Covered in:** [AI governance, approval and evidence automation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `opa test governance/policy` as one read-only checkpoint, not the whole diagnosis. intended use, affected users, autonomy, data and consequence determine control rigor. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control mapping. How do you lead it end to end?
> **Covered in:** [AI governance, approval and evidence automation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/build_approval_package.py --release release.yaml` as one read-only checkpoint, not the whole diagnosis. policy requirement maps to automated/manual control, evidence source, frequency and accountable owner. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Approval package. How do you lead it end to end?
> **Covered in:** [AI governance, approval and evidence automation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/find_impact.py --asset MODEL_DIGEST` as one read-only checkpoint, not the whole diagnosis. immutable release plus evaluation/safety/security/privacy/operational evidence supports decision. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Exception. How do you lead it end to end?
> **Covered in:** [AI governance, approval and evidence automation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/inventory_lint.py inventory/*.yaml` as one read-only checkpoint, not the whole diagnosis. scoped asset/target, rationale, compensating control, risk owner and expiry prevent permanent invisible bypass. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Separation of duties. How do you lead it end to end?
> **Covered in:** [AI governance, approval and evidence automation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `opa test governance/policy` as one read-only checkpoint, not the whole diagnosis. builder/evaluator/approver/deployer roles reduce unilateral high-risk release. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Audit event. How do you lead it end to end?
> **Covered in:** [AI governance, approval and evidence automation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/build_approval_package.py --release release.yaml` as one read-only checkpoint, not the whole diagnosis. actor/action/target/revision/decision/reason/evidence/result/time are tamper-resistant and searchable. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Change impact. How do you lead it end to end?
> **Covered in:** [AI governance, approval and evidence automation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/find_impact.py --asset MODEL_DIGEST` as one read-only checkpoint, not the whole diagnosis. lineage identifies systems, data subjects and controls affected by model/data/prompt/provider change. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Appeal/override. How do you lead it end to end?
> **Covered in:** [AI governance, approval and evidence automation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/inventory_lint.py inventory/*.yaml` as one read-only checkpoint, not the whole diagnosis. operational process records user/customer contest and policy override without erasing original decision. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-GOVERNANCE-APPROVAL-AND-EVIDENCE-AUTOMATION-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retirement. How do you lead it end to end?
> **Covered in:** [AI governance, approval and evidence automation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `opa test governance/policy` as one read-only checkpoint, not the whole diagnosis. disable routes/tools, revoke access, preserve required evidence and delete data/artifacts under policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: LLM safety, red teaming and guardrail operations](../23-safety-redteam-guardrails/README.md) · [Study note](README.md) · [Next: AI supply chain, signing and provenance →](../25-ai-supply-chain/README.md)

<!-- reading-navigation:end -->
