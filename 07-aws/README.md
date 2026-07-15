# AWS interview curriculum tree

<!-- child-topic-toc:start -->
## Table of contents and deeper notes

This parent note explains how the child topics work together. Follow each child link for the deeper mechanism, real commands/configuration, hands-on practice, authoritative documentation, and its local interview bank.

- [Ai Platform](ai-platform/README.md) — [questions and answers](ai-platform/questions-and-answers.md)
- [Compute](compute/README.md) — [questions and answers](compute/questions-and-answers.md)
- [Containers](containers/README.md) — [questions and answers](containers/questions-and-answers.md)
- [Databases](databases/README.md) — [questions and answers](databases/questions-and-answers.md)
- [Foundations](foundations/README.md) — [questions and answers](foundations/questions-and-answers.md)
- [Infrastructure Delivery](infrastructure-delivery/README.md) — [questions and answers](infrastructure-delivery/questions-and-answers.md)
- [Load Balancing](load-balancing/README.md) — [questions and answers](load-balancing/questions-and-answers.md)
- [Messaging Serverless](messaging-serverless/README.md) — [questions and answers](messaging-serverless/questions-and-answers.md)
- [Networking](networking/README.md) — [questions and answers](networking/questions-and-answers.md)
- [Security Operations](security-operations/README.md) — [questions and answers](security-operations/questions-and-answers.md)
- [Storage](storage/README.md) — [questions and answers](storage/questions-and-answers.md)
<!-- child-topic-toc:end -->
AWS interview answers should connect a request to identities, network paths, compute, data, telemetry, failure domains, and cost. Do not answer with isolated service definitions. Begin with the shared-responsibility model and account boundary; choose a managed service only after stating requirements and operational trade-offs.

## Complete tree for this role

```text
AWS
├── Foundation and governance
│   ├── Regions, AZs, edge/Local Zones/Wavelength, quotas
│   ├── Organizations, accounts, OUs, SCPs, Control Tower/landing zones
│   ├── IAM policy evaluation, roles, boundaries, resource policies
│   ├── STS, Identity Center, SAML/OIDC, web identity, cross-account access
│   └── tags, inventory, Config, governance and cost allocation
├── Networking
│   ├── VPC, CIDR/IPAM, public/private/isolated subnets, route tables, IGW
│   ├── security groups, NACLs, DNS/DHCP, Flow Logs, Reachability Analyzer
│   ├── NAT, IPv6 egress, endpoints/PrivateLink and centralized egress
│   ├── peering, Transit Gateway, Cloud WAN, VPC sharing
│   ├── Site-to-Site VPN, Client VPN, Direct Connect, BGP and hybrid DNS
│   └── Route 53 hosted zones, Resolver, health checks and routing policies
├── Compute
│   ├── EC2 families/architectures, Nitro, lifecycle/status checks
│   ├── AMIs, Image Builder/Packer, golden image qualification
│   ├── ENIs/EIPs, enhanced networking/EFA, placement groups
│   ├── instance profiles, IMDSv2, SSM, host/volume security
│   ├── On-Demand, Spot, Savings Plans, RIs, Hosts, reservations/blocks
│   └── Auto Scaling templates, policies, refresh, lifecycle and rebalancing
├── Load balancing and global traffic
│   ├── ALB: HTTP/gRPC/WebSocket routing, authentication, WAF, weighted groups
│   ├── NLB: TCP/UDP/TLS, static IP, source IP, long connections, PrivateLink
│   ├── GWLB: transparent GENEVE appliance fleets and symmetric routing
│   ├── CLB migration, Route 53, CloudFront and Global Accelerator
│   └── health checks, draining, cross-zone behavior, logs and 4xx/5xx diagnosis
├── Storage and data protection
│   ├── S3 object/version/encryption/policy/lifecycle/replication/events
│   ├── EBS types/snapshots/encryption/IOPS/throughput/queue depth
│   ├── EFS NFS/mount targets/access points/performance/throughput
│   ├── FSx Lustre/ONTAP/Windows/OpenZFS
│   └── AWS Backup plans/vaults/lock/cross-account/region and restore tests
├── Containers
│   ├── ECR scanning/signing/immutability/replication/cache/retention
│   ├── ECS tasks/services/Fargate/capacity providers/deployments/discovery
│   ├── EKS control plane/nodes/Fargate/add-ons/access/IRSA/Pod Identity
│   ├── VPC CNI, CSI, load balancer controller, upgrades and observability
│   └── managed groups, Karpenter/Auto Mode, Spot/GPU pools and scale-from-zero
├── Databases, cache, search, messaging and serverless
│   ├── RDS/Aurora availability, replicas, backups, proxies and connection limits
│   ├── DynamoDB key design/capacity/indexes/streams/transactions/global tables
│   ├── ElastiCache Valkey/Redis/Memcached and OpenSearch/vector search
│   ├── SQS/SNS/EventBridge/Step Functions/Kinesis/MSK delivery semantics
│   └── Lambda cold starts/concurrency/events/VPC/idempotency and API Gateway
├── Security and operations
│   ├── KMS/envelope encryption/policies/grants; Secrets Manager/Parameter Store
│   ├── ACM/WAF/Shield; GuardDuty/Security Hub/Inspector/Macie/Detective
│   ├── CloudTrail/Config/Access Analyzer and multi-account response
│   ├── CloudWatch/X-Ray/Application Signals/Container Insights
│   └── Systems Manager inventory/session/patch/automation/OpsCenter
├── Infrastructure delivery
│   ├── CloudFormation stacks/StackSets/change sets/drift/rollback
│   ├── CDK constructs/synthesis/bootstrapping and escape hatches
│   ├── CodeBuild/CodePipeline/CodeDeploy and blue-green delivery
│   └── Service Catalog/Proton and governed self-service
└── AI platform
    ├── Bedrock models/inference profiles/guardrails/knowledge bases/agents/evals
    ├── SageMaker jobs/pipelines/registry/endpoints/autoscaling/monitoring
    ├── EKS GPU inference/training, KServe/vLLM/Triton, EFA and model caches
    ├── GPU instances, Inferentia/Trainium/Neuron and compatibility
    └── quotas/capacity, tenancy, telemetry, data controls and unit economics
```

## Cross-cutting decision sequence

1. **Account and identity:** which account owns it, which principal acts, and which SCP/boundary/resource policy can deny it?
2. **Network path:** source/destination, IP family, subnet/route, SG/NACL, NAT/endpoint/DNS, load balancer and target.
3. **State and failure domain:** what state exists, in which AZ/Region/account, how replicated, and what are RPO/RTO?
4. **Delivery:** desired state, artifact provenance, approvals, drift, rollout and rollback.
5. **Operations:** SLI/SLO, metrics/logs/traces/audit, alert owner, runbook and restore test.
6. **Economics:** allocation tags, unit cost, fixed/variable cost, commitment, egress/NAT/telemetry cost, quota and budget guardrails.

## Common traps

- “Private subnet” means no direct route to an internet gateway; it does not mean no egress or no public IP by itself.
- An IAM allow is not sufficient if a resource policy, permissions boundary, session policy, SCP, VPC endpoint policy, or explicit deny blocks the request.
- Multi-AZ and read scaling solve different problems; backups and tested restores are still required.
- Security groups are stateful; NACLs are stateless. Neither repairs a wrong route or DNS response.
- Auto Scaling group health, load-balancer target health, and EC2 status checks are different signals.
- S3 is an object store, not a POSIX filesystem. EBS is AZ-scoped block storage; EFS is regional NFS.
- Retries require timeouts, backoff/jitter, idempotency, a total retry budget, and overload awareness.
- Spot discounts do not make interruption-sensitive stateful or tightly coupled inference automatically safe.
- Cross-Region inference/replication can affect residency and policy even when marketed as a reliability feature.
- Quotas and physical GPU capacity are different constraints; a raised quota does not guarantee available inventory.
