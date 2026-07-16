#!/usr/bin/env python3
"""Generate the normalized AWS/Kubernetes leaf folders and separate Q&A banks.

The source catalog is intentionally committed next to the generator so coverage is
reviewable. Generated Markdown is deterministic and may be regenerated safely.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from note_explanations import (
    answer_evidence,
    answer_mechanism,
    capability_table,
    command_explanation,
    concept_explanations,
    flow_diagram,
    history_text,
    junior_intro,
    practice_session,
    usable_description,
    worked_example,
)


ROOT = Path(__file__).resolve().parents[1]
NUMBER_PREFIX = re.compile(r"^\d{2,3}-(.+)$")


def unnumbered(name: str) -> str:
    match = NUMBER_PREFIX.match(name)
    return match.group(1) if match else name


def numbered_path(path: Path) -> Path:
    """Resolve unnumbered generator paths into the existing numbered tree."""
    try:
        relative = path.relative_to(ROOT)
    except ValueError:
        return path
    current = ROOT
    for part in relative.parts:
        exact = current / part
        if exact.exists():
            current = exact
            continue
        matches = (
            [child for child in current.iterdir() if child.is_dir() and unnumbered(child.name) == part]
            if current.exists()
            else []
        )
        current = matches[0] if len(matches) == 1 else exact
    return current


@dataclass(frozen=True)
class Leaf:
    area: str
    branch: str
    slug: str
    title: str
    purpose: str
    concepts: tuple[str, ...]
    commands: tuple[str, ...]
    docs: str


def C(*items: str) -> tuple[str, ...]:
    """Concept entries use `name — explanation` to keep the catalog readable."""
    return items


AWS: list[Leaf] = [
    Leaf("07-aws", "foundations", "iam", "AWS IAM", "Evaluate and govern who may perform which AWS action on which resource under which request conditions.", C(
        "Principals — users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles",
        "Identity policies — attached policies grant or deny actions to a principal within the rest of the policy intersection",
        "Resource policies — supported resources can trust principals directly and express cross-account or service access",
        "Explicit deny — any applicable explicit deny overrides allows and is the first guardrail to search during diagnosis",
        "Permissions boundaries — cap identity-policy permissions without granting actions themselves",
        "Session policies — further restrict an assumed-role session and can explain access that differs from the base role",
        "Condition keys — bind access to organization, source network, tags, MFA, audience and other request context",
        "Access Analyzer — validates policies and analyzes external/internal access paths for supported resources",
        "Least privilege — start from task/resource/condition needs, observe actual use, remove unused access and review exceptions",
        "PassRole escalation — permission to attach a powerful role to a service can be equivalent to using that role indirectly",
    ), ("aws sts get-caller-identity", "aws iam simulate-principal-policy --policy-source-arn ROLE_ARN --action-names ACTION", "aws accessanalyzer validate-policy --policy-document file://policy.json --policy-type IDENTITY_POLICY", "aws iam get-account-authorization-details"), "https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html"),
    Leaf("07-aws", "foundations", "organizations", "AWS Organizations", "Use accounts and organizational guardrails as ownership, isolation, governance and billing boundaries.", C(
        "Management account — owns the organization and must be tightly protected rather than used for workloads",
        "Member accounts — separate workloads, environments, teams and blast radii with independent quotas and root identities",
        "Organizational units — group accounts for policy inheritance and lifecycle rather than acting as runtime resources",
        "Service Control Policies — define maximum permissions for member principals but grant no permission",
        "Delegated administrator — lets a security/platform account operate supported organization-wide services",
        "Consolidated billing — aggregates charges and commitment sharing while accounts retain usage ownership",
        "Organization trails/config — centralize immutable audit and configuration history outside workload accounts",
        "Account vending — creates standardized accounts with contacts, identity, networks, logs, budgets and owners",
        "Resource Control Policies — constrain resource-side permissions for supported services within the organization",
        "Break-glass — tested emergency access must remain narrow, monitored and independent of a single federation failure",
    ), ("aws organizations describe-organization", "aws organizations list-roots", "aws organizations list-organizational-units-for-parent --parent-id ROOT_ID", "aws organizations list-policies-for-target --target-id ACCOUNT_ID --filter SERVICE_CONTROL_POLICY"), "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html"),
    Leaf("07-aws", "foundations", "sts-identity-center", "AWS STS, federation and IAM Identity Center", "Issue short-lived human, workload, CI and cross-account sessions with explicit trust and attribution.", C(
        "AssumeRole — exchanges an authenticated caller for temporary role credentials subject to trust and permissions",
        "Trust policy — controls which principal and conditions may assume a role",
        "Role permissions — control what the resulting session can do after assumption",
        "External ID — mitigates confused-deputy risk for third-party cross-account role assumption",
        "OIDC web identity — exchanges a signed workload token with issuer, audience and subject conditions",
        "SAML federation — maps enterprise identity assertions into AWS role sessions",
        "Identity Center — centralizes workforce assignments and permission sets across accounts",
        "Role chaining — assumes another role from a role session and has duration/attribution constraints",
        "Session tags/source identity — propagate authorized attribution/context into policy and audit",
        "Credential refresh — applications must refresh before expiry and avoid persisting temporary credentials",
    ), ("aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME", "aws sts decode-authorization-message --encoded-message MESSAGE", "aws sso login --profile PROFILE", "aws configure export-credentials --profile PROFILE"), "https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html"),
    Leaf("07-aws", "foundations", "control-tower-governance", "AWS Control Tower, tagging, quotas and governance", "Create a governed landing zone and continuously detect ownership, policy, drift, quota and cost risks.", C(
        "Landing zone — standardized multi-account identity, logging, security and network foundation",
        "Control Tower controls — preventive, detective and proactive controls differ in enforcement timing and mechanism",
        "Tag taxonomy — owner, environment, data class, cost center and lifecycle fields support operations and allocation",
        "Tag policies — standardize allowed tag values but may not enforce every resource creation path alone",
        "AWS Config — records supported configuration history and evaluates compliance rules",
        "CloudTrail — records account/API activity and must be centralized/protected",
        "Service quotas — API/resource ceilings need inventory, forecast, alert and early increase requests",
        "AWS Resource Explorer/Config aggregators — provide cross-account resource inventory with service-specific coverage",
        "Budget controls — combine alerts/anomaly detection with service/platform quotas because budgets are not universal hard stops",
        "Drift remediation — decide source of truth and use reviewed automation rather than destructive automatic correction everywhere",
    ), ("aws controltower list-enabled-controls --target-identifier OU_ARN", "aws configservice describe-compliance-by-config-rule", "aws service-quotas list-service-quotas --service-code SERVICE", "aws resource-explorer-2 search --query-string 'tag.key:Owner'"), "https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html"),

    Leaf("07-aws", "networking", "vpc", "Amazon VPC", "Design regional IP, subnet and routing domains and reason about every forward and return packet path.", C(
        "VPC CIDR — regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth",
        "Subnet — AZ-scoped address range whose route table and address behavior determine public/private/isolated use",
        "Route table — longest-prefix match selects a next hop such as local, IGW, NAT, TGW, peering or endpoint",
        "Internet gateway — VPC edge target that supports public internet routing for appropriately addressed resources",
        "Egress-only internet gateway — permits initiated IPv6 egress while blocking unsolicited inbound routing",
        "ENI — carries addresses, security groups and attachment state for compute and managed-service data planes",
        "IPAM — plans, allocates and audits address space across accounts/Regions",
        "DHCP options — influence resolver/domain/NTP settings delivered to instances",
        "VPC Flow Logs — capture accepted/rejected flow metadata, not packet payload or every application event",
        "Reachability Analyzer — evaluates configured network path models and complements runtime packet evidence",
    ), ("aws ec2 describe-vpcs --vpc-ids VPC_ID", "aws ec2 describe-subnets --filters Name=vpc-id,Values=VPC_ID", "aws ec2 describe-route-tables --filters Name=vpc-id,Values=VPC_ID", "aws ec2 start-network-insights-analysis --network-insights-path-id PATH_ID"), "https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html"),
    Leaf("07-aws", "networking", "security-groups-nacls", "Security groups and network ACLs", "Apply stateful ENI and stateless subnet filtering without confusing filters with routing or identity.", C(
        "Security group state — allowed connections automatically permit tracked return traffic",
        "Security group reference — supported paths can allow traffic from ENIs associated with another group",
        "Outbound rules — restrict initiated egress and influence return assumptions only through stateful tracking",
        "NACL ordering — lowest numbered matching allow/deny rule wins",
        "NACL statelessness — return traffic and ephemeral ports require explicit rules in both directions",
        "Default groups/ACLs — defaults may be broad and should not become undocumented production policy",
        "Ephemeral ports — client operating systems choose source ports that stateless rules must accommodate",
        "Rule quotas — excessive per-tenant rules can hit limits and slow operations",
        "Least-path access — allow the exact source/destination/protocol/port and document owner/purpose",
        "Flow evidence — rejected flow logs, Reachability Analyzer and packet capture distinguish policy from listener failure",
    ), ("aws ec2 describe-security-groups --group-ids SG_ID", "aws ec2 describe-network-acls --network-acl-ids ACL_ID", "aws ec2 describe-network-interfaces --filters Name=group-id,Values=SG_ID", "aws ec2 describe-flow-logs"), "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html"),
    Leaf("07-aws", "networking", "nat-egress", "NAT and egress architecture", "Provide resilient, attributable and cost-controlled outbound access without hidden port or AZ failure.", C(
        "NAT gateway — managed AZ-scoped IPv4 translation with hourly and data-processing cost",
        "NAT instance — customer-managed translation with patching, throughput and failover responsibility",
        "Centralized egress — shared inspection/control reduces duplication but adds routing, blast radius and processing cost",
        "Per-AZ egress — aligns failure domains and avoids cross-AZ dependency at higher fixed cost",
        "SNAT port exhaustion — many connections to the same destination can exhaust translation tuples",
        "Egress proxy — authenticates/filters/logs application destinations but needs client/protocol support",
        "IPv6 egress — uses routable addresses and egress-only filtering rather than primary IPv4 NAT semantics",
        "Service endpoints — keep supported service traffic off NAT and can reduce exposure/cost",
        "Domain allowlisting — DNS-to-IP change and encrypted protocols make naive IP lists fragile",
        "Egress telemetry — bytes, errors, ports, destinations and tenant attribution reveal cost and abuse",
    ), ("aws ec2 describe-nat-gateways", "aws cloudwatch get-metric-data --metric-data-queries file://nat-metrics.json --start-time START --end-time END", "aws ec2 describe-route-tables", "aws ec2 describe-vpc-endpoints"), "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html"),
    Leaf("07-aws", "networking", "endpoints-privatelink", "VPC endpoints and AWS PrivateLink", "Reach AWS or producer services privately with explicit DNS, endpoint, resource and identity policy.", C(
        "Gateway endpoint — route-table target for supported services such as S3/DynamoDB without endpoint ENIs",
        "Interface endpoint — PrivateLink ENIs in subnets with security groups and per-hour/data cost",
        "Private DNS — maps standard service hostname to endpoint addresses inside associated VPCs",
        "Endpoint policy — constrains calls through the endpoint but does not grant principal/resource permission",
        "Endpoint service — NLB-backed producer service exposed privately to approved consumers",
        "Acceptance/permissions — service owners control which accounts/principals may create endpoint connections",
        "Zonal design — endpoint ENIs and DNS answers must align with AZ resilience and client paths",
        "Resource policy conditions — source VPC/endpoint conditions can constrain data access under known service semantics",
        "Hybrid DNS/path — on-prem clients need Resolver/routing to use private endpoints correctly",
        "Cost comparison — endpoint hours/data versus NAT processing/cross-AZ/exposure depends on traffic and topology",
    ), ("aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID", "aws ec2 describe-vpc-endpoint-services", "aws ec2 describe-vpc-endpoint-connections", "dig SERVICE.REGION.amazonaws.com"), "https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html"),
    Leaf("07-aws", "networking", "peering-tgw-cloudwan", "VPC peering, Transit Gateway and Cloud WAN", "Connect many VPCs/accounts/Regions under explicit routing, segmentation, ownership and scale constraints.", C(
        "VPC peering — direct non-transitive connectivity that requires non-overlap and routes on both sides",
        "Transit Gateway attachments — connect VPC, VPN, Direct Connect gateway or peering into a routed hub",
        "TGW route association — selects the route table used to route traffic entering an attachment",
        "TGW propagation — inserts learned/attachment routes into selected route tables",
        "Segmentation — separate production, shared services, inspection and customer route domains",
        "Appliance mode — preserves flow symmetry through stateful inspection appliances in supported topology",
        "Inter-Region peering — connects TGWs with explicit routes and data-transfer considerations",
        "Cloud WAN policy — declaratively manages global core network segments and attachments",
        "Overlapping CIDR — blocks ordinary routing and may require renumbering, translation or proxy/service exposure",
        "Route scale/cost — attachment, processing, inter-Region and operations cost grow with hub scope",
    ), ("aws ec2 describe-vpc-peering-connections", "aws ec2 describe-transit-gateway-attachments", "aws ec2 search-transit-gateway-routes --transit-gateway-route-table-id TGW_RT --filters file://filters.json", "aws networkmanager get-core-network-policy --core-network-id CORE_ID --policy-version-id VERSION"), "https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html"),
    Leaf("07-aws", "networking", "hybrid-networking", "AWS hybrid networking", "Connect customer/on-prem and AWS networks with redundant links, routing, DNS and measurable failure behavior.", C(
        "Site-to-Site VPN — redundant IPsec tunnels provide encrypted connectivity over public paths",
        "BGP — exchanges reachability and failover signals under ASN/prefix/timer policy",
        "Direct Connect — dedicated physical connectivity needs redundant locations/devices and operational lead time",
        "Direct Connect gateway — associates virtual interfaces with VPC/TGW connectivity across supported scope",
        "Client VPN — managed remote-user connectivity with identity, authorization and route design",
        "Hybrid DNS — Resolver inbound/outbound endpoints and forwarding rules bridge namespaces",
        "Redundancy — devices, tunnels, DX locations, carriers, power and routes must avoid shared failure",
        "MTU/MSS — encapsulation and path differences can black-hole large packets while small probes pass",
        "Asymmetric routing — stateful firewalls/NAT can drop return paths that choose a different link",
        "Monitoring/runbook — tunnel/BGP/route/DNS/synthetic metrics and tested failover prove design",
    ), ("aws ec2 describe-vpn-connections", "aws directconnect describe-connections", "aws ec2 describe-client-vpn-endpoints", "aws route53resolver list-resolver-endpoints"), "https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/welcome.html"),
    Leaf("07-aws", "networking", "route53", "Amazon Route 53", "Operate authoritative/private DNS, routing policy, resolver integration and health-based failover under caching.", C(
        "Hosted zone — authoritative public or VPC-associated private namespace",
        "Alias record — AWS-specific record that targets supported resources without a CNAME at the zone apex",
        "Weighted routing — probabilistically distributes DNS answers and is affected by resolver/client caching",
        "Latency routing — chooses Region from measured AWS network latency rather than application load",
        "Failover routing — health-check state selects primary/secondary answers but recovery still depends on data/service readiness",
        "TTL — balances cache/query load against change/failover responsiveness",
        "Resolver endpoints — inbound/outbound interfaces bridge VPC and external DNS with forwarding rules",
        "Split-horizon DNS — public/private views can intentionally answer differently and complicate diagnosis",
        "DNSSEC — authenticates signed DNS data; it does not encrypt queries",
        "Health checks — endpoint/calculated/CloudWatch checks need quorum, firewall and false-positive design",
    ), ("aws route53 list-hosted-zones", "aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID", "aws route53 get-health-check-status --health-check-id ID", "aws route53resolver list-resolver-rules", "dig +trace NAME"), "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html"),

    Leaf("07-aws", "compute", "ec2", "Amazon EC2", "Select, secure, operate and troubleshoot virtual machines from measured compute, memory, storage, network and accelerator needs.", C(
        "Instance family — general, compute, memory, storage and accelerator families target different bottlenecks",
        "CPU architecture — x86 and Graviton/ARM require compatible AMIs, agents and multi-architecture artifacts",
        "Nitro system — underpins modern isolation, ENA/EBS and hardware-offload capabilities",
        "Instance lifecycle — pending/running/stopping/stopped/hibernated/terminated transitions affect billing and storage",
        "Status checks — system and instance checks distinguish AWS host from guest reachability signals",
        "Instance profile — delivers temporary role credentials to the instance rather than static keys",
        "IMDSv2 — session-oriented metadata access reduces SSRF credential exposure when enforced/configured correctly",
        "ENA/EFA — enhanced networking and EFA support high throughput/low latency under compatible instances/workloads",
        "Placement groups — cluster/partition/spread strategies trade locality, scale and correlated failure",
        "Purchase/capacity — On-Demand, Spot, commitments, dedicated tenancy and reservations solve different price/capacity needs",
    ), ("aws ec2 describe-instances --instance-ids INSTANCE_ID", "aws ec2 describe-instance-status --include-all-instances", "aws ec2 describe-instance-types --instance-types TYPE", "aws ssm start-session --target INSTANCE_ID"), "https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html"),
    Leaf("07-aws", "compute", "amis-image-builder", "AMIs, Image Builder and golden images", "Produce reproducible, patched, signed and qualified machine images with safe multi-account/Region lifecycle.", C(
        "AMI — boot image metadata and snapshots define instance root and launch compatibility",
        "Golden image — centrally hardened/tested base reduces bootstrap drift and replacement time",
        "Image Builder pipeline — recipes/components/infrastructure/distribution automate build/test/copy",
        "Packer — vendor-neutral image build tool whose builders/provisioners need reproducibility and secret controls",
        "Patch baseline — determines approved updates but must be followed by regression qualification",
        "SBOM/provenance — records packages/build source and supports vulnerability/rebuild decisions",
        "Signing/approval — binds release process to an exact AMI/artifact rather than a name lookup",
        "Distribution — account sharing, KMS keys and Region copies must preserve launch/decrypt permission",
        "Canary instance/pool — validates boot, SSM, agents, workload and performance before fleet refresh",
        "Retirement — owner/reference inventory and rollback window prevent deleting still-used images/snapshots",
    ), ("aws ec2 describe-images --owners self", "aws imagebuilder list-image-pipelines", "aws imagebuilder start-image-pipeline-execution --image-pipeline-arn ARN", "aws ec2 copy-image --source-region REGION --source-image-id AMI --name NAME"), "https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html"),
    Leaf("07-aws", "compute", "ec2-auto-scaling", "EC2 Auto Scaling", "Maintain an EC2 fleet at safe capacity and roll images/configuration without losing state or traffic.", C(
        "Launch template — versions instance image/type/network/role/storage/bootstrap inputs",
        "Min/max/desired — bound fleet capacity while policies adjust desired count",
        "Target tracking — changes desired capacity to keep an aggregate metric near a target",
        "Step scaling — maps alarm breach magnitude to capacity adjustments",
        "Warm-up — prevents new instances distorting metrics before they contribute capacity",
        "Lifecycle hook — pauses launch/termination for initialization, registration, drain or checkpoint",
        "Instance refresh — replaces instances to a selected template with minimum healthy and checkpoints",
        "Mixed instances — diversifies compatible types and On-Demand/Spot allocation strategies",
        "Capacity rebalance — launches replacement on Spot rebalance recommendation before interruption",
        "Health replacement loop — wrong health/grace/bootstrap can continually destroy otherwise diagnosable instances",
    ), ("aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names ASG", "aws autoscaling describe-scaling-activities --auto-scaling-group-name ASG", "aws autoscaling start-instance-refresh --auto-scaling-group-name ASG --preferences file://preferences.json", "aws autoscaling complete-lifecycle-action --lifecycle-hook-name HOOK --auto-scaling-group-name ASG --lifecycle-action-result CONTINUE --instance-id ID"), "https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html"),

    Leaf("07-aws", "load-balancing", "alb", "Application Load Balancer", "Route HTTP, HTTPS, WebSocket and gRPC requests using content-aware rules and observable target health.", C(
        "Listener — accepts a protocol/port and default action under TLS policy/certificates",
        "Listener rule — ordered conditions on host/path/header/query/method/source select actions",
        "Target group — defines target type/protocol/port/health and deregistration behavior",
        "Health check — controls endpoint admission and should represent readiness without excessive dependency coupling",
        "Weighted target groups — split traffic for canary/blue-green while stickiness can distort percentages",
        "Authentication action — integrates supported OIDC/Cognito flows but application authorization remains necessary",
        "gRPC/WebSocket — long-lived/streaming protocols require timeout, draining and client retry alignment",
        "WAF integration — filters L7 traffic and needs tuned rules/false-positive observability",
        "Access logs — distinguish chosen rule/target timing/status and complement CloudWatch metrics/traces",
        "ELB vs target errors — generated 5xx and target 5xx point to different failure layers",
    ), ("aws elbv2 describe-load-balancers --names NAME", "aws elbv2 describe-listeners --load-balancer-arn ARN", "aws elbv2 describe-rules --listener-arn ARN", "aws elbv2 describe-target-health --target-group-arn TG_ARN"), "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html"),
    Leaf("07-aws", "load-balancing", "nlb", "Network Load Balancer", "Handle TCP, UDP and TLS flows with static zonal addresses, source-IP semantics and PrivateLink integration.", C(
        "Layer 4 flow — routing is based on connection/protocol rather than HTTP path/header semantics",
        "Static zonal addresses — one address per enabled zone can satisfy allowlists and anycast/global patterns via other services",
        "Source IP preservation — depends on target type/protocol/settings and affects security/logging/return path",
        "TLS listener — terminates TLS with certificates/policy while a TCP listener can pass TLS through",
        "UDP — health/connection assumptions differ because transport is connectionless",
        "IP targets — route to VPC/on-prem IPs under documented reachability and registration constraints",
        "ALB target — combines NLB static/private/TCP endpoint features with downstream ALB L7 routing",
        "PrivateLink — endpoint services commonly use NLB as producer data plane",
        "Long-lived connections — client/LB/target timeouts, draining and resets govern rollout behavior",
        "Zonal health/cross-zone — capacity in each enabled zone and DNS fail-away influence resilience",
    ), ("aws elbv2 describe-load-balancers --names NAME", "aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN", "aws elbv2 describe-target-health --target-group-arn TG_ARN", "openssl s_client -connect HOST:443 -servername NAME"), "https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html"),
    Leaf("07-aws", "load-balancing", "gwlb", "Gateway Load Balancer", "Insert scalable third-party/virtual appliances transparently while preserving symmetric stateful flows.", C(
        "GENEVE — encapsulates original packets and metadata between GWLB and appliances",
        "GWLB endpoint — PrivateLink-style route target that sends traffic to an appliance service",
        "Appliance target group — health/scaling determines inspection capacity",
        "Symmetric routing — both directions must traverse the same stateful inspection path",
        "Appliance mode — TGW setting helps preserve AZ/flow symmetry through appliance VPC patterns",
        "Flow stickiness — keeps a flow on a target while failures/timeout determine rehash behavior",
        "Fail-open/closed — security and availability policy must define behavior when inspection is unavailable",
        "Autoscaling — new appliance readiness/state sync/licensing must precede traffic",
        "Route insertion — subnet/TGW routes form explicit service chains and can create loops/asymmetry",
        "Observability — endpoint/GWLB/appliance/flow logs and synthetic paths locate packet loss",
    ), ("aws elbv2 describe-load-balancers", "aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=SERVICE", "aws elbv2 describe-target-health --target-group-arn TG_ARN", "aws ec2 describe-route-tables"), "https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html"),
    Leaf("07-aws", "load-balancing", "global-accelerator", "AWS Global Accelerator", "Route users through AWS anycast and network paths to healthy regional endpoints with deterministic addresses.", C(
        "Anycast IP — the same static addresses advertise globally and enter a nearby AWS edge",
        "Accelerator listener — accepts TCP/UDP port ranges and distributes to endpoint groups",
        "Endpoint group — regional endpoints, traffic dial and health/check settings",
        "Endpoint weight — shifts traffic among endpoints within a group under health/capacity policy",
        "Health failover — unhealthy endpoints/regions are removed under detection thresholds and state implications",
        "Client IP preservation — supported endpoint patterns retain source information under constraints",
        "Traffic dial — controls percentage sent to a Region for canary/maintenance/capacity",
        "ALB/NLB/EC2/EIP endpoints — supported endpoint types provide different L7/L4 and address properties",
        "DNS vs anycast — Global Accelerator reacts at network routing without waiting for client DNS TTL",
        "Residency/state — global routing must not send data to a disallowed Region or unprepared replica",
    ), ("aws globalaccelerator list-accelerators --region us-west-2", "aws globalaccelerator list-listeners --accelerator-arn ARN --region us-west-2", "aws globalaccelerator list-endpoint-groups --listener-arn ARN --region us-west-2", "aws globalaccelerator describe-endpoint-group --endpoint-group-arn ARN --region us-west-2"), "https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html"),

    Leaf("07-aws", "storage", "s3", "Amazon S3", "Store, secure, lifecycle, replicate and recover versioned objects under explicit authorization and cost controls.", C(
        "Object/key — immutable-style object bytes plus metadata are addressed by a key; prefixes are not POSIX directories",
        "Strong consistency — successful writes/deletes are reflected by subsequent reads/lists, while concurrent writers still need coordination",
        "Versioning — preserves version IDs/delete markers for recovery and is not sufficient if one principal can purge all versions",
        "Storage classes — trade access/retrieval/minimum-duration/AZ resilience and monitoring cost",
        "Lifecycle — asynchronously transitions/expires current/noncurrent versions and incomplete multipart uploads",
        "Multipart/checksum — parallel parts and integrity checks improve large transfer reliability but abandoned uploads cost money",
        "Authorization intersection — identity, bucket/access point, SCP/boundary/session, endpoint and KMS policies can all constrain",
        "Encryption — SSE-S3/KMS/DSSE/client methods differ in control, audit, quota and recovery",
        "Replication — asynchronous SRR/CRR needs versioning, IAM/KMS, existing-object/delete behavior and monitoring",
        "Events — notifications can duplicate/reorder, so consumers need idempotency and reconciliation",
    ), ("aws s3api head-object --bucket BUCKET --key KEY", "aws s3api list-object-versions --bucket BUCKET --prefix KEY", "aws s3api get-public-access-block --bucket BUCKET", "aws s3api get-bucket-replication --bucket BUCKET"), "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html"),
    Leaf("07-aws", "storage", "ebs", "Amazon EBS", "Provide AZ-scoped block storage with measured latency/IOPS/throughput, encrypted snapshots and safe expansion.", C(
        "gp3 — general SSD with independently configurable size, IOPS and throughput within limits",
        "io2 — high-performance/durability SSD for sustained I/O and supported Multi-Attach cases",
        "st1/sc1 — throughput/cold HDD choices unsuitable for boot/random latency-sensitive workloads",
        "Instance EBS bandwidth — instance attachment limits can bottleneck a provisioned volume",
        "Queue depth/I/O size — workload concurrency and block size determine realized IOPS/throughput/latency",
        "Snapshot — incremental service copy that is crash-consistent unless the application is quiesced/coordinated",
        "Encryption/KMS — volume/snapshot/copy access requires both EC2 and key permissions",
        "Fast Snapshot Restore — pre-initializes supported snapshots in selected AZs at additional cost",
        "Expansion — grow volume then partition/PV/LV/filesystem without shrinking and with rollback evidence",
        "Multi-Attach — supported volumes/instances still require a cluster-aware filesystem/application",
    ), ("aws ec2 describe-volumes --volume-ids VOLUME_ID", "aws ec2 describe-volume-status --volume-ids VOLUME_ID", "aws ec2 modify-volume --volume-id VOLUME_ID --size SIZE", "lsblk -f && iostat -xz 1"), "https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html"),
    Leaf("07-aws", "storage", "efs", "Amazon EFS", "Provide regional NFS with per-AZ mount targets, identity/permission controls and throughput-aware operations.", C(
        "Mount target — ENI per selected AZ provides NFS endpoint and security-group boundary",
        "NFS semantics — shared file access, locking, metadata and close-to-open behavior differ from object/block storage",
        "Access point — enforces root directory and POSIX identity for an application path",
        "IAM/TLS mount — helper can authenticate/encrypt supported client mount sessions",
        "Performance mode — general/max-I/O choices trade latency and scale under service constraints",
        "Throughput mode — bursting/provisioned/elastic choices affect limits and billing",
        "Lifecycle/IA — moves files based on access and incurs retrieval/transition considerations",
        "Local-AZ mount — clients should normally use a mount target in their AZ for availability/cost/latency",
        "POSIX permissions — UID/GID/mode/ACL plus access-point behavior determine file access",
        "Backup/restore — shared filesystem still needs application-consistent policy and restore testing",
    ), ("aws efs describe-file-systems", "aws efs describe-mount-targets --file-system-id FS_ID", "aws efs describe-access-points --file-system-id FS_ID", "mount | rg nfs && nfsstat -m"), "https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html"),
    Leaf("07-aws", "storage", "fsx", "Amazon FSx", "Select and operate managed Lustre, ONTAP, Windows or OpenZFS filesystems from workload semantics and performance.", C(
        "FSx for Lustre — parallel high-throughput filesystem suited to HPC/ML and optional S3 data repository integration",
        "Data repository association — imports/exports metadata/data between Lustre and S3 under explicit lifecycle",
        "FSx for ONTAP — NFS/SMB/iSCSI plus snapshots/clones/tiering for enterprise data workflows",
        "FSx for Windows — SMB/Active Directory integration for Windows applications",
        "FSx for OpenZFS — NFS and ZFS snapshot/clone/compression semantics",
        "Deployment type — scratch/persistent or single/multi-AZ options vary by filesystem and durability need",
        "Throughput/capacity — provisioned storage, throughput, SSD/metadata and cache must match I/O profile",
        "Network/DNS/security — subnets/routes/SG and directory identity are part of mount path",
        "Backup/snapshot — feature and recovery behavior differ by filesystem; test application restore",
        "Model/training cache — benchmark metadata, aggregate read, first load and node count rather than headline throughput",
    ), ("aws fsx describe-file-systems", "aws fsx describe-backups", "aws fsx describe-data-repository-associations", "lfs df -h && lfs osts"), "https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html"),
    Leaf("07-aws", "storage", "aws-backup", "AWS Backup", "Apply immutable cross-account/Region backup policy and prove application recovery through automated restore tests.", C(
        "Backup plan — schedule, window, lifecycle and copy rules define intended RPO/retention",
        "Resource selection — tags/ARNs/roles determine coverage and need inventory validation",
        "Backup vault — access/KMS/lock policies isolate recovery points from workloads",
        "Vault Lock — governance/compliance modes constrain deletion and require careful retention/legal operation",
        "Cross-account copy — reduces workload-account compromise blast radius under organization/KMS policy",
        "Cross-Region copy — addresses regional disaster while adding transfer/residency considerations",
        "Recovery point — provider-specific restore metadata and consistency determine usefulness",
        "Restore testing — scheduled restore plus application validation measures actual recovery",
        "Backup Audit Manager — produces control evidence but needs accurate framework/scope",
        "RPO/RTO evidence — job success, lag, copy and timed restore results must meet business targets",
    ), ("aws backup list-backup-plans", "aws backup list-backup-jobs", "aws backup list-recovery-points-by-backup-vault --backup-vault-name VAULT", "aws backup list-restore-testing-plans", "aws backup list-restore-jobs"), "https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html"),

    Leaf("07-aws", "containers", "ecr", "Amazon ECR", "Store and distribute immutable, scanned, signed and replicated OCI artifacts under least-privilege policy.", C(
        "Repository — regional namespace with IAM/resource policy and encryption",
        "Tag immutability — prevents overwriting release tags while deployment by digest is stronger identity",
        "Image scanning — detects known vulnerabilities and requires prioritization/rebuild rather than in-place patch",
        "Lifecycle policy — expires images by ordered selection rules and can remove rollback artifacts if careless",
        "Cross-Region/account replication — copies eligible artifacts under registry policy and KMS/access constraints",
        "Pull-through cache — mirrors upstream content and reduces availability/rate risk while requiring trust policy",
        "Authentication token — short-lived registry auth derives from AWS identity and must be refreshed",
        "Signature/provenance — external OCI artifacts/attestations bind trusted build identity to digest",
        "Repository policy — supports cross-account pulls/pushes but cannot override explicit organization denies",
        "Large image pull — layers, node cache, network/NAT and registry quota influence startup time",
    ), ("aws ecr describe-repositories", "aws ecr describe-images --repository-name REPO", "aws ecr get-lifecycle-policy --repository-name REPO", "aws ecr get-login-password | docker login --username AWS --password-stdin REGISTRY"), "https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html"),
    Leaf("07-aws", "containers", "ecs", "Amazon ECS", "Run task/service workloads on EC2 or Fargate with correct identity, networking, deployment and capacity-provider behavior.", C(
        "Task definition — versioned container, resource, network, log, secret, volume and role specification",
        "Task — running/scheduled instantiation of a task definition",
        "Service — maintains desired tasks and integrates deployment, load balancing and discovery",
        "Task role — application AWS permissions exposed to containers",
        "Execution role — agent permissions for image pull, logs and startup secret retrieval",
        "awsvpc networking — each task gets an ENI/IP/security groups and consumes subnet capacity",
        "Fargate — managed task compute removes node operations with feature, startup and pricing trade-offs",
        "Capacity provider — associates EC2 ASG/Fargate capacity and placement strategy with services",
        "Deployment circuit breaker — detects failed service stabilization and can roll back",
        "Task draining — load balancer, stop timeout and application signal handling protect in-flight work",
    ), ("aws ecs describe-clusters --clusters CLUSTER", "aws ecs describe-services --cluster CLUSTER --services SERVICE", "aws ecs describe-tasks --cluster CLUSTER --tasks TASK", "aws ecs execute-command --cluster CLUSTER --task TASK --container CONTAINER --interactive --command /bin/sh"), "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html"),
    Leaf("07-aws", "containers", "eks", "Amazon EKS", "Operate managed Kubernetes control planes with secure AWS identity, networking, storage, nodes, add-ons and upgrades.", C(
        "Managed control plane — AWS runs API/etcd availability while customers own access, workloads and most data-plane choices",
        "Access entries — EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources",
        "Managed node group — AWS-integrated ASG lifecycle for tested AMI/update patterns",
        "IRSA — OIDC service-account token assumes an IAM role with trust conditions",
        "EKS Pod Identity — association/agent-based workload role delivery with separate operational semantics",
        "VPC CNI — assigns VPC IPs and is constrained by subnet/ENI/prefix settings",
        "Managed add-on — versioned EKS distribution of components still needs compatibility/config ownership",
        "CSI drivers — EBS/EFS drivers need workload identity, topology and version management",
        "Cluster upgrade — control plane, APIs, add-ons and nodes roll under skew/deprecation constraints",
        "Control-plane logging — API/audit/authenticator/controller/scheduler logs support security and diagnosis at a cost",
    ), ("aws eks describe-cluster --name CLUSTER", "aws eks list-addons --cluster-name CLUSTER", "aws eks list-access-entries --cluster-name CLUSTER", "kubectl get nodes,pods -A -o wide"), "https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html"),
    Leaf("07-aws", "containers", "karpenter-auto-mode", "Karpenter and EKS Auto Mode", "Provision and consolidate nodes from pending-Pod constraints while bounding disruption, compatibility, capacity and spend.", C(
        "Pending-Pod demand — autoscaler reads unschedulable constraints/requests rather than average node CPU alone",
        "NodePool — constrains labels, taints, requirements, disruption and aggregate resource limits",
        "NodeClass — AWS-specific subnets, security groups, AMI, role and storage configuration",
        "Instance diversification — compatible families/sizes/AZs improve capacity and Spot resilience",
        "Consolidation — removes/replaces underutilized nodes after respecting disruption policy",
        "Disruption budget — limits voluntary Karpenter actions but does not stop instance failure",
        "Expiration/drift — rotates nodes for image/config lifecycle under workload availability constraints",
        "Scale from zero — Pod constraints and NodePool metadata must still identify a compatible node",
        "EKS Auto Mode — managed node/storage/network automation builds on Karpenter concepts with supported constraints",
        "Spend limits — NodePool resource limits, quotas/budgets and admission prevent runaway provisioning",
    ), ("kubectl get nodepool,ec2nodeclass,nodeclaim", "kubectl describe nodeclaim NAME", "kubectl logs -n kube-system deploy/karpenter --since=30m", "aws ec2 describe-instance-type-offerings --location-type availability-zone"), "https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html"),
    Leaf("07-aws", "containers", "aws-load-balancer-controller", "AWS Load Balancer Controller", "Reconcile Kubernetes Ingress/Service/Gateway intent into safe ALB/NLB resources and target health.", C(
        "Ingress reconciliation — annotations/spec/class generate ALB listeners/rules/target groups",
        "Service LoadBalancer — controller provisions NLB behavior from Service annotations/spec",
        "Target type ip — registers Pod IPs directly and depends on VPC routability/readiness",
        "Target type instance — registers nodes/NodePorts and adds another data-plane hop",
        "IngressGroup — shares an ALB across Ingresses and expands who can change listener rules",
        "Subnet discovery — tags/explicit subnets determine AZ/scheme and can fail silently through events",
        "IAM workload role — controller requires broad-looking but bounded ELB/EC2/ACM/WAF/tag actions",
        "Certificate/TLS — ACM discovery/ARN/listener policy and host rules must align",
        "Finalizers — controller cleanup can block Kubernetes deletion when AWS/API/IAM fails",
        "Controller events/logs — reconcile errors plus AWS target health locate desired-vs-cloud drift",
    ), ("kubectl get ingress,service -A", "kubectl describe ingress NAME -n NS", "kubectl logs -n kube-system deploy/aws-load-balancer-controller --since=30m", "aws elbv2 describe-target-health --target-group-arn TG_ARN"), "https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/"),

    Leaf("07-aws", "databases", "rds", "Amazon RDS", "Operate managed relational databases with safe connectivity, failover, backups, parameters and connection capacity.", C(
        "DB instance — managed engine compute/storage inside subnet/parameter/security configuration",
        "Multi-AZ — synchronous standby/failover for availability rather than read scaling",
        "Read replica — asynchronous copy for read scale/DR with lag and promotion implications",
        "Automated backups/PITR — transaction-log retention enables restore to a new instance within window",
        "Parameter group — engine settings can be dynamic or require reboot and need tested rollout",
        "RDS Proxy — pools/multiplexes supported connections and credentials with transaction pinning constraints",
        "Maintenance window — provider maintenance/reboot still needs application failover/retry testing",
        "Storage autoscaling — grows storage under thresholds but cannot shrink or fix I/O design",
        "Connection exhaustion — pool size, Lambda scaling and long transactions can overload before CPU",
        "Enhanced Monitoring/Performance Insights — OS/database wait evidence complements CloudWatch",
    ), ("aws rds describe-db-instances --db-instance-identifier DB", "aws rds describe-events --source-identifier DB --source-type db-instance", "aws rds describe-db-snapshots --db-instance-identifier DB", "aws rds reboot-db-instance --db-instance-identifier DB --force-failover"), "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html"),
    Leaf("07-aws", "databases", "aurora", "Amazon Aurora", "Operate distributed relational storage and writer/reader compute with measured failover, global replication and connection behavior.", C(
        "Cluster volume — replicated distributed storage is shared by writer/readers",
        "Writer endpoint — follows current writer and should be used for write-capable connections",
        "Reader endpoint — balances new reader connections but not individual queries or existing sessions",
        "Replica failover tier — influences which reader is promoted and how quickly compatible capacity is available",
        "Aurora Serverless — capacity units/auto-pause/version behavior trade idle cost against scaling/cold response",
        "Global Database — asynchronous cross-Region replication supports DR/read locality with RPO/failback considerations",
        "Backtrack — supported engines/configs can rewind logical time but it is not a substitute for backup",
        "RDS Proxy/pooling — stabilizes connection storms under session/transaction semantics",
        "Replica lag — long transactions/I/O/load can make readers stale and delay failover readiness",
        "Blue/green deployment — supports engine/change rehearsal with replication/switchover constraints",
    ), ("aws rds describe-db-clusters --db-cluster-identifier CLUSTER", "aws rds failover-db-cluster --db-cluster-identifier CLUSTER", "aws rds describe-global-clusters", "aws rds describe-blue-green-deployments"), "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html"),
    Leaf("07-aws", "databases", "dynamodb", "Amazon DynamoDB", "Design access-pattern-first keys, capacity, indexes, streams and global replication without hot partitions.", C(
        "Partition key — hashes items across physical partitions and must distribute request volume",
        "Sort key — orders items within a partition and enables range/prefix access patterns",
        "GSI — asynchronous alternate partition/sort key with its own storage/capacity/failure behavior",
        "LSI — alternate sort key sharing table partition key and creation-time/size constraints",
        "On-demand/provisioned — capacity modes trade predictability/control and can still throttle hot keys",
        "Conditional write — atomically enforces version/idempotency/state transition predicates",
        "Transaction — coordinates multiple items at higher cost/limits and is not a relational query model",
        "Streams — ordered per-item change records feed consumers under retention/idempotency needs",
        "Global Tables — multi-Region active replication with conflict resolution semantics",
        "TTL — asynchronous best-effort expiration; applications must not assume immediate deletion",
    ), ("aws dynamodb describe-table --table-name TABLE", "aws dynamodb query --table-name TABLE --key-condition-expression EXPR --expression-attribute-values file://values.json", "aws dynamodb describe-continuous-backups --table-name TABLE", "aws dynamodb describe-kinesis-streaming-destination --table-name TABLE"), "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html"),
    Leaf("07-aws", "databases", "elasticache", "Amazon ElastiCache", "Use Valkey/Redis or Memcached as bounded acceleration/state with explicit topology, eviction, persistence and recovery.", C(
        "Valkey/Redis replication group — primary and replicas provide failover/read paths under node/AZ design",
        "Cluster mode — shards keys across node groups and requires compatible clients/key strategy",
        "Memcached — simple distributed cache lacks Redis-style replication/persistence structures",
        "Eviction policy — determines which keys are removed under max memory and can affect correctness",
        "TTL — bounds staleness/memory but synchronized expiry can cause stampedes",
        "Persistence/backup — snapshots/AOF support differs and a cache should not silently become source of truth",
        "Failover — endpoint/client reconnect and data loss windows must be tested",
        "Cache stampede — coalescing, jitter, soft TTL and stale-while-revalidate protect downstream databases",
        "Hot key — one key can saturate a shard despite free aggregate capacity",
        "Encryption/auth — TLS, auth tokens/IAM features and subnet/SG protect access under client support",
    ), ("aws elasticache describe-replication-groups", "aws elasticache describe-cache-clusters --show-cache-node-info", "redis-cli --tls -h HOST INFO", "redis-cli --tls -h HOST SLOWLOG GET 20"), "https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html"),
    Leaf("07-aws", "databases", "opensearch", "Amazon OpenSearch Service", "Operate search/vector indexes with correct mappings, shards, access, snapshots, capacity and query observability.", C(
        "Index/mapping — schema and analyzers determine searchable fields and cannot always be changed in place",
        "Primary shard — unit of index distribution whose count affects scale, recovery and overhead",
        "Replica shard — copies improve availability/read scale when placed on separate nodes/AZs",
        "Cluster manager — coordinates metadata and needs dedicated capacity at production scale",
        "JVM heap — memory pressure/GC/circuit breakers often fail before disk/CPU averages",
        "Segment/merge — indexing creates segments and background merging consumes I/O/CPU",
        "Vector search — dimension/index method/recall/latency/memory and filter behavior need benchmark",
        "Snapshot — service-managed/manual repositories support recovery but require restore testing",
        "Fine-grained access — IAM/domain policy, network and index/document permissions form layers",
        "Shard sizing — too many small shards waste heap; too large slows recovery and relocation",
    ), ("aws opensearch describe-domain --domain-name DOMAIN", "curl -s https://HOST/_cluster/health?pretty", "curl -s https://HOST/_cat/shards?v", "curl -s https://HOST/_nodes/stats/jvm,fs,indices?pretty"), "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html"),

    Leaf("07-aws", "messaging-serverless", "sqs", "Amazon SQS", "Decouple producers and consumers with visible delivery semantics, idempotency, DLQs and backlog-based scaling.", C(
        "Standard queue — at-least-once delivery and best-effort order at very high scale",
        "FIFO queue — ordered message groups and deduplication with throughput/parallelism constraints",
        "Visibility timeout — lease after receive must cover/extend processing or a message becomes visible again",
        "Delete message — consumer commit requires the latest receipt handle after successful effect",
        "Long polling — reduces empty receives/cost and latency compared with tight short polling",
        "DLQ redrive — isolates poison/repeated failures and needs controlled diagnosis/replay tooling",
        "Retention — bounds replay window and storage of unprocessed messages",
        "Idempotency — stable event/effect keys prevent duplicate business side effects",
        "Oldest message age — stronger backlog/SLO signal than queue count alone",
        "In-flight quota — excessive concurrency/long visibility can block further receive progress",
    ), ("aws sqs get-queue-attributes --queue-url URL --attribute-names All", "aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10", "aws sqs start-message-move-task --source-arn DLQ_ARN", "aws cloudwatch get-metric-data --metric-data-queries file://sqs.json --start-time START --end-time END"), "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html"),
    Leaf("07-aws", "messaging-serverless", "sns-eventbridge", "Amazon SNS and EventBridge", "Fan out notifications and route domain events with filters, retries, archives and controlled cross-account policy.", C(
        "SNS topic — publisher fan-out to protocol subscriptions under topic policy",
        "Subscription filter — routes messages by attributes/body and can drop unexpected schemas",
        "Delivery retry/DLQ — endpoint-specific retry and dead-letter behavior must be observed",
        "EventBridge bus — account/custom/partner buses receive events under resource policy",
        "Rule pattern — matches structured event fields and routes to targets",
        "Input transformation — reshapes event for a target but creates schema coupling",
        "Archive/replay — retained bus events can be replayed with duplicate/side-effect controls",
        "Schema registry — documents/discovers schemas but compatibility governance remains owned",
        "Cross-account routing — organization/resource policies and target roles define trust",
        "Scheduler — invokes targets on time patterns with retry/DLQ and idempotency requirements",
    ), ("aws sns list-topics", "aws sns list-subscriptions-by-topic --topic-arn ARN", "aws events list-event-buses", "aws events list-rules --event-bus-name BUS", "aws events test-event-pattern --event-pattern file://pattern.json --event file://event.json"), "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html"),
    Leaf("07-aws", "messaging-serverless", "step-functions", "AWS Step Functions", "Coordinate durable workflows with explicit state, retries, compensation, idempotency and execution visibility.", C(
        "State machine — Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states",
        "Standard workflow — durable exactly-once workflow execution semantics for long-running auditable flows",
        "Express workflow — high-volume short workflows with different sync/async delivery/history semantics",
        "Task integration — optimized/AWS SDK/activity/callback patterns invoke external work",
        "Retry — error-specific interval/backoff/max attempts must not duplicate unsafe effects",
        "Catch — routes terminal task error into compensation/recovery paths",
        "Callback token — pauses until an authorized external completion with timeout/heartbeat",
        "Map state — processes collections with concurrency and failure thresholds",
        "Execution history — records transitions/input/output and can leak sensitive data if unbounded",
        "Redrive — resumes eligible failed Standard executions while tasks remain idempotent",
    ), ("aws stepfunctions list-state-machines", "aws stepfunctions validate-state-machine-definition --definition file://machine.asl.json", "aws stepfunctions describe-execution --execution-arn ARN", "aws stepfunctions get-execution-history --execution-arn ARN --reverse-order"), "https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html"),
    Leaf("07-aws", "messaging-serverless", "kinesis-msk", "Kinesis Data Streams and Amazon MSK", "Operate partitioned replayable streams with balanced keys, checkpoints, lag, retention and consumer recovery.", C(
        "Shard/partition — ordered log unit and primary throughput/parallelism boundary",
        "Partition key — determines shard/partition and can create hot spots",
        "Sequence/offset — consumer position supports checkpoint and replay",
        "Consumer group — Kafka partitions are assigned/rebalanced among group members",
        "Enhanced fan-out — Kinesis consumers get dedicated throughput under additional cost",
        "Retention — bounds replay/recovery and storage cost",
        "Lag/iterator age — measures how far consumers are behind and drives capacity response",
        "Reshard/repartition — changes parallelism and ordering/key distribution constraints",
        "MSK broker storage/network — broker/partition count, replication and disk headroom affect recovery",
        "Schema/idempotency — event evolution and at-least-once processing require compatible consumers/effects",
    ), ("aws kinesis describe-stream-summary --stream-name STREAM", "aws kinesis list-shards --stream-name STREAM", "aws kafka describe-cluster-v2 --cluster-arn ARN", "kafka-consumer-groups.sh --bootstrap-server BROKERS --describe --group GROUP"), "https://docs.aws.amazon.com/streams/latest/dev/introduction.html"),
    Leaf("07-aws", "messaging-serverless", "lambda", "AWS Lambda", "Run event-driven functions with controlled initialization, concurrency, identity, network, retry and downstream capacity.", C(
        "Execution environment — initialization may be reused across invocations but must not hold unsafe tenant state",
        "Cold start — package/runtime/init/VPC and extensions contribute before handler execution",
        "Reserved concurrency — reserves and caps concurrency for a function, protecting account/downstream",
        "Provisioned concurrency — pre-initializes environments for latency at continuous cost",
        "Event source mapping — polls streams/queues and manages batches, concurrency, retries and checkpoints",
        "Idempotency — retried/duplicate events need stable business-effect keys and durable records",
        "VPC networking — subnets, IP capacity, SG, NAT/endpoints/DNS become function dependencies",
        "Execution role — function AWS permissions should exclude deployment/administrative capabilities",
        "Destinations/DLQ — async outcomes capture failed/successful invocation metadata under service-specific rules",
        "Timeout/cancellation — function timeout must fit caller/dependency deadlines and leave effects consistent",
    ), ("aws lambda get-function-configuration --function-name FUNCTION", "aws lambda get-function-concurrency --function-name FUNCTION", "aws lambda list-event-source-mappings --function-name FUNCTION", "aws logs tail /aws/lambda/FUNCTION --since 30m --follow"), "https://docs.aws.amazon.com/lambda/latest/dg/welcome.html"),
    Leaf("07-aws", "messaging-serverless", "api-gateway", "Amazon API Gateway", "Publish authenticated, throttled and observable REST/HTTP/WebSocket APIs with safe integration and deployment lifecycle.", C(
        "REST vs HTTP API — feature/integration/authorization/transformation and price differ",
        "WebSocket API — connection routes and state/callback management support bidirectional messaging",
        "Route/resource-method — matches request and invokes an integration",
        "Lambda proxy integration — passes normalized request/event and expects defined response shape",
        "Authorizer — IAM/JWT/Lambda identity decision with cache and failure implications",
        "Usage plan/API key — metering/throttle association is not user authentication by itself",
        "Stage/deployment — immutable API snapshot and stage settings/canary/logging form release unit",
        "Throttling — account/stage/route limits protect gateway/downstream and return retryable errors",
        "Custom domain — certificate, endpoint type, API mapping and DNS compose the public endpoint",
        "Access/execution logs — request IDs, integration latency/status and safe fields support diagnosis",
    ), ("aws apigateway get-rest-apis", "aws apigatewayv2 get-apis", "aws apigateway get-stages --rest-api-id API_ID", "aws apigatewayv2 get-integrations --api-id API_ID"), "https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html"),

    Leaf("07-aws", "security-operations", "kms", "AWS KMS", "Control encryption-key use and lifecycle without making protected data unrecoverable.", C(
        "KMS key — logical key with policy, metadata and protected key material used by integrated services",
        "Envelope encryption — KMS protects data keys while applications/services encrypt bulk data locally",
        "Key policy — primary resource policy can enable IAM delegation or directly authorize principals",
        "Grant — constrained delegated permission often used by AWS services and lifecycle operations",
        "Encryption context — authenticated additional data can bind ciphertext use to resource/purpose",
        "Rotation — creates new backing material for future encrypt while old material remains for decrypt",
        "Multi-Region key — related key material supports regional use but replication/data policy remains separate",
        "Imported/custom key store — increases control with availability/expiry/operations responsibility",
        "Request quota — high-volume SSE-KMS or application calls can throttle a data path",
        "Deletion — waiting period is a last warning; loss of a key can permanently lose every dependent ciphertext",
    ), ("aws kms describe-key --key-id KEY", "aws kms get-key-policy --key-id KEY --policy-name default", "aws kms list-grants --key-id KEY", "aws kms get-key-rotation-status --key-id KEY"), "https://docs.aws.amazon.com/kms/latest/developerguide/overview.html"),
    Leaf("07-aws", "security-operations", "secrets-manager", "AWS Secrets Manager and Parameter Store", "Store, retrieve and rotate secrets/configuration through least-privilege workload identity and safe caching.", C(
        "Secret version/stage — labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback",
        "Rotation Lambda — creates/sets/tests/finishes a new credential under idempotent staged workflow",
        "Resource policy — supports cross-account/service access and must prevent public/external exposure",
        "KMS key — decrypt permission/key policy participates in secret access",
        "Client cache — reduces latency/cost but must respect rotation/revocation and process isolation",
        "Parameter hierarchy — names organize configuration but IAM wildcard scope can overgrant",
        "SecureString — encrypts Parameter Store values with KMS while metadata/history still need control",
        "Dynamic identity — prefer service IAM/database auth over a stored static password where supported",
        "Leak response — revoke/rotate first, then remove logs/source/history and investigate access",
        "Audit — CloudTrail secret API access must be monitored without logging secret values",
    ), ("aws secretsmanager describe-secret --secret-id SECRET", "aws secretsmanager list-secret-version-ids --secret-id SECRET", "aws secretsmanager rotate-secret --secret-id SECRET", "aws ssm get-parameter --name NAME --with-decryption"), "https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html"),
    Leaf("07-aws", "security-operations", "acm-waf-shield", "ACM, AWS WAF and Shield", "Operate TLS certificates and edge protections with expiry, tuning, false-positive and incident considerations.", C(
        "ACM certificate — managed public/private/imported certificate with supported service integration",
        "DNS validation — persistent validation record enables managed renewal when service conditions hold",
        "Imported certificate — customer owns renewal/reimport and expiry alert",
        "TLS policy — protocol/cipher compatibility balances client support and security",
        "WAF web ACL — ordered managed/custom/rate rules return allow/block/count/CAPTCHA/challenge actions",
        "Count mode — observes a new rule before enforcement to detect false positives",
        "Rate-based rule — limits aggregate keys but is not a complete application tenant quota",
        "Managed rule version — updates can change behavior and require staged rollout",
        "Shield Standard/Advanced — DDoS protection/support/cost protection differ by service/tier",
        "Origin protection — edge allowlist/auth/private origin prevents bypassing WAF/CDN controls",
    ), ("aws acm list-certificates", "aws acm describe-certificate --certificate-arn ARN", "aws wafv2 list-web-acls --scope REGIONAL --region REGION", "aws wafv2 get-sampled-requests --web-acl-arn ARN --rule-metric-name METRIC --scope REGIONAL --time-window file://window.json --max-items 100"), "https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html"),
    Leaf("07-aws", "security-operations", "security-detection", "GuardDuty, Security Hub, Inspector, Macie and Detective", "Turn cloud security findings into owned, prioritized, evidence-preserving response rather than alert accumulation.", C(
        "GuardDuty — analyzes supported logs/signals to emit contextual threat findings",
        "Security Hub — aggregates/normalizes findings and control standards across accounts/Regions",
        "Inspector — continuously assesses supported compute/container/function packages and exposure",
        "Macie — discovers/classifies sensitive S3 data and bucket access risk",
        "Detective — correlates activity/entities to support investigation",
        "Delegated administration — central security account manages organization coverage without using management account",
        "Finding severity — vendor score must be combined with asset exposure, data and exploitability",
        "Suppression — tuned archival/suppression needs owner/reason/expiry to avoid hiding new risk",
        "Automation — EventBridge/Security Hub actions can quarantine or ticket with rollback/safety controls",
        "Coverage evidence — inventory accounts/Regions/services and detect disabled sensors or log gaps",
    ), ("aws guardduty list-detectors", "aws securityhub get-findings --filters file://filters.json", "aws inspector2 list-findings --filter-criteria file://criteria.json", "aws macie2 get-macie-session"), "https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html"),
    Leaf("07-aws", "security-operations", "cloudwatch-xray", "Amazon CloudWatch and X-Ray", "Collect actionable metrics, logs, alarms, traces and dashboards with controlled cardinality, privacy and spend.", C(
        "Metric/dimension — numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost",
        "Alarm — evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state",
        "Composite alarm — pages on combinations and can reduce symptom duplication",
        "Log group/stream — retention, KMS, subscription and resource policy define log lifecycle",
        "Logs Insights — query structured/unstructured fields over selected time/bytes",
        "Embedded Metric Format — logs generate custom metrics with cardinality/cost implications",
        "Container Insights — curated container/cluster signals still need SLO application metrics",
        "Application Signals — service-level telemetry/SLO features depend on supported instrumentation",
        "X-Ray segment/subsegment — distributed trace documents service/dependency timing and errors",
        "Sampling/redaction — control trace/log volume and sensitive payload before export/storage",
    ), ("aws cloudwatch describe-alarms --state-value ALARM", "aws logs tail LOG_GROUP --since 30m", "aws logs start-query --log-group-name GROUP --start-time START --end-time END --query-string 'fields @timestamp,@message | limit 20'", "aws xray get-service-graph --start-time START --end-time END"), "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html"),
    Leaf("07-aws", "security-operations", "cloudtrail-config", "AWS CloudTrail and Config", "Preserve organization-wide API/configuration history and detect unauthorized or noncompliant change.", C(
        "Management event — control-plane API activity such as creating/changing resources",
        "Data event — high-volume resource data-plane activity enabled selectively at additional cost",
        "Organization trail — covers current/new member accounts under centralized governance",
        "Log file validation — digest chain helps verify delivered CloudTrail file integrity",
        "CloudTrail Lake — managed event store/query with event data stores and retention/cost",
        "Config recorder — records supported resource configuration and relationship changes",
        "Config rule — evaluates desired compliance periodically or on change",
        "Aggregator — centralizes configuration/compliance across accounts/Regions",
        "Remediation — SSM automation can correct findings but needs blast-radius and exception handling",
        "Delivery protection — independent log account, restrictive bucket/KMS, retention/object lock prevent tampering",
    ), ("aws cloudtrail describe-trails", "aws cloudtrail get-trail-status --name TRAIL", "aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=EVENT", "aws configservice get-resource-config-history --resource-type TYPE --resource-id ID"), "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html"),
    Leaf("07-aws", "security-operations", "systems-manager", "AWS Systems Manager", "Operate fleets through audited sessions, inventory, patch and automation without unmanaged SSH or broad scripts.", C(
        "Managed node — agent/identity/network registration makes a host available to SSM",
        "Session Manager — audited interactive/tunnel access without inbound SSH under IAM/session preferences",
        "Run Command — executes commands across targets with concurrency/error thresholds and output controls",
        "Automation document — typed multi-step workflow with assume role, branching, approvals and rollback design",
        "Patch Manager — baselines, maintenance windows and compliance scan/install coordinate patching",
        "Inventory — collects software/instance metadata for fleet queries and exposure",
        "State Manager — periodically enforces associations and can conflict with image/IaC ownership",
        "Parameter Store — distributes configuration/secrets under hierarchy/KMS/IAM",
        "Fleet Manager — console operations still require least privilege and evidence",
        "Target safety — tags/resource groups, max concurrency/errors and canaries prevent fleet-wide mistakes",
    ), ("aws ssm describe-instance-information", "aws ssm start-session --target INSTANCE_ID", "aws ssm send-command --document-name DOC --targets Key=tag:Environment,Values=stage --max-concurrency 10% --max-errors 1", "aws ssm describe-instance-patch-states --instance-ids INSTANCE_ID"), "https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html"),

    Leaf("07-aws", "infrastructure-delivery", "cloudformation", "AWS CloudFormation", "Reconcile reviewed templates through stack boundaries, change sets, drift and recoverable update workflows.", C(
        "Stack — ownership/lifecycle boundary for a set of resources and outputs",
        "Change set — previews create/update/import actions but cannot predict every service-side effect",
        "Rollback — attempts prior stack state and can fail on irreversible/external/data changes",
        "Stack policy — protects selected resources from update actions",
        "Deletion/retention policy — controls resource/snapshot behavior when template/stack removes stateful resources",
        "Nested stack/module — composes templates but introduces dependency/update propagation",
        "StackSet — deploys instances across accounts/Regions with concurrency/failure controls",
        "Drift detection — compares supported properties to template without deciding correct truth",
        "Import — adopts supported existing resources after template/identity preparation",
        "Continue update rollback — repairs a stuck rollback after fixing/skipping failed resources carefully",
    ), ("aws cloudformation create-change-set --stack-name STACK --change-set-name CHANGE --template-body file://template.yaml --change-set-type UPDATE", "aws cloudformation describe-stack-events --stack-name STACK", "aws cloudformation detect-stack-drift --stack-name STACK", "aws cloudformation continue-update-rollback --stack-name STACK"), "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html"),
    Leaf("07-aws", "infrastructure-delivery", "cdk", "AWS CDK", "Build tested reusable cloud constructs while reviewing synthesized CloudFormation and securing bootstrap/assets.", C(
        "App/stack/construct tree — code composes logical resources and ownership hierarchy",
        "L1 construct — direct generated CloudFormation resource mapping",
        "L2/L3 construct — higher-level intent with defaults and multiple resources",
        "Synthesis — evaluates code/context into CloudFormation templates and assets",
        "Bootstrap — account/Region roles, buckets and repositories are privileged deployment infrastructure",
        "Asset publishing — file/container assets are hashed/uploaded and need provenance/access/lifecycle",
        "Context lookup — cached environment facts can become stale/non-reproducible if unmanaged",
        "Escape hatch — overrides low-level property when abstraction lacks it, increasing coupling",
        "Assertion test — validates synthesized resources/properties while integration tests prove behavior",
        "Logical ID/refactor — construct path changes can replace resources unless identity is preserved",
    ), ("cdk synth", "cdk diff", "cdk doctor", "cdk bootstrap aws://ACCOUNT/REGION", "cdk deploy STACK --require-approval broadening"), "https://docs.aws.amazon.com/cdk/v2/guide/home.html"),
    Leaf("07-aws", "infrastructure-delivery", "code-services", "CodeBuild, CodePipeline and CodeDeploy", "Build and promote trusted artifacts through isolated runners, approvals and observable deployment strategies.", C(
        "CodeBuild project — image/compute/VPC/service role/buildspec define a privileged ephemeral build",
        "Buildspec — phases/commands/artifacts/cache/reports are executable supply-chain code",
        "Privileged mode — enables Docker daemon workflows but greatly expands runner attack surface",
        "CodePipeline stage/action — orchestrates source/build/test/approval/deploy artifacts",
        "Artifact store — encrypted regional bucket must preserve exact immutable promotion inputs",
        "Manual approval — records a decision but needs useful evidence, expiry and authorized approvers",
        "CodeDeploy deployment group — selects targets/strategy/alarms/rollback hooks",
        "Blue-green — parallel replacement and traffic shift need state/schema compatibility",
        "Lifecycle hook — validation scripts can gate traffic but must timeout/emit evidence",
        "OIDC/role separation — source/build/deploy identities should not share broad long-lived credentials",
    ), ("aws codebuild batch-get-builds --ids BUILD_ID", "aws codepipeline get-pipeline-state --name PIPELINE", "aws codepipeline list-action-executions --pipeline-name PIPELINE", "aws deploy get-deployment --deployment-id ID"), "https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html"),
    Leaf("07-aws", "infrastructure-delivery", "service-catalog-proton", "AWS Service Catalog and Proton", "Publish versioned governed infrastructure/service golden paths with ownership, constraints and safe upgrades.", C(
        "Portfolio/product — curated products and versions are shared to approved principals/accounts",
        "Launch constraint — service role separates user permission from provisioned-resource permission",
        "Template constraint — restricts product parameters to policy-safe combinations",
        "Provisioned product — launched stack/resource lifecycle needs owner/status/termination handling",
        "Product version — upgrades need compatibility, migration and deprecation communication",
        "TagOptions — standardize tags but do not replace enforcement or runtime ownership",
        "Proton environment — shared infrastructure context for service instances/templates",
        "Service template — standardizes service pipeline/infrastructure under platform ownership",
        "Self-managed provisioning — integrates external IaC workflows and must reconcile status/failures",
        "Golden-path metrics — adoption, time-to-deploy, success, exceptions and toil measure product value",
    ), ("aws servicecatalog search-products-as-admin", "aws servicecatalog scan-provisioned-products", "aws proton list-environments", "aws proton list-service-templates"), "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html"),

    Leaf("07-aws", "ai-platform", "bedrock", "Amazon Bedrock", "Govern managed foundation-model inference, guardrails, knowledge bases, agents, evaluation, capacity and cost.", C(
        "Foundation model access — model/provider/Region/API capability and terms must be approved",
        "Converse/Invoke API — normalized/model APIs differ in streaming, tools and request schema",
        "Inference profile — routes/model invocation capacity across supported Regions or application profiles",
        "Provisioned throughput — reserves model units/capacity for predictable demand at commitment cost",
        "Guardrail — evaluates input/output policies but is one layer rather than proof of safety",
        "Knowledge Base — managed ingestion/retrieval still needs source authorization, tenancy and freshness",
        "Agent — orchestrates models/actions/knowledge with least-privilege tools and human approval",
        "Model evaluation — datasets/metrics/judges compare candidates but need calibration/versioning",
        "Cross-Region inference — improves capacity while changing data path/residency analysis",
        "Token metering — input/output/cache/model/region usage supports budget and chargeback",
    ), ("aws bedrock list-foundation-models", "aws bedrock-runtime converse --model-id MODEL --messages file://messages.json", "aws bedrock list-guardrails", "aws bedrock list-inference-profiles"), "https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html"),
    Leaf("07-aws", "ai-platform", "sagemaker-ai", "Amazon SageMaker AI", "Operate reproducible training, registry, deployment, monitoring and evaluation across managed inference modes.", C(
        "Training job — immutable container/data/hyperparameter/instance run writes model artifacts/metrics",
        "Processing job — managed batch preprocessing/evaluation under reproducible container and data inputs",
        "Pipeline — DAG connects parameterized steps, cache and conditions with lineage",
        "Model Registry — model packages/versions/approval status bind artifact/container/evidence",
        "Real-time endpoint — provisioned variants serve synchronous low-latency predictions",
        "Async/serverless/batch — queued, intermittent or offline modes trade latency/capacity/features",
        "Multi-model endpoint — shares fleet and dynamically loads models with cache/isolation/cold-start risk",
        "Production variant — weighted/shadow traffic supports controlled release under metric/eval gates",
        "Endpoint autoscaling — invocation/concurrency/backlog metrics must account for model load and downstream",
        "Model Monitor/Clarify — managed monitoring/explainability/bias features need task-specific thresholds and ownership",
    ), ("aws sagemaker list-training-jobs", "aws sagemaker list-model-packages --model-package-group-name GROUP", "aws sagemaker describe-endpoint --endpoint-name ENDPOINT", "aws sagemaker-runtime invoke-endpoint --endpoint-name ENDPOINT --body fileb://request.json output.json"), "https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html"),
    Leaf("07-aws", "ai-platform", "eks-ai-inference", "AI/ML workloads on Amazon EKS", "Serve and train models on EKS with qualified GPU nodes, Karpenter, model caches, queues and inference SLOs.", C(
        "GPU node pool — hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators",
        "Karpenter GPU provisioning — pending resource/label/topology constraints select compatible EC2 capacity",
        "GPU Operator/device plugin — reconciles/advertises devices and telemetry but does not fix application compatibility",
        "KServe/vLLM/Triton — control plane and runtimes trade portability, performance and operations",
        "Model cache — S3/shared/local NVMe distribution controls cold start, integrity and disk pressure",
        "Queue-based scaling — token queue drives replicas; pending Pods drive nodes after long provisioning/warmup",
        "EFA/NCCL — distributed workloads need topology, drivers, placement and network qualification",
        "Spot/capacity — interruptions and scarce types require diversity, checkpoint/fallback and reservations",
        "Inference telemetry — queue, TTFT, inter-token, tokens/s, KV, GPU and quality/cost define goodput",
        "Canary lifecycle — independently qualify node image, driver, runtime, model and prompt/evaluator changes",
    ), ("kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name", "kubectl get pods -A --field-selector=status.phase=Pending", "kubectl logs -n kube-system deploy/karpenter --since=30m", "kubectl exec -n inference POD -- nvidia-smi"), "https://docs.aws.amazon.com/eks/latest/best-practices/aiml-compute.html"),
    Leaf("07-aws", "ai-platform", "aws-accelerators", "AWS GPUs, Inferentia and Trainium", "Select scarce accelerator hardware from model compatibility, memory/compute/topology, capacity, reliability and unit economics.", C(
        "G-family GPU — graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network",
        "P-family GPU — high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation",
        "Inferentia — AWS inference accelerator programmed through Neuron SDK and compiled model support",
        "Trainium — AWS training accelerator with Neuron distributed stack and operation compatibility",
        "Neuron SDK — compiler/runtime/framework integration is a qualification and portability dependency",
        "Accelerator memory — weights, KV/activations/workspace/fragmentation determine fit beyond parameter count",
        "EFA — OS-bypass networking improves supported collectives only with compatible topology/software",
        "Capacity reservation/block — commits specific capacity/time and differs from discount-only commitments",
        "Spot — fault-tolerant jobs need checkpoint/restart and diversified capacity",
        "Benchmark — target model/precision/batch/context/goodput/quality and total cost decide hardware",
    ), ("aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'", "aws ec2 describe-capacity-reservations", "neuron-ls", "nvidia-smi topo -m"), "https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html"),
]


K8S: list[Leaf] = [
    Leaf("06-kubernetes", "architecture", "api-server-etcd", "Kubernetes API server and etcd", "Operate the authoritative API, admission/storage path and consistent etcd quorum under bounded load.", C(
        "API groups/versions — resource kinds evolve through served/storage versions and conversion",
        "Request path — authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence",
        "Watch — streams resource changes from a revision and powers controllers efficiently",
        "ResourceVersion — identifies observed revisions for concurrency/watch rather than a user timestamp",
        "Server-side apply — merges declarative fields by field manager and reports ownership conflicts",
        "etcd quorum — majority of voting members is required for writes and consistent operation",
        "Compaction — removes old MVCC revisions so watches must restart when too old",
        "Defragmentation — reclaims backend file space after compaction under operational care",
        "Encryption at rest — protects selected API resource values with key/provider lifecycle",
        "API priority/fairness — queues/shares requests to protect critical flows from noisy clients",
    ), ("kubectl get --raw '/readyz?verbose'", "kubectl get --raw '/metrics' | rg 'apiserver|etcd'", "kubectl api-resources", "ETCDCTL_API=3 etcdctl endpoint status --cluster -w table"), "https://kubernetes.io/docs/concepts/overview/kubernetes-api/"),
    Leaf("06-kubernetes", "architecture", "scheduler-controllers-kubelet", "Scheduler, controllers and kubelet", "Trace desired state through reconciliation, binding and node execution without confusing component responsibilities.", C(
        "Controller loop — watches desired/observed state and performs level-based idempotent reconciliation",
        "Scheduler queue — unscheduled Pods progress through filtering/scoring/backoff before binding",
        "Filter plugin — rejects nodes that cannot satisfy resources, affinity, taints, topology or volumes",
        "Score plugin — ranks feasible nodes and can favor spread/bin packing/locality",
        "Binding — records selected node in Pod spec after scheduling assumptions/reservations",
        "Kubelet Pod sync — realizes assigned Pod through volume, sandbox, image and container runtime operations",
        "CRI — gRPC boundary from kubelet to containerd/CRI-O runtime",
        "Node status/lease — kubelet heartbeat and conditions drive availability/eviction decisions",
        "Cloud controller — reconciles nodes/routes/load balancers against cloud APIs",
        "Leader election — controllers/schedulers use leases so only active leader mutates shared state",
    ), ("kubectl get events -A --field-selector=reason=FailedScheduling", "kubectl get lease -n kube-system", "kubectl describe node NODE", "journalctl -u kubelet -u containerd --since '-30 min'"), "https://kubernetes.io/docs/concepts/overview/components/"),

    Leaf("06-kubernetes", "workloads", "pods", "Kubernetes Pods", "Operate the shared scheduling/network/storage/security unit and its complete lifecycle.", C(
        "Pod sandbox — containers share network namespace and can share IPC/process/volumes by configuration",
        "Phase — Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail",
        "Init container — sequential prerequisite that must complete before app containers",
        "Sidecar — supporting container lifecycle/order needs explicit startup/termination semantics",
        "Ephemeral container — debug process added to a running Pod without normal resources/probes/restart",
        "Restart policy — kubelet restarts containers under Always/OnFailure/Never and exponential backoff",
        "Termination grace — SIGTERM/preStop/drain must finish before SIGKILL deadline",
        "Pod readiness gate — custom condition can delay readiness beyond container probes",
        "Owner reference — connects Pod to controller garbage collection and desired count",
        "Ephemeral storage — writable layer/logs/emptyDir count toward requests/limits and node disk pressure",
    ), ("kubectl get pod POD -n NS -o yaml", "kubectl describe pod POD -n NS", "kubectl logs POD -n NS --all-containers --previous", "kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER"), "https://kubernetes.io/docs/concepts/workloads/pods/"),
    Leaf("06-kubernetes", "workloads", "deployments", "Deployments and ReplicaSets", "Perform safe stateless rollouts, pause/undo and diagnose progress/readiness without manual Pod ownership.", C(
        "Deployment selector — immutable label contract determines which ReplicaSets/Pods are owned",
        "Pod template hash — creates a new ReplicaSet when template content changes",
        "RollingUpdate — maxSurge/maxUnavailable bound temporary capacity and disruption",
        "Recreate — terminates old Pods before new when coexistence is unsafe",
        "minReadySeconds — requires sustained readiness before a Pod counts available",
        "progressDeadlineSeconds — marks rollout stalled but does not automatically roll back",
        "Revision history — retained ReplicaSets enable undo at storage/resource cost",
        "Pause/resume — batches template changes before a new rollout",
        "Availability condition — desired/updated/ready/available replicas explain rollout state",
        "Drain compatibility — readiness, preStop, grace and LB endpoint propagation protect in-flight work",
    ), ("kubectl rollout status deployment/NAME -n NS", "kubectl rollout history deployment/NAME -n NS", "kubectl rollout undo deployment/NAME -n NS --to-revision=REV", "kubectl get rs -n NS --sort-by=.metadata.creationTimestamp"), "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/"),
    Leaf("06-kubernetes", "workloads", "statefulsets-daemonsets", "StatefulSets and DaemonSets", "Operate stable-identity/stateful workloads and node-local agents under controlled update and disruption.", C(
        "Stateful ordinal — stable Pod name/identity persists across rescheduling but not physical node",
        "Headless Service — publishes per-Pod DNS identity for StatefulSet membership",
        "VolumeClaimTemplate — creates stable per-ordinal PVCs that are not automatically deleted by default semantics",
        "OrderedReady — sequential create/update assumes application readiness and can deadlock bad clusters",
        "Partitioned update — rolls only selected ordinals for canary/manual control",
        "State replication — application/database must implement quorum/failover; StatefulSet does not",
        "DaemonSet eligibility — runs on every matching node and tolerates common node conditions through controller defaults",
        "DaemonSet rollout — maxUnavailable/surge support varies by strategy/version and affects node agent coverage",
        "Critical agents — CNI/storage/log/GPU DaemonSets need priority/resources and upgrade ordering",
        "Node drain — DaemonSet Pods are ignored/recreated, while stateful eviction must respect PDB/storage",
    ), ("kubectl get statefulset,daemonset -A", "kubectl rollout status statefulset/NAME -n NS", "kubectl rollout status daemonset/NAME -n NS", "kubectl get pvc -n NS -l app=NAME"), "https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/"),
    Leaf("06-kubernetes", "workloads", "jobs-cronjobs", "Jobs and CronJobs", "Run idempotent bounded batch work with parallelism, retry, deadlines, schedule and cleanup controls.", C(
        "Completion — Job succeeds after required successful Pods/completions under mode semantics",
        "Parallelism — number of Pods executing concurrently and downstream load",
        "Backoff limit — bounds Pod failures before Job fails but retries can repeat effects",
        "Active deadline — limits total Job runtime including retries",
        "Indexed Job — gives stable completion indexes for partitioned work",
        "Pod failure policy — classifies exit/status outcomes to fail/ignore/count under supported versions",
        "TTL after finish — garbage-collects completed Jobs after evidence retention window",
        "Cron schedule/time zone — controller creates Jobs from wall-clock schedule with missed-run handling",
        "Concurrency policy — Allow/Forbid/Replace controls overlap but application locks may still be needed",
        "Starting deadline — skips or starts missed schedules within a tolerance window",
    ), ("kubectl get job,cronjob -A", "kubectl describe job NAME -n NS", "kubectl create job --from=cronjob/NAME MANUAL -n NS", "kubectl logs -n NS job/NAME --all-containers"), "https://kubernetes.io/docs/concepts/workloads/controllers/job/"),
    Leaf("06-kubernetes", "workloads", "probes-lifecycle", "Probes and container lifecycle", "Separate startup, liveness and readiness to prevent false restarts and unsafe traffic or termination.", C(
        "Startup probe — delays liveness/readiness scheduling until slow initialization succeeds",
        "Liveness probe — detects unrecoverable local process state and triggers restart",
        "Readiness probe — removes a Pod from endpoints without restarting it",
        "HTTP probe — kubelet calls path/port/scheme with specific host/header semantics",
        "TCP probe — verifies connection acceptance but not application correctness",
        "Exec probe — runs in container and can consume resources/hang if poorly designed",
        "gRPC probe — calls standard health protocol under supported version/config",
        "Probe thresholds — period/timeout/success/failure determine detection and recovery timing",
        "preStop — hook runs before termination signal and consumes the same grace period",
        "Stop signal — image/runtime/Pod signal and application handler determine graceful drain",
    ), ("kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'", "kubectl get pod POD -n NS -o jsonpath='{.status.containerStatuses}' | jq", "kubectl get endpointslice -n NS -l kubernetes.io/service-name=SVC -o yaml", "kubectl logs POD -n NS --previous"), "https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/"),

    Leaf("06-kubernetes", "networking", "services-endpoints-dns", "Services, EndpointSlices and CoreDNS", "Route stable virtual service names to ready Pod endpoints and diagnose DNS/data-plane state separately.", C(
        "ClusterIP — virtual internal IP implemented by the cluster service data plane",
        "NodePort — reserves a port on nodes and routes to Service endpoints",
        "LoadBalancer — asks a controller/cloud to expose a Service and report ingress status",
        "ExternalName — DNS CNAME indirection without proxying or health",
        "Headless Service — returns endpoint DNS records without ClusterIP load balancing",
        "EndpointSlice — scalable source of endpoint addresses, ports, readiness and topology hints",
        "Service selector — label query chooses Pods; mismatch yields no endpoints",
        "targetPort — number or named Pod port must match actual listener",
        "CoreDNS — watches Services/EndpointSlices and answers cluster zones plus forwarded external DNS",
        "DNS search/ndots — resolver expansion can create latency and surprising external/internal queries",
    ), ("kubectl get svc,endpoints,endpointslice -A -o wide", "kubectl describe svc NAME -n NS", "kubectl run dns-test --rm -it --image=nicolaka/netshoot -- dig SVC.NS.svc.cluster.local", "kubectl logs -n kube-system -l k8s-app=kube-dns --since=30m"), "https://kubernetes.io/docs/concepts/services-networking/service/"),
    Leaf("06-kubernetes", "networking", "cni-kubeproxy-ebpf", "CNI, kube-proxy and eBPF data planes", "Implement Pod addressing/routing and Service translation under IP, conntrack and policy constraints.", C(
        "Kubernetes network model — Pods have cluster-routable IP identity and communicate without required NAT inside the model",
        "CNI plugin — configures Pod interface, address, route and cleanup when runtime creates sandbox",
        "IPAM — allocates/reclaims Pod addresses and can exhaust/fragment subnet pools",
        "kube-proxy iptables — programs probabilistic NAT rules for Services and endpoints",
        "kube-proxy IPVS — uses kernel virtual server tables with separate synchronization",
        "eBPF data plane — programs kernel hooks/maps for routing, load balancing, policy and observability",
        "Conntrack — tracks NAT/state and can exhaust or retain stale translations",
        "MTU — encapsulation/cloud path mismatch can drop large packets while probes pass",
        "SNAT/source preservation — external/local traffic policy and plugin behavior influence client IP",
        "Node-to-Pod routing — overlay, native routing or cloud ENIs change troubleshooting and scale limits",
    ), ("kubectl get ds -n kube-system", "kubectl logs -n kube-system DS_POD --since=30m", "ip route && ip link", "conntrack -S", "bpftool map list"), "https://kubernetes.io/docs/concepts/cluster-administration/networking/"),
    Leaf("06-kubernetes", "networking", "networkpolicy", "Kubernetes NetworkPolicy", "Implement namespace/workload ingress and egress allow contracts with an enforcing CNI and verifiable DNS/dependency paths.", C(
        "Pod selection — policy applies only to Pods matched in its namespace",
        "Isolation direction — selecting a Pod for ingress/egress isolates that direction to allowed union",
        "Additive policy — all matching policy allows are unioned; deny rules are not in base API",
        "Namespace selector — selects labeled namespaces and needs protected namespace label governance",
        "Pod selector — selects workload labels in the policy/selected namespace context",
        "ipBlock — CIDR/except matches IPs and can behave unexpectedly after NAT",
        "Port/protocol — L3/L4 policy cannot natively authorize DNS names or HTTP paths",
        "Default deny — empty allow list establishes isolation and requires DNS/control/dependency allowances",
        "Both directions — source egress and destination ingress can independently block one flow",
        "CNI enforcement — unsupported/no plugin means accepted objects may have no runtime effect",
    ), ("kubectl get networkpolicy -A -o yaml", "kubectl describe networkpolicy NAME -n NS", "kubectl run netshoot --rm -it -n NS --image=nicolaka/netshoot -- bash", "tcpdump -ni any host IP and port PORT"), "https://kubernetes.io/docs/concepts/services-networking/network-policies/"),
    Leaf("06-kubernetes", "networking", "ingress-gateway-api", "Ingress and Gateway API", "Separate infrastructure listeners from application routing and operate TLS, status, policy and progressive traffic safely.", C(
        "IngressClass/controller — selects implementation and controller-specific features",
        "Ingress rule — host/path routes HTTP(S) to a Service backend under limited portable API",
        "GatewayClass — cluster-scoped implementation class controlled by infrastructure owner",
        "Gateway/listener — address/protocol/port/hostname/TLS attachment owned by platform/network team",
        "HTTPRoute/GRPCRoute — application route match/filter/backend and weighted traffic",
        "Parent status — Accepted/ResolvedRefs/Programmed conditions reveal attachment/reconcile state",
        "ReferenceGrant — explicitly authorizes supported cross-namespace references",
        "TLS termination/passthrough — route visibility, certificate and backend encryption differ",
        "Timeout/retry policy — implementation/API support must align with streaming and end-to-end deadlines",
        "Traffic split — weights need metrics/eval/stickiness and rollback rather than assumption",
    ), ("kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A", "kubectl describe gateway NAME -n NS", "kubectl get httproute NAME -n NS -o jsonpath='{.status.parents}' | jq", "curl -vk --resolve HOST:443:ADDRESS https://HOST/PATH"), "https://gateway-api.sigs.k8s.io/"),
    Leaf("06-kubernetes", "networking", "service-mesh", "Service mesh", "Add workload identity, mTLS, traffic policy and telemetry without losing application/network ownership or overloading sidecars/control planes.", C(
        "Data-plane proxy — sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries",
        "Control plane — distributes service discovery, certificates and policy to proxies",
        "Workload identity — trust-domain/service-account identity authenticates peers rather than IP alone",
        "mTLS — encrypts/authenticates service traffic while certificate issuance/rotation becomes critical",
        "Authorization policy — L4/L7 service identity rules complement Kubernetes NetworkPolicy",
        "Traffic policy — retries/timeouts/circuit/outlier/load balancing can amplify or mask application behavior",
        "Telemetry — proxy metrics/traces improve path visibility at cardinality/resource cost",
        "Injection/attachment — workloads missing sidecar/ambient enrollment can bypass expected controls",
        "Control-plane outage — existing proxy config may continue while new workloads/certs/routes degrade",
        "Upgrade — proxy/control/API skew and canary revision migration prevent fleet-wide breakage",
    ), ("kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{\"/\"}{.metadata.name}{\" \"}{.spec.containers[*].name}{\"\\n\"}{end}' | rg 'proxy'", "istioctl proxy-status", "istioctl analyze -A", "linkerd check"), "https://istio.io/latest/docs/concepts/what-is-istio/"),

    Leaf("06-kubernetes", "storage", "pv-pvc-storageclass", "PersistentVolumes, PVCs and StorageClasses", "Bind workload storage requirements to topology-aware provisioned volumes with explicit retention and expansion.", C(
        "PersistentVolume — cluster object representing provisioned storage and reclaim policy",
        "PersistentVolumeClaim — namespaced request for class, capacity, access mode and volume mode",
        "StorageClass — provisioner and parameters define dynamic storage policy/default",
        "Immediate binding — provisions/binds before scheduling and can choose wrong topology",
        "WaitForFirstConsumer — delays provisioning until scheduler knows Pod node topology",
        "Access mode — RWO/ROX/RWX/RWOP express supported attachment, not application concurrency safety",
        "Volume mode — Filesystem mounts a formatted FS; Block exposes raw device",
        "Reclaim policy — Delete/Retain controls storage after claim release and data lifecycle",
        "Volume expansion — controller/node/filesystem phases must support and report status",
        "Finalizers/protection — prevent deleting bound/in-use objects until controllers finish cleanup",
    ), ("kubectl get sc,pv,pvc -A", "kubectl describe pvc NAME -n NS", "kubectl get pv PV -o yaml", "kubectl get events -n NS --field-selector=involvedObject.kind=PersistentVolumeClaim"), "https://kubernetes.io/docs/concepts/storage/persistent-volumes/"),
    Leaf("06-kubernetes", "storage", "csi-snapshots-backup", "CSI, snapshots and Kubernetes backup", "Provision/attach/mount/snapshot/restore data and reconstruct cluster/application state with tested consistency.", C(
        "CSI controller — external components provision/delete/attach/snapshot/resize volumes",
        "CSI node plugin — stages/publishes/mounts volumes on each node",
        "CSIDriver/CSINode — advertise driver lifecycle and node topology/capability",
        "VolumeAttachment — records controller attach intent/status for attachable storage",
        "VolumeSnapshotClass — selects snapshot driver, deletion policy and parameters",
        "VolumeSnapshot/content — namespaced request and cluster snapshot handle mirror PVC/PV model",
        "Crash consistency — block snapshot alone may not capture application transaction consistency",
        "Velero/resource backup — captures API objects and integrates volume backup methods under plugin limits",
        "Restore ordering — CRDs/operators/secrets/classes/data/workloads and identities must be reconstructed coherently",
        "Restore validation — application queries/checksums and measured RPO/RTO prove recovery",
    ), ("kubectl get csidriver,csinode,volumeattachment", "kubectl get volumesnapshotclass,volumesnapshot,volumesnapshotcontent -A", "kubectl logs -n kube-system -l app=csi-controller --all-containers", "velero backup get && velero restore get"), "https://kubernetes.io/docs/concepts/storage/volume-snapshots/"),

    Leaf("06-kubernetes", "security", "authn-rbac-serviceaccounts", "Kubernetes authentication, RBAC and ServiceAccounts", "Bind short-lived identities to the minimum verbs/resources/namespaces without escalation paths.", C(
        "Authentication — client cert, bearer token, OIDC/webhook identifies user/groups or ServiceAccount",
        "Authorization — RBAC/webhook/node/ABAC modes decide a request after authentication",
        "Role/ClusterRole — namespaced/cluster rule collections over API group/resource/subresource/verb",
        "RoleBinding — grants a Role or ClusterRole within one namespace",
        "ClusterRoleBinding — grants cluster-wide and is a high-blast-radius object",
        "ServiceAccount — namespaced workload identity with projected bound token support",
        "TokenRequest — short-lived audience/expiry-bound token avoids legacy static secret tokens",
        "Impersonation — powerful diagnostic/delegation verb that must be narrowly controlled/audited",
        "bind/escalate — permissions can create bindings/roles beyond a caller's current rights",
        "Workload escalation — create Pod can expose mounted secrets, service account, host/device or node credentials",
    ), ("kubectl auth whoami", "kubectl auth can-i --list -n NS", "kubectl auth can-i VERB RESOURCE --as=USER --as-group=GROUP -n NS", "kubectl create token SA -n NS --duration=10m"), "https://kubernetes.io/docs/reference/access-authn-authz/rbac/"),
    Leaf("06-kubernetes", "security", "pod-security", "Pod and node workload security", "Constrain container privilege, host access, syscalls, identities and filesystems through safe defaults and admission.", C(
        "runAsNonRoot — prevents UID 0 execution when image/runtime identity can be determined",
        "allowPrivilegeEscalation — blocks gaining more privilege through exec/setuid and is affected by privilege/capabilities",
        "Capabilities — drop ALL and add only exact kernel privileges required",
        "Seccomp — RuntimeDefault/local profiles reduce syscall attack surface",
        "Read-only root — prevents image filesystem mutation and requires explicit writable volumes",
        "Privileged container — largely bypasses container isolation and is equivalent to host-level trust",
        "Host namespaces/path — hostNetwork/PID/IPC/hostPath expose shared host attack surface",
        "Pod Security Standards — privileged/baseline/restricted profiles define portable control sets",
        "Pod Security Admission — namespace labels enforce/audit/warn standards by version",
        "Node hardening — kernel/runtime/kubelet/metadata/patch and tenant separation remain outside Pod spec",
    ), ("kubectl get ns --show-labels", "kubectl label ns NS pod-security.kubernetes.io/enforce=restricted", "kubectl get pods -A -o json | jq '.items[] | select(any(.spec.containers[]; .securityContext.privileged==true))'", "kubectl apply --dry-run=server -f pod.yaml"), "https://kubernetes.io/docs/concepts/security/pod-security-standards/"),
    Leaf("06-kubernetes", "security", "secrets-configmaps", "Kubernetes Secrets and ConfigMaps", "Distribute versioned configuration and sensitive values with reload, encryption, access and rotation design.", C(
        "ConfigMap — non-secret key/file configuration consumed via API, env or projected volume",
        "Secret — API object whose data is base64-encoded and requires encryption/RBAC controls",
        "Environment consumption — value is fixed at process start and appears in process/runtime surfaces",
        "Projected volume — kubelet updates mounted data eventually using atomic directory/symlink behavior",
        "subPath — individual file mount does not receive ordinary projected updates",
        "Immutable object — prevents accidental mutation and can improve watch load; version name for changes",
        "Encryption at rest — API server provider encrypts selected resources in etcd with key rotation procedure",
        "External secrets/CSI — synchronizes or mounts secret-manager values with availability/identity trade-offs",
        "Rotation — dual credential/version, reload/restart and dependent revocation must avoid outage",
        "Checksum rollout — template annotation hash deliberately restarts Pods on immutable/config change",
    ), ("kubectl get configmap,secret -n NS", "kubectl get secret NAME -n NS -o jsonpath='{.data.KEY}' | base64 -d", "kubectl auth can-i get secrets --as=system:serviceaccount:NS:SA -n NS", "kubectl create configmap NAME --from-file=config.yaml --dry-run=client -o yaml"), "https://kubernetes.io/docs/concepts/configuration/secret/"),
    Leaf("06-kubernetes", "security", "admission-policies-webhooks", "Kubernetes admission policies and webhooks", "Validate or mutate API writes without turning an unreliable policy service into a cluster outage or bypass.", C(
        "Admission sequence — mutation precedes object schema/defaulting stages and validation before persistence",
        "ValidatingAdmissionPolicy — CEL policy in API server avoids external webhook network dependency",
        "Policy binding — selects parameters, namespaces/resources and validation actions",
        "Mutating webhook — patches objects and must be idempotent/reinvocation aware",
        "Validating webhook — accepts/rejects after mutations and sees admission review context",
        "failurePolicy — Fail protects policy but can block all writes; Ignore preserves availability with bypass risk",
        "Timeout/match conditions — bound webhook latency and exclude irrelevant/system/recovery paths deliberately",
        "SideEffects/dry-run — webhook declaration must truthfully support dry-run safety",
        "Certificate/service — API server must reach trusted webhook endpoint with automated rotation",
        "Observability — admission latency/rejection/error/timeout plus policy version explains API failures",
    ), ("kubectl get validatingadmissionpolicy,validatingadmissionpolicybinding", "kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration", "kubectl apply --dry-run=server -f object.yaml", "kubectl get --raw /metrics | rg admission"), "https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/"),
    Leaf("06-kubernetes", "security", "multitenancy", "Kubernetes multi-tenancy", "Isolate tenant identity, data, network, compute, policy, telemetry and noisy-neighbor effects under an explicit threat model.", C(
        "Namespace tenancy — soft/shared control boundary needing RBAC, policy, quotas and trusted cluster admins",
        "Cluster-per-tenant — stronger failure/control isolation at fleet cost and operational scale",
        "RBAC boundary — tenant admins must not create cluster-wide or privilege-escalating resources",
        "Network isolation — default deny plus controlled ingress/egress/DNS prevents lateral paths",
        "ResourceQuota — aggregate namespace object/compute limits constrain consumption/admission",
        "LimitRange — default/min/max per-object requests/limits and can affect scheduling unexpectedly",
        "Node isolation — taints/dedicated pools/runtime classes protect stronger/noisy workloads",
        "Secret/data isolation — separate workload identity, storage, KMS and backup/restore paths",
        "Telemetry isolation — tenant identifiers/access/redaction/quotas prevent cross-tenant leak and cardinality abuse",
        "Policy delegation — platform owns guardrails; tenant owns namespaced workloads within transparent exceptions",
    ), ("kubectl get resourcequota,limitrange,networkpolicy,rolebinding -A", "kubectl auth can-i --list --as=TENANT -n TENANT_NS", "kubectl top pod -n TENANT_NS", "kubectl get pods -n TENANT_NS -o wide"), "https://kubernetes.io/docs/concepts/security/multi-tenancy/"),

    Leaf("06-kubernetes", "scheduling-autoscaling", "requests-limits-qos", "Resource requests, limits and QoS", "Schedule and isolate CPU, memory, ephemeral storage and extended resources from measured workload needs.", C(
        "CPU request — scheduler reservation and HPA utilization denominator, expressed in cores/millicores",
        "CPU limit — cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores",
        "Memory request — scheduling reservation/eviction signal rather than guaranteed preallocation",
        "Memory limit — cgroup hard boundary can OOM-kill a container",
        "Ephemeral-storage — writable layer/log/emptyDir request/limit interacts with node disk eviction",
        "Guaranteed QoS — equal CPU/memory request/limit on every container gives strongest eviction priority",
        "Burstable QoS — at least one request/limit but not Guaranteed; common production class",
        "BestEffort QoS — no requests/limits and first under resource pressure",
        "LimitRange — injects/enforces per-container defaults and bounds",
        "ResourceQuota — namespace aggregate limits can reject objects or cap priority/storage/GPU counts",
    ), ("kubectl top pod -A --containers", "kubectl describe node NODE", "kubectl get pod POD -o jsonpath='{.status.qosClass}'", "kubectl get resourcequota,limitrange -A"), "https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/"),
    Leaf("06-kubernetes", "scheduling-autoscaling", "placement", "Affinity, taints and topology placement", "Express required hardware/data locality and preferred spread without creating impossible or fragile scheduling constraints.", C(
        "nodeSelector — exact label match for simple required placement",
        "Node affinity — expressive required/preferred label predicates evaluated at scheduling",
        "Pod affinity — co-locates Pods by labels/topology and can be expensive/fragile",
        "Pod anti-affinity — spreads/fences replicas but hard rules can block during failures",
        "Taint — repels Pods by NoSchedule/PreferNoSchedule/NoExecute effects",
        "Toleration — permits but does not require placement on tainted nodes",
        "Topology spread — controls skew across zones/nodes using label selector and unsatisfiable behavior",
        "Volume topology — PV zone/access constrains feasible nodes after/before binding",
        "Well-known labels — topology/arch/os/instance attributes should be trusted and lifecycle-managed",
        "Constraint diagnosis — scheduler events enumerate failed filters; removing safety constraints blindly is not repair",
    ), ("kubectl get nodes --show-labels", "kubectl get events -A --field-selector=reason=FailedScheduling", "kubectl describe pod POD -n NS", "kubectl taint node NODE key=value:NoSchedule"), "https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/"),
    Leaf("06-kubernetes", "scheduling-autoscaling", "hpa-vpa-keda", "HPA, VPA and KEDA", "Scale replicas/resources from stable demand signals while avoiding feedback, metric loss and unsafe churn.", C(
        "HPA ratio — desired replicas derives current/target metric with tolerance and missing/not-ready handling",
        "Resource utilization — usage divided by requests means bad/missing requests break CPU/memory scaling",
        "Custom/external metric — adapter exposes application/provider signal with availability/cardinality semantics",
        "HPA behavior — stabilization and policies bound scale-up/down rate",
        "VPA recommendation — learns requests from usage history and can restart Pods to apply changes",
        "VPA/HPA interaction — both changing CPU requests/replicas can create feedback without design",
        "KEDA trigger — event source drives Scale subresource and supports activation/scale-to-zero",
        "Queue age/depth — leading demand signal but must account for service time/token work",
        "Scale-to-zero — cold start and missing metric/activation path must meet SLO",
        "Downstream protection — replica scale cannot exceed database/provider/tenant capacity",
    ), ("kubectl get hpa -A", "kubectl describe hpa NAME -n NS", "kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1 | jq", "kubectl get scaledobject -A", "kubectl get vpa -A"), "https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/"),
    Leaf("06-kubernetes", "scheduling-autoscaling", "node-autoscaling", "Cluster Autoscaler, Karpenter and node lifecycle", "Provision/remove nodes from unschedulable Pods while preserving topology, disruption, compatibility and spend.", C(
        "Unschedulable Pod — requests/constraints are the node capacity specification",
        "Node group template — Cluster Autoscaler simulates predefined group capacity/labels/taints",
        "Karpenter NodePool — provisions flexible nodes directly from constraints/provider class",
        "Scale-down candidate — utilization and movable Pods determine safe removal",
        "PDB/local storage/system Pod — eviction constraints can block consolidation",
        "Cloud quota/capacity — autoscaler decision can be correct while provider launch fails",
        "Node bootstrap — image, kubelet, runtime, CNI/CSI/device plugin must become Ready before capacity",
        "Diversification — multiple compatible types/AZs improve capacity and Spot resilience",
        "Drift/expiration — node image/config updates require controlled replacement",
        "Budget — maximum nodes/resources plus admission and cloud budget prevent runaway scale",
    ), ("kubectl get pods -A --field-selector=status.phase=Pending", "kubectl logs -n kube-system deploy/cluster-autoscaler --since=30m", "kubectl logs -n kube-system deploy/karpenter --since=30m", "kubectl describe node NODE"), "https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/"),
    Leaf("06-kubernetes", "scheduling-autoscaling", "disruption-priority", "PDB, priority, preemption and eviction", "Control voluntary disruption and overload scheduling without assuming protection from node failure.", C(
        "PDB — minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods",
        "Eviction API — admission checks PDB and graceful deletion compared with direct delete",
        "Unhealthy eviction policy — controls drain behavior for unhealthy Pods under supported API",
        "PriorityClass — numeric scheduling/eviction priority with globalDefault/preemption policy",
        "Preemption — scheduler removes lower-priority Pods when that can make a high-priority Pod feasible",
        "Nominated node — indicates expected preemption placement but can change before binding",
        "Node-pressure eviction — kubelet reclaims resources based on signals/QoS/priority and is involuntary",
        "Taint eviction — NoExecute taint can evict non-tolerating Pods after tolerationSeconds",
        "Drain — cordons then evicts/deletes workload Pods while respecting flags/PDB",
        "Overprotection — strict PDB/priority can block maintenance or starve lower-value platform services",
    ), ("kubectl get pdb,priorityclass -A", "kubectl describe pdb NAME -n NS", "kubectl drain NODE --ignore-daemonsets --dry-run=server", "kubectl get events -A | rg 'Preempt|Evict|Disruption'"), "https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/"),

    Leaf("06-kubernetes", "packaging-extensions", "helm-kustomize", "Helm and Kustomize", "Package and customize Kubernetes desired state with reproducible rendering, schema/policy tests and safe lifecycle.", C(
        "Helm chart — templates/default values/schema/dependencies/hooks package Kubernetes resources",
        "Values merge — files/--set precedence and type coercion can produce surprising rendered output",
        "Release secret/state — Helm records revisions in cluster for upgrade/history/rollback",
        "Hook — ordered lifecycle resource can execute irreversible work outside ordinary rollback",
        "Atomic upgrade — waits and rolls back rendered resources on failure but cannot undo external side effects",
        "Chart dependency — version/repository lock and provenance affect supply-chain trust",
        "Kustomize base — reusable raw resources without templating",
        "Overlay/patch — environment-specific changes use strategic/JSON patches, replacements and generators",
        "Generator hash — ConfigMap/Secret name suffix triggers rollout when references update",
        "Render validation — schema, API conformance, policy, diff and server dry-run catch different errors",
    ), ("helm lint CHART", "helm template RELEASE CHART -f values.yaml", "helm upgrade --install RELEASE CHART --atomic --timeout 10m", "kubectl kustomize OVERLAY", "kubectl diff -k OVERLAY"), "https://helm.sh/docs/topics/charts/"),
    Leaf("06-kubernetes", "packaging-extensions", "crds-operators", "CRDs and operators", "Extend Kubernetes with versioned APIs and idempotent controllers that report status and clean external state safely.", C(
        "CRD schema — structural OpenAPI validation/defaulting/pruning define accepted desired state",
        "Reconciler — level-based idempotent loop converges desired and observed state under retries",
        "Status subresource — controller reports conditions/observedGeneration without mutating spec",
        "Finalizer — ensures external cleanup before deletion completes and can stick when controller fails",
        "Owner reference — drives garbage collection for Kubernetes child resources",
        "Work queue — event keys, rate limiting and retries coalesce reconciliation",
        "Webhook — default/validate/convert custom resources with HA/certificate/timeout needs",
        "Version conversion — served/storage versions and conversion preserve compatibility",
        "Controller leader election — only one active replica performs shared mutation while others stand by",
        "RBAC/cache scope — controller watches and permissions should be limited to owned resources/tenants",
    ), ("kubectl get crd", "kubectl explain CRD_KIND.spec --recursive", "kubectl get CRD_KIND NAME -o yaml", "kubectl get events --field-selector=involvedObject.kind=CRD_KIND", "kubectl logs deploy/CONTROLLER --since=30m"), "https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/"),
    Leaf("06-kubernetes", "packaging-extensions", "gitops", "Argo CD, Flux and GitOps", "Continuously reconcile signed reviewed desired state across clusters with explicit tenancy, promotion, secrets and emergency workflow.", C(
        "Desired source — Git/OCI revision plus render inputs is the audit/reconciliation truth",
        "Reconciliation — controller compares live and desired then applies/prunes under policy",
        "Health — resource-specific status estimates rollout but needs user/SLO verification",
        "Sync wave/hook — orders dependencies/migrations with failure and idempotency concerns",
        "ApplicationSet/Flux Kustomization — generates fleet/environment instances from controlled templates",
        "Project/tenant boundary — limits source repositories, clusters/namespaces and resource kinds",
        "Prune/self-heal — deletes drifted/removed resources and can amplify a bad commit",
        "Secret workflow — encrypted/external secret references prevent plaintext Git while preserving rotation",
        "Promotion — pull request updates immutable artifact/version between environment sources",
        "Emergency change — pause/reconcile source quickly so controller does not revert mitigation",
    ), ("argocd app diff APP", "argocd app sync APP --revision REV", "argocd app wait APP --health --sync", "flux get kustomizations -A", "flux reconcile kustomization NAME --with-source"), "https://argo-cd.readthedocs.io/en/stable/"),

    Leaf("06-kubernetes", "operations", "observability", "Kubernetes observability", "Correlate API/control-plane, node, workload, network, storage and application signals without uncontrolled telemetry cost.", C(
        "kube-state-metrics — exposes object desired/status metrics rather than container usage",
        "Metrics Server — lightweight resource metrics for top/HPA, not a long-term monitoring backend",
        "kubelet/cAdvisor — node/container CPU/memory/filesystem/network metrics under version/runtime coverage",
        "Control-plane metrics — API latency/errors/inflight, scheduler attempts, controller queue and etcd latency/space",
        "Events — best-effort short-retention diagnostic records, not an audit log",
        "Audit log — API request identity/verb/resource/stage evidence with privacy/volume policy",
        "Container logs — stdout/stderr rotation/collection requires node agent and structured context",
        "Network telemetry — DNS/CNI/conntrack/eBPF/flow/LB signals locate service paths",
        "Storage telemetry — CSI operations, attach/mount, volume latency/capacity and snapshot state",
        "Cardinality — Pod/container/UID labels already churn; user/request IDs must not become metric labels",
    ), ("kubectl top node && kubectl top pod -A --containers", "kubectl get --raw /metrics | head", "kubectl get events -A --sort-by=.metadata.creationTimestamp", "kubectl logs -n monitoring deploy/prometheus --since=30m"), "https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/"),
    Leaf("06-kubernetes", "operations", "upgrades", "Kubernetes upgrades and API deprecations", "Upgrade control plane, nodes, add-ons, CRDs and workloads within version-skew and compatibility evidence.", C(
        "Version skew — supported kubelet/kube-proxy/controller relationships bound rolling upgrade order",
        "API deprecation — served versions are removed on schedule and manifests/clients/controllers must migrate",
        "Storage version — existing objects may remain encoded in old version until storage migration/update",
        "Control-plane first — managed/self-managed procedures normally upgrade API before nodes within skew",
        "Add-on compatibility — CNI/CSI/CoreDNS/proxy/metrics/admission/operator versions need matrices",
        "Canary node pool — validates image/runtime/kernel/driver/workload before fleet drain",
        "Drain/PDB — maintenance success depends on budgets, state/storage and graceful termination",
        "CRD conversion — webhook and stored-version correctness must precede removing versions",
        "Rollback — control-plane downgrade is often unavailable, so backups/blue-green cluster migration matter",
        "Qualification — conformance plus real workload/SLO/security/DR validates more than node Ready",
    ), ("kubectl version", "kubectl get --raw /version", "kubectl get --raw /metrics | rg apiserver_requested_deprecated_apis", "kubectl get crd -o json | jq '.items[] | {name:.metadata.name,storedVersions:.status.storedVersions}'"), "https://kubernetes.io/releases/version-skew-policy/"),
    Leaf("06-kubernetes", "operations", "backup-dr-etcd", "Kubernetes backup and disaster recovery", "Reconstruct API desired state and application-consistent data, identity, network and platform dependencies within tested RPO/RTO.", C(
        "etcd snapshot — captures API storage for self-managed control planes with matching encryption/config needs",
        "Resource backup — exported API objects need CRDs, versions, ownership and secret protection",
        "Volume backup — CSI snapshot/file backup needs application consistency and external snapshot retention",
        "Velero — orchestrates Kubernetes resources and provider volume/plugin backups under coverage limits",
        "Cluster rebuild — IaC/bootstrap/add-ons/controllers restore platform before workloads",
        "Restore ordering — CRDs/operators, namespaces/policy, secrets, storage, data, services and apps",
        "Identity/KMS — OIDC, CAs, encryption keys and cloud roles are recovery dependencies",
        "RPO — latest consistent recoverable point includes async replication/backup lag",
        "RTO — provisioning, data transfer, model/cache warm and validation time determine recovery",
        "Restore test — isolated environment plus user/data correctness and failback proves runbook",
    ), ("ETCDCTL_API=3 etcdctl snapshot save snapshot.db", "ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table", "velero backup create NAME --include-namespaces NS --wait", "velero restore create --from-backup NAME --wait"), "https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/"),
    Leaf("06-kubernetes", "operations", "troubleshooting-kubectl", "Kubernetes troubleshooting and kubectl", "Diagnose desired state through API, controllers, scheduler, node/runtime, network, storage and application using read-only evidence first.", C(
        "Object status/conditions — observedGeneration, reason and message show controller interpretation",
        "Events — scheduling, pull, mount, probe and controller records point to the first failing transition",
        "Previous logs — retrieve terminated container output during CrashLoopBackOff",
        "Ephemeral debug — add diagnostic tooling without rebuilding the production image",
        "Raw API/jsonpath/jq — inspect exact fields and aggregated status rather than visually scanning YAML",
        "Node debug — enter host namespaces/filesystem carefully for kubelet/runtime/CNI evidence",
        "EndpointSlice — confirms whether readiness/selector produced routable Service targets",
        "VolumeAttachment/CSI logs — separate scheduler topology from controller attach and node mount",
        "Managed fields — identify which manager owns or overwrites a field",
        "Source reconciliation — repair Git/Helm/operator/IaC after any imperative mitigation",
    ), ("kubectl describe pod POD -n NS", "kubectl logs POD -n NS --all-containers --previous", "kubectl debug -it POD -n NS --image=nicolaka/netshoot --target=CONTAINER", "kubectl get events -A --sort-by=.lastTimestamp", "kubectl cluster-info dump --output-directory=./dump"), "https://kubernetes.io/docs/tasks/debug/"),

    Leaf("06-kubernetes", "gpu-llmops", "gpu-operator-dra", "GPU Operator, device plugins and DRA", "Expose, allocate, monitor and lifecycle GPU devices through a qualified driver/runtime/Kubernetes integration.", C(
        "Driver — host kernel module/firmware is the foundation and must match hardware/kernel/runtime",
        "Container toolkit — injects device/library/runtime configuration into GPU containers",
        "Device plugin — advertises integer extended resources and allocates device nodes",
        "GPU Feature Discovery — labels node hardware/capabilities for scheduling policy",
        "GPU Operator — reconciles driver/toolkit/plugin/GFD/DCGM/MIG components under one version matrix",
        "DRA ResourceSlice — driver publishes device inventory/attributes/topology",
        "DeviceClass — admin policy selects device characteristics using CEL",
        "ResourceClaim — workload requests and records allocated/prepared device",
        "Device health — unhealthy device reduces future allocatable or reports claim/Pod status under mechanism",
        "Canary upgrade — drain one pool, update driver/operator/runtime, qualify CUDA/NCCL/model then expand",
    ), ("kubectl get pods -n gpu-operator -o wide", "kubectl get nodes -o custom-columns='NAME:.metadata.name,GPU:.status.allocatable.nvidia\\.com/gpu'", "kubectl get deviceclass,resourceslice,resourceclaim -A", "kubectl exec -n ai POD -- nvidia-smi"), "https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/"),
    Leaf("06-kubernetes", "gpu-llmops", "gpu-sharing-scheduling", "GPU sharing, scheduling and queueing", "Choose whole GPU, MIG, time-slicing or MPS and schedule scarce topology-aware capacity fairly and safely.", C(
        "Whole GPU — simple exclusive allocation offers strongest default isolation at fragmentation cost",
        "MIG — supported GPUs partition hardware memory/fault domains into fixed profiles",
        "Time-slicing — oversubscribes compute without memory/fault isolation and weakens attribution",
        "CUDA MPS — coordinates compatible processes for concurrency with separate operational/isolation constraints",
        "GPU fragmentation — free devices/profiles spread across nodes may not fit multi-GPU Pods",
        "Gang scheduling — admits all workers/resources together so distributed jobs do not deadlock holding partial capacity",
        "Fair sharing — queues/cohorts borrow quota while preventing one tenant from monopolizing GPUs",
        "Topology — NUMA/PCIe/NVLink/NVSwitch/NIC placement determines collective/serving performance",
        "Priority/preemption — scarce urgent workloads need policy, checkpoint/drain and starvation protection",
        "Quota/accounting — tenant GPU/profile/time/token budgets need admission and usage measurement",
    ), ("kubectl describe node GPU_NODE", "kubectl get events -A --field-selector=reason=FailedScheduling", "nvidia-smi topo -m", "nvidia-smi mig -lgi", "kubectl get workload,localqueue,clusterqueue -A"), "https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html"),
    Leaf("06-kubernetes", "gpu-llmops", "model-serving", "KServe, vLLM and Triton on Kubernetes", "Operate model artifact loading, high-throughput runtime, routing, readiness, batching and release on accelerators.", C(
        "InferenceService — KServe resource declares predictor/runtime/storage/traffic under deployment mode",
        "ServingRuntime — reusable supported model format/container/protocol contract",
        "vLLM continuous batching — dynamically combines active sequences for throughput",
        "PagedAttention/KV cache — manages noncontiguous KV blocks and capacity/eviction",
        "Triton model repository — versioned model/config layout controls loading and backend",
        "Dynamic batching — waits briefly to combine requests under latency/shape limits",
        "Model readiness — exact weights/tokenizer/config loaded, warmed and able to respond",
        "OpenAI/V2 protocol — northbound schema compatibility does not guarantee semantic feature parity",
        "Model cache — verified shared/local artifacts reduce cold start but need version/tenant/disk lifecycle",
        "Canary/shadow — route controlled traffic and gate latency/error/quality/cost before promotion",
    ), ("kubectl get inferenceservice,servingruntime -A", "kubectl describe inferenceservice NAME -n NS", "kubectl logs -n NS POD --all-containers", "curl -s http://ENDPOINT/metrics | rg 'queue|token|cache|request'"), "https://kserve.github.io/website/docs/model-serving/"),
    Leaf("06-kubernetes", "gpu-llmops", "inference-autoscaling", "Inference autoscaling and capacity", "Scale model replicas and accelerator nodes from token queue and SLO while accounting for long cold starts and scarce capacity.", C(
        "Queue depth/age — leading overload signal when arrival work exceeds serving goodput",
        "Predicted token work — input/output length estimate better reflects heterogeneous request cost",
        "TTFT/inter-token — user latency separates queue/prefill from decode behavior",
        "KV cache pressure — memory/concurrency saturation can predict rejection before GPU utilization",
        "HPA/KEDA — scales replicas from custom/external metrics with stabilization and activation",
        "Node autoscaler — provisions GPU nodes only after replicas become Pending",
        "Cold path — cloud capacity, boot, driver/plugin, image, model download/load/warm dominate delay",
        "Warm buffer — preprovisioned nodes/replicas/cache trades cost for burst SLO",
        "Scale down — drain streams, protect cache/work, PDB/consolidation and minimum capacity",
        "Capacity fallback — diversified approved hardware/Region/provider requires compatibility/quality/residency tests",
    ), ("kubectl describe hpa NAME -n NS", "kubectl get scaledobject -A", "kubectl get pods -A --field-selector=status.phase=Pending", "kubectl logs -n kube-system deploy/karpenter --since=30m", "curl -s http://MODEL/metrics"), "https://docs.aws.amazon.com/eks/latest/userguide/ml-inference-autoscaling.html"),
    Leaf("06-kubernetes", "gpu-llmops", "llmops-release-evaluation", "LLMOps release and evaluation on Kubernetes", "Bind prompts, models, RAG indexes, runtimes and evaluators into reproducible quality-gated progressive delivery.", C(
        "Release manifest — exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity",
        "Golden dataset — versioned owned task examples and edge/adversarial cases",
        "Offline evaluation — compares quality/safety/latency/cost before production under reproducible inputs",
        "Model-as-judge — scalable evaluator with bias/non-determinism/calibration and version risk",
        "Shadow evaluation — production input copy provides realism under privacy/side-effect/cost controls",
        "Canary — small user/tenant traffic with automated infrastructure and quality rollback gates",
        "Champion/challenger — compares incumbent/candidate while retaining explicit promotion authority",
        "Prompt/index drift — prompt or retrieval changes are model-release changes and need lineage/eval",
        "Rollback — retains prior artifacts/config/index and handles in-flight/cache/schema compatibility",
        "Audit — approval links dataset/evaluator/results/exception/actor to deployed revision",
    ), ("kubectl get deployment,inferenceservice -n inference -o yaml", "kubectl rollout history deployment/NAME -n inference", "argocd app history APP", "python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl"), "https://kserve.github.io/website/docs/model-serving/predictive-inference/rollout-strategies/canary-examples"),
    Leaf("06-kubernetes", "gpu-llmops", "gateway-rag", "LLM gateway and RAG on Kubernetes", "Operate tenant-aware gateway, retrieval, vector/search and model paths with policy, backpressure, security and observability.", C(
        "Gateway identity — authenticates workload/user and derives tenant/project/policy context",
        "Model route — alias selects approved provider/model/region/capability under health and budget",
        "Token quota — rate/concurrency/queued work protects fairness/provider/GPU capacity",
        "Streaming retry — after output starts, transparent retry can duplicate content/effect/billing",
        "Ingestion pipeline — parses/chunks/embeds/indexes source documents idempotently with lineage",
        "Authorization filter — retrieval applies source ACL/tenant constraints before returning context",
        "Hybrid retrieval/rerank — dense/sparse candidates plus reranker trade recall/latency/cost",
        "Prompt injection — retrieved content is untrusted data and cannot grant tool/system authority",
        "Freshness/deletion — source changes, right-to-delete, re-embedding and cache/index versions reconcile",
        "End-to-end trace — gateway→retrieval→rerank→model→tool spans include safe IDs/tokens/latency/cost/eval",
    ), ("kubectl get gateway,httproute,networkpolicy -A", "kubectl top pod -n ai-platform --containers", "kubectl logs -n ai-platform deploy/llm-gateway --since=30m", "curl -N https://gateway.example/v1/chat/completions -H 'Authorization: Bearer TOKEN' -d @request.json"), "https://gateway-api.sigs.k8s.io/"),
]


def split_concept(entry: str) -> tuple[str, str]:
    name, sep, explanation = entry.partition(" — ")
    if not sep:
        return entry, f"{entry} is a required mechanism in this leaf and must be understood in context."
    return name, explanation.rstrip(".") + "."


def safe_id(value: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "-", value.upper()).strip("-")


def branch_overview(area: str, branch: str, leaves: list[Leaf]) -> str:
    title = branch.replace("-", " ").title()
    concepts = []
    for leaf in leaves:
        concepts.extend(split_concept(c)[0] for c in leaf.concepts[:3])
    diagram_nodes = "\n".join(f"  B --> S{i}[{leaf.title}]" for i, leaf in enumerate(leaves, 1))
    return f"""# {title}

This branch README connects the service chapters into one production capability. The root reading tree places each service chapter directly after this overview.

```mermaid
flowchart LR
  B[{title}]
{diagram_nodes}
```

## Branch learning contract

Learn the easy mental model first, run the read-only commands in a sandbox, render/apply the examples only in disposable environments, then break and repair one dependency at a time. Be able to connect these topics across the branch: {", ".join(concepts)}.

## Branch interview bank

See [questions-and-answers.md](questions-and-answers.md) for 60 additional branch-level questions and answers. Service-specific banks contain another 60 per service.
"""


def notes(leaf: Leaf) -> str:
    topic_names = [split_concept(c)[0] for c in leaf.concepts]
    return f"""# {leaf.title}

> Interview bank: [questions-and-answers.md](questions-and-answers.md) · Official documentation: <{leaf.docs}>

## Explanation

### What it is and why it exists

{junior_intro(leaf.title, leaf.area, leaf.purpose, topic_names)}

### History and evolution

{history_text(leaf.title, leaf.area, leaf.purpose)}

### How it works: the end-to-end path

{flow_diagram(leaf.title, leaf.area)}

The diagram is a feedback loop rather than a one-way provisioning sequence. A caller supplies identity and intent; the control plane validates and records that intent; asynchronous controllers, runtimes or managed infrastructure create the effective data plane; and status and telemetry feed the next decision. A successful API response can therefore mean only "the request was accepted," not "the workload outcome is healthy."

For **{leaf.title}**, the mechanisms participating in that loop are {", ".join(topic_names)}. Some run synchronously on the caller's request, while others converge later. This timing distinction explains many production surprises: the desired object can exist before capacity is ready, a data path can continue while its control plane is impaired, and a timeout can leave the final side effect unknown.

### Core concepts explained in detail

{concept_explanations(leaf.concepts, leaf.title, leaf.area)}

### Worked command and configuration example

{worked_example(leaf.commands, leaf.title)}

### Security and trust boundaries

Security begins with the actor and the exact operation, not with a network location. Human, workload, CI and service identities have different lifecycles; every hop must authenticate the relevant identity and authorize the action against the resource and current conditions. Network controls reduce reachable paths, while resource policy and application authorization decide what an already-reachable caller may do. Encryption protects data in transit or at rest, but key access, rotation, revocation and recovery are part of the same system.

The safe design minimizes public paths, long-lived credentials, wildcard permissions and implicit cross-tenant trust. It also protects the evidence plane: audit logs, traces and command history must not become a second copy of secrets or customer content. A production review should be able to identify the enforcement point, default behavior, bypass path, break-glass owner and proof that revoked access actually stops working.

### Reliability and failure behavior

Availability is an end-to-end property. The service depends on identity, quota, API/control-plane health, DNS and network paths, capacity, downstream services and any durable state required to recover. Replicas improve availability only when they occupy independent failure domains and clients can reach a healthy replica; a managed-service label does not remove customer responsibility for configuration, load, data correctness or recovery testing.

Timeouts, bounded retry budgets with jitter, idempotency, backpressure, load shedding and graceful drain control how failures spread. They must match the protocol and side-effect model. A timeout is ambiguous because the remote operation may have completed; blind retry is unsafe when the operation is not idempotent. Recovery is complete only when the original user action works and data, latency, error rate and backlog have returned to acceptable bounds.

### Performance, scaling and cost

Capacity planning starts with a work unit and a distribution, not an average utilization percentage. Relevant signals include request or job arrival rate, work size, latency percentiles, errors, queue age, saturation and service-specific limits. Scaling application replicas and provisioning underlying nodes, storage or provider quota are separate feedback loops with different delays. Cold starts and warm-up determine whether newly allocated capacity helps before the burst is over.

Total cost includes idle headroom, request or token work, storage and retention, cross-zone or cross-Region transfer, NAT/egress, observability, licenses and recovery capacity. The useful optimization target is cost per successful SLO- or quality-controlled outcome. A cheaper configuration that increases retries, operator toil, data risk or missed objectives can raise total cost.

### Observability and troubleshooting

Diagnosis follows the same path as the request. First establish time, user impact, identity and exact target; then compare desired configuration with observed status and recent changes. Continue through control-plane reconciliation, network and protocol evidence, runtime state, dependencies and resource saturation. Metrics show trends, logs explain discrete events, traces connect boundaries, profiles attribute resource use and audit logs explain security decisions.

The most useful next check is the one that distinguishes competing causes. A permission denial calls for policy-evaluation evidence, not a restart; a connection refusal means something different from a timeout; a pending resource with a scheduling reason differs from a running resource whose application is unready. Reversible mitigation stabilizes impact, while the durable repair updates Git, IaC, policy or the owning service and adds a regression test or alert.

### What you should be able to explain

Use this table only after reading the explanations above. It is a revision checklist, not a substitute for the lesson.

| # | Concept | What you must be able to explain |
|---:|---|---|
{capability_table(leaf.concepts)}

### Common interview traps

- Naming a feature without explaining request/resource lifecycle or failure semantics.
- Treating an allow, encryption checkbox, replica count or managed-service label as a complete security/reliability design.
- Mutating production before capturing identity, status, events, metrics, logs, audit and recent changes.
- Scaling the wrong layer or retrying overload/permanent errors.
- Omitting quotas, cold start, deletion/restore, observability cost or customer/tenant boundaries.

## Practice

{practice_session(leaf.title, leaf.area, leaf.commands)}
"""


def qna(leaf: Leaf, *, branch: bool = False) -> str:
    leaf_id = safe_id(("BRANCH-" if branch else "") + leaf.title)[:48]
    concepts = []
    for concept in leaf.concepts:
        name, description = split_concept(concept)
        concepts.append((name, usable_description(name, description, leaf.title, leaf.area).rstrip(".") + "."))
    while len(concepts) < 10:
        concepts += concepts
    concepts = concepts[:10]
    commands = list(leaf.commands) or ["inspect the service state"]

    out = [
        f"# {leaf.title} — interview questions and answers",
        "",
        f"> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.",
        "",
    ]

    def add_section(title: str, level: str, mode: str, entries: list[tuple[str, str, str]]):
        out.extend([f"## {title}", ""])
        for idx, (tag, question, answer) in enumerate(entries, 1):
            out.extend([
                f"### {leaf_id}-{level}{mode}-{idx:02d}",
                "",
                f"- [ ] {tag}**Question:** {question}",
                "",
                f"**Answer:** {answer}",
                "",
            ])

    jn = []
    for i, (name, explanation) in enumerate(concepts):
        tag = "**Code:** " if i in (7, 8, 9) else ""
        q = (f"What does `{commands[i % len(commands)]}` help you verify for {leaf.title}?" if tag
             else f"What is {name}, and why does it matter in {leaf.title}?")
        cmd = commands[i % len(commands)]
        mechanism_detail = answer_mechanism(name, explanation, leaf.title, leaf.area)
        evidence_detail = answer_evidence(name, explanation, leaf.title, leaf.area)
        a = (
            f"**Purpose.** `{cmd}` {command_explanation(cmd)}. "
            f"**Mechanism.** The relevant {leaf.title} concept is {name}: {explanation} The command reads one representation of desired or observed state; it does not by itself prove that every controller, dependency or user path is healthy. "
            "**Evidence.** Confirm identity, account/project/cluster, location and exact resource first, then preserve IDs, status/reason fields, timestamps and exit status. Compare them with source-controlled intent and a known healthy baseline, and correlate the nearest event, metric, log, trace or audit record. "
            "**Failure and trade-off.** Empty output, permission denial, stale state and an unavailable dependency require different next checks; immediately mutating the target destroys evidence and may widen impact. "
            f"**Production example.** During a {leaf.title} rollout, an operator uses this check to decide whether the fault is in accepted configuration, reconciliation or the live data path, and verifies the final repair from the original client."
            if tag
            else
            f"**Definition.** {explanation} "
            f"**Mechanism.** {mechanism_detail} Its guarantee applies only at its own boundary, so upstream identity, downstream dependencies and asynchronous convergence still matter. "
            f"**Evidence and failure behavior.** {evidence_detail} Compare those signals with desired configuration, workload shape and a known healthy baseline before choosing a mitigation. "
            "**Trade-off.** The choice normally balances simplicity, isolation, performance, recovery effort, portability and cost; moving a boundary solves one problem while shifting another to the caller or operator. "
            f"**Production example.** A team operating a service in which {name} matters records the workload and configuration baseline, injects one bounded failure in a sandbox, alerts on the first user-impact or saturation signal, and verifies recovery through the original {leaf.title} journey rather than an administrative green status alone."
        )
        jn.append((tag, q, a))
    add_section("Junior — normal conceptual and code questions", "J", "N", jn)

    jp = []
    for i, (name, explanation) in enumerate(concepts):
        cmd = commands[i % len(commands)]
        tag = "**Code:** " if i % 3 == 0 else ""
        q = f"A basic {name} check fails. What would you do first{' using the CLI' if tag else ''}?"
        a = (
            "**Stabilize and scope.** Confirm the user-visible symptom, start time, affected tenants/locations and current change owner; freeze unrelated changes and avoid retry amplification. "
            f"**Inspect.** Verify a read-only identity and exact target, then run `{cmd}`. This {command_explanation(cmd)}. Capture the full error, exit status, resource or request ID and timestamp. "
            f"**Reason about the mechanism.** {explanation} Compare declared and effective state, then inspect the immediately adjacent identity, control-plane, network, dependency or capacity layer instead of restarting blindly. "
            "**Mitigate versus repair.** A mitigation changes one reversible variable—such as pausing traffic or returning to a known compatible revision—without widening trust. The durable repair updates Git/IaC/policy or the owning service and adds a regression test or alert. "
            f"**Verify.** Repeat the original {leaf.title} client action, confirm correctness plus latency/error/backlog recovery, and record the timeline and prevention."
        )
        jp.append((tag, q, a))
    add_section("Junior — procedural and command questions", "J", "P", jp)

    mn = []
    for i, (left, left_expl) in enumerate(concepts):
        right, right_expl = concepts[(i + 1) % len(concepts)]
        tag = "**Configuration review:** " if i in (3, 6, 9) else ""
        q = f"Compare {left} with {right}. When would each change your design?"
        a = (
            f"**Definitions.** {left}: {left_expl} {right}: {right_expl} "
            f"**Mechanism.** In {leaf.title}, compare where each acts in the request or resource lifecycle, which state it owns, whether its result is synchronous or eventually reconciled, and how callers observe completion. They may be complementary layers rather than substitutes. "
            "**Decision criteria.** Select using workload shape and protocol, identity and tenant isolation, failure-domain independence, consistency and recovery contract, latency/throughput limits, team ownership and total cost. "
            "**Failure evidence.** State which metric, event, status field or controlled test would distinguish failure of one from the other, and how rollback differs. "
            f"**Production example.** For a production {leaf.title} design, use the simpler option until measured SLO, isolation, scale or recovery evidence crosses an explicit threshold; document that threshold so the decision can be revisited instead of becoming permanent folklore."
        )
        mn.append((tag, q, a))
    add_section("Mid-level — normal, comparison and configuration questions", "M", "N", mn)

    mp = []
    for i, (name, explanation) in enumerate(concepts):
        cmd = commands[i % len(commands)]
        tag = "**CLI/debugging:** " if i % 2 == 0 else ""
        q = f"Production is degraded around {name}; walk through diagnosis, mitigation and durable repair."
        a = (
            "**Incident control.** Declare impact, severity, owner, communications cadence and abort criteria; freeze risky changes and preserve evidence. Segment by tenant, location, revision and request type to reduce the search space. "
            f"**Diagnosis.** Start with `{cmd}` plus recent changes and the user-facing SLI. The command {command_explanation(cmd)}. Walk identity/policy → API/control-plane reconciliation → DNS/network/TLS → runtime/data path → dependency → quota/capacity, stopping when evidence discriminates the first broken transition. "
            f"**Mechanism.** {explanation} This matters because mitigation at the wrong layer can leave the cause intact or amplify load. "
            "**Mitigation.** Bound retries, shed or drain traffic, pause reconciliation or return to a known compatible revision only when the action is reversible and preserves tenant/data guarantees. Do not treat broad permission or an unqualified failover target as recovery. "
            f"**Durable repair and proof.** Update the {leaf.title} source of truth, add a regression test and leading alert, verify the original user outcome plus correctness and backlog, and rehearse the revised runbook in a sandbox or game day."
        )
        mp.append((tag, q, a))
    add_section("Mid-level — procedural, CLI and troubleshooting questions", "M", "P", mp)

    sn = []
    for i, (name, explanation) in enumerate(concepts):
        n2, e2 = concepts[(i + 3) % len(concepts)]
        n3, e3 = concepts[(i + 6) % len(concepts)]
        tag = "**Architecture/configuration:** " if i % 2 else ""
        q = f"Design a production {leaf.title} capability where {name}, {n2} and {n3} are first-class requirements."
        a = (
            "**Requirements and assumptions.** Clarify tenants, workload distribution and 10× case, latency/quality SLO, data class and residency, RPO/RTO, deployment locations, team skills and budget. Turn each ambiguous requirement into a measurable acceptance or rejection criterion. "
            f"**Mechanisms.** {name}: {explanation} {n2}: {e2} {n3}: {e3} Place each on a control/data-plane and synchronous/asynchronous diagram, then identify its source of truth, owner and failure domain. "
            "**Security and reliability.** Use short-lived identity, least privilege, explicit tenant boundaries and recoverable encryption keys; design independent capacity and bounded failure propagation rather than assuming replica count equals availability. "
            "**Delivery and operations.** Bind reviewed source to immutable artifacts, qualify with representative tests, release progressively and retain a tested rollback or rebuild path. Instrument user SLO, queue/saturation, audit and cost per successful outcome. "
            f"**Trade-offs and example.** Compare managed, shared and dedicated {leaf.title} options across isolation, portability, operator load and cost. Pilot the highest-risk dependency, perform a restore/failover test, and define migration and exit triggers before committing the full platform."
        )
        sn.append((tag, q, a))
    add_section("Senior — architecture, trade-off and code-design questions", "S", "N", sn)

    sp = []
    for i, (name, explanation) in enumerate(concepts):
        cmd = commands[i % len(commands)]
        tag = "**Incident/migration:** "
        q = f"You own a high-severity failure or migration involving {name}. How do you lead it end to end?"
        a = (
            "**Lead the work.** Establish incident or change command, impact, decision rights, stakeholder cadence, success measures and abort criteria. Freeze conflicting changes, preserve a timeline and keep one accountable technical owner for each workstream. "
            f"**Build evidence.** Use `{cmd}` as one checkpoint because it {command_explanation(cmd)}. Correlate identity, desired revision, events, SLI, dependency state and capacity; never make a destructive move from a single green or red field. "
            f"**Mechanism and risk.** {explanation} Translate that behavior into explicit data, tenant, compatibility and partial-completion risks. "
            "**Execute safely.** Rehearse on representative state, protect backups and rollback artifacts, canary one failure domain or tenant, stop at thresholds, and prefer reversible containment. Recover in waves so error, latency, correctness, security and billing evidence can halt expansion. "
            f"**Close the loop.** Verify {leaf.title} from the user path, reconcile the durable source, publish the timeline and trade-off record or postmortem, assign preventive actions with owners and dates, and prove them in a restore test, game day or migration rehearsal."
        )
        sp.append((tag, q, a))
    add_section("Senior — procedural incident, migration and ownership questions", "S", "P", sp)

    out.extend([
        "## Self-grading",
        "",
        "A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.",
        "",
    ])
    return "\n".join(out)


def write(path: Path, content: str) -> None:
    path = numbered_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def generate_area(leaves: list[Leaf]) -> None:
    by_branch: dict[tuple[str, str], list[Leaf]] = {}
    for leaf in leaves:
        by_branch.setdefault((leaf.area, leaf.branch), []).append(leaf)

    for (area, branch), branch_leaves in by_branch.items():
        base = numbered_path(ROOT / area / branch)
        branch_leaf = Leaf(
            area, branch, branch, branch.replace("-", " ").title(),
            f"Integrate the {branch.replace('-', ' ')} branch as one production capability rather than isolated products.",
            tuple(item for leaf in branch_leaves for item in leaf.concepts[:2])[:10],
            tuple(cmd for leaf in branch_leaves for cmd in leaf.commands[:1])[:10],
            branch_leaves[0].docs,
        )
        branch_notes = notes(branch_leaf)
        branch_notes = branch_notes.split("\n", 1)[1].lstrip()
        write(base / "README.md", branch_overview(area, branch, branch_leaves) + "\n" + branch_notes)
        write(base / "questions-and-answers.md", qna(branch_leaf, branch=True))

        for leaf in branch_leaves:
            service = numbered_path(base / leaf.slug)
            write(service / "README.md", notes(leaf))
            write(service / "questions-and-answers.md", qna(leaf))

    by_area: dict[str, list[Leaf]] = {}
    for leaf in leaves:
        by_area.setdefault(leaf.area, []).append(leaf)
    for area, area_leaves in by_area.items():
        area_topic = Leaf(
            area, "", "", area.replace("-", " ").title(),
            "Integrate all child branches into one secure, reliable, observable and cost-controlled platform.",
            tuple(item for leaf in area_leaves for item in leaf.concepts[:1])[:10],
            tuple(cmd for leaf in area_leaves for cmd in leaf.commands[:1])[:10],
            area_leaves[0].docs,
        )
        write(ROOT / area / "questions-and-answers.md", qna(area_topic, branch=True))

    # Migration from the earlier three-file prototype: README.md is now the note.
    for area in by_area:
        for old_note in (ROOT / area).rglob("notes.md"):
            old_note.unlink()


def generate_mega_bank() -> None:
    groups = [
        Leaf("", "", "", "General DevOps foundations", "Integrate systems, Linux, networking, delivery, security and SRE fundamentals.", C(
            "Linux resource path — CPU, memory, disk, descriptors, processes, cgroups and kernel evidence explain application symptoms",
            "Network request path — DNS, route, firewall/NAT, transport, TLS, proxy/load balancer and application must all agree",
            "Distributed failure — timeout does not reveal whether a remote side effect occurred, so idempotency and reconciliation matter",
            "Git delivery — reviewed source must bind to immutable artifact, provenance, environment and rollback evidence",
            "Container isolation — namespaces, cgroups, capabilities, seccomp and mounts constrain ordinary host processes",
            "CI/CD security — untrusted code near runner credentials requires isolation, pinning and short-lived identity",
            "Observability — metrics, logs, traces and profiles answer distinct questions under cardinality/privacy/cost limits",
            "SLO/error budget — user outcome target and burn rate guide paging and risk decisions",
            "Incident response — command, containment, evidence, reversible mitigation, verification and prevention form the lifecycle",
            "Disaster recovery — protected backup plus timed application restore/failover proves RPO and RTO",
        ), ("uptime; vmstat 1; iostat -xz 1", "ip route; ss -lntp; dig NAME; curl -v URL", "git log --graph --oneline --all", "docker inspect CONTAINER"), "https://sre.google/books/"),
        Leaf("", "", "", "Cloud, Kubernetes and Infrastructure as Code", "Design and operate cloud/Kubernetes/IaC as one reconciled production system.", C(
            "Cloud account/project — ownership, quota, billing and policy boundary reduces blast radius",
            "Workload identity — short-lived federated runtime credentials replace static cloud keys",
            "Kubernetes reconciliation — API/controllers/scheduler/kubelet converge desired state through plugins/runtime",
            "Kubernetes networking — Service/EndpointSlice/CNI/DNS/policy/load balancer form the request path",
            "Kubernetes storage — PVC/StorageClass/CSI/topology/snapshot bind state to workloads",
            "Autoscaling — demand metric scales replicas and unschedulable requests scale infrastructure after cold delay",
            "Terraform state — sensitive mapping from addresses to remote identities makes safe plan/refactor possible",
            "Pulumi Outputs — asynchronous dependency/secret values must stay inside engine-aware transformations",
            "GitOps — pull reconciliation audits and repairs drift but can amplify bad desired state",
            "Cloud economics — fixed capacity, work units, storage, network and telemetry combine into unit cost",
        ), ("kubectl get pods,nodes -A -o wide", "terraform plan -out=tfplan", "pulumi preview --diff", "aws sts get-caller-identity"), "https://kubernetes.io/docs/concepts/"),
        Leaf("", "", "", "Senior AI platform engineering", "Own GPU compute, serving, gateways, RAG, evaluation, governance and customer deployment outcomes.", C(
            "GPU compatibility chain — hardware, driver, runtime, device allocation, framework and model must be qualified together",
            "Inference queue — token work, KV memory, TTFT and goodput govern admission/batching/autoscaling",
            "Model release — weights, tokenizer, prompt, adapters, runtime, hardware, data/index and evaluator form one lineage",
            "LLM gateway — identity, policy, quota, routing, streaming, fallback, metering and audit normalize governed access",
            "RAG authorization — retrieval must enforce source and tenant access before context reaches a model",
            "Evaluation — versioned datasets and calibrated human/automated judges gate quality/safety regressions",
            "Agent tool security — model output proposes actions; deterministic policy, least privilege and approval authorize them",
            "AI governance — inventory, ownership, risk, data/model/prompt lineage, audit and retirement make controls operable",
            "AI FinOps — optimize cost per successful quality-controlled task rather than raw token or GPU hour",
            "Deployment portability — SaaS, customer cloud, on-prem and air gap require explicit packaging, identity, upgrades and support contracts",
        ), ("nvidia-smi topo -m", "kubectl get inferenceservice -A", "curl -s http://MODEL/metrics", "python -m evals.run --manifest release.yaml"), "https://genai.owasp.org/"),
    ]
    content = ["# Mega DevOps and AI Platform interview questions and answers", "", "> Mark a question complete by changing `- [ ]` to `- [x]`. This bank contains 180 answered questions; every topic folder has its own additional bank.", ""]
    for group in groups:
        content.append(qna(group, branch=True))
    write(ROOT / "questions-and-answers.md", "\n".join(content))


def main() -> None:
    generate_area(AWS)
    generate_area(K8S)
    generate_mega_bank()
    print(f"generated {len(AWS)} AWS and {len(K8S)} Kubernetes service leaves")


if __name__ == "__main__":
    main()
