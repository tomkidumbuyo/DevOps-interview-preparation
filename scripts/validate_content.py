#!/usr/bin/env python3
"""Validate the numbered handbook, continuous navigation, links and Q&A banks."""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r"^(\d{2})-(.+)$")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
QUESTION = re.compile(r"^- \[[ xX]\].*\*\*Question:\*\*", re.M)
ANSWER = re.compile(r"^\*\*Answer:\*\*", re.M)
COVERED = re.compile(r"^> \*\*Covered in:\*\* \[[^\]]+\]\(([^)]+)\)$", re.M)
QUESTION_WITH_COVERAGE = re.compile(
    r"^- \[[ xX]\].*\*\*Question:\*\*.*\n> \*\*Covered in:\*\* ", re.M
)
ID = re.compile(r"^###\s+\S+-(JN|JP|MN|MP|SN|SP)-(\d{2})\s*$", re.M)
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)


def is_topic(directory: Path) -> bool:
    return (directory / "README.md").is_file() and (
        directory / "questions-and-answers.md"
    ).is_file()


def topic_roots() -> list[Path]:
    return sorted(
        [directory for directory in ROOT.iterdir() if directory.is_dir() and is_topic(directory)],
        key=lambda directory: int(NUMBERED.match(directory.name).group(1))
        if NUMBERED.match(directory.name)
        else 10_000,
    )


def topic_children(directory: Path) -> list[Path]:
    return sorted(
        [child for child in directory.iterdir() if child.is_dir() and is_topic(child)],
        key=lambda child: int(NUMBERED.match(child.name).group(1))
        if NUMBERED.match(child.name)
        else 10_000,
    )


def reading_sequence() -> list[Path]:
    result: list[Path] = []

    def visit(directory: Path) -> None:
        result.append(directory)
        for child in topic_children(directory):
            visit(child)

    for root in topic_roots():
        visit(root)
    return result


def link_target(document: Path, raw: str) -> tuple[Path | None, str]:
    value = raw.strip().strip("<>").split(maxsplit=1)[0]
    if not value or value.startswith(("http://", "https://", "mailto:")):
        return None, ""
    path_text, _, anchor = value.partition("#")
    path_text = unquote(path_text.split("?", 1)[0])
    if path_text.startswith("/"):
        return None, anchor
    target = document if not path_text else (document.parent / path_text).resolve()
    return target, anchor


def local_link_errors() -> list[str]:
    errors: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target, _ = link_target(markdown, raw)
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"link escapes repository: {markdown.relative_to(ROOT)} -> {raw}")
                continue
            if not target.exists():
                errors.append(f"broken link: {markdown.relative_to(ROOT)} -> {raw}")
    return errors


def plain_heading(value: str) -> str:
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    return value.strip()


def github_anchor(value: str) -> str:
    value = plain_heading(value).lower()
    value = re.sub(r"[^a-z0-9 _-]", "", value)
    value = re.sub(r"[ _]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


@lru_cache(maxsize=None)
def heading_anchors(document: Path) -> set[str]:
    anchors: set[str] = set()
    counts: Counter[str] = Counter()
    for heading in HEADING.findall(document.read_text(encoding="utf-8")):
        base = github_anchor(heading)
        suffix = counts[base]
        counts[base] += 1
        anchors.add(base if suffix == 0 else f"{base}-{suffix}")
    return anchors


def coverage_anchor_errors(question_file: Path) -> list[str]:
    errors: list[str] = []
    for raw in COVERED.findall(question_file.read_text(encoding="utf-8")):
        target, anchor = link_target(question_file, raw)
        if target is None or not target.exists():
            errors.append(f"coverage link has no document: {question_file.relative_to(ROOT)} -> {raw}")
            continue
        if not anchor:
            errors.append(f"coverage link has no heading anchor: {question_file.relative_to(ROOT)} -> {raw}")
            continue
        if target.suffix.lower() != ".md" or anchor not in heading_anchors(target):
            errors.append(f"coverage anchor not found: {question_file.relative_to(ROOT)} -> {raw}")
    return errors


def numbering_errors(sequence: list[Path]) -> list[str]:
    errors: list[str] = []
    roots = topic_roots()
    expected_roots = list(range(len(roots)))
    actual_roots = []
    for root in roots:
        match = NUMBERED.match(root.name)
        if not match:
            errors.append(f"unnumbered topic root: {root.relative_to(ROOT)}")
            continue
        actual_roots.append(int(match.group(1)))
    if actual_roots != expected_roots:
        errors.append(f"top-level numbering is not contiguous: {actual_roots}")

    for directory in sequence:
        children = topic_children(directory)
        actual = []
        for child in children:
            match = NUMBERED.match(child.name)
            if not match:
                errors.append(f"unnumbered child topic: {child.relative_to(ROOT)}")
                continue
            actual.append(int(match.group(1)))
            if match.group(2) == "services":
                errors.append(f"redundant services index topic: {child.relative_to(ROOT)}")
        expected = list(range(1, len(children) + 1))
        if actual != expected:
            errors.append(f"child numbering is not contiguous in {directory.relative_to(ROOT)}: {actual}")
    return errors


def navigation_errors(sequence: list[Path]) -> list[str]:
    errors: list[str] = []
    root_readme = ROOT / "README.md"
    root_text = root_readme.read_text(encoding="utf-8")
    toc_headings = []
    for readme in ROOT.rglob("README.md"):
        text = readme.read_text(encoding="utf-8")
        if re.search(r"^## .*table of contents", text, re.I | re.M):
            toc_headings.append(readme.relative_to(ROOT).as_posix())
        if readme != root_readme and any(
            marker in text
            for marker in ("child-topic-toc:start", "generated-topic-index:start")
        ):
            errors.append(f"local table-of-contents block remains: {readme.relative_to(ROOT)}")
    if toc_headings != ["README.md"]:
        errors.append(f"root must contain the only table of contents; found {toc_headings}")

    for index, directory in enumerate(sequence):
        readme = directory / "README.md"
        qna = directory / "questions-and-answers.md"
        readme_text = readme.read_text(encoding="utf-8")
        qna_text = qna.read_text(encoding="utf-8")
        if "<!-- chapter-guide:start -->" not in readme_text:
            errors.append(f"missing chapter guide: {readme.relative_to(ROOT)}")
        if "<!-- reading-navigation:start -->" not in readme_text:
            errors.append(f"missing README navigation: {readme.relative_to(ROOT)}")
        if "<!-- reading-navigation:start -->" not in qna_text:
            errors.append(f"missing question-bank navigation: {qna.relative_to(ROOT)}")

        expected_targets = [ROOT / "README.md" if index == 0 else sequence[index - 1] / "README.md", qna]
        if index + 1 < len(sequence):
            expected_targets.append(sequence[index + 1] / "README.md")
        resolved = {
            target
            for raw in LINK.findall(readme_text)
            for target, _ in [link_target(readme, raw)]
            if target is not None
        }
        for target in expected_targets:
            if target.resolve() not in resolved:
                errors.append(
                    f"navigation target missing: {readme.relative_to(ROOT)} -> {target.relative_to(ROOT)}"
                )

        rel_readme = readme.relative_to(ROOT).as_posix()
        rel_qna = qna.relative_to(ROOT).as_posix()
        if f"]({rel_readme})" not in root_text or f"]({rel_qna})" not in root_text:
            errors.append(f"root tree omits topic: {directory.relative_to(ROOT)}")

    if f"through **Step {len(sequence):03d}**" not in root_text:
        errors.append("root reading path has a stale final step count")
    return errors


def topic_contract_errors(sequence: list[Path]) -> list[str]:
    errors: list[str] = []
    for directory in sequence:
        readme = directory / "README.md"
        qna = directory / "questions-and-answers.md"
        if not readme.exists() or not qna.exists():
            errors.append(f"incomplete topic folder: {directory.relative_to(ROOT)}")
    duplicate_notes = sorted(ROOT.rglob("notes.md")) + sorted(ROOT.rglob("commands.md"))
    for duplicate in duplicate_notes:
        errors.append(f"separate note/command file violates README-as-note contract: {duplicate.relative_to(ROOT)}")
    return errors


def question_errors() -> tuple[list[str], int, int, int]:
    errors: list[str] = []
    total = 0
    files = 0
    coverage_links = 0
    for qna in ROOT.rglob("questions-and-answers.md"):
        files += 1
        text = qna.read_text(encoding="utf-8")
        questions = QUESTION.findall(text)
        answers = ANSWER.findall(text)
        covered = COVERED.findall(text)
        paired = QUESTION_WITH_COVERAGE.findall(text)
        total += len(questions)
        coverage_links += len(covered)
        if len(questions) < 60:
            errors.append(f"fewer than 60 checkbox questions ({len(questions)}): {qna.relative_to(ROOT)}")
        if len(answers) < len(questions):
            errors.append(f"fewer answers ({len(answers)}) than questions ({len(questions)}): {qna.relative_to(ROOT)}")
        if len(covered) != len(questions) or len(paired) != len(questions):
            errors.append(
                f"question coverage mismatch ({len(questions)} questions, {len(covered)} links, {len(paired)} adjacent): {qna.relative_to(ROOT)}"
            )
        errors.extend(coverage_anchor_errors(qna))
        counts = Counter(kind for kind, _ in ID.findall(text))
        for kind in ("JN", "JP", "MN", "MP", "SN", "SP"):
            if counts[kind] < 10:
                errors.append(f"question bank has only {counts[kind]} {kind} entries: {qna.relative_to(ROOT)}")

    scenario = ROOT / "13-scenarios" / "120-cross-domain-scenarios.md"
    if not scenario.exists():
        errors.append("missing cross-domain scenario bank")
    else:
        text = scenario.read_text(encoding="utf-8")
        scenario_count = len(QUESTION.findall(text))
        scenario_covered = len(COVERED.findall(text))
        total += scenario_count
        coverage_links += scenario_covered
        if scenario_count <= 100:
            errors.append(f"cross-domain scenario bank must exceed 100; found {scenario_count}")
        if scenario_covered != scenario_count or len(QUESTION_WITH_COVERAGE.findall(text)) != scenario_count:
            errors.append(
                f"cross-domain coverage mismatch ({scenario_count} questions, {scenario_covered} links)"
            )
        if "<!-- reading-navigation:start -->" not in text:
            errors.append("cross-domain scenario bank is missing reading navigation")
        errors.extend(coverage_anchor_errors(scenario))
    return errors, files, total, coverage_links


def main() -> int:
    sequence = reading_sequence()
    errors = local_link_errors()
    errors.extend(numbering_errors(sequence))
    errors.extend(navigation_errors(sequence))
    errors.extend(topic_contract_errors(sequence))
    question_problem, qna_files, total_questions, coverage_links = question_errors()
    errors.extend(question_problem)

    readmes = sum(1 for _ in ROOT.rglob("README.md"))
    markdown = sum(1 for _ in ROOT.rglob("*.md"))
    print(f"markdown_files={markdown}")
    print(f"topic_pages={len(sequence)}")
    print(f"readmes={readmes}")
    print(f"question_banks={qna_files}")
    print(f"checkbox_questions_including_scenarios={total_questions}")
    print(f"question_coverage_links={coverage_links}")
    print(f"errors={len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
