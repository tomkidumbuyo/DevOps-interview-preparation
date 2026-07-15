# Kubernetes authentication, RBAC and ServiceAccounts

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <https://kubernetes.io/docs/reference/access-authn-authz/rbac/>

## Easy mode: purpose and mental model

Bind short-lived identities to the minimum verbs/resources/namespaces without escalation paths.

```mermaid
flowchart LR
  I[identity and desired state] --> C[Kubernetes authentication, RBAC and ServiceAccounts control plane]
  C --> D[Kubernetes authentication, RBAC and ServiceAccounts data plane]
  D --> U[user/workload outcome]
  D --> O[metrics logs traces audit]
  O --> R[reconcile scale recover optimize]
```

## Detailed learning notes

| # | Concept | What you must be able to explain |
|---:|---|---|
| 1 | **Authentication** | client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount. |
| 2 | **Authorization** | RBAC/webhook/node/ABAC modes decide a request after authentication. |
| 3 | **Role/ClusterRole** | namespaced/cluster rule collections over API group/resource/subresource/verb. |
| 4 | **RoleBinding** | grants a Role or ClusterRole within one namespace. |
| 5 | **ClusterRoleBinding** | grants cluster-wide and is a high-blast-radius object. |
| 6 | **ServiceAccount** | namespaced workload identity with projected bound token support. |
| 7 | **TokenRequest** | short-lived audience/expiry-bound token avoids legacy static secret tokens. |
| 8 | **Impersonation** | powerful diagnostic/delegation verb that must be narrowly controlled/audited. |
| 9 | **bind/escalate** | permissions can create bindings/roles beyond a caller's current rights. |
| 10 | **Workload escalation** | create Pod can expose mounted secrets, service account, host/device or node credentials. |

## Architecture and lifecycle

Trace this service from request/authentication and desired configuration through provisioning, steady-state data path, scaling, change, failure, recovery and retirement. Bind every production resource to an owner, environment, data classification, source-of-truth revision, SLO, runbook, cost center and deletion/retention policy.

For Kubernetes authentication, RBAC and ServiceAccounts, draw a real request/resource path and label where these mechanisms act: Authentication, Authorization, Role/ClusterRole, RoleBinding, ClusterRoleBinding, ServiceAccount, TokenRequest, Impersonation, bind/escalate, Workload escalation. State which parts are control plane versus data plane, regional versus zonal/global, synchronous versus asynchronous, and customer versus provider responsibility.

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
kubectl auth whoami
kubectl auth can-i --list -n NS
kubectl auth can-i VERB RESOURCE --as=USER --as-group=GROUP -n NS
kubectl create token SA -n NS --duration=10m
```

For each command, record: identity/context, exact resource, expected healthy fields, one failing output, the next command/query, and which mutation would be reversible. Never paste secrets/tokens into committed notes or shared terminal history.

## Real-world exercise: easy → hard

1. **Easy:** inventory one healthy Kubernetes authentication, RBAC and ServiceAccounts resource and draw identity/control/data/dependency paths.
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

Explain Kubernetes authentication, RBAC and ServiceAccounts in five passes: purpose/selection, mechanism/lifecycle, security/failure, operation/commands, and architecture/economics. Then complete the separate [answered question bank](questions-and-answers.md) without looking at these notes.
