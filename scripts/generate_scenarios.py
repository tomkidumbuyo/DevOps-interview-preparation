#!/usr/bin/env python3
"""Generate the answered cross-domain senior procedural scenario bank."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "scenarios" / "120-cross-domain-scenarios.md"


CATEGORIES = [
    ("Linux and host incidents", "HOST", (
        "A production API host has load average 80 but CPU utilization is below 20%.",
        "A service is OOM-killed inside its container while the node still shows free memory.",
        "The root filesystem reports 100% full, but visible files account for only half the space.",
        "A host has free disk blocks but applications fail with `No space left on device`.",
        "A systemd service enters a rapid restart loop immediately after a configuration rollout.",
        "SSH login latency jumps to 40 seconds although established sessions are healthy.",
        "One NUMA-heavy inference process is slow only on a subset of otherwise identical hosts.",
        "New outbound connections fail intermittently while existing connections remain healthy.",
        "Disk latency spikes after a database change although average IOPS is below the advertised limit.",
        "A kernel upgrade leaves several GPU nodes unable to boot into the normal target.",
    ), "`date -u; uptime; systemctl --failed; vmstat 1; iostat -xz 1; journalctl -b -p warning`", "process/cgroup limits, PSI, open-deleted files, inodes, service lifecycle, kernel/device evidence"),
    ("Networking, DNS, TLS and load balancing", "NET", (
        "A hostname resolves correctly on your laptop but not inside one production subnet.",
        "TLS works by IP with verification disabled but fails by the public hostname.",
        "An ALB reports healthy targets while users receive intermittent 502 responses.",
        "Only large HTTP responses stall after a new VPN or overlay-network rollout.",
        "TCP connections complete in one direction but return traffic takes a different firewall path.",
        "A DNS migration causes sporadic traffic to continue reaching the old environment for hours.",
        "A reverse proxy retries streaming LLM requests and some users receive duplicated output.",
        "A NAT gateway is healthy, but one busy node cannot create more outbound connections.",
        "A NetworkPolicy rollout breaks DNS for selected namespaces while direct IP connections work.",
        "Certificate rotation succeeds on the load balancer but several clients reject the new chain.",
    ), "`getent ahosts NAME; ip route get IP; nc -vz HOST PORT; curl -vk URL; openssl s_client -connect HOST:443 -servername HOST </dev/null`", "resolver path, route/policy/NAT, MTU, TCP state, SNI/trust chain, proxy/LB versus target evidence"),
    ("Containers and software supply chain", "CTR", (
        "A container works locally but exits immediately in Kubernetes with no useful application log.",
        "An image tag was overwritten and two replicas run different bytes under the same release name.",
        "A build cache accidentally includes a cloud credential in an image layer.",
        "A non-root container cannot write to a mounted volume after security hardening.",
        "A container consumes all host PIDs even though its CPU and memory are within limits.",
        "A critical base-image CVE has no fixed package version and production release is tomorrow.",
        "A multi-stage Docker build produces an image three times larger than expected.",
        "A registry outage blocks deployment even though the image ran on the node yesterday.",
        "A privileged debugging container is left running on a GPU node after an incident.",
        "A signed image verifies, but the deployment still contains unreviewed vulnerable code.",
    ), "`docker image inspect IMAGE; docker history --no-trunc IMAGE; docker inspect CONTAINER; docker events --since 30m`", "digest/provenance, entrypoint/PID 1, UID/mounts, namespaces/cgroups/capabilities, cache/layers, registry and policy"),
    ("Kubernetes control plane and cluster lifecycle", "KCP", (
        "The Kubernetes API is intermittently slow while workloads continue serving traffic.",
        "etcd disk usage grows rapidly and API writes begin timing out.",
        "A validating admission webhook outage blocks emergency production changes.",
        "A controller repeatedly updates the same object and creates an API-server hot loop.",
        "A cluster upgrade reveals an API version removed from the new control plane.",
        "All new Pods remain Pending after a scheduler configuration change.",
        "A kubelet certificate expires on a subset of nodes.",
        "An operator upgrade corrupts status reconciliation but desired custom resources remain intact.",
        "A failed control-plane restore returns the API but not the expected workload state.",
        "A noisy tenant consumes API request capacity and delays critical controllers.",
    ), "`kubectl get --raw '/readyz?verbose'; kubectl get events -A --sort-by=.lastTimestamp; kubectl get --raw /metrics`", "API request path, admission, APF, watch/reconcile loops, etcd quorum/storage, version skew, backup/restore validation"),
    ("Kubernetes workloads, network and storage", "KWS", (
        "A Deployment is stuck with old and new ReplicaSets both consuming full capacity.",
        "Pods are Ready but receive no Service traffic after a label change.",
        "A StatefulSet cannot reschedule because its volume is attached in another zone.",
        "A readiness probe causes a cascading outage during downstream latency.",
        "A node drain hangs on a workload with a strict PodDisruptionBudget.",
        "A DaemonSet update removes the CNI agent from too many nodes simultaneously.",
        "A CronJob runs twice around a controller restart and duplicates a billing operation.",
        "A namespace default-deny policy blocks an undocumented external dependency.",
        "Pods restart with ephemeral-storage eviction while the persistent volume has space.",
        "CoreDNS latency rises only for names with many search-domain expansions.",
    ), "`kubectl get pod,deploy,rs,svc,endpointslice,pvc -A -o wide; kubectl describe pod POD -n NS; kubectl get events -n NS --sort-by=.lastTimestamp`", "desired/observed rollout, readiness/endpoints, placement/topology, PDB/eviction, CNI/DNS/policy, CSI attachment and idempotency"),
    ("AWS production operations", "AWS", (
        "Private-subnet instances lose S3 access after an egress-cost optimization.",
        "An EC2 Auto Scaling group adds instances, but the ALB never routes to them.",
        "An S3 cross-account application receives AccessDenied despite an apparent IAM allow.",
        "A DynamoDB table throttles one customer although aggregate capacity looks low.",
        "Lambda concurrency spikes and overloads an RDS database.",
        "An EKS node group cannot launch GPU instances despite available account quota.",
        "CloudTrail evidence is missing from one newly created AWS account.",
        "A KMS key-policy change makes encrypted snapshots unusable in the DR account.",
        "Route 53 failover sends traffic to a healthy endpoint whose database is stale.",
        "A NAT Gateway bill triples after an EKS topology change.",
    ), "`aws sts get-caller-identity; aws configure list; aws cloudtrail lookup-events --max-results 20; aws service-quotas list-service-quotas --service-code SERVICE`", "identity/SCP/resource/key/endpoint policy, Region/account, route and endpoint, target health, partition-key/concurrency, capacity and cost path"),
    ("GCP and multi-cloud operations", "GCP", (
        "A GKE workload can call Google APIs in one project but receives 403 in another.",
        "Shared VPC routes exist, but a service project cannot reach a private managed endpoint.",
        "A global external load balancer serves an old backend after a regional failover.",
        "GPU Pods remain Pending even though the GCP console shows quota in the region.",
        "A Vertex AI endpoint rollout increases latency only for one model version.",
        "Cloud Run scales rapidly and exhausts a private database connection limit.",
        "Pub/Sub redeliveries cause duplicate writes after subscriber latency increases.",
        "A dual-cloud failover violates the promised data-residency boundary.",
        "Cloud Logging cost doubles after enabling detailed AI request telemetry.",
        "Workload Identity Federation stops working after an external issuer rotates keys.",
    ), "`gcloud auth list; gcloud config list; gcloud projects describe PROJECT; gcloud logging read 'severity>=ERROR' --limit=20`", "resource hierarchy/IAM, project/quota/zone, Shared VPC and private access, backend health, workload identity, model revision and cross-cloud contract"),
    ("Terraform, Pulumi, CI/CD and GitOps", "IAC", (
        "Terraform proposes replacing a production database after a module refactor.",
        "A state-lock holder disappeared, but the remote backend still reports the lock.",
        "A `for_each` key change plans destructive recreation of many stable resources.",
        "Pulumi preview shows unknown Outputs that a developer tried to convert to plain strings.",
        "A CI runner from an untrusted pull request can request cloud credentials.",
        "A GitOps controller continually reverts an approved emergency mitigation.",
        "A canary deployment passes infrastructure health but fails a business-quality metric.",
        "A database migration succeeds in staging but locks the production table.",
        "A provider upgrade changes defaults across hundreds of stacks.",
        "A secrets scanner finds a token in old Git history after it was deleted from HEAD.",
    ), "`git diff --check; terraform fmt -check -recursive; terraform validate; terraform plan -out=tfplan; pulumi preview --diff`", "identity/state/address mapping, plan evidence, refactor/import, secret Outputs, runner trust, reconciliation, compatibility, rollout and rollback"),
    ("Observability, SRE and disaster recovery", "SRE", (
        "The dashboard is green while customers report high tail latency.",
        "A high-cardinality label causes the Prometheus backend to run out of memory.",
        "Trace sampling drops nearly every request from a rare but severe error path.",
        "An alert fires every morning but never requires action.",
        "A service burns its monthly error budget in 45 minutes.",
        "A dependency outage triggers synchronized retries across the platform.",
        "A backup job is green, but the restored application fails integrity checks.",
        "A regional failover meets infrastructure RTO but clients cache old DNS.",
        "An OpenTelemetry Collector outage silently drops AI cost telemetry.",
        "A postmortem has many action items, but the same incident recurs three months later.",
    ), "`curl -s http://SERVICE/metrics; kubectl get events -A --sort-by=.lastTimestamp; promtool check rules rules.yml`", "user SLI and distributions, telemetry pipeline, cardinality/sampling, burn rate, retry/backpressure, application restore and verified ownership"),
    ("Security and incident response", "SEC", (
        "A long-lived cloud access key is exposed in a public repository.",
        "A Kubernetes ServiceAccount token appears in application logs.",
        "An attacker used an overly broad CI role to create a new administrator identity.",
        "A compromised container contacts an unfamiliar external IP.",
        "A secret rotation breaks half the replicas because connections are pooled.",
        "A customer asks for proof that one tenant cannot retrieve another tenant's data.",
        "A vulnerability scanner flags a critical library that is unreachable at runtime.",
        "A WAF rule blocks legitimate streaming prompts after a managed-rule update.",
        "Audit logs contain sensitive prompts that policy says must not be retained.",
        "A BYOD contractor laptop is lost while it still has active platform sessions.",
    ), "`date -u; whoami; git log --since='24 hours ago'; kubectl auth can-i --list; aws sts get-caller-identity`", "containment without evidence loss, revoke/rotate/session scope, identity and audit timeline, tenant boundary, exfiltration, recovery and control verification"),
    ("GPU infrastructure", "GPU", (
        "A GPU is visible on the host but Kubernetes advertises zero allocatable GPUs.",
        "CUDA reports a driver/runtime compatibility error after a node-image update.",
        "NCCL collectives hang only for multi-node training jobs.",
        "GPU utilization is near 100%, but inference token throughput falls sharply.",
        "MIG reconfiguration leaves scheduled Pods unable to start.",
        "Time-sliced GPU tenants interfere and violate latency SLOs.",
        "Karpenter cannot satisfy a pending GPU Pod despite broad instance-family selection.",
        "Spot interruption repeatedly loses a long training job's progress.",
        "Model downloads saturate network and delay every GPU node cold start.",
        "DCGM metrics disappear from one node pool while inference continues.",
    ), "`nvidia-smi; nvidia-smi topo -m; kubectl get nodes -o custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia\\.com/gpu; kubectl describe pod POD -n NS`", "hardware→driver→runtime→plugin/DRA→framework chain, topology, memory/ECC/Xid, scheduling resource names, capacity/caching and SLO"),
    ("Model serving and inference", "SERVE", (
        "A new model fits on disk but crashes with GPU OOM during warmup.",
        "Time to first token rises while inter-token latency remains stable.",
        "Continuous batching increases throughput but breaches one tenant's latency objective.",
        "A canary has healthy HTTP probes but produces lower-quality answers.",
        "A vLLM rollout fails because tokenizer and model revisions do not match.",
        "KServe scales to zero successfully but misses the first-request SLO.",
        "A multi-model server thrashes its model cache under a changed traffic mix.",
        "Quantization reduces memory but changes output quality for one language.",
        "A streaming client disconnect leaves expensive generation running.",
        "An inference autoscaler oscillates between too many and too few replicas.",
    ), "`kubectl get deployment,inferenceservice,pod -n inference -o wide; kubectl logs POD -n inference --since=30m; curl -s http://MODEL/metrics`", "weights/tokenizer/template/runtime/hardware lineage, queue/prefill/decode/KV memory, cancellation, batching, cold path, quality gate and scaling stability"),
    ("LLM gateway and provider operations", "GW", (
        "One tenant exhausts provider quota and degrades every other tenant.",
        "A provider returns 429, but gateway retries make the incident worse.",
        "A fallback model is available but cannot satisfy the required data residency.",
        "Streaming responses are billed twice after a mid-stream connection failure.",
        "A semantic cache returns an answer generated under another tenant's policy.",
        "A model alias changes underneath an application without a release record.",
        "Gateway token estimates consistently undercount requests with images or tools.",
        "A prompt policy blocks a critical customer workflow after a rules update.",
        "Provider latency is healthy but end-to-end gateway latency doubles.",
        "Gateway logs help debugging but expose prompts and credentials.",
    ), "`curl -N -v GATEWAY_URL/v1/chat/completions -H 'Authorization: Bearer TEST_TOKEN' -d @request.json; curl -s GATEWAY_URL/metrics`", "tenant identity/policy/quota, normalized semantics, retry/fallback after streaming, token/concurrency work, privacy-safe tracing, metering and release ownership"),
    ("RAG, evaluation, agents and AI governance", "AIG", (
        "A RAG system returns documents the requesting user cannot open at the source.",
        "Deleted source content continues appearing in answers from an old vector index.",
        "Retrieval recall improves while answer faithfulness gets worse.",
        "A model-as-judge approves its own model family much more often than humans do.",
        "An evaluation release gate is stable but does not predict production complaints.",
        "A retrieved document instructs an agent to exfiltrate secrets through a tool.",
        "An agent repeats a costly write tool after a timeout with unknown outcome.",
        "A prompt change reaches production without model, dataset or evaluator lineage.",
        "A customer requests all AI assets and data flows involving its records.",
        "A high-risk AI feature must be paused while preserving audit and appeal evidence.",
    ), "`python -m pytest -q; python -m evals.run --manifest release.yaml --dataset golden.jsonl; curl -s VECTOR_DB/health`", "source ACL before retrieval, ingestion/delete lineage, retrieval versus generation metrics, evaluator calibration, deterministic tool authorization/idempotency, inventory and governance workflow"),
    ("Platform ownership, deployment models and FinOps", "PLAT", (
        "You inherit an undocumented AI platform and the Head of Engineering needs immediate operational relief.",
        "A SaaS control plane must manage customer-cloud data planes without permanent administrator access.",
        "An on-prem customer cannot provide the GPU model assumed by the release.",
        "An air-gapped deployment requires upgrades and vulnerability evidence without registry access.",
        "A multi-cloud design promises portability but depends deeply on one provider's identity and queue semantics.",
        "GPU reservation cost is high while customers still see capacity-related errors.",
        "Teams bypass the platform golden path because onboarding takes two weeks.",
        "A cost-cutting request demands 30% savings without changing the production SLO.",
        "A platform migration has unclear decision rights across engineering, security and a customer team.",
        "You must explain an AI incident, trade-offs and recovery plan to executives and affected engineers.",
    ), "`git log --since='90 days ago' --stat; kubectl get events -A --sort-by=.lastTimestamp; terraform plan; cloud-cost-export-query`", "inventory/ownership, control/data trust, packaging/compatibility/upgrades/support, demand and unit economics, golden-path product metrics, ADR and communication"),
]


def answer(category: str, command: str, focus: str) -> str:
    return (
        f"**1. Stabilize and lead.** State the user/tenant impact, start time, SLO or safety risk, incident owner and communications cadence; pause risky changes and protect data. "
        f"**2. Scope safely.** Confirm identity, environment, Region/cluster/host and recent changes. Start read-only with {command}. Preserve timestamps, request/change IDs and exact errors. "
        f"**3. Trace the mechanism.** For this {category.lower()} case, test {focus}. Compare healthy and failing cohorts and use one discriminating hypothesis at a time. "
        "**4. Mitigate.** Stop amplification, shed or reroute only to an approved compatible path, and prefer a reversible configuration or rollback. Do not widen access, delete evidence, or assume a timeout means no side effect. "
        "**5. Verify.** Re-run the original user/workload path and verify SLO, correctness/quality, tenant/security boundary, data integrity and billing—not merely resource health. "
        "**6. Repair and prevent.** Fix desired state in Git/IaC, add a regression test and leading alert, document the runbook/decision, assign an owner/deadline and rehearse the corrected failure. In an interview, state which result would disprove your first hypothesis and when you would escalate or roll back."
    )


def main() -> None:
    out = [
        "# 150 cross-domain procedural scenarios with answers",
        "",
        "> This is the requested post-topic mega scenario bank. Mark rehearsal progress by changing `- [ ]` to `- [x]`. Give your answer before revealing the model answer.",
        "",
        "Use **stabilize → scope → inspect → hypothesize → test → mitigate → verify → prevent**. Senior answers must also cover incident/change leadership, communication, security and tenant boundaries, SLO/RPO/RTO, cost, source-of-truth repair and ownership.",
        "",
    ]
    total = 0
    for category, prefix, prompts, command, focus in CATEGORIES:
        out.extend([f"## {category}", ""])
        for index, prompt in enumerate(prompts, 1):
            total += 1
            out.extend([
                f"### {prefix}-{index:02d}",
                "",
                f"- [ ] **Question:** {prompt} Walk through immediate safety, evidence, hypotheses, commands/queries, reversible mitigation, user-facing verification, durable repair and prevention.",
                "",
                f"**Answer:** {answer(category, command, focus)}",
                "",
            ])
    assert total == 150
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"generated {total} answered cross-domain scenarios")


if __name__ == "__main__":
    main()
