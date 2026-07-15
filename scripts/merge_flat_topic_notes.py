#!/usr/bin/env python3
"""Migrate early flat study notes into the canonical topic README files."""

from pathlib import Path
import re

from generate_leaf_library import numbered_path


ROOT = Path(__file__).resolve().parents[1]
MAPPINGS = {
    "06-kubernetes/gpu-platform.md": "06-kubernetes/gpu-llmops/README.md",
    "07-aws/ai-platform.md": "07-aws/ai-platform/README.md",
    "07-aws/block-file-backup.md": "07-aws/storage/README.md",
    "07-aws/containers.md": "07-aws/containers/README.md",
    "07-aws/data-messaging-serverless.md": "07-aws/messaging-serverless/README.md",
    "07-aws/ec2-auto-scaling.md": "07-aws/compute/README.md",
    "07-aws/elastic-load-balancing.md": "07-aws/load-balancing/README.md",
    "07-aws/foundations-iam-governance.md": "07-aws/foundations/README.md",
    "07-aws/infrastructure-delivery.md": "07-aws/infrastructure-delivery/README.md",
    "07-aws/s3.md": "07-aws/storage/services/s3/README.md",
    "07-aws/security-observability-operations.md": "07-aws/security-operations/README.md",
    "07-aws/vpc-networking.md": "07-aws/networking/README.md",
    "08-gcp/vertex-ai-platform.md": "08-gcp/vertex-ai-and-gcp-ai-platform/README.md",
    "09-iac-delivery/cicd.md": "09-iac-delivery/ci-cd/README.md",
    "09-iac-delivery/terraform.md": "09-iac-delivery/terraform/README.md",
    "10-operations/observability.md": "10-operations/observability/README.md",
    "10-operations/security.md": "10-operations/platform-and-cloud-security/README.md",
    "10-operations/sre-reliability.md": "10-operations/sre-and-reliability-engineering/README.md",
    "11-ai-platform/fundamentals-and-gpu.md": "11-ai-platform/gpu-compute-architecture/README.md",
    "11-ai-platform/llm-gateway.md": "11-ai-platform/llm-gateway/README.md",
    "11-ai-platform/model-serving.md": "11-ai-platform/model-serving-and-inference-platforms/README.md",
}


def strip_title(text: str) -> str:
    return re.sub(r"^#\s+[^\n]+\n+", "", text, count=1).lstrip()


def main() -> None:
    merged = 0
    for source_name, target_name in MAPPINGS.items():
        source = ROOT / source_name
        target = numbered_path(ROOT / target_name)
        if not source.exists():
            continue
        source_text = source.read_text(encoding="utf-8")
        target_text = target.read_text(encoding="utf-8").rstrip()
        marker = source_name.upper().replace("/", "-").replace(".", "-")
        start = f"<!-- merged-{marker}:start -->"
        end = f"<!-- merged-{marker}:end -->"
        target_text = re.sub(rf"\n?{re.escape(start)}.*?{re.escape(end)}\n?", "\n", target_text, flags=re.S).rstrip()
        addition = (
            f"\n\n{start}\n"
            f"## Practical deep dive\n\n"
            f"{strip_title(source_text)}\n"
            f"{end}\n"
        )
        target.write_text(target_text + addition, encoding="utf-8")
        source.unlink()
        merged += 1
    print(f"merged {merged} flat topic notes into canonical READMEs")


if __name__ == "__main__":
    main()
