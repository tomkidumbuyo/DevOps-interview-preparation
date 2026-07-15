# Infrastructure Delivery — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-INFRASTRUCTURE-DELIVERY-JN-01

- [ ] **Question:** What is Stack, and why does it matter in Infrastructure Delivery?

**Answer:** ownership/lifecycle boundary for a set of resources and outputs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INFRASTRUCTURE-DELIVERY-JN-02

- [ ] **Question:** What is Change set, and why does it matter in Infrastructure Delivery?

**Answer:** previews create/update/import actions but cannot predict every service-side effect. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INFRASTRUCTURE-DELIVERY-JN-03

- [ ] **Question:** What is App/stack/construct tree, and why does it matter in Infrastructure Delivery?

**Answer:** code composes logical resources and ownership hierarchy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INFRASTRUCTURE-DELIVERY-JN-04

- [ ] **Question:** What is L1 construct, and why does it matter in Infrastructure Delivery?

**Answer:** direct generated CloudFormation resource mapping. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INFRASTRUCTURE-DELIVERY-JN-05

- [ ] **Question:** What is CodeBuild project, and why does it matter in Infrastructure Delivery?

**Answer:** image/compute/VPC/service role/buildspec define a privileged ephemeral build. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INFRASTRUCTURE-DELIVERY-JN-06

- [ ] **Question:** What is Buildspec, and why does it matter in Infrastructure Delivery?

**Answer:** phases/commands/artifacts/cache/reports are executable supply-chain code. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INFRASTRUCTURE-DELIVERY-JN-07

- [ ] **Question:** What is Portfolio/product, and why does it matter in Infrastructure Delivery?

**Answer:** curated products and versions are shared to approved principals/accounts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INFRASTRUCTURE-DELIVERY-JN-08

- [ ] **Code:** **Question:** What does `aws servicecatalog search-products-as-admin` help you verify for Infrastructure Delivery?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: service role separates user permission from provisioned-resource permission.

### BRANCH-INFRASTRUCTURE-DELIVERY-JN-09

- [ ] **Code:** **Question:** What does `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` help you verify for Infrastructure Delivery?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: ownership/lifecycle boundary for a set of resources and outputs.

### BRANCH-INFRASTRUCTURE-DELIVERY-JN-10

- [ ] **Code:** **Question:** What does `cdk synth` help you verify for Infrastructure Delivery?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: previews create/update/import actions but cannot predict every service-side effect.

## Junior — procedural and command questions

### BRANCH-INFRASTRUCTURE-DELIVERY-JP-01

- [ ] **Code:** **Question:** A basic Stack check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` and capture exact status/reason/request ID. ownership/lifecycle boundary for a set of resources and outputs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INFRASTRUCTURE-DELIVERY-JP-02

- [ ] **Question:** A basic Change set check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk synth` and capture exact status/reason/request ID. previews create/update/import actions but cannot predict every service-side effect. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INFRASTRUCTURE-DELIVERY-JP-03

- [ ] **Question:** A basic App/stack/construct tree check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws codebuild batch-get-builds --ids BUILD_ID` and capture exact status/reason/request ID. code composes logical resources and ownership hierarchy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INFRASTRUCTURE-DELIVERY-JP-04

- [ ] **Code:** **Question:** A basic L1 construct check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws servicecatalog search-products-as-admin` and capture exact status/reason/request ID. direct generated CloudFormation resource mapping. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INFRASTRUCTURE-DELIVERY-JP-05

- [ ] **Question:** A basic CodeBuild project check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` and capture exact status/reason/request ID. image/compute/VPC/service role/buildspec define a privileged ephemeral build. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INFRASTRUCTURE-DELIVERY-JP-06

- [ ] **Question:** A basic Buildspec check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk synth` and capture exact status/reason/request ID. phases/commands/artifacts/cache/reports are executable supply-chain code. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INFRASTRUCTURE-DELIVERY-JP-07

- [ ] **Code:** **Question:** A basic Portfolio/product check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws codebuild batch-get-builds --ids BUILD_ID` and capture exact status/reason/request ID. curated products and versions are shared to approved principals/accounts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INFRASTRUCTURE-DELIVERY-JP-08

- [ ] **Question:** A basic Launch constraint check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws servicecatalog search-products-as-admin` and capture exact status/reason/request ID. service role separates user permission from provisioned-resource permission. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INFRASTRUCTURE-DELIVERY-JP-09

- [ ] **Question:** A basic Stack check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` and capture exact status/reason/request ID. ownership/lifecycle boundary for a set of resources and outputs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INFRASTRUCTURE-DELIVERY-JP-10

- [ ] **Code:** **Question:** A basic Change set check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk synth` and capture exact status/reason/request ID. previews create/update/import actions but cannot predict every service-side effect. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-INFRASTRUCTURE-DELIVERY-MN-01

- [ ] **Question:** Compare Stack with Change set. When would each change your design?

**Answer:** Stack: ownership/lifecycle boundary for a set of resources and outputs. Change set: previews create/update/import actions but cannot predict every service-side effect. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INFRASTRUCTURE-DELIVERY-MN-02

- [ ] **Question:** Compare Change set with App/stack/construct tree. When would each change your design?

**Answer:** Change set: previews create/update/import actions but cannot predict every service-side effect. App/stack/construct tree: code composes logical resources and ownership hierarchy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INFRASTRUCTURE-DELIVERY-MN-03

- [ ] **Question:** Compare App/stack/construct tree with L1 construct. When would each change your design?

**Answer:** App/stack/construct tree: code composes logical resources and ownership hierarchy. L1 construct: direct generated CloudFormation resource mapping. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INFRASTRUCTURE-DELIVERY-MN-04

- [ ] **Configuration review:** **Question:** Compare L1 construct with CodeBuild project. When would each change your design?

**Answer:** L1 construct: direct generated CloudFormation resource mapping. CodeBuild project: image/compute/VPC/service role/buildspec define a privileged ephemeral build. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INFRASTRUCTURE-DELIVERY-MN-05

- [ ] **Question:** Compare CodeBuild project with Buildspec. When would each change your design?

**Answer:** CodeBuild project: image/compute/VPC/service role/buildspec define a privileged ephemeral build. Buildspec: phases/commands/artifacts/cache/reports are executable supply-chain code. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INFRASTRUCTURE-DELIVERY-MN-06

- [ ] **Question:** Compare Buildspec with Portfolio/product. When would each change your design?

**Answer:** Buildspec: phases/commands/artifacts/cache/reports are executable supply-chain code. Portfolio/product: curated products and versions are shared to approved principals/accounts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INFRASTRUCTURE-DELIVERY-MN-07

- [ ] **Configuration review:** **Question:** Compare Portfolio/product with Launch constraint. When would each change your design?

**Answer:** Portfolio/product: curated products and versions are shared to approved principals/accounts. Launch constraint: service role separates user permission from provisioned-resource permission. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INFRASTRUCTURE-DELIVERY-MN-08

- [ ] **Question:** Compare Launch constraint with Stack. When would each change your design?

**Answer:** Launch constraint: service role separates user permission from provisioned-resource permission. Stack: ownership/lifecycle boundary for a set of resources and outputs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INFRASTRUCTURE-DELIVERY-MN-09

- [ ] **Question:** Compare Stack with Change set. When would each change your design?

**Answer:** Stack: ownership/lifecycle boundary for a set of resources and outputs. Change set: previews create/update/import actions but cannot predict every service-side effect. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INFRASTRUCTURE-DELIVERY-MN-10

- [ ] **Configuration review:** **Question:** Compare Change set with Stack. When would each change your design?

**Answer:** Change set: previews create/update/import actions but cannot predict every service-side effect. Stack: ownership/lifecycle boundary for a set of resources and outputs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-INFRASTRUCTURE-DELIVERY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Stack; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` plus recent events/changes, then correlate the service-specific SLI. ownership/lifecycle boundary for a set of resources and outputs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INFRASTRUCTURE-DELIVERY-MP-02

- [ ] **Question:** Production is degraded around Change set; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk synth` plus recent events/changes, then correlate the service-specific SLI. previews create/update/import actions but cannot predict every service-side effect. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INFRASTRUCTURE-DELIVERY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around App/stack/construct tree; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws codebuild batch-get-builds --ids BUILD_ID` plus recent events/changes, then correlate the service-specific SLI. code composes logical resources and ownership hierarchy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INFRASTRUCTURE-DELIVERY-MP-04

- [ ] **Question:** Production is degraded around L1 construct; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws servicecatalog search-products-as-admin` plus recent events/changes, then correlate the service-specific SLI. direct generated CloudFormation resource mapping. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INFRASTRUCTURE-DELIVERY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around CodeBuild project; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` plus recent events/changes, then correlate the service-specific SLI. image/compute/VPC/service role/buildspec define a privileged ephemeral build. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INFRASTRUCTURE-DELIVERY-MP-06

- [ ] **Question:** Production is degraded around Buildspec; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk synth` plus recent events/changes, then correlate the service-specific SLI. phases/commands/artifacts/cache/reports are executable supply-chain code. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INFRASTRUCTURE-DELIVERY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Portfolio/product; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws codebuild batch-get-builds --ids BUILD_ID` plus recent events/changes, then correlate the service-specific SLI. curated products and versions are shared to approved principals/accounts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INFRASTRUCTURE-DELIVERY-MP-08

- [ ] **Question:** Production is degraded around Launch constraint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws servicecatalog search-products-as-admin` plus recent events/changes, then correlate the service-specific SLI. service role separates user permission from provisioned-resource permission. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INFRASTRUCTURE-DELIVERY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Stack; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` plus recent events/changes, then correlate the service-specific SLI. ownership/lifecycle boundary for a set of resources and outputs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INFRASTRUCTURE-DELIVERY-MP-10

- [ ] **Question:** Production is degraded around Change set; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk synth` plus recent events/changes, then correlate the service-specific SLI. previews create/update/import actions but cannot predict every service-side effect. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-INFRASTRUCTURE-DELIVERY-SN-01

- [ ] **Question:** Design a production Infrastructure Delivery capability where Stack, L1 construct and Portfolio/product are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ownership/lifecycle boundary for a set of resources and outputs. direct generated CloudFormation resource mapping. curated products and versions are shared to approved principals/accounts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INFRASTRUCTURE-DELIVERY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Infrastructure Delivery capability where Change set, CodeBuild project and Launch constraint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: previews create/update/import actions but cannot predict every service-side effect. image/compute/VPC/service role/buildspec define a privileged ephemeral build. service role separates user permission from provisioned-resource permission. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INFRASTRUCTURE-DELIVERY-SN-03

- [ ] **Question:** Design a production Infrastructure Delivery capability where App/stack/construct tree, Buildspec and Stack are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: code composes logical resources and ownership hierarchy. phases/commands/artifacts/cache/reports are executable supply-chain code. ownership/lifecycle boundary for a set of resources and outputs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INFRASTRUCTURE-DELIVERY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Infrastructure Delivery capability where L1 construct, Portfolio/product and Change set are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: direct generated CloudFormation resource mapping. curated products and versions are shared to approved principals/accounts. previews create/update/import actions but cannot predict every service-side effect. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INFRASTRUCTURE-DELIVERY-SN-05

- [ ] **Question:** Design a production Infrastructure Delivery capability where CodeBuild project, Launch constraint and Stack are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: image/compute/VPC/service role/buildspec define a privileged ephemeral build. service role separates user permission from provisioned-resource permission. ownership/lifecycle boundary for a set of resources and outputs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INFRASTRUCTURE-DELIVERY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Infrastructure Delivery capability where Buildspec, Stack and Change set are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: phases/commands/artifacts/cache/reports are executable supply-chain code. ownership/lifecycle boundary for a set of resources and outputs. previews create/update/import actions but cannot predict every service-side effect. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INFRASTRUCTURE-DELIVERY-SN-07

- [ ] **Question:** Design a production Infrastructure Delivery capability where Portfolio/product, Change set and App/stack/construct tree are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: curated products and versions are shared to approved principals/accounts. previews create/update/import actions but cannot predict every service-side effect. code composes logical resources and ownership hierarchy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INFRASTRUCTURE-DELIVERY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Infrastructure Delivery capability where Launch constraint, Stack and L1 construct are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: service role separates user permission from provisioned-resource permission. ownership/lifecycle boundary for a set of resources and outputs. direct generated CloudFormation resource mapping. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INFRASTRUCTURE-DELIVERY-SN-09

- [ ] **Question:** Design a production Infrastructure Delivery capability where Stack, Change set and CodeBuild project are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ownership/lifecycle boundary for a set of resources and outputs. previews create/update/import actions but cannot predict every service-side effect. image/compute/VPC/service role/buildspec define a privileged ephemeral build. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INFRASTRUCTURE-DELIVERY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Infrastructure Delivery capability where Change set, App/stack/construct tree and Buildspec are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: previews create/update/import actions but cannot predict every service-side effect. code composes logical resources and ownership hierarchy. phases/commands/artifacts/cache/reports are executable supply-chain code. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-INFRASTRUCTURE-DELIVERY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stack. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` as one read-only checkpoint, not the whole diagnosis. ownership/lifecycle boundary for a set of resources and outputs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INFRASTRUCTURE-DELIVERY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Change set. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk synth` as one read-only checkpoint, not the whole diagnosis. previews create/update/import actions but cannot predict every service-side effect. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INFRASTRUCTURE-DELIVERY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving App/stack/construct tree. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws codebuild batch-get-builds --ids BUILD_ID` as one read-only checkpoint, not the whole diagnosis. code composes logical resources and ownership hierarchy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INFRASTRUCTURE-DELIVERY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving L1 construct. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws servicecatalog search-products-as-admin` as one read-only checkpoint, not the whole diagnosis. direct generated CloudFormation resource mapping. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INFRASTRUCTURE-DELIVERY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CodeBuild project. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` as one read-only checkpoint, not the whole diagnosis. image/compute/VPC/service role/buildspec define a privileged ephemeral build. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INFRASTRUCTURE-DELIVERY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Buildspec. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk synth` as one read-only checkpoint, not the whole diagnosis. phases/commands/artifacts/cache/reports are executable supply-chain code. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INFRASTRUCTURE-DELIVERY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Portfolio/product. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws codebuild batch-get-builds --ids BUILD_ID` as one read-only checkpoint, not the whole diagnosis. curated products and versions are shared to approved principals/accounts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INFRASTRUCTURE-DELIVERY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Launch constraint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws servicecatalog search-products-as-admin` as one read-only checkpoint, not the whole diagnosis. service role separates user permission from provisioned-resource permission. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INFRASTRUCTURE-DELIVERY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stack. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE` as one read-only checkpoint, not the whole diagnosis. ownership/lifecycle boundary for a set of resources and outputs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INFRASTRUCTURE-DELIVERY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Change set. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk synth` as one read-only checkpoint, not the whole diagnosis. previews create/update/import actions but cannot predict every service-side effect. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
