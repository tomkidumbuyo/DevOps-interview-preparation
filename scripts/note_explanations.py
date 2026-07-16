#!/usr/bin/env python3
"""Shared explanation-first building blocks for generated handbook notes.

The curriculum catalogs deliberately remain terse.  This module turns their
facts into a beginner-readable lesson before any lab or revision checklist.
Generators use it so a regeneration cannot bring back checklist-only notes.
"""

from __future__ import annotations

import re


AREA_HISTORY = {
    "00-role-ownership": (
        "Operations work began as a specialist system-administration function, then broadened through Agile, DevOps, SRE and platform engineering. "
        "The important change was not a job-title change: teams moved from owning isolated tickets to owning measurable service outcomes, safe delivery and the developer experience over the full lifecycle."
    ),
    "01-foundations": (
        "Modern computing grew from single machines and batch programs into time-sharing, networked services and globally distributed systems. "
        "Each step improved sharing and scale but introduced concurrency, partial failure and consistency problems, which is why the foundational mechanisms in this chapter still appear inside cloud and AI platforms."
    ),
    "02-linux": (
        "Linux inherits the Unix process, file and permission model developed from the late 1960s. Linus Torvalds released the Linux kernel in 1991; networking, loadable modules, namespaces, cgroups, modern filesystems and service managers later turned it into the common substrate for servers, containers and Kubernetes nodes."
    ),
    "03-networking": (
        "Packet networking developed from early research networks into the TCP/IP Internet; ARPANET adopted TCP/IP in 1983, DNS replaced a centrally maintained host list, and HTTP/TLS later made the network an application platform. "
        "Modern overlays, proxies and cloud load balancers add layers, but every request still depends on naming, forwarding, transport and application contracts agreeing."
    ),
    "04-git-delivery": (
        "Version control evolved from local file histories to centralized systems and then distributed commit graphs. Git was created in 2005 for Linux kernel development; content-addressed objects and cheap branches made distributed collaboration fast, while hosted review, signing and CI/CD added governance around the graph."
    ),
    "05-containers": (
        "Container isolation did not begin with Docker. Unix `chroot`, FreeBSD jails, Linux namespaces and cgroups gradually supplied filesystem, identity and resource boundaries; Docker made image-based workflows popular in 2013, and the OCI later standardized image and runtime contracts."
    ),
    "06-kubernetes": (
        "Kubernetes grew from lessons learned running large fleets at Google and was released as open source in 2014. It joined the CNCF as its first project and evolved from basic container scheduling into an extensible API and reconciliation platform with standardized networking, storage, policy and custom-resource interfaces."
    ),
    "07-aws": (
        "AWS helped turn infrastructure into an on-demand API with services such as S3 and EC2 in 2006. The platform expanded from individual virtual resources into regional managed control planes, global identity and governance, event-driven services and specialized data and AI systems; automation therefore became as important as resource creation."
    ),
    "08-gcp": (
        "Google Cloud grew from Google's internal distributed-systems experience and early managed products such as App Engine. It developed into a project- and organization-scoped platform spanning global networks, data systems, Kubernetes, serverless and AI, with APIs and IAM acting as the common control surface."
    ),
    "09-iac-delivery": (
        "Infrastructure automation evolved from shell scripts and host configuration tools into declarative resource graphs, remote state and reviewed delivery pipelines. Terraform popularized provider-based declarative provisioning from 2014, while later tools and GitOps connected infrastructure changes to normal software review, testing and promotion practices."
    ),
    "10-operations": (
        "Production operations moved from checking individual hosts to measuring distributed user journeys. SRE formalized service levels, error budgets and engineering approaches to toil; observability, incident command, post-incident learning and policy-as-code extended that model across cloud platforms."
    ),
    "11-ai-platform": (
        "Machine-learning systems evolved from offline statistical jobs into GPU-intensive training and always-on inference platforms. Foundation models added token-based capacity, very large artifacts, probabilistic quality and new safety concerns, so model, data, prompt, runtime and evaluation revisions now have to travel as one governed release."
    ),
    "12-platform-engineering": (
        "Platform engineering grew from the DevOps goal of shared ownership and the need to reduce repeated infrastructure work across many teams. Internal platforms package secure defaults and operational knowledge into self-service products, while keeping application teams responsible for the behavior of what they deploy."
    ),
    "13-scenarios": (
        "Case-based technical learning mirrors incident drills, game days and design reviews used by production teams. A scenario is valuable because it forces several mechanisms to interact under incomplete evidence, which is closer to real operations than recalling an isolated definition."
    ),
}


AREA_INTRO = {
    "00-role-ownership": "The subject is an ownership system: people turn ambiguous needs into decisions, changes, operated services and evidence that the outcome remains healthy.",
    "01-foundations": "The subject is a system of state and work: inputs arrive, compute and storage transform state, concurrent actors coordinate, and callers observe an outcome even when components fail independently.",
    "02-linux": "The subject lives across user space and the Linux kernel. A process asks the kernel for CPU, memory, files, devices or network access through system calls; the kernel enforces identity, isolation, accounting and lifecycle rules.",
    "03-networking": "The subject is part of an end-to-end packet path. An application names a peer, the host selects a route and next hop, transports establish communication, and application protocols interpret the bytes returned.",
    "04-git-delivery": "The subject is part of a content-addressed change graph. Files become immutable objects, commits connect snapshots to parents, refs name graph tips, and review and automation decide which graph state may become a release.",
    "05-containers": "The subject combines an immutable image with an ordinary host process constrained by namespaces, cgroups, capabilities, seccomp, mounts and network setup. A container is isolation and packaging, not a separate kernel or a complete security boundary.",
    "06-kubernetes": "The subject is governed through an API-driven feedback system. A client writes desired state, controllers compare it with observed state, the scheduler chooses placement, and node agents and plugins produce the running data plane.",
    "07-aws": "The subject has an API control plane and a workload data plane. An authenticated request is authorized, validated and persisted; managed controllers then create or reconfigure regional or global resources that serve traffic or process data.",
    "08-gcp": "The subject is an API-managed resource under organization, folder and project boundaries. Identity and policy authorize a control-plane change, while regional or global managed infrastructure produces the data-path behavior.",
    "09-iac-delivery": "The subject turns version-controlled intent into a reviewed state transition. A tool parses configuration, resolves dependencies, compares desired and recorded/remote state, proposes a change set and calls provider APIs after approval.",
    "10-operations": "The subject closes the loop between a user outcome and engineering action. Telemetry describes behavior, objectives define acceptable behavior, alerts identify urgent risk, and responders mitigate and repair the source of truth.",
    "11-ai-platform": "The subject links data, model and runtime state. A versioned input becomes an artifact, a serving system turns requests into token or prediction work, and evaluation decides whether quality, safety, latency and cost are acceptable.",
    "12-platform-engineering": "The subject is a product and control plane for engineering teams. Users request a capability through a supported interface, automation provisions it with guardrails, and the platform reports ownership, health, cost and lifecycle state.",
    "13-scenarios": "The subject is an evidence-driven decision path. Start with a user-visible symptom, separate the system into layers, test the cheapest discriminating hypothesis and keep mitigation distinct from the durable repair.",
}


AREA_FLOW = {
    "00-role-ownership": ("requirement or incident", "decision and accountable owner", "delivery and operation", "measured outcome"),
    "01-foundations": ("input and state", "compute and coordination", "dependency or storage", "observable result"),
    "02-linux": ("process or user request", "system call and kernel subsystem", "resource or device", "process-visible result"),
    "03-networking": ("application request", "name route and policy", "transport and remote service", "application response"),
    "04-git-delivery": ("working change", "object graph and review", "artifact and deployment", "verified release"),
    "05-containers": ("image and runtime request", "namespaces cgroups and policy", "host kernel and network/storage", "containerized process"),
    "06-kubernetes": ("desired API object", "admission and reconciliation", "node plugins and runtime", "running workload outcome"),
    "07-aws": ("signed API request", "IAM and service control plane", "regional or global data plane", "customer outcome"),
    "08-gcp": ("authenticated API request", "IAM and managed control plane", "service data plane", "consumer outcome"),
    "09-iac-delivery": ("versioned configuration", "graph state and preview", "provider API and rollout", "verified desired state"),
    "10-operations": ("user journey", "telemetry and objective", "response and source repair", "verified recovery"),
    "11-ai-platform": ("data prompt or request", "model and platform control", "training or inference runtime", "quality-controlled result"),
    "12-platform-engineering": ("developer intent", "platform API and guardrails", "provisioned capability", "supported product outcome"),
    "13-scenarios": ("symptom", "evidence and hypothesis", "reversible mitigation and repair", "user verification"),
}


AREA_FALLBACK = {
    "00-role-ownership": "a responsibility and decision mechanism that connects an accountable person, an explicit outcome, evidence, escalation and follow-through",
    "01-foundations": "a computing mechanism that changes how work, state or communication is represented and coordinated",
    "02-linux": "a kernel or user-space mechanism that changes how a process obtains, shares, limits or observes an operating-system resource",
    "03-networking": "a protocol or forwarding mechanism that changes how endpoints identify peers, move packets or interpret a response",
    "04-git-delivery": "a source-control or delivery mechanism that changes how revisions are represented, reviewed, integrated or promoted",
    "05-containers": "an image, runtime or kernel-isolation mechanism that changes the filesystem, resource or security view of a process",
    "06-kubernetes": "an API or reconciliation mechanism that changes desired state, placement or workload data-plane behavior",
    "07-aws": "an AWS control- or data-plane mechanism exposed through a versioned API and bounded by account, Region, identity and quota",
    "08-gcp": "a Google Cloud control- or data-plane mechanism bounded by resource hierarchy, location, identity, quota and service contract",
    "09-iac-delivery": "a configuration, state or promotion mechanism that moves a reviewed revision toward effective runtime state",
    "10-operations": "an operational feedback mechanism that connects service behavior to detection, decision, recovery and prevention",
    "11-ai-platform": "an AI lifecycle mechanism that affects the identity, quality, safety, performance or cost of a data, model or runtime revision",
    "12-platform-engineering": "a platform-product mechanism that turns a user intent into a governed, supported and observable capability",
    "13-scenarios": "a diagnostic mechanism that distinguishes competing causes and supports a reversible operational decision",
}


FALLBACK_DEFINITION_RULES = [
    (r"versus|\bvs\b", "is a comparison boundary: the two sides solve related problems with different ownership, timing, guarantees and failure behavior, so the workload contract determines which side is appropriate"),
    (r"architect|topology|design$", "describes how components, state and dependencies are arranged and where control, data, trust and failure boundaries sit"),
    (r"lifecycle|workflow", "describes the ordered states from creation or submission through active use, change, failure, recovery and retirement, including who owns each transition"),
    (r"pipeline", "is an ordered or dependency-aware chain of stages that transforms versioned inputs into outputs and records status so failed work can be retried, resumed or rolled back safely"),
    (r"endpoint|api$|protocol", "is a network-facing contract that defines request and response shape, authentication, errors, timeouts, compatibility and the point where callers meet the service data path"),
    (r"gateway|proxy", "is an intermediary boundary that accepts a caller connection and applies routing, policy, transformation or observability before forwarding to a selected backend"),
    (r"controller|operator|reconciliation", "is a feedback-loop component that watches desired and observed state, computes a difference and performs idempotent actions until the managed resource converges or reports why it cannot"),
    (r"webhook|admission", "is a synchronous callback or policy checkpoint invoked during an API transition; its scope, timeout and failure policy determine whether an unavailable dependency blocks or bypasses the request"),
    (r"registry|catalog|inventory", "is an authoritative or indexed catalog of assets and metadata used to discover identity, owner, revision, lifecycle state and relationships without scanning every runtime separately"),
    (r"queue|messag|event|stream|topic|subscription", "is an asynchronous hand-off mechanism that decouples producers from consumers and therefore must define ordering, retention, delivery, acknowledgement, retry and backlog behavior"),
    (r"cache|caching", "keeps reusable results closer to the caller to reduce repeated work or latency, while introducing freshness, eviction, capacity and invalidation behavior that becomes part of correctness"),
    (r"storage|volume|filesystem|database|data store", "holds state beyond one operation or process lifetime and therefore must define durability, consistency, concurrency, replication, backup, restore and deletion semantics"),
    (r"model|prompt|embedding|retriev|rag|feature|dataset", "is an AI data or behavior artifact whose exact revision, inputs, transformations, compatibility and evaluation evidence affect the result produced at runtime"),
    (r"metric|log|trace|profile|telemetry|signal", "is an observability signal that records a defined aspect of runtime behavior; its schema, context, sampling, retention and query semantics determine which hypotheses it can distinguish"),
    (r"auth|identity|role|permission|policy|security|hardening|secret|key|certificate", "is a trust-control mechanism that identifies an actor or protected asset and enforces which action is allowed under explicit context, with audit, rotation, revocation and recovery behavior"),
    (r"deploy|release|rollout|promotion|version|artifact|build", "is a delivery mechanism that binds reviewed source to an immutable revision and moves that revision through validation and bounded rollout toward verified runtime state"),
    (r"backup|restore|recovery|disaster|migration|upgrade", "is a controlled state transition that protects compatibility and data, defines abort or rollback criteria and proves completion through integrity and user-facing RPO/RTO evidence"),
    (r"scal|capacity|performance|latency|throughput|optimization", "connects workload demand and work size to queueing, resource saturation, provisioning delay, headroom and unit cost so capacity changes follow measured bottlenecks"),
    (r"cost|billing|budget|finops", "connects attributed resource consumption to a useful workload outcome and applies forecast, quota, anomaly, commitment and optimization decisions without ignoring reliability or quality"),
    (r"govern|compliance|risk|approval|ownership", "turns organizational requirements into named owners, enforceable controls, evidence, exceptions with expiry and lifecycle decisions that can be audited and repeated"),
    (r"test|validation|evaluation|benchmark", "is a repeatable comparison between defined input, expected or baseline behavior and an acceptance threshold, with recorded environment and artifact revisions so the result can support a release decision"),
]


KIND_PATTERNS = [
    ("identity and policy", r"identity|iam|auth|permission|rbac|principal|role|policy|credential|secret|certificate|encryption|key|trust|tenant|security|admission|audit"),
    ("network request path", r"network|route|routing|packet|dns|tcp|udp|http|tls|proxy|gateway|load balan|firewall|nat|cidr|subnet|vpc|endpoint|service mesh|ingress|egress|socket|port"),
    ("memory management", r"virtual memory|resident memory|shared memory|page cache|buffers|swap|memory pressure|out.of.memory|memory leak|huge pages|numa"),
    ("telemetry", r"observ|monitor|metric|log|trace|alert|sli|slo|error budget|dashboard|profile|event"),
    ("failure control", r"failure|retry|timeout|circuit|bulkhead|backpressure|resilien|availability|recovery|disaster|drift|incident|degrad|failover|health|probe|disruption"),
    ("data and model lifecycle", r"model|prompt|rag|retriev|vector|embedding|dataset|feature|evaluation|llm|token|fine.?tun|agent|tool call|guardrail|drift"),
    ("queued work", r"queue|message|event|stream|pub.?sub|kafka|batch|job|cron|worker|consumer|producer"),
    ("compute and scheduling", r"cpu|gpu|compute|scheduler|scheduling|placement|autoscal|capacity|quota|thread|process|container|pod|node|runtime|inference|training|parallel"),
    ("delivery and lifecycle", r"git|build|image|deploy|release|rollout|upgrade|migration|version|pipeline|workflow|terraform|pulumi|helm|kustomize|gitops|provenance|sign|provider|resource|variable|output|expression|function|dependency graph"),
    ("durable state", r"storage|disk|volume|filesystem|database|state|snapshot|backup|restore|replica|consisten|etcd|cache|index|registry|artifact"),
    ("economics and governance", r"cost|billing|budget|finops|govern|organization|ownership|compliance|risk|roadmap|decision|support|on.?call"),
]


AREA_DEFAULT_KIND = {
    "00-role-ownership": "economics and governance",
    "01-foundations": "state transition",
    "02-linux": "compute and scheduling",
    "03-networking": "network request path",
    "04-git-delivery": "delivery and lifecycle",
    "05-containers": "compute and scheduling",
    "06-kubernetes": "state transition",
    "07-aws": "state transition",
    "08-gcp": "state transition",
    "09-iac-delivery": "delivery and lifecycle",
    "10-operations": "failure control",
    "11-ai-platform": "data and model lifecycle",
    "12-platform-engineering": "economics and governance",
    "13-scenarios": "failure control",
}


KIND_EXPLANATIONS = {
    "identity and policy": (
        "Think of this as a badge plus a checkpoint: identity says who or what is acting, while policy decides whether that actor may perform this exact action on this exact target under the current conditions.",
        "At runtime a caller presents or derives an identity, the enforcement point gathers identity, resource and request context, and applicable rules produce allow or deny. The effective decision is the intersection of all guardrails; encryption protects bytes but does not replace authorization, and audit records explain which decision was made.",
        "Healthy evidence includes a short-lived attributable identity, narrowly scoped access and an audit event for the intended resource. Failures commonly come from expired credentials, mismatched trust, an overriding deny, wrong resource scope or key/certificate lifecycle problems; widening access may hide the cause while creating a breach path.",
    ),
    "network request path": (
        "A useful analogy is a parcel journey: the name identifies the destination, routing selects each next hop, policy decides whether the parcel may pass, transport tracks delivery, and the application decides what the contents mean.",
        "A real request crosses several independent states: name resolution returns an address, the source selects a route and source address, link or overlay forwarding reaches the next hop, stateful or stateless policy evaluates the flow, transport establishes communication, and TLS/application protocols negotiate their own contract. The return path must also work.",
        "Healthy evidence progresses layer by layer: correct name/address, expected route, permitted flow, listening endpoint, successful handshake and valid application response. Timeouts, refusals, resets and protocol errors mean different layers; packet loss, MTU, asymmetric paths, connection-state exhaustion and proxy timeout mismatch are common production failures.",
    ),
    "memory management": (
        "Imagine every process receiving a private map of a much larger address space. The kernel translates that map to physical RAM, shared pages, file-backed cache or swap and can reclaim or deny memory when the machine or cgroup is under pressure.",
        "A process reserves virtual address ranges and faults pages in when it first touches them. Page tables translate virtual pages to physical frames; anonymous pages hold heap and stack data, file-backed pages participate in the page cache, and shared mappings can point several processes at the same frames. Reclaim drops clean cache first, writes dirty pages when necessary and may swap eligible anonymous pages before an OOM policy selects a victim.",
        "Healthy evidence separates virtual size, resident set, shared/file-backed cache, page-fault rate, reclaim, swap activity, PSI stall time and cgroup events. A low `free` number is not automatically failure because cache is reclaimable; sustained major faults, swap-in/out, direct reclaim, growing RSS with stable workload, OOM events or remote NUMA access explain real latency and termination risk.",
    ),
    "durable state": (
        "Think of this as a library catalog plus shelves: metadata says what should exist and where, while physical or remote storage holds the bytes. A successful write is not necessarily durable, replicated, backed up or restorable under the same contract.",
        "A write normally passes validation and authorization, enters a buffer or transaction, reaches a durable medium, and may then replicate or become visible to readers. Caches and indexes accelerate access but introduce freshness and eviction behavior; snapshots preserve a point-in-time representation but application consistency depends on write ordering.",
        "Healthy evidence combines capacity, latency, error, replication and integrity signals with a tested read or restore. Typical failures include exhausted bytes or inodes, throttling, stale replicas, corrupt metadata, topology mismatch, lost encryption keys and backups that exist but cannot reconstruct the application within RPO/RTO.",
    ),
    "queued work": (
        "A queue is like a numbered waiting line: producers can hand off work without waiting for completion, but someone must define ordering, capacity, acknowledgement and what happens when a worker disappears.",
        "A producer serializes and publishes a message, the service stores or routes it, a consumer receives it under a delivery contract, and acknowledgement advances or removes the item. At-least-once systems can redeliver after an unknown outcome, so stable operation identifiers and idempotent state changes are part of correctness.",
        "Healthy evidence includes publish and consume rates, queue depth and age, processing latency, retry/dead-letter counts and end-to-end business completion. Poison messages, hot partitions, backlog growth, duplicate effects and retry storms are common; adding consumers helps only when the downstream dependency and partition model can absorb them.",
    ),
    "compute and scheduling": (
        "Think of a scheduler as allocating seats and time slots: a request states what it needs, available workers advertise capacity, and policy chooses a placement. Requested capacity, usable capacity and completed useful work are different quantities.",
        "Work enters a runnable or pending state, eligibility filters remove incompatible placements, scoring or queue policy selects a worker, and a runtime creates the process and accounts for CPU, memory, devices and time. Autoscaling observes demand, requests more replicas or machines, and waits through provisioning and warm-up before capacity becomes useful.",
        "Healthy evidence connects queue delay, placement, utilization, throttling, memory/device pressure, runtime readiness and successful work. Fragmentation, inaccurate requests, quota, topology, cold starts and a saturated downstream service can leave capacity apparently free while latency and pending work grow.",
    ),
    "delivery and lifecycle": (
        "Treat delivery like a controlled assembly line: reviewed source becomes an immutable artifact, the artifact is promoted without being rebuilt, and each environment records exactly which revision is effective.",
        "The lifecycle begins with versioned intent, validates syntax and policy, resolves dependencies, builds or selects immutable inputs, produces a diff or release plan, changes the target in bounded waves, and records status. Reconciliation keeps desired and observed state aligned; rollback is another tested state transition, not merely a command name.",
        "Healthy evidence links source revision, review, test, artifact digest, signer/provenance, deployment target and user-facing verification. Mutable tags, environment-specific rebuilds, unpinned dependencies, non-idempotent migrations and controllers fighting emergency changes are recurring failure modes.",
    ),
    "telemetry": (
        "Telemetry is the instrument panel, not the system itself. Metrics summarize trends, logs preserve discrete context, traces connect work across boundaries, profiles attribute resource use, and audit events record security-relevant actions.",
        "Instrumentation observes a defined event or state, attaches bounded context, transports the signal, stores it under retention rules and makes it queryable. A useful signal has documented semantics and can distinguish at least two competing explanations; correlation identifiers belong in logs or traces rather than unbounded metric labels.",
        "Healthy evidence includes coverage of the user journey, known collection delay and actionable SLO or saturation views. Missing telemetry, sampling bias, cardinality explosions, sensitive payload capture and alert thresholds disconnected from user impact are failures of the observability system itself.",
    ),
    "failure control": (
        "Failure controls are traffic rules for unhealthy conditions: they bound how long work waits, how often it retries, how much enters the system and what reduced service remains possible.",
        "A caller assigns a deadline and attempt budget, classifies an error, applies bounded backoff with jitter only when retry is safe, and propagates capacity limits upstream. Circuit breakers, bulkheads and load shedding prevent one dependency from consuming every worker; recovery probes and gradual traffic return avoid a second overload.",
        "Healthy evidence shows bounded queues, stable retry ratios and recovery within an objective. Unbounded retries, identical timeouts at every layer, non-idempotent replays, shared resource pools and failover to an unqualified target commonly turn a small fault into an outage.",
    ),
    "data and model lifecycle": (
        "An AI result is produced by a release made of several moving parts—not only model weights. Data, tokenizer, prompt/template, adapter, retrieval index, runtime, hardware and evaluator can each change behavior.",
        "Inputs are validated and transformed, a versioned model or pipeline performs work, and post-processing and policy produce the exposed result. Offline evaluation compares a candidate with a baseline; shadow or canary traffic supplies production evidence; lineage connects the decision back to exact artifacts and data.",
        "Healthy evidence combines task quality and safety with latency, token or accelerator work, failure rate and unit cost. Training-serving skew, stale or unauthorized retrieval, incompatible runtime/hardware, biased evaluators, prompt injection and silent provider/model changes are core production risks.",
    ),
    "economics and governance": (
        "Governance is how a team makes repeated decisions visible and enforceable; economics shows which resources those decisions consume. Neither is a one-time approval or a monthly bill review.",
        "An asset or service receives an owner, lifecycle state, data/risk class, policy, budget and evidence requirements. Usage is attributed to stable organizational dimensions, compared with outcome and SLO, and reviewed through changes, exceptions and retirement; automated guardrails enforce the decisions at the relevant control point.",
        "Healthy evidence connects an accountable owner and approved intent to runtime inventory, audit and unit cost. Orphaned resources, permanent exceptions, unallocated shared cost, vanity utilization and savings that damage reliability or quality are common failure modes.",
    ),
    "state transition": (
        "The simplest mental model is a state machine: an input is checked, current state is read, a rule computes the next state, and an observable result tells callers whether the transition succeeded.",
        "The mechanism receives configuration or runtime input, validates preconditions, changes or derives state, and exposes status to the next component. Synchronous parts return a direct outcome; asynchronous parts need durable status, reconciliation and idempotency because the original caller may disappear.",
        "Healthy evidence shows the expected state transition and its owner, timestamp and reason. Invalid input, stale state, conflicting writers, hidden limits and dependencies that partially complete are the most useful failure categories to distinguish.",
    ),
}


# Exact explanations are used where a category-level model would hide an
# important distinction.  These are deliberately written as short textbook
# lessons: definition, analogy, mechanism, and production evidence.
EXACT_CONCEPT_DETAILS = {
    "virtual memory": (
        "Virtual memory is the per-process address space presented by the kernel. A virtual address is not a RAM location; page tables map it to a physical frame, a file-backed page, a shared frame, a swapped-out page or no page at all.",
        "Think of virtual addresses as apartment numbers and physical frames as rooms. Every process can use apartment 0x1000, while its private page table directs that number to a different room and permissions decide whether the room may be read, written or executed.",
        "When code reserves memory, the kernel usually creates a virtual mapping without immediately allocating every physical page. First access raises a page fault; the kernel validates the mapping, obtains or loads a page, updates the page table and resumes the instruction. The MMU and TLB accelerate later translations. Copy-on-write lets processes initially share a page and creates a private copy only after a write.",
        "`VSZ` can therefore be much larger than RAM without indicating a leak. Investigate RSS, proportional set size, anonymous versus file-backed pages, minor and major faults, swap and cgroup limits. Address-space exhaustion, permission faults, TLB pressure and overcommit/OOM behavior are distinct failure modes.",
    ),
    "resident memory": (
        "Resident memory is the subset of a process's mapped pages currently present in physical RAM. RSS counts resident pages but can double-count shared pages across processes, so it is not the same as uniquely owned memory.",
        "If virtual memory is a catalog of possible pages, resident memory is the set currently on the desk. Pages can enter on allocation or fault and leave through reclaim, unmapping, process exit or swap.",
        "The kernel updates mappings as pages are faulted in and reclaimed. Anonymous heap/stack, shared libraries, memory-mapped files and page-cache-backed mappings can all contribute to RSS. Proportional set size divides shared pages between users and is often better for estimating a process's real contribution.",
        "A healthy service has an RSS distribution compatible with its workload and cgroup limit. A steadily growing anonymous RSS, rising reclaim stalls or repeated cgroup `oom_kill` events is stronger leak or capacity evidence than one large VSZ value.",
    ),
    "shared memory": (
        "Shared memory maps the same physical pages into more than one process so processes can exchange data without copying it through a socket or file for every operation. POSIX shared memory, System V shared memory and shared `mmap` mappings provide related interfaces.",
        "It is like several workers using the same whiteboard: updates are immediately visible, but the whiteboard does not decide whose turn it is or whether a reader sees a complete multi-step update.",
        "The kernel creates a shared object or file-backed mapping and installs references to its pages in each participating process's page tables. The CPU cache-coherence system makes memory updates visible, while the application must use mutexes, semaphores, atomics or another protocol for ordering and consistency.",
        "Shared memory reduces copy and serialization cost but expands the corruption and synchronization blast radius. Inspect mapping size, ownership and permissions plus application lock contention; stale segments, permissive modes, false sharing and a crashed writer leaving inconsistent data are common failures.",
    ),
    "page cache": (
        "The page cache is RAM used by the Linux kernel to cache file contents. Reads can be served without another device access, and buffered writes modify cached pages before writeback makes them durable.",
        "It is a reusable reading desk for filesystem pages: keeping recently used pages nearby is faster than fetching them from storage again, and the desk can be cleared when applications need the space.",
        "A file read faults or copies pages into cache; later reads reuse them. A buffered write marks pages dirty, background writeback flushes them according to kernel thresholds, and `fsync` or related application ordering asks for durability under the storage contract. Clean cache is readily reclaimable, while dirty-page pressure can force foreground work to wait.",
        "High cache usage is normally healthy. Diagnose cache hit behavior, dirty/writeback pages, major faults, I/O latency and PSI together. Dropping caches in production destroys useful state and usually hides the real workload or storage bottleneck.",
    ),
    "buffers": (
        "In modern Linux memory reporting, buffers are primarily kernel memory used for block-device metadata and related I/O bookkeeping, while cached file contents are accounted mainly as page cache. The historical `buffers/cache` grouping is why the terms are often confused.",
        "Think of buffers as the labels and transfer paperwork around blocks, while the page cache is the file data being kept close for reuse.",
        "Kernel subsystems allocate buffer heads or other metadata structures to describe block mappings and I/O. These structures participate in reclaim and are reported separately or inside broader reclaimable slab/cache counters depending on the kernel and tool.",
        "Do not diagnose a leak from the `buff/cache` column alone. Use `/proc/meminfo`, slab information, reclaim and workload evidence to separate file cache, reclaimable kernel objects and unreclaimable slab growth.",
    ),
    "swap": (
        "Swap is disk- or device-backed space that can hold eligible anonymous memory pages evicted from RAM. It extends reclaim choices but is much slower than RAM and is not a substitute for sufficient capacity.",
        "Swap is an overflow storeroom: it can keep an infrequently used page instead of killing a process, but repeatedly walking to the storeroom makes active work very slow.",
        "Under pressure, the kernel selects cold anonymous pages, writes them to a swap area and updates their page-table entries. Access later causes a major fault and reads the page back. `swappiness`, memory cgroups, workload locking and platform policy influence use; file-backed clean pages can usually be dropped and reread instead.",
        "Some swap use can be harmless after an old pressure event. Sustained `si/so`, major faults and PSI with user latency indicates thrashing. Disabling swap changes failure behavior toward earlier OOM and may be required or discouraged by specific orchestration versions, so treat it as a workload/platform decision.",
    ),
    "memory pressure": (
        "Memory pressure is the condition in which workloads spend time reclaiming, compacting or waiting for memory because readily usable capacity is scarce. It is about stalled useful work, not merely a low `MemFree` value.",
        "A crowded room is not yet a problem if people can move; pressure begins when people must repeatedly stop, rearrange the room or leave before useful work continues.",
        "Allocation crosses watermarks and wakes background reclaim; heavier demand enters direct reclaim in the allocating task. The kernel drops cache, writes dirty pages, swaps eligible anonymous pages or compacts memory for contiguous allocations. If progress is impossible inside a host or cgroup boundary, OOM handling begins.",
        "Use memory PSI, reclaim scans, major faults, swap, dirty/writeback pages, cgroup `memory.events` and latency. A full page cache with low stalls is healthy; rising `some/full` PSI, allocation latency and OOM events is actionable pressure.",
    ),
    "out-of-memory killer": (
        "The OOM killer is the kernel's last-resort recovery mechanism when an allocation cannot make progress through reclaim under the applicable host or cgroup limit. It selects a process to terminate so memory becomes available.",
        "It is an emergency circuit breaker, not a fair workload scheduler: the kernel sacrifices a process to keep the rest of the system or constrained group alive.",
        "The kernel calculates badness using memory footprint and adjustments such as `oom_score_adj`; a memory-cgroup OOM normally chooses within that cgroup, while a global OOM can affect the host. Termination is recorded in kernel logs and cgroup counters, and an orchestrator may then restart the process.",
        "A restart can hide the event while data loss or a crash loop continues. Correlate kernel/cgroup OOM evidence with the limit, workload peak and restart reason. Durable fixes address leaks, sizing, admission or workload behavior rather than disabling the killer or granting unbounded memory.",
    ),
    "memory leaks": (
        "A memory leak occurs when a program retains allocations that are no longer useful, preventing the allocator and kernel from reclaiming them for other work. Growth can be in heap objects, native allocations, mappings, caches or kernel resources and is not always visible to one language profiler.",
        "It is like keeping every completed task on the active desk because a forgotten reference says it might still be needed.",
        "The allocator obtains pages from the operating system and suballocates objects. If reachable references, native handles or cache policy retain those objects, garbage collection cannot release them; even freed objects may stay in allocator arenas instead of immediately reducing RSS. The diagnostic method must match the allocation layer.",
        "Look for memory growth normalized by traffic and over a long enough window, then compare heap profiles, RSS/PSS, mappings and allocator metrics. A bounded cache, fragmentation and a true leak have different steady-state shapes and remediations; restart is containment, not the source repair.",
    ),
    "huge pages": (
        "Huge pages map memory with pages larger than the usual base page, reducing page-table entries and TLB misses for large, stable working sets. Linux supports explicitly reserved HugeTLB pages and transparent huge pages with different allocation behavior.",
        "A huge page is a large map tile: fewer tiles cover the same territory, so translation is cheaper, but finding one large contiguous empty space is harder and wasting part of a tile costs more.",
        "The kernel installs a larger page-table mapping and the TLB covers more bytes per entry. HugeTLB pools are reserved and explicitly consumed; transparent huge pages attempt promotion and may perform compaction. NUMA placement and application access patterns determine whether the reduction in translation overhead helps.",
        "Measure TLB misses and application throughput/latency before enabling broadly. Allocation failures, long compaction stalls, internal fragmentation and scarce reserved pages are common trade-offs; databases and model runtimes often require workload-specific qualification.",
    ),
    "numa": (
        "NUMA divides a multi-socket or large machine into nodes where CPUs access local memory faster than memory attached to another node. Total free memory can look sufficient while the local node needed by a workload is pressured.",
        "It resembles workers seated near different supply cabinets: every worker can reach every cabinet, but crossing the room for every item is slower and congests the shared path.",
        "Firmware exposes topology, Linux schedules threads and allocates pages using policy and first-touch behavior, and applications or runtimes may pin CPUs and memory. A thread migrating away from the node holding its pages increases remote accesses; multi-GPU workloads also depend on CPU, memory, PCIe and NIC locality.",
        "Inspect `numactl --hardware`, per-node memory and counters plus CPU/device topology. Poor pinning, unbalanced first touch and container CPU/memory policies can reduce throughput even when aggregate utilization appears moderate.",
    ),
    "api groups/versions": (
        "Kubernetes API groups organize related resource kinds and versions define the schema contract served to clients. A served version can differ from the storage version used in etcd, with conversion translating between them.",
        "Think of API versions as supported editions of a form: clients may submit an older or newer edition, while the records office keeps one canonical internal edition.",
        "The API server resolves group, version and resource from the URL, decodes and validates that schema, defaults fields and converts the object to an internal representation. Before persistence it converts to the configured storage version; reads reverse the conversion for the requested served version. CRDs can use conversion webhooks when schemas differ materially.",
        "Discovery endpoints and CRD/APIService status show what is served; `status.storedVersions` and deprecation metrics reveal migration work. Removing a served version before clients/manifests/controllers migrate causes request failure, while leaving old stored objects can break later conversion or rollback plans.",
    ),
    "request path": (
        "The Kubernetes API request path is the ordered chain that turns an HTTPS request into an authorized, admitted and persisted object or a precise rejection.",
        "It is a guarded records office: prove identity, check authority, apply controlled edits, validate the final form, then commit it to the ledger.",
        "After TLS termination and request parsing, authentication establishes user and groups; authorization evaluates the verb/resource/name/namespace; mutating admission can change the object; schema defaulting and validation establish a valid representation; validating admission enforces final policy; the registry layer applies concurrency and persistence through etcd. Audit stages can record receipt, response start and completion.",
        "HTTP status, audit events, admission messages, API latency histograms and etcd metrics localize failure. Webhook timeouts or broad failure-closed policies can block unrelated writes, while failure-open can bypass policy, so webhook scope, timeout and availability are production design decisions.",
    ),
    "watch": (
        "A Kubernetes watch is a long-lived API stream of resource changes after a known revision. Controllers use list-then-watch to maintain a local cache without repeatedly listing every object.",
        "It resembles subscribing to ledger updates after taking an initial snapshot: the snapshot gives current state and the update stream keeps the local copy current.",
        "A client lists objects and records the returned `resourceVersion`, starts a watch from that revision, then processes ADDED, MODIFIED, DELETED and BOOKMARK events. Client libraries relist or resume after disconnect. etcd compaction eventually removes old revisions, so a client that falls too far behind receives an expired-resource response and must rebuild its cache.",
        "Watch count, event rate, cache/list latency and client relist loops reveal health. Slow consumers, oversized objects, very broad watches and synchronized relists can overload the API server and etcd even when ordinary point reads still succeed.",
    ),
    "resourceversion": (
        "`resourceVersion` is Kubernetes' opaque concurrency and change-stream token for an observed object or collection state. It is not a wall-clock timestamp, generation number or value applications should numerically interpret.",
        "Treat it like a receipt number from the storage timeline: it lets the API detect whether you are updating the version you actually read and tells a watch where to continue.",
        "The API server returns the token on reads and lists. A conditional update includes the last observed value; if another writer changed the object, optimistic concurrency rejects the stale update. Watches use a collection revision to request later events, subject to cache and compaction semantics.",
        "Conflicts are normal evidence of concurrent writers and should trigger read-modify-retry with bounded logic, not forced overwrite. Expired versions require relist; copying tokens between unrelated objects or treating them as timestamps leads to incorrect ordering assumptions.",
    ),
    "server-side apply": (
        "Server-side apply is Kubernetes' declarative merge mechanism that records which field manager owns each field and reports conflicts when another manager tries to change owned intent.",
        "It is shared-document editing with named owners for individual fields rather than one owner for the entire file.",
        "A client sends an apply patch with a field-manager name. The API server compares the submitted field set with `managedFields`, merges associative structures using the schema, removes fields that manager previously owned but now omitted and rejects conflicting changes unless ownership is deliberately forced.",
        "Inspect `metadata.managedFields` and conflict responses to find competing controllers or tools. Reusing one manager name across unrelated automation hides ownership; forcing conflicts can steal fields from an active controller and cause an endless reconciliation fight.",
    ),
    "etcd quorum": (
        "An etcd quorum is the majority of voting members required for Raft to elect a leader and commit writes. In a three-member cluster, two members form quorum; losing two preserves data on disk but stops consistent progress.",
        "It is a committee rule: a proposal becomes official only after a majority records it, so any two majorities overlap and cannot approve conflicting histories.",
        "The leader appends a log entry and replicates it to followers; after a majority acknowledges durable log state, the entry commits and the state machine applies it. Leader election also requires majority communication. Adding members increases fault tolerance only at particular odd sizes and increases replication latency and operational complexity.",
        "Endpoint status, leader changes, proposal latency/failures and peer network/disk latency show health. Spreading members across unreliable high-latency links, losing quorum during maintenance or restoring members independently can threaten availability or consistency; recovery follows the documented snapshot/member procedure.",
    ),
    "compaction": (
        "etcd compaction discards old MVCC history before a selected revision while retaining current key values. It bounds historical revision growth but means a watch cannot resume from a compacted revision.",
        "It is removing old ledger pages after keeping the latest balance: current truth remains, but a subscriber that last read an old page must request a fresh snapshot.",
        "etcd stores multiple key revisions. Periodic or explicit compaction marks older revisions unavailable; later backend maintenance can reclaim physical space. Kubernetes clients that receive an expired revision relist current objects and restart their watch from the new list revision.",
        "Revision age, database size, watch expiry/relist rate and API list load must be considered together. Compacting does not immediately shrink the backend file, and overly slow clients can cause expensive relist storms after their revision disappears.",
    ),
    "defragmentation": (
        "etcd defragmentation rewrites the backend database to release free pages left after deletes and compaction. Compaction removes logical history; defragmentation is the separate physical space-reclamation step.",
        "Compaction crosses old entries out of a ledger; defragmentation copies the remaining entries into a clean, smaller book.",
        "The member rebuilds its backend file without unused pages. Defragmentation is performed per member and can block that member's reads and writes while it runs, so healthy quorum, load, free disk and member order matter.",
        "Compare logical database use with allocated backend size and watch request latency during maintenance. Running all members simultaneously or waiting until disk is nearly full can turn routine maintenance into control-plane unavailability.",
    ),
    "encryption at rest": (
        "Kubernetes encryption at rest transforms selected API resource values before the API server stores them in etcd. It protects raw etcd data or snapshots from directly revealing those values but does not prevent an authorized API read.",
        "It is an encrypted filing cabinet behind the API desk: stealing the cabinet contents is harder, while a clerk with permission can still retrieve and decrypt a record.",
        "The API server evaluates encryption providers in configuration order. The first provider writes new data and matching providers can read older ciphertext; envelope KMS providers use an external key service for key protection. Changing configuration affects new writes, so existing objects require a controlled rewrite to migrate ciphertext.",
        "Test key availability, rotation, API read/write behavior and snapshot recovery. Losing key access can make the control plane unable to read protected objects; leaving `identity` first silently stores plaintext, and encrypting secrets does not fix overly broad RBAC or secret exposure in workloads and logs.",
    ),
    "api priority/fairness": (
        "API Priority and Fairness classifies Kubernetes API requests into priority levels and flow queues so a noisy client cannot consume every API-server concurrency slot.",
        "It is a multi-lane service desk: emergency control traffic receives protected capacity, while callers within a class share queues instead of one caller occupying every clerk.",
        "Flow schemas match request attributes and assign a priority level. The API server queues requests into shuffled subqueues, executes them within the level's concurrency share and rejects excess waiting after limits. Long-running watches receive special treatment because their concurrency behavior differs from short mutating requests.",
        "Observe queue length, wait duration, rejected requests and per-flow classification together with client retry behavior. Incorrect broad matches can starve critical controllers, while aggressive retries after 429 responses can defeat fairness and increase control-plane load.",
    ),
}


CONTEXT_DEFINITIONS = {
    # Google Cloud resource hierarchy and governance.
    ("08-gcp", "*", "organizations"): "A Google Cloud organization is the top-level resource representing a company or institutional domain. It is the ancestor for folders and projects and the highest normal inheritance point for IAM and organization policy",
    ("08-gcp", "*", "folders"): "A Google Cloud folder is an optional grouping node between the organization and projects. Folders model departments, environments or policy boundaries and pass inherited IAM and organization policies to their descendants",
    ("08-gcp", "*", "projects"): "A Google Cloud project is the main ownership, API enablement, quota and billing container for cloud resources. Resources belong to a project even when their data plane is regional, zonal or global",
    ("08-gcp", "*", "billing accounts"): "A billing account is the payment and invoicing relationship linked to one or more projects. Linking a project enables billable use but does not grant IAM access to that project's resources",
    ("08-gcp", "*", "resource hierarchy"): "The Google Cloud resource hierarchy is the organization → folder → project → resource ancestry used for policy inheritance, ownership and inventory. A child receives applicable ancestor policy in addition to policy set directly on it",
    ("08-gcp", "*", "iam principals"): "IAM principals are the identities that can request Google Cloud actions, including users, groups, service accounts, workforce identities and federated workload identities",
    ("08-gcp", "*", "roles"): "A Google Cloud IAM role is a named bundle of permissions. Basic, predefined and custom roles differ in scope and maintenance; a role grants nothing until an IAM policy binds it to a principal on a resource",
    ("08-gcp", "*", "service accounts"): "A Google Cloud service account is a project-owned workload identity used by applications and automation. Code should obtain short-lived credentials for it instead of distributing long-lived service-account keys",
    ("08-gcp", "*", "workload identity federation"): "Workload Identity Federation exchanges a trusted external OIDC or AWS identity assertion for short-lived Google Cloud credentials without storing a Google service-account key in the external system",
    ("08-gcp", "*", "organization policies"): "Organization Policy Service applies inherited constraints to resource configuration, such as allowed locations or whether a capability may be enabled. It limits what configurations are permitted but does not replace IAM authorization",
    ("08-gcp", "*", "labels and tags"): "Labels are resource metadata mainly used for organization and cost reporting, while Resource Manager tags are hierarchical key/value resources that can participate in supported policy conditions. Their enforcement semantics are not interchangeable",
    ("08-gcp", "*", "quotas"): "Google Cloud quotas limit resource counts, allocation or API rate for a project, user or Region. They protect shared capacity and spending but can block scale-out before a workload reaches a machine-level bottleneck",
    ("08-gcp", "*", "cloud asset inventory"): "Cloud Asset Inventory records supported resource metadata, IAM policy and change history across a project, folder or organization so teams can query inventory, relationships and drift centrally",

    # Terraform's language and graph model.
    ("09-iac-delivery", "terraform fundamentals", "hcl"): "HashiCorp Configuration Language is Terraform's declarative configuration syntax. Blocks describe objects and relationships, while expressions compute values; HCL describes desired configuration rather than an ordered shell script",
    ("09-iac-delivery", "terraform fundamentals", "providers"): "A Terraform provider is a versioned plugin that defines resource and data-source schemas and translates Terraform operations into remote API calls. Provider version, configuration and credentials are part of the execution contract",
    ("09-iac-delivery", "terraform fundamentals", "resources"): "A Terraform resource block declares a managed object's desired arguments. Its resource address is associated through state with a remote identity so Terraform can plan create, read, update or delete operations",
    ("09-iac-delivery", "terraform fundamentals", "data sources"): "A Terraform data source reads information managed outside the current resource address. It supplies values to the graph but does not make Terraform the lifecycle owner of the remote object",
    ("09-iac-delivery", "terraform fundamentals", "variables"): "Terraform input variables are the typed external parameters of a module. Defaults, validation, sensitivity and nullable behavior define the module's caller contract",
    ("09-iac-delivery", "terraform fundamentals", "local values"): "Terraform local values give names to expressions inside a module. They reduce repetition and centralize transformation but are not external inputs and do not create independently stored resources",
    ("09-iac-delivery", "terraform fundamentals", "outputs"): "Terraform outputs expose selected root-module results or child-module return values. An output can depend on values unknown until apply and marking it sensitive only redacts normal display—it may still exist in state",
    ("09-iac-delivery", "terraform fundamentals", "expressions"): "Terraform expressions combine literals, references, operators, conditionals and collection transformations to compute typed values. References also let Terraform infer dependency edges",
    ("09-iac-delivery", "terraform fundamentals", "functions"): "Terraform functions are built-in pure transformations such as encoding, string, collection and filesystem helpers. They return values during configuration evaluation and do not call providers or create resources",
    ("09-iac-delivery", "terraform fundamentals", "dependency graph"): "Terraform builds a directed dependency graph from references and explicit `depends_on` relationships. It walks independent vertices concurrently and orders operations whose correctness depends on another object",

    # Core observability signals.
    ("10-operations", "observability fundamentals", "metrics"): "Metrics are timestamped numeric measurements, usually organized as time series with bounded labels. Counters, gauges and histogram-like distributions summarize rates, levels and latency without preserving every individual event",
    ("10-operations", "observability fundamentals", "logs"): "Logs are discrete timestamped records of events or state transitions. Structured logs make stable fields queryable, while message text and high-cardinality identifiers preserve detail that would be unsafe or expensive as metric labels",
    ("10-operations", "observability fundamentals", "traces"): "A distributed trace represents one request or unit of work as causally related spans across services. Each span records timing, status, attributes and parent/child context for one operation boundary",
    ("10-operations", "observability fundamentals", "events"): "Operational events are discrete records that something happened, such as a deployment, scheduler decision or resource state change. They add change context but may be best-effort and short-lived rather than a durable audit history",
    ("10-operations", "observability fundamentals", "profiles"): "Profiles aggregate where a program spends CPU time, allocations, lock wait or other sampled resources. They attribute cost inside a process when request-level metrics or traces show that a service is slow but not which code consumes the resource",
    ("10-operations", "observability fundamentals", "correlation"): "Correlation connects signals that describe the same request, revision, tenant or incident window. It narrows investigation but does not by itself prove causation; time, propagation and dependency evidence still matter",
    ("10-operations", "observability fundamentals", "context propagation"): "Context propagation carries trace, correlation and selected baggage fields across process and asynchronous boundaries so downstream telemetry can be joined to the originating work without relying only on timestamps",
    ("10-operations", "observability fundamentals", "structured telemetry"): "Structured telemetry encodes fields according to a stable schema instead of embedding all meaning in free text. Consistent names, units and semantic conventions make queries and cross-service correlation reliable",
}


DEFAULT_COMMANDS = {
    "00-role-ownership": ("git log --since='30 days ago' --stat", "git shortlog -sn"),
    "01-foundations": ("lscpu", "free -h", "ss -s"),
    "02-linux": ("uname -a", "systemctl --failed", "journalctl -b -p warning --no-pager"),
    "03-networking": ("ip -br addr", "ip route", "getent ahosts NAME", "curl -v URL"),
    "04-git-delivery": ("git status --short", "git log --graph --oneline --decorate -10", "git diff --check"),
    "05-containers": ("docker image inspect IMAGE", "docker inspect CONTAINER", "docker stats --no-stream CONTAINER"),
    "06-kubernetes": ("kubectl config current-context", "kubectl get nodes -o wide", "kubectl get events -A --sort-by=.lastTimestamp"),
    "07-aws": ("aws sts get-caller-identity", "aws configure list", "aws resourcegroupstaggingapi get-resources --resources-per-page 5"),
    "08-gcp": ("gcloud auth list", "gcloud config list", "gcloud projects describe PROJECT"),
    "09-iac-delivery": ("terraform fmt -check -recursive", "terraform validate", "terraform plan"),
    "10-operations": ("date -u", "curl -sS URL/metrics", "kubectl get events -A --sort-by=.lastTimestamp"),
    "11-ai-platform": ("nvidia-smi", "curl -sS MODEL_URL/metrics", "python -m pytest -q"),
    "12-platform-engineering": ("git diff --check", "python -m pytest -q", "go test ./..."),
    "13-scenarios": ("date -u", "whoami", "git log --since='2 hours ago' --oneline"),
}


def area_key(area: str) -> str:
    """Return a known top-level area key even when a nested path is supplied."""
    for key in AREA_HISTORY:
        if area == key or area.startswith(key + "/"):
            return key
    return "01-foundations"


def split_concept(entry: str) -> tuple[str, str]:
    name, sep, description = entry.partition(" — ")
    return name.strip(), description.strip().rstrip(".") if sep else ""


def concept_kind(name: str, description: str, title: str = "", area: str = "") -> str:
    name_value = name.lower()
    title_value = title.lower()
    key = area_key(area) if area else ""

    if "observab" in title_value and re.search(r"event|signal|correlation|context|telemetry", name_value):
        return "telemetry"
    if re.search(r"messag|event.driven|stream|queue", title_value) and re.search(r"event|stream|topic|subscription|consumer|producer", name_value):
        return "queued work"
    if key == "08-gcp" and name_value in {
        "organizations", "folders", "projects", "billing accounts",
        "resource hierarchy", "labels and tags", "quotas", "cloud asset inventory",
    }:
        return "economics and governance"

    # The concept name is more authoritative than broad vocabulary in its
    # description. For example, "traces" must select telemetry even when a
    # generic description mentions event state.
    for kind, pattern in KIND_PATTERNS:
        if re.search(pattern, name_value):
            return kind

    if key in AREA_DEFAULT_KIND:
        return AREA_DEFAULT_KIND[key]

    value = f"{name} {description}".lower()
    for kind, pattern in KIND_PATTERNS:
        if re.search(pattern, value):
            return kind
    return "state transition"


def usable_description(name: str, description: str, title: str, area: str) -> str:
    exact = EXACT_CONCEPT_DETAILS.get(name.lower())
    if exact:
        return exact[0].rstrip(".")
    key = area_key(area)
    contextual = CONTEXT_DEFINITIONS.get((key, title.lower(), name.lower()))
    if contextual is None:
        contextual = CONTEXT_DEFINITIONS.get((key, "*", name.lower()))
    if contextual:
        return contextual.rstrip(".")
    placeholder = "learn its precise definition" in description.lower() or not description
    if placeholder:
        for pattern, meaning in FALLBACK_DEFINITION_RULES:
            if re.search(pattern, name.lower()):
                return f"The term {name} {meaning} within {title}"
        fallback = AREA_FALLBACK[area_key(area)]
        return f"The term {name} refers to {fallback} within {title}"
    return description[0].upper() + description[1:]


def answer_mechanism(name: str, description: str, title: str = "", area: str = "") -> str:
    """Return the mechanism paragraph used by detailed interview answers."""
    exact = EXACT_CONCEPT_DETAILS.get(name.lower())
    if exact:
        return exact[2]
    return KIND_EXPLANATIONS[concept_kind(name, description, title, area)][1]


def answer_evidence(name: str, description: str, title: str = "", area: str = "") -> str:
    """Return production evidence and failure behavior for an answer."""
    exact = EXACT_CONCEPT_DETAILS.get(name.lower())
    if exact:
        return exact[3]
    return KIND_EXPLANATIONS[concept_kind(name, description, title, area)][2]


def history_text(title: str, area: str, purpose: str = "") -> str:
    key = area_key(area)
    purpose_sentence = purpose.strip().rstrip(".")
    modern = (
        f"In this chapter, **{title}** is the next layer of that evolution. Its modern purpose is to {purpose_sentence[0].lower() + purpose_sentence[1:]}"
        if purpose_sentence
        else f"In this chapter, **{title}** is the next layer of that evolution: it packages earlier mechanisms into a repeatable production capability"
    )
    return f"{AREA_HISTORY[key]}\n\n{modern}. The exact product surface may change by version, but the underlying state, request path and failure boundaries remain the durable ideas to learn."


def junior_intro(title: str, area: str, purpose: str, concepts: list[str]) -> str:
    key = area_key(area)
    examples = ", ".join(concepts[:4])
    return (
        f"**{title}** is easiest to understand as one part of a larger path. {AREA_INTRO[key]}\n\n"
        f"The chapter focuses on {examples or title}. These are connected mechanisms, not vocabulary to memorize. "
        f"{purpose.strip().rstrip('.')} The explanations below first build the simple model, then add the exact system behavior and production consequences."
    )


def flow_diagram(title: str, area: str) -> str:
    first, second, third, fourth = AREA_FLOW[area_key(area)]
    return f"""```mermaid
flowchart LR
  A[\"{first}\"] --> B[\"{second}\"]
  B --> C[\"{title}: {third}\"]
  C --> D[\"{fourth}\"]
  D -. \"status and evidence\" .-> B
```"""


def concept_explanations(concepts: tuple[str, ...], title: str, area: str) -> str:
    sections: list[str] = []
    for entry in concepts:
        name, raw_description = split_concept(entry)
        exact = EXACT_CONCEPT_DETAILS.get(name.lower())
        if exact:
            definition, analogy, mechanism, evidence = exact
            sections.extend(
                [
                    f"#### {name}",
                    "",
                    f"**What it is.** {definition}",
                    "",
                    f"**Junior mental model.** {analogy}",
                    "",
                    f"**How it works.** {mechanism}",
                    "",
                    f"**What it looks like in production.** {evidence}",
                    "",
                ]
            )
            continue
        description = usable_description(name, raw_description, title, area)
        kind = concept_kind(name, description, title, area)
        analogy, mechanism, evidence = KIND_EXPLANATIONS[kind]
        sections.extend(
            [
                f"#### {name}",
                "",
                f"**What it is.** {description.rstrip('.')}.",
                "",
                f"**Junior mental model.** {analogy}",
                "",
                f"**How it works.** {mechanism}",
                "",
                f"**What it looks like in production.** {evidence}",
                "",
            ]
        )
    return "\n".join(sections).rstrip()


def capability_table(concepts: tuple[str, ...]) -> str:
    rows = []
    for index, entry in enumerate(concepts, 1):
        name, description = split_concept(entry)
        rows.append(f"| {index} | **{name}** | {description or 'Explain its meaning, mechanism, evidence, failure modes and trade-offs.'} |")
    return "\n".join(rows)


def command_explanation(command: str) -> str:
    lower = command.lower()
    if "current-context" in lower or "get-caller-identity" in lower or "auth list" in lower or "config list" in lower:
        return "establishes which identity and target context subsequent commands will inspect; a correct resource in the wrong account, project or cluster is still the wrong result"
    if lower.startswith("kubectl"):
        return "reads Kubernetes API desired/status state or recent reconciliation evidence without treating a single `Ready` value as proof of the user journey"
    if lower.startswith("aws "):
        return "queries the AWS service control plane; IDs, Region, status/reason fields and request attribution should be correlated with CloudTrail and service metrics"
    if lower.startswith("gcloud "):
        return "queries Google Cloud's control plane using the active account, project and location; compare the returned resource with source-controlled intent"
    if "terraform" in lower or "pulumi" in lower:
        return "checks configuration or previews the dependency-aware state transition before any apply; the preview must be reviewed for replacement, deletion, identity and cost"
    if lower.startswith("docker") or "ctr " in lower or "crictl" in lower:
        return "shows image or runtime state so you can separate declared container configuration from the host process, namespaces and resource limits that actually exist"
    if "curl" in lower or "openssl" in lower or "dig" in lower or "getent" in lower or "tcpdump" in lower:
        return "tests one part of the end-to-end request path and preserves protocol-level evidence such as resolution, connection, handshake, status or packet direction"
    if lower.startswith("git "):
        return "inspects the repository's object graph, refs or diff so a delivery decision is tied to exact content rather than an assumed branch name"
    if "nvidia-smi" in lower:
        return "shows the host-visible GPU, driver, topology or workload state; it proves hardware visibility but not framework compatibility or useful model goodput"
    return "captures a read-oriented state snapshot that must be interpreted against a healthy baseline, the exact target and the next adjacent dependency"


def worked_example(commands: tuple[str, ...], title: str) -> str:
    commands = commands or ("inspect RESOURCE",)
    code = "\n".join(commands)
    explanations = "\n".join(f"- `{command}` {command_explanation(command)}." for command in commands)
    return f"""The following is a diagnostic example, not an unexplained command dump. Define every uppercase placeholder first—for example `NAME`, `RESOURCE`, `PROJECT`, `REGION`, `NAMESPACE`, `URL`, `IMAGE` or `CONTAINER`—and use a sandbox or read-only production role.

```bash
{code}
```

What the example demonstrates:

{explanations}

A healthy run returns the intended identity/context, exits successfully and shows the expected object or response without a new warning, retry loop or saturation signal. A failure is useful evidence: preserve the exact exit code, status/reason, timestamp and target, then inspect the immediately adjacent layer before changing anything. This makes the example part of the explanation of **{title}**, not merely a list to copy."""


def practice_session(
    title: str,
    area: str,
    commands: tuple[str, ...] | None = None,
    lab: str | None = None,
) -> str:
    selected = commands or DEFAULT_COMMANDS[area_key(area)]
    code = "\n".join(selected)
    setup = lab or (
        "Use a disposable local environment, sandbox account/project or isolated namespace. Confirm the effective identity and target, record the start time, and set a cost limit before creating anything."
    )
    return f"""### Practice objective

Build a small, safe proof of **{title}** and explain the result in your own words. The goal is not command completion; it is to connect input, internal mechanism, observable state and user outcome.

### Prerequisites and setup

{setup}

Record tool and platform versions because flags, APIs and defaults can change. Define every uppercase placeholder before use and keep secrets out of shell history and committed files.

### Activity 1: establish a healthy baseline

Run the read-oriented example first:

```bash
{code}
```

For each line, write down the layer it inspects, the expected healthy field or response, and one thing it cannot prove. The expected result is an attributable request against the intended target plus enough state to draw the path from input to outcome.

### Activity 2: create or review the smallest working example

Put the smallest relevant command, configuration, manifest or code sample in source control. Validate or lint it, produce a preview/diff where the tool supports one, and apply only inside the disposable boundary. Record the exact revision and resulting resource or process ID. If the topic is observational rather than configurable, save a sanitized baseline and an automated assertion instead of mutating the system.

### Activity 3: controlled failure and troubleshooting

Introduce one bounded failure: use a definitely nonexistent resource name, an invalid sandbox-only value, a denied test identity, a closed test port or a stopped disposable dependency. Capture the exact error and classify it as identity/policy, input/configuration, control-plane reconciliation, network/protocol, dependency or capacity. Test one discriminating hypothesis at a time; do not widen access or restart unrelated components.

Expected failure evidence is a specific non-zero exit, status/reason, event or protocol response that disappears when the controlled fault is removed. If healthy and failing runs look identical, the chosen signal does not explain the phenomenon and the exercise is not complete.

### Verification

Repeat the original client or user-facing check, not only an administrative status command. Confirm the desired revision, data correctness where applicable, error and latency recovery, and absence of a continuing retry/backlog/saturation condition. Explain why this evidence proves recovery and what uncertainty remains.

### Cleanup and rollback

Revert the configuration in its source of truth and review the rollback diff before applying it. Delete only the named sandbox resources, stop disposable processes, remove temporary credentials and verify that no billable resource, volume, artifact, queue item or background job remains. Read-only activities require no infrastructure rollback, but sanitized captures must still follow retention policy.

### Harder extension

Automate the healthy and failing paths in CI, use short-lived identity, add one SLI/alert or policy assertion, and write a five-step runbook another engineer can execute without hidden context. Then explain how the design changes for two tenants, a zonal or dependency failure, 10× load and a strict cost or recovery target."""
