# ACM, AWS WAF and Shield — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### ACM-AWS-WAF-AND-SHIELD-JN-01

- [ ] **Question:** What is ACM certificate, and why does it matter in ACM, AWS WAF and Shield?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** managed public/private/imported certificate with supported service integration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ACM-AWS-WAF-AND-SHIELD-JN-02

- [ ] **Question:** What is DNS validation, and why does it matter in ACM, AWS WAF and Shield?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** persistent validation record enables managed renewal when service conditions hold. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ACM-AWS-WAF-AND-SHIELD-JN-03

- [ ] **Question:** What is Imported certificate, and why does it matter in ACM, AWS WAF and Shield?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** customer owns renewal/reimport and expiry alert. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ACM-AWS-WAF-AND-SHIELD-JN-04

- [ ] **Question:** What is TLS policy, and why does it matter in ACM, AWS WAF and Shield?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** protocol/cipher compatibility balances client support and security. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ACM-AWS-WAF-AND-SHIELD-JN-05

- [ ] **Question:** What is WAF web ACL, and why does it matter in ACM, AWS WAF and Shield?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ordered managed/custom/rate rules return allow/block/count/CAPTCHA/challenge actions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ACM-AWS-WAF-AND-SHIELD-JN-06

- [ ] **Question:** What is Count mode, and why does it matter in ACM, AWS WAF and Shield?
> **Covered in:** [ACM, AWS WAF and Shield — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** observes a new rule before enforcement to detect false positives. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ACM-AWS-WAF-AND-SHIELD-JN-07

- [ ] **Question:** What is Rate-based rule, and why does it matter in ACM, AWS WAF and Shield?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** limits aggregate keys but is not a complete application tenant quota. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ACM-AWS-WAF-AND-SHIELD-JN-08

- [ ] **Code:** **Question:** What does `aws wafv2 get-sampled-requests --web-acl-arn ARN --rule-metric-name METRIC --scope REGIONAL --time-window file://window.json --max-items 100` help you verify for ACM, AWS WAF and Shield?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: updates can change behavior and require staged rollout.

### ACM-AWS-WAF-AND-SHIELD-JN-09

- [ ] **Code:** **Question:** What does `aws acm list-certificates` help you verify for ACM, AWS WAF and Shield?
> **Covered in:** [ACM, AWS WAF and Shield — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: DDoS protection/support/cost protection differ by service/tier.

### ACM-AWS-WAF-AND-SHIELD-JN-10

- [ ] **Code:** **Question:** What does `aws acm describe-certificate --certificate-arn ARN` help you verify for ACM, AWS WAF and Shield?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: edge allowlist/auth/private origin prevents bypassing WAF/CDN controls.

## Junior — procedural and command questions

### ACM-AWS-WAF-AND-SHIELD-JP-01

- [ ] **Code:** **Question:** A basic ACM certificate check fails. What would you do first using the CLI?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws acm list-certificates` and capture exact status/reason/request ID. managed public/private/imported certificate with supported service integration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ACM-AWS-WAF-AND-SHIELD-JP-02

- [ ] **Question:** A basic DNS validation check fails. What would you do first?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws acm describe-certificate --certificate-arn ARN` and capture exact status/reason/request ID. persistent validation record enables managed renewal when service conditions hold. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ACM-AWS-WAF-AND-SHIELD-JP-03

- [ ] **Question:** A basic Imported certificate check fails. What would you do first?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws wafv2 list-web-acls --scope REGIONAL --region REGION` and capture exact status/reason/request ID. customer owns renewal/reimport and expiry alert. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ACM-AWS-WAF-AND-SHIELD-JP-04

- [ ] **Code:** **Question:** A basic TLS policy check fails. What would you do first using the CLI?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws wafv2 get-sampled-requests --web-acl-arn ARN --rule-metric-name METRIC --scope REGIONAL --time-window file://window.json --max-items 100` and capture exact status/reason/request ID. protocol/cipher compatibility balances client support and security. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ACM-AWS-WAF-AND-SHIELD-JP-05

- [ ] **Question:** A basic WAF web ACL check fails. What would you do first?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws acm list-certificates` and capture exact status/reason/request ID. ordered managed/custom/rate rules return allow/block/count/CAPTCHA/challenge actions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ACM-AWS-WAF-AND-SHIELD-JP-06

- [ ] **Question:** A basic Count mode check fails. What would you do first?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws acm describe-certificate --certificate-arn ARN` and capture exact status/reason/request ID. observes a new rule before enforcement to detect false positives. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ACM-AWS-WAF-AND-SHIELD-JP-07

- [ ] **Code:** **Question:** A basic Rate-based rule check fails. What would you do first using the CLI?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws wafv2 list-web-acls --scope REGIONAL --region REGION` and capture exact status/reason/request ID. limits aggregate keys but is not a complete application tenant quota. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ACM-AWS-WAF-AND-SHIELD-JP-08

- [ ] **Question:** A basic Managed rule version check fails. What would you do first?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws wafv2 get-sampled-requests --web-acl-arn ARN --rule-metric-name METRIC --scope REGIONAL --time-window file://window.json --max-items 100` and capture exact status/reason/request ID. updates can change behavior and require staged rollout. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ACM-AWS-WAF-AND-SHIELD-JP-09

- [ ] **Question:** A basic Shield Standard/Advanced check fails. What would you do first?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws acm list-certificates` and capture exact status/reason/request ID. DDoS protection/support/cost protection differ by service/tier. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ACM-AWS-WAF-AND-SHIELD-JP-10

- [ ] **Code:** **Question:** A basic Origin protection check fails. What would you do first using the CLI?
> **Covered in:** [ACM, AWS WAF and Shield — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws acm describe-certificate --certificate-arn ARN` and capture exact status/reason/request ID. edge allowlist/auth/private origin prevents bypassing WAF/CDN controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### ACM-AWS-WAF-AND-SHIELD-MN-01

- [ ] **Question:** Compare ACM certificate with DNS validation. When would each change your design?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ACM certificate: managed public/private/imported certificate with supported service integration. DNS validation: persistent validation record enables managed renewal when service conditions hold. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ACM-AWS-WAF-AND-SHIELD-MN-02

- [ ] **Question:** Compare DNS validation with Imported certificate. When would each change your design?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** DNS validation: persistent validation record enables managed renewal when service conditions hold. Imported certificate: customer owns renewal/reimport and expiry alert. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ACM-AWS-WAF-AND-SHIELD-MN-03

- [ ] **Question:** Compare Imported certificate with TLS policy. When would each change your design?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Imported certificate: customer owns renewal/reimport and expiry alert. TLS policy: protocol/cipher compatibility balances client support and security. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ACM-AWS-WAF-AND-SHIELD-MN-04

- [ ] **Configuration review:** **Question:** Compare TLS policy with WAF web ACL. When would each change your design?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** TLS policy: protocol/cipher compatibility balances client support and security. WAF web ACL: ordered managed/custom/rate rules return allow/block/count/CAPTCHA/challenge actions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ACM-AWS-WAF-AND-SHIELD-MN-05

- [ ] **Question:** Compare WAF web ACL with Count mode. When would each change your design?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** WAF web ACL: ordered managed/custom/rate rules return allow/block/count/CAPTCHA/challenge actions. Count mode: observes a new rule before enforcement to detect false positives. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ACM-AWS-WAF-AND-SHIELD-MN-06

- [ ] **Question:** Compare Count mode with Rate-based rule. When would each change your design?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Count mode: observes a new rule before enforcement to detect false positives. Rate-based rule: limits aggregate keys but is not a complete application tenant quota. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ACM-AWS-WAF-AND-SHIELD-MN-07

- [ ] **Configuration review:** **Question:** Compare Rate-based rule with Managed rule version. When would each change your design?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Rate-based rule: limits aggregate keys but is not a complete application tenant quota. Managed rule version: updates can change behavior and require staged rollout. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ACM-AWS-WAF-AND-SHIELD-MN-08

- [ ] **Question:** Compare Managed rule version with Shield Standard/Advanced. When would each change your design?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Managed rule version: updates can change behavior and require staged rollout. Shield Standard/Advanced: DDoS protection/support/cost protection differ by service/tier. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ACM-AWS-WAF-AND-SHIELD-MN-09

- [ ] **Question:** Compare Shield Standard/Advanced with Origin protection. When would each change your design?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Shield Standard/Advanced: DDoS protection/support/cost protection differ by service/tier. Origin protection: edge allowlist/auth/private origin prevents bypassing WAF/CDN controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ACM-AWS-WAF-AND-SHIELD-MN-10

- [ ] **Configuration review:** **Question:** Compare Origin protection with ACM certificate. When would each change your design?
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Origin protection: edge allowlist/auth/private origin prevents bypassing WAF/CDN controls. ACM certificate: managed public/private/imported certificate with supported service integration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### ACM-AWS-WAF-AND-SHIELD-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around ACM certificate; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws acm list-certificates` plus recent events/changes, then correlate the service-specific SLI. managed public/private/imported certificate with supported service integration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ACM-AWS-WAF-AND-SHIELD-MP-02

- [ ] **Question:** Production is degraded around DNS validation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws acm describe-certificate --certificate-arn ARN` plus recent events/changes, then correlate the service-specific SLI. persistent validation record enables managed renewal when service conditions hold. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ACM-AWS-WAF-AND-SHIELD-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Imported certificate; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws wafv2 list-web-acls --scope REGIONAL --region REGION` plus recent events/changes, then correlate the service-specific SLI. customer owns renewal/reimport and expiry alert. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ACM-AWS-WAF-AND-SHIELD-MP-04

- [ ] **Question:** Production is degraded around TLS policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws wafv2 get-sampled-requests --web-acl-arn ARN --rule-metric-name METRIC --scope REGIONAL --time-window file://window.json --max-items 100` plus recent events/changes, then correlate the service-specific SLI. protocol/cipher compatibility balances client support and security. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ACM-AWS-WAF-AND-SHIELD-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around WAF web ACL; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws acm list-certificates` plus recent events/changes, then correlate the service-specific SLI. ordered managed/custom/rate rules return allow/block/count/CAPTCHA/challenge actions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ACM-AWS-WAF-AND-SHIELD-MP-06

- [ ] **Question:** Production is degraded around Count mode; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws acm describe-certificate --certificate-arn ARN` plus recent events/changes, then correlate the service-specific SLI. observes a new rule before enforcement to detect false positives. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ACM-AWS-WAF-AND-SHIELD-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Rate-based rule; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws wafv2 list-web-acls --scope REGIONAL --region REGION` plus recent events/changes, then correlate the service-specific SLI. limits aggregate keys but is not a complete application tenant quota. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ACM-AWS-WAF-AND-SHIELD-MP-08

- [ ] **Question:** Production is degraded around Managed rule version; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws wafv2 get-sampled-requests --web-acl-arn ARN --rule-metric-name METRIC --scope REGIONAL --time-window file://window.json --max-items 100` plus recent events/changes, then correlate the service-specific SLI. updates can change behavior and require staged rollout. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ACM-AWS-WAF-AND-SHIELD-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Shield Standard/Advanced; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws acm list-certificates` plus recent events/changes, then correlate the service-specific SLI. DDoS protection/support/cost protection differ by service/tier. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ACM-AWS-WAF-AND-SHIELD-MP-10

- [ ] **Question:** Production is degraded around Origin protection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws acm describe-certificate --certificate-arn ARN` plus recent events/changes, then correlate the service-specific SLI. edge allowlist/auth/private origin prevents bypassing WAF/CDN controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### ACM-AWS-WAF-AND-SHIELD-SN-01

- [ ] **Question:** Design a production ACM, AWS WAF and Shield capability where ACM certificate, TLS policy and Rate-based rule are first-class requirements.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed public/private/imported certificate with supported service integration. protocol/cipher compatibility balances client support and security. limits aggregate keys but is not a complete application tenant quota. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ACM-AWS-WAF-AND-SHIELD-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production ACM, AWS WAF and Shield capability where DNS validation, WAF web ACL and Managed rule version are first-class requirements.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: persistent validation record enables managed renewal when service conditions hold. ordered managed/custom/rate rules return allow/block/count/CAPTCHA/challenge actions. updates can change behavior and require staged rollout. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ACM-AWS-WAF-AND-SHIELD-SN-03

- [ ] **Question:** Design a production ACM, AWS WAF and Shield capability where Imported certificate, Count mode and Shield Standard/Advanced are first-class requirements.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: customer owns renewal/reimport and expiry alert. observes a new rule before enforcement to detect false positives. DDoS protection/support/cost protection differ by service/tier. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ACM-AWS-WAF-AND-SHIELD-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production ACM, AWS WAF and Shield capability where TLS policy, Rate-based rule and Origin protection are first-class requirements.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: protocol/cipher compatibility balances client support and security. limits aggregate keys but is not a complete application tenant quota. edge allowlist/auth/private origin prevents bypassing WAF/CDN controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ACM-AWS-WAF-AND-SHIELD-SN-05

- [ ] **Question:** Design a production ACM, AWS WAF and Shield capability where WAF web ACL, Managed rule version and ACM certificate are first-class requirements.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ordered managed/custom/rate rules return allow/block/count/CAPTCHA/challenge actions. updates can change behavior and require staged rollout. managed public/private/imported certificate with supported service integration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ACM-AWS-WAF-AND-SHIELD-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production ACM, AWS WAF and Shield capability where Count mode, Shield Standard/Advanced and DNS validation are first-class requirements.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: observes a new rule before enforcement to detect false positives. DDoS protection/support/cost protection differ by service/tier. persistent validation record enables managed renewal when service conditions hold. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ACM-AWS-WAF-AND-SHIELD-SN-07

- [ ] **Question:** Design a production ACM, AWS WAF and Shield capability where Rate-based rule, Origin protection and Imported certificate are first-class requirements.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: limits aggregate keys but is not a complete application tenant quota. edge allowlist/auth/private origin prevents bypassing WAF/CDN controls. customer owns renewal/reimport and expiry alert. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ACM-AWS-WAF-AND-SHIELD-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production ACM, AWS WAF and Shield capability where Managed rule version, ACM certificate and TLS policy are first-class requirements.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: updates can change behavior and require staged rollout. managed public/private/imported certificate with supported service integration. protocol/cipher compatibility balances client support and security. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ACM-AWS-WAF-AND-SHIELD-SN-09

- [ ] **Question:** Design a production ACM, AWS WAF and Shield capability where Shield Standard/Advanced, DNS validation and WAF web ACL are first-class requirements.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: DDoS protection/support/cost protection differ by service/tier. persistent validation record enables managed renewal when service conditions hold. ordered managed/custom/rate rules return allow/block/count/CAPTCHA/challenge actions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ACM-AWS-WAF-AND-SHIELD-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production ACM, AWS WAF and Shield capability where Origin protection, Imported certificate and Count mode are first-class requirements.
> **Covered in:** [ACM, AWS WAF and Shield — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: edge allowlist/auth/private origin prevents bypassing WAF/CDN controls. customer owns renewal/reimport and expiry alert. observes a new rule before enforcement to detect false positives. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### ACM-AWS-WAF-AND-SHIELD-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ACM certificate. How do you lead it end to end?
> **Covered in:** [ACM, AWS WAF and Shield — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws acm list-certificates` as one read-only checkpoint, not the whole diagnosis. managed public/private/imported certificate with supported service integration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ACM-AWS-WAF-AND-SHIELD-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DNS validation. How do you lead it end to end?
> **Covered in:** [ACM, AWS WAF and Shield — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws acm describe-certificate --certificate-arn ARN` as one read-only checkpoint, not the whole diagnosis. persistent validation record enables managed renewal when service conditions hold. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ACM-AWS-WAF-AND-SHIELD-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Imported certificate. How do you lead it end to end?
> **Covered in:** [ACM, AWS WAF and Shield — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws wafv2 list-web-acls --scope REGIONAL --region REGION` as one read-only checkpoint, not the whole diagnosis. customer owns renewal/reimport and expiry alert. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ACM-AWS-WAF-AND-SHIELD-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TLS policy. How do you lead it end to end?
> **Covered in:** [ACM, AWS WAF and Shield — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws wafv2 get-sampled-requests --web-acl-arn ARN --rule-metric-name METRIC --scope REGIONAL --time-window file://window.json --max-items 100` as one read-only checkpoint, not the whole diagnosis. protocol/cipher compatibility balances client support and security. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ACM-AWS-WAF-AND-SHIELD-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving WAF web ACL. How do you lead it end to end?
> **Covered in:** [ACM, AWS WAF and Shield — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws acm list-certificates` as one read-only checkpoint, not the whole diagnosis. ordered managed/custom/rate rules return allow/block/count/CAPTCHA/challenge actions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ACM-AWS-WAF-AND-SHIELD-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Count mode. How do you lead it end to end?
> **Covered in:** [ACM, AWS WAF and Shield — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws acm describe-certificate --certificate-arn ARN` as one read-only checkpoint, not the whole diagnosis. observes a new rule before enforcement to detect false positives. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ACM-AWS-WAF-AND-SHIELD-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rate-based rule. How do you lead it end to end?
> **Covered in:** [ACM, AWS WAF and Shield — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws wafv2 list-web-acls --scope REGIONAL --region REGION` as one read-only checkpoint, not the whole diagnosis. limits aggregate keys but is not a complete application tenant quota. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ACM-AWS-WAF-AND-SHIELD-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Managed rule version. How do you lead it end to end?
> **Covered in:** [ACM, AWS WAF and Shield — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws wafv2 get-sampled-requests --web-acl-arn ARN --rule-metric-name METRIC --scope REGIONAL --time-window file://window.json --max-items 100` as one read-only checkpoint, not the whole diagnosis. updates can change behavior and require staged rollout. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ACM-AWS-WAF-AND-SHIELD-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Shield Standard/Advanced. How do you lead it end to end?
> **Covered in:** [ACM, AWS WAF and Shield — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws acm list-certificates` as one read-only checkpoint, not the whole diagnosis. DDoS protection/support/cost protection differ by service/tier. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ACM-AWS-WAF-AND-SHIELD-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Origin protection. How do you lead it end to end?
> **Covered in:** [ACM, AWS WAF and Shield — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws acm describe-certificate --certificate-arn ARN` as one read-only checkpoint, not the whole diagnosis. edge allowlist/auth/private origin prevents bypassing WAF/CDN controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AWS Secrets Manager and Parameter Store](../02-secrets-manager/README.md) · [Study note](README.md) · [Next: GuardDuty, Security Hub, Inspector, Macie and Detective →](../04-security-detection/README.md)

<!-- reading-navigation:end -->
