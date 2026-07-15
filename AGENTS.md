# Repository authoring contract

This repository is a practical interview-preparation handbook, not a glossary. Apply these rules to every new or edited topic at any folder depth.

## Folder contract

Every study topic or branch is a folder containing:

- `README.md` — the complete study note and local table of contents. Do not create a separate `notes.md` or command-reference file.
- `questions-and-answers.md` — the separate answered interview bank.

Parent folders also have their own README and question bank because parent questions may combine several child topics. Folder depth is unlimited when a concept benefits from a narrower practice unit.

## Required README learning flow

Teach from beginner mental model to senior production ownership. For each major concept, follow this sequence:

1. **Explain it:** define the concept, describe how it works, trace its lifecycle or request/data path, and distinguish it from nearby alternatives.
2. **Show it:** include a realistic command, configuration, manifest, IaC, API request, code sample, query, or log/metric example. Explain what important fields mean; do not give unexplained command dumps.
3. **Practise it:** give a safe hands-on exercise with prerequisites, setup, expected result, verification, at least one controlled failure or troubleshooting step, rollback/cleanup, and a harder extension. Prefer local, sandbox, free-tier, or disposable environments and clearly label commands that mutate state or incur cost.
4. **Read further:** link directly to current authoritative documentation, specifications, upstream projects, or primary research. Mark version-sensitive material and avoid relying on marketing summaries as the only source.

The note should also cover security, reliability/failure modes, observability, performance/scaling, cost, troubleshooting, production trade-offs, and common interview traps where they apply. Mermaid diagrams are preferred for request paths, lifecycles, dependencies, control/data planes, and failure domains.

## Examples and command safety

- Use real runnable examples with named placeholders such as `CLUSTER`, `REGION`, `ACCOUNT_ID`, `NAMESPACE`, and `RESOURCE`; define those placeholders before use.
- Start operational procedures with identity/context and read-only inspection. Explain healthy output, one failing output, and the next discriminating check.
- Separate reversible mitigation from the durable source-of-truth repair. Include user-facing verification and cleanup.
- Never embed real credentials, private endpoints, customer data, or unverified artifact digests. Do not imply that a destructive production command is safe merely because it is syntactically valid.
- For Kubernetes, include YAML and relevant `kubectl`/Helm/Kustomize commands. For IaC, include format, validate, test, preview/plan, apply/deploy, drift, import/refactor, and rollback examples. For Linux/networking, explain what evidence each command supplies. For AI platforms, include GPU/model/runtime compatibility, serving, evaluation, quality, safety, latency, tokens, capacity, and cost signals.

## Interview-bank contract

- Every question begins with `- [ ]` so the learner can change it to `- [x]` after rehearsal.
- Each topic has at least 20 answered junior, 20 answered mid-level, and 20 answered senior questions.
- At each level, split the bank into at least 10 normal/conceptual/code-review questions and 10 procedural/troubleshooting/implementation questions.
- Include command, configuration, code, architecture, failure, security, reliability, cost, and real-world questions where relevant.
- Answers must explain reasoning, mechanism, evidence, trade-offs, failure modes, and a concrete production example—not only give a definition.

## Completion checks

Before considering a topic complete, verify that local relative links resolve, README is the note, the separate Q&A bank meets its counts, examples are syntactically plausible, practice steps include verification and cleanup, and external links point to authoritative material. Preserve every item in `curriculum/master-curriculum.txt`; additions may extend it but must not remove its scope.
