#!/usr/bin/env python3
"""Map all 67 numbered curriculum branches to recursive notes and Q&A."""

from pathlib import Path
import re

from generate_curriculum_topics import AREA_BY_MAJOR, parse_curriculum, slug
from generate_leaf_library import numbered_path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "curriculum" / "coverage-matrix.md"


SPECIAL = {
    0: "00-role-ownership",
    1: "01-foundations",
    2: "02-linux",
    3: "03-networking",
    4: "04-git-delivery",
    5: "05-containers",
    6: "06-kubernetes",
    7: "06-kubernetes/gpu-llmops",
    8: "07-aws/foundations",
    9: "07-aws/networking",
    10: "07-aws/compute",
    11: "07-aws/load-balancing",
    12: "07-aws/storage",
    13: "07-aws/containers",
    14: "07-aws/databases",
    15: "07-aws/messaging-serverless",
    16: "07-aws/messaging-serverless",
    17: "07-aws/security-operations",
    18: "07-aws/security-operations",
    19: "07-aws/infrastructure-delivery",
    20: "07-aws/ai-platform",
}


def path_for(number: int, title: str) -> str:
    if number in SPECIAL:
        path = SPECIAL[number]
    else:
        area = AREA_BY_MAJOR[number]
        path = f"{area}/{slug(title)}"
    return numbered_path(ROOT / path).relative_to(ROOT).as_posix()


def main() -> None:
    rows = []
    for major in parse_curriculum():
        path = path_for(major.number, major.title)
        rows.append(
            f"| {major.number} | {major.priority or '—'} | {major.title} | "
            f"[README](../{path}/README.md) | [Q&A](../{path}/questions-and-answers.md) |"
        )
    content = """# Curriculum coverage matrix

Every numbered branch from the supplied master curriculum is preserved and mapped below. The linked README is the note; the separate bank contains at least 20 answered junior, 20 mid-level and 20 senior checkbox questions. Child tables of contents lead to deeper leaves.

| # | Priority | Supplied branch | Study note | Interview bank |
|---:|---|---|---|---|
""" + "\n".join(rows) + """

## Additive coverage beyond the supplied tree

- CircleCI and expanded GitHub Actions/Pulumi file anatomy live under [Infrastructure as Code and delivery](../09-iac-delivery/README.md).
- Twenty-six detailed MLOps/LLMOps operational leaves live under [MLOps and LLMOps lifecycle](../11-ai-platform/mlops-and-llmops-lifecycle/README.md).
- AWS has individual service folders under each branch's `services/` directory; Kubernetes has subsystem/service leaves and GPU/LLMOps topics.
- The [cross-domain bank](../13-scenarios/120-cross-domain-scenarios.md) contains 150 additional production procedures.

Run `python3 scripts/validate_content.py` from the repository root to verify local links, folder contracts, parent child tables and minimum question counts.
"""
    OUT.write_text(content, encoding="utf-8")
    print(f"generated coverage for {len(rows)} numbered branches")


if __name__ == "__main__":
    main()
