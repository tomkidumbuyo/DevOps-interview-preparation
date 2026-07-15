# AI supply chain, signing and provenance — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JN-01

- [ ] **Question:** What is Source provenance, and why does it matter in AI supply chain, signing and provenance?
> **Covered in:** [AI supply chain, signing and provenance — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** repository/revision/review and build identity connect declared source to artifact. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JN-02

- [ ] **Question:** What is Dependency lock/SBOM, and why does it matter in AI supply chain, signing and provenance?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** software names/versions/hashes/licenses/vulnerabilities cover training and serving environments. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JN-03

- [ ] **Question:** What is Model provenance, and why does it matter in AI supply chain, signing and provenance?
> **Covered in:** [AI supply chain, signing and provenance — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** origin, base, fine-tuning data/process, transforms and digest establish lineage beyond filename. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JN-04

- [ ] **Question:** What is Unsafe serialization, and why does it matter in AI supply chain, signing and provenance?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** pickle-like formats can execute code; prefer safe formats and isolated inspection for untrusted models. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JN-05

- [ ] **Question:** What is OCI artifact, and why does it matter in AI supply chain, signing and provenance?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** media types/manifests/subject/referrers store models, SBOMs, signatures and attestations in registries. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JN-06

- [ ] **Question:** What is Signature, and why does it matter in AI supply chain, signing and provenance?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** verifies signer/keyless identity and bytes under trust policy, not model quality or authorization alone. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JN-07

- [ ] **Question:** What is Attestation, and why does it matter in AI supply chain, signing and provenance?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** predicate records build/training/evaluation facts with verifiable producer identity and inputs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JN-08

- [ ] **Code:** **Question:** What does `cosign verify-attestation --type slsaprovenance MODEL_REF` help you verify for AI supply chain, signing and provenance?
> **Covered in:** [AI supply chain, signing and provenance — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: immutability, retention, replication, vulnerability/malware scanning and access logs protect promotion.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JN-09

- [ ] **Code:** **Question:** What does `syft IMAGE -o cyclonedx-json` help you verify for AI supply chain, signing and provenance?
> **Covered in:** [AI supply chain, signing and provenance — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: admission checks exact digest, signature/attestation, policy and environment compatibility.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JN-10

- [ ] **Code:** **Question:** What does `oras manifest fetch MODEL_REF` help you verify for AI supply chain, signing and provenance?
> **Covered in:** [AI supply chain, signing and provenance — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: inventory maps compromised dependency/model to runs, releases and deployments for containment.

## Junior — procedural and command questions

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JP-01

- [ ] **Code:** **Question:** A basic Source provenance check fails. What would you do first using the CLI?
> **Covered in:** [AI supply chain, signing and provenance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `syft IMAGE -o cyclonedx-json` and capture exact status/reason/request ID. repository/revision/review and build identity connect declared source to artifact. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JP-02

- [ ] **Question:** A basic Dependency lock/SBOM check fails. What would you do first?
> **Covered in:** [AI supply chain, signing and provenance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `oras manifest fetch MODEL_REF` and capture exact status/reason/request ID. software names/versions/hashes/licenses/vulnerabilities cover training and serving environments. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JP-03

- [ ] **Question:** A basic Model provenance check fails. What would you do first?
> **Covered in:** [AI supply chain, signing and provenance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cosign verify MODEL_REF` and capture exact status/reason/request ID. origin, base, fine-tuning data/process, transforms and digest establish lineage beyond filename. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JP-04

- [ ] **Code:** **Question:** A basic Unsafe serialization check fails. What would you do first using the CLI?
> **Covered in:** [AI supply chain, signing and provenance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cosign verify-attestation --type slsaprovenance MODEL_REF` and capture exact status/reason/request ID. pickle-like formats can execute code; prefer safe formats and isolated inspection for untrusted models. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JP-05

- [ ] **Question:** A basic OCI artifact check fails. What would you do first?
> **Covered in:** [AI supply chain, signing and provenance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `syft IMAGE -o cyclonedx-json` and capture exact status/reason/request ID. media types/manifests/subject/referrers store models, SBOMs, signatures and attestations in registries. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JP-06

- [ ] **Question:** A basic Signature check fails. What would you do first?
> **Covered in:** [AI supply chain, signing and provenance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `oras manifest fetch MODEL_REF` and capture exact status/reason/request ID. verifies signer/keyless identity and bytes under trust policy, not model quality or authorization alone. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JP-07

- [ ] **Code:** **Question:** A basic Attestation check fails. What would you do first using the CLI?
> **Covered in:** [AI supply chain, signing and provenance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cosign verify MODEL_REF` and capture exact status/reason/request ID. predicate records build/training/evaluation facts with verifiable producer identity and inputs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JP-08

- [ ] **Question:** A basic Registry policy check fails. What would you do first?
> **Covered in:** [AI supply chain, signing and provenance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cosign verify-attestation --type slsaprovenance MODEL_REF` and capture exact status/reason/request ID. immutability, retention, replication, vulnerability/malware scanning and access logs protect promotion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JP-09

- [ ] **Question:** A basic Release verification check fails. What would you do first?
> **Covered in:** [AI supply chain, signing and provenance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `syft IMAGE -o cyclonedx-json` and capture exact status/reason/request ID. admission checks exact digest, signature/attestation, policy and environment compatibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-JP-10

- [ ] **Code:** **Question:** A basic Revocation/response check fails. What would you do first using the CLI?
> **Covered in:** [AI supply chain, signing and provenance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `oras manifest fetch MODEL_REF` and capture exact status/reason/request ID. inventory maps compromised dependency/model to runs, releases and deployments for containment. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MN-01

- [ ] **Question:** Compare Source provenance with Dependency lock/SBOM. When would each change your design?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Source provenance: repository/revision/review and build identity connect declared source to artifact. Dependency lock/SBOM: software names/versions/hashes/licenses/vulnerabilities cover training and serving environments. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MN-02

- [ ] **Question:** Compare Dependency lock/SBOM with Model provenance. When would each change your design?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Dependency lock/SBOM: software names/versions/hashes/licenses/vulnerabilities cover training and serving environments. Model provenance: origin, base, fine-tuning data/process, transforms and digest establish lineage beyond filename. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MN-03

- [ ] **Question:** Compare Model provenance with Unsafe serialization. When would each change your design?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Model provenance: origin, base, fine-tuning data/process, transforms and digest establish lineage beyond filename. Unsafe serialization: pickle-like formats can execute code; prefer safe formats and isolated inspection for untrusted models. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MN-04

- [ ] **Configuration review:** **Question:** Compare Unsafe serialization with OCI artifact. When would each change your design?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Unsafe serialization: pickle-like formats can execute code; prefer safe formats and isolated inspection for untrusted models. OCI artifact: media types/manifests/subject/referrers store models, SBOMs, signatures and attestations in registries. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MN-05

- [ ] **Question:** Compare OCI artifact with Signature. When would each change your design?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** OCI artifact: media types/manifests/subject/referrers store models, SBOMs, signatures and attestations in registries. Signature: verifies signer/keyless identity and bytes under trust policy, not model quality or authorization alone. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MN-06

- [ ] **Question:** Compare Signature with Attestation. When would each change your design?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Signature: verifies signer/keyless identity and bytes under trust policy, not model quality or authorization alone. Attestation: predicate records build/training/evaluation facts with verifiable producer identity and inputs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MN-07

- [ ] **Configuration review:** **Question:** Compare Attestation with Registry policy. When would each change your design?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Attestation: predicate records build/training/evaluation facts with verifiable producer identity and inputs. Registry policy: immutability, retention, replication, vulnerability/malware scanning and access logs protect promotion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MN-08

- [ ] **Question:** Compare Registry policy with Release verification. When would each change your design?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Registry policy: immutability, retention, replication, vulnerability/malware scanning and access logs protect promotion. Release verification: admission checks exact digest, signature/attestation, policy and environment compatibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MN-09

- [ ] **Question:** Compare Release verification with Revocation/response. When would each change your design?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Release verification: admission checks exact digest, signature/attestation, policy and environment compatibility. Revocation/response: inventory maps compromised dependency/model to runs, releases and deployments for containment. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MN-10

- [ ] **Configuration review:** **Question:** Compare Revocation/response with Source provenance. When would each change your design?
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Revocation/response: inventory maps compromised dependency/model to runs, releases and deployments for containment. Source provenance: repository/revision/review and build identity connect declared source to artifact. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Source provenance; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `syft IMAGE -o cyclonedx-json` plus recent events/changes, then correlate the service-specific SLI. repository/revision/review and build identity connect declared source to artifact. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MP-02

- [ ] **Question:** Production is degraded around Dependency lock/SBOM; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `oras manifest fetch MODEL_REF` plus recent events/changes, then correlate the service-specific SLI. software names/versions/hashes/licenses/vulnerabilities cover training and serving environments. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model provenance; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI supply chain, signing and provenance — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cosign verify MODEL_REF` plus recent events/changes, then correlate the service-specific SLI. origin, base, fine-tuning data/process, transforms and digest establish lineage beyond filename. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MP-04

- [ ] **Question:** Production is degraded around Unsafe serialization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cosign verify-attestation --type slsaprovenance MODEL_REF` plus recent events/changes, then correlate the service-specific SLI. pickle-like formats can execute code; prefer safe formats and isolated inspection for untrusted models. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around OCI artifact; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `syft IMAGE -o cyclonedx-json` plus recent events/changes, then correlate the service-specific SLI. media types/manifests/subject/referrers store models, SBOMs, signatures and attestations in registries. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MP-06

- [ ] **Question:** Production is degraded around Signature; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `oras manifest fetch MODEL_REF` plus recent events/changes, then correlate the service-specific SLI. verifies signer/keyless identity and bytes under trust policy, not model quality or authorization alone. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Attestation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cosign verify MODEL_REF` plus recent events/changes, then correlate the service-specific SLI. predicate records build/training/evaluation facts with verifiable producer identity and inputs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MP-08

- [ ] **Question:** Production is degraded around Registry policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cosign verify-attestation --type slsaprovenance MODEL_REF` plus recent events/changes, then correlate the service-specific SLI. immutability, retention, replication, vulnerability/malware scanning and access logs protect promotion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Release verification; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `syft IMAGE -o cyclonedx-json` plus recent events/changes, then correlate the service-specific SLI. admission checks exact digest, signature/attestation, policy and environment compatibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-MP-10

- [ ] **Question:** Production is degraded around Revocation/response; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `oras manifest fetch MODEL_REF` plus recent events/changes, then correlate the service-specific SLI. inventory maps compromised dependency/model to runs, releases and deployments for containment. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SN-01

- [ ] **Question:** Design a production AI supply chain, signing and provenance capability where Source provenance, Unsafe serialization and Attestation are first-class requirements.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: repository/revision/review and build identity connect declared source to artifact. pickle-like formats can execute code; prefer safe formats and isolated inspection for untrusted models. predicate records build/training/evaluation facts with verifiable producer identity and inputs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AI supply chain, signing and provenance capability where Dependency lock/SBOM, OCI artifact and Registry policy are first-class requirements.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: software names/versions/hashes/licenses/vulnerabilities cover training and serving environments. media types/manifests/subject/referrers store models, SBOMs, signatures and attestations in registries. immutability, retention, replication, vulnerability/malware scanning and access logs protect promotion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SN-03

- [ ] **Question:** Design a production AI supply chain, signing and provenance capability where Model provenance, Signature and Release verification are first-class requirements.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: origin, base, fine-tuning data/process, transforms and digest establish lineage beyond filename. verifies signer/keyless identity and bytes under trust policy, not model quality or authorization alone. admission checks exact digest, signature/attestation, policy and environment compatibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AI supply chain, signing and provenance capability where Unsafe serialization, Attestation and Revocation/response are first-class requirements.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pickle-like formats can execute code; prefer safe formats and isolated inspection for untrusted models. predicate records build/training/evaluation facts with verifiable producer identity and inputs. inventory maps compromised dependency/model to runs, releases and deployments for containment. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SN-05

- [ ] **Question:** Design a production AI supply chain, signing and provenance capability where OCI artifact, Registry policy and Source provenance are first-class requirements.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: media types/manifests/subject/referrers store models, SBOMs, signatures and attestations in registries. immutability, retention, replication, vulnerability/malware scanning and access logs protect promotion. repository/revision/review and build identity connect declared source to artifact. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AI supply chain, signing and provenance capability where Signature, Release verification and Dependency lock/SBOM are first-class requirements.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: verifies signer/keyless identity and bytes under trust policy, not model quality or authorization alone. admission checks exact digest, signature/attestation, policy and environment compatibility. software names/versions/hashes/licenses/vulnerabilities cover training and serving environments. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SN-07

- [ ] **Question:** Design a production AI supply chain, signing and provenance capability where Attestation, Revocation/response and Model provenance are first-class requirements.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: predicate records build/training/evaluation facts with verifiable producer identity and inputs. inventory maps compromised dependency/model to runs, releases and deployments for containment. origin, base, fine-tuning data/process, transforms and digest establish lineage beyond filename. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AI supply chain, signing and provenance capability where Registry policy, Source provenance and Unsafe serialization are first-class requirements.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutability, retention, replication, vulnerability/malware scanning and access logs protect promotion. repository/revision/review and build identity connect declared source to artifact. pickle-like formats can execute code; prefer safe formats and isolated inspection for untrusted models. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SN-09

- [ ] **Question:** Design a production AI supply chain, signing and provenance capability where Release verification, Dependency lock/SBOM and OCI artifact are first-class requirements.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: admission checks exact digest, signature/attestation, policy and environment compatibility. software names/versions/hashes/licenses/vulnerabilities cover training and serving environments. media types/manifests/subject/referrers store models, SBOMs, signatures and attestations in registries. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AI supply chain, signing and provenance capability where Revocation/response, Model provenance and Signature are first-class requirements.
> **Covered in:** [AI supply chain, signing and provenance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: inventory maps compromised dependency/model to runs, releases and deployments for containment. origin, base, fine-tuning data/process, transforms and digest establish lineage beyond filename. verifies signer/keyless identity and bytes under trust policy, not model quality or authorization alone. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Source provenance. How do you lead it end to end?
> **Covered in:** [AI supply chain, signing and provenance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `syft IMAGE -o cyclonedx-json` as one read-only checkpoint, not the whole diagnosis. repository/revision/review and build identity connect declared source to artifact. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dependency lock/SBOM. How do you lead it end to end?
> **Covered in:** [AI supply chain, signing and provenance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `oras manifest fetch MODEL_REF` as one read-only checkpoint, not the whole diagnosis. software names/versions/hashes/licenses/vulnerabilities cover training and serving environments. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model provenance. How do you lead it end to end?
> **Covered in:** [AI supply chain, signing and provenance — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cosign verify MODEL_REF` as one read-only checkpoint, not the whole diagnosis. origin, base, fine-tuning data/process, transforms and digest establish lineage beyond filename. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Unsafe serialization. How do you lead it end to end?
> **Covered in:** [AI supply chain, signing and provenance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cosign verify-attestation --type slsaprovenance MODEL_REF` as one read-only checkpoint, not the whole diagnosis. pickle-like formats can execute code; prefer safe formats and isolated inspection for untrusted models. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving OCI artifact. How do you lead it end to end?
> **Covered in:** [AI supply chain, signing and provenance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `syft IMAGE -o cyclonedx-json` as one read-only checkpoint, not the whole diagnosis. media types/manifests/subject/referrers store models, SBOMs, signatures and attestations in registries. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Signature. How do you lead it end to end?
> **Covered in:** [AI supply chain, signing and provenance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `oras manifest fetch MODEL_REF` as one read-only checkpoint, not the whole diagnosis. verifies signer/keyless identity and bytes under trust policy, not model quality or authorization alone. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Attestation. How do you lead it end to end?
> **Covered in:** [AI supply chain, signing and provenance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cosign verify MODEL_REF` as one read-only checkpoint, not the whole diagnosis. predicate records build/training/evaluation facts with verifiable producer identity and inputs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Registry policy. How do you lead it end to end?
> **Covered in:** [AI supply chain, signing and provenance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cosign verify-attestation --type slsaprovenance MODEL_REF` as one read-only checkpoint, not the whole diagnosis. immutability, retention, replication, vulnerability/malware scanning and access logs protect promotion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Release verification. How do you lead it end to end?
> **Covered in:** [AI supply chain, signing and provenance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `syft IMAGE -o cyclonedx-json` as one read-only checkpoint, not the whole diagnosis. admission checks exact digest, signature/attestation, policy and environment compatibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-SUPPLY-CHAIN-SIGNING-AND-PROVENANCE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Revocation/response. How do you lead it end to end?
> **Covered in:** [AI supply chain, signing and provenance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `oras manifest fetch MODEL_REF` as one read-only checkpoint, not the whole diagnosis. inventory maps compromised dependency/model to runs, releases and deployments for containment. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AI governance, approval and evidence automation](../24-governance-approval-evidence/README.md) · [Study note](README.md) · [Next: MLOps/LLMOps FinOps and capacity →](../26-ai-finops-capacity/README.md)

<!-- reading-navigation:end -->
