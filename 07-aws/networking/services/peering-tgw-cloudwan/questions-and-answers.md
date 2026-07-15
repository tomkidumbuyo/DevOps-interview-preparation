# VPC peering, Transit Gateway and Cloud WAN — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JN-01

- [ ] **Question:** What is VPC peering, and why does it matter in VPC peering, Transit Gateway and Cloud WAN?

**Answer:** direct non-transitive connectivity that requires non-overlap and routes on both sides. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JN-02

- [ ] **Question:** What is Transit Gateway attachments, and why does it matter in VPC peering, Transit Gateway and Cloud WAN?

**Answer:** connect VPC, VPN, Direct Connect gateway or peering into a routed hub. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JN-03

- [ ] **Question:** What is TGW route association, and why does it matter in VPC peering, Transit Gateway and Cloud WAN?

**Answer:** selects the route table used to route traffic entering an attachment. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JN-04

- [ ] **Question:** What is TGW propagation, and why does it matter in VPC peering, Transit Gateway and Cloud WAN?

**Answer:** inserts learned/attachment routes into selected route tables. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JN-05

- [ ] **Question:** What is Segmentation, and why does it matter in VPC peering, Transit Gateway and Cloud WAN?

**Answer:** separate production, shared services, inspection and customer route domains. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JN-06

- [ ] **Question:** What is Appliance mode, and why does it matter in VPC peering, Transit Gateway and Cloud WAN?

**Answer:** preserves flow symmetry through stateful inspection appliances in supported topology. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JN-07

- [ ] **Question:** What is Inter-Region peering, and why does it matter in VPC peering, Transit Gateway and Cloud WAN?

**Answer:** connects TGWs with explicit routes and data-transfer considerations. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JN-08

- [ ] **Code:** **Question:** What does `aws networkmanager get-core-network-policy --core-network-id CORE_ID --policy-version-id VERSION` help you verify for VPC peering, Transit Gateway and Cloud WAN?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: declaratively manages global core network segments and attachments.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-vpc-peering-connections` help you verify for VPC peering, Transit Gateway and Cloud WAN?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: blocks ordinary routing and may require renumbering, translation or proxy/service exposure.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JN-10

- [ ] **Code:** **Question:** What does `aws ec2 describe-transit-gateway-attachments` help you verify for VPC peering, Transit Gateway and Cloud WAN?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: attachment, processing, inter-Region and operations cost grow with hub scope.

## Junior — procedural and command questions

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JP-01

- [ ] **Code:** **Question:** A basic VPC peering check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-peering-connections` and capture exact status/reason/request ID. direct non-transitive connectivity that requires non-overlap and routes on both sides. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JP-02

- [ ] **Question:** A basic Transit Gateway attachments check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-transit-gateway-attachments` and capture exact status/reason/request ID. connect VPC, VPN, Direct Connect gateway or peering into a routed hub. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JP-03

- [ ] **Question:** A basic TGW route association check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 search-transit-gateway-routes --transit-gateway-route-table-id TGW_RT --filters file://filters.json` and capture exact status/reason/request ID. selects the route table used to route traffic entering an attachment. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JP-04

- [ ] **Code:** **Question:** A basic TGW propagation check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws networkmanager get-core-network-policy --core-network-id CORE_ID --policy-version-id VERSION` and capture exact status/reason/request ID. inserts learned/attachment routes into selected route tables. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JP-05

- [ ] **Question:** A basic Segmentation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-peering-connections` and capture exact status/reason/request ID. separate production, shared services, inspection and customer route domains. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JP-06

- [ ] **Question:** A basic Appliance mode check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-transit-gateway-attachments` and capture exact status/reason/request ID. preserves flow symmetry through stateful inspection appliances in supported topology. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JP-07

- [ ] **Code:** **Question:** A basic Inter-Region peering check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 search-transit-gateway-routes --transit-gateway-route-table-id TGW_RT --filters file://filters.json` and capture exact status/reason/request ID. connects TGWs with explicit routes and data-transfer considerations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JP-08

- [ ] **Question:** A basic Cloud WAN policy check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws networkmanager get-core-network-policy --core-network-id CORE_ID --policy-version-id VERSION` and capture exact status/reason/request ID. declaratively manages global core network segments and attachments. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JP-09

- [ ] **Question:** A basic Overlapping CIDR check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-peering-connections` and capture exact status/reason/request ID. blocks ordinary routing and may require renumbering, translation or proxy/service exposure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-JP-10

- [ ] **Code:** **Question:** A basic Route scale/cost check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-transit-gateway-attachments` and capture exact status/reason/request ID. attachment, processing, inter-Region and operations cost grow with hub scope. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MN-01

- [ ] **Question:** Compare VPC peering with Transit Gateway attachments. When would each change your design?

**Answer:** VPC peering: direct non-transitive connectivity that requires non-overlap and routes on both sides. Transit Gateway attachments: connect VPC, VPN, Direct Connect gateway or peering into a routed hub. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MN-02

- [ ] **Question:** Compare Transit Gateway attachments with TGW route association. When would each change your design?

**Answer:** Transit Gateway attachments: connect VPC, VPN, Direct Connect gateway or peering into a routed hub. TGW route association: selects the route table used to route traffic entering an attachment. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MN-03

- [ ] **Question:** Compare TGW route association with TGW propagation. When would each change your design?

**Answer:** TGW route association: selects the route table used to route traffic entering an attachment. TGW propagation: inserts learned/attachment routes into selected route tables. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MN-04

- [ ] **Configuration review:** **Question:** Compare TGW propagation with Segmentation. When would each change your design?

**Answer:** TGW propagation: inserts learned/attachment routes into selected route tables. Segmentation: separate production, shared services, inspection and customer route domains. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MN-05

- [ ] **Question:** Compare Segmentation with Appliance mode. When would each change your design?

**Answer:** Segmentation: separate production, shared services, inspection and customer route domains. Appliance mode: preserves flow symmetry through stateful inspection appliances in supported topology. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MN-06

- [ ] **Question:** Compare Appliance mode with Inter-Region peering. When would each change your design?

**Answer:** Appliance mode: preserves flow symmetry through stateful inspection appliances in supported topology. Inter-Region peering: connects TGWs with explicit routes and data-transfer considerations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MN-07

- [ ] **Configuration review:** **Question:** Compare Inter-Region peering with Cloud WAN policy. When would each change your design?

**Answer:** Inter-Region peering: connects TGWs with explicit routes and data-transfer considerations. Cloud WAN policy: declaratively manages global core network segments and attachments. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MN-08

- [ ] **Question:** Compare Cloud WAN policy with Overlapping CIDR. When would each change your design?

**Answer:** Cloud WAN policy: declaratively manages global core network segments and attachments. Overlapping CIDR: blocks ordinary routing and may require renumbering, translation or proxy/service exposure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MN-09

- [ ] **Question:** Compare Overlapping CIDR with Route scale/cost. When would each change your design?

**Answer:** Overlapping CIDR: blocks ordinary routing and may require renumbering, translation or proxy/service exposure. Route scale/cost: attachment, processing, inter-Region and operations cost grow with hub scope. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MN-10

- [ ] **Configuration review:** **Question:** Compare Route scale/cost with VPC peering. When would each change your design?

**Answer:** Route scale/cost: attachment, processing, inter-Region and operations cost grow with hub scope. VPC peering: direct non-transitive connectivity that requires non-overlap and routes on both sides. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around VPC peering; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-peering-connections` plus recent events/changes, then correlate the service-specific SLI. direct non-transitive connectivity that requires non-overlap and routes on both sides. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MP-02

- [ ] **Question:** Production is degraded around Transit Gateway attachments; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-transit-gateway-attachments` plus recent events/changes, then correlate the service-specific SLI. connect VPC, VPN, Direct Connect gateway or peering into a routed hub. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around TGW route association; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 search-transit-gateway-routes --transit-gateway-route-table-id TGW_RT --filters file://filters.json` plus recent events/changes, then correlate the service-specific SLI. selects the route table used to route traffic entering an attachment. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MP-04

- [ ] **Question:** Production is degraded around TGW propagation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws networkmanager get-core-network-policy --core-network-id CORE_ID --policy-version-id VERSION` plus recent events/changes, then correlate the service-specific SLI. inserts learned/attachment routes into selected route tables. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Segmentation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-peering-connections` plus recent events/changes, then correlate the service-specific SLI. separate production, shared services, inspection and customer route domains. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MP-06

- [ ] **Question:** Production is degraded around Appliance mode; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-transit-gateway-attachments` plus recent events/changes, then correlate the service-specific SLI. preserves flow symmetry through stateful inspection appliances in supported topology. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Inter-Region peering; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 search-transit-gateway-routes --transit-gateway-route-table-id TGW_RT --filters file://filters.json` plus recent events/changes, then correlate the service-specific SLI. connects TGWs with explicit routes and data-transfer considerations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MP-08

- [ ] **Question:** Production is degraded around Cloud WAN policy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws networkmanager get-core-network-policy --core-network-id CORE_ID --policy-version-id VERSION` plus recent events/changes, then correlate the service-specific SLI. declaratively manages global core network segments and attachments. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Overlapping CIDR; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-peering-connections` plus recent events/changes, then correlate the service-specific SLI. blocks ordinary routing and may require renumbering, translation or proxy/service exposure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-MP-10

- [ ] **Question:** Production is degraded around Route scale/cost; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-transit-gateway-attachments` plus recent events/changes, then correlate the service-specific SLI. attachment, processing, inter-Region and operations cost grow with hub scope. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SN-01

- [ ] **Question:** Design a production VPC peering, Transit Gateway and Cloud WAN capability where VPC peering, TGW propagation and Inter-Region peering are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: direct non-transitive connectivity that requires non-overlap and routes on both sides. inserts learned/attachment routes into selected route tables. connects TGWs with explicit routes and data-transfer considerations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production VPC peering, Transit Gateway and Cloud WAN capability where Transit Gateway attachments, Segmentation and Cloud WAN policy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: connect VPC, VPN, Direct Connect gateway or peering into a routed hub. separate production, shared services, inspection and customer route domains. declaratively manages global core network segments and attachments. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SN-03

- [ ] **Question:** Design a production VPC peering, Transit Gateway and Cloud WAN capability where TGW route association, Appliance mode and Overlapping CIDR are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: selects the route table used to route traffic entering an attachment. preserves flow symmetry through stateful inspection appliances in supported topology. blocks ordinary routing and may require renumbering, translation or proxy/service exposure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production VPC peering, Transit Gateway and Cloud WAN capability where TGW propagation, Inter-Region peering and Route scale/cost are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: inserts learned/attachment routes into selected route tables. connects TGWs with explicit routes and data-transfer considerations. attachment, processing, inter-Region and operations cost grow with hub scope. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SN-05

- [ ] **Question:** Design a production VPC peering, Transit Gateway and Cloud WAN capability where Segmentation, Cloud WAN policy and VPC peering are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: separate production, shared services, inspection and customer route domains. declaratively manages global core network segments and attachments. direct non-transitive connectivity that requires non-overlap and routes on both sides. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production VPC peering, Transit Gateway and Cloud WAN capability where Appliance mode, Overlapping CIDR and Transit Gateway attachments are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: preserves flow symmetry through stateful inspection appliances in supported topology. blocks ordinary routing and may require renumbering, translation or proxy/service exposure. connect VPC, VPN, Direct Connect gateway or peering into a routed hub. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SN-07

- [ ] **Question:** Design a production VPC peering, Transit Gateway and Cloud WAN capability where Inter-Region peering, Route scale/cost and TGW route association are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: connects TGWs with explicit routes and data-transfer considerations. attachment, processing, inter-Region and operations cost grow with hub scope. selects the route table used to route traffic entering an attachment. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production VPC peering, Transit Gateway and Cloud WAN capability where Cloud WAN policy, VPC peering and TGW propagation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: declaratively manages global core network segments and attachments. direct non-transitive connectivity that requires non-overlap and routes on both sides. inserts learned/attachment routes into selected route tables. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SN-09

- [ ] **Question:** Design a production VPC peering, Transit Gateway and Cloud WAN capability where Overlapping CIDR, Transit Gateway attachments and Segmentation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: blocks ordinary routing and may require renumbering, translation or proxy/service exposure. connect VPC, VPN, Direct Connect gateway or peering into a routed hub. separate production, shared services, inspection and customer route domains. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production VPC peering, Transit Gateway and Cloud WAN capability where Route scale/cost, TGW route association and Appliance mode are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: attachment, processing, inter-Region and operations cost grow with hub scope. selects the route table used to route traffic entering an attachment. preserves flow symmetry through stateful inspection appliances in supported topology. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPC peering. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-peering-connections` as one read-only checkpoint, not the whole diagnosis. direct non-transitive connectivity that requires non-overlap and routes on both sides. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Transit Gateway attachments. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-transit-gateway-attachments` as one read-only checkpoint, not the whole diagnosis. connect VPC, VPN, Direct Connect gateway or peering into a routed hub. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TGW route association. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 search-transit-gateway-routes --transit-gateway-route-table-id TGW_RT --filters file://filters.json` as one read-only checkpoint, not the whole diagnosis. selects the route table used to route traffic entering an attachment. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TGW propagation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws networkmanager get-core-network-policy --core-network-id CORE_ID --policy-version-id VERSION` as one read-only checkpoint, not the whole diagnosis. inserts learned/attachment routes into selected route tables. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Segmentation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-peering-connections` as one read-only checkpoint, not the whole diagnosis. separate production, shared services, inspection and customer route domains. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Appliance mode. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-transit-gateway-attachments` as one read-only checkpoint, not the whole diagnosis. preserves flow symmetry through stateful inspection appliances in supported topology. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Inter-Region peering. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 search-transit-gateway-routes --transit-gateway-route-table-id TGW_RT --filters file://filters.json` as one read-only checkpoint, not the whole diagnosis. connects TGWs with explicit routes and data-transfer considerations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cloud WAN policy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws networkmanager get-core-network-policy --core-network-id CORE_ID --policy-version-id VERSION` as one read-only checkpoint, not the whole diagnosis. declaratively manages global core network segments and attachments. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Overlapping CIDR. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-peering-connections` as one read-only checkpoint, not the whole diagnosis. blocks ordinary routing and may require renumbering, translation or proxy/service exposure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### VPC-PEERING-TRANSIT-GATEWAY-AND-CLOUD-WAN-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Route scale/cost. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-transit-gateway-attachments` as one read-only checkpoint, not the whole diagnosis. attachment, processing, inter-Region and operations cost grow with hub scope. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
