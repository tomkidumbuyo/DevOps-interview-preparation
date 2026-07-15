# AMIs, Image Builder and golden images — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JN-01

- [ ] **Question:** What is AMI, and why does it matter in AMIs, Image Builder and golden images?

**Answer:** boot image metadata and snapshots define instance root and launch compatibility. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JN-02

- [ ] **Question:** What is Golden image, and why does it matter in AMIs, Image Builder and golden images?

**Answer:** centrally hardened/tested base reduces bootstrap drift and replacement time. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JN-03

- [ ] **Question:** What is Image Builder pipeline, and why does it matter in AMIs, Image Builder and golden images?

**Answer:** recipes/components/infrastructure/distribution automate build/test/copy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JN-04

- [ ] **Question:** What is Packer, and why does it matter in AMIs, Image Builder and golden images?

**Answer:** vendor-neutral image build tool whose builders/provisioners need reproducibility and secret controls. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JN-05

- [ ] **Question:** What is Patch baseline, and why does it matter in AMIs, Image Builder and golden images?

**Answer:** determines approved updates but must be followed by regression qualification. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JN-06

- [ ] **Question:** What is SBOM/provenance, and why does it matter in AMIs, Image Builder and golden images?

**Answer:** records packages/build source and supports vulnerability/rebuild decisions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JN-07

- [ ] **Question:** What is Signing/approval, and why does it matter in AMIs, Image Builder and golden images?

**Answer:** binds release process to an exact AMI/artifact rather than a name lookup. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JN-08

- [ ] **Code:** **Question:** What does `aws ec2 copy-image --source-region REGION --source-image-id AMI --name NAME` help you verify for AMIs, Image Builder and golden images?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: account sharing, KMS keys and Region copies must preserve launch/decrypt permission.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-images --owners self` help you verify for AMIs, Image Builder and golden images?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: validates boot, SSM, agents, workload and performance before fleet refresh.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JN-10

- [ ] **Code:** **Question:** What does `aws imagebuilder list-image-pipelines` help you verify for AMIs, Image Builder and golden images?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: owner/reference inventory and rollback window prevent deleting still-used images/snapshots.

## Junior — procedural and command questions

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JP-01

- [ ] **Code:** **Question:** A basic AMI check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-images --owners self` and capture exact status/reason/request ID. boot image metadata and snapshots define instance root and launch compatibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JP-02

- [ ] **Question:** A basic Golden image check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws imagebuilder list-image-pipelines` and capture exact status/reason/request ID. centrally hardened/tested base reduces bootstrap drift and replacement time. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JP-03

- [ ] **Question:** A basic Image Builder pipeline check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws imagebuilder start-image-pipeline-execution --image-pipeline-arn ARN` and capture exact status/reason/request ID. recipes/components/infrastructure/distribution automate build/test/copy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JP-04

- [ ] **Code:** **Question:** A basic Packer check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 copy-image --source-region REGION --source-image-id AMI --name NAME` and capture exact status/reason/request ID. vendor-neutral image build tool whose builders/provisioners need reproducibility and secret controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JP-05

- [ ] **Question:** A basic Patch baseline check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-images --owners self` and capture exact status/reason/request ID. determines approved updates but must be followed by regression qualification. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JP-06

- [ ] **Question:** A basic SBOM/provenance check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws imagebuilder list-image-pipelines` and capture exact status/reason/request ID. records packages/build source and supports vulnerability/rebuild decisions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JP-07

- [ ] **Code:** **Question:** A basic Signing/approval check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws imagebuilder start-image-pipeline-execution --image-pipeline-arn ARN` and capture exact status/reason/request ID. binds release process to an exact AMI/artifact rather than a name lookup. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JP-08

- [ ] **Question:** A basic Distribution check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 copy-image --source-region REGION --source-image-id AMI --name NAME` and capture exact status/reason/request ID. account sharing, KMS keys and Region copies must preserve launch/decrypt permission. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JP-09

- [ ] **Question:** A basic Canary instance/pool check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-images --owners self` and capture exact status/reason/request ID. validates boot, SSM, agents, workload and performance before fleet refresh. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-JP-10

- [ ] **Code:** **Question:** A basic Retirement check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws imagebuilder list-image-pipelines` and capture exact status/reason/request ID. owner/reference inventory and rollback window prevent deleting still-used images/snapshots. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MN-01

- [ ] **Question:** Compare AMI with Golden image. When would each change your design?

**Answer:** AMI: boot image metadata and snapshots define instance root and launch compatibility. Golden image: centrally hardened/tested base reduces bootstrap drift and replacement time. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MN-02

- [ ] **Question:** Compare Golden image with Image Builder pipeline. When would each change your design?

**Answer:** Golden image: centrally hardened/tested base reduces bootstrap drift and replacement time. Image Builder pipeline: recipes/components/infrastructure/distribution automate build/test/copy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MN-03

- [ ] **Question:** Compare Image Builder pipeline with Packer. When would each change your design?

**Answer:** Image Builder pipeline: recipes/components/infrastructure/distribution automate build/test/copy. Packer: vendor-neutral image build tool whose builders/provisioners need reproducibility and secret controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MN-04

- [ ] **Configuration review:** **Question:** Compare Packer with Patch baseline. When would each change your design?

**Answer:** Packer: vendor-neutral image build tool whose builders/provisioners need reproducibility and secret controls. Patch baseline: determines approved updates but must be followed by regression qualification. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MN-05

- [ ] **Question:** Compare Patch baseline with SBOM/provenance. When would each change your design?

**Answer:** Patch baseline: determines approved updates but must be followed by regression qualification. SBOM/provenance: records packages/build source and supports vulnerability/rebuild decisions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MN-06

- [ ] **Question:** Compare SBOM/provenance with Signing/approval. When would each change your design?

**Answer:** SBOM/provenance: records packages/build source and supports vulnerability/rebuild decisions. Signing/approval: binds release process to an exact AMI/artifact rather than a name lookup. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MN-07

- [ ] **Configuration review:** **Question:** Compare Signing/approval with Distribution. When would each change your design?

**Answer:** Signing/approval: binds release process to an exact AMI/artifact rather than a name lookup. Distribution: account sharing, KMS keys and Region copies must preserve launch/decrypt permission. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MN-08

- [ ] **Question:** Compare Distribution with Canary instance/pool. When would each change your design?

**Answer:** Distribution: account sharing, KMS keys and Region copies must preserve launch/decrypt permission. Canary instance/pool: validates boot, SSM, agents, workload and performance before fleet refresh. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MN-09

- [ ] **Question:** Compare Canary instance/pool with Retirement. When would each change your design?

**Answer:** Canary instance/pool: validates boot, SSM, agents, workload and performance before fleet refresh. Retirement: owner/reference inventory and rollback window prevent deleting still-used images/snapshots. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MN-10

- [ ] **Configuration review:** **Question:** Compare Retirement with AMI. When would each change your design?

**Answer:** Retirement: owner/reference inventory and rollback window prevent deleting still-used images/snapshots. AMI: boot image metadata and snapshots define instance root and launch compatibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around AMI; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-images --owners self` plus recent events/changes, then correlate the service-specific SLI. boot image metadata and snapshots define instance root and launch compatibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MP-02

- [ ] **Question:** Production is degraded around Golden image; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws imagebuilder list-image-pipelines` plus recent events/changes, then correlate the service-specific SLI. centrally hardened/tested base reduces bootstrap drift and replacement time. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Image Builder pipeline; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws imagebuilder start-image-pipeline-execution --image-pipeline-arn ARN` plus recent events/changes, then correlate the service-specific SLI. recipes/components/infrastructure/distribution automate build/test/copy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MP-04

- [ ] **Question:** Production is degraded around Packer; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 copy-image --source-region REGION --source-image-id AMI --name NAME` plus recent events/changes, then correlate the service-specific SLI. vendor-neutral image build tool whose builders/provisioners need reproducibility and secret controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Patch baseline; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-images --owners self` plus recent events/changes, then correlate the service-specific SLI. determines approved updates but must be followed by regression qualification. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MP-06

- [ ] **Question:** Production is degraded around SBOM/provenance; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws imagebuilder list-image-pipelines` plus recent events/changes, then correlate the service-specific SLI. records packages/build source and supports vulnerability/rebuild decisions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Signing/approval; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws imagebuilder start-image-pipeline-execution --image-pipeline-arn ARN` plus recent events/changes, then correlate the service-specific SLI. binds release process to an exact AMI/artifact rather than a name lookup. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MP-08

- [ ] **Question:** Production is degraded around Distribution; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 copy-image --source-region REGION --source-image-id AMI --name NAME` plus recent events/changes, then correlate the service-specific SLI. account sharing, KMS keys and Region copies must preserve launch/decrypt permission. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Canary instance/pool; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-images --owners self` plus recent events/changes, then correlate the service-specific SLI. validates boot, SSM, agents, workload and performance before fleet refresh. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-MP-10

- [ ] **Question:** Production is degraded around Retirement; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws imagebuilder list-image-pipelines` plus recent events/changes, then correlate the service-specific SLI. owner/reference inventory and rollback window prevent deleting still-used images/snapshots. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SN-01

- [ ] **Question:** Design a production AMIs, Image Builder and golden images capability where AMI, Packer and Signing/approval are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: boot image metadata and snapshots define instance root and launch compatibility. vendor-neutral image build tool whose builders/provisioners need reproducibility and secret controls. binds release process to an exact AMI/artifact rather than a name lookup. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AMIs, Image Builder and golden images capability where Golden image, Patch baseline and Distribution are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: centrally hardened/tested base reduces bootstrap drift and replacement time. determines approved updates but must be followed by regression qualification. account sharing, KMS keys and Region copies must preserve launch/decrypt permission. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SN-03

- [ ] **Question:** Design a production AMIs, Image Builder and golden images capability where Image Builder pipeline, SBOM/provenance and Canary instance/pool are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: recipes/components/infrastructure/distribution automate build/test/copy. records packages/build source and supports vulnerability/rebuild decisions. validates boot, SSM, agents, workload and performance before fleet refresh. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AMIs, Image Builder and golden images capability where Packer, Signing/approval and Retirement are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: vendor-neutral image build tool whose builders/provisioners need reproducibility and secret controls. binds release process to an exact AMI/artifact rather than a name lookup. owner/reference inventory and rollback window prevent deleting still-used images/snapshots. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SN-05

- [ ] **Question:** Design a production AMIs, Image Builder and golden images capability where Patch baseline, Distribution and AMI are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: determines approved updates but must be followed by regression qualification. account sharing, KMS keys and Region copies must preserve launch/decrypt permission. boot image metadata and snapshots define instance root and launch compatibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AMIs, Image Builder and golden images capability where SBOM/provenance, Canary instance/pool and Golden image are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: records packages/build source and supports vulnerability/rebuild decisions. validates boot, SSM, agents, workload and performance before fleet refresh. centrally hardened/tested base reduces bootstrap drift and replacement time. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SN-07

- [ ] **Question:** Design a production AMIs, Image Builder and golden images capability where Signing/approval, Retirement and Image Builder pipeline are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: binds release process to an exact AMI/artifact rather than a name lookup. owner/reference inventory and rollback window prevent deleting still-used images/snapshots. recipes/components/infrastructure/distribution automate build/test/copy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AMIs, Image Builder and golden images capability where Distribution, AMI and Packer are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: account sharing, KMS keys and Region copies must preserve launch/decrypt permission. boot image metadata and snapshots define instance root and launch compatibility. vendor-neutral image build tool whose builders/provisioners need reproducibility and secret controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SN-09

- [ ] **Question:** Design a production AMIs, Image Builder and golden images capability where Canary instance/pool, Golden image and Patch baseline are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: validates boot, SSM, agents, workload and performance before fleet refresh. centrally hardened/tested base reduces bootstrap drift and replacement time. determines approved updates but must be followed by regression qualification. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AMIs, Image Builder and golden images capability where Retirement, Image Builder pipeline and SBOM/provenance are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: owner/reference inventory and rollback window prevent deleting still-used images/snapshots. recipes/components/infrastructure/distribution automate build/test/copy. records packages/build source and supports vulnerability/rebuild decisions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AMI. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-images --owners self` as one read-only checkpoint, not the whole diagnosis. boot image metadata and snapshots define instance root and launch compatibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Golden image. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws imagebuilder list-image-pipelines` as one read-only checkpoint, not the whole diagnosis. centrally hardened/tested base reduces bootstrap drift and replacement time. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Image Builder pipeline. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws imagebuilder start-image-pipeline-execution --image-pipeline-arn ARN` as one read-only checkpoint, not the whole diagnosis. recipes/components/infrastructure/distribution automate build/test/copy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Packer. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 copy-image --source-region REGION --source-image-id AMI --name NAME` as one read-only checkpoint, not the whole diagnosis. vendor-neutral image build tool whose builders/provisioners need reproducibility and secret controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Patch baseline. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-images --owners self` as one read-only checkpoint, not the whole diagnosis. determines approved updates but must be followed by regression qualification. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SBOM/provenance. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws imagebuilder list-image-pipelines` as one read-only checkpoint, not the whole diagnosis. records packages/build source and supports vulnerability/rebuild decisions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Signing/approval. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws imagebuilder start-image-pipeline-execution --image-pipeline-arn ARN` as one read-only checkpoint, not the whole diagnosis. binds release process to an exact AMI/artifact rather than a name lookup. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Distribution. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 copy-image --source-region REGION --source-image-id AMI --name NAME` as one read-only checkpoint, not the whole diagnosis. account sharing, KMS keys and Region copies must preserve launch/decrypt permission. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Canary instance/pool. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-images --owners self` as one read-only checkpoint, not the whole diagnosis. validates boot, SSM, agents, workload and performance before fleet refresh. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMIS-IMAGE-BUILDER-AND-GOLDEN-IMAGES-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retirement. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws imagebuilder list-image-pipelines` as one read-only checkpoint, not the whole diagnosis. owner/reference inventory and rollback window prevent deleting still-used images/snapshots. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
