#!/usr/bin/env python3
"""Validate handbook links, recursive folder contract and question counts."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
TOPIC_ROOTS = [
    ROOT / f"{number:02d}-{name}"
    for number, name in [
        (0, "role-ownership"), (1, "foundations"), (2, "linux"),
        (3, "networking"), (4, "git-delivery"), (5, "containers"),
        (6, "kubernetes"), (7, "aws"), (8, "gcp"),
        (9, "iac-delivery"), (10, "operations"), (11, "ai-platform"),
        (12, "platform-engineering"),
    ]
] + [ROOT / "scenarios"]

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
QUESTION = re.compile(r"^- \[[ xX]\].*\*\*Question:\*\*", re.M)
ANSWER = re.compile(r"^\*\*Answer:\*\*", re.M)
ID = re.compile(r"^###\s+\S+-(JN|JP|MN|MP|SN|SP)-(\d{2})\s*$", re.M)


def local_link_errors() -> list[str]:
    errors: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = raw.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "/")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (markdown.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"link escapes repository: {markdown.relative_to(ROOT)} -> {raw}")
                continue
            if not resolved.exists():
                errors.append(f"broken link: {markdown.relative_to(ROOT)} -> {raw}")
    return errors


def topic_contract_errors() -> list[str]:
    errors: list[str] = []
    for topic_root in TOPIC_ROOTS:
        if not topic_root.exists():
            errors.append(f"missing topic root: {topic_root.relative_to(ROOT)}")
            continue
        directories = [topic_root] + [p for p in topic_root.rglob("*") if p.is_dir()]
        for directory in directories:
            # A study directory participates in the contract when it has a
            # README or contains immediate study children with READMEs.
            readme = directory / "README.md"
            children = [p for p in directory.iterdir() if p.is_dir() and (p / "README.md").exists()]
            if not readme.exists() and children:
                errors.append(f"parent without README: {directory.relative_to(ROOT)}")
                continue
            if not readme.exists():
                continue
            qna = directory / "questions-and-answers.md"
            if not qna.exists():
                errors.append(f"topic without questions-and-answers.md: {directory.relative_to(ROOT)}")
            if children:
                content = readme.read_text(encoding="utf-8")
                if "<!-- child-topic-toc:start -->" not in content:
                    errors.append(f"parent missing child table of contents: {directory.relative_to(ROOT)}")
                for child in children:
                    if f"({child.name}/README.md)" not in content:
                        errors.append(f"parent does not link child: {directory.relative_to(ROOT)} -> {child.name}")
    duplicate_notes = sorted(ROOT.rglob("notes.md")) + sorted(ROOT.rglob("commands.md"))
    for duplicate in duplicate_notes:
        errors.append(f"separate note/command file violates README-as-note contract: {duplicate.relative_to(ROOT)}")
    return errors


def question_errors() -> tuple[list[str], int, int]:
    errors: list[str] = []
    total = 0
    files = 0
    for qna in ROOT.rglob("questions-and-answers.md"):
        files += 1
        text = qna.read_text(encoding="utf-8")
        questions = QUESTION.findall(text)
        answers = ANSWER.findall(text)
        total += len(questions)
        if len(questions) < 60:
            errors.append(f"fewer than 60 checkbox questions ({len(questions)}): {qna.relative_to(ROOT)}")
        if len(answers) < len(questions):
            errors.append(f"fewer answers ({len(answers)}) than questions ({len(questions)}): {qna.relative_to(ROOT)}")
        counts = Counter(kind for kind, _ in ID.findall(text))
        # Root mega bank concatenates multiple 60-question sections. All
        # ordinary banks still have at least ten of each kind.
        for kind in ("JN", "JP", "MN", "MP", "SN", "SP"):
            if counts[kind] < 10:
                errors.append(f"question bank has only {counts[kind]} {kind} entries: {qna.relative_to(ROOT)}")
    scenario = ROOT / "scenarios" / "120-cross-domain-scenarios.md"
    if not scenario.exists():
        errors.append("missing cross-domain scenario bank")
    else:
        scenario_count = len(QUESTION.findall(scenario.read_text(encoding="utf-8")))
        total += scenario_count
        if scenario_count <= 100:
            errors.append(f"cross-domain scenario bank must exceed 100; found {scenario_count}")
    return errors, files, total


def main() -> int:
    errors = local_link_errors()
    errors.extend(topic_contract_errors())
    question_problem, qna_files, total_questions = question_errors()
    errors.extend(question_problem)

    readmes = sum(1 for _ in ROOT.rglob("README.md"))
    markdown = sum(1 for _ in ROOT.rglob("*.md"))
    print(f"markdown_files={markdown}")
    print(f"readmes={readmes}")
    print(f"question_banks={qna_files}")
    print(f"checkbox_questions_including_scenarios={total_questions}")
    print(f"errors={len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
