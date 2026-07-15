# Amazon ECR — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-ECR-JN-01

- [ ] **Question:** What is Repository, and why does it matter in Amazon ECR?

**Answer:** regional namespace with IAM/resource policy and encryption. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECR-JN-02

- [ ] **Question:** What is Tag immutability, and why does it matter in Amazon ECR?

**Answer:** prevents overwriting release tags while deployment by digest is stronger identity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECR-JN-03

- [ ] **Question:** What is Image scanning, and why does it matter in Amazon ECR?

**Answer:** detects known vulnerabilities and requires prioritization/rebuild rather than in-place patch. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECR-JN-04

- [ ] **Question:** What is Lifecycle policy, and why does it matter in Amazon ECR?

**Answer:** expires images by ordered selection rules and can remove rollback artifacts if careless. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECR-JN-05

- [ ] **Question:** What is Cross-Region/account replication, and why does it matter in Amazon ECR?

**Answer:** copies eligible artifacts under registry policy and KMS/access constraints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECR-JN-06

- [ ] **Question:** What is Pull-through cache, and why does it matter in Amazon ECR?

**Answer:** mirrors upstream content and reduces availability/rate risk while requiring trust policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECR-JN-07

- [ ] **Question:** What is Authentication token, and why does it matter in Amazon ECR?

**Answer:** short-lived registry auth derives from AWS identity and must be refreshed. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECR-JN-08

- [ ] **Code:** **Question:** What does `aws ecr get-login-password | docker login --username AWS --password-stdin REGISTRY` help you verify for Amazon ECR?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: external OCI artifacts/attestations bind trusted build identity to digest.

### AMAZON-ECR-JN-09

- [ ] **Code:** **Question:** What does `aws ecr describe-repositories` help you verify for Amazon ECR?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: supports cross-account pulls/pushes but cannot override explicit organization denies.

### AMAZON-ECR-JN-10

- [ ] **Code:** **Question:** What does `aws ecr describe-images --repository-name REPO` help you verify for Amazon ECR?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: layers, node cache, network/NAT and registry quota influence startup time.

## Junior — procedural and command questions

### AMAZON-ECR-JP-01

- [ ] **Code:** **Question:** A basic Repository check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr describe-repositories` and capture exact status/reason/request ID. regional namespace with IAM/resource policy and encryption. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECR-JP-02

- [ ] **Question:** A basic Tag immutability check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr describe-images --repository-name REPO` and capture exact status/reason/request ID. prevents overwriting release tags while deployment by digest is stronger identity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECR-JP-03

- [ ] **Question:** A basic Image scanning check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr get-lifecycle-policy --repository-name REPO` and capture exact status/reason/request ID. detects known vulnerabilities and requires prioritization/rebuild rather than in-place patch. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECR-JP-04

- [ ] **Code:** **Question:** A basic Lifecycle policy check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr get-login-password | docker login --username AWS --password-stdin REGISTRY` and capture exact status/reason/request ID. expires images by ordered selection rules and can remove rollback artifacts if careless. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECR-JP-05

- [ ] **Question:** A basic Cross-Region/account replication check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr describe-repositories` and capture exact status/reason/request ID. copies eligible artifacts under registry policy and KMS/access constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECR-JP-06

- [ ] **Question:** A basic Pull-through cache check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr describe-images --repository-name REPO` and capture exact status/reason/request ID. mirrors upstream content and reduces availability/rate risk while requiring trust policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECR-JP-07

- [ ] **Code:** **Question:** A basic Authentication token check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr get-lifecycle-policy --repository-name REPO` and capture exact status/reason/request ID. short-lived registry auth derives from AWS identity and must be refreshed. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECR-JP-08

- [ ] **Question:** A basic Signature/provenance check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr get-login-password | docker login --username AWS --password-stdin REGISTRY` and capture exact status/reason/request ID. external OCI artifacts/attestations bind trusted build identity to digest. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECR-JP-09

- [ ] **Question:** A basic Repository policy check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr describe-repositories` and capture exact status/reason/request ID. supports cross-account pulls/pushes but cannot override explicit organization denies. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECR-JP-10

- [ ] **Code:** **Question:** A basic Large image pull check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr describe-images --repository-name REPO` and capture exact status/reason/request ID. layers, node cache, network/NAT and registry quota influence startup time. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-ECR-MN-01

- [ ] **Question:** Compare Repository with Tag immutability. When would each change your design?

**Answer:** Repository: regional namespace with IAM/resource policy and encryption. Tag immutability: prevents overwriting release tags while deployment by digest is stronger identity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECR-MN-02

- [ ] **Question:** Compare Tag immutability with Image scanning. When would each change your design?

**Answer:** Tag immutability: prevents overwriting release tags while deployment by digest is stronger identity. Image scanning: detects known vulnerabilities and requires prioritization/rebuild rather than in-place patch. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECR-MN-03

- [ ] **Question:** Compare Image scanning with Lifecycle policy. When would each change your design?

**Answer:** Image scanning: detects known vulnerabilities and requires prioritization/rebuild rather than in-place patch. Lifecycle policy: expires images by ordered selection rules and can remove rollback artifacts if careless. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECR-MN-04

- [ ] **Configuration review:** **Question:** Compare Lifecycle policy with Cross-Region/account replication. When would each change your design?

**Answer:** Lifecycle policy: expires images by ordered selection rules and can remove rollback artifacts if careless. Cross-Region/account replication: copies eligible artifacts under registry policy and KMS/access constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECR-MN-05

- [ ] **Question:** Compare Cross-Region/account replication with Pull-through cache. When would each change your design?

**Answer:** Cross-Region/account replication: copies eligible artifacts under registry policy and KMS/access constraints. Pull-through cache: mirrors upstream content and reduces availability/rate risk while requiring trust policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECR-MN-06

- [ ] **Question:** Compare Pull-through cache with Authentication token. When would each change your design?

**Answer:** Pull-through cache: mirrors upstream content and reduces availability/rate risk while requiring trust policy. Authentication token: short-lived registry auth derives from AWS identity and must be refreshed. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECR-MN-07

- [ ] **Configuration review:** **Question:** Compare Authentication token with Signature/provenance. When would each change your design?

**Answer:** Authentication token: short-lived registry auth derives from AWS identity and must be refreshed. Signature/provenance: external OCI artifacts/attestations bind trusted build identity to digest. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECR-MN-08

- [ ] **Question:** Compare Signature/provenance with Repository policy. When would each change your design?

**Answer:** Signature/provenance: external OCI artifacts/attestations bind trusted build identity to digest. Repository policy: supports cross-account pulls/pushes but cannot override explicit organization denies. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECR-MN-09

- [ ] **Question:** Compare Repository policy with Large image pull. When would each change your design?

**Answer:** Repository policy: supports cross-account pulls/pushes but cannot override explicit organization denies. Large image pull: layers, node cache, network/NAT and registry quota influence startup time. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECR-MN-10

- [ ] **Configuration review:** **Question:** Compare Large image pull with Repository. When would each change your design?

**Answer:** Large image pull: layers, node cache, network/NAT and registry quota influence startup time. Repository: regional namespace with IAM/resource policy and encryption. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-ECR-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Repository; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr describe-repositories` plus recent events/changes, then correlate the service-specific SLI. regional namespace with IAM/resource policy and encryption. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECR-MP-02

- [ ] **Question:** Production is degraded around Tag immutability; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr describe-images --repository-name REPO` plus recent events/changes, then correlate the service-specific SLI. prevents overwriting release tags while deployment by digest is stronger identity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECR-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Image scanning; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr get-lifecycle-policy --repository-name REPO` plus recent events/changes, then correlate the service-specific SLI. detects known vulnerabilities and requires prioritization/rebuild rather than in-place patch. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECR-MP-04

- [ ] **Question:** Production is degraded around Lifecycle policy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr get-login-password | docker login --username AWS --password-stdin REGISTRY` plus recent events/changes, then correlate the service-specific SLI. expires images by ordered selection rules and can remove rollback artifacts if careless. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECR-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cross-Region/account replication; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr describe-repositories` plus recent events/changes, then correlate the service-specific SLI. copies eligible artifacts under registry policy and KMS/access constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECR-MP-06

- [ ] **Question:** Production is degraded around Pull-through cache; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr describe-images --repository-name REPO` plus recent events/changes, then correlate the service-specific SLI. mirrors upstream content and reduces availability/rate risk while requiring trust policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECR-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Authentication token; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr get-lifecycle-policy --repository-name REPO` plus recent events/changes, then correlate the service-specific SLI. short-lived registry auth derives from AWS identity and must be refreshed. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECR-MP-08

- [ ] **Question:** Production is degraded around Signature/provenance; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr get-login-password | docker login --username AWS --password-stdin REGISTRY` plus recent events/changes, then correlate the service-specific SLI. external OCI artifacts/attestations bind trusted build identity to digest. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECR-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Repository policy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr describe-repositories` plus recent events/changes, then correlate the service-specific SLI. supports cross-account pulls/pushes but cannot override explicit organization denies. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECR-MP-10

- [ ] **Question:** Production is degraded around Large image pull; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr describe-images --repository-name REPO` plus recent events/changes, then correlate the service-specific SLI. layers, node cache, network/NAT and registry quota influence startup time. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-ECR-SN-01

- [ ] **Question:** Design a production Amazon ECR capability where Repository, Lifecycle policy and Authentication token are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: regional namespace with IAM/resource policy and encryption. expires images by ordered selection rules and can remove rollback artifacts if careless. short-lived registry auth derives from AWS identity and must be refreshed. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECR-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ECR capability where Tag immutability, Cross-Region/account replication and Signature/provenance are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prevents overwriting release tags while deployment by digest is stronger identity. copies eligible artifacts under registry policy and KMS/access constraints. external OCI artifacts/attestations bind trusted build identity to digest. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECR-SN-03

- [ ] **Question:** Design a production Amazon ECR capability where Image scanning, Pull-through cache and Repository policy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: detects known vulnerabilities and requires prioritization/rebuild rather than in-place patch. mirrors upstream content and reduces availability/rate risk while requiring trust policy. supports cross-account pulls/pushes but cannot override explicit organization denies. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECR-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ECR capability where Lifecycle policy, Authentication token and Large image pull are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: expires images by ordered selection rules and can remove rollback artifacts if careless. short-lived registry auth derives from AWS identity and must be refreshed. layers, node cache, network/NAT and registry quota influence startup time. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECR-SN-05

- [ ] **Question:** Design a production Amazon ECR capability where Cross-Region/account replication, Signature/provenance and Repository are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: copies eligible artifacts under registry policy and KMS/access constraints. external OCI artifacts/attestations bind trusted build identity to digest. regional namespace with IAM/resource policy and encryption. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECR-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ECR capability where Pull-through cache, Repository policy and Tag immutability are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: mirrors upstream content and reduces availability/rate risk while requiring trust policy. supports cross-account pulls/pushes but cannot override explicit organization denies. prevents overwriting release tags while deployment by digest is stronger identity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECR-SN-07

- [ ] **Question:** Design a production Amazon ECR capability where Authentication token, Large image pull and Image scanning are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: short-lived registry auth derives from AWS identity and must be refreshed. layers, node cache, network/NAT and registry quota influence startup time. detects known vulnerabilities and requires prioritization/rebuild rather than in-place patch. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECR-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ECR capability where Signature/provenance, Repository and Lifecycle policy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: external OCI artifacts/attestations bind trusted build identity to digest. regional namespace with IAM/resource policy and encryption. expires images by ordered selection rules and can remove rollback artifacts if careless. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECR-SN-09

- [ ] **Question:** Design a production Amazon ECR capability where Repository policy, Tag immutability and Cross-Region/account replication are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supports cross-account pulls/pushes but cannot override explicit organization denies. prevents overwriting release tags while deployment by digest is stronger identity. copies eligible artifacts under registry policy and KMS/access constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECR-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ECR capability where Large image pull, Image scanning and Pull-through cache are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: layers, node cache, network/NAT and registry quota influence startup time. detects known vulnerabilities and requires prioritization/rebuild rather than in-place patch. mirrors upstream content and reduces availability/rate risk while requiring trust policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-ECR-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Repository. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr describe-repositories` as one read-only checkpoint, not the whole diagnosis. regional namespace with IAM/resource policy and encryption. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECR-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tag immutability. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr describe-images --repository-name REPO` as one read-only checkpoint, not the whole diagnosis. prevents overwriting release tags while deployment by digest is stronger identity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECR-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Image scanning. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr get-lifecycle-policy --repository-name REPO` as one read-only checkpoint, not the whole diagnosis. detects known vulnerabilities and requires prioritization/rebuild rather than in-place patch. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECR-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lifecycle policy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr get-login-password | docker login --username AWS --password-stdin REGISTRY` as one read-only checkpoint, not the whole diagnosis. expires images by ordered selection rules and can remove rollback artifacts if careless. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECR-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cross-Region/account replication. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr describe-repositories` as one read-only checkpoint, not the whole diagnosis. copies eligible artifacts under registry policy and KMS/access constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECR-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pull-through cache. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr describe-images --repository-name REPO` as one read-only checkpoint, not the whole diagnosis. mirrors upstream content and reduces availability/rate risk while requiring trust policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECR-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authentication token. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr get-lifecycle-policy --repository-name REPO` as one read-only checkpoint, not the whole diagnosis. short-lived registry auth derives from AWS identity and must be refreshed. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECR-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Signature/provenance. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr get-login-password | docker login --username AWS --password-stdin REGISTRY` as one read-only checkpoint, not the whole diagnosis. external OCI artifacts/attestations bind trusted build identity to digest. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECR-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Repository policy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr describe-repositories` as one read-only checkpoint, not the whole diagnosis. supports cross-account pulls/pushes but cannot override explicit organization denies. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECR-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Large image pull. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr describe-images --repository-name REPO` as one read-only checkpoint, not the whole diagnosis. layers, node cache, network/NAT and registry quota influence startup time. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
