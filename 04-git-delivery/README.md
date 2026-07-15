# Git and software-delivery fundamentals

<!-- chapter-guide:start -->
> **Step 041 of 373 — 04**
>
> **Builds on:** [Network troubleshooting](../03-networking/12-network-troubleshooting/README.md)
>
> **Now:** Learn **Git and software-delivery fundamentals** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Git object model](01-git-object-model/README.md).
<!-- chapter-guide:end -->

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

Production ownership includes failure recovery, reliability, observability and cost: preserve reflogs and immutable release evidence, measure pipeline and review latency, make rollback versus revert explicit, and avoid repository or CI designs whose storage and runner cost grows without ownership.

## Read further

- [Git reference documentation](https://git-scm.com/docs) — authoritative command and behavior reference; use the child chapters to connect individual commands to safe collaboration and delivery workflows.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Network troubleshooting](../03-networking/12-network-troubleshooting/README.md) · [Questions](questions-and-answers.md) · [Next: Git object model →](01-git-object-model/README.md)

<!-- reading-navigation:end -->
