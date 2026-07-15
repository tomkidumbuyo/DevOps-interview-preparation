# GuardDuty, Security Hub, Inspector, Macie and Detective — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JN-01

- [ ] **Question:** What is GuardDuty, and why does it matter in GuardDuty, Security Hub, Inspector, Macie and Detective?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** analyzes supported logs/signals to emit contextual threat findings. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JN-02

- [ ] **Question:** What is Security Hub, and why does it matter in GuardDuty, Security Hub, Inspector, Macie and Detective?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** aggregates/normalizes findings and control standards across accounts/Regions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JN-03

- [ ] **Question:** What is Inspector, and why does it matter in GuardDuty, Security Hub, Inspector, Macie and Detective?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** continuously assesses supported compute/container/function packages and exposure. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JN-04

- [ ] **Question:** What is Macie, and why does it matter in GuardDuty, Security Hub, Inspector, Macie and Detective?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** discovers/classifies sensitive S3 data and bucket access risk. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JN-05

- [ ] **Question:** What is Detective, and why does it matter in GuardDuty, Security Hub, Inspector, Macie and Detective?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** correlates activity/entities to support investigation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JN-06

- [ ] **Question:** What is Delegated administration, and why does it matter in GuardDuty, Security Hub, Inspector, Macie and Detective?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** central security account manages organization coverage without using management account. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JN-07

- [ ] **Question:** What is Finding severity, and why does it matter in GuardDuty, Security Hub, Inspector, Macie and Detective?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** vendor score must be combined with asset exposure, data and exploitability. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JN-08

- [ ] **Code:** **Question:** What does `aws macie2 get-macie-session` help you verify for GuardDuty, Security Hub, Inspector, Macie and Detective?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: tuned archival/suppression needs owner/reason/expiry to avoid hiding new risk.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JN-09

- [ ] **Code:** **Question:** What does `aws guardduty list-detectors` help you verify for GuardDuty, Security Hub, Inspector, Macie and Detective?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: EventBridge/Security Hub actions can quarantine or ticket with rollback/safety controls.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JN-10

- [ ] **Code:** **Question:** What does `aws securityhub get-findings --filters file://filters.json` help you verify for GuardDuty, Security Hub, Inspector, Macie and Detective?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: inventory accounts/Regions/services and detect disabled sensors or log gaps.

## Junior — procedural and command questions

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JP-01

- [ ] **Code:** **Question:** A basic GuardDuty check fails. What would you do first using the CLI?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws guardduty list-detectors` and capture exact status/reason/request ID. analyzes supported logs/signals to emit contextual threat findings. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JP-02

- [ ] **Question:** A basic Security Hub check fails. What would you do first?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Security model](README.md#security-model)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws securityhub get-findings --filters file://filters.json` and capture exact status/reason/request ID. aggregates/normalizes findings and control standards across accounts/Regions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JP-03

- [ ] **Question:** A basic Inspector check fails. What would you do first?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws inspector2 list-findings --filter-criteria file://criteria.json` and capture exact status/reason/request ID. continuously assesses supported compute/container/function packages and exposure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JP-04

- [ ] **Code:** **Question:** A basic Macie check fails. What would you do first using the CLI?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws macie2 get-macie-session` and capture exact status/reason/request ID. discovers/classifies sensitive S3 data and bucket access risk. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JP-05

- [ ] **Question:** A basic Detective check fails. What would you do first?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws guardduty list-detectors` and capture exact status/reason/request ID. correlates activity/entities to support investigation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JP-06

- [ ] **Question:** A basic Delegated administration check fails. What would you do first?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws securityhub get-findings --filters file://filters.json` and capture exact status/reason/request ID. central security account manages organization coverage without using management account. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JP-07

- [ ] **Code:** **Question:** A basic Finding severity check fails. What would you do first using the CLI?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws inspector2 list-findings --filter-criteria file://criteria.json` and capture exact status/reason/request ID. vendor score must be combined with asset exposure, data and exploitability. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JP-08

- [ ] **Question:** A basic Suppression check fails. What would you do first?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws macie2 get-macie-session` and capture exact status/reason/request ID. tuned archival/suppression needs owner/reason/expiry to avoid hiding new risk. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JP-09

- [ ] **Question:** A basic Automation check fails. What would you do first?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws guardduty list-detectors` and capture exact status/reason/request ID. EventBridge/Security Hub actions can quarantine or ticket with rollback/safety controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-JP-10

- [ ] **Code:** **Question:** A basic Coverage evidence check fails. What would you do first using the CLI?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws securityhub get-findings --filters file://filters.json` and capture exact status/reason/request ID. inventory accounts/Regions/services and detect disabled sensors or log gaps. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MN-01

- [ ] **Question:** Compare GuardDuty with Security Hub. When would each change your design?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** GuardDuty: analyzes supported logs/signals to emit contextual threat findings. Security Hub: aggregates/normalizes findings and control standards across accounts/Regions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MN-02

- [ ] **Question:** Compare Security Hub with Inspector. When would each change your design?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** Security Hub: aggregates/normalizes findings and control standards across accounts/Regions. Inspector: continuously assesses supported compute/container/function packages and exposure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MN-03

- [ ] **Question:** Compare Inspector with Macie. When would each change your design?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** Inspector: continuously assesses supported compute/container/function packages and exposure. Macie: discovers/classifies sensitive S3 data and bucket access risk. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MN-04

- [ ] **Configuration review:** **Question:** Compare Macie with Detective. When would each change your design?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** Macie: discovers/classifies sensitive S3 data and bucket access risk. Detective: correlates activity/entities to support investigation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MN-05

- [ ] **Question:** Compare Detective with Delegated administration. When would each change your design?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Detective: correlates activity/entities to support investigation. Delegated administration: central security account manages organization coverage without using management account. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MN-06

- [ ] **Question:** Compare Delegated administration with Finding severity. When would each change your design?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Delegated administration: central security account manages organization coverage without using management account. Finding severity: vendor score must be combined with asset exposure, data and exploitability. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MN-07

- [ ] **Configuration review:** **Question:** Compare Finding severity with Suppression. When would each change your design?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Finding severity: vendor score must be combined with asset exposure, data and exploitability. Suppression: tuned archival/suppression needs owner/reason/expiry to avoid hiding new risk. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MN-08

- [ ] **Question:** Compare Suppression with Automation. When would each change your design?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Suppression: tuned archival/suppression needs owner/reason/expiry to avoid hiding new risk. Automation: EventBridge/Security Hub actions can quarantine or ticket with rollback/safety controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MN-09

- [ ] **Question:** Compare Automation with Coverage evidence. When would each change your design?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Automation: EventBridge/Security Hub actions can quarantine or ticket with rollback/safety controls. Coverage evidence: inventory accounts/Regions/services and detect disabled sensors or log gaps. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MN-10

- [ ] **Configuration review:** **Question:** Compare Coverage evidence with GuardDuty. When would each change your design?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Coverage evidence: inventory accounts/Regions/services and detect disabled sensors or log gaps. GuardDuty: analyzes supported logs/signals to emit contextual threat findings. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around GuardDuty; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws guardduty list-detectors` plus recent events/changes, then correlate the service-specific SLI. analyzes supported logs/signals to emit contextual threat findings. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MP-02

- [ ] **Question:** Production is degraded around Security Hub; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws securityhub get-findings --filters file://filters.json` plus recent events/changes, then correlate the service-specific SLI. aggregates/normalizes findings and control standards across accounts/Regions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Inspector; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws inspector2 list-findings --filter-criteria file://criteria.json` plus recent events/changes, then correlate the service-specific SLI. continuously assesses supported compute/container/function packages and exposure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MP-04

- [ ] **Question:** Production is degraded around Macie; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws macie2 get-macie-session` plus recent events/changes, then correlate the service-specific SLI. discovers/classifies sensitive S3 data and bucket access risk. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Detective; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws guardduty list-detectors` plus recent events/changes, then correlate the service-specific SLI. correlates activity/entities to support investigation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MP-06

- [ ] **Question:** Production is degraded around Delegated administration; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws securityhub get-findings --filters file://filters.json` plus recent events/changes, then correlate the service-specific SLI. central security account manages organization coverage without using management account. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Finding severity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws inspector2 list-findings --filter-criteria file://criteria.json` plus recent events/changes, then correlate the service-specific SLI. vendor score must be combined with asset exposure, data and exploitability. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MP-08

- [ ] **Question:** Production is degraded around Suppression; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws macie2 get-macie-session` plus recent events/changes, then correlate the service-specific SLI. tuned archival/suppression needs owner/reason/expiry to avoid hiding new risk. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Automation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws guardduty list-detectors` plus recent events/changes, then correlate the service-specific SLI. EventBridge/Security Hub actions can quarantine or ticket with rollback/safety controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-MP-10

- [ ] **Question:** Production is degraded around Coverage evidence; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws securityhub get-findings --filters file://filters.json` plus recent events/changes, then correlate the service-specific SLI. inventory accounts/Regions/services and detect disabled sensors or log gaps. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SN-01

- [ ] **Question:** Design a production GuardDuty, Security Hub, Inspector, Macie and Detective capability where GuardDuty, Macie and Finding severity are first-class requirements.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: analyzes supported logs/signals to emit contextual threat findings. discovers/classifies sensitive S3 data and bucket access risk. vendor score must be combined with asset exposure, data and exploitability. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production GuardDuty, Security Hub, Inspector, Macie and Detective capability where Security Hub, Detective and Suppression are first-class requirements.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: aggregates/normalizes findings and control standards across accounts/Regions. correlates activity/entities to support investigation. tuned archival/suppression needs owner/reason/expiry to avoid hiding new risk. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SN-03

- [ ] **Question:** Design a production GuardDuty, Security Hub, Inspector, Macie and Detective capability where Inspector, Delegated administration and Automation are first-class requirements.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: continuously assesses supported compute/container/function packages and exposure. central security account manages organization coverage without using management account. EventBridge/Security Hub actions can quarantine or ticket with rollback/safety controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production GuardDuty, Security Hub, Inspector, Macie and Detective capability where Macie, Finding severity and Coverage evidence are first-class requirements.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: discovers/classifies sensitive S3 data and bucket access risk. vendor score must be combined with asset exposure, data and exploitability. inventory accounts/Regions/services and detect disabled sensors or log gaps. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SN-05

- [ ] **Question:** Design a production GuardDuty, Security Hub, Inspector, Macie and Detective capability where Detective, Suppression and GuardDuty are first-class requirements.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: correlates activity/entities to support investigation. tuned archival/suppression needs owner/reason/expiry to avoid hiding new risk. analyzes supported logs/signals to emit contextual threat findings. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production GuardDuty, Security Hub, Inspector, Macie and Detective capability where Delegated administration, Automation and Security Hub are first-class requirements.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: central security account manages organization coverage without using management account. EventBridge/Security Hub actions can quarantine or ticket with rollback/safety controls. aggregates/normalizes findings and control standards across accounts/Regions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SN-07

- [ ] **Question:** Design a production GuardDuty, Security Hub, Inspector, Macie and Detective capability where Finding severity, Coverage evidence and Inspector are first-class requirements.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: vendor score must be combined with asset exposure, data and exploitability. inventory accounts/Regions/services and detect disabled sensors or log gaps. continuously assesses supported compute/container/function packages and exposure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production GuardDuty, Security Hub, Inspector, Macie and Detective capability where Suppression, GuardDuty and Macie are first-class requirements.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tuned archival/suppression needs owner/reason/expiry to avoid hiding new risk. analyzes supported logs/signals to emit contextual threat findings. discovers/classifies sensitive S3 data and bucket access risk. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SN-09

- [ ] **Question:** Design a production GuardDuty, Security Hub, Inspector, Macie and Detective capability where Automation, Security Hub and Detective are first-class requirements.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: EventBridge/Security Hub actions can quarantine or ticket with rollback/safety controls. aggregates/normalizes findings and control standards across accounts/Regions. correlates activity/entities to support investigation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production GuardDuty, Security Hub, Inspector, Macie and Detective capability where Coverage evidence, Inspector and Delegated administration are first-class requirements.
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: inventory accounts/Regions/services and detect disabled sensors or log gaps. continuously assesses supported compute/container/function packages and exposure. central security account manages organization coverage without using management account. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GuardDuty. How do you lead it end to end?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws guardduty list-detectors` as one read-only checkpoint, not the whole diagnosis. analyzes supported logs/signals to emit contextual threat findings. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Security Hub. How do you lead it end to end?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws securityhub get-findings --filters file://filters.json` as one read-only checkpoint, not the whole diagnosis. aggregates/normalizes findings and control standards across accounts/Regions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Inspector. How do you lead it end to end?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws inspector2 list-findings --filter-criteria file://criteria.json` as one read-only checkpoint, not the whole diagnosis. continuously assesses supported compute/container/function packages and exposure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Macie. How do you lead it end to end?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws macie2 get-macie-session` as one read-only checkpoint, not the whole diagnosis. discovers/classifies sensitive S3 data and bucket access risk. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Detective. How do you lead it end to end?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws guardduty list-detectors` as one read-only checkpoint, not the whole diagnosis. correlates activity/entities to support investigation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Delegated administration. How do you lead it end to end?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws securityhub get-findings --filters file://filters.json` as one read-only checkpoint, not the whole diagnosis. central security account manages organization coverage without using management account. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Finding severity. How do you lead it end to end?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws inspector2 list-findings --filter-criteria file://criteria.json` as one read-only checkpoint, not the whole diagnosis. vendor score must be combined with asset exposure, data and exploitability. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Suppression. How do you lead it end to end?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws macie2 get-macie-session` as one read-only checkpoint, not the whole diagnosis. tuned archival/suppression needs owner/reason/expiry to avoid hiding new risk. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Automation. How do you lead it end to end?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws guardduty list-detectors` as one read-only checkpoint, not the whole diagnosis. EventBridge/Security Hub actions can quarantine or ticket with rollback/safety controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GUARDDUTY-SECURITY-HUB-INSPECTOR-MACIE-AND-DETEC-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Coverage evidence. How do you lead it end to end?
> **Covered in:** [GuardDuty, Security Hub, Inspector, Macie and Detective — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws securityhub get-findings --filters file://filters.json` as one read-only checkpoint, not the whole diagnosis. inventory accounts/Regions/services and detect disabled sensors or log gaps. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: ACM, AWS WAF and Shield](../03-acm-waf-shield/README.md) · [Study note](README.md) · [Next: Amazon CloudWatch and X-Ray →](../05-cloudwatch-xray/README.md)

<!-- reading-navigation:end -->
