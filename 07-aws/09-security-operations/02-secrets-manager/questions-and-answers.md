# AWS Secrets Manager and Parameter Store — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JN-01

- [ ] **Question:** What is Secret version/stage, and why does it matter in AWS Secrets Manager and Parameter Store?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JN-02

- [ ] **Question:** What is Rotation Lambda, and why does it matter in AWS Secrets Manager and Parameter Store?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** creates/sets/tests/finishes a new credential under idempotent staged workflow. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JN-03

- [ ] **Question:** What is Resource policy, and why does it matter in AWS Secrets Manager and Parameter Store?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** supports cross-account/service access and must prevent public/external exposure. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JN-04

- [ ] **Question:** What is KMS key, and why does it matter in AWS Secrets Manager and Parameter Store?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** decrypt permission/key policy participates in secret access. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JN-05

- [ ] **Question:** What is Client cache, and why does it matter in AWS Secrets Manager and Parameter Store?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** reduces latency/cost but must respect rotation/revocation and process isolation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JN-06

- [ ] **Question:** What is Parameter hierarchy, and why does it matter in AWS Secrets Manager and Parameter Store?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** names organize configuration but IAM wildcard scope can overgrant. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JN-07

- [ ] **Question:** What is SecureString, and why does it matter in AWS Secrets Manager and Parameter Store?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** encrypts Parameter Store values with KMS while metadata/history still need control. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JN-08

- [ ] **Code:** **Question:** What does `aws ssm get-parameter --name NAME --with-decryption` help you verify for AWS Secrets Manager and Parameter Store?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: prefer service IAM/database auth over a stored static password where supported.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JN-09

- [ ] **Code:** **Question:** What does `aws secretsmanager describe-secret --secret-id SECRET` help you verify for AWS Secrets Manager and Parameter Store?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: revoke/rotate first, then remove logs/source/history and investigate access.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JN-10

- [ ] **Code:** **Question:** What does `aws secretsmanager list-secret-version-ids --secret-id SECRET` help you verify for AWS Secrets Manager and Parameter Store?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: CloudTrail secret API access must be monitored without logging secret values.

## Junior — procedural and command questions

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JP-01

- [ ] **Code:** **Question:** A basic Secret version/stage check fails. What would you do first using the CLI?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws secretsmanager describe-secret --secret-id SECRET` and capture exact status/reason/request ID. labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JP-02

- [ ] **Question:** A basic Rotation Lambda check fails. What would you do first?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws secretsmanager list-secret-version-ids --secret-id SECRET` and capture exact status/reason/request ID. creates/sets/tests/finishes a new credential under idempotent staged workflow. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JP-03

- [ ] **Question:** A basic Resource policy check fails. What would you do first?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws secretsmanager rotate-secret --secret-id SECRET` and capture exact status/reason/request ID. supports cross-account/service access and must prevent public/external exposure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JP-04

- [ ] **Code:** **Question:** A basic KMS key check fails. What would you do first using the CLI?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm get-parameter --name NAME --with-decryption` and capture exact status/reason/request ID. decrypt permission/key policy participates in secret access. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JP-05

- [ ] **Question:** A basic Client cache check fails. What would you do first?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws secretsmanager describe-secret --secret-id SECRET` and capture exact status/reason/request ID. reduces latency/cost but must respect rotation/revocation and process isolation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JP-06

- [ ] **Question:** A basic Parameter hierarchy check fails. What would you do first?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws secretsmanager list-secret-version-ids --secret-id SECRET` and capture exact status/reason/request ID. names organize configuration but IAM wildcard scope can overgrant. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JP-07

- [ ] **Code:** **Question:** A basic SecureString check fails. What would you do first using the CLI?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws secretsmanager rotate-secret --secret-id SECRET` and capture exact status/reason/request ID. encrypts Parameter Store values with KMS while metadata/history still need control. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JP-08

- [ ] **Question:** A basic Dynamic identity check fails. What would you do first?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm get-parameter --name NAME --with-decryption` and capture exact status/reason/request ID. prefer service IAM/database auth over a stored static password where supported. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JP-09

- [ ] **Question:** A basic Leak response check fails. What would you do first?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws secretsmanager describe-secret --secret-id SECRET` and capture exact status/reason/request ID. revoke/rotate first, then remove logs/source/history and investigate access. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-JP-10

- [ ] **Code:** **Question:** A basic Audit check fails. What would you do first using the CLI?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws secretsmanager list-secret-version-ids --secret-id SECRET` and capture exact status/reason/request ID. CloudTrail secret API access must be monitored without logging secret values. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MN-01

- [ ] **Question:** Compare Secret version/stage with Rotation Lambda. When would each change your design?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Secret version/stage: labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Rotation Lambda: creates/sets/tests/finishes a new credential under idempotent staged workflow. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MN-02

- [ ] **Question:** Compare Rotation Lambda with Resource policy. When would each change your design?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Rotation Lambda: creates/sets/tests/finishes a new credential under idempotent staged workflow. Resource policy: supports cross-account/service access and must prevent public/external exposure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MN-03

- [ ] **Question:** Compare Resource policy with KMS key. When would each change your design?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Resource policy: supports cross-account/service access and must prevent public/external exposure. KMS key: decrypt permission/key policy participates in secret access. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MN-04

- [ ] **Configuration review:** **Question:** Compare KMS key with Client cache. When would each change your design?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** KMS key: decrypt permission/key policy participates in secret access. Client cache: reduces latency/cost but must respect rotation/revocation and process isolation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MN-05

- [ ] **Question:** Compare Client cache with Parameter hierarchy. When would each change your design?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Client cache: reduces latency/cost but must respect rotation/revocation and process isolation. Parameter hierarchy: names organize configuration but IAM wildcard scope can overgrant. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MN-06

- [ ] **Question:** Compare Parameter hierarchy with SecureString. When would each change your design?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Parameter hierarchy: names organize configuration but IAM wildcard scope can overgrant. SecureString: encrypts Parameter Store values with KMS while metadata/history still need control. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MN-07

- [ ] **Configuration review:** **Question:** Compare SecureString with Dynamic identity. When would each change your design?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** SecureString: encrypts Parameter Store values with KMS while metadata/history still need control. Dynamic identity: prefer service IAM/database auth over a stored static password where supported. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MN-08

- [ ] **Question:** Compare Dynamic identity with Leak response. When would each change your design?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Dynamic identity: prefer service IAM/database auth over a stored static password where supported. Leak response: revoke/rotate first, then remove logs/source/history and investigate access. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MN-09

- [ ] **Question:** Compare Leak response with Audit. When would each change your design?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Leak response: revoke/rotate first, then remove logs/source/history and investigate access. Audit: CloudTrail secret API access must be monitored without logging secret values. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MN-10

- [ ] **Configuration review:** **Question:** Compare Audit with Secret version/stage. When would each change your design?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Audit: CloudTrail secret API access must be monitored without logging secret values. Secret version/stage: labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Secret version/stage; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws secretsmanager describe-secret --secret-id SECRET` plus recent events/changes, then correlate the service-specific SLI. labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MP-02

- [ ] **Question:** Production is degraded around Rotation Lambda; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws secretsmanager list-secret-version-ids --secret-id SECRET` plus recent events/changes, then correlate the service-specific SLI. creates/sets/tests/finishes a new credential under idempotent staged workflow. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Resource policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws secretsmanager rotate-secret --secret-id SECRET` plus recent events/changes, then correlate the service-specific SLI. supports cross-account/service access and must prevent public/external exposure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MP-04

- [ ] **Question:** Production is degraded around KMS key; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm get-parameter --name NAME --with-decryption` plus recent events/changes, then correlate the service-specific SLI. decrypt permission/key policy participates in secret access. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Client cache; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws secretsmanager describe-secret --secret-id SECRET` plus recent events/changes, then correlate the service-specific SLI. reduces latency/cost but must respect rotation/revocation and process isolation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MP-06

- [ ] **Question:** Production is degraded around Parameter hierarchy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws secretsmanager list-secret-version-ids --secret-id SECRET` plus recent events/changes, then correlate the service-specific SLI. names organize configuration but IAM wildcard scope can overgrant. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around SecureString; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws secretsmanager rotate-secret --secret-id SECRET` plus recent events/changes, then correlate the service-specific SLI. encrypts Parameter Store values with KMS while metadata/history still need control. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MP-08

- [ ] **Question:** Production is degraded around Dynamic identity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm get-parameter --name NAME --with-decryption` plus recent events/changes, then correlate the service-specific SLI. prefer service IAM/database auth over a stored static password where supported. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Leak response; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws secretsmanager describe-secret --secret-id SECRET` plus recent events/changes, then correlate the service-specific SLI. revoke/rotate first, then remove logs/source/history and investigate access. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-MP-10

- [ ] **Question:** Production is degraded around Audit; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws secretsmanager list-secret-version-ids --secret-id SECRET` plus recent events/changes, then correlate the service-specific SLI. CloudTrail secret API access must be monitored without logging secret values. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SN-01

- [ ] **Question:** Design a production AWS Secrets Manager and Parameter Store capability where Secret version/stage, KMS key and SecureString are first-class requirements.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. decrypt permission/key policy participates in secret access. encrypts Parameter Store values with KMS while metadata/history still need control. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Secrets Manager and Parameter Store capability where Rotation Lambda, Client cache and Dynamic identity are first-class requirements.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: creates/sets/tests/finishes a new credential under idempotent staged workflow. reduces latency/cost but must respect rotation/revocation and process isolation. prefer service IAM/database auth over a stored static password where supported. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SN-03

- [ ] **Question:** Design a production AWS Secrets Manager and Parameter Store capability where Resource policy, Parameter hierarchy and Leak response are first-class requirements.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supports cross-account/service access and must prevent public/external exposure. names organize configuration but IAM wildcard scope can overgrant. revoke/rotate first, then remove logs/source/history and investigate access. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Secrets Manager and Parameter Store capability where KMS key, SecureString and Audit are first-class requirements.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: decrypt permission/key policy participates in secret access. encrypts Parameter Store values with KMS while metadata/history still need control. CloudTrail secret API access must be monitored without logging secret values. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SN-05

- [ ] **Question:** Design a production AWS Secrets Manager and Parameter Store capability where Client cache, Dynamic identity and Secret version/stage are first-class requirements.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reduces latency/cost but must respect rotation/revocation and process isolation. prefer service IAM/database auth over a stored static password where supported. labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Secrets Manager and Parameter Store capability where Parameter hierarchy, Leak response and Rotation Lambda are first-class requirements.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: names organize configuration but IAM wildcard scope can overgrant. revoke/rotate first, then remove logs/source/history and investigate access. creates/sets/tests/finishes a new credential under idempotent staged workflow. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SN-07

- [ ] **Question:** Design a production AWS Secrets Manager and Parameter Store capability where SecureString, Audit and Resource policy are first-class requirements.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: encrypts Parameter Store values with KMS while metadata/history still need control. CloudTrail secret API access must be monitored without logging secret values. supports cross-account/service access and must prevent public/external exposure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Secrets Manager and Parameter Store capability where Dynamic identity, Secret version/stage and KMS key are first-class requirements.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prefer service IAM/database auth over a stored static password where supported. labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. decrypt permission/key policy participates in secret access. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SN-09

- [ ] **Question:** Design a production AWS Secrets Manager and Parameter Store capability where Leak response, Rotation Lambda and Client cache are first-class requirements.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: revoke/rotate first, then remove logs/source/history and investigate access. creates/sets/tests/finishes a new credential under idempotent staged workflow. reduces latency/cost but must respect rotation/revocation and process isolation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Secrets Manager and Parameter Store capability where Audit, Resource policy and Parameter hierarchy are first-class requirements.
> **Covered in:** [AWS Secrets Manager and Parameter Store — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: CloudTrail secret API access must be monitored without logging secret values. supports cross-account/service access and must prevent public/external exposure. names organize configuration but IAM wildcard scope can overgrant. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secret version/stage. How do you lead it end to end?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws secretsmanager describe-secret --secret-id SECRET` as one read-only checkpoint, not the whole diagnosis. labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rotation Lambda. How do you lead it end to end?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws secretsmanager list-secret-version-ids --secret-id SECRET` as one read-only checkpoint, not the whole diagnosis. creates/sets/tests/finishes a new credential under idempotent staged workflow. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource policy. How do you lead it end to end?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws secretsmanager rotate-secret --secret-id SECRET` as one read-only checkpoint, not the whole diagnosis. supports cross-account/service access and must prevent public/external exposure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving KMS key. How do you lead it end to end?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm get-parameter --name NAME --with-decryption` as one read-only checkpoint, not the whole diagnosis. decrypt permission/key policy participates in secret access. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Client cache. How do you lead it end to end?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws secretsmanager describe-secret --secret-id SECRET` as one read-only checkpoint, not the whole diagnosis. reduces latency/cost but must respect rotation/revocation and process isolation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Parameter hierarchy. How do you lead it end to end?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws secretsmanager list-secret-version-ids --secret-id SECRET` as one read-only checkpoint, not the whole diagnosis. names organize configuration but IAM wildcard scope can overgrant. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SecureString. How do you lead it end to end?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws secretsmanager rotate-secret --secret-id SECRET` as one read-only checkpoint, not the whole diagnosis. encrypts Parameter Store values with KMS while metadata/history still need control. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dynamic identity. How do you lead it end to end?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm get-parameter --name NAME --with-decryption` as one read-only checkpoint, not the whole diagnosis. prefer service IAM/database auth over a stored static password where supported. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Leak response. How do you lead it end to end?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws secretsmanager describe-secret --secret-id SECRET` as one read-only checkpoint, not the whole diagnosis. revoke/rotate first, then remove logs/source/history and investigate access. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-SECRETS-MANAGER-AND-PARAMETER-STORE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Audit. How do you lead it end to end?
> **Covered in:** [AWS Secrets Manager and Parameter Store — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws secretsmanager list-secret-version-ids --secret-id SECRET` as one read-only checkpoint, not the whole diagnosis. CloudTrail secret API access must be monitored without logging secret values. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AWS KMS](../01-kms/README.md) · [Study note](README.md) · [Next: ACM, AWS WAF and Shield →](../03-acm-waf-shield/README.md)

<!-- reading-navigation:end -->
