# AWS STS, federation and IAM Identity Center — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JN-01

- [ ] **Question:** What is AssumeRole, and why does it matter in AWS STS, federation and IAM Identity Center?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** exchanges an authenticated caller for temporary role credentials subject to trust and permissions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JN-02

- [ ] **Question:** What is Trust policy, and why does it matter in AWS STS, federation and IAM Identity Center?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** controls which principal and conditions may assume a role. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JN-03

- [ ] **Question:** What is Role permissions, and why does it matter in AWS STS, federation and IAM Identity Center?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** control what the resulting session can do after assumption. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JN-04

- [ ] **Question:** What is External ID, and why does it matter in AWS STS, federation and IAM Identity Center?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** mitigates confused-deputy risk for third-party cross-account role assumption. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JN-05

- [ ] **Question:** What is OIDC web identity, and why does it matter in AWS STS, federation and IAM Identity Center?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** exchanges a signed workload token with issuer, audience and subject conditions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JN-06

- [ ] **Question:** What is SAML federation, and why does it matter in AWS STS, federation and IAM Identity Center?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** maps enterprise identity assertions into AWS role sessions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JN-07

- [ ] **Question:** What is Identity Center, and why does it matter in AWS STS, federation and IAM Identity Center?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** centralizes workforce assignments and permission sets across accounts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JN-08

- [ ] **Code:** **Question:** What does `aws configure export-credentials --profile PROFILE` help you verify for AWS STS, federation and IAM Identity Center?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: assumes another role from a role session and has duration/attribution constraints.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JN-09

- [ ] **Code:** **Question:** What does `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` help you verify for AWS STS, federation and IAM Identity Center?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: propagate authorized attribution/context into policy and audit.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JN-10

- [ ] **Code:** **Question:** What does `aws sts decode-authorization-message --encoded-message MESSAGE` help you verify for AWS STS, federation and IAM Identity Center?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: applications must refresh before expiry and avoid persisting temporary credentials.

## Junior — procedural and command questions

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JP-01

- [ ] **Code:** **Question:** A basic AssumeRole check fails. What would you do first using the CLI?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` and capture exact status/reason/request ID. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JP-02

- [ ] **Question:** A basic Trust policy check fails. What would you do first?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts decode-authorization-message --encoded-message MESSAGE` and capture exact status/reason/request ID. controls which principal and conditions may assume a role. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JP-03

- [ ] **Question:** A basic Role permissions check fails. What would you do first?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sso login --profile PROFILE` and capture exact status/reason/request ID. control what the resulting session can do after assumption. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JP-04

- [ ] **Code:** **Question:** A basic External ID check fails. What would you do first using the CLI?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws configure export-credentials --profile PROFILE` and capture exact status/reason/request ID. mitigates confused-deputy risk for third-party cross-account role assumption. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JP-05

- [ ] **Question:** A basic OIDC web identity check fails. What would you do first?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` and capture exact status/reason/request ID. exchanges a signed workload token with issuer, audience and subject conditions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JP-06

- [ ] **Question:** A basic SAML federation check fails. What would you do first?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts decode-authorization-message --encoded-message MESSAGE` and capture exact status/reason/request ID. maps enterprise identity assertions into AWS role sessions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JP-07

- [ ] **Code:** **Question:** A basic Identity Center check fails. What would you do first using the CLI?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sso login --profile PROFILE` and capture exact status/reason/request ID. centralizes workforce assignments and permission sets across accounts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JP-08

- [ ] **Question:** A basic Role chaining check fails. What would you do first?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws configure export-credentials --profile PROFILE` and capture exact status/reason/request ID. assumes another role from a role session and has duration/attribution constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JP-09

- [ ] **Question:** A basic Session tags/source identity check fails. What would you do first?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` and capture exact status/reason/request ID. propagate authorized attribution/context into policy and audit. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-JP-10

- [ ] **Code:** **Question:** A basic Credential refresh check fails. What would you do first using the CLI?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts decode-authorization-message --encoded-message MESSAGE` and capture exact status/reason/request ID. applications must refresh before expiry and avoid persisting temporary credentials. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MN-01

- [ ] **Question:** Compare AssumeRole with Trust policy. When would each change your design?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** AssumeRole: exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Trust policy: controls which principal and conditions may assume a role. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MN-02

- [ ] **Question:** Compare Trust policy with Role permissions. When would each change your design?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Trust policy: controls which principal and conditions may assume a role. Role permissions: control what the resulting session can do after assumption. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MN-03

- [ ] **Question:** Compare Role permissions with External ID. When would each change your design?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Role permissions: control what the resulting session can do after assumption. External ID: mitigates confused-deputy risk for third-party cross-account role assumption. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MN-04

- [ ] **Configuration review:** **Question:** Compare External ID with OIDC web identity. When would each change your design?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** External ID: mitigates confused-deputy risk for third-party cross-account role assumption. OIDC web identity: exchanges a signed workload token with issuer, audience and subject conditions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MN-05

- [ ] **Question:** Compare OIDC web identity with SAML federation. When would each change your design?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** OIDC web identity: exchanges a signed workload token with issuer, audience and subject conditions. SAML federation: maps enterprise identity assertions into AWS role sessions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MN-06

- [ ] **Question:** Compare SAML federation with Identity Center. When would each change your design?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** SAML federation: maps enterprise identity assertions into AWS role sessions. Identity Center: centralizes workforce assignments and permission sets across accounts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MN-07

- [ ] **Configuration review:** **Question:** Compare Identity Center with Role chaining. When would each change your design?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Identity Center: centralizes workforce assignments and permission sets across accounts. Role chaining: assumes another role from a role session and has duration/attribution constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MN-08

- [ ] **Question:** Compare Role chaining with Session tags/source identity. When would each change your design?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Role chaining: assumes another role from a role session and has duration/attribution constraints. Session tags/source identity: propagate authorized attribution/context into policy and audit. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MN-09

- [ ] **Question:** Compare Session tags/source identity with Credential refresh. When would each change your design?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Session tags/source identity: propagate authorized attribution/context into policy and audit. Credential refresh: applications must refresh before expiry and avoid persisting temporary credentials. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MN-10

- [ ] **Configuration review:** **Question:** Compare Credential refresh with AssumeRole. When would each change your design?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Credential refresh: applications must refresh before expiry and avoid persisting temporary credentials. AssumeRole: exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around AssumeRole; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` plus recent events/changes, then correlate the service-specific SLI. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MP-02

- [ ] **Question:** Production is degraded around Trust policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts decode-authorization-message --encoded-message MESSAGE` plus recent events/changes, then correlate the service-specific SLI. controls which principal and conditions may assume a role. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Role permissions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sso login --profile PROFILE` plus recent events/changes, then correlate the service-specific SLI. control what the resulting session can do after assumption. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MP-04

- [ ] **Question:** Production is degraded around External ID; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws configure export-credentials --profile PROFILE` plus recent events/changes, then correlate the service-specific SLI. mitigates confused-deputy risk for third-party cross-account role assumption. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around OIDC web identity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` plus recent events/changes, then correlate the service-specific SLI. exchanges a signed workload token with issuer, audience and subject conditions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MP-06

- [ ] **Question:** Production is degraded around SAML federation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts decode-authorization-message --encoded-message MESSAGE` plus recent events/changes, then correlate the service-specific SLI. maps enterprise identity assertions into AWS role sessions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Identity Center; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sso login --profile PROFILE` plus recent events/changes, then correlate the service-specific SLI. centralizes workforce assignments and permission sets across accounts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MP-08

- [ ] **Question:** Production is degraded around Role chaining; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws configure export-credentials --profile PROFILE` plus recent events/changes, then correlate the service-specific SLI. assumes another role from a role session and has duration/attribution constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Session tags/source identity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` plus recent events/changes, then correlate the service-specific SLI. propagate authorized attribution/context into policy and audit. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-MP-10

- [ ] **Question:** Production is degraded around Credential refresh; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts decode-authorization-message --encoded-message MESSAGE` plus recent events/changes, then correlate the service-specific SLI. applications must refresh before expiry and avoid persisting temporary credentials. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SN-01

- [ ] **Question:** Design a production AWS STS, federation and IAM Identity Center capability where AssumeRole, External ID and Identity Center are first-class requirements.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exchanges an authenticated caller for temporary role credentials subject to trust and permissions. mitigates confused-deputy risk for third-party cross-account role assumption. centralizes workforce assignments and permission sets across accounts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS STS, federation and IAM Identity Center capability where Trust policy, OIDC web identity and Role chaining are first-class requirements.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controls which principal and conditions may assume a role. exchanges a signed workload token with issuer, audience and subject conditions. assumes another role from a role session and has duration/attribution constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SN-03

- [ ] **Question:** Design a production AWS STS, federation and IAM Identity Center capability where Role permissions, SAML federation and Session tags/source identity are first-class requirements.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: control what the resulting session can do after assumption. maps enterprise identity assertions into AWS role sessions. propagate authorized attribution/context into policy and audit. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS STS, federation and IAM Identity Center capability where External ID, Identity Center and Credential refresh are first-class requirements.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: mitigates confused-deputy risk for third-party cross-account role assumption. centralizes workforce assignments and permission sets across accounts. applications must refresh before expiry and avoid persisting temporary credentials. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SN-05

- [ ] **Question:** Design a production AWS STS, federation and IAM Identity Center capability where OIDC web identity, Role chaining and AssumeRole are first-class requirements.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exchanges a signed workload token with issuer, audience and subject conditions. assumes another role from a role session and has duration/attribution constraints. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS STS, federation and IAM Identity Center capability where SAML federation, Session tags/source identity and Trust policy are first-class requirements.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: maps enterprise identity assertions into AWS role sessions. propagate authorized attribution/context into policy and audit. controls which principal and conditions may assume a role. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SN-07

- [ ] **Question:** Design a production AWS STS, federation and IAM Identity Center capability where Identity Center, Credential refresh and Role permissions are first-class requirements.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: centralizes workforce assignments and permission sets across accounts. applications must refresh before expiry and avoid persisting temporary credentials. control what the resulting session can do after assumption. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS STS, federation and IAM Identity Center capability where Role chaining, AssumeRole and External ID are first-class requirements.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: assumes another role from a role session and has duration/attribution constraints. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. mitigates confused-deputy risk for third-party cross-account role assumption. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SN-09

- [ ] **Question:** Design a production AWS STS, federation and IAM Identity Center capability where Session tags/source identity, Trust policy and OIDC web identity are first-class requirements.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: propagate authorized attribution/context into policy and audit. controls which principal and conditions may assume a role. exchanges a signed workload token with issuer, audience and subject conditions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS STS, federation and IAM Identity Center capability where Credential refresh, Role permissions and SAML federation are first-class requirements.
> **Covered in:** [AWS STS, federation and IAM Identity Center — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: applications must refresh before expiry and avoid persisting temporary credentials. control what the resulting session can do after assumption. maps enterprise identity assertions into AWS role sessions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AssumeRole. How do you lead it end to end?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` as one read-only checkpoint, not the whole diagnosis. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Trust policy. How do you lead it end to end?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts decode-authorization-message --encoded-message MESSAGE` as one read-only checkpoint, not the whole diagnosis. controls which principal and conditions may assume a role. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Role permissions. How do you lead it end to end?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sso login --profile PROFILE` as one read-only checkpoint, not the whole diagnosis. control what the resulting session can do after assumption. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving External ID. How do you lead it end to end?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws configure export-credentials --profile PROFILE` as one read-only checkpoint, not the whole diagnosis. mitigates confused-deputy risk for third-party cross-account role assumption. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving OIDC web identity. How do you lead it end to end?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` as one read-only checkpoint, not the whole diagnosis. exchanges a signed workload token with issuer, audience and subject conditions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SAML federation. How do you lead it end to end?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts decode-authorization-message --encoded-message MESSAGE` as one read-only checkpoint, not the whole diagnosis. maps enterprise identity assertions into AWS role sessions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Identity Center. How do you lead it end to end?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sso login --profile PROFILE` as one read-only checkpoint, not the whole diagnosis. centralizes workforce assignments and permission sets across accounts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Role chaining. How do you lead it end to end?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws configure export-credentials --profile PROFILE` as one read-only checkpoint, not the whole diagnosis. assumes another role from a role session and has duration/attribution constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Session tags/source identity. How do you lead it end to end?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` as one read-only checkpoint, not the whole diagnosis. propagate authorized attribution/context into policy and audit. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STS-FEDERATION-AND-IAM-IDENTITY-CENTER-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Credential refresh. How do you lead it end to end?
> **Covered in:** [AWS STS, federation and IAM Identity Center — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts decode-authorization-message --encoded-message MESSAGE` as one read-only checkpoint, not the whole diagnosis. applications must refresh before expiry and avoid persisting temporary credentials. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AWS Organizations](../02-organizations/README.md) · [Study note](README.md) · [Next: AWS Control Tower, tagging, quotas and governance →](../04-control-tower-governance/README.md)

<!-- reading-navigation:end -->
