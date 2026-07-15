# AWS KMS — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-KMS-JN-01

- [ ] **Question:** What is KMS key, and why does it matter in AWS KMS?
> **Covered in:** [AWS KMS — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** logical key with policy, metadata and protected key material used by integrated services. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-KMS-JN-02

- [ ] **Question:** What is Envelope encryption, and why does it matter in AWS KMS?
> **Covered in:** [AWS KMS — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** KMS protects data keys while applications/services encrypt bulk data locally. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-KMS-JN-03

- [ ] **Question:** What is Key policy, and why does it matter in AWS KMS?
> **Covered in:** [AWS KMS — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** primary resource policy can enable IAM delegation or directly authorize principals. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-KMS-JN-04

- [ ] **Question:** What is Grant, and why does it matter in AWS KMS?
> **Covered in:** [AWS KMS — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** constrained delegated permission often used by AWS services and lifecycle operations. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-KMS-JN-05

- [ ] **Question:** What is Encryption context, and why does it matter in AWS KMS?
> **Covered in:** [AWS KMS — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** authenticated additional data can bind ciphertext use to resource/purpose. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-KMS-JN-06

- [ ] **Question:** What is Rotation, and why does it matter in AWS KMS?
> **Covered in:** [AWS KMS — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** creates new backing material for future encrypt while old material remains for decrypt. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-KMS-JN-07

- [ ] **Question:** What is Multi-Region key, and why does it matter in AWS KMS?
> **Covered in:** [AWS KMS — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** related key material supports regional use but replication/data policy remains separate. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-KMS-JN-08

- [ ] **Code:** **Question:** What does `aws kms get-key-rotation-status --key-id KEY` help you verify for AWS KMS?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: increases control with availability/expiry/operations responsibility.

### AWS-KMS-JN-09

- [ ] **Code:** **Question:** What does `aws kms describe-key --key-id KEY` help you verify for AWS KMS?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: high-volume SSE-KMS or application calls can throttle a data path.

### AWS-KMS-JN-10

- [ ] **Code:** **Question:** What does `aws kms get-key-policy --key-id KEY --policy-name default` help you verify for AWS KMS?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: waiting period is a last warning; loss of a key can permanently lose every dependent ciphertext.

## Junior — procedural and command questions

### AWS-KMS-JP-01

- [ ] **Code:** **Question:** A basic KMS key check fails. What would you do first using the CLI?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms describe-key --key-id KEY` and capture exact status/reason/request ID. logical key with policy, metadata and protected key material used by integrated services. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-KMS-JP-02

- [ ] **Question:** A basic Envelope encryption check fails. What would you do first?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms get-key-policy --key-id KEY --policy-name default` and capture exact status/reason/request ID. KMS protects data keys while applications/services encrypt bulk data locally. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-KMS-JP-03

- [ ] **Question:** A basic Key policy check fails. What would you do first?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms list-grants --key-id KEY` and capture exact status/reason/request ID. primary resource policy can enable IAM delegation or directly authorize principals. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-KMS-JP-04

- [ ] **Code:** **Question:** A basic Grant check fails. What would you do first using the CLI?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms get-key-rotation-status --key-id KEY` and capture exact status/reason/request ID. constrained delegated permission often used by AWS services and lifecycle operations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-KMS-JP-05

- [ ] **Question:** A basic Encryption context check fails. What would you do first?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms describe-key --key-id KEY` and capture exact status/reason/request ID. authenticated additional data can bind ciphertext use to resource/purpose. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-KMS-JP-06

- [ ] **Question:** A basic Rotation check fails. What would you do first?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms get-key-policy --key-id KEY --policy-name default` and capture exact status/reason/request ID. creates new backing material for future encrypt while old material remains for decrypt. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-KMS-JP-07

- [ ] **Code:** **Question:** A basic Multi-Region key check fails. What would you do first using the CLI?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms list-grants --key-id KEY` and capture exact status/reason/request ID. related key material supports regional use but replication/data policy remains separate. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-KMS-JP-08

- [ ] **Question:** A basic Imported/custom key store check fails. What would you do first?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms get-key-rotation-status --key-id KEY` and capture exact status/reason/request ID. increases control with availability/expiry/operations responsibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-KMS-JP-09

- [ ] **Question:** A basic Request quota check fails. What would you do first?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms describe-key --key-id KEY` and capture exact status/reason/request ID. high-volume SSE-KMS or application calls can throttle a data path. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-KMS-JP-10

- [ ] **Code:** **Question:** A basic Deletion check fails. What would you do first using the CLI?
> **Covered in:** [AWS KMS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms get-key-policy --key-id KEY --policy-name default` and capture exact status/reason/request ID. waiting period is a last warning; loss of a key can permanently lose every dependent ciphertext. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-KMS-MN-01

- [ ] **Question:** Compare KMS key with Envelope encryption. When would each change your design?
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** KMS key: logical key with policy, metadata and protected key material used by integrated services. Envelope encryption: KMS protects data keys while applications/services encrypt bulk data locally. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-KMS-MN-02

- [ ] **Question:** Compare Envelope encryption with Key policy. When would each change your design?
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Envelope encryption: KMS protects data keys while applications/services encrypt bulk data locally. Key policy: primary resource policy can enable IAM delegation or directly authorize principals. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-KMS-MN-03

- [ ] **Question:** Compare Key policy with Grant. When would each change your design?
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Key policy: primary resource policy can enable IAM delegation or directly authorize principals. Grant: constrained delegated permission often used by AWS services and lifecycle operations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-KMS-MN-04

- [ ] **Configuration review:** **Question:** Compare Grant with Encryption context. When would each change your design?
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Grant: constrained delegated permission often used by AWS services and lifecycle operations. Encryption context: authenticated additional data can bind ciphertext use to resource/purpose. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-KMS-MN-05

- [ ] **Question:** Compare Encryption context with Rotation. When would each change your design?
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Encryption context: authenticated additional data can bind ciphertext use to resource/purpose. Rotation: creates new backing material for future encrypt while old material remains for decrypt. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-KMS-MN-06

- [ ] **Question:** Compare Rotation with Multi-Region key. When would each change your design?
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Rotation: creates new backing material for future encrypt while old material remains for decrypt. Multi-Region key: related key material supports regional use but replication/data policy remains separate. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-KMS-MN-07

- [ ] **Configuration review:** **Question:** Compare Multi-Region key with Imported/custom key store. When would each change your design?
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Multi-Region key: related key material supports regional use but replication/data policy remains separate. Imported/custom key store: increases control with availability/expiry/operations responsibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-KMS-MN-08

- [ ] **Question:** Compare Imported/custom key store with Request quota. When would each change your design?
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Imported/custom key store: increases control with availability/expiry/operations responsibility. Request quota: high-volume SSE-KMS or application calls can throttle a data path. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-KMS-MN-09

- [ ] **Question:** Compare Request quota with Deletion. When would each change your design?
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Request quota: high-volume SSE-KMS or application calls can throttle a data path. Deletion: waiting period is a last warning; loss of a key can permanently lose every dependent ciphertext. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-KMS-MN-10

- [ ] **Configuration review:** **Question:** Compare Deletion with KMS key. When would each change your design?
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Deletion: waiting period is a last warning; loss of a key can permanently lose every dependent ciphertext. KMS key: logical key with policy, metadata and protected key material used by integrated services. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-KMS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around KMS key; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms describe-key --key-id KEY` plus recent events/changes, then correlate the service-specific SLI. logical key with policy, metadata and protected key material used by integrated services. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-KMS-MP-02

- [ ] **Question:** Production is degraded around Envelope encryption; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms get-key-policy --key-id KEY --policy-name default` plus recent events/changes, then correlate the service-specific SLI. KMS protects data keys while applications/services encrypt bulk data locally. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-KMS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Key policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms list-grants --key-id KEY` plus recent events/changes, then correlate the service-specific SLI. primary resource policy can enable IAM delegation or directly authorize principals. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-KMS-MP-04

- [ ] **Question:** Production is degraded around Grant; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms get-key-rotation-status --key-id KEY` plus recent events/changes, then correlate the service-specific SLI. constrained delegated permission often used by AWS services and lifecycle operations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-KMS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Encryption context; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms describe-key --key-id KEY` plus recent events/changes, then correlate the service-specific SLI. authenticated additional data can bind ciphertext use to resource/purpose. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-KMS-MP-06

- [ ] **Question:** Production is degraded around Rotation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms get-key-policy --key-id KEY --policy-name default` plus recent events/changes, then correlate the service-specific SLI. creates new backing material for future encrypt while old material remains for decrypt. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-KMS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Multi-Region key; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms list-grants --key-id KEY` plus recent events/changes, then correlate the service-specific SLI. related key material supports regional use but replication/data policy remains separate. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-KMS-MP-08

- [ ] **Question:** Production is degraded around Imported/custom key store; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms get-key-rotation-status --key-id KEY` plus recent events/changes, then correlate the service-specific SLI. increases control with availability/expiry/operations responsibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-KMS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Request quota; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms describe-key --key-id KEY` plus recent events/changes, then correlate the service-specific SLI. high-volume SSE-KMS or application calls can throttle a data path. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-KMS-MP-10

- [ ] **Question:** Production is degraded around Deletion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms get-key-policy --key-id KEY --policy-name default` plus recent events/changes, then correlate the service-specific SLI. waiting period is a last warning; loss of a key can permanently lose every dependent ciphertext. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-KMS-SN-01

- [ ] **Question:** Design a production AWS KMS capability where KMS key, Grant and Multi-Region key are first-class requirements.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: logical key with policy, metadata and protected key material used by integrated services. constrained delegated permission often used by AWS services and lifecycle operations. related key material supports regional use but replication/data policy remains separate. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-KMS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS KMS capability where Envelope encryption, Encryption context and Imported/custom key store are first-class requirements.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: KMS protects data keys while applications/services encrypt bulk data locally. authenticated additional data can bind ciphertext use to resource/purpose. increases control with availability/expiry/operations responsibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-KMS-SN-03

- [ ] **Question:** Design a production AWS KMS capability where Key policy, Rotation and Request quota are first-class requirements.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: primary resource policy can enable IAM delegation or directly authorize principals. creates new backing material for future encrypt while old material remains for decrypt. high-volume SSE-KMS or application calls can throttle a data path. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-KMS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS KMS capability where Grant, Multi-Region key and Deletion are first-class requirements.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: constrained delegated permission often used by AWS services and lifecycle operations. related key material supports regional use but replication/data policy remains separate. waiting period is a last warning; loss of a key can permanently lose every dependent ciphertext. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-KMS-SN-05

- [ ] **Question:** Design a production AWS KMS capability where Encryption context, Imported/custom key store and KMS key are first-class requirements.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: authenticated additional data can bind ciphertext use to resource/purpose. increases control with availability/expiry/operations responsibility. logical key with policy, metadata and protected key material used by integrated services. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-KMS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS KMS capability where Rotation, Request quota and Envelope encryption are first-class requirements.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: creates new backing material for future encrypt while old material remains for decrypt. high-volume SSE-KMS or application calls can throttle a data path. KMS protects data keys while applications/services encrypt bulk data locally. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-KMS-SN-07

- [ ] **Question:** Design a production AWS KMS capability where Multi-Region key, Deletion and Key policy are first-class requirements.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: related key material supports regional use but replication/data policy remains separate. waiting period is a last warning; loss of a key can permanently lose every dependent ciphertext. primary resource policy can enable IAM delegation or directly authorize principals. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-KMS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS KMS capability where Imported/custom key store, KMS key and Grant are first-class requirements.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: increases control with availability/expiry/operations responsibility. logical key with policy, metadata and protected key material used by integrated services. constrained delegated permission often used by AWS services and lifecycle operations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-KMS-SN-09

- [ ] **Question:** Design a production AWS KMS capability where Request quota, Envelope encryption and Encryption context are first-class requirements.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: high-volume SSE-KMS or application calls can throttle a data path. KMS protects data keys while applications/services encrypt bulk data locally. authenticated additional data can bind ciphertext use to resource/purpose. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-KMS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS KMS capability where Deletion, Key policy and Rotation are first-class requirements.
> **Covered in:** [AWS KMS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: waiting period is a last warning; loss of a key can permanently lose every dependent ciphertext. primary resource policy can enable IAM delegation or directly authorize principals. creates new backing material for future encrypt while old material remains for decrypt. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-KMS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving KMS key. How do you lead it end to end?
> **Covered in:** [AWS KMS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms describe-key --key-id KEY` as one read-only checkpoint, not the whole diagnosis. logical key with policy, metadata and protected key material used by integrated services. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-KMS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Envelope encryption. How do you lead it end to end?
> **Covered in:** [AWS KMS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms get-key-policy --key-id KEY --policy-name default` as one read-only checkpoint, not the whole diagnosis. KMS protects data keys while applications/services encrypt bulk data locally. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-KMS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Key policy. How do you lead it end to end?
> **Covered in:** [AWS KMS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms list-grants --key-id KEY` as one read-only checkpoint, not the whole diagnosis. primary resource policy can enable IAM delegation or directly authorize principals. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-KMS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Grant. How do you lead it end to end?
> **Covered in:** [AWS KMS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms get-key-rotation-status --key-id KEY` as one read-only checkpoint, not the whole diagnosis. constrained delegated permission often used by AWS services and lifecycle operations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-KMS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Encryption context. How do you lead it end to end?
> **Covered in:** [AWS KMS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms describe-key --key-id KEY` as one read-only checkpoint, not the whole diagnosis. authenticated additional data can bind ciphertext use to resource/purpose. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-KMS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rotation. How do you lead it end to end?
> **Covered in:** [AWS KMS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms get-key-policy --key-id KEY --policy-name default` as one read-only checkpoint, not the whole diagnosis. creates new backing material for future encrypt while old material remains for decrypt. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-KMS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Multi-Region key. How do you lead it end to end?
> **Covered in:** [AWS KMS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms list-grants --key-id KEY` as one read-only checkpoint, not the whole diagnosis. related key material supports regional use but replication/data policy remains separate. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-KMS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Imported/custom key store. How do you lead it end to end?
> **Covered in:** [AWS KMS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms get-key-rotation-status --key-id KEY` as one read-only checkpoint, not the whole diagnosis. increases control with availability/expiry/operations responsibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-KMS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Request quota. How do you lead it end to end?
> **Covered in:** [AWS KMS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms describe-key --key-id KEY` as one read-only checkpoint, not the whole diagnosis. high-volume SSE-KMS or application calls can throttle a data path. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-KMS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deletion. How do you lead it end to end?
> **Covered in:** [AWS KMS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms get-key-policy --key-id KEY --policy-name default` as one read-only checkpoint, not the whole diagnosis. waiting period is a last warning; loss of a key can permanently lose every dependent ciphertext. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Security Operations](../README.md) · [Study note](README.md) · [Next: AWS Secrets Manager and Parameter Store →](../02-secrets-manager/README.md)

<!-- reading-navigation:end -->
