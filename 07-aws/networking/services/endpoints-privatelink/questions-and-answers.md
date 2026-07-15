# VPC endpoints and AWS PrivateLink — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JN-01

- [ ] **Question:** What is Gateway endpoint, and why does it matter in VPC endpoints and AWS PrivateLink?

**Answer:** route-table target for supported services such as S3/DynamoDB without endpoint ENIs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JN-02

- [ ] **Question:** What is Interface endpoint, and why does it matter in VPC endpoints and AWS PrivateLink?

**Answer:** PrivateLink ENIs in subnets with security groups and per-hour/data cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JN-03

- [ ] **Question:** What is Private DNS, and why does it matter in VPC endpoints and AWS PrivateLink?

**Answer:** maps standard service hostname to endpoint addresses inside associated VPCs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JN-04

- [ ] **Question:** What is Endpoint policy, and why does it matter in VPC endpoints and AWS PrivateLink?

**Answer:** constrains calls through the endpoint but does not grant principal/resource permission. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JN-05

- [ ] **Question:** What is Endpoint service, and why does it matter in VPC endpoints and AWS PrivateLink?

**Answer:** NLB-backed producer service exposed privately to approved consumers. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JN-06

- [ ] **Question:** What is Acceptance/permissions, and why does it matter in VPC endpoints and AWS PrivateLink?

**Answer:** service owners control which accounts/principals may create endpoint connections. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JN-07

- [ ] **Question:** What is Zonal design, and why does it matter in VPC endpoints and AWS PrivateLink?

**Answer:** endpoint ENIs and DNS answers must align with AZ resilience and client paths. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JN-08

- [ ] **Code:** **Question:** What does `dig SERVICE.REGION.amazonaws.com` help you verify for VPC endpoints and AWS PrivateLink?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: source VPC/endpoint conditions can constrain data access under known service semantics.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` help you verify for VPC endpoints and AWS PrivateLink?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: on-prem clients need Resolver/routing to use private endpoints correctly.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JN-10

- [ ] **Code:** **Question:** What does `aws ec2 describe-vpc-endpoint-services` help you verify for VPC endpoints and AWS PrivateLink?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: endpoint hours/data versus NAT processing/cross-AZ/exposure depends on traffic and topology.

## Junior — procedural and command questions

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JP-01

- [ ] **Code:** **Question:** A basic Gateway endpoint check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` and capture exact status/reason/request ID. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JP-02

- [ ] **Question:** A basic Interface endpoint check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoint-services` and capture exact status/reason/request ID. PrivateLink ENIs in subnets with security groups and per-hour/data cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JP-03

- [ ] **Question:** A basic Private DNS check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoint-connections` and capture exact status/reason/request ID. maps standard service hostname to endpoint addresses inside associated VPCs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JP-04

- [ ] **Code:** **Question:** A basic Endpoint policy check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig SERVICE.REGION.amazonaws.com` and capture exact status/reason/request ID. constrains calls through the endpoint but does not grant principal/resource permission. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JP-05

- [ ] **Question:** A basic Endpoint service check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` and capture exact status/reason/request ID. NLB-backed producer service exposed privately to approved consumers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JP-06

- [ ] **Question:** A basic Acceptance/permissions check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoint-services` and capture exact status/reason/request ID. service owners control which accounts/principals may create endpoint connections. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JP-07

- [ ] **Code:** **Question:** A basic Zonal design check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoint-connections` and capture exact status/reason/request ID. endpoint ENIs and DNS answers must align with AZ resilience and client paths. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JP-08

- [ ] **Question:** A basic Resource policy conditions check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig SERVICE.REGION.amazonaws.com` and capture exact status/reason/request ID. source VPC/endpoint conditions can constrain data access under known service semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JP-09

- [ ] **Question:** A basic Hybrid DNS/path check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` and capture exact status/reason/request ID. on-prem clients need Resolver/routing to use private endpoints correctly. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-JP-10

- [ ] **Code:** **Question:** A basic Cost comparison check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoint-services` and capture exact status/reason/request ID. endpoint hours/data versus NAT processing/cross-AZ/exposure depends on traffic and topology. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MN-01

- [ ] **Question:** Compare Gateway endpoint with Interface endpoint. When would each change your design?

**Answer:** Gateway endpoint: route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Interface endpoint: PrivateLink ENIs in subnets with security groups and per-hour/data cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MN-02

- [ ] **Question:** Compare Interface endpoint with Private DNS. When would each change your design?

**Answer:** Interface endpoint: PrivateLink ENIs in subnets with security groups and per-hour/data cost. Private DNS: maps standard service hostname to endpoint addresses inside associated VPCs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MN-03

- [ ] **Question:** Compare Private DNS with Endpoint policy. When would each change your design?

**Answer:** Private DNS: maps standard service hostname to endpoint addresses inside associated VPCs. Endpoint policy: constrains calls through the endpoint but does not grant principal/resource permission. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MN-04

- [ ] **Configuration review:** **Question:** Compare Endpoint policy with Endpoint service. When would each change your design?

**Answer:** Endpoint policy: constrains calls through the endpoint but does not grant principal/resource permission. Endpoint service: NLB-backed producer service exposed privately to approved consumers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MN-05

- [ ] **Question:** Compare Endpoint service with Acceptance/permissions. When would each change your design?

**Answer:** Endpoint service: NLB-backed producer service exposed privately to approved consumers. Acceptance/permissions: service owners control which accounts/principals may create endpoint connections. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MN-06

- [ ] **Question:** Compare Acceptance/permissions with Zonal design. When would each change your design?

**Answer:** Acceptance/permissions: service owners control which accounts/principals may create endpoint connections. Zonal design: endpoint ENIs and DNS answers must align with AZ resilience and client paths. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MN-07

- [ ] **Configuration review:** **Question:** Compare Zonal design with Resource policy conditions. When would each change your design?

**Answer:** Zonal design: endpoint ENIs and DNS answers must align with AZ resilience and client paths. Resource policy conditions: source VPC/endpoint conditions can constrain data access under known service semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MN-08

- [ ] **Question:** Compare Resource policy conditions with Hybrid DNS/path. When would each change your design?

**Answer:** Resource policy conditions: source VPC/endpoint conditions can constrain data access under known service semantics. Hybrid DNS/path: on-prem clients need Resolver/routing to use private endpoints correctly. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MN-09

- [ ] **Question:** Compare Hybrid DNS/path with Cost comparison. When would each change your design?

**Answer:** Hybrid DNS/path: on-prem clients need Resolver/routing to use private endpoints correctly. Cost comparison: endpoint hours/data versus NAT processing/cross-AZ/exposure depends on traffic and topology. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MN-10

- [ ] **Configuration review:** **Question:** Compare Cost comparison with Gateway endpoint. When would each change your design?

**Answer:** Cost comparison: endpoint hours/data versus NAT processing/cross-AZ/exposure depends on traffic and topology. Gateway endpoint: route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Gateway endpoint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` plus recent events/changes, then correlate the service-specific SLI. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MP-02

- [ ] **Question:** Production is degraded around Interface endpoint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoint-services` plus recent events/changes, then correlate the service-specific SLI. PrivateLink ENIs in subnets with security groups and per-hour/data cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Private DNS; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoint-connections` plus recent events/changes, then correlate the service-specific SLI. maps standard service hostname to endpoint addresses inside associated VPCs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MP-04

- [ ] **Question:** Production is degraded around Endpoint policy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig SERVICE.REGION.amazonaws.com` plus recent events/changes, then correlate the service-specific SLI. constrains calls through the endpoint but does not grant principal/resource permission. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Endpoint service; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` plus recent events/changes, then correlate the service-specific SLI. NLB-backed producer service exposed privately to approved consumers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MP-06

- [ ] **Question:** Production is degraded around Acceptance/permissions; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoint-services` plus recent events/changes, then correlate the service-specific SLI. service owners control which accounts/principals may create endpoint connections. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Zonal design; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoint-connections` plus recent events/changes, then correlate the service-specific SLI. endpoint ENIs and DNS answers must align with AZ resilience and client paths. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MP-08

- [ ] **Question:** Production is degraded around Resource policy conditions; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig SERVICE.REGION.amazonaws.com` plus recent events/changes, then correlate the service-specific SLI. source VPC/endpoint conditions can constrain data access under known service semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Hybrid DNS/path; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` plus recent events/changes, then correlate the service-specific SLI. on-prem clients need Resolver/routing to use private endpoints correctly. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-MP-10

- [ ] **Question:** Production is degraded around Cost comparison; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoint-services` plus recent events/changes, then correlate the service-specific SLI. endpoint hours/data versus NAT processing/cross-AZ/exposure depends on traffic and topology. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SN-01

- [ ] **Question:** Design a production VPC endpoints and AWS PrivateLink capability where Gateway endpoint, Endpoint policy and Zonal design are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: route-table target for supported services such as S3/DynamoDB without endpoint ENIs. constrains calls through the endpoint but does not grant principal/resource permission. endpoint ENIs and DNS answers must align with AZ resilience and client paths. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production VPC endpoints and AWS PrivateLink capability where Interface endpoint, Endpoint service and Resource policy conditions are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: PrivateLink ENIs in subnets with security groups and per-hour/data cost. NLB-backed producer service exposed privately to approved consumers. source VPC/endpoint conditions can constrain data access under known service semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SN-03

- [ ] **Question:** Design a production VPC endpoints and AWS PrivateLink capability where Private DNS, Acceptance/permissions and Hybrid DNS/path are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: maps standard service hostname to endpoint addresses inside associated VPCs. service owners control which accounts/principals may create endpoint connections. on-prem clients need Resolver/routing to use private endpoints correctly. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production VPC endpoints and AWS PrivateLink capability where Endpoint policy, Zonal design and Cost comparison are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: constrains calls through the endpoint but does not grant principal/resource permission. endpoint ENIs and DNS answers must align with AZ resilience and client paths. endpoint hours/data versus NAT processing/cross-AZ/exposure depends on traffic and topology. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SN-05

- [ ] **Question:** Design a production VPC endpoints and AWS PrivateLink capability where Endpoint service, Resource policy conditions and Gateway endpoint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: NLB-backed producer service exposed privately to approved consumers. source VPC/endpoint conditions can constrain data access under known service semantics. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production VPC endpoints and AWS PrivateLink capability where Acceptance/permissions, Hybrid DNS/path and Interface endpoint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: service owners control which accounts/principals may create endpoint connections. on-prem clients need Resolver/routing to use private endpoints correctly. PrivateLink ENIs in subnets with security groups and per-hour/data cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SN-07

- [ ] **Question:** Design a production VPC endpoints and AWS PrivateLink capability where Zonal design, Cost comparison and Private DNS are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: endpoint ENIs and DNS answers must align with AZ resilience and client paths. endpoint hours/data versus NAT processing/cross-AZ/exposure depends on traffic and topology. maps standard service hostname to endpoint addresses inside associated VPCs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production VPC endpoints and AWS PrivateLink capability where Resource policy conditions, Gateway endpoint and Endpoint policy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: source VPC/endpoint conditions can constrain data access under known service semantics. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. constrains calls through the endpoint but does not grant principal/resource permission. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SN-09

- [ ] **Question:** Design a production VPC endpoints and AWS PrivateLink capability where Hybrid DNS/path, Interface endpoint and Endpoint service are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: on-prem clients need Resolver/routing to use private endpoints correctly. PrivateLink ENIs in subnets with security groups and per-hour/data cost. NLB-backed producer service exposed privately to approved consumers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production VPC endpoints and AWS PrivateLink capability where Cost comparison, Private DNS and Acceptance/permissions are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: endpoint hours/data versus NAT processing/cross-AZ/exposure depends on traffic and topology. maps standard service hostname to endpoint addresses inside associated VPCs. service owners control which accounts/principals may create endpoint connections. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Gateway endpoint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` as one read-only checkpoint, not the whole diagnosis. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Interface endpoint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoint-services` as one read-only checkpoint, not the whole diagnosis. PrivateLink ENIs in subnets with security groups and per-hour/data cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Private DNS. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoint-connections` as one read-only checkpoint, not the whole diagnosis. maps standard service hostname to endpoint addresses inside associated VPCs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Endpoint policy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig SERVICE.REGION.amazonaws.com` as one read-only checkpoint, not the whole diagnosis. constrains calls through the endpoint but does not grant principal/resource permission. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Endpoint service. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` as one read-only checkpoint, not the whole diagnosis. NLB-backed producer service exposed privately to approved consumers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Acceptance/permissions. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoint-services` as one read-only checkpoint, not the whole diagnosis. service owners control which accounts/principals may create endpoint connections. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Zonal design. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoint-connections` as one read-only checkpoint, not the whole diagnosis. endpoint ENIs and DNS answers must align with AZ resilience and client paths. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource policy conditions. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig SERVICE.REGION.amazonaws.com` as one read-only checkpoint, not the whole diagnosis. source VPC/endpoint conditions can constrain data access under known service semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hybrid DNS/path. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` as one read-only checkpoint, not the whole diagnosis. on-prem clients need Resolver/routing to use private endpoints correctly. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-ENDPOINTS-AND-AWS-PRIVATELINK-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cost comparison. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoint-services` as one read-only checkpoint, not the whole diagnosis. endpoint hours/data versus NAT processing/cross-AZ/exposure depends on traffic and topology. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
