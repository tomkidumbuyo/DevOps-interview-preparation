# AWS IAM — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-IAM-JN-01

- [ ] **Question:** What is Principals, and why does it matter in AWS IAM?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-IAM-JN-02

- [ ] **Question:** What is Identity policies, and why does it matter in AWS IAM?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** attached policies grant or deny actions to a principal within the rest of the policy intersection. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-IAM-JN-03

- [ ] **Question:** What is Resource policies, and why does it matter in AWS IAM?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** supported resources can trust principals directly and express cross-account or service access. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-IAM-JN-04

- [ ] **Question:** What is Explicit deny, and why does it matter in AWS IAM?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** any applicable explicit deny overrides allows and is the first guardrail to search during diagnosis. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-IAM-JN-05

- [ ] **Question:** What is Permissions boundaries, and why does it matter in AWS IAM?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** cap identity-policy permissions without granting actions themselves. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-IAM-JN-06

- [ ] **Question:** What is Session policies, and why does it matter in AWS IAM?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** further restrict an assumed-role session and can explain access that differs from the base role. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-IAM-JN-07

- [ ] **Question:** What is Condition keys, and why does it matter in AWS IAM?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** bind access to organization, source network, tags, MFA, audience and other request context. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-IAM-JN-08

- [ ] **Code:** **Question:** What does `aws iam get-account-authorization-details` help you verify for AWS IAM?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: validates policies and analyzes external/internal access paths for supported resources.

### AWS-IAM-JN-09

- [ ] **Code:** **Question:** What does `aws sts get-caller-identity` help you verify for AWS IAM?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: start from task/resource/condition needs, observe actual use, remove unused access and review exceptions.

### AWS-IAM-JN-10

- [ ] **Code:** **Question:** What does `aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION` help you verify for AWS IAM?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: permission to attach a powerful role to a service can be equivalent to using that role indirectly.

## Junior — procedural and command questions

### AWS-IAM-JP-01

- [ ] **Code:** **Question:** A basic Principals check fails. What would you do first using the CLI?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts get-caller-identity` and capture exact status/reason/request ID. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-IAM-JP-02

- [ ] **Question:** A basic Identity policies check fails. What would you do first?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION` and capture exact status/reason/request ID. attached policies grant or deny actions to a principal within the rest of the policy intersection. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-IAM-JP-03

- [ ] **Question:** A basic Resource policies check fails. What would you do first?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws accessanalyzer validate-policy --policy-document file://policy.json --policy-type IDENTITY_POLICY` and capture exact status/reason/request ID. supported resources can trust principals directly and express cross-account or service access. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-IAM-JP-04

- [ ] **Code:** **Question:** A basic Explicit deny check fails. What would you do first using the CLI?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws iam get-account-authorization-details` and capture exact status/reason/request ID. any applicable explicit deny overrides allows and is the first guardrail to search during diagnosis. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-IAM-JP-05

- [ ] **Question:** A basic Permissions boundaries check fails. What would you do first?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts get-caller-identity` and capture exact status/reason/request ID. cap identity-policy permissions without granting actions themselves. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-IAM-JP-06

- [ ] **Question:** A basic Session policies check fails. What would you do first?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION` and capture exact status/reason/request ID. further restrict an assumed-role session and can explain access that differs from the base role. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-IAM-JP-07

- [ ] **Code:** **Question:** A basic Condition keys check fails. What would you do first using the CLI?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws accessanalyzer validate-policy --policy-document file://policy.json --policy-type IDENTITY_POLICY` and capture exact status/reason/request ID. bind access to organization, source network, tags, MFA, audience and other request context. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-IAM-JP-08

- [ ] **Question:** A basic Access Analyzer check fails. What would you do first?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws iam get-account-authorization-details` and capture exact status/reason/request ID. validates policies and analyzes external/internal access paths for supported resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-IAM-JP-09

- [ ] **Question:** A basic Least privilege check fails. What would you do first?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts get-caller-identity` and capture exact status/reason/request ID. start from task/resource/condition needs, observe actual use, remove unused access and review exceptions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-IAM-JP-10

- [ ] **Code:** **Question:** A basic PassRole escalation check fails. What would you do first using the CLI?
> **Covered in:** [AWS IAM — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION` and capture exact status/reason/request ID. permission to attach a powerful role to a service can be equivalent to using that role indirectly. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-IAM-MN-01

- [ ] **Question:** Compare Principals with Identity policies. When would each change your design?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Principals: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Identity policies: attached policies grant or deny actions to a principal within the rest of the policy intersection. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-IAM-MN-02

- [ ] **Question:** Compare Identity policies with Resource policies. When would each change your design?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Identity policies: attached policies grant or deny actions to a principal within the rest of the policy intersection. Resource policies: supported resources can trust principals directly and express cross-account or service access. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-IAM-MN-03

- [ ] **Question:** Compare Resource policies with Explicit deny. When would each change your design?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Resource policies: supported resources can trust principals directly and express cross-account or service access. Explicit deny: any applicable explicit deny overrides allows and is the first guardrail to search during diagnosis. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-IAM-MN-04

- [ ] **Configuration review:** **Question:** Compare Explicit deny with Permissions boundaries. When would each change your design?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Explicit deny: any applicable explicit deny overrides allows and is the first guardrail to search during diagnosis. Permissions boundaries: cap identity-policy permissions without granting actions themselves. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-IAM-MN-05

- [ ] **Question:** Compare Permissions boundaries with Session policies. When would each change your design?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Permissions boundaries: cap identity-policy permissions without granting actions themselves. Session policies: further restrict an assumed-role session and can explain access that differs from the base role. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-IAM-MN-06

- [ ] **Question:** Compare Session policies with Condition keys. When would each change your design?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Session policies: further restrict an assumed-role session and can explain access that differs from the base role. Condition keys: bind access to organization, source network, tags, MFA, audience and other request context. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-IAM-MN-07

- [ ] **Configuration review:** **Question:** Compare Condition keys with Access Analyzer. When would each change your design?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Condition keys: bind access to organization, source network, tags, MFA, audience and other request context. Access Analyzer: validates policies and analyzes external/internal access paths for supported resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-IAM-MN-08

- [ ] **Question:** Compare Access Analyzer with Least privilege. When would each change your design?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Access Analyzer: validates policies and analyzes external/internal access paths for supported resources. Least privilege: start from task/resource/condition needs, observe actual use, remove unused access and review exceptions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-IAM-MN-09

- [ ] **Question:** Compare Least privilege with PassRole escalation. When would each change your design?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Least privilege: start from task/resource/condition needs, observe actual use, remove unused access and review exceptions. PassRole escalation: permission to attach a powerful role to a service can be equivalent to using that role indirectly. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-IAM-MN-10

- [ ] **Configuration review:** **Question:** Compare PassRole escalation with Principals. When would each change your design?
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** PassRole escalation: permission to attach a powerful role to a service can be equivalent to using that role indirectly. Principals: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-IAM-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Principals; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts get-caller-identity` plus recent events/changes, then correlate the service-specific SLI. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-IAM-MP-02

- [ ] **Question:** Production is degraded around Identity policies; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION` plus recent events/changes, then correlate the service-specific SLI. attached policies grant or deny actions to a principal within the rest of the policy intersection. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-IAM-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Resource policies; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws accessanalyzer validate-policy --policy-document file://policy.json --policy-type IDENTITY_POLICY` plus recent events/changes, then correlate the service-specific SLI. supported resources can trust principals directly and express cross-account or service access. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-IAM-MP-04

- [ ] **Question:** Production is degraded around Explicit deny; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws iam get-account-authorization-details` plus recent events/changes, then correlate the service-specific SLI. any applicable explicit deny overrides allows and is the first guardrail to search during diagnosis. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-IAM-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Permissions boundaries; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts get-caller-identity` plus recent events/changes, then correlate the service-specific SLI. cap identity-policy permissions without granting actions themselves. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-IAM-MP-06

- [ ] **Question:** Production is degraded around Session policies; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION` plus recent events/changes, then correlate the service-specific SLI. further restrict an assumed-role session and can explain access that differs from the base role. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-IAM-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Condition keys; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws accessanalyzer validate-policy --policy-document file://policy.json --policy-type IDENTITY_POLICY` plus recent events/changes, then correlate the service-specific SLI. bind access to organization, source network, tags, MFA, audience and other request context. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-IAM-MP-08

- [ ] **Question:** Production is degraded around Access Analyzer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws iam get-account-authorization-details` plus recent events/changes, then correlate the service-specific SLI. validates policies and analyzes external/internal access paths for supported resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-IAM-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Least privilege; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts get-caller-identity` plus recent events/changes, then correlate the service-specific SLI. start from task/resource/condition needs, observe actual use, remove unused access and review exceptions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-IAM-MP-10

- [ ] **Question:** Production is degraded around PassRole escalation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION` plus recent events/changes, then correlate the service-specific SLI. permission to attach a powerful role to a service can be equivalent to using that role indirectly. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-IAM-SN-01

- [ ] **Question:** Design a production AWS IAM capability where Principals, Explicit deny and Condition keys are first-class requirements.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. any applicable explicit deny overrides allows and is the first guardrail to search during diagnosis. bind access to organization, source network, tags, MFA, audience and other request context. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-IAM-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS IAM capability where Identity policies, Permissions boundaries and Access Analyzer are first-class requirements.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: attached policies grant or deny actions to a principal within the rest of the policy intersection. cap identity-policy permissions without granting actions themselves. validates policies and analyzes external/internal access paths for supported resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-IAM-SN-03

- [ ] **Question:** Design a production AWS IAM capability where Resource policies, Session policies and Least privilege are first-class requirements.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supported resources can trust principals directly and express cross-account or service access. further restrict an assumed-role session and can explain access that differs from the base role. start from task/resource/condition needs, observe actual use, remove unused access and review exceptions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-IAM-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS IAM capability where Explicit deny, Condition keys and PassRole escalation are first-class requirements.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: any applicable explicit deny overrides allows and is the first guardrail to search during diagnosis. bind access to organization, source network, tags, MFA, audience and other request context. permission to attach a powerful role to a service can be equivalent to using that role indirectly. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-IAM-SN-05

- [ ] **Question:** Design a production AWS IAM capability where Permissions boundaries, Access Analyzer and Principals are first-class requirements.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cap identity-policy permissions without granting actions themselves. validates policies and analyzes external/internal access paths for supported resources. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-IAM-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS IAM capability where Session policies, Least privilege and Identity policies are first-class requirements.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: further restrict an assumed-role session and can explain access that differs from the base role. start from task/resource/condition needs, observe actual use, remove unused access and review exceptions. attached policies grant or deny actions to a principal within the rest of the policy intersection. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-IAM-SN-07

- [ ] **Question:** Design a production AWS IAM capability where Condition keys, PassRole escalation and Resource policies are first-class requirements.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bind access to organization, source network, tags, MFA, audience and other request context. permission to attach a powerful role to a service can be equivalent to using that role indirectly. supported resources can trust principals directly and express cross-account or service access. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-IAM-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS IAM capability where Access Analyzer, Principals and Explicit deny are first-class requirements.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: validates policies and analyzes external/internal access paths for supported resources. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. any applicable explicit deny overrides allows and is the first guardrail to search during diagnosis. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-IAM-SN-09

- [ ] **Question:** Design a production AWS IAM capability where Least privilege, Identity policies and Permissions boundaries are first-class requirements.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: start from task/resource/condition needs, observe actual use, remove unused access and review exceptions. attached policies grant or deny actions to a principal within the rest of the policy intersection. cap identity-policy permissions without granting actions themselves. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-IAM-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS IAM capability where PassRole escalation, Resource policies and Session policies are first-class requirements.
> **Covered in:** [AWS IAM — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: permission to attach a powerful role to a service can be equivalent to using that role indirectly. supported resources can trust principals directly and express cross-account or service access. further restrict an assumed-role session and can explain access that differs from the base role. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-IAM-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Principals. How do you lead it end to end?
> **Covered in:** [AWS IAM — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts get-caller-identity` as one read-only checkpoint, not the whole diagnosis. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-IAM-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Identity policies. How do you lead it end to end?
> **Covered in:** [AWS IAM — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION` as one read-only checkpoint, not the whole diagnosis. attached policies grant or deny actions to a principal within the rest of the policy intersection. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-IAM-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource policies. How do you lead it end to end?
> **Covered in:** [AWS IAM — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws accessanalyzer validate-policy --policy-document file://policy.json --policy-type IDENTITY_POLICY` as one read-only checkpoint, not the whole diagnosis. supported resources can trust principals directly and express cross-account or service access. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-IAM-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Explicit deny. How do you lead it end to end?
> **Covered in:** [AWS IAM — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws iam get-account-authorization-details` as one read-only checkpoint, not the whole diagnosis. any applicable explicit deny overrides allows and is the first guardrail to search during diagnosis. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-IAM-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Permissions boundaries. How do you lead it end to end?
> **Covered in:** [AWS IAM — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts get-caller-identity` as one read-only checkpoint, not the whole diagnosis. cap identity-policy permissions without granting actions themselves. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-IAM-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Session policies. How do you lead it end to end?
> **Covered in:** [AWS IAM — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION` as one read-only checkpoint, not the whole diagnosis. further restrict an assumed-role session and can explain access that differs from the base role. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-IAM-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Condition keys. How do you lead it end to end?
> **Covered in:** [AWS IAM — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws accessanalyzer validate-policy --policy-document file://policy.json --policy-type IDENTITY_POLICY` as one read-only checkpoint, not the whole diagnosis. bind access to organization, source network, tags, MFA, audience and other request context. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-IAM-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Access Analyzer. How do you lead it end to end?
> **Covered in:** [AWS IAM — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws iam get-account-authorization-details` as one read-only checkpoint, not the whole diagnosis. validates policies and analyzes external/internal access paths for supported resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-IAM-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Least privilege. How do you lead it end to end?
> **Covered in:** [AWS IAM — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts get-caller-identity` as one read-only checkpoint, not the whole diagnosis. start from task/resource/condition needs, observe actual use, remove unused access and review exceptions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-IAM-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving PassRole escalation. How do you lead it end to end?
> **Covered in:** [AWS IAM — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION` as one read-only checkpoint, not the whole diagnosis. permission to attach a powerful role to a service can be equivalent to using that role indirectly. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Foundations](../README.md) · [Study note](README.md) · [Next: AWS Organizations →](../02-organizations/README.md)

<!-- reading-navigation:end -->
