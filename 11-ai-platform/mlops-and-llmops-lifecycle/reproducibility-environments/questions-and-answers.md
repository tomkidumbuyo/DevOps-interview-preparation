# Reproducibility and environment capture — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JN-01

- [ ] **Question:** What is Code revision, and why does it matter in Reproducibility and environment capture?

**Answer:** clean commit plus reviewed patch/submodule identity is stronger than an uncommitted notebook snapshot. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JN-02

- [ ] **Question:** What is Dependency lock, and why does it matter in Reproducibility and environment capture?

**Answer:** resolved package names/versions/hashes and index source prevent floating environments. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JN-03

- [ ] **Question:** What is Container digest, and why does it matter in Reproducibility and environment capture?

**Answer:** captures userspace bytes but not host kernel, driver, devices, external services or mutable downloads. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JN-04

- [ ] **Question:** What is Dataset manifest, and why does it matter in Reproducibility and environment capture?

**Answer:** immutable snapshot/transform/split identity is required in addition to a storage URI. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JN-05

- [ ] **Question:** What is Randomness, and why does it matter in Reproducibility and environment capture?

**Answer:** seeds and RNG states across libraries/workers are recorded while nondeterminism is measured. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JN-06

- [ ] **Question:** What is Hardware/software fingerprint, and why does it matter in Reproducibility and environment capture?

**Answer:** accelerator, driver, CUDA/ROCm, library and topology can change numerics/performance. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JN-07

- [ ] **Question:** What is Configuration, and why does it matter in Reproducibility and environment capture?

**Answer:** effective validated config is stored after defaults/overrides without secrets. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JN-08

- [ ] **Code:** **Question:** What does `nvidia-smi --query-gpu=name,driver_version --format=csv` help you verify for Reproducibility and environment capture?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: foundation APIs, base models, feature services and remote code need version/contract evidence.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JN-09

- [ ] **Code:** **Question:** What does `git status --short; git rev-parse HEAD` help you verify for Reproducibility and environment capture?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: bitwise, numerical or metric-range criteria depend on workload and kernel behavior.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JN-10

- [ ] **Code:** **Question:** What does `python -m pip freeze; python -m pip check` help you verify for Reproducibility and environment capture?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: isolated build with pinned sources proves more than retaining an old mutable worker.

## Junior — procedural and command questions

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JP-01

- [ ] **Code:** **Question:** A basic Code revision check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git status --short; git rev-parse HEAD` and capture exact status/reason/request ID. clean commit plus reviewed patch/submodule identity is stronger than an uncommitted notebook snapshot. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JP-02

- [ ] **Question:** A basic Dependency lock check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pip freeze; python -m pip check` and capture exact status/reason/request ID. resolved package names/versions/hashes and index source prevent floating environments. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JP-03

- [ ] **Question:** A basic Container digest check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker image inspect IMAGE --format '{{json .RepoDigests}}'` and capture exact status/reason/request ID. captures userspace bytes but not host kernel, driver, devices, external services or mutable downloads. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JP-04

- [ ] **Code:** **Question:** A basic Dataset manifest check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi --query-gpu=name,driver_version --format=csv` and capture exact status/reason/request ID. immutable snapshot/transform/split identity is required in addition to a storage URI. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JP-05

- [ ] **Question:** A basic Randomness check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git status --short; git rev-parse HEAD` and capture exact status/reason/request ID. seeds and RNG states across libraries/workers are recorded while nondeterminism is measured. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JP-06

- [ ] **Question:** A basic Hardware/software fingerprint check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pip freeze; python -m pip check` and capture exact status/reason/request ID. accelerator, driver, CUDA/ROCm, library and topology can change numerics/performance. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JP-07

- [ ] **Code:** **Question:** A basic Configuration check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker image inspect IMAGE --format '{{json .RepoDigests}}'` and capture exact status/reason/request ID. effective validated config is stored after defaults/overrides without secrets. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JP-08

- [ ] **Question:** A basic External dependency check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi --query-gpu=name,driver_version --format=csv` and capture exact status/reason/request ID. foundation APIs, base models, feature services and remote code need version/contract evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JP-09

- [ ] **Question:** A basic Reproduction tolerance check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git status --short; git rev-parse HEAD` and capture exact status/reason/request ID. bitwise, numerical or metric-range criteria depend on workload and kernel behavior. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-JP-10

- [ ] **Code:** **Question:** A basic Hermetic rebuild check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pip freeze; python -m pip check` and capture exact status/reason/request ID. isolated build with pinned sources proves more than retaining an old mutable worker. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MN-01

- [ ] **Question:** Compare Code revision with Dependency lock. When would each change your design?

**Answer:** Code revision: clean commit plus reviewed patch/submodule identity is stronger than an uncommitted notebook snapshot. Dependency lock: resolved package names/versions/hashes and index source prevent floating environments. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MN-02

- [ ] **Question:** Compare Dependency lock with Container digest. When would each change your design?

**Answer:** Dependency lock: resolved package names/versions/hashes and index source prevent floating environments. Container digest: captures userspace bytes but not host kernel, driver, devices, external services or mutable downloads. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MN-03

- [ ] **Question:** Compare Container digest with Dataset manifest. When would each change your design?

**Answer:** Container digest: captures userspace bytes but not host kernel, driver, devices, external services or mutable downloads. Dataset manifest: immutable snapshot/transform/split identity is required in addition to a storage URI. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MN-04

- [ ] **Configuration review:** **Question:** Compare Dataset manifest with Randomness. When would each change your design?

**Answer:** Dataset manifest: immutable snapshot/transform/split identity is required in addition to a storage URI. Randomness: seeds and RNG states across libraries/workers are recorded while nondeterminism is measured. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MN-05

- [ ] **Question:** Compare Randomness with Hardware/software fingerprint. When would each change your design?

**Answer:** Randomness: seeds and RNG states across libraries/workers are recorded while nondeterminism is measured. Hardware/software fingerprint: accelerator, driver, CUDA/ROCm, library and topology can change numerics/performance. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MN-06

- [ ] **Question:** Compare Hardware/software fingerprint with Configuration. When would each change your design?

**Answer:** Hardware/software fingerprint: accelerator, driver, CUDA/ROCm, library and topology can change numerics/performance. Configuration: effective validated config is stored after defaults/overrides without secrets. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MN-07

- [ ] **Configuration review:** **Question:** Compare Configuration with External dependency. When would each change your design?

**Answer:** Configuration: effective validated config is stored after defaults/overrides without secrets. External dependency: foundation APIs, base models, feature services and remote code need version/contract evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MN-08

- [ ] **Question:** Compare External dependency with Reproduction tolerance. When would each change your design?

**Answer:** External dependency: foundation APIs, base models, feature services and remote code need version/contract evidence. Reproduction tolerance: bitwise, numerical or metric-range criteria depend on workload and kernel behavior. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MN-09

- [ ] **Question:** Compare Reproduction tolerance with Hermetic rebuild. When would each change your design?

**Answer:** Reproduction tolerance: bitwise, numerical or metric-range criteria depend on workload and kernel behavior. Hermetic rebuild: isolated build with pinned sources proves more than retaining an old mutable worker. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MN-10

- [ ] **Configuration review:** **Question:** Compare Hermetic rebuild with Code revision. When would each change your design?

**Answer:** Hermetic rebuild: isolated build with pinned sources proves more than retaining an old mutable worker. Code revision: clean commit plus reviewed patch/submodule identity is stronger than an uncommitted notebook snapshot. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Code revision; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git status --short; git rev-parse HEAD` plus recent events/changes, then correlate the service-specific SLI. clean commit plus reviewed patch/submodule identity is stronger than an uncommitted notebook snapshot. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MP-02

- [ ] **Question:** Production is degraded around Dependency lock; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pip freeze; python -m pip check` plus recent events/changes, then correlate the service-specific SLI. resolved package names/versions/hashes and index source prevent floating environments. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Container digest; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker image inspect IMAGE --format '{{json .RepoDigests}}'` plus recent events/changes, then correlate the service-specific SLI. captures userspace bytes but not host kernel, driver, devices, external services or mutable downloads. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MP-04

- [ ] **Question:** Production is degraded around Dataset manifest; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi --query-gpu=name,driver_version --format=csv` plus recent events/changes, then correlate the service-specific SLI. immutable snapshot/transform/split identity is required in addition to a storage URI. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Randomness; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git status --short; git rev-parse HEAD` plus recent events/changes, then correlate the service-specific SLI. seeds and RNG states across libraries/workers are recorded while nondeterminism is measured. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MP-06

- [ ] **Question:** Production is degraded around Hardware/software fingerprint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pip freeze; python -m pip check` plus recent events/changes, then correlate the service-specific SLI. accelerator, driver, CUDA/ROCm, library and topology can change numerics/performance. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Configuration; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker image inspect IMAGE --format '{{json .RepoDigests}}'` plus recent events/changes, then correlate the service-specific SLI. effective validated config is stored after defaults/overrides without secrets. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MP-08

- [ ] **Question:** Production is degraded around External dependency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi --query-gpu=name,driver_version --format=csv` plus recent events/changes, then correlate the service-specific SLI. foundation APIs, base models, feature services and remote code need version/contract evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Reproduction tolerance; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git status --short; git rev-parse HEAD` plus recent events/changes, then correlate the service-specific SLI. bitwise, numerical or metric-range criteria depend on workload and kernel behavior. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-MP-10

- [ ] **Question:** Production is degraded around Hermetic rebuild; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pip freeze; python -m pip check` plus recent events/changes, then correlate the service-specific SLI. isolated build with pinned sources proves more than retaining an old mutable worker. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SN-01

- [ ] **Question:** Design a production Reproducibility and environment capture capability where Code revision, Dataset manifest and Configuration are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: clean commit plus reviewed patch/submodule identity is stronger than an uncommitted notebook snapshot. immutable snapshot/transform/split identity is required in addition to a storage URI. effective validated config is stored after defaults/overrides without secrets. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Reproducibility and environment capture capability where Dependency lock, Randomness and External dependency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: resolved package names/versions/hashes and index source prevent floating environments. seeds and RNG states across libraries/workers are recorded while nondeterminism is measured. foundation APIs, base models, feature services and remote code need version/contract evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SN-03

- [ ] **Question:** Design a production Reproducibility and environment capture capability where Container digest, Hardware/software fingerprint and Reproduction tolerance are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: captures userspace bytes but not host kernel, driver, devices, external services or mutable downloads. accelerator, driver, CUDA/ROCm, library and topology can change numerics/performance. bitwise, numerical or metric-range criteria depend on workload and kernel behavior. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Reproducibility and environment capture capability where Dataset manifest, Configuration and Hermetic rebuild are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable snapshot/transform/split identity is required in addition to a storage URI. effective validated config is stored after defaults/overrides without secrets. isolated build with pinned sources proves more than retaining an old mutable worker. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SN-05

- [ ] **Question:** Design a production Reproducibility and environment capture capability where Randomness, External dependency and Code revision are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: seeds and RNG states across libraries/workers are recorded while nondeterminism is measured. foundation APIs, base models, feature services and remote code need version/contract evidence. clean commit plus reviewed patch/submodule identity is stronger than an uncommitted notebook snapshot. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Reproducibility and environment capture capability where Hardware/software fingerprint, Reproduction tolerance and Dependency lock are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: accelerator, driver, CUDA/ROCm, library and topology can change numerics/performance. bitwise, numerical or metric-range criteria depend on workload and kernel behavior. resolved package names/versions/hashes and index source prevent floating environments. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SN-07

- [ ] **Question:** Design a production Reproducibility and environment capture capability where Configuration, Hermetic rebuild and Container digest are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: effective validated config is stored after defaults/overrides without secrets. isolated build with pinned sources proves more than retaining an old mutable worker. captures userspace bytes but not host kernel, driver, devices, external services or mutable downloads. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Reproducibility and environment capture capability where External dependency, Code revision and Dataset manifest are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: foundation APIs, base models, feature services and remote code need version/contract evidence. clean commit plus reviewed patch/submodule identity is stronger than an uncommitted notebook snapshot. immutable snapshot/transform/split identity is required in addition to a storage URI. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SN-09

- [ ] **Question:** Design a production Reproducibility and environment capture capability where Reproduction tolerance, Dependency lock and Randomness are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bitwise, numerical or metric-range criteria depend on workload and kernel behavior. resolved package names/versions/hashes and index source prevent floating environments. seeds and RNG states across libraries/workers are recorded while nondeterminism is measured. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Reproducibility and environment capture capability where Hermetic rebuild, Container digest and Hardware/software fingerprint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: isolated build with pinned sources proves more than retaining an old mutable worker. captures userspace bytes but not host kernel, driver, devices, external services or mutable downloads. accelerator, driver, CUDA/ROCm, library and topology can change numerics/performance. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Code revision. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git status --short; git rev-parse HEAD` as one read-only checkpoint, not the whole diagnosis. clean commit plus reviewed patch/submodule identity is stronger than an uncommitted notebook snapshot. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dependency lock. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pip freeze; python -m pip check` as one read-only checkpoint, not the whole diagnosis. resolved package names/versions/hashes and index source prevent floating environments. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Container digest. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker image inspect IMAGE --format '{{json .RepoDigests}}'` as one read-only checkpoint, not the whole diagnosis. captures userspace bytes but not host kernel, driver, devices, external services or mutable downloads. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dataset manifest. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi --query-gpu=name,driver_version --format=csv` as one read-only checkpoint, not the whole diagnosis. immutable snapshot/transform/split identity is required in addition to a storage URI. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Randomness. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git status --short; git rev-parse HEAD` as one read-only checkpoint, not the whole diagnosis. seeds and RNG states across libraries/workers are recorded while nondeterminism is measured. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hardware/software fingerprint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pip freeze; python -m pip check` as one read-only checkpoint, not the whole diagnosis. accelerator, driver, CUDA/ROCm, library and topology can change numerics/performance. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Configuration. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker image inspect IMAGE --format '{{json .RepoDigests}}'` as one read-only checkpoint, not the whole diagnosis. effective validated config is stored after defaults/overrides without secrets. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving External dependency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi --query-gpu=name,driver_version --format=csv` as one read-only checkpoint, not the whole diagnosis. foundation APIs, base models, feature services and remote code need version/contract evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reproduction tolerance. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git status --short; git rev-parse HEAD` as one read-only checkpoint, not the whole diagnosis. bitwise, numerical or metric-range criteria depend on workload and kernel behavior. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### REPRODUCIBILITY-AND-ENVIRONMENT-CAPTURE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hermetic rebuild. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pip freeze; python -m pip check` as one read-only checkpoint, not the whole diagnosis. isolated build with pinned sources proves more than retaining an old mutable worker. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
