#!/usr/bin/env python3
"""Insert a child-topic table of contents into every parent README."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
START = "<!-- child-topic-toc:start -->"
END = "<!-- child-topic-toc:end -->"


def title(readme: Path) -> str:
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return readme.parent.name.replace("-", " ").title()


def update(directory: Path) -> bool:
    readme = directory / "README.md"
    if not readme.exists():
        return False
    children = sorted(
        child for child in directory.iterdir()
        if child.is_dir() and not child.name.startswith(".") and (child / "README.md").exists()
    )
    text = readme.read_text(encoding="utf-8")
    text = re.sub(rf"\n?{re.escape(START)}.*?{re.escape(END)}\n?", "\n", text, flags=re.S)
    if not children:
        readme.write_text(text.rstrip() + "\n", encoding="utf-8")
        return False

    rows = []
    for child in children:
        label = title(child / "README.md")
        qna = child / "questions-and-answers.md"
        links = f"[{label}]({child.name}/README.md)"
        if qna.exists():
            links += f" — [questions and answers]({child.name}/questions-and-answers.md)"
        rows.append(f"- {links}")

    block = (
        f"{START}\n"
        "## Table of contents and deeper notes\n\n"
        "This parent note explains how the child topics work together. Follow each child link for the deeper mechanism, real commands/configuration, hands-on practice, authoritative documentation, and its local interview bank.\n\n"
        + "\n".join(rows)
        + f"\n{END}\n"
    )
    match = re.search(r"^# .+\n", text)
    if match:
        text = text[: match.end()] + "\n" + block + text[match.end():].lstrip("\n")
    else:
        text = block + "\n" + text
    readme.write_text(text.rstrip() + "\n", encoding="utf-8")
    return True


def main() -> None:
    count = 0
    directories = [ROOT] + sorted(path for path in ROOT.rglob("*") if path.is_dir())
    for directory in directories:
        if any(part.startswith(".") for part in directory.relative_to(ROOT).parts):
            continue
        count += int(update(directory))
    print(f"updated child-topic tables of contents in {count} parent READMEs")


if __name__ == "__main__":
    main()
