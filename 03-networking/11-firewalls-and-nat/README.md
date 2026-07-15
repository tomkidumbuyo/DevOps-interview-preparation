# Firewalls and NAT

<!-- chapter-guide:start -->
> **Step 039 of 373 — 03.11**
>
> **Builds on:** [Proxies and gateways](../10-proxies-and-gateways/README.md)
>
> **Now:** Learn **Firewalls and NAT** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Network troubleshooting](../12-network-troubleshooting/README.md).
<!-- chapter-guide:end -->

> [Interview questions and answers](questions-and-answers.md) · [Master curriculum](../../curriculum/master-curriculum.txt) · Official starting point: <https://www.rfc-editor.org/>

## Easy mode: mental model

Master Firewalls and NAT from first principles through safe production operation and senior architecture decisions.

Learn this topic in layers: name the object or mechanism, trace its lifecycle/data path, configure it safely, observe a healthy and failed state, recover it, and then design it across failure domains and team boundaries.

```mermaid
flowchart LR
  R[requirement or symptom] --> M[Firewalls and NAT mechanism]
  M --> S[state and dependencies]
  S --> O[commands metrics logs traces audit]
  O --> D[decision mitigation or design]
  D --> V[user-facing verification]
```

## Complete curriculum checklist

| # | Topic | What you must understand and demonstrate |
|---:|---|---|
| 1 | **Stateless versus stateful firewalls** | is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. |
| 2 | **Ingress and egress rules** | is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 3 | **NAT** | is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 4 | **SNAT** | rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity. |
| 5 | **DNAT** | rewrites destination addressing for published services and must align with routing, policy and connection state. |
| 6 | **PAT** | is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 7 | **Connection tracking** | records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners. |
| 8 | **Network address exhaustion** | is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 9 | **Stateless versus stateful firewalls** | is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. |
| 10 | **Ingress and egress rules** | is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 11 | **NAT** | is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 12 | **SNAT** | rewrites source addressing, commonly for egress, changing return paths, attribution and ephemeral-port capacity. |
| 13 | **DNAT** | rewrites destination addressing for published services and must align with routing, policy and connection state. |
| 14 | **PAT** | is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 15 | **Connection tracking** | records stateful flow/NAT mappings; table exhaustion or stale state can break new connections despite open listeners. |
| 16 | **Network address exhaustion** | is part of Firewalls and NAT; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |

## Beginner → mid-level → senior learning path

1. **Beginner:** define every term; identify the relevant file, object, protocol, API, or command; explain one normal use.
2. **Mid-level:** configure it from source control, inspect effective runtime state, diagnose two failure modes, automate a safe change, and explain one trade-off.
3. **Senior:** clarify ambiguous requirements, map trust and failure domains, quantify capacity/SLO/RPO/RTO/cost, compare alternatives, plan migration/rollback, and assign ownership.

## Command and configuration lab

Run read-only checks first in a sandbox. For each command, predict healthy output, one failing result, the next discriminating check, and the safe rollback for any later mutation.

```bash
nft list ruleset
iptables-save 2>/dev/null
conntrack -L; conntrack -S
tcpdump -ni any 'host IP and port PORT'
```

## Hands-on practice: setup → failure → verification → cleanup

Create a disposable network lab: `docker network create devops-net-lab`; start `docker run -d --name web-lab --network devops-net-lab nginx:1.27-alpine`; verify with `docker run --rm --network devops-net-lab curlimages/curl:8.10.1 -sv http://web-lab/`. Controlled failure: query a wrong name and a closed port, compare DNS versus TCP evidence, then inspect the Docker network. Cleanup: `docker rm -f web-lab` and `docker network rm devops-net-lab`. Pulling images uses network/bandwidth; pin a verified digest in a governed environment.

Expected result: you can show the healthy evidence, reproduce a safe failure, explain why each command distinguishes one layer from another, restore the baseline, and prove cleanup. Hard extension: automate the lab from source control, add a test or alert for the injected failure, and write a five-step runbook another engineer can execute.

For code/configuration, be ready to review an intentionally unsafe diff and improve idempotency, secret handling, timeouts, validation, logging, tests, and rollback.

## Senior design checklist

State assumptions for tenants, traffic/work units, latency and availability targets, data classification/residency, recovery, team skills and budget. Draw control/data planes and synchronous/asynchronous dependencies. Cover identity, policy, encryption/key lifecycle, delivery provenance, observability, capacity, unit cost, operational ownership, migration and exit criteria. Name the evidence that would cause you to revise the design.

## Revision and practice

Complete the separate [checkbox interview bank](questions-and-answers.md). Do not memorize wording: speak in the order **definition → mechanism → evidence/configuration → failure/trade-off → production example**. For procedures use **stabilize → scope → inspect → hypothesize → test → mitigate → verify → prevent**.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Proxies and gateways](../10-proxies-and-gateways/README.md) · [Questions](questions-and-answers.md) · [Next: Network troubleshooting →](../12-network-troubleshooting/README.md)

<!-- reading-navigation:end -->
