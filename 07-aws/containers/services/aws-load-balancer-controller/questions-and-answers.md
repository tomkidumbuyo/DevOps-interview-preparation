# AWS Load Balancer Controller — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-LOAD-BALANCER-CONTROLLER-JN-01

- [ ] **Question:** What is Ingress reconciliation, and why does it matter in AWS Load Balancer Controller?

**Answer:** annotations/spec/class generate ALB listeners/rules/target groups. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LOAD-BALANCER-CONTROLLER-JN-02

- [ ] **Question:** What is Service LoadBalancer, and why does it matter in AWS Load Balancer Controller?

**Answer:** controller provisions NLB behavior from Service annotations/spec. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LOAD-BALANCER-CONTROLLER-JN-03

- [ ] **Question:** What is Target type ip, and why does it matter in AWS Load Balancer Controller?

**Answer:** registers Pod IPs directly and depends on VPC routability/readiness. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LOAD-BALANCER-CONTROLLER-JN-04

- [ ] **Question:** What is Target type instance, and why does it matter in AWS Load Balancer Controller?

**Answer:** registers nodes/NodePorts and adds another data-plane hop. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LOAD-BALANCER-CONTROLLER-JN-05

- [ ] **Question:** What is IngressGroup, and why does it matter in AWS Load Balancer Controller?

**Answer:** shares an ALB across Ingresses and expands who can change listener rules. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LOAD-BALANCER-CONTROLLER-JN-06

- [ ] **Question:** What is Subnet discovery, and why does it matter in AWS Load Balancer Controller?

**Answer:** tags/explicit subnets determine AZ/scheme and can fail silently through events. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LOAD-BALANCER-CONTROLLER-JN-07

- [ ] **Question:** What is IAM workload role, and why does it matter in AWS Load Balancer Controller?

**Answer:** controller requires broad-looking but bounded ELB/EC2/ACM/WAF/tag actions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LOAD-BALANCER-CONTROLLER-JN-08

- [ ] **Code:** **Question:** What does `aws elbv2 describe-target-health --target-group-arn TG_ARN` help you verify for AWS Load Balancer Controller?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: ACM discovery/ARN/listener policy and host rules must align.

### AWS-LOAD-BALANCER-CONTROLLER-JN-09

- [ ] **Code:** **Question:** What does `kubectl get ingress,service -A` help you verify for AWS Load Balancer Controller?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: controller cleanup can block Kubernetes deletion when AWS/API/IAM fails.

### AWS-LOAD-BALANCER-CONTROLLER-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe ingress NAME -n NS` help you verify for AWS Load Balancer Controller?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: reconcile errors plus AWS target health locate desired-vs-cloud drift.

## Junior — procedural and command questions

### AWS-LOAD-BALANCER-CONTROLLER-JP-01

- [ ] **Code:** **Question:** A basic Ingress reconciliation check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ingress,service -A` and capture exact status/reason/request ID. annotations/spec/class generate ALB listeners/rules/target groups. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LOAD-BALANCER-CONTROLLER-JP-02

- [ ] **Question:** A basic Service LoadBalancer check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe ingress NAME -n NS` and capture exact status/reason/request ID. controller provisions NLB behavior from Service annotations/spec. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LOAD-BALANCER-CONTROLLER-JP-03

- [ ] **Question:** A basic Target type ip check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/aws-load-balancer-controller --since=30m` and capture exact status/reason/request ID. registers Pod IPs directly and depends on VPC routability/readiness. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LOAD-BALANCER-CONTROLLER-JP-04

- [ ] **Code:** **Question:** A basic Target type instance check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-target-health --target-group-arn TG_ARN` and capture exact status/reason/request ID. registers nodes/NodePorts and adds another data-plane hop. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LOAD-BALANCER-CONTROLLER-JP-05

- [ ] **Question:** A basic IngressGroup check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ingress,service -A` and capture exact status/reason/request ID. shares an ALB across Ingresses and expands who can change listener rules. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LOAD-BALANCER-CONTROLLER-JP-06

- [ ] **Question:** A basic Subnet discovery check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe ingress NAME -n NS` and capture exact status/reason/request ID. tags/explicit subnets determine AZ/scheme and can fail silently through events. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LOAD-BALANCER-CONTROLLER-JP-07

- [ ] **Code:** **Question:** A basic IAM workload role check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/aws-load-balancer-controller --since=30m` and capture exact status/reason/request ID. controller requires broad-looking but bounded ELB/EC2/ACM/WAF/tag actions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LOAD-BALANCER-CONTROLLER-JP-08

- [ ] **Question:** A basic Certificate/TLS check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-target-health --target-group-arn TG_ARN` and capture exact status/reason/request ID. ACM discovery/ARN/listener policy and host rules must align. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LOAD-BALANCER-CONTROLLER-JP-09

- [ ] **Question:** A basic Finalizers check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ingress,service -A` and capture exact status/reason/request ID. controller cleanup can block Kubernetes deletion when AWS/API/IAM fails. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LOAD-BALANCER-CONTROLLER-JP-10

- [ ] **Code:** **Question:** A basic Controller events/logs check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe ingress NAME -n NS` and capture exact status/reason/request ID. reconcile errors plus AWS target health locate desired-vs-cloud drift. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-LOAD-BALANCER-CONTROLLER-MN-01

- [ ] **Question:** Compare Ingress reconciliation with Service LoadBalancer. When would each change your design?

**Answer:** Ingress reconciliation: annotations/spec/class generate ALB listeners/rules/target groups. Service LoadBalancer: controller provisions NLB behavior from Service annotations/spec. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LOAD-BALANCER-CONTROLLER-MN-02

- [ ] **Question:** Compare Service LoadBalancer with Target type ip. When would each change your design?

**Answer:** Service LoadBalancer: controller provisions NLB behavior from Service annotations/spec. Target type ip: registers Pod IPs directly and depends on VPC routability/readiness. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LOAD-BALANCER-CONTROLLER-MN-03

- [ ] **Question:** Compare Target type ip with Target type instance. When would each change your design?

**Answer:** Target type ip: registers Pod IPs directly and depends on VPC routability/readiness. Target type instance: registers nodes/NodePorts and adds another data-plane hop. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LOAD-BALANCER-CONTROLLER-MN-04

- [ ] **Configuration review:** **Question:** Compare Target type instance with IngressGroup. When would each change your design?

**Answer:** Target type instance: registers nodes/NodePorts and adds another data-plane hop. IngressGroup: shares an ALB across Ingresses and expands who can change listener rules. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LOAD-BALANCER-CONTROLLER-MN-05

- [ ] **Question:** Compare IngressGroup with Subnet discovery. When would each change your design?

**Answer:** IngressGroup: shares an ALB across Ingresses and expands who can change listener rules. Subnet discovery: tags/explicit subnets determine AZ/scheme and can fail silently through events. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LOAD-BALANCER-CONTROLLER-MN-06

- [ ] **Question:** Compare Subnet discovery with IAM workload role. When would each change your design?

**Answer:** Subnet discovery: tags/explicit subnets determine AZ/scheme and can fail silently through events. IAM workload role: controller requires broad-looking but bounded ELB/EC2/ACM/WAF/tag actions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LOAD-BALANCER-CONTROLLER-MN-07

- [ ] **Configuration review:** **Question:** Compare IAM workload role with Certificate/TLS. When would each change your design?

**Answer:** IAM workload role: controller requires broad-looking but bounded ELB/EC2/ACM/WAF/tag actions. Certificate/TLS: ACM discovery/ARN/listener policy and host rules must align. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LOAD-BALANCER-CONTROLLER-MN-08

- [ ] **Question:** Compare Certificate/TLS with Finalizers. When would each change your design?

**Answer:** Certificate/TLS: ACM discovery/ARN/listener policy and host rules must align. Finalizers: controller cleanup can block Kubernetes deletion when AWS/API/IAM fails. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LOAD-BALANCER-CONTROLLER-MN-09

- [ ] **Question:** Compare Finalizers with Controller events/logs. When would each change your design?

**Answer:** Finalizers: controller cleanup can block Kubernetes deletion when AWS/API/IAM fails. Controller events/logs: reconcile errors plus AWS target health locate desired-vs-cloud drift. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LOAD-BALANCER-CONTROLLER-MN-10

- [ ] **Configuration review:** **Question:** Compare Controller events/logs with Ingress reconciliation. When would each change your design?

**Answer:** Controller events/logs: reconcile errors plus AWS target health locate desired-vs-cloud drift. Ingress reconciliation: annotations/spec/class generate ALB listeners/rules/target groups. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-LOAD-BALANCER-CONTROLLER-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Ingress reconciliation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ingress,service -A` plus recent events/changes, then correlate the service-specific SLI. annotations/spec/class generate ALB listeners/rules/target groups. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LOAD-BALANCER-CONTROLLER-MP-02

- [ ] **Question:** Production is degraded around Service LoadBalancer; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe ingress NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. controller provisions NLB behavior from Service annotations/spec. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LOAD-BALANCER-CONTROLLER-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Target type ip; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/aws-load-balancer-controller --since=30m` plus recent events/changes, then correlate the service-specific SLI. registers Pod IPs directly and depends on VPC routability/readiness. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LOAD-BALANCER-CONTROLLER-MP-04

- [ ] **Question:** Production is degraded around Target type instance; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-target-health --target-group-arn TG_ARN` plus recent events/changes, then correlate the service-specific SLI. registers nodes/NodePorts and adds another data-plane hop. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LOAD-BALANCER-CONTROLLER-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around IngressGroup; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ingress,service -A` plus recent events/changes, then correlate the service-specific SLI. shares an ALB across Ingresses and expands who can change listener rules. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LOAD-BALANCER-CONTROLLER-MP-06

- [ ] **Question:** Production is degraded around Subnet discovery; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe ingress NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. tags/explicit subnets determine AZ/scheme and can fail silently through events. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LOAD-BALANCER-CONTROLLER-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around IAM workload role; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/aws-load-balancer-controller --since=30m` plus recent events/changes, then correlate the service-specific SLI. controller requires broad-looking but bounded ELB/EC2/ACM/WAF/tag actions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LOAD-BALANCER-CONTROLLER-MP-08

- [ ] **Question:** Production is degraded around Certificate/TLS; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-target-health --target-group-arn TG_ARN` plus recent events/changes, then correlate the service-specific SLI. ACM discovery/ARN/listener policy and host rules must align. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LOAD-BALANCER-CONTROLLER-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Finalizers; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ingress,service -A` plus recent events/changes, then correlate the service-specific SLI. controller cleanup can block Kubernetes deletion when AWS/API/IAM fails. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LOAD-BALANCER-CONTROLLER-MP-10

- [ ] **Question:** Production is degraded around Controller events/logs; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe ingress NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. reconcile errors plus AWS target health locate desired-vs-cloud drift. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-LOAD-BALANCER-CONTROLLER-SN-01

- [ ] **Question:** Design a production AWS Load Balancer Controller capability where Ingress reconciliation, Target type instance and IAM workload role are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: annotations/spec/class generate ALB listeners/rules/target groups. registers nodes/NodePorts and adds another data-plane hop. controller requires broad-looking but bounded ELB/EC2/ACM/WAF/tag actions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LOAD-BALANCER-CONTROLLER-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Load Balancer Controller capability where Service LoadBalancer, IngressGroup and Certificate/TLS are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controller provisions NLB behavior from Service annotations/spec. shares an ALB across Ingresses and expands who can change listener rules. ACM discovery/ARN/listener policy and host rules must align. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LOAD-BALANCER-CONTROLLER-SN-03

- [ ] **Question:** Design a production AWS Load Balancer Controller capability where Target type ip, Subnet discovery and Finalizers are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: registers Pod IPs directly and depends on VPC routability/readiness. tags/explicit subnets determine AZ/scheme and can fail silently through events. controller cleanup can block Kubernetes deletion when AWS/API/IAM fails. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LOAD-BALANCER-CONTROLLER-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Load Balancer Controller capability where Target type instance, IAM workload role and Controller events/logs are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: registers nodes/NodePorts and adds another data-plane hop. controller requires broad-looking but bounded ELB/EC2/ACM/WAF/tag actions. reconcile errors plus AWS target health locate desired-vs-cloud drift. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LOAD-BALANCER-CONTROLLER-SN-05

- [ ] **Question:** Design a production AWS Load Balancer Controller capability where IngressGroup, Certificate/TLS and Ingress reconciliation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: shares an ALB across Ingresses and expands who can change listener rules. ACM discovery/ARN/listener policy and host rules must align. annotations/spec/class generate ALB listeners/rules/target groups. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LOAD-BALANCER-CONTROLLER-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Load Balancer Controller capability where Subnet discovery, Finalizers and Service LoadBalancer are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tags/explicit subnets determine AZ/scheme and can fail silently through events. controller cleanup can block Kubernetes deletion when AWS/API/IAM fails. controller provisions NLB behavior from Service annotations/spec. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LOAD-BALANCER-CONTROLLER-SN-07

- [ ] **Question:** Design a production AWS Load Balancer Controller capability where IAM workload role, Controller events/logs and Target type ip are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controller requires broad-looking but bounded ELB/EC2/ACM/WAF/tag actions. reconcile errors plus AWS target health locate desired-vs-cloud drift. registers Pod IPs directly and depends on VPC routability/readiness. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LOAD-BALANCER-CONTROLLER-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Load Balancer Controller capability where Certificate/TLS, Ingress reconciliation and Target type instance are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ACM discovery/ARN/listener policy and host rules must align. annotations/spec/class generate ALB listeners/rules/target groups. registers nodes/NodePorts and adds another data-plane hop. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LOAD-BALANCER-CONTROLLER-SN-09

- [ ] **Question:** Design a production AWS Load Balancer Controller capability where Finalizers, Service LoadBalancer and IngressGroup are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controller cleanup can block Kubernetes deletion when AWS/API/IAM fails. controller provisions NLB behavior from Service annotations/spec. shares an ALB across Ingresses and expands who can change listener rules. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LOAD-BALANCER-CONTROLLER-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Load Balancer Controller capability where Controller events/logs, Target type ip and Subnet discovery are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reconcile errors plus AWS target health locate desired-vs-cloud drift. registers Pod IPs directly and depends on VPC routability/readiness. tags/explicit subnets determine AZ/scheme and can fail silently through events. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-LOAD-BALANCER-CONTROLLER-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ingress reconciliation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ingress,service -A` as one read-only checkpoint, not the whole diagnosis. annotations/spec/class generate ALB listeners/rules/target groups. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LOAD-BALANCER-CONTROLLER-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service LoadBalancer. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe ingress NAME -n NS` as one read-only checkpoint, not the whole diagnosis. controller provisions NLB behavior from Service annotations/spec. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LOAD-BALANCER-CONTROLLER-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Target type ip. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/aws-load-balancer-controller --since=30m` as one read-only checkpoint, not the whole diagnosis. registers Pod IPs directly and depends on VPC routability/readiness. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LOAD-BALANCER-CONTROLLER-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Target type instance. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-target-health --target-group-arn TG_ARN` as one read-only checkpoint, not the whole diagnosis. registers nodes/NodePorts and adds another data-plane hop. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LOAD-BALANCER-CONTROLLER-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IngressGroup. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ingress,service -A` as one read-only checkpoint, not the whole diagnosis. shares an ALB across Ingresses and expands who can change listener rules. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LOAD-BALANCER-CONTROLLER-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Subnet discovery. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe ingress NAME -n NS` as one read-only checkpoint, not the whole diagnosis. tags/explicit subnets determine AZ/scheme and can fail silently through events. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LOAD-BALANCER-CONTROLLER-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IAM workload role. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/aws-load-balancer-controller --since=30m` as one read-only checkpoint, not the whole diagnosis. controller requires broad-looking but bounded ELB/EC2/ACM/WAF/tag actions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LOAD-BALANCER-CONTROLLER-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Certificate/TLS. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-target-health --target-group-arn TG_ARN` as one read-only checkpoint, not the whole diagnosis. ACM discovery/ARN/listener policy and host rules must align. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LOAD-BALANCER-CONTROLLER-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Finalizers. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ingress,service -A` as one read-only checkpoint, not the whole diagnosis. controller cleanup can block Kubernetes deletion when AWS/API/IAM fails. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LOAD-BALANCER-CONTROLLER-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Controller events/logs. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe ingress NAME -n NS` as one read-only checkpoint, not the whole diagnosis. reconcile errors plus AWS target health locate desired-vs-cloud drift. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
