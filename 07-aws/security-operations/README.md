# Security Operations

<!-- child-topic-toc:start -->
## Table of contents and deeper notes

This parent note explains how the child topics work together. Follow each child link for the deeper mechanism, real commands/configuration, hands-on practice, authoritative documentation, and its local interview bank.

- [Security Operations service leaves](services/README.md) — [questions and answers](services/questions-and-answers.md)
<!-- child-topic-toc:end -->
This branch README is both the study note and the map. Each service leaf keeps its notes in its own README and its answered interview bank in a separate file.

```mermaid
flowchart LR
  B[Security Operations]
  B --> S1[AWS KMS]
  B --> S2[AWS Secrets Manager and Parameter Store]
  B --> S3[ACM, AWS WAF and Shield]
  B --> S4[GuardDuty, Security Hub, Inspector, Macie and Detective]
  B --> S5[Amazon CloudWatch and X-Ray]
  B --> S6[AWS CloudTrail and Config]
  B --> S7[AWS Systems Manager]
```

## Service leaves

- [AWS KMS](services/kms/README.md) — [Q&A](services/kms/questions-and-answers.md)
- [AWS Secrets Manager and Parameter Store](services/secrets-manager/README.md) — [Q&A](services/secrets-manager/questions-and-answers.md)
- [ACM, AWS WAF and Shield](services/acm-waf-shield/README.md) — [Q&A](services/acm-waf-shield/questions-and-answers.md)
- [GuardDuty, Security Hub, Inspector, Macie and Detective](services/security-detection/README.md) — [Q&A](services/security-detection/questions-and-answers.md)
- [Amazon CloudWatch and X-Ray](services/cloudwatch-xray/README.md) — [Q&A](services/cloudwatch-xray/questions-and-answers.md)
- [AWS CloudTrail and Config](services/cloudtrail-config/README.md) — [Q&A](services/cloudtrail-config/questions-and-answers.md)
- [AWS Systems Manager](services/systems-manager/README.md) — [Q&A](services/systems-manager/questions-and-answers.md)

## Branch learning contract

Learn the easy mental model first, run the read-only commands in a sandbox, render/apply the examples only in disposable environments, then break and repair one dependency at a time. Be able to connect these topics across the branch: KMS key, Envelope encryption, Key policy, Secret version/stage, Rotation Lambda, Resource policy, ACM certificate, DNS validation, Imported certificate, GuardDuty, Security Hub, Inspector, Metric/dimension, Alarm, Composite alarm, Management event, Data event, Organization trail, Managed node, Session Manager, Run Command.

## Branch interview bank

See [questions-and-answers.md](questions-and-answers.md) for 60 additional branch-level questions and answers. Service-specific banks contain another 60 per service.

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/kms/latest/developerguide/overview.html>

## Easy mode: purpose and mental model

Integrate the security operations branch as one production capability rather than isolated products.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Security Operations control plane]
  C --> D[Security Operations data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **KMS key** | logical key with policy, metadata and protected key material used by integrated services. |
| 2 | **Envelope encryption** | KMS protects data keys while applications/services encrypt bulk data locally. |
| 3 | **Secret version/stage** | labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. |
| 4 | **Rotation Lambda** | creates/sets/tests/finishes a new credential under idempotent staged workflow. |
| 5 | **ACM certificate** | managed public/private/imported certificate with supported service integration. |
| 6 | **DNS validation** | persistent validation record enables managed renewal when service conditions hold. |
| 7 | **GuardDuty** | analyzes supported logs/signals to emit contextual threat findings. |
| 8 | **Security Hub** | aggregates/normalizes findings and control standards across accounts/Regions. |
| 9 | **Metric/dimension** | numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. |
| 10 | **Alarm** | evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Security Operations, draw a real request/resource path and label where these mechanisms act: KMS key, Envelope encryption, Secret version/stage, Rotation Lambda, ACM certificate, DNS validation, GuardDuty, Security Hub, Metric/dimension, Alarm. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

## Security model

Start with the caller/workload identity and evaluate every applicable identity, resource, organization, network-endpoint, encryption-key and admission policy. Minimize public paths, long-lived credentials, wildcard actions/resources and unreviewed cross-account/tenant trust. Encrypt in transit/at rest where applicable, but include key/certificate rotation and recovery. Protect audit evidence and prevent secrets/customer content from entering command history, logs, traces or metric labels.

## Availability and failure modes

List dependencies and failure domains before claiming high availability. Test quota/capacity, identity/control-plane, DNS/network/TLS, configuration drift, downstream saturation, zonal/Regional/node failure and recovery from protected state. Use bounded timeout, retry budget, jitter, idempotency, backpressure, load shedding and graceful drain according to protocol. A green resource status is not a user-facing recovery check.

## Performance, scaling and cost

Measure workload distribution and SLI before sizing. Track rate/work units, latency distribution, errors, saturation/queue and service-specific limits. Separate replica/task scaling from infrastructure/capacity scaling and include cold-start/provisioning delay. Cost includes idle/provisioned capacity, requests/work units, storage/retention, cross-AZ/Region/egress/NAT, observability, licenses/support and failure headroom. Optimize cost per successful SLO/quality-controlled task.

## Observability

Correlate a request/change across user, route/resource, dependency and underlying compute/storage/network. Use stable owner/environment/region/service dimensions; put high-cardinality request/object IDs in sampled logs/traces rather than metric labels. Alert on actionable SLO burn and leading exhaustion. Monitor the telemetry path and keep a read-only diagnostic role.

## Command lab

Run in a sandbox with the correct account/context/Region. Read and explain output before mutation.

```bash
aws kms describe-key --key-id KEY
aws secretsmanager describe-secret --secret-id SECRET
aws acm list-certificates
aws guardduty list-detectors
aws cloudwatch describe-alarms --state-value ALARM
aws cloudtrail describe-trails
aws ssm describe-instance-information
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Security Operations resource and draw identity/control/data/dependency paths.
2. **Intermediate:** reproduce a safe configuration change with IaC, preview/diff, apply to a sandbox, verify and roll back.
3. **Hard:** inject one policy/network/quota/capacity/dependency failure, diagnose from user symptom to root mechanism, mitigate without widening access, then add an alert/test/runbook.
4. **Senior:** design the service for two tenants, multi-zone/Region failure, RPO/RTO, regulated data, 10× demand and a 30% cost reduction; quantify trade-offs.

## Common interview traps

- Naming a feature without explaining request/resource lifecycle or failure semantics.
- Treating an allow, encryption checkbox, replica count or managed-service label as a complete security/reliability design.
- Mutating production before capturing identity, status, events, metrics, logs, audit and recent changes.
- Scaling the wrong layer or retrying overload/permanent errors.
- Omitting quotas, cold start, deletion/restore, observability cost or customer/tenant boundaries.

## Revision summary

Explain Security Operations in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.

<!-- merged-07-AWS-SECURITY-OBSERVABILITY-OPERATIONS-MD:start -->
## Practical deep dive

## Security control planes

KMS keys protect data keys through envelope encryption. Key policies are foundational; IAM permissions alone may not be enough. Grants delegate constrained use, encryption context can bind purpose, and rotation semantics differ for AWS-managed/customer-managed/imported key material. Plan deletion carefully and test decrypt/restore before retiring keys.

Secrets Manager stores/rotates secrets through controlled workflows; Parameter Store handles configuration and secure strings with different feature/cost profiles. Prefer workload identity and dynamic/rotated credentials, cache briefly with revocation awareness, restrict resource/KMS policies, audit reads and never emit values to logs/traces. ACM manages public/private certificates in supported integrations; imported/private cert lifecycle needs monitoring.

WAF filters Layer 7 requests and needs tuning/false-positive response; Shield addresses DDoS protections; GuardDuty detects suspicious activity; Security Hub aggregates/normalizes findings; Inspector assesses workloads/images; Macie discovers sensitive S3 data; Detective supports investigation. These services do not replace identity/network/data controls or an owned response process.

CloudTrail records account/API activity with management/data/Insights event choices; organization trails and immutable centralized destinations protect evidence. AWS Config records supported resource configuration/compliance over time. IAM Access Analyzer finds external/internal access issues and validates policies. Use delegated security administration and separate log/security accounts to reduce workload compromise blast radius.

## Observability model

CloudWatch metrics are time series; Logs stores/queries events; alarms evaluate metrics; composite alarms combine alarm state; dashboards communicate views. Embedded Metric Format derives metrics from structured logs but still affects cardinality/cost. Container Insights/Application Signals add curated telemetry; X-Ray traces sampled request paths. CloudTrail is audit, not application performance telemetry.

Start from SLIs: availability/error, latency distributions/TTFT, throughput/tokens, saturation/queue/GPU/cache, correctness/quality where AI is involved. Use dimensions that enable owner/tenant/model/region diagnosis without uncontrolled cardinality or sensitive content. Define retention/tiering, sampling and redaction at collection time. Monitor the telemetry pipeline itself.

Systems Manager Inventory, Session Manager, Patch Manager, Automation and Run Command provide fleet operations. Treat documents/parameters/targets as privileged code: review, constrain `iam:PassRole`, stage concurrency/error thresholds, log output securely and test rollback. OpsCenter/Incident Manager-style workflows can organize response, but humans still own severity, command and communication.

## Incident response

1. Declare severity/roles, protect life/data, scope accounts/Regions/resources and preserve time/evidence.
2. Contain reversibly: quarantine SG/NACL/route/role/session/resource policy, disable exposed key, or isolate instance—without destroying forensic data.
3. Query organization CloudTrail, Config history, GuardDuty/Security Hub and workload/network/identity telemetry; build a timeline.
4. Eradicate the persistence/root cause, rotate affected credentials/secrets/keys, rebuild from trusted artifacts and repair policy/IaC.
5. Recover progressively with explicit validation and heightened monitoring.
6. Notify required stakeholders/regulators/customers, preserve chain of custody, and track preventive actions to effectiveness review.

## Reliability, cost and practical checks

Keep alarm actions and paging independent enough from the failing workload; test log delivery and cross-account access. Avoid one Region/account being the only evidence path. Costs grow through log ingestion/retention/query, custom/high-resolution metrics, high-cardinality dimensions, data events, traces and cross-Region copies. Budget telemetry per diagnostic value and compliance obligation.

```bash
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=EVENT
aws configservice get-resource-config-history --resource-type TYPE --resource-id ID
aws cloudwatch describe-alarms --state-value ALARM
aws logs start-query --log-group-name GROUP --start-time START --end-time END --query-string QUERY
aws ssm describe-instance-information
```

## Revision summary

- KMS authorization and lifecycle can make encrypted data unavailable.
- Detection services provide signals; owned response converts signals into risk reduction.
- Audit, configuration history and application telemetry answer different questions.
- Instrument from SLOs and diagnostic decisions, with privacy/cardinality/cost controls.
- Contain safely, preserve evidence, rebuild from trusted state and verify prevention.


<!-- merged-07-AWS-SECURITY-OBSERVABILITY-OPERATIONS-MD:end -->
