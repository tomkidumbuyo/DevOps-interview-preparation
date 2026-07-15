# Operations, observability, reliability and security

<!-- child-topic-toc:start -->
## Table of contents and deeper notes

This parent note explains how the child topics work together. Follow each child link for the deeper mechanism, real commands/configuration, hands-on practice, authoritative documentation, and its local interview bank.

- [Observability](observability/README.md) — [questions and answers](observability/questions-and-answers.md)
- [Platform and cloud security](platform-and-cloud-security/README.md) — [questions and answers](platform-and-cloud-security/questions-and-answers.md)
- [SRE and reliability engineering](sre-and-reliability-engineering/README.md) — [questions and answers](sre-and-reliability-engineering/questions-and-answers.md)
<!-- child-topic-toc:end -->
<!-- generated-topic-index:start -->
## Deep topic branches

- [Observability](observability/README.md) — [Q&A](observability/questions-and-answers.md)
- [SRE and reliability engineering](sre-and-reliability-engineering/README.md) — [Q&A](sre-and-reliability-engineering/questions-and-answers.md)
- [Platform and cloud security](platform-and-cloud-security/README.md) — [Q&A](platform-and-cloud-security/questions-and-answers.md)
<!-- generated-topic-index:end -->

## Integrated operations mental model

Observe user outcomes and system state, compare them with explicit SLO and security objectives, and take the smallest reversible action that reduces risk. Metrics, logs, traces, profiles and audit records answer different questions; telemetry itself needs availability, privacy, retention and cost controls. Reliability work joins capacity, alerting, incident response, postmortems, disaster recovery and game days with identity, secret, network, supply-chain and workload security.

```bash
curl -s http://SERVICE/metrics
kubectl get events -A --sort-by=.lastTimestamp
promtool check rules rules.yml
trivy fs .
```

Practise by selecting one disposable service, defining a user-facing SLI/SLO, adding a dashboard and multi-window burn alert, injecting a bounded latency or dependency failure, following metrics→trace→logs→change/audit evidence, restoring the SLO, and proving that the alert and runbook worked. Then test a restore rather than merely checking that a backup job is green.

Authoritative starting points: [OpenTelemetry](https://opentelemetry.io/docs/), [Google SRE books](https://sre.google/books/), and [SLSA](https://slsa.dev/).
