# Git and software-delivery fundamentals

<!-- child-topic-toc:start -->
## Table of contents and deeper notes

This parent note explains how the child topics work together. Follow each child link for the deeper mechanism, real commands/configuration, hands-on practice, authoritative documentation, and its local interview bank.

- [Branching](branching/README.md) — [questions and answers](branching/questions-and-answers.md)
- [Change integration](change-integration/README.md) — [questions and answers](change-integration/questions-and-answers.md)
- [Collaboration](collaboration/README.md) — [questions and answers](collaboration/questions-and-answers.md)
- [Git object model](git-object-model/README.md) — [questions and answers](git-object-model/questions-and-answers.md)
- [Git security](git-security/README.md) — [questions and answers](git-security/questions-and-answers.md)
- [Release management](release-management/README.md) — [questions and answers](release-management/questions-and-answers.md)
<!-- child-topic-toc:end -->
## Object and collaboration model

Git stores content-addressed blobs, trees and commits; refs point to commits; `HEAD` identifies the checked-out ref/commit; the index stages the next tree. A commit records snapshot, parents, author/committer and message. Understanding the graph makes merge/rebase/reset/revert predictable.

Merge preserves both histories with a merge commit when needed. Rebase copies commits onto a new base and rewrites IDs; avoid rewriting shared protected history. Cherry-pick copies selected changes. Revert adds an inverse commit and is the safe public-history undo. Reset moves a ref/index/worktree depending on mode and is dangerous on shared work. Use reflog for local recovery while entries remain.

Trunk-based development uses small changes and flags for integration speed; feature branches isolate review; GitFlow adds release branches and overhead. Choose from release cadence, compliance and team coordination. Branch protection, required checks/reviews, CODEOWNERS and merge queues encode governance but need emergency and stale-owner procedures.

## Releases and security

Semantic versions communicate compatibility only if the project defines/enforces its contract. Tags identify commits; release artifacts must be immutable and linked to commit, build, dependencies, SBOM, signature/provenance and tests. Promote the same artifact; do not rebuild production from a mutable branch. Changelogs emphasize user/operational impact and migration/rollback.

Sign commits/tags where identity assurance matters, protect signing keys and verify in automation. Use least-privilege repository/app/token permissions, SSO/MFA, protected environments, ephemeral CI identity, secret scanning with rotation, dependency updates and pinned actions/dependencies. A deleted secret is still compromised in history/logs/caches; revoke first, then rewrite history only with coordination.

## Safe workflows

```bash
git status --short
git log --graph --decorate --oneline --all
git diff; git diff --staged
git switch -c feature/name
git fetch --prune
git rebase origin/main       # only for an appropriate private branch
git revert COMMIT
git reflog
git show --show-signature TAG
```

Resolve conflicts by understanding both intentions and running tests, not choosing “ours/theirs” blindly. For incidents, map deployed artifact/digest back to commit and pipeline evidence. Hotfix the smallest safe change, preserve normal review where time allows, and merge the fix back to all maintained lines.

## Revision summary

- Git is a content-addressed commit graph plus movable refs.
- Rebase/reset rewrite/move history; revert records a safe public undo.
- Small integrated changes reduce merge and rollback risk.
- Releases bind source to immutable artifact and evidence.
- Rotate leaked secrets before repository history cleanup.

<!-- generated-topic-index:start -->
## Deep topic folders

- [4.1 Git object model](git-object-model/README.md) — [Q&A](git-object-model/questions-and-answers.md)
- [4.2 Branching](branching/README.md) — [Q&A](branching/questions-and-answers.md)
- [4.3 Change integration](change-integration/README.md) — [Q&A](change-integration/questions-and-answers.md)
- [4.4 Collaboration](collaboration/README.md) — [Q&A](collaboration/questions-and-answers.md)
- [4.5 Release management](release-management/README.md) — [Q&A](release-management/questions-and-answers.md)
- [4.6 Git security](git-security/README.md) — [Q&A](git-security/questions-and-answers.md)
<!-- generated-topic-index:end -->
