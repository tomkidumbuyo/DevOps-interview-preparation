# Andela DevOps / Senior AI Platform interview readiness

Andela's current assessment material describes practical work simulations that may include system design, coding, code review and collaboration. Its live technical interview guidance describes a roughly 60-minute technical discussion/practical assessment of experience, technical proficiency, problem solving and communication. Exact client stages vary, so confirm the invitation instructions and obey each exercise's AI/tool policy.

Official references:

- [Introducing Andela Assessment](https://help.andela.com/hc/en-us/articles/53139205189395-Introducing-Andela-Assessment)
- [Live technical interview](https://help.andela.com/hc/en-us/articles/26571687079955-Step-2-The-live-technical-interview)
- [How to succeed in the Andela assessment](https://help.andela.com/hc/en-us/articles/53139336343571-How-to-succeed-in-the-Andela-assessment)
- [Technical screening preparation shortlist](https://help.andela.com/hc/en-us/articles/26609902057747-Technical-screening-interview-preparation-short-list)
- [Possible client interview formats](https://help.andela.com/hc/en-us/articles/33928645296275-What-type-of-client-interview-could-I-expect)

## 90-minute mock simulation

### 0–10 minutes: requirement discovery

Ask about tenants, request/token distribution, model sizes, GPU/provider constraints, latency/quality/availability SLOs, data class/residency, RPO/RTO, SaaS/private/on-prem modes, team/on-call and budget. State assumptions when the interviewer withholds data.

### 10–35 minutes: system design

Design a tenant-aware AI platform with Kubernetes/GPU capacity, model serving, LLM gateway, RAG, evaluation, release lineage, observability, governance and cost allocation. Compare managed versus portable components. Draw control/data planes, trust/failure domains and request path. Include canary/rollback, regional/customer deployment, upgrades and support.

### 35–55 minutes: code/configuration

Implement or repair one of:

- Kubernetes Deployment/Service/HPA/PDB/NetworkPolicy with probes, resources, security context and config/secret references;
- Terraform module/state-safe refactor or Pulumi component/Output handling;
- GitHub Actions/CircleCI workflow with test, immutable artifact, OIDC, environment/approval and verification;
- Python/shell automation with typed validation, timeout/retry/idempotency, safe logging and tests.

Narrate intent, edge cases and how you would test; do not silently type.

### 55–70 minutes: code review

Look for secret exposure, wildcard identity, mutable tags/actions, untrusted runner context, non-idempotent retry, missing timeout, unsafe deletion/replacement, wrong Kubernetes readiness/resources, missing rollback, excessive telemetry data and unbounded cost/concurrency. Prioritize severity and propose a minimal safe patch plus longer-term improvement.

### 70–85 minutes: incident scenario

Example: “TTFT and 429s rose after a model release; GPU utilization is high, one RAG tenant sees stale content and gateway cost doubled.” Use incident command, scope cohorts/recent changes, trace gateway→retrieval→queue/prefill/decode/provider, stop amplification, roll back or shed reversibly, verify quality/security/billing and add prevention.

### 85–90 minutes: candidate questions

Ask about ownership, platform users, current failure/cost burden, on-call, decision authority, deployment modes, GPU/provider contracts, governance expectations, success in 30/90 days and why the role is open.

## Communication contract

- Lead with the decision or next diagnostic hypothesis.
- State what a command/result would prove and what would falsify the hypothesis.
- Distinguish what you know from what you would verify in current docs/account/cluster.
- Think aloud without narrating every keystroke.
- When stuck, reduce scope, restate invariants and test the safest smallest assumption.
- Do not bluff vendor behavior or regulatory conclusions.

## Environment checklist

- Stable EU-overlap availability/timezone statement and interview calendar conversion.
- Tested camera, microphone, screen share, terminal, editor and diagram tool.
- Clean disposable repository/sandbox; no employer/customer credentials, VPNs or data.
- Current `git`, Docker/container runtime, `kubectl`, Terraform, Pulumi, Python and optional `gh`/CircleCI CLI.
- Local command history and screen free of secrets.
- Follow the assessment's explicit policy on AI and external help; some scenarios may allow tools and others may not.
