# Question and answer standard

Each question-bearing leaf uses six banks. The minimum is ten questions per bank, giving **20 questions per level** and **60 total per leaf**:

| Level | Normal | Procedural | Minimum total |
|---|---:|---:|---:|
| Junior | 10 | 10 | 20 |
| Mid | 10 | 10 | 20 |
| Senior | 10 | 10 | 20 |

Question IDs use `JN`, `JP`, `MN`, `MP`, `SN`, and `SP`. For example, `AWS-S3-MP-04` is a mid-level procedural S3 question.

## Answer-quality rubric

A strong normal answer includes:

- a correct definition and mental model;
- the mechanism or lifecycle, not only a feature list;
- at least one use case and one constraint/failure mode;
- security, reliability, performance, observability, or cost implications where relevant;
- a concise production example.

A strong procedural answer includes:

- safety and blast-radius control before mutation;
- symptoms, impact, scope, recent changes, and an explicit hypothesis;
- a layer-by-layer inspection path with commands, queries, events, metrics, logs, or traces;
- reversible mitigation separated from root-cause repair;
- user-facing verification and rollback criteria;
- prevention: tests, guardrails, monitoring, ownership, and runbook changes.

A strong senior answer additionally includes:

- clarified functional and non-functional requirements;
- explicit assumptions and rough capacity/economic calculations;
- failure domains, trust boundaries, RPO/RTO and SLOs;
- at least two viable designs and why one wins under the stated constraints;
- migration, compatibility, rollout, rollback and organizational ownership;
- what evidence would cause the decision to be revisited.

## Scenario independence

Questions may intentionally ask beyond the preceding notes. Interviews test transfer, not recall. When the notes do not state a direct answer, derive one from the mental model and say what you would verify in current documentation.

