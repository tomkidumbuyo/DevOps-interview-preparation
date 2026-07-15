# CodeBuild, CodePipeline and CodeDeploy — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JN-01

- [ ] **Question:** What is CodeBuild project, and why does it matter in CodeBuild, CodePipeline and CodeDeploy?

**Answer:** image/compute/VPC/service role/buildspec define a privileged ephemeral build. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JN-02

- [ ] **Question:** What is Buildspec, and why does it matter in CodeBuild, CodePipeline and CodeDeploy?

**Answer:** phases/commands/artifacts/cache/reports are executable supply-chain code. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JN-03

- [ ] **Question:** What is Privileged mode, and why does it matter in CodeBuild, CodePipeline and CodeDeploy?

**Answer:** enables Docker daemon workflows but greatly expands runner attack surface. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JN-04

- [ ] **Question:** What is CodePipeline stage/action, and why does it matter in CodeBuild, CodePipeline and CodeDeploy?

**Answer:** orchestrates source/build/test/approval/deploy artifacts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JN-05

- [ ] **Question:** What is Artifact store, and why does it matter in CodeBuild, CodePipeline and CodeDeploy?

**Answer:** encrypted regional bucket must preserve exact immutable promotion inputs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JN-06

- [ ] **Question:** What is Manual approval, and why does it matter in CodeBuild, CodePipeline and CodeDeploy?

**Answer:** records a decision but needs useful evidence, expiry and authorized approvers. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JN-07

- [ ] **Question:** What is CodeDeploy deployment group, and why does it matter in CodeBuild, CodePipeline and CodeDeploy?

**Answer:** selects targets/strategy/alarms/rollback hooks. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JN-08

- [ ] **Code:** **Question:** What does `aws deploy get-deployment --deployment-id ID` help you verify for CodeBuild, CodePipeline and CodeDeploy?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: parallel replacement and traffic shift need state/schema compatibility.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JN-09

- [ ] **Code:** **Question:** What does `aws codebuild batch-get-builds --ids BUILD_ID` help you verify for CodeBuild, CodePipeline and CodeDeploy?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: validation scripts can gate traffic but must timeout/emit evidence.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JN-10

- [ ] **Code:** **Question:** What does `aws codepipeline get-pipeline-state --name PIPELINE` help you verify for CodeBuild, CodePipeline and CodeDeploy?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: source/build/deploy identities should not share broad long-lived credentials.

## Junior — procedural and command questions

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JP-01

- [ ] **Code:** **Question:** A basic CodeBuild project check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws codebuild batch-get-builds --ids BUILD_ID` and capture exact status/reason/request ID. image/compute/VPC/service role/buildspec define a privileged ephemeral build. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JP-02

- [ ] **Question:** A basic Buildspec check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws codepipeline get-pipeline-state --name PIPELINE` and capture exact status/reason/request ID. phases/commands/artifacts/cache/reports are executable supply-chain code. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JP-03

- [ ] **Question:** A basic Privileged mode check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws codepipeline list-action-executions --pipeline-name PIPELINE` and capture exact status/reason/request ID. enables Docker daemon workflows but greatly expands runner attack surface. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JP-04

- [ ] **Code:** **Question:** A basic CodePipeline stage/action check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws deploy get-deployment --deployment-id ID` and capture exact status/reason/request ID. orchestrates source/build/test/approval/deploy artifacts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JP-05

- [ ] **Question:** A basic Artifact store check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws codebuild batch-get-builds --ids BUILD_ID` and capture exact status/reason/request ID. encrypted regional bucket must preserve exact immutable promotion inputs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JP-06

- [ ] **Question:** A basic Manual approval check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws codepipeline get-pipeline-state --name PIPELINE` and capture exact status/reason/request ID. records a decision but needs useful evidence, expiry and authorized approvers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JP-07

- [ ] **Code:** **Question:** A basic CodeDeploy deployment group check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws codepipeline list-action-executions --pipeline-name PIPELINE` and capture exact status/reason/request ID. selects targets/strategy/alarms/rollback hooks. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JP-08

- [ ] **Question:** A basic Blue-green check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws deploy get-deployment --deployment-id ID` and capture exact status/reason/request ID. parallel replacement and traffic shift need state/schema compatibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JP-09

- [ ] **Question:** A basic Lifecycle hook check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws codebuild batch-get-builds --ids BUILD_ID` and capture exact status/reason/request ID. validation scripts can gate traffic but must timeout/emit evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-JP-10

- [ ] **Code:** **Question:** A basic OIDC/role separation check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws codepipeline get-pipeline-state --name PIPELINE` and capture exact status/reason/request ID. source/build/deploy identities should not share broad long-lived credentials. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MN-01

- [ ] **Question:** Compare CodeBuild project with Buildspec. When would each change your design?

**Answer:** CodeBuild project: image/compute/VPC/service role/buildspec define a privileged ephemeral build. Buildspec: phases/commands/artifacts/cache/reports are executable supply-chain code. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MN-02

- [ ] **Question:** Compare Buildspec with Privileged mode. When would each change your design?

**Answer:** Buildspec: phases/commands/artifacts/cache/reports are executable supply-chain code. Privileged mode: enables Docker daemon workflows but greatly expands runner attack surface. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MN-03

- [ ] **Question:** Compare Privileged mode with CodePipeline stage/action. When would each change your design?

**Answer:** Privileged mode: enables Docker daemon workflows but greatly expands runner attack surface. CodePipeline stage/action: orchestrates source/build/test/approval/deploy artifacts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MN-04

- [ ] **Configuration review:** **Question:** Compare CodePipeline stage/action with Artifact store. When would each change your design?

**Answer:** CodePipeline stage/action: orchestrates source/build/test/approval/deploy artifacts. Artifact store: encrypted regional bucket must preserve exact immutable promotion inputs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MN-05

- [ ] **Question:** Compare Artifact store with Manual approval. When would each change your design?

**Answer:** Artifact store: encrypted regional bucket must preserve exact immutable promotion inputs. Manual approval: records a decision but needs useful evidence, expiry and authorized approvers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MN-06

- [ ] **Question:** Compare Manual approval with CodeDeploy deployment group. When would each change your design?

**Answer:** Manual approval: records a decision but needs useful evidence, expiry and authorized approvers. CodeDeploy deployment group: selects targets/strategy/alarms/rollback hooks. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MN-07

- [ ] **Configuration review:** **Question:** Compare CodeDeploy deployment group with Blue-green. When would each change your design?

**Answer:** CodeDeploy deployment group: selects targets/strategy/alarms/rollback hooks. Blue-green: parallel replacement and traffic shift need state/schema compatibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MN-08

- [ ] **Question:** Compare Blue-green with Lifecycle hook. When would each change your design?

**Answer:** Blue-green: parallel replacement and traffic shift need state/schema compatibility. Lifecycle hook: validation scripts can gate traffic but must timeout/emit evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MN-09

- [ ] **Question:** Compare Lifecycle hook with OIDC/role separation. When would each change your design?

**Answer:** Lifecycle hook: validation scripts can gate traffic but must timeout/emit evidence. OIDC/role separation: source/build/deploy identities should not share broad long-lived credentials. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MN-10

- [ ] **Configuration review:** **Question:** Compare OIDC/role separation with CodeBuild project. When would each change your design?

**Answer:** OIDC/role separation: source/build/deploy identities should not share broad long-lived credentials. CodeBuild project: image/compute/VPC/service role/buildspec define a privileged ephemeral build. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around CodeBuild project; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws codebuild batch-get-builds --ids BUILD_ID` plus recent events/changes, then correlate the service-specific SLI. image/compute/VPC/service role/buildspec define a privileged ephemeral build. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MP-02

- [ ] **Question:** Production is degraded around Buildspec; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws codepipeline get-pipeline-state --name PIPELINE` plus recent events/changes, then correlate the service-specific SLI. phases/commands/artifacts/cache/reports are executable supply-chain code. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Privileged mode; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws codepipeline list-action-executions --pipeline-name PIPELINE` plus recent events/changes, then correlate the service-specific SLI. enables Docker daemon workflows but greatly expands runner attack surface. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MP-04

- [ ] **Question:** Production is degraded around CodePipeline stage/action; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws deploy get-deployment --deployment-id ID` plus recent events/changes, then correlate the service-specific SLI. orchestrates source/build/test/approval/deploy artifacts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Artifact store; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws codebuild batch-get-builds --ids BUILD_ID` plus recent events/changes, then correlate the service-specific SLI. encrypted regional bucket must preserve exact immutable promotion inputs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MP-06

- [ ] **Question:** Production is degraded around Manual approval; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws codepipeline get-pipeline-state --name PIPELINE` plus recent events/changes, then correlate the service-specific SLI. records a decision but needs useful evidence, expiry and authorized approvers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around CodeDeploy deployment group; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws codepipeline list-action-executions --pipeline-name PIPELINE` plus recent events/changes, then correlate the service-specific SLI. selects targets/strategy/alarms/rollback hooks. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MP-08

- [ ] **Question:** Production is degraded around Blue-green; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws deploy get-deployment --deployment-id ID` plus recent events/changes, then correlate the service-specific SLI. parallel replacement and traffic shift need state/schema compatibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Lifecycle hook; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws codebuild batch-get-builds --ids BUILD_ID` plus recent events/changes, then correlate the service-specific SLI. validation scripts can gate traffic but must timeout/emit evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-MP-10

- [ ] **Question:** Production is degraded around OIDC/role separation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws codepipeline get-pipeline-state --name PIPELINE` plus recent events/changes, then correlate the service-specific SLI. source/build/deploy identities should not share broad long-lived credentials. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SN-01

- [ ] **Question:** Design a production CodeBuild, CodePipeline and CodeDeploy capability where CodeBuild project, CodePipeline stage/action and CodeDeploy deployment group are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: image/compute/VPC/service role/buildspec define a privileged ephemeral build. orchestrates source/build/test/approval/deploy artifacts. selects targets/strategy/alarms/rollback hooks. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production CodeBuild, CodePipeline and CodeDeploy capability where Buildspec, Artifact store and Blue-green are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: phases/commands/artifacts/cache/reports are executable supply-chain code. encrypted regional bucket must preserve exact immutable promotion inputs. parallel replacement and traffic shift need state/schema compatibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SN-03

- [ ] **Question:** Design a production CodeBuild, CodePipeline and CodeDeploy capability where Privileged mode, Manual approval and Lifecycle hook are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: enables Docker daemon workflows but greatly expands runner attack surface. records a decision but needs useful evidence, expiry and authorized approvers. validation scripts can gate traffic but must timeout/emit evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production CodeBuild, CodePipeline and CodeDeploy capability where CodePipeline stage/action, CodeDeploy deployment group and OIDC/role separation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: orchestrates source/build/test/approval/deploy artifacts. selects targets/strategy/alarms/rollback hooks. source/build/deploy identities should not share broad long-lived credentials. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SN-05

- [ ] **Question:** Design a production CodeBuild, CodePipeline and CodeDeploy capability where Artifact store, Blue-green and CodeBuild project are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: encrypted regional bucket must preserve exact immutable promotion inputs. parallel replacement and traffic shift need state/schema compatibility. image/compute/VPC/service role/buildspec define a privileged ephemeral build. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production CodeBuild, CodePipeline and CodeDeploy capability where Manual approval, Lifecycle hook and Buildspec are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: records a decision but needs useful evidence, expiry and authorized approvers. validation scripts can gate traffic but must timeout/emit evidence. phases/commands/artifacts/cache/reports are executable supply-chain code. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SN-07

- [ ] **Question:** Design a production CodeBuild, CodePipeline and CodeDeploy capability where CodeDeploy deployment group, OIDC/role separation and Privileged mode are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: selects targets/strategy/alarms/rollback hooks. source/build/deploy identities should not share broad long-lived credentials. enables Docker daemon workflows but greatly expands runner attack surface. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production CodeBuild, CodePipeline and CodeDeploy capability where Blue-green, CodeBuild project and CodePipeline stage/action are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: parallel replacement and traffic shift need state/schema compatibility. image/compute/VPC/service role/buildspec define a privileged ephemeral build. orchestrates source/build/test/approval/deploy artifacts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SN-09

- [ ] **Question:** Design a production CodeBuild, CodePipeline and CodeDeploy capability where Lifecycle hook, Buildspec and Artifact store are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: validation scripts can gate traffic but must timeout/emit evidence. phases/commands/artifacts/cache/reports are executable supply-chain code. encrypted regional bucket must preserve exact immutable promotion inputs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production CodeBuild, CodePipeline and CodeDeploy capability where OIDC/role separation, Privileged mode and Manual approval are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: source/build/deploy identities should not share broad long-lived credentials. enables Docker daemon workflows but greatly expands runner attack surface. records a decision but needs useful evidence, expiry and authorized approvers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CodeBuild project. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws codebuild batch-get-builds --ids BUILD_ID` as one read-only checkpoint, not the whole diagnosis. image/compute/VPC/service role/buildspec define a privileged ephemeral build. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Buildspec. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws codepipeline get-pipeline-state --name PIPELINE` as one read-only checkpoint, not the whole diagnosis. phases/commands/artifacts/cache/reports are executable supply-chain code. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Privileged mode. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws codepipeline list-action-executions --pipeline-name PIPELINE` as one read-only checkpoint, not the whole diagnosis. enables Docker daemon workflows but greatly expands runner attack surface. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CodePipeline stage/action. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws deploy get-deployment --deployment-id ID` as one read-only checkpoint, not the whole diagnosis. orchestrates source/build/test/approval/deploy artifacts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Artifact store. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws codebuild batch-get-builds --ids BUILD_ID` as one read-only checkpoint, not the whole diagnosis. encrypted regional bucket must preserve exact immutable promotion inputs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Manual approval. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws codepipeline get-pipeline-state --name PIPELINE` as one read-only checkpoint, not the whole diagnosis. records a decision but needs useful evidence, expiry and authorized approvers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CodeDeploy deployment group. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws codepipeline list-action-executions --pipeline-name PIPELINE` as one read-only checkpoint, not the whole diagnosis. selects targets/strategy/alarms/rollback hooks. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Blue-green. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws deploy get-deployment --deployment-id ID` as one read-only checkpoint, not the whole diagnosis. parallel replacement and traffic shift need state/schema compatibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lifecycle hook. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws codebuild batch-get-builds --ids BUILD_ID` as one read-only checkpoint, not the whole diagnosis. validation scripts can gate traffic but must timeout/emit evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CODEBUILD-CODEPIPELINE-AND-CODEDEPLOY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving OIDC/role separation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws codepipeline get-pipeline-state --name PIPELINE` as one read-only checkpoint, not the whole diagnosis. source/build/deploy identities should not share broad long-lived credentials. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
