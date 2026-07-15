# Model registry, artifacts and lineage — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JN-01

- [ ] **Question:** What is Registered model, and why does it matter in Model registry, artifacts and lineage?

**Answer:** logical product/capability groups versions without conflating mutable alias with byte identity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JN-02

- [ ] **Question:** What is Model version, and why does it matter in Model registry, artifacts and lineage?

**Answer:** immutable digest plus source run/data/code/config defines one candidate. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JN-03

- [ ] **Question:** What is Alias, and why does it matter in Model registry, artifacts and lineage?

**Answer:** Champion/Challenger/production is a mutable pointer changed through authorized auditable promotion. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JN-04

- [ ] **Question:** What is Artifact format, and why does it matter in Model registry, artifacts and lineage?

**Answer:** framework-native, safetensors, ONNX or MLflow flavor determines loader/runtime compatibility and attack surface. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JN-05

- [ ] **Question:** What is Signature/schema, and why does it matter in Model registry, artifacts and lineage?

**Answer:** input/output names/types/shapes and preprocessing contract prevent silent integration mismatch. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JN-06

- [ ] **Question:** What is Lineage, and why does it matter in Model registry, artifacts and lineage?

**Answer:** dataset/run/checkpoint/evaluation/license/approval links support reproduction and impact analysis. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JN-07

- [ ] **Question:** What is Model card, and why does it matter in Model registry, artifacts and lineage?

**Answer:** intended use, limitations, training/evaluation data summary and risk evidence inform consumers. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JN-08

- [ ] **Code:** **Question:** What does `oras manifest fetch REGISTRY/REPOSITORY@sha256:DIGEST` help you verify for Model registry, artifacts and lineage?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: encryption, immutable retention, replication, malware/unsafe-deserialization controls and restore tests protect artifacts.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JN-09

- [ ] **Code:** **Question:** What does `mlflow models search -f 'name = MODEL_NAME'` help you verify for Model registry, artifacts and lineage?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: separate discover/download/promote/delete privileges and audit sensitive model exfiltration.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JN-10

- [ ] **Code:** **Question:** What does `mlflow artifacts download --run-id RUN_ID --artifact-path model` help you verify for Model registry, artifacts and lineage?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: deployed endpoint records exact model/runtime/prompt/index/policy revision rather than only an alias.

## Junior — procedural and command questions

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JP-01

- [ ] **Code:** **Question:** A basic Registered model check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow models search -f 'name = MODEL_NAME'` and capture exact status/reason/request ID. logical product/capability groups versions without conflating mutable alias with byte identity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JP-02

- [ ] **Question:** A basic Model version check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow artifacts download --run-id RUN_ID --artifact-path model` and capture exact status/reason/request ID. immutable digest plus source run/data/code/config defines one candidate. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JP-03

- [ ] **Question:** A basic Alias check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `sha256sum MODEL_ARTIFACT` and capture exact status/reason/request ID. Champion/Challenger/production is a mutable pointer changed through authorized auditable promotion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JP-04

- [ ] **Code:** **Question:** A basic Artifact format check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `oras manifest fetch REGISTRY/REPOSITORY@sha256:DIGEST` and capture exact status/reason/request ID. framework-native, safetensors, ONNX or MLflow flavor determines loader/runtime compatibility and attack surface. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JP-05

- [ ] **Question:** A basic Signature/schema check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow models search -f 'name = MODEL_NAME'` and capture exact status/reason/request ID. input/output names/types/shapes and preprocessing contract prevent silent integration mismatch. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JP-06

- [ ] **Question:** A basic Lineage check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow artifacts download --run-id RUN_ID --artifact-path model` and capture exact status/reason/request ID. dataset/run/checkpoint/evaluation/license/approval links support reproduction and impact analysis. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JP-07

- [ ] **Code:** **Question:** A basic Model card check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `sha256sum MODEL_ARTIFACT` and capture exact status/reason/request ID. intended use, limitations, training/evaluation data summary and risk evidence inform consumers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JP-08

- [ ] **Question:** A basic Storage check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `oras manifest fetch REGISTRY/REPOSITORY@sha256:DIGEST` and capture exact status/reason/request ID. encryption, immutable retention, replication, malware/unsafe-deserialization controls and restore tests protect artifacts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JP-09

- [ ] **Question:** A basic Access check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow models search -f 'name = MODEL_NAME'` and capture exact status/reason/request ID. separate discover/download/promote/delete privileges and audit sensitive model exfiltration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-JP-10

- [ ] **Code:** **Question:** A basic Deployment binding check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow artifacts download --run-id RUN_ID --artifact-path model` and capture exact status/reason/request ID. deployed endpoint records exact model/runtime/prompt/index/policy revision rather than only an alias. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MN-01

- [ ] **Question:** Compare Registered model with Model version. When would each change your design?

**Answer:** Registered model: logical product/capability groups versions without conflating mutable alias with byte identity. Model version: immutable digest plus source run/data/code/config defines one candidate. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MN-02

- [ ] **Question:** Compare Model version with Alias. When would each change your design?

**Answer:** Model version: immutable digest plus source run/data/code/config defines one candidate. Alias: Champion/Challenger/production is a mutable pointer changed through authorized auditable promotion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MN-03

- [ ] **Question:** Compare Alias with Artifact format. When would each change your design?

**Answer:** Alias: Champion/Challenger/production is a mutable pointer changed through authorized auditable promotion. Artifact format: framework-native, safetensors, ONNX or MLflow flavor determines loader/runtime compatibility and attack surface. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MN-04

- [ ] **Configuration review:** **Question:** Compare Artifact format with Signature/schema. When would each change your design?

**Answer:** Artifact format: framework-native, safetensors, ONNX or MLflow flavor determines loader/runtime compatibility and attack surface. Signature/schema: input/output names/types/shapes and preprocessing contract prevent silent integration mismatch. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MN-05

- [ ] **Question:** Compare Signature/schema with Lineage. When would each change your design?

**Answer:** Signature/schema: input/output names/types/shapes and preprocessing contract prevent silent integration mismatch. Lineage: dataset/run/checkpoint/evaluation/license/approval links support reproduction and impact analysis. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MN-06

- [ ] **Question:** Compare Lineage with Model card. When would each change your design?

**Answer:** Lineage: dataset/run/checkpoint/evaluation/license/approval links support reproduction and impact analysis. Model card: intended use, limitations, training/evaluation data summary and risk evidence inform consumers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MN-07

- [ ] **Configuration review:** **Question:** Compare Model card with Storage. When would each change your design?

**Answer:** Model card: intended use, limitations, training/evaluation data summary and risk evidence inform consumers. Storage: encryption, immutable retention, replication, malware/unsafe-deserialization controls and restore tests protect artifacts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MN-08

- [ ] **Question:** Compare Storage with Access. When would each change your design?

**Answer:** Storage: encryption, immutable retention, replication, malware/unsafe-deserialization controls and restore tests protect artifacts. Access: separate discover/download/promote/delete privileges and audit sensitive model exfiltration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MN-09

- [ ] **Question:** Compare Access with Deployment binding. When would each change your design?

**Answer:** Access: separate discover/download/promote/delete privileges and audit sensitive model exfiltration. Deployment binding: deployed endpoint records exact model/runtime/prompt/index/policy revision rather than only an alias. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MN-10

- [ ] **Configuration review:** **Question:** Compare Deployment binding with Registered model. When would each change your design?

**Answer:** Deployment binding: deployed endpoint records exact model/runtime/prompt/index/policy revision rather than only an alias. Registered model: logical product/capability groups versions without conflating mutable alias with byte identity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Registered model; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow models search -f 'name = MODEL_NAME'` plus recent events/changes, then correlate the service-specific SLI. logical product/capability groups versions without conflating mutable alias with byte identity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MP-02

- [ ] **Question:** Production is degraded around Model version; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow artifacts download --run-id RUN_ID --artifact-path model` plus recent events/changes, then correlate the service-specific SLI. immutable digest plus source run/data/code/config defines one candidate. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Alias; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `sha256sum MODEL_ARTIFACT` plus recent events/changes, then correlate the service-specific SLI. Champion/Challenger/production is a mutable pointer changed through authorized auditable promotion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MP-04

- [ ] **Question:** Production is degraded around Artifact format; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `oras manifest fetch REGISTRY/REPOSITORY@sha256:DIGEST` plus recent events/changes, then correlate the service-specific SLI. framework-native, safetensors, ONNX or MLflow flavor determines loader/runtime compatibility and attack surface. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Signature/schema; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow models search -f 'name = MODEL_NAME'` plus recent events/changes, then correlate the service-specific SLI. input/output names/types/shapes and preprocessing contract prevent silent integration mismatch. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MP-06

- [ ] **Question:** Production is degraded around Lineage; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow artifacts download --run-id RUN_ID --artifact-path model` plus recent events/changes, then correlate the service-specific SLI. dataset/run/checkpoint/evaluation/license/approval links support reproduction and impact analysis. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model card; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `sha256sum MODEL_ARTIFACT` plus recent events/changes, then correlate the service-specific SLI. intended use, limitations, training/evaluation data summary and risk evidence inform consumers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MP-08

- [ ] **Question:** Production is degraded around Storage; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `oras manifest fetch REGISTRY/REPOSITORY@sha256:DIGEST` plus recent events/changes, then correlate the service-specific SLI. encryption, immutable retention, replication, malware/unsafe-deserialization controls and restore tests protect artifacts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Access; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow models search -f 'name = MODEL_NAME'` plus recent events/changes, then correlate the service-specific SLI. separate discover/download/promote/delete privileges and audit sensitive model exfiltration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-MP-10

- [ ] **Question:** Production is degraded around Deployment binding; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow artifacts download --run-id RUN_ID --artifact-path model` plus recent events/changes, then correlate the service-specific SLI. deployed endpoint records exact model/runtime/prompt/index/policy revision rather than only an alias. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SN-01

- [ ] **Question:** Design a production Model registry, artifacts and lineage capability where Registered model, Artifact format and Model card are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: logical product/capability groups versions without conflating mutable alias with byte identity. framework-native, safetensors, ONNX or MLflow flavor determines loader/runtime compatibility and attack surface. intended use, limitations, training/evaluation data summary and risk evidence inform consumers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Model registry, artifacts and lineage capability where Model version, Signature/schema and Storage are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable digest plus source run/data/code/config defines one candidate. input/output names/types/shapes and preprocessing contract prevent silent integration mismatch. encryption, immutable retention, replication, malware/unsafe-deserialization controls and restore tests protect artifacts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SN-03

- [ ] **Question:** Design a production Model registry, artifacts and lineage capability where Alias, Lineage and Access are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Champion/Challenger/production is a mutable pointer changed through authorized auditable promotion. dataset/run/checkpoint/evaluation/license/approval links support reproduction and impact analysis. separate discover/download/promote/delete privileges and audit sensitive model exfiltration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Model registry, artifacts and lineage capability where Artifact format, Model card and Deployment binding are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: framework-native, safetensors, ONNX or MLflow flavor determines loader/runtime compatibility and attack surface. intended use, limitations, training/evaluation data summary and risk evidence inform consumers. deployed endpoint records exact model/runtime/prompt/index/policy revision rather than only an alias. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SN-05

- [ ] **Question:** Design a production Model registry, artifacts and lineage capability where Signature/schema, Storage and Registered model are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: input/output names/types/shapes and preprocessing contract prevent silent integration mismatch. encryption, immutable retention, replication, malware/unsafe-deserialization controls and restore tests protect artifacts. logical product/capability groups versions without conflating mutable alias with byte identity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Model registry, artifacts and lineage capability where Lineage, Access and Model version are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: dataset/run/checkpoint/evaluation/license/approval links support reproduction and impact analysis. separate discover/download/promote/delete privileges and audit sensitive model exfiltration. immutable digest plus source run/data/code/config defines one candidate. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SN-07

- [ ] **Question:** Design a production Model registry, artifacts and lineage capability where Model card, Deployment binding and Alias are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: intended use, limitations, training/evaluation data summary and risk evidence inform consumers. deployed endpoint records exact model/runtime/prompt/index/policy revision rather than only an alias. Champion/Challenger/production is a mutable pointer changed through authorized auditable promotion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Model registry, artifacts and lineage capability where Storage, Registered model and Artifact format are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: encryption, immutable retention, replication, malware/unsafe-deserialization controls and restore tests protect artifacts. logical product/capability groups versions without conflating mutable alias with byte identity. framework-native, safetensors, ONNX or MLflow flavor determines loader/runtime compatibility and attack surface. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SN-09

- [ ] **Question:** Design a production Model registry, artifacts and lineage capability where Access, Model version and Signature/schema are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: separate discover/download/promote/delete privileges and audit sensitive model exfiltration. immutable digest plus source run/data/code/config defines one candidate. input/output names/types/shapes and preprocessing contract prevent silent integration mismatch. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Model registry, artifacts and lineage capability where Deployment binding, Alias and Lineage are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: deployed endpoint records exact model/runtime/prompt/index/policy revision rather than only an alias. Champion/Challenger/production is a mutable pointer changed through authorized auditable promotion. dataset/run/checkpoint/evaluation/license/approval links support reproduction and impact analysis. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Registered model. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow models search -f 'name = MODEL_NAME'` as one read-only checkpoint, not the whole diagnosis. logical product/capability groups versions without conflating mutable alias with byte identity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model version. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow artifacts download --run-id RUN_ID --artifact-path model` as one read-only checkpoint, not the whole diagnosis. immutable digest plus source run/data/code/config defines one candidate. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Alias. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `sha256sum MODEL_ARTIFACT` as one read-only checkpoint, not the whole diagnosis. Champion/Challenger/production is a mutable pointer changed through authorized auditable promotion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Artifact format. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `oras manifest fetch REGISTRY/REPOSITORY@sha256:DIGEST` as one read-only checkpoint, not the whole diagnosis. framework-native, safetensors, ONNX or MLflow flavor determines loader/runtime compatibility and attack surface. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Signature/schema. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow models search -f 'name = MODEL_NAME'` as one read-only checkpoint, not the whole diagnosis. input/output names/types/shapes and preprocessing contract prevent silent integration mismatch. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lineage. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow artifacts download --run-id RUN_ID --artifact-path model` as one read-only checkpoint, not the whole diagnosis. dataset/run/checkpoint/evaluation/license/approval links support reproduction and impact analysis. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model card. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `sha256sum MODEL_ARTIFACT` as one read-only checkpoint, not the whole diagnosis. intended use, limitations, training/evaluation data summary and risk evidence inform consumers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Storage. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `oras manifest fetch REGISTRY/REPOSITORY@sha256:DIGEST` as one read-only checkpoint, not the whole diagnosis. encryption, immutable retention, replication, malware/unsafe-deserialization controls and restore tests protect artifacts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Access. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow models search -f 'name = MODEL_NAME'` as one read-only checkpoint, not the whole diagnosis. separate discover/download/promote/delete privileges and audit sensitive model exfiltration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MODEL-REGISTRY-ARTIFACTS-AND-LINEAGE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deployment binding. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow artifacts download --run-id RUN_ID --artifact-path model` as one read-only checkpoint, not the whole diagnosis. deployed endpoint records exact model/runtime/prompt/index/policy revision rather than only an alias. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
