# AWS CloudFormation — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-CLOUDFORMATION-JN-01

- [ ] **Question:** What is Stack, and why does it matter in AWS CloudFormation?
> **Covered in:** [AWS CloudFormation — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** ownership/lifecycle boundary for a set of resources and outputs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDFORMATION-JN-02

- [ ] **Question:** What is Change set, and why does it matter in AWS CloudFormation?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** previews create/update/import actions but cannot predict every service-side effect. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDFORMATION-JN-03

- [ ] **Question:** What is Rollback, and why does it matter in AWS CloudFormation?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** attempts prior stack state and can fail on irreversible/external/data changes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDFORMATION-JN-04

- [ ] **Question:** What is Stack policy, and why does it matter in AWS CloudFormation?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** protects selected resources from update actions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDFORMATION-JN-05

- [ ] **Question:** What is Deletion/retention policy, and why does it matter in AWS CloudFormation?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** controls resource/snapshot behavior when template/stack removes stateful resources. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDFORMATION-JN-06

- [ ] **Question:** What is Nested stack/module, and why does it matter in AWS CloudFormation?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** composes templates but introduces dependency/update propagation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDFORMATION-JN-07

- [ ] **Question:** What is StackSet, and why does it matter in AWS CloudFormation?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** deploys instances across accounts/Regions with concurrency/failure controls. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDFORMATION-JN-08

- [ ] **Code:** **Question:** What does `aws cloudformation continue-update-rollback --stack-name STACK` help you verify for AWS CloudFormation?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: compares supported properties to template without deciding correct truth.

### AWS-CLOUDFORMATION-JN-09

- [ ] **Code:** **Question:** What does `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` help you verify for AWS CloudFormation?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: adopts supported existing resources after template/identity preparation.

### AWS-CLOUDFORMATION-JN-10

- [ ] **Code:** **Question:** What does `aws cloudformation describe-stack-events --stack-name STACK` help you verify for AWS CloudFormation?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: repairs a stuck rollback after fixing/skipping failed resources carefully.

## Junior — procedural and command questions

### AWS-CLOUDFORMATION-JP-01

- [ ] **Code:** **Question:** A basic Stack check fails. What would you do first using the CLI?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` and capture exact status/reason/request ID. ownership/lifecycle boundary for a set of resources and outputs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDFORMATION-JP-02

- [ ] **Question:** A basic Change set check fails. What would you do first?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation describe-stack-events --stack-name STACK` and capture exact status/reason/request ID. previews create/update/import actions but cannot predict every service-side effect. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDFORMATION-JP-03

- [ ] **Question:** A basic Rollback check fails. What would you do first?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation detect-stack-drift --stack-name STACK` and capture exact status/reason/request ID. attempts prior stack state and can fail on irreversible/external/data changes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDFORMATION-JP-04

- [ ] **Code:** **Question:** A basic Stack policy check fails. What would you do first using the CLI?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation continue-update-rollback --stack-name STACK` and capture exact status/reason/request ID. protects selected resources from update actions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDFORMATION-JP-05

- [ ] **Question:** A basic Deletion/retention policy check fails. What would you do first?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` and capture exact status/reason/request ID. controls resource/snapshot behavior when template/stack removes stateful resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDFORMATION-JP-06

- [ ] **Question:** A basic Nested stack/module check fails. What would you do first?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation describe-stack-events --stack-name STACK` and capture exact status/reason/request ID. composes templates but introduces dependency/update propagation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDFORMATION-JP-07

- [ ] **Code:** **Question:** A basic StackSet check fails. What would you do first using the CLI?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation detect-stack-drift --stack-name STACK` and capture exact status/reason/request ID. deploys instances across accounts/Regions with concurrency/failure controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDFORMATION-JP-08

- [ ] **Question:** A basic Drift detection check fails. What would you do first?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation continue-update-rollback --stack-name STACK` and capture exact status/reason/request ID. compares supported properties to template without deciding correct truth. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDFORMATION-JP-09

- [ ] **Question:** A basic Import check fails. What would you do first?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` and capture exact status/reason/request ID. adopts supported existing resources after template/identity preparation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDFORMATION-JP-10

- [ ] **Code:** **Question:** A basic Continue update rollback check fails. What would you do first using the CLI?
> **Covered in:** [AWS CloudFormation — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation describe-stack-events --stack-name STACK` and capture exact status/reason/request ID. repairs a stuck rollback after fixing/skipping failed resources carefully. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-CLOUDFORMATION-MN-01

- [ ] **Question:** Compare Stack with Change set. When would each change your design?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Stack: ownership/lifecycle boundary for a set of resources and outputs. Change set: previews create/update/import actions but cannot predict every service-side effect. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDFORMATION-MN-02

- [ ] **Question:** Compare Change set with Rollback. When would each change your design?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Change set: previews create/update/import actions but cannot predict every service-side effect. Rollback: attempts prior stack state and can fail on irreversible/external/data changes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDFORMATION-MN-03

- [ ] **Question:** Compare Rollback with Stack policy. When would each change your design?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Rollback: attempts prior stack state and can fail on irreversible/external/data changes. Stack policy: protects selected resources from update actions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDFORMATION-MN-04

- [ ] **Configuration review:** **Question:** Compare Stack policy with Deletion/retention policy. When would each change your design?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Stack policy: protects selected resources from update actions. Deletion/retention policy: controls resource/snapshot behavior when template/stack removes stateful resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDFORMATION-MN-05

- [ ] **Question:** Compare Deletion/retention policy with Nested stack/module. When would each change your design?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Deletion/retention policy: controls resource/snapshot behavior when template/stack removes stateful resources. Nested stack/module: composes templates but introduces dependency/update propagation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDFORMATION-MN-06

- [ ] **Question:** Compare Nested stack/module with StackSet. When would each change your design?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Nested stack/module: composes templates but introduces dependency/update propagation. StackSet: deploys instances across accounts/Regions with concurrency/failure controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDFORMATION-MN-07

- [ ] **Configuration review:** **Question:** Compare StackSet with Drift detection. When would each change your design?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** StackSet: deploys instances across accounts/Regions with concurrency/failure controls. Drift detection: compares supported properties to template without deciding correct truth. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDFORMATION-MN-08

- [ ] **Question:** Compare Drift detection with Import. When would each change your design?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Drift detection: compares supported properties to template without deciding correct truth. Import: adopts supported existing resources after template/identity preparation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDFORMATION-MN-09

- [ ] **Question:** Compare Import with Continue update rollback. When would each change your design?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Import: adopts supported existing resources after template/identity preparation. Continue update rollback: repairs a stuck rollback after fixing/skipping failed resources carefully. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDFORMATION-MN-10

- [ ] **Configuration review:** **Question:** Compare Continue update rollback with Stack. When would each change your design?
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Continue update rollback: repairs a stuck rollback after fixing/skipping failed resources carefully. Stack: ownership/lifecycle boundary for a set of resources and outputs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-CLOUDFORMATION-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Stack; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` plus recent events/changes, then correlate the service-specific SLI. ownership/lifecycle boundary for a set of resources and outputs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDFORMATION-MP-02

- [ ] **Question:** Production is degraded around Change set; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation describe-stack-events --stack-name STACK` plus recent events/changes, then correlate the service-specific SLI. previews create/update/import actions but cannot predict every service-side effect. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDFORMATION-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Rollback; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation detect-stack-drift --stack-name STACK` plus recent events/changes, then correlate the service-specific SLI. attempts prior stack state and can fail on irreversible/external/data changes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDFORMATION-MP-04

- [ ] **Question:** Production is degraded around Stack policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation continue-update-rollback --stack-name STACK` plus recent events/changes, then correlate the service-specific SLI. protects selected resources from update actions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDFORMATION-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Deletion/retention policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` plus recent events/changes, then correlate the service-specific SLI. controls resource/snapshot behavior when template/stack removes stateful resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDFORMATION-MP-06

- [ ] **Question:** Production is degraded around Nested stack/module; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation describe-stack-events --stack-name STACK` plus recent events/changes, then correlate the service-specific SLI. composes templates but introduces dependency/update propagation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDFORMATION-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around StackSet; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation detect-stack-drift --stack-name STACK` plus recent events/changes, then correlate the service-specific SLI. deploys instances across accounts/Regions with concurrency/failure controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDFORMATION-MP-08

- [ ] **Question:** Production is degraded around Drift detection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation continue-update-rollback --stack-name STACK` plus recent events/changes, then correlate the service-specific SLI. compares supported properties to template without deciding correct truth. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDFORMATION-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Import; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` plus recent events/changes, then correlate the service-specific SLI. adopts supported existing resources after template/identity preparation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDFORMATION-MP-10

- [ ] **Question:** Production is degraded around Continue update rollback; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation describe-stack-events --stack-name STACK` plus recent events/changes, then correlate the service-specific SLI. repairs a stuck rollback after fixing/skipping failed resources carefully. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-CLOUDFORMATION-SN-01

- [ ] **Question:** Design a production AWS CloudFormation capability where Stack, Stack policy and StackSet are first-class requirements.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ownership/lifecycle boundary for a set of resources and outputs. protects selected resources from update actions. deploys instances across accounts/Regions with concurrency/failure controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDFORMATION-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CloudFormation capability where Change set, Deletion/retention policy and Drift detection are first-class requirements.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: previews create/update/import actions but cannot predict every service-side effect. controls resource/snapshot behavior when template/stack removes stateful resources. compares supported properties to template without deciding correct truth. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDFORMATION-SN-03

- [ ] **Question:** Design a production AWS CloudFormation capability where Rollback, Nested stack/module and Import are first-class requirements.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: attempts prior stack state and can fail on irreversible/external/data changes. composes templates but introduces dependency/update propagation. adopts supported existing resources after template/identity preparation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDFORMATION-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CloudFormation capability where Stack policy, StackSet and Continue update rollback are first-class requirements.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: protects selected resources from update actions. deploys instances across accounts/Regions with concurrency/failure controls. repairs a stuck rollback after fixing/skipping failed resources carefully. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDFORMATION-SN-05

- [ ] **Question:** Design a production AWS CloudFormation capability where Deletion/retention policy, Drift detection and Stack are first-class requirements.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controls resource/snapshot behavior when template/stack removes stateful resources. compares supported properties to template without deciding correct truth. ownership/lifecycle boundary for a set of resources and outputs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDFORMATION-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CloudFormation capability where Nested stack/module, Import and Change set are first-class requirements.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: composes templates but introduces dependency/update propagation. adopts supported existing resources after template/identity preparation. previews create/update/import actions but cannot predict every service-side effect. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDFORMATION-SN-07

- [ ] **Question:** Design a production AWS CloudFormation capability where StackSet, Continue update rollback and Rollback are first-class requirements.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: deploys instances across accounts/Regions with concurrency/failure controls. repairs a stuck rollback after fixing/skipping failed resources carefully. attempts prior stack state and can fail on irreversible/external/data changes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDFORMATION-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CloudFormation capability where Drift detection, Stack and Stack policy are first-class requirements.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: compares supported properties to template without deciding correct truth. ownership/lifecycle boundary for a set of resources and outputs. protects selected resources from update actions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDFORMATION-SN-09

- [ ] **Question:** Design a production AWS CloudFormation capability where Import, Change set and Deletion/retention policy are first-class requirements.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: adopts supported existing resources after template/identity preparation. previews create/update/import actions but cannot predict every service-side effect. controls resource/snapshot behavior when template/stack removes stateful resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDFORMATION-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CloudFormation capability where Continue update rollback, Rollback and Nested stack/module are first-class requirements.
> **Covered in:** [AWS CloudFormation — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: repairs a stuck rollback after fixing/skipping failed resources carefully. attempts prior stack state and can fail on irreversible/external/data changes. composes templates but introduces dependency/update propagation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-CLOUDFORMATION-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stack. How do you lead it end to end?
> **Covered in:** [AWS CloudFormation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` as one read-only checkpoint, not the whole diagnosis. ownership/lifecycle boundary for a set of resources and outputs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDFORMATION-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Change set. How do you lead it end to end?
> **Covered in:** [AWS CloudFormation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation describe-stack-events --stack-name STACK` as one read-only checkpoint, not the whole diagnosis. previews create/update/import actions but cannot predict every service-side effect. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDFORMATION-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rollback. How do you lead it end to end?
> **Covered in:** [AWS CloudFormation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation detect-stack-drift --stack-name STACK` as one read-only checkpoint, not the whole diagnosis. attempts prior stack state and can fail on irreversible/external/data changes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDFORMATION-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stack policy. How do you lead it end to end?
> **Covered in:** [AWS CloudFormation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation continue-update-rollback --stack-name STACK` as one read-only checkpoint, not the whole diagnosis. protects selected resources from update actions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDFORMATION-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deletion/retention policy. How do you lead it end to end?
> **Covered in:** [AWS CloudFormation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` as one read-only checkpoint, not the whole diagnosis. controls resource/snapshot behavior when template/stack removes stateful resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDFORMATION-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Nested stack/module. How do you lead it end to end?
> **Covered in:** [AWS CloudFormation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation describe-stack-events --stack-name STACK` as one read-only checkpoint, not the whole diagnosis. composes templates but introduces dependency/update propagation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDFORMATION-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving StackSet. How do you lead it end to end?
> **Covered in:** [AWS CloudFormation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation detect-stack-drift --stack-name STACK` as one read-only checkpoint, not the whole diagnosis. deploys instances across accounts/Regions with concurrency/failure controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDFORMATION-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Drift detection. How do you lead it end to end?
> **Covered in:** [AWS CloudFormation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation continue-update-rollback --stack-name STACK` as one read-only checkpoint, not the whole diagnosis. compares supported properties to template without deciding correct truth. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDFORMATION-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Import. How do you lead it end to end?
> **Covered in:** [AWS CloudFormation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` as one read-only checkpoint, not the whole diagnosis. adopts supported existing resources after template/identity preparation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDFORMATION-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Continue update rollback. How do you lead it end to end?
> **Covered in:** [AWS CloudFormation — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation describe-stack-events --stack-name STACK` as one read-only checkpoint, not the whole diagnosis. repairs a stuck rollback after fixing/skipping failed resources carefully. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Infrastructure Delivery](../README.md) · [Study note](README.md) · [Next: AWS CDK →](../02-cdk/README.md)

<!-- reading-navigation:end -->
