# Operations, observability, reliability and security

<!-- chapter-guide:start -->
> **Step 210 of 373 — 10**
>
> **Builds on:** [CircleCI](../09-iac-delivery/03-ci-cd/09-circleci/README.md)
>
> **Now:** Learn **Operations, observability, reliability and security** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Observability](01-observability/README.md).
<!-- chapter-guide:end -->

## Integrated operations mental model

Observe user outcomes and system state, compare them with explicit SLO and security objectives, and take the smallest reversible action that reduces risk. Metrics, logs, traces, profiles and audit records answer different questions; telemetry itself needs availability, privacy, retention and cost controls. Reliability work joins capacity, alerting, incident response, postmortems, disaster recovery and game days with identity, secret, network, supply-chain and workload security.

```bash
curl -s http://SERVICE/metrics
kubectl get events -A --sort-by=.lastTimestamp
promtool check rules rules.yml
trivy fs .
```

Practise by selecting one disposable service, defining a user-facing SLI/SLO, adding a dashboard and multi-window burn alert, injecting a bounded latency or dependency failure, following metrics→trace→logs→change/audit evidence, restoring the SLO, and proving that the alert and runbook worked. Then test a restore rather than merely checking that a backup job is green.

Cleanup the injected failure, temporary alerts, dashboards, test data and disposable service; confirm telemetry ingestion and billable resources returned to the intended baseline.

Authoritative starting points: [OpenTelemetry](https://opentelemetry.io/docs/), [Google SRE books](https://sre.google/books/), and [SLSA](https://slsa.dev/).

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: CircleCI](../09-iac-delivery/03-ci-cd/09-circleci/README.md) · [Questions](questions-and-answers.md) · [Next: Observability →](01-observability/README.md)

<!-- reading-navigation:end -->
