# Filesystems — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### FILESYSTEMS-JN-01

- [ ] **Question:** What is Linux directory structure, and why does it matter in Filesystems?
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FILESYSTEMS-JN-02

- [ ] **Question:** What is /etc, /var, /proc, /sys, /dev, /tmp, and why does it matter in Filesystems?
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FILESYSTEMS-JN-03

- [ ] **Question:** What is ext4, and why does it matter in Filesystems?
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FILESYSTEMS-JN-04

- [ ] **Question:** What is XFS, and why does it matter in Filesystems?
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FILESYSTEMS-JN-05

- [ ] **Question:** What is NFS, and why does it matter in Filesystems?
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FILESYSTEMS-JN-06

- [ ] **Question:** What is OverlayFS, and why does it matter in Filesystems?
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FILESYSTEMS-JN-07

- [ ] **Question:** What is Mounts, and why does it matter in Filesystems?
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### FILESYSTEMS-JN-08

- [ ] **Code:** **Question:** What does `ip route; ss -lntup; journalctl -b` help you verify for Filesystems?
> **Covered in:** [Filesystems — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### FILESYSTEMS-JN-09

- [ ] **Code:** **Question:** What does `uname -a; systemd-analyze` help you verify for Filesystems?
> **Covered in:** [Filesystems — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: store filesystem object metadata and block references while directories map names to inode numbers; inode exhaustion is separate from byte exhaustion.

### FILESYSTEMS-JN-10

- [ ] **Code:** **Question:** What does `ps -eo pid,ppid,state,pcpu,pmem,cmd` help you verify for Filesystems?
> **Covered in:** [Filesystems — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: add another directory name for the same inode and normally cannot cross filesystems; data remains until the final link/open reference disappears.

## Junior — procedural and command questions

### FILESYSTEMS-JP-01

- [ ] **Code:** **Question:** A basic Linux directory structure check fails. What would you do first using the CLI?
> **Covered in:** [Filesystems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `uname -a; systemd-analyze` and capture exact status/reason/request ID. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FILESYSTEMS-JP-02

- [ ] **Question:** A basic /etc, /var, /proc, /sys, /dev, /tmp check fails. What would you do first?
> **Covered in:** [Filesystems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ps -eo pid,ppid,state,pcpu,pmem,cmd` and capture exact status/reason/request ID. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FILESYSTEMS-JP-03

- [ ] **Question:** A basic ext4 check fails. What would you do first?
> **Covered in:** [Filesystems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `vmstat 1; iostat -xz 1` and capture exact status/reason/request ID. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FILESYSTEMS-JP-04

- [ ] **Code:** **Question:** A basic XFS check fails. What would you do first using the CLI?
> **Covered in:** [Filesystems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip route; ss -lntup; journalctl -b` and capture exact status/reason/request ID. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FILESYSTEMS-JP-05

- [ ] **Question:** A basic NFS check fails. What would you do first?
> **Covered in:** [Filesystems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `uname -a; systemd-analyze` and capture exact status/reason/request ID. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FILESYSTEMS-JP-06

- [ ] **Question:** A basic OverlayFS check fails. What would you do first?
> **Covered in:** [Filesystems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ps -eo pid,ppid,state,pcpu,pmem,cmd` and capture exact status/reason/request ID. presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FILESYSTEMS-JP-07

- [ ] **Code:** **Question:** A basic Mounts check fails. What would you do first using the CLI?
> **Covered in:** [Filesystems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `vmstat 1; iostat -xz 1` and capture exact status/reason/request ID. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FILESYSTEMS-JP-08

- [ ] **Question:** A basic Bind mounts check fails. What would you do first?
> **Covered in:** [Filesystems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ip route; ss -lntup; journalctl -b` and capture exact status/reason/request ID. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FILESYSTEMS-JP-09

- [ ] **Question:** A basic Inodes check fails. What would you do first?
> **Covered in:** [Filesystems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `uname -a; systemd-analyze` and capture exact status/reason/request ID. store filesystem object metadata and block references while directories map names to inode numbers; inode exhaustion is separate from byte exhaustion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### FILESYSTEMS-JP-10

- [ ] **Code:** **Question:** A basic Hard links check fails. What would you do first using the CLI?
> **Covered in:** [Filesystems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ps -eo pid,ppid,state,pcpu,pmem,cmd` and capture exact status/reason/request ID. add another directory name for the same inode and normally cannot cross filesystems; data remains until the final link/open reference disappears. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### FILESYSTEMS-MN-01

- [ ] **Question:** Compare Linux directory structure with /etc, /var, /proc, /sys, /dev, /tmp. When would each change your design?
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Linux directory structure: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. /etc, /var, /proc, /sys, /dev, /tmp: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FILESYSTEMS-MN-02

- [ ] **Question:** Compare /etc, /var, /proc, /sys, /dev, /tmp with ext4. When would each change your design?
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** /etc, /var, /proc, /sys, /dev, /tmp: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. ext4: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FILESYSTEMS-MN-03

- [ ] **Question:** Compare ext4 with XFS. When would each change your design?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** ext4: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. XFS: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FILESYSTEMS-MN-04

- [ ] **Configuration review:** **Question:** Compare XFS with NFS. When would each change your design?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** XFS: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. NFS: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FILESYSTEMS-MN-05

- [ ] **Question:** Compare NFS with OverlayFS. When would each change your design?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** NFS: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. OverlayFS: presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FILESYSTEMS-MN-06

- [ ] **Question:** Compare OverlayFS with Mounts. When would each change your design?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** OverlayFS: presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Mounts: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FILESYSTEMS-MN-07

- [ ] **Configuration review:** **Question:** Compare Mounts with Bind mounts. When would each change your design?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Mounts: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Bind mounts: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FILESYSTEMS-MN-08

- [ ] **Question:** Compare Bind mounts with Inodes. When would each change your design?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Bind mounts: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Inodes: store filesystem object metadata and block references while directories map names to inode numbers; inode exhaustion is separate from byte exhaustion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FILESYSTEMS-MN-09

- [ ] **Question:** Compare Inodes with Hard links. When would each change your design?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Inodes: store filesystem object metadata and block references while directories map names to inode numbers; inode exhaustion is separate from byte exhaustion. Hard links: add another directory name for the same inode and normally cannot cross filesystems; data remains until the final link/open reference disappears. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### FILESYSTEMS-MN-10

- [ ] **Configuration review:** **Question:** Compare Hard links with Linux directory structure. When would each change your design?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Hard links: add another directory name for the same inode and normally cannot cross filesystems; data remains until the final link/open reference disappears. Linux directory structure: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### FILESYSTEMS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Linux directory structure; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `uname -a; systemd-analyze` plus recent events/changes, then correlate the service-specific SLI. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FILESYSTEMS-MP-02

- [ ] **Question:** Production is degraded around /etc, /var, /proc, /sys, /dev, /tmp; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ps -eo pid,ppid,state,pcpu,pmem,cmd` plus recent events/changes, then correlate the service-specific SLI. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FILESYSTEMS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around ext4; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `vmstat 1; iostat -xz 1` plus recent events/changes, then correlate the service-specific SLI. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FILESYSTEMS-MP-04

- [ ] **Question:** Production is degraded around XFS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip route; ss -lntup; journalctl -b` plus recent events/changes, then correlate the service-specific SLI. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FILESYSTEMS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around NFS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `uname -a; systemd-analyze` plus recent events/changes, then correlate the service-specific SLI. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FILESYSTEMS-MP-06

- [ ] **Question:** Production is degraded around OverlayFS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ps -eo pid,ppid,state,pcpu,pmem,cmd` plus recent events/changes, then correlate the service-specific SLI. presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FILESYSTEMS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Mounts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `vmstat 1; iostat -xz 1` plus recent events/changes, then correlate the service-specific SLI. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FILESYSTEMS-MP-08

- [ ] **Question:** Production is degraded around Bind mounts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ip route; ss -lntup; journalctl -b` plus recent events/changes, then correlate the service-specific SLI. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FILESYSTEMS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Inodes; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `uname -a; systemd-analyze` plus recent events/changes, then correlate the service-specific SLI. store filesystem object metadata and block references while directories map names to inode numbers; inode exhaustion is separate from byte exhaustion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### FILESYSTEMS-MP-10

- [ ] **Question:** Production is degraded around Hard links; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ps -eo pid,ppid,state,pcpu,pmem,cmd` plus recent events/changes, then correlate the service-specific SLI. add another directory name for the same inode and normally cannot cross filesystems; data remains until the final link/open reference disappears. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### FILESYSTEMS-SN-01

- [ ] **Question:** Design a production Filesystems capability where Linux directory structure, XFS and Mounts are first-class requirements.
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FILESYSTEMS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Filesystems capability where /etc, /var, /proc, /sys, /dev, /tmp, NFS and Bind mounts are first-class requirements.
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FILESYSTEMS-SN-03

- [ ] **Question:** Design a production Filesystems capability where ext4, OverlayFS and Inodes are first-class requirements.
> **Covered in:** [Filesystems — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. store filesystem object metadata and block references while directories map names to inode numbers; inode exhaustion is separate from byte exhaustion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FILESYSTEMS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Filesystems capability where XFS, Mounts and Hard links are first-class requirements.
> **Covered in:** [Filesystems — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. add another directory name for the same inode and normally cannot cross filesystems; data remains until the final link/open reference disappears. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FILESYSTEMS-SN-05

- [ ] **Question:** Design a production Filesystems capability where NFS, Bind mounts and Linux directory structure are first-class requirements.
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FILESYSTEMS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Filesystems capability where OverlayFS, Inodes and /etc, /var, /proc, /sys, /dev, /tmp are first-class requirements.
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. store filesystem object metadata and block references while directories map names to inode numbers; inode exhaustion is separate from byte exhaustion. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FILESYSTEMS-SN-07

- [ ] **Question:** Design a production Filesystems capability where Mounts, Hard links and ext4 are first-class requirements.
> **Covered in:** [Filesystems — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. add another directory name for the same inode and normally cannot cross filesystems; data remains until the final link/open reference disappears. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FILESYSTEMS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Filesystems capability where Bind mounts, Linux directory structure and XFS are first-class requirements.
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FILESYSTEMS-SN-09

- [ ] **Question:** Design a production Filesystems capability where Inodes, /etc, /var, /proc, /sys, /dev, /tmp and NFS are first-class requirements.
> **Covered in:** [Filesystems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: store filesystem object metadata and block references while directories map names to inode numbers; inode exhaustion is separate from byte exhaustion. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### FILESYSTEMS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Filesystems capability where Hard links, ext4 and OverlayFS are first-class requirements.
> **Covered in:** [Filesystems — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: add another directory name for the same inode and normally cannot cross filesystems; data remains until the final link/open reference disappears. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### FILESYSTEMS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Linux directory structure. How do you lead it end to end?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `uname -a; systemd-analyze` as one read-only checkpoint, not the whole diagnosis. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FILESYSTEMS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving /etc, /var, /proc, /sys, /dev, /tmp. How do you lead it end to end?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ps -eo pid,ppid,state,pcpu,pmem,cmd` as one read-only checkpoint, not the whole diagnosis. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FILESYSTEMS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ext4. How do you lead it end to end?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `vmstat 1; iostat -xz 1` as one read-only checkpoint, not the whole diagnosis. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FILESYSTEMS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving XFS. How do you lead it end to end?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip route; ss -lntup; journalctl -b` as one read-only checkpoint, not the whole diagnosis. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FILESYSTEMS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NFS. How do you lead it end to end?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `uname -a; systemd-analyze` as one read-only checkpoint, not the whole diagnosis. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FILESYSTEMS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving OverlayFS. How do you lead it end to end?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ps -eo pid,ppid,state,pcpu,pmem,cmd` as one read-only checkpoint, not the whole diagnosis. presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FILESYSTEMS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Mounts. How do you lead it end to end?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `vmstat 1; iostat -xz 1` as one read-only checkpoint, not the whole diagnosis. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FILESYSTEMS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Bind mounts. How do you lead it end to end?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ip route; ss -lntup; journalctl -b` as one read-only checkpoint, not the whole diagnosis. is part of Filesystems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FILESYSTEMS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Inodes. How do you lead it end to end?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `uname -a; systemd-analyze` as one read-only checkpoint, not the whole diagnosis. store filesystem object metadata and block references while directories map names to inode numbers; inode exhaustion is separate from byte exhaustion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### FILESYSTEMS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hard links. How do you lead it end to end?
> **Covered in:** [Filesystems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ps -eo pid,ppid,state,pcpu,pmem,cmd` as one read-only checkpoint, not the whole diagnosis. add another directory name for the same inode and normally cannot cross filesystems; data remains until the final link/open reference disappears. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Linux architecture](../01-linux-architecture/README.md) · [Study note](README.md) · [Next: Users and permissions →](../03-users-and-permissions/README.md)

<!-- reading-navigation:end -->
