#!/usr/bin/env python3
"""Generate question banks for delivery topics added beyond the source tree."""

from pathlib import Path

from generate_leaf_library import C, Leaf, qna, write


ROOT = Path(__file__).resolve().parents[1]


CIRCLECI = Leaf("09-iac-delivery", "ci-cd", "circleci", "CircleCI", "Design secure CircleCI pipelines with reusable configuration, isolated executors, workflow gates, OIDC, caching, artifacts and operational evidence.", C(
    "Config file — `.circleci/config.yml` version 2.1 defines parameters, orbs, executors, commands, jobs and workflows",
    "Pipeline — one triggered config evaluation carries values and parameters into one or more workflows",
    "Workflow — orchestrates jobs with fan-out/fan-in, requires, filters, approvals, scheduling and serial groups",
    "Job — named steps execute in Docker, machine, macOS, Windows or self-hosted runner environment",
    "Step — checkout, run, cache, workspace, artifact and reusable command operations execute in order",
    "Executor/resource class — defines runtime image/VM and compute size; trust, compatibility and cost differ",
    "Reusable configuration — commands/executors/jobs and parameterized orbs reduce duplication but expand supply-chain trust",
    "Workspace/cache/artifact — workflow file transfer, dependency acceleration and retained evidence have distinct lifecycle/security",
    "Context and OIDC — protected environment variables or short-lived identity are attached to authorized workflow jobs",
    "Dynamic configuration — setup workflow and continuation generate a reviewed bounded second-stage config",
    "Approval and serial group — human decision and cross-pipeline mutual exclusion protect deployment targets",
    "Operations — validate, process, rerun, SSH-debug, Insights, audit and API evidence support troubleshooting",
), ("circleci config validate .circleci/config.yml", "circleci config process .circleci/config.yml", "circleci local execute --job test", "circleci config pack .circleci/src"), "https://circleci.com/docs/reference/configuration-reference/")


def main() -> None:
    path = ROOT / "09-iac-delivery" / "ci-cd" / "circleci"
    write(path / "questions-and-answers.md", qna(CIRCLECI))
    print("generated CircleCI 60-question bank")


if __name__ == "__main__":
    main()
