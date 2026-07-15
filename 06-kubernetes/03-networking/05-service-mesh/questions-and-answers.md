# Service mesh — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### SERVICE-MESH-JN-01

- [ ] **Question:** What is Data-plane proxy, and why does it matter in Service mesh?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-MESH-JN-02

- [ ] **Question:** What is Control plane, and why does it matter in Service mesh?
> **Covered in:** [Service mesh — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** distributes service discovery, certificates and policy to proxies. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-MESH-JN-03

- [ ] **Question:** What is Workload identity, and why does it matter in Service mesh?
> **Covered in:** [Service mesh — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** trust-domain/service-account identity authenticates peers rather than IP alone. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-MESH-JN-04

- [ ] **Question:** What is mTLS, and why does it matter in Service mesh?
> **Covered in:** [Service mesh — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** encrypts/authenticates service traffic while certificate issuance/rotation becomes critical. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-MESH-JN-05

- [ ] **Question:** What is Authorization policy, and why does it matter in Service mesh?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** L4/L7 service identity rules complement Kubernetes NetworkPolicy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-MESH-JN-06

- [ ] **Question:** What is Traffic policy, and why does it matter in Service mesh?
> **Covered in:** [Service mesh — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** retries/timeouts/circuit/outlier/load balancing can amplify or mask application behavior. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-MESH-JN-07

- [ ] **Question:** What is Telemetry, and why does it matter in Service mesh?
> **Covered in:** [Service mesh — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** proxy metrics/traces improve path visibility at cardinality/resource cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-MESH-JN-08

- [ ] **Code:** **Question:** What does `linkerd check` help you verify for Service mesh?
> **Covered in:** [Service mesh — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: workloads missing sidecar/ambient enrollment can bypass expected controls.

### SERVICE-MESH-JN-09

- [ ] **Code:** **Question:** What does `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` help you verify for Service mesh?
> **Covered in:** [Service mesh — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: existing proxy config may continue while new workloads/certs/routes degrade.

### SERVICE-MESH-JN-10

- [ ] **Code:** **Question:** What does `istioctl proxy-status` help you verify for Service mesh?
> **Covered in:** [Service mesh — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: proxy/control/API skew and canary revision migration prevent fleet-wide breakage.

## Junior — procedural and command questions

### SERVICE-MESH-JP-01

- [ ] **Code:** **Question:** A basic Data-plane proxy check fails. What would you do first using the CLI?
> **Covered in:** [Service mesh — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` and capture exact status/reason/request ID. sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-MESH-JP-02

- [ ] **Question:** A basic Control plane check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `istioctl proxy-status` and capture exact status/reason/request ID. distributes service discovery, certificates and policy to proxies. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-MESH-JP-03

- [ ] **Question:** A basic Workload identity check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `istioctl analyze -A` and capture exact status/reason/request ID. trust-domain/service-account identity authenticates peers rather than IP alone. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-MESH-JP-04

- [ ] **Code:** **Question:** A basic mTLS check fails. What would you do first using the CLI?
> **Covered in:** [Service mesh — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `linkerd check` and capture exact status/reason/request ID. encrypts/authenticates service traffic while certificate issuance/rotation becomes critical. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-MESH-JP-05

- [ ] **Question:** A basic Authorization policy check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` and capture exact status/reason/request ID. L4/L7 service identity rules complement Kubernetes NetworkPolicy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-MESH-JP-06

- [ ] **Question:** A basic Traffic policy check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `istioctl proxy-status` and capture exact status/reason/request ID. retries/timeouts/circuit/outlier/load balancing can amplify or mask application behavior. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-MESH-JP-07

- [ ] **Code:** **Question:** A basic Telemetry check fails. What would you do first using the CLI?
> **Covered in:** [Service mesh — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `istioctl analyze -A` and capture exact status/reason/request ID. proxy metrics/traces improve path visibility at cardinality/resource cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-MESH-JP-08

- [ ] **Question:** A basic Injection/attachment check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `linkerd check` and capture exact status/reason/request ID. workloads missing sidecar/ambient enrollment can bypass expected controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-MESH-JP-09

- [ ] **Question:** A basic Control-plane outage check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` and capture exact status/reason/request ID. existing proxy config may continue while new workloads/certs/routes degrade. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-MESH-JP-10

- [ ] **Code:** **Question:** A basic Upgrade check fails. What would you do first using the CLI?
> **Covered in:** [Service mesh — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `istioctl proxy-status` and capture exact status/reason/request ID. proxy/control/API skew and canary revision migration prevent fleet-wide breakage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### SERVICE-MESH-MN-01

- [ ] **Question:** Compare Data-plane proxy with Control plane. When would each change your design?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Data-plane proxy: sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Control plane: distributes service discovery, certificates and policy to proxies. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-MESH-MN-02

- [ ] **Question:** Compare Control plane with Workload identity. When would each change your design?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Control plane: distributes service discovery, certificates and policy to proxies. Workload identity: trust-domain/service-account identity authenticates peers rather than IP alone. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-MESH-MN-03

- [ ] **Question:** Compare Workload identity with mTLS. When would each change your design?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Workload identity: trust-domain/service-account identity authenticates peers rather than IP alone. mTLS: encrypts/authenticates service traffic while certificate issuance/rotation becomes critical. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-MESH-MN-04

- [ ] **Configuration review:** **Question:** Compare mTLS with Authorization policy. When would each change your design?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** mTLS: encrypts/authenticates service traffic while certificate issuance/rotation becomes critical. Authorization policy: L4/L7 service identity rules complement Kubernetes NetworkPolicy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-MESH-MN-05

- [ ] **Question:** Compare Authorization policy with Traffic policy. When would each change your design?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Authorization policy: L4/L7 service identity rules complement Kubernetes NetworkPolicy. Traffic policy: retries/timeouts/circuit/outlier/load balancing can amplify or mask application behavior. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-MESH-MN-06

- [ ] **Question:** Compare Traffic policy with Telemetry. When would each change your design?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Traffic policy: retries/timeouts/circuit/outlier/load balancing can amplify or mask application behavior. Telemetry: proxy metrics/traces improve path visibility at cardinality/resource cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-MESH-MN-07

- [ ] **Configuration review:** **Question:** Compare Telemetry with Injection/attachment. When would each change your design?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Telemetry: proxy metrics/traces improve path visibility at cardinality/resource cost. Injection/attachment: workloads missing sidecar/ambient enrollment can bypass expected controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-MESH-MN-08

- [ ] **Question:** Compare Injection/attachment with Control-plane outage. When would each change your design?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Injection/attachment: workloads missing sidecar/ambient enrollment can bypass expected controls. Control-plane outage: existing proxy config may continue while new workloads/certs/routes degrade. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-MESH-MN-09

- [ ] **Question:** Compare Control-plane outage with Upgrade. When would each change your design?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Control-plane outage: existing proxy config may continue while new workloads/certs/routes degrade. Upgrade: proxy/control/API skew and canary revision migration prevent fleet-wide breakage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-MESH-MN-10

- [ ] **Configuration review:** **Question:** Compare Upgrade with Data-plane proxy. When would each change your design?
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Upgrade: proxy/control/API skew and canary revision migration prevent fleet-wide breakage. Data-plane proxy: sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### SERVICE-MESH-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Data-plane proxy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` plus recent events/changes, then correlate the service-specific SLI. sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-MESH-MP-02

- [ ] **Question:** Production is degraded around Control plane; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `istioctl proxy-status` plus recent events/changes, then correlate the service-specific SLI. distributes service discovery, certificates and policy to proxies. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-MESH-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Workload identity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `istioctl analyze -A` plus recent events/changes, then correlate the service-specific SLI. trust-domain/service-account identity authenticates peers rather than IP alone. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-MESH-MP-04

- [ ] **Question:** Production is degraded around mTLS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `linkerd check` plus recent events/changes, then correlate the service-specific SLI. encrypts/authenticates service traffic while certificate issuance/rotation becomes critical. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-MESH-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Authorization policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` plus recent events/changes, then correlate the service-specific SLI. L4/L7 service identity rules complement Kubernetes NetworkPolicy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-MESH-MP-06

- [ ] **Question:** Production is degraded around Traffic policy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `istioctl proxy-status` plus recent events/changes, then correlate the service-specific SLI. retries/timeouts/circuit/outlier/load balancing can amplify or mask application behavior. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-MESH-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Telemetry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `istioctl analyze -A` plus recent events/changes, then correlate the service-specific SLI. proxy metrics/traces improve path visibility at cardinality/resource cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-MESH-MP-08

- [ ] **Question:** Production is degraded around Injection/attachment; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `linkerd check` plus recent events/changes, then correlate the service-specific SLI. workloads missing sidecar/ambient enrollment can bypass expected controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-MESH-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Control-plane outage; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` plus recent events/changes, then correlate the service-specific SLI. existing proxy config may continue while new workloads/certs/routes degrade. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-MESH-MP-10

- [ ] **Question:** Production is degraded around Upgrade; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `istioctl proxy-status` plus recent events/changes, then correlate the service-specific SLI. proxy/control/API skew and canary revision migration prevent fleet-wide breakage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### SERVICE-MESH-SN-01

- [ ] **Question:** Design a production Service mesh capability where Data-plane proxy, mTLS and Telemetry are first-class requirements.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. encrypts/authenticates service traffic while certificate issuance/rotation becomes critical. proxy metrics/traces improve path visibility at cardinality/resource cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-MESH-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Service mesh capability where Control plane, Authorization policy and Injection/attachment are first-class requirements.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: distributes service discovery, certificates and policy to proxies. L4/L7 service identity rules complement Kubernetes NetworkPolicy. workloads missing sidecar/ambient enrollment can bypass expected controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-MESH-SN-03

- [ ] **Question:** Design a production Service mesh capability where Workload identity, Traffic policy and Control-plane outage are first-class requirements.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: trust-domain/service-account identity authenticates peers rather than IP alone. retries/timeouts/circuit/outlier/load balancing can amplify or mask application behavior. existing proxy config may continue while new workloads/certs/routes degrade. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-MESH-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Service mesh capability where mTLS, Telemetry and Upgrade are first-class requirements.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: encrypts/authenticates service traffic while certificate issuance/rotation becomes critical. proxy metrics/traces improve path visibility at cardinality/resource cost. proxy/control/API skew and canary revision migration prevent fleet-wide breakage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-MESH-SN-05

- [ ] **Question:** Design a production Service mesh capability where Authorization policy, Injection/attachment and Data-plane proxy are first-class requirements.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: L4/L7 service identity rules complement Kubernetes NetworkPolicy. workloads missing sidecar/ambient enrollment can bypass expected controls. sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-MESH-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Service mesh capability where Traffic policy, Control-plane outage and Control plane are first-class requirements.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retries/timeouts/circuit/outlier/load balancing can amplify or mask application behavior. existing proxy config may continue while new workloads/certs/routes degrade. distributes service discovery, certificates and policy to proxies. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-MESH-SN-07

- [ ] **Question:** Design a production Service mesh capability where Telemetry, Upgrade and Workload identity are first-class requirements.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: proxy metrics/traces improve path visibility at cardinality/resource cost. proxy/control/API skew and canary revision migration prevent fleet-wide breakage. trust-domain/service-account identity authenticates peers rather than IP alone. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-MESH-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Service mesh capability where Injection/attachment, Data-plane proxy and mTLS are first-class requirements.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: workloads missing sidecar/ambient enrollment can bypass expected controls. sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. encrypts/authenticates service traffic while certificate issuance/rotation becomes critical. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-MESH-SN-09

- [ ] **Question:** Design a production Service mesh capability where Control-plane outage, Control plane and Authorization policy are first-class requirements.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: existing proxy config may continue while new workloads/certs/routes degrade. distributes service discovery, certificates and policy to proxies. L4/L7 service identity rules complement Kubernetes NetworkPolicy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-MESH-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Service mesh capability where Upgrade, Workload identity and Traffic policy are first-class requirements.
> **Covered in:** [Service mesh — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: proxy/control/API skew and canary revision migration prevent fleet-wide breakage. trust-domain/service-account identity authenticates peers rather than IP alone. retries/timeouts/circuit/outlier/load balancing can amplify or mask application behavior. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### SERVICE-MESH-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Data-plane proxy. How do you lead it end to end?
> **Covered in:** [Service mesh — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` as one read-only checkpoint, not the whole diagnosis. sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-MESH-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control plane. How do you lead it end to end?
> **Covered in:** [Service mesh — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `istioctl proxy-status` as one read-only checkpoint, not the whole diagnosis. distributes service discovery, certificates and policy to proxies. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-MESH-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Workload identity. How do you lead it end to end?
> **Covered in:** [Service mesh — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `istioctl analyze -A` as one read-only checkpoint, not the whole diagnosis. trust-domain/service-account identity authenticates peers rather than IP alone. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-MESH-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving mTLS. How do you lead it end to end?
> **Covered in:** [Service mesh — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `linkerd check` as one read-only checkpoint, not the whole diagnosis. encrypts/authenticates service traffic while certificate issuance/rotation becomes critical. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-MESH-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authorization policy. How do you lead it end to end?
> **Covered in:** [Service mesh — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` as one read-only checkpoint, not the whole diagnosis. L4/L7 service identity rules complement Kubernetes NetworkPolicy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-MESH-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Traffic policy. How do you lead it end to end?
> **Covered in:** [Service mesh — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `istioctl proxy-status` as one read-only checkpoint, not the whole diagnosis. retries/timeouts/circuit/outlier/load balancing can amplify or mask application behavior. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-MESH-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Telemetry. How do you lead it end to end?
> **Covered in:** [Service mesh — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `istioctl analyze -A` as one read-only checkpoint, not the whole diagnosis. proxy metrics/traces improve path visibility at cardinality/resource cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-MESH-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Injection/attachment. How do you lead it end to end?
> **Covered in:** [Service mesh — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `linkerd check` as one read-only checkpoint, not the whole diagnosis. workloads missing sidecar/ambient enrollment can bypass expected controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-MESH-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control-plane outage. How do you lead it end to end?
> **Covered in:** [Service mesh — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` as one read-only checkpoint, not the whole diagnosis. existing proxy config may continue while new workloads/certs/routes degrade. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-MESH-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Upgrade. How do you lead it end to end?
> **Covered in:** [Service mesh — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `istioctl proxy-status` as one read-only checkpoint, not the whole diagnosis. proxy/control/API skew and canary revision migration prevent fleet-wide breakage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Ingress and Gateway API](../04-ingress-gateway-api/README.md) · [Study note](README.md) · [Next: Storage →](../../04-storage/README.md)

<!-- reading-navigation:end -->
