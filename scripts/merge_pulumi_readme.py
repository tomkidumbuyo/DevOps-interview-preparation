#!/usr/bin/env python3
"""One-time migration: merge the older flat Pulumi note into branch README."""

from pathlib import Path
import re

from generate_leaf_library import numbered_path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "09-iac-delivery" / "pulumi.md"
TARGET = numbered_path(ROOT / "09-iac-delivery" / "pulumi" / "README.md")
START = "<!-- merged-practical-pulumi-note:start -->"
END = "<!-- merged-practical-pulumi-note:end -->"


def main() -> None:
    if not SOURCE.exists():
        print("Pulumi flat note already merged")
        return
    target = TARGET.read_text(encoding="utf-8")
    target = re.sub(rf"\n?{re.escape(START)}.*?{re.escape(END)}\n?", "\n", target, flags=re.S).rstrip()
    source = SOURCE.read_text(encoding="utf-8")
    source = re.sub(r"^# Pulumi\s*", "", source, count=1)
    merged = (
        target
        + "\n\n"
        + START
        + "\n## Practical Pulumi deep dive\n\n"
        + source.lstrip()
        + "\n"
        + END
        + "\n"
    )
    TARGET.write_text(merged, encoding="utf-8")
    SOURCE.unlink()
    print("merged 09-iac-delivery/pulumi.md into pulumi/README.md")


if __name__ == "__main__":
    main()
