# AWS Service Catalog and Proton — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-SERVICE-CATALOG-AND-PROTON-JN-01

- [ ] **Question:** What is Portfolio/product, and why does it matter in AWS Service Catalog and Proton?

**Answer:** curated products and versions are shared to approved principals/accounts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SERVICE-CATALOG-AND-PROTON-JN-02

- [ ] **Question:** What is Launch constraint, and why does it matter in AWS Service Catalog and Proton?

**Answer:** service role separates user permission from provisioned-resource permission. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SERVICE-CATALOG-AND-PROTON-JN-03

- [ ] **Question:** What is Template constraint, and why does it matter in AWS Service Catalog and Proton?

**Answer:** restricts product parameters to policy-safe combinations. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SERVICE-CATALOG-AND-PROTON-JN-04

- [ ] **Question:** What is Provisioned product, and why does it matter in AWS Service Catalog and Proton?

**Answer:** launched stack/resource lifecycle needs owner/status/termination handling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SERVICE-CATALOG-AND-PROTON-JN-05

- [ ] **Question:** What is Product version, and why does it matter in AWS Service Catalog and Proton?

**Answer:** upgrades need compatibility, migration and deprecation communication. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SERVICE-CATALOG-AND-PROTON-JN-06

- [ ] **Question:** What is TagOptions, and why does it matter in AWS Service Catalog and Proton?

**Answer:** standardize tags but do not replace enforcement or runtime ownership. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SERVICE-CATALOG-AND-PROTON-JN-07

- [ ] **Question:** What is Proton environment, and why does it matter in AWS Service Catalog and Proton?

**Answer:** shared infrastructure context for service instances/templates. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SERVICE-CATALOG-AND-PROTON-JN-08

- [ ] **Code:** **Question:** What does `aws proton list-service-templates` help you verify for AWS Service Catalog and Proton?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: standardizes service pipeline/infrastructure under platform ownership.

### AWS-SERVICE-CATALOG-AND-PROTON-JN-09

- [ ] **Code:** **Question:** What does `aws servicecatalog search-products-as-admin` help you verify for AWS Service Catalog and Proton?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: integrates external IaC workflows and must reconcile status/failures.

### AWS-SERVICE-CATALOG-AND-PROTON-JN-10

- [ ] **Code:** **Question:** What does `aws servicecatalog scan-provisioned-products` help you verify for AWS Service Catalog and Proton?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: adoption, time-to-deploy, success, exceptions and toil measure product value.

## Junior — procedural and command questions

### AWS-SERVICE-CATALOG-AND-PROTON-JP-01

- [ ] **Code:** **Question:** A basic Portfolio/product check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws servicecatalog search-products-as-admin` and capture exact status/reason/request ID. curated products and versions are shared to approved principals/accounts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SERVICE-CATALOG-AND-PROTON-JP-02

- [ ] **Question:** A basic Launch constraint check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws servicecatalog scan-provisioned-products` and capture exact status/reason/request ID. service role separates user permission from provisioned-resource permission. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SERVICE-CATALOG-AND-PROTON-JP-03

- [ ] **Question:** A basic Template constraint check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws proton list-environments` and capture exact status/reason/request ID. restricts product parameters to policy-safe combinations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SERVICE-CATALOG-AND-PROTON-JP-04

- [ ] **Code:** **Question:** A basic Provisioned product check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws proton list-service-templates` and capture exact status/reason/request ID. launched stack/resource lifecycle needs owner/status/termination handling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SERVICE-CATALOG-AND-PROTON-JP-05

- [ ] **Question:** A basic Product version check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws servicecatalog search-products-as-admin` and capture exact status/reason/request ID. upgrades need compatibility, migration and deprecation communication. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SERVICE-CATALOG-AND-PROTON-JP-06

- [ ] **Question:** A basic TagOptions check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws servicecatalog scan-provisioned-products` and capture exact status/reason/request ID. standardize tags but do not replace enforcement or runtime ownership. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SERVICE-CATALOG-AND-PROTON-JP-07

- [ ] **Code:** **Question:** A basic Proton environment check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws proton list-environments` and capture exact status/reason/request ID. shared infrastructure context for service instances/templates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SERVICE-CATALOG-AND-PROTON-JP-08

- [ ] **Question:** A basic Service template check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws proton list-service-templates` and capture exact status/reason/request ID. standardizes service pipeline/infrastructure under platform ownership. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SERVICE-CATALOG-AND-PROTON-JP-09

- [ ] **Question:** A basic Self-managed provisioning check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws servicecatalog search-products-as-admin` and capture exact status/reason/request ID. integrates external IaC workflows and must reconcile status/failures. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SERVICE-CATALOG-AND-PROTON-JP-10

- [ ] **Code:** **Question:** A basic Golden-path metrics check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws servicecatalog scan-provisioned-products` and capture exact status/reason/request ID. adoption, time-to-deploy, success, exceptions and toil measure product value. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-SERVICE-CATALOG-AND-PROTON-MN-01

- [ ] **Question:** Compare Portfolio/product with Launch constraint. When would each change your design?

**Answer:** Portfolio/product: curated products and versions are shared to approved principals/accounts. Launch constraint: service role separates user permission from provisioned-resource permission. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SERVICE-CATALOG-AND-PROTON-MN-02

- [ ] **Question:** Compare Launch constraint with Template constraint. When would each change your design?

**Answer:** Launch constraint: service role separates user permission from provisioned-resource permission. Template constraint: restricts product parameters to policy-safe combinations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SERVICE-CATALOG-AND-PROTON-MN-03

- [ ] **Question:** Compare Template constraint with Provisioned product. When would each change your design?

**Answer:** Template constraint: restricts product parameters to policy-safe combinations. Provisioned product: launched stack/resource lifecycle needs owner/status/termination handling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SERVICE-CATALOG-AND-PROTON-MN-04

- [ ] **Configuration review:** **Question:** Compare Provisioned product with Product version. When would each change your design?

**Answer:** Provisioned product: launched stack/resource lifecycle needs owner/status/termination handling. Product version: upgrades need compatibility, migration and deprecation communication. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SERVICE-CATALOG-AND-PROTON-MN-05

- [ ] **Question:** Compare Product version with TagOptions. When would each change your design?

**Answer:** Product version: upgrades need compatibility, migration and deprecation communication. TagOptions: standardize tags but do not replace enforcement or runtime ownership. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SERVICE-CATALOG-AND-PROTON-MN-06

- [ ] **Question:** Compare TagOptions with Proton environment. When would each change your design?

**Answer:** TagOptions: standardize tags but do not replace enforcement or runtime ownership. Proton environment: shared infrastructure context for service instances/templates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SERVICE-CATALOG-AND-PROTON-MN-07

- [ ] **Configuration review:** **Question:** Compare Proton environment with Service template. When would each change your design?

**Answer:** Proton environment: shared infrastructure context for service instances/templates. Service template: standardizes service pipeline/infrastructure under platform ownership. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SERVICE-CATALOG-AND-PROTON-MN-08

- [ ] **Question:** Compare Service template with Self-managed provisioning. When would each change your design?

**Answer:** Service template: standardizes service pipeline/infrastructure under platform ownership. Self-managed provisioning: integrates external IaC workflows and must reconcile status/failures. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SERVICE-CATALOG-AND-PROTON-MN-09

- [ ] **Question:** Compare Self-managed provisioning with Golden-path metrics. When would each change your design?

**Answer:** Self-managed provisioning: integrates external IaC workflows and must reconcile status/failures. Golden-path metrics: adoption, time-to-deploy, success, exceptions and toil measure product value. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SERVICE-CATALOG-AND-PROTON-MN-10

- [ ] **Configuration review:** **Question:** Compare Golden-path metrics with Portfolio/product. When would each change your design?

**Answer:** Golden-path metrics: adoption, time-to-deploy, success, exceptions and toil measure product value. Portfolio/product: curated products and versions are shared to approved principals/accounts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-SERVICE-CATALOG-AND-PROTON-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Portfolio/product; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws servicecatalog search-products-as-admin` plus recent events/changes, then correlate the service-specific SLI. curated products and versions are shared to approved principals/accounts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SERVICE-CATALOG-AND-PROTON-MP-02

- [ ] **Question:** Production is degraded around Launch constraint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws servicecatalog scan-provisioned-products` plus recent events/changes, then correlate the service-specific SLI. service role separates user permission from provisioned-resource permission. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SERVICE-CATALOG-AND-PROTON-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Template constraint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws proton list-environments` plus recent events/changes, then correlate the service-specific SLI. restricts product parameters to policy-safe combinations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SERVICE-CATALOG-AND-PROTON-MP-04

- [ ] **Question:** Production is degraded around Provisioned product; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws proton list-service-templates` plus recent events/changes, then correlate the service-specific SLI. launched stack/resource lifecycle needs owner/status/termination handling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SERVICE-CATALOG-AND-PROTON-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Product version; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws servicecatalog search-products-as-admin` plus recent events/changes, then correlate the service-specific SLI. upgrades need compatibility, migration and deprecation communication. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SERVICE-CATALOG-AND-PROTON-MP-06

- [ ] **Question:** Production is degraded around TagOptions; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws servicecatalog scan-provisioned-products` plus recent events/changes, then correlate the service-specific SLI. standardize tags but do not replace enforcement or runtime ownership. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SERVICE-CATALOG-AND-PROTON-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Proton environment; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws proton list-environments` plus recent events/changes, then correlate the service-specific SLI. shared infrastructure context for service instances/templates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SERVICE-CATALOG-AND-PROTON-MP-08

- [ ] **Question:** Production is degraded around Service template; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws proton list-service-templates` plus recent events/changes, then correlate the service-specific SLI. standardizes service pipeline/infrastructure under platform ownership. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SERVICE-CATALOG-AND-PROTON-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Self-managed provisioning; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws servicecatalog search-products-as-admin` plus recent events/changes, then correlate the service-specific SLI. integrates external IaC workflows and must reconcile status/failures. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SERVICE-CATALOG-AND-PROTON-MP-10

- [ ] **Question:** Production is degraded around Golden-path metrics; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws servicecatalog scan-provisioned-products` plus recent events/changes, then correlate the service-specific SLI. adoption, time-to-deploy, success, exceptions and toil measure product value. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-SERVICE-CATALOG-AND-PROTON-SN-01

- [ ] **Question:** Design a production AWS Service Catalog and Proton capability where Portfolio/product, Provisioned product and Proton environment are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: curated products and versions are shared to approved principals/accounts. launched stack/resource lifecycle needs owner/status/termination handling. shared infrastructure context for service instances/templates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SERVICE-CATALOG-AND-PROTON-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Service Catalog and Proton capability where Launch constraint, Product version and Service template are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: service role separates user permission from provisioned-resource permission. upgrades need compatibility, migration and deprecation communication. standardizes service pipeline/infrastructure under platform ownership. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SERVICE-CATALOG-AND-PROTON-SN-03

- [ ] **Question:** Design a production AWS Service Catalog and Proton capability where Template constraint, TagOptions and Self-managed provisioning are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: restricts product parameters to policy-safe combinations. standardize tags but do not replace enforcement or runtime ownership. integrates external IaC workflows and must reconcile status/failures. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SERVICE-CATALOG-AND-PROTON-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Service Catalog and Proton capability where Provisioned product, Proton environment and Golden-path metrics are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: launched stack/resource lifecycle needs owner/status/termination handling. shared infrastructure context for service instances/templates. adoption, time-to-deploy, success, exceptions and toil measure product value. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SERVICE-CATALOG-AND-PROTON-SN-05

- [ ] **Question:** Design a production AWS Service Catalog and Proton capability where Product version, Service template and Portfolio/product are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: upgrades need compatibility, migration and deprecation communication. standardizes service pipeline/infrastructure under platform ownership. curated products and versions are shared to approved principals/accounts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SERVICE-CATALOG-AND-PROTON-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Service Catalog and Proton capability where TagOptions, Self-managed provisioning and Launch constraint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: standardize tags but do not replace enforcement or runtime ownership. integrates external IaC workflows and must reconcile status/failures. service role separates user permission from provisioned-resource permission. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SERVICE-CATALOG-AND-PROTON-SN-07

- [ ] **Question:** Design a production AWS Service Catalog and Proton capability where Proton environment, Golden-path metrics and Template constraint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: shared infrastructure context for service instances/templates. adoption, time-to-deploy, success, exceptions and toil measure product value. restricts product parameters to policy-safe combinations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SERVICE-CATALOG-AND-PROTON-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Service Catalog and Proton capability where Service template, Portfolio/product and Provisioned product are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: standardizes service pipeline/infrastructure under platform ownership. curated products and versions are shared to approved principals/accounts. launched stack/resource lifecycle needs owner/status/termination handling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SERVICE-CATALOG-AND-PROTON-SN-09

- [ ] **Question:** Design a production AWS Service Catalog and Proton capability where Self-managed provisioning, Launch constraint and Product version are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: integrates external IaC workflows and must reconcile status/failures. service role separates user permission from provisioned-resource permission. upgrades need compatibility, migration and deprecation communication. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SERVICE-CATALOG-AND-PROTON-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Service Catalog and Proton capability where Golden-path metrics, Template constraint and TagOptions are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: adoption, time-to-deploy, success, exceptions and toil measure product value. restricts product parameters to policy-safe combinations. standardize tags but do not replace enforcement or runtime ownership. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-SERVICE-CATALOG-AND-PROTON-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Portfolio/product. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws servicecatalog search-products-as-admin` as one read-only checkpoint, not the whole diagnosis. curated products and versions are shared to approved principals/accounts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SERVICE-CATALOG-AND-PROTON-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Launch constraint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws servicecatalog scan-provisioned-products` as one read-only checkpoint, not the whole diagnosis. service role separates user permission from provisioned-resource permission. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SERVICE-CATALOG-AND-PROTON-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Template constraint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws proton list-environments` as one read-only checkpoint, not the whole diagnosis. restricts product parameters to policy-safe combinations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SERVICE-CATALOG-AND-PROTON-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Provisioned product. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws proton list-service-templates` as one read-only checkpoint, not the whole diagnosis. launched stack/resource lifecycle needs owner/status/termination handling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SERVICE-CATALOG-AND-PROTON-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Product version. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws servicecatalog search-products-as-admin` as one read-only checkpoint, not the whole diagnosis. upgrades need compatibility, migration and deprecation communication. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SERVICE-CATALOG-AND-PROTON-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TagOptions. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws servicecatalog scan-provisioned-products` as one read-only checkpoint, not the whole diagnosis. standardize tags but do not replace enforcement or runtime ownership. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SERVICE-CATALOG-AND-PROTON-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Proton environment. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws proton list-environments` as one read-only checkpoint, not the whole diagnosis. shared infrastructure context for service instances/templates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SERVICE-CATALOG-AND-PROTON-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service template. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws proton list-service-templates` as one read-only checkpoint, not the whole diagnosis. standardizes service pipeline/infrastructure under platform ownership. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SERVICE-CATALOG-AND-PROTON-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Self-managed provisioning. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws servicecatalog search-products-as-admin` as one read-only checkpoint, not the whole diagnosis. integrates external IaC workflows and must reconcile status/failures. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SERVICE-CATALOG-AND-PROTON-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Golden-path metrics. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws servicecatalog scan-provisioned-products` as one read-only checkpoint, not the whole diagnosis. adoption, time-to-deploy, success, exceptions and toil measure product value. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
