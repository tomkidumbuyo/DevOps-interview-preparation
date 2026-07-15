# AWS Systems Manager — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-SYSTEMS-MANAGER-JN-01

- [ ] **Question:** What is Managed node, and why does it matter in AWS Systems Manager?

**Answer:** agent/identity/network registration makes a host available to SSM. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SYSTEMS-MANAGER-JN-02

- [ ] **Question:** What is Session Manager, and why does it matter in AWS Systems Manager?

**Answer:** audited interactive/tunnel access without inbound SSH under IAM/session preferences. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SYSTEMS-MANAGER-JN-03

- [ ] **Question:** What is Run Command, and why does it matter in AWS Systems Manager?

**Answer:** executes commands across targets with concurrency/error thresholds and output controls. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SYSTEMS-MANAGER-JN-04

- [ ] **Question:** What is Automation document, and why does it matter in AWS Systems Manager?

**Answer:** typed multi-step workflow with assume role, branching, approvals and rollback design. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SYSTEMS-MANAGER-JN-05

- [ ] **Question:** What is Patch Manager, and why does it matter in AWS Systems Manager?

**Answer:** baselines, maintenance windows and compliance scan/install coordinate patching. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SYSTEMS-MANAGER-JN-06

- [ ] **Question:** What is Inventory, and why does it matter in AWS Systems Manager?

**Answer:** collects software/instance metadata for fleet queries and exposure. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SYSTEMS-MANAGER-JN-07

- [ ] **Question:** What is State Manager, and why does it matter in AWS Systems Manager?

**Answer:** periodically enforces associations and can conflict with image/IaC ownership. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SYSTEMS-MANAGER-JN-08

- [ ] **Code:** **Question:** What does `aws ssm describe-instance-patch-states --instance-ids INSTANCE_ID` help you verify for AWS Systems Manager?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: distributes configuration/secrets under hierarchy/KMS/IAM.

### AWS-SYSTEMS-MANAGER-JN-09

- [ ] **Code:** **Question:** What does `aws ssm describe-instance-information` help you verify for AWS Systems Manager?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: console operations still require least privilege and evidence.

### AWS-SYSTEMS-MANAGER-JN-10

- [ ] **Code:** **Question:** What does `aws ssm start-session --target INSTANCE_ID` help you verify for AWS Systems Manager?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: tags/resource groups, max concurrency/errors and canaries prevent fleet-wide mistakes.

## Junior — procedural and command questions

### AWS-SYSTEMS-MANAGER-JP-01

- [ ] **Code:** **Question:** A basic Managed node check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm describe-instance-information` and capture exact status/reason/request ID. agent/identity/network registration makes a host available to SSM. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SYSTEMS-MANAGER-JP-02

- [ ] **Question:** A basic Session Manager check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm start-session --target INSTANCE_ID` and capture exact status/reason/request ID. audited interactive/tunnel access without inbound SSH under IAM/session preferences. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SYSTEMS-MANAGER-JP-03

- [ ] **Question:** A basic Run Command check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm send-command --document-name DOC --targets Key=tag:Environment,Values=stage --max-concurrency 10% --max-errors 1` and capture exact status/reason/request ID. executes commands across targets with concurrency/error thresholds and output controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SYSTEMS-MANAGER-JP-04

- [ ] **Code:** **Question:** A basic Automation document check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm describe-instance-patch-states --instance-ids INSTANCE_ID` and capture exact status/reason/request ID. typed multi-step workflow with assume role, branching, approvals and rollback design. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SYSTEMS-MANAGER-JP-05

- [ ] **Question:** A basic Patch Manager check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm describe-instance-information` and capture exact status/reason/request ID. baselines, maintenance windows and compliance scan/install coordinate patching. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SYSTEMS-MANAGER-JP-06

- [ ] **Question:** A basic Inventory check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm start-session --target INSTANCE_ID` and capture exact status/reason/request ID. collects software/instance metadata for fleet queries and exposure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SYSTEMS-MANAGER-JP-07

- [ ] **Code:** **Question:** A basic State Manager check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm send-command --document-name DOC --targets Key=tag:Environment,Values=stage --max-concurrency 10% --max-errors 1` and capture exact status/reason/request ID. periodically enforces associations and can conflict with image/IaC ownership. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SYSTEMS-MANAGER-JP-08

- [ ] **Question:** A basic Parameter Store check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm describe-instance-patch-states --instance-ids INSTANCE_ID` and capture exact status/reason/request ID. distributes configuration/secrets under hierarchy/KMS/IAM. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SYSTEMS-MANAGER-JP-09

- [ ] **Question:** A basic Fleet Manager check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm describe-instance-information` and capture exact status/reason/request ID. console operations still require least privilege and evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SYSTEMS-MANAGER-JP-10

- [ ] **Code:** **Question:** A basic Target safety check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm start-session --target INSTANCE_ID` and capture exact status/reason/request ID. tags/resource groups, max concurrency/errors and canaries prevent fleet-wide mistakes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-SYSTEMS-MANAGER-MN-01

- [ ] **Question:** Compare Managed node with Session Manager. When would each change your design?

**Answer:** Managed node: agent/identity/network registration makes a host available to SSM. Session Manager: audited interactive/tunnel access without inbound SSH under IAM/session preferences. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SYSTEMS-MANAGER-MN-02

- [ ] **Question:** Compare Session Manager with Run Command. When would each change your design?

**Answer:** Session Manager: audited interactive/tunnel access without inbound SSH under IAM/session preferences. Run Command: executes commands across targets with concurrency/error thresholds and output controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SYSTEMS-MANAGER-MN-03

- [ ] **Question:** Compare Run Command with Automation document. When would each change your design?

**Answer:** Run Command: executes commands across targets with concurrency/error thresholds and output controls. Automation document: typed multi-step workflow with assume role, branching, approvals and rollback design. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SYSTEMS-MANAGER-MN-04

- [ ] **Configuration review:** **Question:** Compare Automation document with Patch Manager. When would each change your design?

**Answer:** Automation document: typed multi-step workflow with assume role, branching, approvals and rollback design. Patch Manager: baselines, maintenance windows and compliance scan/install coordinate patching. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SYSTEMS-MANAGER-MN-05

- [ ] **Question:** Compare Patch Manager with Inventory. When would each change your design?

**Answer:** Patch Manager: baselines, maintenance windows and compliance scan/install coordinate patching. Inventory: collects software/instance metadata for fleet queries and exposure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SYSTEMS-MANAGER-MN-06

- [ ] **Question:** Compare Inventory with State Manager. When would each change your design?

**Answer:** Inventory: collects software/instance metadata for fleet queries and exposure. State Manager: periodically enforces associations and can conflict with image/IaC ownership. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SYSTEMS-MANAGER-MN-07

- [ ] **Configuration review:** **Question:** Compare State Manager with Parameter Store. When would each change your design?

**Answer:** State Manager: periodically enforces associations and can conflict with image/IaC ownership. Parameter Store: distributes configuration/secrets under hierarchy/KMS/IAM. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SYSTEMS-MANAGER-MN-08

- [ ] **Question:** Compare Parameter Store with Fleet Manager. When would each change your design?

**Answer:** Parameter Store: distributes configuration/secrets under hierarchy/KMS/IAM. Fleet Manager: console operations still require least privilege and evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SYSTEMS-MANAGER-MN-09

- [ ] **Question:** Compare Fleet Manager with Target safety. When would each change your design?

**Answer:** Fleet Manager: console operations still require least privilege and evidence. Target safety: tags/resource groups, max concurrency/errors and canaries prevent fleet-wide mistakes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SYSTEMS-MANAGER-MN-10

- [ ] **Configuration review:** **Question:** Compare Target safety with Managed node. When would each change your design?

**Answer:** Target safety: tags/resource groups, max concurrency/errors and canaries prevent fleet-wide mistakes. Managed node: agent/identity/network registration makes a host available to SSM. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-SYSTEMS-MANAGER-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Managed node; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm describe-instance-information` plus recent events/changes, then correlate the service-specific SLI. agent/identity/network registration makes a host available to SSM. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SYSTEMS-MANAGER-MP-02

- [ ] **Question:** Production is degraded around Session Manager; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm start-session --target INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. audited interactive/tunnel access without inbound SSH under IAM/session preferences. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SYSTEMS-MANAGER-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Run Command; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm send-command --document-name DOC --targets Key=tag:Environment,Values=stage --max-concurrency 10% --max-errors 1` plus recent events/changes, then correlate the service-specific SLI. executes commands across targets with concurrency/error thresholds and output controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SYSTEMS-MANAGER-MP-04

- [ ] **Question:** Production is degraded around Automation document; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm describe-instance-patch-states --instance-ids INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. typed multi-step workflow with assume role, branching, approvals and rollback design. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SYSTEMS-MANAGER-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Patch Manager; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm describe-instance-information` plus recent events/changes, then correlate the service-specific SLI. baselines, maintenance windows and compliance scan/install coordinate patching. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SYSTEMS-MANAGER-MP-06

- [ ] **Question:** Production is degraded around Inventory; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm start-session --target INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. collects software/instance metadata for fleet queries and exposure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SYSTEMS-MANAGER-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around State Manager; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm send-command --document-name DOC --targets Key=tag:Environment,Values=stage --max-concurrency 10% --max-errors 1` plus recent events/changes, then correlate the service-specific SLI. periodically enforces associations and can conflict with image/IaC ownership. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SYSTEMS-MANAGER-MP-08

- [ ] **Question:** Production is degraded around Parameter Store; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm describe-instance-patch-states --instance-ids INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. distributes configuration/secrets under hierarchy/KMS/IAM. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SYSTEMS-MANAGER-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Fleet Manager; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm describe-instance-information` plus recent events/changes, then correlate the service-specific SLI. console operations still require least privilege and evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SYSTEMS-MANAGER-MP-10

- [ ] **Question:** Production is degraded around Target safety; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm start-session --target INSTANCE_ID` plus recent events/changes, then correlate the service-specific SLI. tags/resource groups, max concurrency/errors and canaries prevent fleet-wide mistakes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-SYSTEMS-MANAGER-SN-01

- [ ] **Question:** Design a production AWS Systems Manager capability where Managed node, Automation document and State Manager are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: agent/identity/network registration makes a host available to SSM. typed multi-step workflow with assume role, branching, approvals and rollback design. periodically enforces associations and can conflict with image/IaC ownership. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SYSTEMS-MANAGER-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Systems Manager capability where Session Manager, Patch Manager and Parameter Store are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: audited interactive/tunnel access without inbound SSH under IAM/session preferences. baselines, maintenance windows and compliance scan/install coordinate patching. distributes configuration/secrets under hierarchy/KMS/IAM. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SYSTEMS-MANAGER-SN-03

- [ ] **Question:** Design a production AWS Systems Manager capability where Run Command, Inventory and Fleet Manager are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: executes commands across targets with concurrency/error thresholds and output controls. collects software/instance metadata for fleet queries and exposure. console operations still require least privilege and evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SYSTEMS-MANAGER-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Systems Manager capability where Automation document, State Manager and Target safety are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: typed multi-step workflow with assume role, branching, approvals and rollback design. periodically enforces associations and can conflict with image/IaC ownership. tags/resource groups, max concurrency/errors and canaries prevent fleet-wide mistakes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SYSTEMS-MANAGER-SN-05

- [ ] **Question:** Design a production AWS Systems Manager capability where Patch Manager, Parameter Store and Managed node are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: baselines, maintenance windows and compliance scan/install coordinate patching. distributes configuration/secrets under hierarchy/KMS/IAM. agent/identity/network registration makes a host available to SSM. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SYSTEMS-MANAGER-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Systems Manager capability where Inventory, Fleet Manager and Session Manager are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: collects software/instance metadata for fleet queries and exposure. console operations still require least privilege and evidence. audited interactive/tunnel access without inbound SSH under IAM/session preferences. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SYSTEMS-MANAGER-SN-07

- [ ] **Question:** Design a production AWS Systems Manager capability where State Manager, Target safety and Run Command are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: periodically enforces associations and can conflict with image/IaC ownership. tags/resource groups, max concurrency/errors and canaries prevent fleet-wide mistakes. executes commands across targets with concurrency/error thresholds and output controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SYSTEMS-MANAGER-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Systems Manager capability where Parameter Store, Managed node and Automation document are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: distributes configuration/secrets under hierarchy/KMS/IAM. agent/identity/network registration makes a host available to SSM. typed multi-step workflow with assume role, branching, approvals and rollback design. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SYSTEMS-MANAGER-SN-09

- [ ] **Question:** Design a production AWS Systems Manager capability where Fleet Manager, Session Manager and Patch Manager are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: console operations still require least privilege and evidence. audited interactive/tunnel access without inbound SSH under IAM/session preferences. baselines, maintenance windows and compliance scan/install coordinate patching. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SYSTEMS-MANAGER-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Systems Manager capability where Target safety, Run Command and Inventory are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tags/resource groups, max concurrency/errors and canaries prevent fleet-wide mistakes. executes commands across targets with concurrency/error thresholds and output controls. collects software/instance metadata for fleet queries and exposure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-SYSTEMS-MANAGER-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Managed node. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm describe-instance-information` as one read-only checkpoint, not the whole diagnosis. agent/identity/network registration makes a host available to SSM. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SYSTEMS-MANAGER-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Session Manager. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm start-session --target INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. audited interactive/tunnel access without inbound SSH under IAM/session preferences. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SYSTEMS-MANAGER-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Run Command. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm send-command --document-name DOC --targets Key=tag:Environment,Values=stage --max-concurrency 10% --max-errors 1` as one read-only checkpoint, not the whole diagnosis. executes commands across targets with concurrency/error thresholds and output controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SYSTEMS-MANAGER-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Automation document. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm describe-instance-patch-states --instance-ids INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. typed multi-step workflow with assume role, branching, approvals and rollback design. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SYSTEMS-MANAGER-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Patch Manager. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm describe-instance-information` as one read-only checkpoint, not the whole diagnosis. baselines, maintenance windows and compliance scan/install coordinate patching. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SYSTEMS-MANAGER-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Inventory. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm start-session --target INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. collects software/instance metadata for fleet queries and exposure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SYSTEMS-MANAGER-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving State Manager. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm send-command --document-name DOC --targets Key=tag:Environment,Values=stage --max-concurrency 10% --max-errors 1` as one read-only checkpoint, not the whole diagnosis. periodically enforces associations and can conflict with image/IaC ownership. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SYSTEMS-MANAGER-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Parameter Store. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm describe-instance-patch-states --instance-ids INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. distributes configuration/secrets under hierarchy/KMS/IAM. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SYSTEMS-MANAGER-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Fleet Manager. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm describe-instance-information` as one read-only checkpoint, not the whole diagnosis. console operations still require least privilege and evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SYSTEMS-MANAGER-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Target safety. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm start-session --target INSTANCE_ID` as one read-only checkpoint, not the whole diagnosis. tags/resource groups, max concurrency/errors and canaries prevent fleet-wide mistakes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
