#!/usr/bin/env python3
"""Wrap the hand-authored branch notes in Explanation and Practice sessions.

Generated leaves get this structure from their generators.  The sixteen
hand-authored topic READMEs need a one-time, deterministic normalization while
the root README remains the repository's table of contents.
"""

from __future__ import annotations

from pathlib import Path
import re

from note_explanations import flow_diagram, history_text, junior_intro, practice_session


ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- explanation-practice-normalizer:v1 -->"

PURPOSES = {
    "00-role-ownership/README.md": "Role ownership connects technical decisions, delivery, support and communication to one accountable outcome over the service lifecycle.",
    "01-foundations/README.md": "The foundations branch explains the computing, concurrency, distributed-state, resilience and API mechanisms on which the later platform chapters depend.",
    "02-linux/README.md": "The Linux branch explains how processes use kernel-managed CPU, memory, files, devices, identity and networking and how those layers produce application symptoms.",
    "03-networking/README.md": "The networking branch explains the complete path from a name and application request through packets, routes, policy, transport, TLS and the remote response.",
    "04-git-delivery/README.md": "The Git delivery branch explains how content becomes commits and refs, how histories integrate, and how reviewed revisions become trustworthy releases.",
    "05-containers/README.md": "The containers branch explains how images, runtime configuration and Linux isolation create a portable process environment and where that boundary can fail.",
    "06-kubernetes/README.md": "The Kubernetes branch explains the API, reconciliation, scheduling, node, networking, storage and policy loops that turn desired objects into running workloads.",
    "07-aws/README.md": "The AWS branch connects identity, regional and global control planes, workload data paths, managed-state guarantees and cost into one cloud operating model.",
    "08-gcp/README.md": "The GCP branch connects resource hierarchy and IAM to global networking, managed compute, data, messaging, operations and AI service behavior.",
    "09-iac-delivery/README.md": "The infrastructure-delivery branch explains how source configuration, dependency graphs, state, plans, artifacts and promotion produce reviewed runtime changes.",
    "09-iac-delivery/03-ci-cd/03-github-actions/README.md": "GitHub Actions is a repository-integrated workflow engine in which events create workflow runs, jobs execute on runners and permissions govern access to code, secrets and deployment targets.",
    "09-iac-delivery/03-ci-cd/09-circleci/README.md": "CircleCI is a pipeline and workflow engine that evaluates versioned configuration, schedules jobs on selected executors and moves caches, workspaces, artifacts and approvals through a delivery graph.",
    "10-operations/README.md": "The operations branch connects telemetry and service objectives to incident response, recovery, security controls and durable prevention.",
    "11-ai-platform/README.md": "The AI platform branch connects data, training, model artifacts, GPU capacity, serving, evaluation, gateways, retrieval, safety and governance into one release lifecycle.",
    "12-platform-engineering/README.md": "The platform-engineering branch explains how an internal product converts developer intent into governed self-service capabilities with lifecycle ownership and feedback.",
    "13-scenarios/README.md": "The scenarios branch combines mechanisms from the handbook into realistic diagnosis, migration and design cases where evidence is incomplete and trade-offs matter.",
}

PRACTICE_START = re.compile(
    r"^## (?=(?:Practice|Practical|Real-world lab|Hands-on|\d+\. (?:Hands-on|Real-world labs)|How to practise))",
    re.M | re.I,
)
TRAILING_EXPLANATION = re.compile(
    r"^## (?=(?:Common interview traps|Interview traps|Revision summary|Read further|Further documentation|Documentation and videos))",
    re.M | re.I,
)
CHAPTER_GUIDE = re.compile(
    r"\n?<!-- chapter-guide:start -->.*?<!-- chapter-guide:end -->\n?",
    re.S,
)
READING_NAV = re.compile(
    r"\n?<!-- reading-navigation:start -->.*?<!-- reading-navigation:end -->\n?",
    re.S,
)


def demote_headings(text: str) -> str:
    return re.sub(r"^(#{2,5})(\s+)", lambda match: "#" + match.group(1) + match.group(2), text, flags=re.M)


def top_area(relative: str) -> str:
    return relative.split("/", 1)[0]


def normalize(relative: str, purpose: str) -> None:
    path = ROOT / relative
    original = path.read_text(encoding="utf-8")
    if MARKER in original:
        return

    title_line, _, rest = original.partition("\n")
    title = title_line.removeprefix("# ").strip()

    navigation_match = READING_NAV.search(rest)
    navigation = navigation_match.group(0).strip() if navigation_match else ""
    without_navigation = READING_NAV.sub("\n", rest).strip()

    guide_match = CHAPTER_GUIDE.search(without_navigation)
    guide = guide_match.group(0).strip() if guide_match else ""
    body = CHAPTER_GUIDE.sub("\n", without_navigation).strip()

    practice_match = PRACTICE_START.search(body)
    if practice_match:
        explanation_body = body[: practice_match.start()].strip()
        practice_body = body[practice_match.start() :].strip()
    else:
        explanation_body = body
        practice_body = ""

    trailing = ""
    trailing_match = TRAILING_EXPLANATION.search(practice_body)
    if trailing_match:
        trailing = practice_body[trailing_match.start() :].strip()
        practice_body = practice_body[: trailing_match.start()].strip()

    area = top_area(relative)
    explanation_parts = [
        "## Explanation",
        "",
        "### What this chapter is and why it exists",
        "",
        junior_intro(title, area, purpose, []),
        "",
        "### History and evolution",
        "",
        history_text(title, area, purpose),
        "",
        "### How the complete branch works",
        "",
        flow_diagram(title, area),
        "",
        "A branch overview connects child mechanisms into one lifecycle. The input crosses identity and policy, a control or decision plane, the runtime data path and its dependencies before producing a user-visible result. Status and telemetry travel back through the loop so operators and controllers can correct drift or failure. Reading the child chapters adds precision, but this overview explains why those chapters depend on one another.",
        "",
        "A useful test of understanding is to trace one concrete request or change from origin to outcome and name the authoritative state at each boundary. That trace reveals where work is synchronous or asynchronous, which failure domains are independent, what a timeout can prove, and which evidence distinguishes accepted intent from healthy behavior.",
    ]
    if explanation_body:
        explanation_parts.extend(["", demote_headings(explanation_body)])
    if trailing:
        explanation_parts.extend(["", demote_headings(trailing)])

    practice_parts = ["## Practice", ""]
    if practice_body:
        practice_parts.extend([demote_headings(practice_body), ""])
    practice_parts.append(practice_session(title, area))

    parts = [title_line, "", MARKER]
    if guide:
        parts.extend(["", guide])
    parts.extend(["", "\n".join(explanation_parts).strip(), "", "\n".join(practice_parts).strip()])
    if navigation:
        parts.extend(["", navigation])
    path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    for relative, purpose in PURPOSES.items():
        normalize(relative, purpose)
    print(f"normalized {len(PURPOSES)} hand-authored topic notes")


if __name__ == "__main__":
    main()
