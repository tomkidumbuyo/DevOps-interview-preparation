# AWS IAM

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>

## Easy mode: purpose and mental model

Evaluate and govern who may perform which AWS action on which resource under which request conditions.

```mermaid
flowchart LR
  I[identity and desired state] --> C[AWS IAM control plane]
  C --> D[AWS IAM data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Principals** | users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. |
| 2 | **Identity policies** | attached policies grant or deny actions to a principal within the rest of the policy intersection. |
| 3 | **Resource policies** | supported resources can trust principals directly and express cross-account or service access. |
| 4 | **Explicit deny** | any applicable explicit deny overrides allows and is the first guardrail to search during diagnosis. |
| 5 | **Permissions boundaries** | cap identity-policy permissions without granting actions themselves. |
| 6 | **Session policies** | further restrict an assumed-role session and can explain access that differs from the base role. |
| 7 | **Condition keys** | bind access to organization, source network, tags, MFA, audience and other request context. |
| 8 | **Access Analyzer** | validates policies and analyzes external/internal access paths for supported resources. |
| 9 | **Least privilege** | start from task/resource/condition needs, observe actual use, remove unused access and review exceptions. |
| 10 | **PassRole escalation** | permission to attach a powerful role to a service can be equivalent to using that role indirectly. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For AWS IAM, draw a real request/resource path and label where these mechanisms act: Principals, Identity policies, Resource policies, Explicit deny, Permissions boundaries, Session policies, Condition keys, Access Analyzer, Least privilege, PassRole escalation. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
aws sts get-caller-identity
aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION
aws accessanalyzer validate-policy --policy-document file://policy.json --policy-type IDENTITY_POLICY
aws iam get-account-authorization-details
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy AWS IAM resource and draw identity/control/data/dependency paths.
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

Explain AWS IAM in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
