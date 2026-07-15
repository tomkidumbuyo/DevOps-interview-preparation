# AWS CDK — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-CDK-JN-01

- [ ] **Question:** What is App/stack/construct tree, and why does it matter in AWS CDK?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** code composes logical resources and ownership hierarchy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CDK-JN-02

- [ ] **Question:** What is L1 construct, and why does it matter in AWS CDK?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** direct generated CloudFormation resource mapping. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CDK-JN-03

- [ ] **Question:** What is L2/L3 construct, and why does it matter in AWS CDK?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** higher-level intent with defaults and multiple resources. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CDK-JN-04

- [ ] **Question:** What is Synthesis, and why does it matter in AWS CDK?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** evaluates code/context into CloudFormation templates and assets. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CDK-JN-05

- [ ] **Question:** What is Bootstrap, and why does it matter in AWS CDK?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** account/Region roles, buckets and repositories are privileged deployment infrastructure. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CDK-JN-06

- [ ] **Question:** What is Asset publishing, and why does it matter in AWS CDK?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** file/container assets are hashed/uploaded and need provenance/access/lifecycle. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CDK-JN-07

- [ ] **Question:** What is Context lookup, and why does it matter in AWS CDK?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** cached environment facts can become stale/non-reproducible if unmanaged. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CDK-JN-08

- [ ] **Code:** **Question:** What does `cdk doctor` help you verify for AWS CDK?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: overrides low-level property when abstraction lacks it, increasing coupling.

### AWS-CDK-JN-09

- [ ] **Code:** **Question:** What does `cdk bootstrap aws://ACCOUNT/REGION` help you verify for AWS CDK?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: validates synthesized resources/properties while integration tests prove behavior.

### AWS-CDK-JN-10

- [ ] **Code:** **Question:** What does `cdk deploy STACK --require-approval broadening` help you verify for AWS CDK?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: construct path changes can replace resources unless identity is preserved.

## Junior — procedural and command questions

### AWS-CDK-JP-01

- [ ] **Code:** **Question:** A basic App/stack/construct tree check fails. What would you do first using the CLI?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk synth` and capture exact status/reason/request ID. code composes logical resources and ownership hierarchy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CDK-JP-02

- [ ] **Question:** A basic L1 construct check fails. What would you do first?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk diff` and capture exact status/reason/request ID. direct generated CloudFormation resource mapping. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CDK-JP-03

- [ ] **Question:** A basic L2/L3 construct check fails. What would you do first?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk doctor` and capture exact status/reason/request ID. higher-level intent with defaults and multiple resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CDK-JP-04

- [ ] **Code:** **Question:** A basic Synthesis check fails. What would you do first using the CLI?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk bootstrap aws://ACCOUNT/REGION` and capture exact status/reason/request ID. evaluates code/context into CloudFormation templates and assets. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CDK-JP-05

- [ ] **Question:** A basic Bootstrap check fails. What would you do first?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk deploy STACK --require-approval broadening` and capture exact status/reason/request ID. account/Region roles, buckets and repositories are privileged deployment infrastructure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CDK-JP-06

- [ ] **Question:** A basic Asset publishing check fails. What would you do first?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk synth` and capture exact status/reason/request ID. file/container assets are hashed/uploaded and need provenance/access/lifecycle. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CDK-JP-07

- [ ] **Code:** **Question:** A basic Context lookup check fails. What would you do first using the CLI?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk diff` and capture exact status/reason/request ID. cached environment facts can become stale/non-reproducible if unmanaged. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CDK-JP-08

- [ ] **Question:** A basic Escape hatch check fails. What would you do first?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk doctor` and capture exact status/reason/request ID. overrides low-level property when abstraction lacks it, increasing coupling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CDK-JP-09

- [ ] **Question:** A basic Assertion test check fails. What would you do first?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk bootstrap aws://ACCOUNT/REGION` and capture exact status/reason/request ID. validates synthesized resources/properties while integration tests prove behavior. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CDK-JP-10

- [ ] **Code:** **Question:** A basic Logical ID/refactor check fails. What would you do first using the CLI?
> **Covered in:** [AWS CDK — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `cdk deploy STACK --require-approval broadening` and capture exact status/reason/request ID. construct path changes can replace resources unless identity is preserved. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-CDK-MN-01

- [ ] **Question:** Compare App/stack/construct tree with L1 construct. When would each change your design?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** App/stack/construct tree: code composes logical resources and ownership hierarchy. L1 construct: direct generated CloudFormation resource mapping. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CDK-MN-02

- [ ] **Question:** Compare L1 construct with L2/L3 construct. When would each change your design?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** L1 construct: direct generated CloudFormation resource mapping. L2/L3 construct: higher-level intent with defaults and multiple resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CDK-MN-03

- [ ] **Question:** Compare L2/L3 construct with Synthesis. When would each change your design?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** L2/L3 construct: higher-level intent with defaults and multiple resources. Synthesis: evaluates code/context into CloudFormation templates and assets. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CDK-MN-04

- [ ] **Configuration review:** **Question:** Compare Synthesis with Bootstrap. When would each change your design?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Synthesis: evaluates code/context into CloudFormation templates and assets. Bootstrap: account/Region roles, buckets and repositories are privileged deployment infrastructure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CDK-MN-05

- [ ] **Question:** Compare Bootstrap with Asset publishing. When would each change your design?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Bootstrap: account/Region roles, buckets and repositories are privileged deployment infrastructure. Asset publishing: file/container assets are hashed/uploaded and need provenance/access/lifecycle. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CDK-MN-06

- [ ] **Question:** Compare Asset publishing with Context lookup. When would each change your design?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Asset publishing: file/container assets are hashed/uploaded and need provenance/access/lifecycle. Context lookup: cached environment facts can become stale/non-reproducible if unmanaged. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CDK-MN-07

- [ ] **Configuration review:** **Question:** Compare Context lookup with Escape hatch. When would each change your design?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Context lookup: cached environment facts can become stale/non-reproducible if unmanaged. Escape hatch: overrides low-level property when abstraction lacks it, increasing coupling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CDK-MN-08

- [ ] **Question:** Compare Escape hatch with Assertion test. When would each change your design?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Escape hatch: overrides low-level property when abstraction lacks it, increasing coupling. Assertion test: validates synthesized resources/properties while integration tests prove behavior. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CDK-MN-09

- [ ] **Question:** Compare Assertion test with Logical ID/refactor. When would each change your design?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Assertion test: validates synthesized resources/properties while integration tests prove behavior. Logical ID/refactor: construct path changes can replace resources unless identity is preserved. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CDK-MN-10

- [ ] **Configuration review:** **Question:** Compare Logical ID/refactor with App/stack/construct tree. When would each change your design?
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Logical ID/refactor: construct path changes can replace resources unless identity is preserved. App/stack/construct tree: code composes logical resources and ownership hierarchy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-CDK-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around App/stack/construct tree; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk synth` plus recent events/changes, then correlate the service-specific SLI. code composes logical resources and ownership hierarchy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CDK-MP-02

- [ ] **Question:** Production is degraded around L1 construct; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk diff` plus recent events/changes, then correlate the service-specific SLI. direct generated CloudFormation resource mapping. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CDK-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around L2/L3 construct; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk doctor` plus recent events/changes, then correlate the service-specific SLI. higher-level intent with defaults and multiple resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CDK-MP-04

- [ ] **Question:** Production is degraded around Synthesis; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk bootstrap aws://ACCOUNT/REGION` plus recent events/changes, then correlate the service-specific SLI. evaluates code/context into CloudFormation templates and assets. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CDK-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Bootstrap; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk deploy STACK --require-approval broadening` plus recent events/changes, then correlate the service-specific SLI. account/Region roles, buckets and repositories are privileged deployment infrastructure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CDK-MP-06

- [ ] **Question:** Production is degraded around Asset publishing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk synth` plus recent events/changes, then correlate the service-specific SLI. file/container assets are hashed/uploaded and need provenance/access/lifecycle. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CDK-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Context lookup; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk diff` plus recent events/changes, then correlate the service-specific SLI. cached environment facts can become stale/non-reproducible if unmanaged. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CDK-MP-08

- [ ] **Question:** Production is degraded around Escape hatch; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk doctor` plus recent events/changes, then correlate the service-specific SLI. overrides low-level property when abstraction lacks it, increasing coupling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CDK-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Assertion test; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk bootstrap aws://ACCOUNT/REGION` plus recent events/changes, then correlate the service-specific SLI. validates synthesized resources/properties while integration tests prove behavior. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CDK-MP-10

- [ ] **Question:** Production is degraded around Logical ID/refactor; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `cdk deploy STACK --require-approval broadening` plus recent events/changes, then correlate the service-specific SLI. construct path changes can replace resources unless identity is preserved. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-CDK-SN-01

- [ ] **Question:** Design a production AWS CDK capability where App/stack/construct tree, Synthesis and Context lookup are first-class requirements.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: code composes logical resources and ownership hierarchy. evaluates code/context into CloudFormation templates and assets. cached environment facts can become stale/non-reproducible if unmanaged. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CDK-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CDK capability where L1 construct, Bootstrap and Escape hatch are first-class requirements.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: direct generated CloudFormation resource mapping. account/Region roles, buckets and repositories are privileged deployment infrastructure. overrides low-level property when abstraction lacks it, increasing coupling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CDK-SN-03

- [ ] **Question:** Design a production AWS CDK capability where L2/L3 construct, Asset publishing and Assertion test are first-class requirements.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: higher-level intent with defaults and multiple resources. file/container assets are hashed/uploaded and need provenance/access/lifecycle. validates synthesized resources/properties while integration tests prove behavior. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CDK-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CDK capability where Synthesis, Context lookup and Logical ID/refactor are first-class requirements.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: evaluates code/context into CloudFormation templates and assets. cached environment facts can become stale/non-reproducible if unmanaged. construct path changes can replace resources unless identity is preserved. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CDK-SN-05

- [ ] **Question:** Design a production AWS CDK capability where Bootstrap, Escape hatch and App/stack/construct tree are first-class requirements.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: account/Region roles, buckets and repositories are privileged deployment infrastructure. overrides low-level property when abstraction lacks it, increasing coupling. code composes logical resources and ownership hierarchy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CDK-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CDK capability where Asset publishing, Assertion test and L1 construct are first-class requirements.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: file/container assets are hashed/uploaded and need provenance/access/lifecycle. validates synthesized resources/properties while integration tests prove behavior. direct generated CloudFormation resource mapping. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CDK-SN-07

- [ ] **Question:** Design a production AWS CDK capability where Context lookup, Logical ID/refactor and L2/L3 construct are first-class requirements.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cached environment facts can become stale/non-reproducible if unmanaged. construct path changes can replace resources unless identity is preserved. higher-level intent with defaults and multiple resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CDK-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CDK capability where Escape hatch, App/stack/construct tree and Synthesis are first-class requirements.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: overrides low-level property when abstraction lacks it, increasing coupling. code composes logical resources and ownership hierarchy. evaluates code/context into CloudFormation templates and assets. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CDK-SN-09

- [ ] **Question:** Design a production AWS CDK capability where Assertion test, L1 construct and Bootstrap are first-class requirements.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: validates synthesized resources/properties while integration tests prove behavior. direct generated CloudFormation resource mapping. account/Region roles, buckets and repositories are privileged deployment infrastructure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CDK-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CDK capability where Logical ID/refactor, L2/L3 construct and Asset publishing are first-class requirements.
> **Covered in:** [AWS CDK — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: construct path changes can replace resources unless identity is preserved. higher-level intent with defaults and multiple resources. file/container assets are hashed/uploaded and need provenance/access/lifecycle. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-CDK-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving App/stack/construct tree. How do you lead it end to end?
> **Covered in:** [AWS CDK — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk synth` as one read-only checkpoint, not the whole diagnosis. code composes logical resources and ownership hierarchy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CDK-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving L1 construct. How do you lead it end to end?
> **Covered in:** [AWS CDK — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk diff` as one read-only checkpoint, not the whole diagnosis. direct generated CloudFormation resource mapping. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CDK-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving L2/L3 construct. How do you lead it end to end?
> **Covered in:** [AWS CDK — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk doctor` as one read-only checkpoint, not the whole diagnosis. higher-level intent with defaults and multiple resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CDK-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Synthesis. How do you lead it end to end?
> **Covered in:** [AWS CDK — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk bootstrap aws://ACCOUNT/REGION` as one read-only checkpoint, not the whole diagnosis. evaluates code/context into CloudFormation templates and assets. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CDK-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Bootstrap. How do you lead it end to end?
> **Covered in:** [AWS CDK — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk deploy STACK --require-approval broadening` as one read-only checkpoint, not the whole diagnosis. account/Region roles, buckets and repositories are privileged deployment infrastructure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CDK-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Asset publishing. How do you lead it end to end?
> **Covered in:** [AWS CDK — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk synth` as one read-only checkpoint, not the whole diagnosis. file/container assets are hashed/uploaded and need provenance/access/lifecycle. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CDK-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Context lookup. How do you lead it end to end?
> **Covered in:** [AWS CDK — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk diff` as one read-only checkpoint, not the whole diagnosis. cached environment facts can become stale/non-reproducible if unmanaged. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CDK-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Escape hatch. How do you lead it end to end?
> **Covered in:** [AWS CDK — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk doctor` as one read-only checkpoint, not the whole diagnosis. overrides low-level property when abstraction lacks it, increasing coupling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CDK-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Assertion test. How do you lead it end to end?
> **Covered in:** [AWS CDK — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk bootstrap aws://ACCOUNT/REGION` as one read-only checkpoint, not the whole diagnosis. validates synthesized resources/properties while integration tests prove behavior. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CDK-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Logical ID/refactor. How do you lead it end to end?
> **Covered in:** [AWS CDK — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `cdk deploy STACK --require-approval broadening` as one read-only checkpoint, not the whole diagnosis. construct path changes can replace resources unless identity is preserved. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AWS CloudFormation](../01-cloudformation/README.md) · [Study note](README.md) · [Next: CodeBuild, CodePipeline and CodeDeploy →](../03-code-services/README.md)

<!-- reading-navigation:end -->
