#!/usr/bin/env python3
"""Number every study topic and maintain one continuous handbook reading path.

The root README is the only table of contents. Topic READMEs form a depth-first
sequence; their question banks are linked practice detours rather than steps in
that sequence. The script is idempotent and also numbers newly added topics.
"""

from __future__ import annotations

import os
from pathlib import Path
import re
from dataclasses import dataclass


ROOT = Path(__file__).resolve().parents[1]

TOP_LEVEL_ORDER = [
    "role-ownership",
    "foundations",
    "linux",
    "networking",
    "git-delivery",
    "containers",
    "kubernetes",
    "aws",
    "gcp",
    "iac-delivery",
    "operations",
    "ai-platform",
    "platform-engineering",
    "scenarios",
]

# These two branches do not contain a complete curated child list elsewhere in
# their notes. Their order is therefore kept explicitly as prerequisite-first.
MANUAL_CHILD_ORDER = {
    "kubernetes": [
        "architecture",
        "workloads",
        "networking",
        "storage",
        "security",
        "scheduling-autoscaling",
        "packaging-extensions",
        "operations",
        "gpu-llmops",
    ],
    "ai-platform/mlops-and-llmops-lifecycle": [
        "lifecycle-platform-architecture",
        "experiment-tracking",
        "data-versioning-quality-lineage",
        "feature-store-training-serving",
        "pipeline-orchestration",
        "training-platform",
        "distributed-training",
        "hyperparameter-tuning",
        "reproducibility-environments",
        "model-registry-artifact-lineage",
        "llm-release-manifest",
        "model-validation-release-gates",
        "deployment-progressive-release",
        "monitoring-drift",
        "retraining-feedback-loops",
        "promptops",
        "llm-finetuning-peft",
        "ragops-index-lifecycle",
        "evalops",
        "gateway-providerops",
        "agentops",
        "llm-observability",
        "safety-redteam-guardrails",
        "governance-approval-evidence",
        "ai-supply-chain",
        "ai-finops-capacity",
    ],
}

NUMBER_PREFIX = re.compile(r"^\d{2,3}-(.+)$")
MARKDOWN_LINK = re.compile(
    r"(?P<open>!?\[[^\]\n]*\]\()(?P<target>[^)\n]+)(?P<close>\))"
)
OLD_TOC = re.compile(
    r"\n?<!-- child-topic-toc:start -->.*?<!-- child-topic-toc:end -->\n?",
    re.S,
)
READING_NAV = re.compile(
    r"\n?<!-- reading-navigation:start -->.*?<!-- reading-navigation:end -->\n?",
    re.S,
)
COMPLETE_TOC = re.compile(
    r"\n?<!-- complete-reading-path:start -->.*?<!-- complete-reading-path:end -->\n?",
    re.S,
)
GENERATED_LOCAL_INDEX = re.compile(
    r"\n?<!-- generated-topic-index:start -->.*?<!-- generated-topic-index:end -->\n?",
    re.S,
)
LOCAL_SERVICE_INDEX = re.compile(
    r"\n## Service leaves\n.*?(?=\n## |\n<!-- reading-navigation:start -->|\Z)",
    re.S,
)
CHAPTER_GUIDE = re.compile(
    r"\n?<!-- chapter-guide:start -->.*?<!-- chapter-guide:end -->\n?",
    re.S,
)
REVIEW_LINE = re.compile(r"^> \*\*Covered in:\*\* .*\n?", re.M)
QUESTION_LINE = re.compile(r"^- \[[ xX]\].*\*\*Question:\*\*(.*)$", re.M)
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
WORD = re.compile(r"[a-z0-9][a-z0-9+#./-]*")

STOP_WORDS = {
    "a", "about", "after", "all", "an", "and", "are", "as", "at",
    "be", "because", "before", "but", "by", "can", "code", "could",
    "describe", "do", "does", "during", "explain", "for", "from", "give",
    "how", "i", "if", "in", "into", "is", "it", "its", "name", "of",
    "on", "or", "our", "should", "that", "the", "their", "then", "this",
    "to", "use", "using", "versus", "what", "when", "where", "which",
    "why", "with", "would", "you", "your",
}

SCENARIO_CONTEXT_ROOTS = {
    "linux and host incidents": ["linux"],
    "networking dns tls and load balancing": ["networking"],
    "containers and software supply chain": ["containers", "operations/platform-and-cloud-security"],
    "kubernetes control plane and cluster lifecycle": ["kubernetes"],
    "kubernetes workloads network and storage": ["kubernetes"],
    "aws production operations": ["aws"],
    "gcp and multi cloud operations": ["gcp", "platform-engineering/multi-cloud-architecture"],
    "terraform pulumi ci/cd and gitops": ["iac-delivery"],
    "observability sre and disaster recovery": ["operations"],
    "security and incident response": ["operations/platform-and-cloud-security", "operations/sre-and-reliability-engineering"],
    "gpu infrastructure": ["ai-platform/gpu-compute-architecture", "kubernetes/gpu-llmops"],
    "model serving and inference": ["ai-platform/model-serving-and-inference-platforms"],
    "llm gateway and provider operations": ["ai-platform/llm-gateway", "ai-platform/mlops-and-llmops-lifecycle/gateway-providerops"],
    "rag evaluation agents and ai governance": ["ai-platform"],
    "platform ownership deployment models and finops": ["role-ownership", "platform-engineering"],
}

# The cross-domain scenario bank is curated and stable, so route each scenario
# to the chapter that actually teaches its primary discriminating mechanism.
# The list order matches the ten questions under each scenario heading.
SCENARIO_TARGETS = {
    "linux and host incidents": [
        "linux/cpu-performance",
        "linux/memory",
        "linux/filesystems",
        "linux/filesystems",
        "linux/systemd",
        "linux/linux-logs-and-troubleshooting",
        "linux/cpu-performance",
        "linux/linux-networking",
        "linux/storage-and-i-o",
        "linux/linux-architecture",
    ],
    "networking dns tls and load balancing": [
        "networking/dns",
        "networking/tls-and-certificates",
        "networking/load-balancing",
        "networking/network-troubleshooting",
        "networking/routing",
        "networking/dns",
        "networking/proxies-and-gateways",
        "networking/firewalls-and-nat",
        "kubernetes/networking/networkpolicy",
        "networking/tls-and-certificates",
    ],
    "containers and software supply chain": [
        "containers/docker-runtime",
        "containers/registries",
        "containers/container-security",
        "containers/container-storage",
        "containers/container-internals",
        "containers/container-security",
        "containers/docker-images",
        "containers/registries",
        "containers/container-security",
        "containers/container-security",
    ],
    "kubernetes control plane and cluster lifecycle": [
        "kubernetes/architecture/api-server-etcd",
        "kubernetes/architecture/api-server-etcd",
        "kubernetes/security/admission-policies-webhooks",
        "kubernetes/architecture/scheduler-controllers-kubelet",
        "kubernetes/operations/upgrades",
        "kubernetes/architecture/scheduler-controllers-kubelet",
        "kubernetes/architecture/scheduler-controllers-kubelet",
        "kubernetes/packaging-extensions/crds-operators",
        "kubernetes/operations/backup-dr-etcd",
        "kubernetes/architecture/api-server-etcd",
    ],
    "kubernetes workloads network and storage": [
        "kubernetes/workloads/deployments",
        "kubernetes/networking/services-endpoints-dns",
        "kubernetes/storage/pv-pvc-storageclass",
        "kubernetes/workloads/probes-lifecycle",
        "kubernetes/scheduling-autoscaling/disruption-priority",
        "kubernetes/workloads/statefulsets-daemonsets",
        "kubernetes/workloads/jobs-cronjobs",
        "kubernetes/networking/networkpolicy",
        "kubernetes/scheduling-autoscaling/requests-limits-qos",
        "kubernetes/networking/services-endpoints-dns",
    ],
    "aws production operations": [
        "aws/networking/endpoints-privatelink",
        "aws/compute/ec2-auto-scaling",
        "aws/storage/s3",
        "aws/databases/dynamodb",
        "aws/messaging-serverless/lambda",
        "aws/ai-platform/aws-accelerators",
        "aws/security-operations/cloudtrail-config",
        "aws/security-operations/kms",
        "aws/networking/route53",
        "aws/networking/nat-egress",
    ],
    "gcp and multi cloud operations": [
        "gcp/gcp-foundations-and-governance",
        "gcp/gcp-networking",
        "gcp/gcp-load-balancing",
        "gcp/gcp-compute-and-containers",
        "gcp/vertex-ai-and-gcp-ai-platform",
        "gcp/gcp-compute-and-containers",
        "gcp/gcp-messaging-and-data-processing",
        "platform-engineering/multi-cloud-architecture",
        "gcp/gcp-operations-security-and-cost",
        "gcp/gcp-foundations-and-governance",
    ],
    "terraform pulumi ci/cd and gitops": [
        "iac-delivery/terraform/terraform-resource-lifecycle",
        "iac-delivery/terraform/terraform-state",
        "iac-delivery/terraform/import-and-refactoring",
        "iac-delivery/pulumi/pulumi-concepts",
        "iac-delivery/ci-cd/ci-cd-security",
        "iac-delivery/ci-cd/gitops",
        "iac-delivery/ci-cd/deployment-strategies",
        "iac-delivery/ci-cd/cd-fundamentals",
        "iac-delivery/terraform/terraform-planning",
        "git-delivery/git-security",
    ],
    "observability sre and disaster recovery": [
        "operations/observability/observability-fundamentals",
        "operations/observability/metrics",
        "operations/observability/distributed-tracing",
        "operations/sre-and-reliability-engineering/alerting",
        "operations/sre-and-reliability-engineering/service-indicators-and-objectives",
        "operations/sre-and-reliability-engineering/reliability-concepts",
        "operations/sre-and-reliability-engineering/disaster-recovery",
        "operations/sre-and-reliability-engineering/disaster-recovery",
        "operations/observability/observability-fundamentals",
        "operations/sre-and-reliability-engineering/post-incident-work",
    ],
    "security and incident response": [
        "operations/platform-and-cloud-security/secret-management",
        "kubernetes/security/authn-rbac-serviceaccounts",
        "operations/platform-and-cloud-security/software-supply-chain",
        "operations/platform-and-cloud-security/network-security",
        "operations/platform-and-cloud-security/secret-management",
        "kubernetes/security/multitenancy",
        "operations/platform-and-cloud-security/vulnerability-management",
        "operations/platform-and-cloud-security/network-security",
        "operations/platform-and-cloud-security/compliance-evidence",
        "role-ownership/contractor-and-remote-work-readiness",
    ],
    "gpu infrastructure": [
        "kubernetes/gpu-llmops/gpu-operator-dra",
        "ai-platform/gpu-compute-architecture",
        "ai-platform/gpu-compute-architecture",
        "ai-platform/gpu-compute-architecture",
        "kubernetes/gpu-llmops/gpu-sharing-scheduling",
        "kubernetes/gpu-llmops/gpu-sharing-scheduling",
        "kubernetes/gpu-llmops/gpu-sharing-scheduling",
        "ai-platform/mlops-and-llmops-lifecycle/distributed-training",
        "kubernetes/gpu-llmops/model-serving",
        "kubernetes/gpu-llmops/gpu-operator-dra",
    ],
    "model serving and inference": [
        "ai-platform/model-serving-and-inference-platforms/model-loading-lifecycle",
        "ai-platform/model-serving-and-inference-platforms/inference-performance",
        "ai-platform/model-serving-and-inference-platforms/inference-performance",
        "ai-platform/model-serving-and-inference-platforms/model-release-strategies",
        "ai-platform/model-serving-and-inference-platforms/vllm",
        "ai-platform/model-serving-and-inference-platforms/kserve",
        "ai-platform/model-serving-and-inference-platforms/multi-model-serving",
        "ai-platform/model-serving-and-inference-platforms/inference-performance",
        "ai-platform/model-serving-and-inference-platforms/serving-failure-modes",
        "ai-platform/model-serving-and-inference-platforms/scaling-inference",
    ],
    "llm gateway and provider operations": [
        "ai-platform/llm-gateway/traffic-control",
        "ai-platform/llm-gateway/reliability",
        "ai-platform/llm-gateway/routing",
        "ai-platform/llm-gateway/reliability",
        "ai-platform/llm-gateway/caching",
        "ai-platform/llm-gateway/routing",
        "ai-platform/llm-gateway/cost-management",
        "ai-platform/llm-gateway/security-policies",
        "ai-platform/llm-gateway/gateway-observability",
        "ai-platform/llm-gateway/gateway-observability",
    ],
    "rag evaluation agents and ai governance": [
        "ai-platform/rag-engineering/rag-security",
        "ai-platform/rag-engineering/rag-freshness-and-lifecycle",
        "ai-platform/ai-evaluation-infrastructure/rag-metrics",
        "ai-platform/ai-evaluation-infrastructure/evaluation-reliability",
        "ai-platform/ai-evaluation-infrastructure/release-gates",
        "ai-platform/ai-and-llm-security/prompt-injection",
        "ai-platform/agents-and-tool-using-ai",
        "ai-platform/mlops-and-llmops-lifecycle/promptops",
        "ai-platform/ai-governance/ai-asset-inventory",
        "ai-platform/ai-governance/policy-enforcement",
    ],
    "platform ownership deployment models and finops": [
        "role-ownership/taking-ownership-of-an-existing-platform",
        "platform-engineering/customer-private-cloud-deployment",
        "platform-engineering/on-premises-deployment",
        "platform-engineering/air-gapped-and-restricted-environments",
        "platform-engineering/multi-cloud-architecture",
        "platform-engineering/ai-finops-and-cost-control/cost-optimization",
        "platform-engineering/internal-developer-platform-for-ai/golden-paths",
        "platform-engineering/ai-finops-and-cost-control/cost-optimization",
        "role-ownership/operating-model",
        "scenarios/leadership-and-behavioural-questions",
    ],
}


@dataclass(frozen=True)
class StudySection:
    document: Path
    document_title: str
    heading: str
    anchor: str
    heading_tokens: frozenset[str]
    content_tokens: frozenset[str]


def unnumbered(name: str) -> str:
    match = NUMBER_PREFIX.match(name)
    return match.group(1) if match else name


def canonical_key(path: Path) -> str:
    return "/".join(unnumbered(part) for part in path.relative_to(ROOT).parts)


def is_topic(directory: Path) -> bool:
    return (directory / "README.md").is_file() and (
        directory / "questions-and-answers.md"
    ).is_file()


def top_level_topics() -> list[Path]:
    by_name = {
        unnumbered(path.name): path
        for path in ROOT.iterdir()
        if path.is_dir() and is_topic(path)
    }
    missing = [name for name in TOP_LEVEL_ORDER if name not in by_name]
    if missing:
        raise RuntimeError(f"missing top-level study topics: {', '.join(missing)}")
    return [by_name[name] for name in TOP_LEVEL_ORDER]


def topic_children(directory: Path) -> list[Path]:
    return [
        child
        for child in directory.iterdir()
        if child.is_dir() and not child.name.startswith(".") and is_topic(child)
    ]


def clean_for_ordering(text: str) -> str:
    return READING_NAV.sub("\n", OLD_TOC.sub("\n", text))


def local_link_target(document: Path, raw: str) -> Path | None:
    value = raw.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1]
    value = value.split(maxsplit=1)[0]
    if not value or value.startswith(("#", "/", "http://", "https://", "mailto:")):
        return None
    value = value.split("#", 1)[0].split("?", 1)[0]
    return (document.parent / value).resolve()


def linked_child_order(parent: Path, children: list[Path]) -> list[Path]:
    """Recover curated order from this README, then its ancestor READMEs."""
    ordered: list[Path] = []
    scan = [parent]
    cursor = parent.parent
    while cursor == ROOT or ROOT in cursor.parents:
        scan.append(cursor)
        if cursor == ROOT:
            break
        cursor = cursor.parent

    for directory in scan:
        document = directory / "README.md"
        if not document.exists():
            continue
        text = clean_for_ordering(document.read_text(encoding="utf-8"))
        for match in MARKDOWN_LINK.finditer(text):
            target = local_link_target(document, match.group("target"))
            if target is None:
                continue
            for child in children:
                try:
                    target.relative_to(child.resolve())
                except ValueError:
                    continue
                if child not in ordered:
                    ordered.append(child)
                break
    return ordered


def ordered_children(parent: Path) -> list[Path]:
    children = topic_children(parent)
    if not children:
        return []
    by_name = {unnumbered(child.name): child for child in children}
    ordered: list[Path] = []

    # Existing contiguous prefixes are the durable reviewed order. Manual
    # branches remain authoritative because they correct older alphabetical
    # layouts and establish their prerequisite-first sequence.
    if canonical_key(parent) not in MANUAL_CHILD_ORDER:
        prefixes = [
            int(child.name.split("-", 1)[0])
            for child in children
            if NUMBER_PREFIX.match(child.name)
        ]
        if len(prefixes) == len(children) and sorted(prefixes) == list(range(1, len(children) + 1)):
            return sorted(children, key=numeric_key)

    for name in MANUAL_CHILD_ORDER.get(canonical_key(parent), []):
        child = by_name.get(name)
        if child is not None and child not in ordered:
            ordered.append(child)

    for child in linked_child_order(parent, children):
        if child not in ordered:
            ordered.append(child)

    # New topics with no curated link are appended deterministically. Once the
    # root tree is reviewed, their numeric prefix becomes the durable order.
    ordered.extend(
        sorted(
            (child for child in children if child not in ordered),
            key=lambda child: unnumbered(child.name),
        )
    )
    return ordered


def build_directory_map() -> dict[Path, Path]:
    """Map current absolute topic directories to final root-relative paths."""
    mapping: dict[Path, Path] = {}

    def visit(parent: Path, final_parent: Path) -> None:
        for index, child in enumerate(ordered_children(parent), start=1):
            final = final_parent / f"{index:02d}-{unnumbered(child.name)}"
            mapping[child.resolve()] = final
            visit(child, final)

    for index, topic in enumerate(top_level_topics()):
        final = Path(f"{index:02d}-{unnumbered(topic.name)}")
        mapping[topic.resolve()] = final
        visit(topic, final)
    return mapping


def mapped_path(path: Path, directory_map: dict[Path, Path]) -> Path:
    absolute = path.resolve()
    candidates = [
        directory
        for directory in directory_map
        if absolute == directory or directory in absolute.parents
    ]
    if not candidates:
        return absolute
    base = max(candidates, key=lambda item: len(item.parts))
    return ROOT / directory_map[base] / absolute.relative_to(base)


def rewrite_markdown_links(directory_map: dict[Path, Path]) -> int:
    changed = 0
    for document in sorted(ROOT.rglob("*.md")):
        if ".git" in document.parts:
            continue
        original = document.read_text(encoding="utf-8")
        future_document = mapped_path(document, directory_map)

        def replace(match: re.Match[str]) -> str:
            raw = match.group("target")
            target = local_link_target(document, raw)
            if target is None or not target.exists():
                return match.group(0)
            try:
                target.relative_to(ROOT)
            except ValueError:
                return match.group(0)

            future_target = mapped_path(target, directory_map)
            relative = Path(
                os.path.relpath(future_target, start=future_document.parent)
            ).as_posix()
            fragment = ""
            plain = raw.strip()
            if "#" in plain:
                fragment = "#" + plain.split("#", 1)[1]
            elif "?" in plain:
                fragment = "?" + plain.split("?", 1)[1]
            return f"{match.group('open')}{relative}{fragment}{match.group('close')}"

        updated = MARKDOWN_LINK.sub(replace, original)
        if updated != original:
            document.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def flatten_service_indexes() -> tuple[int, int]:
    """Remove duplicate `services` index topics while retaining real leaves."""
    service_directories = sorted(
        [
            directory
            for directory in ROOT.rglob("*")
            if directory.is_dir()
            and unnumbered(directory.name) == "services"
            and is_topic(directory)
            and topic_children(directory)
        ],
        key=lambda item: len(item.parts),
        reverse=True,
    )
    if not service_directories:
        return 0, 0

    flatten_map: dict[Path, Path] = {}
    for services in service_directories:
        parent_relative = services.parent.relative_to(ROOT)
        flatten_map[services.resolve()] = parent_relative
        for child in topic_children(services):
            flatten_map[child.resolve()] = parent_relative / unnumbered(child.name)

    rewritten = rewrite_markdown_links(flatten_map)
    moved = 0
    for services in service_directories:
        parent = services.parent
        for child in topic_children(services):
            destination = parent / unnumbered(child.name)
            if destination.exists():
                raise RuntimeError(f"cannot flatten {child}: {destination} already exists")
            child.rename(destination)
            moved += 1
        for filename in ("README.md", "questions-and-answers.md"):
            (services / filename).unlink()
        if any(services.iterdir()):
            leftovers = ", ".join(path.name for path in services.iterdir())
            raise RuntimeError(f"unexpected files in duplicate index {services}: {leftovers}")
        services.rmdir()
    return moved, rewritten


def rename_topic_directories(directory_map: dict[Path, Path]) -> int:
    changed = 0
    for source in sorted(directory_map, key=lambda item: len(item.parts), reverse=True):
        destination = source.parent / directory_map[source].name
        if source == destination:
            continue
        if destination.exists():
            raise RuntimeError(f"cannot rename {source}: {destination} already exists")
        source.rename(destination)
        changed += 1
    return changed


def numeric_key(path: Path) -> tuple[int, str]:
    prefix, _, rest = path.name.partition("-")
    return (int(prefix), rest)


def numbered_topic_roots() -> list[Path]:
    return sorted(
        [path for path in ROOT.iterdir() if path.is_dir() and is_topic(path)],
        key=numeric_key,
    )


def numbered_children(directory: Path) -> list[Path]:
    return sorted(topic_children(directory), key=numeric_key)


def reading_sequence() -> list[Path]:
    result: list[Path] = []

    def visit(directory: Path) -> None:
        result.append(directory)
        for child in numbered_children(directory):
            visit(child)

    for topic in numbered_topic_roots():
        visit(topic)
    return result


def title(document: Path) -> str:
    for line in document.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return unnumbered(document.parent.name).replace("-", " ").title()


def relative_link(source: Path, target: Path, label: str) -> str:
    path = Path(os.path.relpath(target, start=source.parent)).as_posix()
    return f"[{label}]({path})"


def navigation_footer(parts: list[str]) -> str:
    return (
        "<!-- reading-navigation:start -->\n"
        "---\n\n"
        "**Reading path:** "
        + " · ".join(parts)
        + "\n\n<!-- reading-navigation:end -->"
    )


def without_generated_blocks(text: str) -> str:
    text = READING_NAV.sub("\n", OLD_TOC.sub("\n", text))
    text = GENERATED_LOCAL_INDEX.sub("\n", text)
    return LOCAL_SERVICE_INDEX.sub("\n", text).rstrip()


def write_chapter_guides(sequence: list[Path]) -> int:
    changed = 0
    root_readme = ROOT / "README.md"
    total = len(sequence)
    for index, directory in enumerate(sequence):
        readme = directory / "README.md"
        previous = root_readme if index == 0 else sequence[index - 1] / "README.md"
        next_readme = sequence[index + 1] / "README.md" if index + 1 < total else None
        previous_label = "the handbook contents" if index == 0 else title(previous)
        next_label = "the end of the handbook" if next_readme is None else title(next_readme)
        guide = (
            "<!-- chapter-guide:start -->\n"
            f"> **Step {index + 1:03d} of {total:03d} — {breadcrumb(directory)}**\n>\n"
            f"> **Builds on:** {relative_link(readme, previous, previous_label)}\n>\n"
            f"> **Now:** Learn **{title(readme)}** from its mental model through production ownership.\n>\n"
            + (
                "> **Then:** Rehearse the linked questions; this is the final chapter.\n"
                if next_readme is None
                else f"> **Then:** Rehearse the linked questions and continue to {relative_link(readme, next_readme, next_label)}.\n"
            )
            + "<!-- chapter-guide:end -->"
        )
        old = readme.read_text(encoding="utf-8")
        clean = CHAPTER_GUIDE.sub("\n", old)
        heading = re.search(r"^# .+\n", clean)
        if heading is None:
            raise RuntimeError(f"topic README has no title: {readme.relative_to(ROOT)}")
        new = clean[: heading.end()] + "\n" + guide + "\n\n" + clean[heading.end():].lstrip("\n")
        if new != old:
            readme.write_text(new, encoding="utf-8")
            changed += 1
    return changed


def plain_heading(value: str) -> str:
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    return value.strip()


def github_anchor(value: str) -> str:
    value = plain_heading(value).lower()
    value = re.sub(r"[^a-z0-9 _-]", "", value)
    value = re.sub(r"[ _]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def tokens(value: str) -> frozenset[str]:
    return frozenset(
        token.strip("./-")
        for token in WORD.findall(value.lower())
        if token.strip("./-") and token.strip("./-") not in STOP_WORDS
    )


def normalized_context(value: str) -> str:
    value = re.sub(r"[^a-z0-9/]+", " ", value.lower())
    return re.sub(r"\s+", " ", value).strip()


def sections_for(document: Path) -> list[StudySection]:
    text = CHAPTER_GUIDE.sub("\n", READING_NAV.sub("\n", document.read_text(encoding="utf-8")))
    matches = list(HEADING.finditer(text))
    seen_anchors: dict[str, int] = {}
    sections: list[StudySection] = []
    document_title = title(document)
    ignored = {
        "complete table of contents and reading sequence",
        "numbered study tree",
        "study support outside the numbered path",
    }
    for index, match in enumerate(matches):
        level = len(match.group(1))
        heading = plain_heading(match.group(2))
        if level == 1 or heading.lower() in ignored:
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end]
        base_anchor = github_anchor(heading)
        duplicate = seen_anchors.get(base_anchor, 0)
        seen_anchors[base_anchor] = duplicate + 1
        anchor = base_anchor if duplicate == 0 else f"{base_anchor}-{duplicate}"
        sections.append(
            StudySection(
                document=document,
                document_title=document_title,
                heading=heading,
                anchor=anchor,
                heading_tokens=tokens(heading),
                content_tokens=tokens(body),
            )
        )
    if not sections:
        sections.append(
            StudySection(
                document=document,
                document_title=document_title,
                heading=document_title,
                anchor=github_anchor(document_title),
                heading_tokens=tokens(document_title),
                content_tokens=tokens(text),
            )
        )
    return sections


def best_section(query: str, candidates: list[StudySection]) -> tuple[StudySection, int]:
    query_tokens = tokens(query)
    best = candidates[0]
    best_score = -1
    for candidate in candidates:
        heading_overlap = len(query_tokens & candidate.heading_tokens)
        content_overlap = len(query_tokens & candidate.content_tokens)
        phrase_bonus = 0
        heading_lower = candidate.heading.lower()
        for token in query_tokens:
            if len(token) >= 5 and token in heading_lower:
                phrase_bonus += 2
        score = heading_overlap * 5 + content_overlap * 2 + phrase_bonus
        if score > best_score:
            best = candidate
            best_score = score
    return best, best_score


def add_question_coverage_links(sequence: list[Path]) -> tuple[int, int, int]:
    """Link every checkbox question to the most relevant documented section."""
    sections_by_directory = {
        directory: sections_for(directory / "README.md") for directory in sequence
    }
    directories_by_key = {canonical_key(directory): directory for directory in sequence}
    all_sections = [section for directory in sequence for section in sections_by_directory[directory]]
    changed = 0
    linked = 0
    low_confidence = 0

    directories_by_depth = sorted(sequence, key=lambda item: len(item.parts), reverse=True)

    def owner_for(qna: Path) -> Path | None:
        for directory in directories_by_depth:
            if qna.parent == directory:
                return directory
        return None

    qna_files = [ROOT / "questions-and-answers.md"] + [
        directory / "questions-and-answers.md" for directory in sequence
    ]
    qna_files.extend(
        document
        for directory in sequence
        for document in extra_study_pages(directory)
        if QUESTION_LINE.search(document.read_text(encoding="utf-8"))
    )
    for qna in qna_files:
        owner = owner_for(qna)
        if owner is None or qna.name != "questions-and-answers.md":
            candidates = all_sections
        else:
            candidates = [
                section
                for directory in sequence
                if directory == owner or owner in directory.parents
                for section in sections_by_directory[directory]
            ]
        old = qna.read_text(encoding="utf-8")
        clean = REVIEW_LINE.sub("", old)
        current_context = ""
        scenario_positions: dict[str, int] = {}
        out: list[str] = []
        for line in clean.splitlines():
            if line.startswith(("# ", "## ")):
                current_context = plain_heading(line.lstrip("# "))
            out.append(line)
            match = QUESTION_LINE.match(line)
            if match is None:
                continue
            query = (
                match.group(1)
                if qna.name != "questions-and-answers.md"
                else f"{current_context} {match.group(1)}"
            )
            question_candidates = candidates
            if qna.name != "questions-and-answers.md":
                context_key = normalized_context(current_context)
                position = scenario_positions.get(context_key, 0)
                scenario_positions[context_key] = position + 1
                targets = SCENARIO_TARGETS.get(context_key, [])
                if position < len(targets):
                    target_key = targets[position]
                    target_directory = directories_by_key.get(target_key)
                    if target_directory is None:
                        raise RuntimeError(
                            f"scenario target does not exist: {context_key} -> {target_key}"
                        )
                    question_candidates = sections_by_directory[target_directory]
                else:
                    root_keys = SCENARIO_CONTEXT_ROOTS.get(context_key, [])
                    roots = [directories_by_key[key] for key in root_keys if key in directories_by_key]
                    scoped = [
                        section
                        for directory in sequence
                        if any(directory == root or root in directory.parents for root in roots)
                        for section in sections_by_directory[directory]
                    ]
                    if scoped:
                        question_candidates = scoped
            section, score = best_section(query, question_candidates)
            destination = Path(
                os.path.relpath(section.document, start=qna.parent)
            ).as_posix()
            label = f"{section.document_title} — {section.heading}"
            out.append(f"> **Covered in:** [{label}]({destination}#{section.anchor})")
            linked += 1
            if score <= 1:
                low_confidence += 1
        new = "\n".join(out).rstrip() + "\n"
        if new != old:
            qna.write_text(new, encoding="utf-8")
            changed += 1
    return changed, linked, low_confidence


def write_navigation(sequence: list[Path]) -> int:
    changed = 0
    root_readme = ROOT / "README.md"

    for index, directory in enumerate(sequence):
        readme = directory / "README.md"
        qna = directory / "questions-and-answers.md"
        previous = root_readme if index == 0 else sequence[index - 1] / "README.md"
        next_readme = sequence[index + 1] / "README.md" if index + 1 < len(sequence) else None

        readme_parts = [
            relative_link(
                readme,
                previous,
                "← Back: Contents" if index == 0 else f"← Back: {title(previous)}",
            ),
            relative_link(readme, qna, "Questions"),
        ]
        if next_readme is None:
            readme_parts.append("**End of handbook ✓**")
        else:
            readme_parts.append(relative_link(readme, next_readme, f"Next: {title(next_readme)} →"))

        old = readme.read_text(encoding="utf-8")
        new = without_generated_blocks(old) + "\n\n" + navigation_footer(readme_parts) + "\n"
        if new != old:
            readme.write_text(new, encoding="utf-8")
            changed += 1

        qna_parts = [
            relative_link(
                qna,
                previous,
                "← Back: Contents" if index == 0 else f"← Back: {title(previous)}",
            ),
            relative_link(qna, readme, "Study note"),
        ]
        if next_readme is None:
            qna_parts.append("**End of handbook ✓**")
        else:
            qna_parts.append(relative_link(qna, next_readme, f"Next: {title(next_readme)} →"))

        old = qna.read_text(encoding="utf-8")
        new = without_generated_blocks(old) + "\n\n" + navigation_footer(qna_parts) + "\n"
        if new != old:
            qna.write_text(new, encoding="utf-8")
            changed += 1

    first = sequence[0] / "README.md"
    root_parts = [
        "**Start here**",
        relative_link(root_readme, ROOT / "questions-and-answers.md", "Questions"),
        relative_link(root_readme, first, f"Begin: {title(first)} →"),
    ]
    old = root_readme.read_text(encoding="utf-8")
    new = without_generated_blocks(old) + "\n\n" + navigation_footer(root_parts) + "\n"
    if new != old:
        root_readme.write_text(new, encoding="utf-8")
        changed += 1

    root_qna = ROOT / "questions-and-answers.md"
    root_qna_parts = [
        relative_link(root_qna, root_readme, "← Contents"),
        relative_link(root_qna, first, f"Begin: {title(first)} →"),
    ]
    old = root_qna.read_text(encoding="utf-8")
    new = without_generated_blocks(old) + "\n\n" + navigation_footer(root_qna_parts) + "\n"
    if new != old:
        root_qna.write_text(new, encoding="utf-8")
        changed += 1

    return changed


def breadcrumb(directory: Path) -> str:
    return ".".join(part.split("-", 1)[0] for part in directory.relative_to(ROOT).parts)


def extra_study_pages(directory: Path) -> list[Path]:
    return sorted(
        path
        for path in directory.glob("*.md")
        if path.name not in {"README.md", "questions-and-answers.md"}
    )


def render_complete_toc(sequence: list[Path]) -> str:
    step = {directory: index for index, directory in enumerate(sequence, start=1)}
    lines = [
        "<!-- complete-reading-path:start -->",
        "## Complete table of contents and reading sequence",
        "",
        f"Start at **Step 001** and follow each page's **Next** link through **Step {len(sequence):03d}**. "
        "Read a parent overview before its indented children. The **Questions** link is practice for that note and does not change your place in the main sequence.",
        "",
        f"**Start:** [Step 001 — {title(sequence[0] / 'README.md')}]({(sequence[0] / 'README.md').relative_to(ROOT).as_posix()})",
        "",
        f"**End:** Step {len(sequence):03d} — {title(sequence[-1] / 'README.md')}",
        "",
        "### Numbered study tree",
        "",
    ]

    def visit(directory: Path, depth: int) -> None:
        readme = directory / "README.md"
        qna = directory / "questions-and-answers.md"
        indent = "  " * depth
        lines.append(
            f"{indent}- **{step[directory]:03d}.** "
            f"[`{breadcrumb(directory)}` {title(readme)}]({readme.relative_to(ROOT).as_posix()}) "
            f"· [Questions]({qna.relative_to(ROOT).as_posix()})"
        )
        for extra in extra_study_pages(directory):
            lines.append(
                f"{indent}  - Supplement: [{title(extra)}]({extra.relative_to(ROOT).as_posix()})"
            )
        for child in numbered_children(directory):
            visit(child, depth + 1)

    for topic in numbered_topic_roots():
        visit(topic, 0)

    lines.extend(["", "### Study support outside the numbered path", ""])
    support_files = []
    for folder in ("curriculum", "sources", "study-plan"):
        support_files.extend(sorted((ROOT / folder).glob("*.md")))
    support_files.append(ROOT / "curriculum" / "master-curriculum.txt")
    for document in support_files:
        label = title(document) if document.suffix == ".md" else "Master curriculum baseline"
        lines.append(f"- [{label}]({document.relative_to(ROOT).as_posix()})")

    lines.extend(
        [
            "- [Root cross-domain questions and answers](questions-and-answers.md)",
            "",
            "<!-- complete-reading-path:end -->",
        ]
    )
    return "\n".join(lines)


def write_root_toc(sequence: list[Path]) -> bool:
    path = ROOT / "README.md"
    original = path.read_text(encoding="utf-8")
    block = render_complete_toc(sequence)
    if COMPLETE_TOC.search(original):
        text = COMPLETE_TOC.sub("\n" + block + "\n", original)
    else:
        text = OLD_TOC.sub("\n", original)
        old_master = re.compile(
            r"\n## Master table of contents\n.*?(?=\n## Interview answer contracts\n)",
            re.S,
        )
        if old_master.search(text):
            text = old_master.sub("\n\n" + block + "\n", text)
        else:
            anchor = "\n## Interview answer contracts\n"
            if anchor not in text:
                raise RuntimeError("could not locate root README insertion point")
            text = text.replace(anchor, "\n\n" + block + "\n" + anchor, 1)

    text = text.replace(
        "This README is the main table of contents. Start with P0 material, practise the scenario bank aloud, then fill gaps using P1 and P2 material.",
        "This README is the only table of contents. Follow the numbered reading sequence from start to finish, and use each topic's question bank after studying its note.",
    )
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def write_auxiliary_navigation(sequence: list[Path]) -> int:
    """Give supplemental study pages a route back into their owning sequence."""
    changed = 0
    positions = {directory: index for index, directory in enumerate(sequence)}
    for directory in sequence:
        extras = extra_study_pages(directory)
        if not extras:
            continue
        index = positions[directory]
        next_readme = sequence[index + 1] / "README.md" if index + 1 < len(sequence) else None
        for document in extras:
            parts = [
                relative_link(document, directory / "README.md", "← Back: Topic note"),
                relative_link(document, directory / "questions-and-answers.md", "Questions"),
            ]
            if next_readme is None:
                parts.append("**End of handbook ✓**")
            else:
                parts.append(relative_link(document, next_readme, f"Next: {title(next_readme)} →"))
            old = document.read_text(encoding="utf-8")
            new = without_generated_blocks(old) + "\n\n" + navigation_footer(parts) + "\n"
            if new != old:
                document.write_text(new, encoding="utf-8")
                changed += 1
    return changed


def main() -> None:
    flattened_leaves, flatten_rewrites = flatten_service_indexes()
    directory_map = build_directory_map()
    paths_will_change = any(
        source.relative_to(ROOT) != destination
        for source, destination in directory_map.items()
    )
    rewritten = flatten_rewrites
    if paths_will_change:
        rewritten += rewrite_markdown_links(directory_map)
    renamed = rename_topic_directories(directory_map)
    sequence = reading_sequence()
    toc_changed = int(write_root_toc(sequence))
    chapter_guides_changed = write_chapter_guides(sequence)
    navigation_changed = write_navigation(sequence)
    auxiliary_changed = write_auxiliary_navigation(sequence)
    coverage_changed, coverage_links, low_confidence = add_question_coverage_links(sequence)
    print(f"topic_pages={len(sequence)}")
    print(f"service_leaves_moved={flattened_leaves}")
    print(f"renamed_directories={renamed}")
    print(f"markdown_files_with_rewritten_links={rewritten}")
    print(f"root_toc_changed={toc_changed}")
    print(f"chapter_guides_changed={chapter_guides_changed}")
    print(f"pages_with_navigation_changes={navigation_changed + auxiliary_changed}")
    print(f"question_banks_with_coverage_changes={coverage_changed}")
    print(f"question_coverage_links={coverage_links}")
    print(f"low_confidence_coverage_links={low_confidence}")


if __name__ == "__main__":
    main()
