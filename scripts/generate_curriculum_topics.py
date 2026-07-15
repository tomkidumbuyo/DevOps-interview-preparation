#!/usr/bin/env python3
"""Expand every non-AWS/Kubernetes curriculum branch into recursive study folders.

README.md is always the note. questions-and-answers.md is always the separate
checkbox practice bank. The user's preserved curriculum is the source of topic
names, so adding another numbered branch automatically creates another folder.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from generate_leaf_library import Leaf, numbered_path, qna, safe_id, write


ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "curriculum" / "master-curriculum.txt"


AREA_BY_MAJOR = {
    0: "00-role-ownership",
    1: "01-foundations",
    2: "02-linux",
    3: "03-networking",
    4: "04-git-delivery",
    5: "05-containers",
    **{n: "08-gcp" for n in range(21, 29)},
    **{n: "09-iac-delivery" for n in range(29, 32)},
    **{n: "10-operations" for n in range(32, 35)},
    **{n: "11-ai-platform" for n in range(35, 47)},
    **{n: "12-platform-engineering" for n in range(47, 61)},
    **{n: "13-scenarios" for n in range(61, 67)},
}


DOCS_BY_MAJOR = {
    0: "https://sre.google/workbook/on-call/",
    1: "https://sre.google/sre-book/handling-overload/",
    2: "https://docs.kernel.org/",
    3: "https://www.rfc-editor.org/",
    4: "https://git-scm.com/book/en/v2",
    5: "https://opencontainers.org/",
    21: "https://cloud.google.com/docs/overview",
    22: "https://cloud.google.com/vpc/docs/overview",
    23: "https://cloud.google.com/load-balancing/docs/load-balancing-overview",
    24: "https://cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview",
    25: "https://cloud.google.com/storage/docs/introduction",
    26: "https://cloud.google.com/pubsub/docs/overview",
    27: "https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform",
    28: "https://cloud.google.com/architecture/framework",
    29: "https://developer.hashicorp.com/terraform/docs",
    30: "https://www.pulumi.com/docs/",
    31: "https://docs.github.com/en/actions",
    32: "https://opentelemetry.io/docs/",
    33: "https://sre.google/books/",
    34: "https://slsa.dev/spec/v1.0/",
    35: "https://ml-ops.org/",
    36: "https://huggingface.co/learn/llm-course/",
    37: "https://docs.nvidia.com/datacenter/cloud-native/",
    38: "https://kserve.github.io/website/docs/",
    39: "https://opentelemetry.io/docs/specs/semconv/gen-ai/",
    40: "https://docs.llamaindex.ai/",
    41: "https://www.nist.gov/itl/ai-risk-management-framework",
    42: "https://ml-ops.org/",
    43: "https://modelcontextprotocol.io/docs/getting-started/intro",
    44: "https://genai.owasp.org/",
    45: "https://www.nist.gov/itl/ai-risk-management-framework",
    46: "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai",
    47: "https://www.finops.org/framework/",
    48: "https://cloud.google.com/architecture/framework",
    49: "https://sre.google/sre-book/service-best-practices/",
    50: "https://kubernetes.io/docs/concepts/security/multi-tenancy/",
    51: "https://kubernetes.io/docs/setup/production-environment/",
    52: "https://opentelemetry.io/docs/collector/deployment/",
    53: "https://slsa.dev/",
    54: "https://platformengineering.org/blog/what-is-platform-engineering",
    55: "https://openfeature.dev/docs/reference/intro/",
    56: "https://www.postgresql.org/docs/current/",
    57: "https://docs.python.org/3/",
    58: "https://go.dev/doc/",
    59: "https://www.gnu.org/software/bash/manual/bash.html",
    60: "https://www.postgresql.org/docs/current/tutorial-sql.html",
}


COMMANDS_BY_AREA = {
    "00-role-ownership": ("git log --since='30 days ago' --stat", "kubectl get events -A --sort-by=.lastTimestamp", "terraform plan", "git shortlog -sn"),
    "01-foundations": ("lscpu; free -h; lsblk; ip -br addr", "ss -s", "curl -v URL", "dig NAME"),
    "02-linux": ("uname -a; systemd-analyze", "ps -eo pid,ppid,state,pcpu,pmem,cmd", "vmstat 1; iostat -xz 1", "ip route; ss -lntup; journalctl -b"),
    "03-networking": ("ip -br addr; ip route; ip neigh", "dig +trace NAME", "curl -vk URL", "tcpdump -ni any 'host IP and port PORT'"),
    "04-git-delivery": ("git cat-file -p HEAD", "git log --graph --oneline --decorate --all", "git diff --check", "git verify-commit HEAD"),
    "05-containers": ("docker image inspect IMAGE", "docker inspect CONTAINER", "docker stats --no-stream", "docker events --since 30m"),
    "08-gcp": ("gcloud auth list", "gcloud config list", "gcloud projects describe PROJECT", "gcloud logging read 'severity>=ERROR' --limit=20"),
    "09-iac-delivery": ("terraform fmt -check -recursive", "terraform validate; terraform plan", "pulumi preview --diff", "git diff --check"),
    "10-operations": ("curl -s http://SERVICE/metrics", "promtool check rules rules.yml", "kubectl get events -A --sort-by=.lastTimestamp", "trivy fs ."),
    "11-ai-platform": ("nvidia-smi", "kubectl get pods -A -o wide", "curl -s http://MODEL/metrics", "python -m pytest -q"),
    "12-platform-engineering": ("python -m pytest -q", "go test ./...", "shellcheck scripts/*.sh", "git diff --check"),
    "13-scenarios": ("date -u; whoami; hostname", "kubectl get events -A --sort-by=.lastTimestamp", "terraform plan", "git log --since='2 hours ago' --oneline"),
}


COMMANDS_BY_TOPIC = {
    "linux architecture": ("uname -a; cat /etc/os-release", "systemd-analyze; systemd-analyze critical-chain", "journalctl -b -k; dmesg --level=err,warn", "ls -l /boot; cat /proc/cmdline"),
    "filesystems": ("findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS", "df -hT; df -i; du -xhd1 /var | sort -h", "stat PATH; namei -l PATH", "lsof +L1"),
    "users and permissions": ("id USER; getent passwd USER; getent group GROUP", "stat -c '%A %a %U:%G %n' PATH; getfacl PATH", "sudo -l -U USER; umask", "getcap -r /usr/bin 2>/dev/null"),
    "process management": ("ps -eo pid,ppid,user,state,ni,psr,pcpu,pmem,rss,etime,cmd --sort=-pcpu", "pstree -ap; pgrep -af NAME", "cat /proc/PID/status; cat /proc/PID/limits", "pidstat -wru -p PID 1"),
    "systemd": ("systemctl status UNIT; systemctl cat UNIT", "systemctl show UNIT -p ActiveState,SubState,Result,ExecMainStatus,Restart,NRestarts", "systemctl list-dependencies UNIT", "journalctl -u UNIT --since '-30 min' -o short-iso"),
    "memory": ("free -h; vmstat 1", "cat /proc/meminfo; cat /proc/pressure/memory", "ps -eo pid,comm,rss,vsz,pmem --sort=-rss | head", "cat /sys/fs/cgroup/memory.current; cat /sys/fs/cgroup/memory.events"),
    "cpu performance": ("uptime; mpstat -P ALL 1", "pidstat -u -w 1; vmstat 1", "cat /proc/pressure/cpu", "ps -eo pid,psr,ni,stat,pcpu,comm --sort=-pcpu | head"),
    "storage and i-o": ("lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS; findmnt", "iostat -xz 1; cat /proc/pressure/io", "pvs; vgs; lvs -a -o +devices", "lsof +L1; fuser -vm MOUNT"),
    "linux networking": ("ip -br addr; ip route; ip rule; ip neigh", "ss -lntup; ss -s; ss -tan state time-wait", "nft list ruleset; conntrack -S", "tcpdump -ni IFACE 'host IP and port PORT'"),
    "linux security": ("getenforce 2>/dev/null; sestatus 2>/dev/null; aa-status 2>/dev/null", "capsh --print; getcap -r /usr/bin 2>/dev/null", "sshd -T | sort; last -a | head", "ausearch -m AVC,USER_AUTH -ts recent 2>/dev/null"),
    "linux logs and troubleshooting": ("date -u; uptime; systemctl --failed", "journalctl -b -p warning -o short-iso", "dmesg --level=err,warn; coredumpctl list", "vmstat 1; iostat -xz 1; ss -s"),
    "essential linux commands": ("pwd; ls -la; stat PATH; find ROOT -xdev -type f -size +1G", "rg -n 'PATTERN' ROOT; awk '{count[$1]++} END {for (k in count) print count[k],k}' FILE", "ps -ef; ss -lntup; lsof -p PID", "tar -tzf ARCHIVE; rsync -aHAXn SOURCE/ DEST/"),
    "osi and tcp-ip models": ("ip -s link; ip route", "ss -tin dst IP", "tracepath HOST", "tcpdump -ni IFACE -vv 'host IP'"),
    "ip addressing": ("ip -br addr; ip route get IP", "python3 -c 'import ipaddress; print(ipaddress.ip_network(\"10.20.0.0/20\").subnets(new_prefix=24))'", "ipcalc 10.20.3.17/24", "arping -D -I IFACE IP"),
    "layer 2 networking": ("ip -d link; bridge link; bridge vlan show", "ip neigh show", "ethtool IFACE", "tcpdump -eni IFACE 'arp or icmp6'"),
    "routing": ("ip route show table all; ip rule", "ip route get DEST from SOURCE", "traceroute -n DEST; tracepath DEST", "tcpdump -ni IFACE 'host DEST'"),
    "tcp and udp": ("ss -lntup; ss -tin", "nc -vz HOST PORT; nc -vzu HOST PORT", "tcpdump -ni IFACE 'tcp port PORT or udp port PORT'", "sysctl net.ipv4.ip_local_port_range"),
    "dns": ("getent ahosts NAME", "dig NAME A; dig NAME AAAA; dig NAME CNAME", "dig +trace NAME", "dig @SERVER NAME TYPE +norecurse"),
    "http": ("curl -sv --connect-timeout 3 --max-time 10 URL -o /dev/null", "curl -sS -D- -o /dev/null URL", "curl --http2 -v URL", "openssl s_client -connect HOST:443 -servername HOST </dev/null"),
    "tls and certificates": ("openssl s_client -connect HOST:443 -servername HOST -showcerts </dev/null", "openssl x509 -in CERT -noout -subject -issuer -serial -dates -ext subjectAltName", "openssl verify -CAfile CA_BUNDLE CERT", "curl -v --cacert CA_BUNDLE https://HOST/"),
    "load balancing": ("curl -sS -D- URL -o /dev/null", "for i in 1 2 3 4 5; do curl -sS URL; done", "ss -s; ss -tin", "tcpdump -ni IFACE 'host VIP and port PORT'"),
    "proxies and gateways": ("curl -v -x http://PROXY:PORT https://DEST/", "curl -v -H 'Host: SERVICE.example' http://PROXY_IP/", "env | rg -i 'https?_proxy|no_proxy'", "openssl s_client -proxy PROXY:PORT -connect HOST:443 -servername HOST </dev/null"),
    "firewalls and nat": ("nft list ruleset", "iptables-save 2>/dev/null", "conntrack -L; conntrack -S", "tcpdump -ni any 'host IP and port PORT'"),
    "network troubleshooting": ("date -u; getent ahosts NAME; ip route get IP", "nc -vz HOST PORT; curl -vk URL", "ss -tin dst IP; conntrack -S", "tcpdump -ni any 'host IP and port PORT'"),
    "git object model": ("git rev-parse HEAD; git cat-file -t HEAD; git cat-file -p HEAD", "git ls-tree -r HEAD | head", "git show-ref; git reflog --date=iso", "git fsck --full"),
    "branching": ("git branch -vv; git log --graph --oneline --decorate --all", "git merge-base BRANCH_A BRANCH_B", "git diff BRANCH_A...BRANCH_B", "git worktree list"),
    "change integration": ("git merge --no-commit --no-ff BRANCH", "git rebase --rebase-merges BASE", "git cherry-pick --no-commit COMMIT", "git rerere status; git diff --check"),
    "collaboration": ("git remote -v; git fetch --prune --tags", "git log --format='%h %G? %an %s' -20", "git diff --stat BASE...HEAD; git diff --check BASE...HEAD", "git shortlog -sn BASE..HEAD"),
    "release management": ("git tag --list --sort=-creatordate | head", "git show TAG; git verify-tag TAG", "git log PREVIOUS_TAG..TAG --oneline", "git archive --format=tar TAG | sha256sum"),
    "git security": ("git log --show-signature -5", "git verify-commit HEAD; git verify-tag TAG", "git grep -n -I -E '(BEGIN .*PRIVATE KEY|password=|token=)'", "git config --show-origin --get-regexp 'credential|signing|safe.directory'"),
    "container internals": ("docker inspect CONTAINER", "docker top CONTAINER; docker stats --no-stream CONTAINER", "docker exec CONTAINER cat /proc/1/status", "nsenter -t PID -n ip addr"),
    "docker images": ("docker image inspect IMAGE", "docker history --no-trunc IMAGE", "docker buildx build --check .", "docker image ls --digests; docker scout cves IMAGE"),
    "docker runtime": ("docker run --rm --read-only --cap-drop=ALL IMAGE COMMAND", "docker inspect CONTAINER", "docker logs --timestamps CONTAINER", "docker events --since 30m"),
    "container networking": ("docker network ls; docker network inspect NETWORK", "docker exec CONTAINER ip route", "docker exec CONTAINER getent hosts NAME", "docker port CONTAINER; ss -lntup"),
    "container storage": ("docker volume ls; docker volume inspect VOLUME", "docker inspect CONTAINER --format '{{json .Mounts}}'", "docker system df -v", "findmnt; df -hT; df -i"),
    "registries": ("docker manifest inspect IMAGE:TAG", "docker pull IMAGE@sha256:DIGEST", "docker image inspect IMAGE --format '{{json .RepoDigests}}'", "cosign verify IMAGE@sha256:DIGEST"),
    "container security": ("docker inspect CONTAINER --format '{{json .HostConfig}}'", "docker run --rm --cap-drop=ALL --security-opt=no-new-privileges IMAGE id", "trivy image IMAGE", "docker scout cves IMAGE"),
}


LABS_BY_AREA = {
    "02-linux": """Use a disposable Linux VM or container. Record `date -u`, `uname -a`, distribution, effective user and cgroup before the topic commands. Capture a healthy baseline, run one command with an intentionally nonexistent PID/path/unit to learn its error and exit code, then return to the real object and explain the discriminating fields. Do not change mounts, firewall, users, kernel settings or services on a shared host. Cleanup: exit and delete the disposable environment.""",
    "03-networking": """Create a disposable network lab: `docker network create devops-net-lab`; start `docker run -d --name web-lab --network devops-net-lab nginx:1.27-alpine`; verify with `docker run --rm --network devops-net-lab curlimages/curl:8.10.1 -sv http://web-lab/`. Controlled failure: query a wrong name and a closed port, compare DNS versus TCP evidence, then inspect the Docker network. Cleanup: `docker rm -f web-lab` and `docker network rm devops-net-lab`. Pulling images uses network/bandwidth; pin a verified digest in a governed environment.""",
    "04-git-delivery": """Create an isolated repository under a directory from `mktemp -d`, set repository-local test identity, make three small commits on two branches, and inspect objects/graphs/diffs before merging or rebasing. Create one intentional content conflict, resolve it by preserving both intended behaviors, run `git diff --check`, and compare the history before/after. Cleanup: remove only the printed temporary directory after verifying it is the lab path.""",
    "05-containers": """Use a disposable local runtime. Run a small container with explicit CPU/memory/pid limits, read-only root, dropped capabilities and a temporary writable mount; inspect effective state, logs, processes, namespaces and limits. Trigger a safe failure with a nonexistent command or an over-tight test limit, explain the exit status/event, then recreate from source configuration. Cleanup the named lab container, network and volume; confirm with the runtime inventory.""",
    "09-iac-delivery": """Use a disposable state/backend and sandbox account. Format, validate and test first; preview/plan and save the reviewed output; apply one harmless tagged resource only after checking identity and estimated cost; introduce a configuration-only diff; inspect the plan; revert it in source; and verify no drift. Destroy only the exact sandbox stack after inspecting the destroy preview and retaining no required state.""",
    "11-ai-platform": """Use a tiny local model or approved sandbox endpoint and a versioned JSONL dataset. Record model/tokenizer/prompt/runtime/hardware and baseline latency, token and quality metrics; change one bounded variable; rerun; compare; then simulate an unavailable route or rejected request and verify safe fallback/denial. Cleanup artifacts, endpoint and cached test data according to their classification and retention policy.""",
}


# Short, factual definitions for concepts that recur heavily in interviews. Terms
# not present here still receive a mechanism/failure/operation learning contract.
DEFINITIONS = {
    "CPU": "executes instructions on logical processors; run-queue pressure, per-core saturation, steal time, affinity, quotas and throttling determine effective compute",
    "Memory": "maps virtual pages to RAM or swap; RSS, cache, faults, reclaim, PSI, NUMA locality and cgroup limits explain pressure better than one free-memory number",
    "Disk": "persists blocks through filesystem, page cache, block queue and device; IOPS, throughput, latency, queue depth, durability and failure are distinct",
    "Network": "moves packets through name resolution, routing, policy/NAT, transport, TLS and application layers; each hop has independent state and failure",
    "Processes": "are kernel-scheduled execution/resource containers with address space, credentials, descriptors, namespaces, cgroups, signals and lifecycle state",
    "Threads": "share a process address space and resources while retaining independent stacks and scheduling state, trading lower communication cost for synchronization risk",
    "File descriptors": "are per-process integer handles to open files, sockets, pipes and kernel objects; process and system limits can exhaust independently",
    "System calls": "cross the user/kernel boundary to request controlled operations such as open, read, write, mmap, clone and network I/O",
    "Race conditions": "make results depend on unsafe interleavings; remove them with ownership, immutability, atomic operations or correctly scoped synchronization",
    "Deadlocks": "occur when wait dependencies form a cycle; prevent with ordering, bounded acquisition, reduced lock scope and observable contention",
    "Async I/O": "lets work progress without dedicating one blocked thread per operation, but still requires cancellation, deadlines, backpressure and error propagation",
    "Partial failure": "means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred",
    "Retries": "repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms",
    "Idempotency": "makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records",
    "At-least-once delivery": "may redeliver and therefore requires idempotent consumers, deduplication and safe acknowledgement ordering",
    "Strong consistency": "makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions",
    "Eventual consistency": "allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts",
    "Quorums": "require overlapping read/write or voting majorities so operations intersect authoritative state, with latency and partition trade-offs",
    "CAP theorem": "states that during a network partition a distributed system cannot guarantee both linearizable consistency and availability for every request",
    "Circuit breakers": "stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics",
    "Backpressure": "propagates downstream capacity limits to producers through bounded queues, admission or rate reduction instead of unbounded buffering",
    "REST": "models resources over HTTP methods/status/cache semantics; good design makes identity, idempotency, pagination and versioning explicit",
    "gRPC": "uses protobuf contracts and HTTP/2 for typed unary or streaming RPCs, requiring deadline, status, load-balancing and compatibility discipline",
    "Microservices": "split deployable ownership and scaling boundaries but add network, consistency, discovery, observability and organizational coordination costs",
    "Kernel space versus user space": "separates privileged kernel resource control from isolated applications; system calls, faults and signals connect the domains",
    "Linux boot process": "progresses firmware → bootloader → kernel/initramfs → root filesystem → PID 1 → targets/units, so diagnose the earliest failing stage",
    "Inodes": "store filesystem object metadata and block references while directories map names to inode numbers; inode exhaustion is separate from byte exhaustion",
    "Hard links": "add another directory name for the same inode and normally cannot cross filesystems; data remains until the final link/open reference disappears",
    "Symbolic links": "store a path resolved at access time, can cross filesystems, and can dangle or create security-sensitive traversal",
    "chmod": "changes Unix mode bits for owner/group/other; actual access can also depend on ACL, capabilities, mount flags and mandatory access control",
    "SUID": "runs an executable with the file owner's effective identity and therefore creates a sensitive privilege boundary requiring minimal audited binaries",
    "POSIX ACLs": "add named user/group permissions beyond basic mode bits and interact with the ACL mask and inherited defaults",
    "Linux capabilities": "split many root powers into independently grantable process/file privileges, but several remain broad escalation paths",
    "Zombie processes": "have exited but retain a process-table entry until the parent waits; fix the parent/reaping lifecycle rather than killing the zombie",
    "Signals": "deliver asynchronous process notifications; SIGTERM enables cleanup while SIGKILL cannot be caught and risks unfinished work",
    "ulimit": "exposes shell/process resource limits such as open files and processes; systemd, PAM and cgroup limits may set other effective ceilings",
    "systemd units": "declaratively describe services, sockets, timers, mounts, targets and dependencies with lifecycle, identity, sandbox and resource controls",
    "Page cache": "uses reclaimable RAM for file data to reduce I/O; it is not automatically a leak, but writeback and dirty-page pressure affect latency",
    "Out-of-memory killer": "selects a victim when memory cannot be reclaimed; host and cgroup OOM scopes, scores and memory events reveal why",
    "NUMA": "groups CPUs and local memory; remote-memory access and poor placement can reduce throughput even when aggregate capacity looks free",
    "Load average": "counts runnable and uninterruptible tasks over time, so high load can mean CPU contention or blocked I/O rather than CPU percentage",
    "I/O wait": "is CPU accounting for idle time while tasks await I/O and must be correlated with device latency/queue and application blocking",
    "LVM": "maps flexible logical volumes onto physical extents through PVs and VGs, enabling controlled allocation, snapshots and online expansion workflows",
    "RAID": "combines devices for redundancy/performance according to level, but correlated failure, rebuild risk and deletion still require backups",
    "fsync": "asks the storage stack to make dirty data/metadata durable under its contract; application ordering and hardware honesty still matter",
    "Network namespaces": "isolate interfaces, routes, firewall rules and sockets; veth/bridge or routed links connect namespaces",
    "Connection tracking": "records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners",
    "Ephemeral ports": "identify client-side flow tuples; narrow ranges, long TIME_WAIT and NAT sharing can exhaust outbound concurrency",
    "SELinux": "enforces label-based mandatory access control independently of Unix modes; inspect denials and policy rather than disabling enforcement",
    "Seccomp": "filters allowed system calls to reduce kernel attack surface; profiles must match workload behavior and architecture",
    "OSI model": "is a diagnostic abstraction from physical/link through network/transport/session/presentation/application, not a literal implementation stack",
    "MTU": "bounds packet/frame payload per link; encapsulation and blocked path-MTU discovery can create large-packet black holes",
    "CIDR": "represents an address prefix and host space; subnet planning must include reservations, summarization, growth and overlapping-range constraints",
    "ARP": "resolves IPv4 next-hop addresses to link-layer addresses on a local segment; caches, spoofing and duplicate IPs affect reachability",
    "Longest-prefix match": "selects the most specific matching route before administrative/metric tie-breaks in the relevant routing table",
    "BGP": "exchanges reachability between autonomous routing domains using policy and path attributes; convergence and filtering are operational concerns",
    "TCP handshake": "uses SYN, SYN-ACK and ACK to establish sequence/state; failures localize listener, routing, firewall and return-path problems",
    "TIME_WAIT": "keeps the active closer's tuple state to absorb delayed segments; high counts are not inherently failure but can contribute to tuple exhaustion",
    "UDP": "provides connectionless datagrams without built-in ordering, retransmission or congestion semantics; the application must supply what it needs",
    "QUIC": "runs secure multiplexed streams over UDP with integrated TLS and connection migration, shifting observability and policy assumptions",
    "DNS recursion": "has a resolver pursue delegations on a client's behalf while authoritative servers publish zone data; caches obey record semantics and TTL",
    "DNSSEC": "authenticates DNS data with a signed chain of trust but does not encrypt queries and requires careful key/delegation rollover",
    "HTTP keep-alive": "reuses transport connections to reduce handshake cost while pool size, idle timeout and proxy alignment affect failure behavior",
    "HTTP/2": "multiplexes streams over one TCP connection with header compression, but connection loss and transport head-of-line effects remain",
    "TLS handshake": "negotiates version/cipher, authenticates certificates and derives session keys; hostname/SNI, trust chain and time must agree",
    "SNI": "carries the requested hostname in the TLS ClientHello so one address can select certificates/routes; legacy/privacy considerations remain",
    "Reverse proxies": "accept client traffic and forward to backends while applying routing, TLS, policy and observability; trust forwarded identity only from known hops",
    "SNAT": "rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity",
    "DNAT": "rewrites destination addressing for published services and must align with routing, policy and connection state",
    "Git blob": "stores file content by object ID without filename; trees provide names and modes",
    "Git tree": "maps filenames and modes to blobs/subtrees, representing one directory snapshot",
    "Git commit": "references a root tree, parent commit(s), author/committer metadata and message; branches are movable refs to commits",
    "HEAD": "symbolically identifies the checked-out branch or directly a commit in detached state",
    "Rebase": "replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination",
    "Merge": "combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution",
    "cherry-pick": "replays selected commit changes onto the current branch with new identity and possible conflict/duplication risk",
    "CODEOWNERS": "requests or enforces review ownership for matching paths when paired with hosting-branch protection; it is not runtime authorization",
    "Signed commits": "bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves",
    "Namespaces": "isolate process-visible kernel resources such as PID, mount, network, IPC, UTS and user IDs",
    "cgroups": "account, prioritize and limit process groups for CPU, memory, I/O and pids; pressure/throttling can occur below host capacity",
    "OCI image": "is an immutable manifest/config plus content-addressed filesystem layers and metadata, promoted by digest rather than rebuilt per environment",
    "OverlayFS": "presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance",
    "PID 1 behavior": "must reap orphaned children and forward/handle signals correctly so containers stop cleanly",
    "Container capabilities": "are inherited Linux privileges; drop all unnecessary capabilities and avoid privileged mode/host namespaces",
}


@dataclass
class Section:
    number: str
    title: str
    items: list[str] = field(default_factory=list)


@dataclass
class Major:
    number: int
    title: str
    priority: str
    items: list[str] = field(default_factory=list)
    sections: list[Section] = field(default_factory=list)


def slug(value: str) -> str:
    value = value.lower().replace("/", "-").replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def parse_curriculum() -> list[Major]:
    majors: list[Major] = []
    major: Major | None = None
    section: Section | None = None
    for raw in CURRICULUM.read_text(encoding="utf-8").splitlines()[1:]:
        line = raw.strip()
        if not line or line.startswith("Part "):
            continue
        main_match = re.match(r"^(\d+)\.\s+(.+?)(?:\s+—\s+(P\d))?$", line)
        sub_match = re.match(r"^(\d+\.\d+)\s+(.+)$", line)
        if main_match and not sub_match:
            major = Major(int(main_match.group(1)), main_match.group(2), main_match.group(3) or "")
            majors.append(major)
            section = None
        elif sub_match and major:
            section = Section(sub_match.group(1), sub_match.group(2))
            major.sections.append(section)
        elif major:
            (section.items if section else major.items).append(line)
    return majors


def explanation(term: str, section: str) -> str:
    exact = DEFINITIONS.get(term)
    if exact:
        return exact.rstrip(".") + "."
    lower = term.lower()
    if "versus" in lower:
        return f"is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference."
    if any(word in lower for word in ("troubleshooting", "failure", "incident", "debug")):
        return "requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair."
    if any(word in lower for word in ("security", "hardening", "authorization", "authentication", "policy")):
        return "defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery."
    if any(word in lower for word in ("scaling", "autoscaling", "capacity", "performance", "optimization")):
        return "must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions."
    if any(word in lower for word in ("backup", "recovery", "restore", "migration", "upgrade")):
        return "is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion."
    if any(word in lower for word in ("logs", "metrics", "tracing", "observability", "monitoring", "alert")):
        return "turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses."
    return f"is part of {section}; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off."


def concepts_for(items: list[str], title: str) -> tuple[str, ...]:
    selected = list(items)
    if not selected:
        selected = [title]
    while len(selected) < 10:
        selected.extend(selected)
    # Keep every curriculum item in the note. The Q&A generator uses the first
    # ten mechanisms to produce 60 ranked questions.
    return tuple(f"{item} — {explanation(item, title)}" for item in selected)


def render_note(
    title: str,
    purpose: str,
    concepts: tuple[str, ...],
    commands: tuple[str, ...],
    docs: str,
    master_link: str,
    area: str,
    children: list[tuple[str, str]] | None = None,
) -> str:
    rows = []
    for idx, concept in enumerate(concepts, 1):
        name, _, desc = concept.partition(" — ")
        rows.append(f"| {idx} | **{name}** | {desc} |")
    # Child order and navigation live only in the root reading tree. Keep the
    # argument for generator-call compatibility, but do not emit a local TOC.
    children_text = ""
    commands = COMMANDS_BY_TOPIC.get(title.lower(), commands)
    command_text = "\n".join(commands)
    lab = LABS_BY_AREA.get(
        area,
        "Use a disposable local or cloud sandbox. Confirm identity/context and cost boundary, capture a healthy baseline with the commands above, introduce one bounded configuration or invalid-input failure, compare evidence, revert from source control, verify the original outcome, and delete only the named lab resources.",
    )
    return f"""# {title}

> [Interview questions and answers](questions-and-answers.md) · [Master curriculum]({master_link}) · Official starting point: <{docs}>

## Easy mode: mental model

{purpose}

Learn this topic in layers: name the object or mechanism, trace its lifecycle/data path, configure it safely, observe a healthy and failed state, recover it, and then design it across failure domains and team boundaries.

```mermaid
flowchart LR
  R[requirement or symptom] --> M[{title} mechanism]
  M --> S[state and dependencies]
  S --> O[commands metrics logs traces audit]
  O --> D[decision mitigation or design]
  D --> V[user-facing verification]
```
{children_text}
## Complete curriculum checklist

| # | Topic | What you must understand and demonstrate |
|---:|---|---|
{chr(10).join(rows)}

## Beginner → mid-level → senior learning path

1. **Beginner:** define every term; identify the relevant file, object, protocol, API, or command; explain one normal use.
2. **Mid-level:** configure it from source control, inspect effective runtime state, diagnose two failure modes, automate a safe change, and explain one trade-off.
3. **Senior:** clarify ambiguous requirements, map trust and failure domains, quantify capacity/SLO/RPO/RTO/cost, compare alternatives, plan migration/rollback, and assign ownership.

## Command and configuration lab

Run read-only checks first in a sandbox. For each command, predict healthy output, one failing result, the next discriminating check, and the safe rollback for any later mutation.

```bash
{command_text}
```

## Hands-on practice: setup → failure → verification → cleanup

{lab}

Expected result: you can show the healthy evidence, reproduce a safe failure, explain why each command distinguishes one layer from another, restore the baseline, and prove cleanup. Hard extension: automate the lab from source control, add a test or alert for the injected failure, and write a five-step runbook another engineer can execute.

For code/configuration, be ready to review an intentionally unsafe diff and improve idempotency, secret handling, timeouts, validation, logging, tests, and rollback.

## Senior design checklist

State assumptions for tenants, traffic/work units, latency and availability targets, data classification/residency, recovery, team skills and budget. Draw control/data planes and synchronous/asynchronous dependencies. Cover identity, policy, encryption/key lifecycle, delivery provenance, observability, capacity, unit cost, operational ownership, migration and exit criteria. Name the evidence that would cause you to revise the design.

## Revision and practice

Complete the separate [checkbox interview bank](questions-and-answers.md). Do not memorize wording: speak in the order **definition → mechanism → evidence/configuration → failure/trade-off → production example**. For procedures use **stabilize → scope → inspect → hypothesize → test → mitigate → verify → prevent**.
"""


def topic_leaf(area: str, title: str, purpose: str, items: list[str], commands: tuple[str, ...], docs: str) -> Leaf:
    return Leaf(area, "", slug(title), title, purpose, concepts_for(items, title), commands, docs)


def replace_generated_index(path: Path, block: str) -> None:
    """Remove legacy local indexes; the root README owns the complete tree."""
    path = numbered_path(path)
    start = "<!-- generated-topic-index:start -->"
    end = "<!-- generated-topic-index:end -->"
    if not path.exists():
        return
    existing = path.read_text(encoding="utf-8")
    updated = re.sub(
        rf"\n?{re.escape(start)}.*?{re.escape(end)}\n?",
        "\n",
        existing,
        flags=re.S,
    ).rstrip() + "\n"
    if updated != existing:
        path.write_text(updated, encoding="utf-8")


def generate() -> tuple[int, int]:
    majors = [m for m in parse_curriculum() if m.number in AREA_BY_MAJOR]
    by_area: dict[str, list[Major]] = {}
    leaf_count = 0

    for major in majors:
        by_area.setdefault(AREA_BY_MAJOR[major.number], []).append(major)

    for area, area_majors in by_area.items():
        area_path = numbered_path(ROOT / area)
        commands = COMMANDS_BY_AREA[area]
        area_children: list[tuple[str, str]] = []
        area_concepts: list[str] = []

        for major in area_majors:
            docs = DOCS_BY_MAJOR.get(major.number, "https://sre.google/books/")
            # Areas 0–5 already correspond one-to-one with the numbered major.
            major_path = area_path if len(area_majors) == 1 else numbered_path(area_path / slug(major.title))
            major_rel = "." if major_path == area_path else major_path.name
            if major_path != area_path:
                area_children.append((major.title, major_rel))

            section_children: list[tuple[str, str]] = []
            all_major_items = list(major.items)
            for section in major.sections:
                section_slug = slug(section.title)
                section_path = numbered_path(major_path / section_slug)
                section_children.append((f"{section.number} {section.title}", section_path.name))
                all_major_items.extend(section.items)
                leaf = topic_leaf(
                    area,
                    section.title,
                    f"Master {section.title} from first principles through safe production operation and senior architecture decisions.",
                    section.items,
                    commands,
                    docs,
                )
                master_link = Path(*([".."] * len(section_path.relative_to(ROOT).parts))) / "curriculum" / "master-curriculum.txt"
                write(section_path / "README.md", render_note(leaf.title, leaf.purpose, leaf.concepts, leaf.commands, leaf.docs, master_link.as_posix(), area))
                write(section_path / "questions-and-answers.md", qna(leaf))
                leaf_count += 1

            branch_leaf = topic_leaf(
                area,
                major.title,
                f"Integrate every part of {major.title} into one secure, reliable, observable, supportable and cost-aware production capability.",
                all_major_items,
                commands,
                docs,
            )
            if major_path == area_path:
                # Preserve the hand-written area note and add only the recursive map.
                index = "## Deep topic folders\n\n" + "\n".join(
                    f"- [{name}]({path}/README.md) — [Q&A]({path}/questions-and-answers.md)" for name, path in section_children
                )
                replace_generated_index(area_path / "README.md", index)
            else:
                master_link = Path(*([".."] * len(major_path.relative_to(ROOT).parts))) / "curriculum" / "master-curriculum.txt"
                write(major_path / "README.md", render_note(branch_leaf.title, branch_leaf.purpose, branch_leaf.concepts, branch_leaf.commands, branch_leaf.docs, master_link.as_posix(), area, section_children))
            write(major_path / "questions-and-answers.md", qna(branch_leaf, branch=True))
            area_concepts.extend(all_major_items)

        area_leaf = topic_leaf(
            area,
            area.replace("-", " ").title(),
            f"Connect all {area.replace('-', ' ')} branches and own their combined production outcomes.",
            area_concepts,
            commands,
            DOCS_BY_MAJOR.get(area_majors[0].number, "https://sre.google/books/"),
        )
        if len(area_majors) > 1:
            area_index = "## Deep topic branches\n\n" + "\n".join(
                f"- [{name}]({path}/README.md) — [Q&A]({path}/questions-and-answers.md)" for name, path in area_children
            )
            replace_generated_index(area_path / "README.md", area_index)
            write(area_path / "questions-and-answers.md", qna(area_leaf, branch=True))
        leaf_count += len(area_majors)

    return len(by_area), leaf_count


if __name__ == "__main__":
    area_count, leaf_count = generate()
    print(f"generated {leaf_count} curriculum topic/branch banks across {area_count} areas")
