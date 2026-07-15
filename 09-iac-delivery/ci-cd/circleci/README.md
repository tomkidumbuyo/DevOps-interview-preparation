# CircleCI

> [60 junior/mid/senior questions and answers](questions-and-answers.md) · [Parent CI/CD note](../README.md) · Verify version-sensitive syntax against the current CircleCI configuration reference.

## Mental model and file structure

CircleCI reads `.circleci/config.yml`. One trigger creates a pipeline; config processing creates workflows; workflows orchestrate jobs; each job obtains an executor and runs ordered steps. Workflows—not the job definitions—express dependencies, filters, contexts and approvals.

```mermaid
flowchart LR
  V[VCS API or schedule trigger] --> P[pipeline and parameters]
  P --> C[config compile]
  C --> W[workflow]
  W --> B[build job]
  W --> T[test jobs]
  B --> A[approval]
  T --> A
  A --> D[deploy job + restricted context/OIDC]
```

```text
repository/
├── .circleci/
│   ├── config.yml           # normal entry point
│   ├── src/                 # optional split source for `circleci config pack`
│   │   ├── @orb.yml
│   │   ├── commands/
│   │   ├── executors/
│   │   └── jobs/
│   └── continue.yml         # optional generated/dynamic continuation config
├── scripts/                 # locally runnable build/test/deploy logic
└── application/IaC source
```

## Top-level configuration format

```yaml
version: 2.1

setup: false                  # true only for dynamic setup configuration

parameters:                   # pipeline-level typed inputs
  deploy:
    type: boolean
    default: false
  target:
    type: enum
    enum: [staging, production]
    default: staging

orbs:                         # reusable packaged configuration
  aws-cli: circleci/aws-cli@x.y.z

executors:                    # reusable execution environments
  python:
    docker:
      - image: cimg/python:3.12
    resource_class: medium
    working_directory: ~/project

commands:                     # reusable parameterized step sequences
  install-dependencies:
    parameters:
      lockfile:
        type: string
        default: requirements.txt
    steps:
      - restore_cache:
          keys:
            - pip-v1-{{ checksum "<< parameters.lockfile >>" }}
            - pip-v1-
      - run:
          name: Install dependencies
          command: python -m pip install -r << parameters.lockfile >>
      - save_cache:
          key: pip-v1-{{ checksum "<< parameters.lockfile >>" }}
          paths: [~/.cache/pip]

jobs:                         # how one runner executes ordered steps
  test:
    executor: python
    parameters:
      shard:
        type: integer
        default: 0
    steps:
      - checkout
      - install-dependencies
      - run:
          name: Tests
          command: python -m pytest -q
          no_output_timeout: 10m
      - store_test_results:
          path: test-results
      - store_artifacts:
          path: test-results
          destination: tests

workflows:                    # when and in what order jobs run
  build-test-deploy:
    jobs:
      - test:
          filters:
            branches:
              ignore: docs-only
      - hold-production:
          type: approval
          requires: [test]
          filters:
            branches:
              only: main
      - deploy:
          requires: [hold-production]
          context: production-deploy
          serial-group: production/my-service
          filters:
            branches:
              only: main
```

Core top-level keys:

| Key | Purpose |
|---|---|
| `version` | CircleCI configuration version; 2.1 enables reusable config/orbs. |
| `setup` | Marks the first phase of dynamic configuration. |
| `parameters` | Typed pipeline inputs available during config processing. |
| `orbs` | Imports or defines reusable commands, executors and jobs. |
| `executors` | Names reusable Docker/machine/macOS/Windows execution environments. |
| `commands` | Names reusable step sequences; commands run inside a job. |
| `jobs` | Defines executor, parameters, environment and ordered steps. |
| `workflows` | Invokes jobs and defines dependencies, filters, schedules, contexts, approvals and serialization. |

## Full practical build/test/deploy example

This example uses Docker executor jobs, a PostgreSQL secondary container, workspaces to move the built artifact within the workflow, test artifacts for retained evidence, an approval and a restricted context. Replace `YOUR_ORG` and the deploy script. Pin all production images and orbs to reviewed immutable versions/digests where supported.

```yaml
version: 2.1

parameters:
  run_deploy:
    type: boolean
    default: false

executors:
  python-executor:
    docker:
      - image: cimg/python:3.12
    resource_class: medium

commands:
  install:
    steps:
      - restore_cache:
          keys:
            - pip-v2-{{ checksum "requirements.txt" }}
            - pip-v2-
      - run:
          name: Install locked dependencies
          command: python -m pip install -r requirements.txt
      - save_cache:
          key: pip-v2-{{ checksum "requirements.txt" }}
          paths: [~/.cache/pip]

jobs:
  lint:
    executor: python-executor
    steps:
      - checkout
      - install
      - run: python -m ruff check .
      - run: python -m mypy src

  test:
    docker:
      - image: cimg/python:3.12
        environment:
          DATABASE_URL: postgresql://test:test@localhost:5432/app
      - image: cimg/postgres:16.4
        environment:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: app
    resource_class: medium
    steps:
      - checkout
      - install
      - run:
          name: Wait for test database
          command: dockerize -wait tcp://localhost:5432 -timeout 60s
      - run:
          name: Tests
          command: python -m pytest --junitxml=test-results/results.xml
      - store_test_results:
          path: test-results
      - store_artifacts:
          path: test-results
          destination: tests

  build:
    executor: python-executor
    steps:
      - checkout
      - run:
          name: Build immutable archive and digest
          command: |
            set -Eeuo pipefail
            mkdir -p /tmp/workspace
            tar -czf /tmp/workspace/application.tgz src requirements.txt
            sha256sum /tmp/workspace/application.tgz | tee /tmp/workspace/application.sha256
      - persist_to_workspace:
          root: /tmp/workspace
          paths:
            - application.tgz
            - application.sha256

  deploy-staging:
    executor: python-executor
    environment:
      TARGET_ENVIRONMENT: staging
    steps:
      - checkout
      - attach_workspace:
          at: /tmp/workspace
      - run:
          name: Verify promoted artifact
          command: cd /tmp/workspace && sha256sum --check application.sha256
      - run:
          name: Exchange CircleCI OIDC token for short-lived cloud credentials
          command: ./scripts/cloud-login-oidc.sh
      - run:
          name: Deploy and verify user path
          command: ./scripts/deploy-and-smoke.sh /tmp/workspace/application.tgz staging

  deploy-production:
    executor: python-executor
    environment:
      TARGET_ENVIRONMENT: production
    steps:
      - checkout
      - attach_workspace:
          at: /tmp/workspace
      - run: cd /tmp/workspace && sha256sum --check application.sha256
      - run: ./scripts/cloud-login-oidc.sh
      - run: ./scripts/deploy-and-smoke.sh /tmp/workspace/application.tgz production

workflows:
  delivery:
    jobs:
      - lint
      - test
      - build:
          requires: [lint, test]
      - deploy-staging:
          requires: [build]
          context: staging-deploy
          serial-group: YOUR_ORG/my-service/staging
          filters:
            branches:
              only: main
      - approve-production:
          type: approval
          requires: [deploy-staging]
          filters:
            branches:
              only: main
      - deploy-production:
          requires: [approve-production]
          context: production-deploy
          serial-group: YOUR_ORG/my-service/production
          filters:
            branches:
              only: main
```

The first Docker image is the primary container in which steps execute. Additional images are service containers reachable through `localhost` in the Docker executor model. Workspaces move files between jobs in one workflow; artifacts retain downloadable evidence after the run; caches accelerate future jobs. They are not interchangeable.

## Executors and resource classes

- `docker`: fastest container-based executor for builds that do not require a full VM/privileged nested runtime. The primary container's image entrypoint/command behavior differs from ordinary `docker run`; inspect the current reference.
- `machine`: full VM suited to Docker builds, low-level networking and host operations; pin a supported image.
- `macos`/`windows`: platform-specific executors with distinct images and costs.
- self-hosted runners: custom network/hardware/GPU access, but runner isolation, patching, persistence and untrusted code become your responsibility.
- `resource_class`: selects CPU/memory/accelerator class and directly affects capacity and cost.

Use a clean ephemeral executor for untrusted changes. Do not attach public-fork pipelines to persistent privileged runners or contexts with production access.

## Pipelines, parameters and dynamic configuration

Pipeline parameters are resolved while configuration is compiled and use `<< pipeline.parameters.name >>`. Job/command/executor parameters use `<< parameters.name >>`. Shell environment variables are runtime values and are not the same substitution phase.

```yaml
parameters:
  service:
    type: enum
    enum: [gateway, evaluator, indexer]
    default: gateway

workflows:
  service-ci:
    when: << pipeline.parameters.run_ci >>
    jobs:
      - test:
          service: << pipeline.parameters.service >>
```

Dynamic configuration sets `setup: true` in the initial config, computes pipeline values and invokes the continuation API/orb with another configuration. Treat generated config as code: validate inputs, constrain possible jobs/executors/contexts, persist the generated output for audit and prevent a PR from generating a privileged deployment path.

## Reusable configuration and orbs

An orb can package commands, executors and jobs. Registry orbs are versioned packages; URL orbs and inline orbs have different distribution/trust models. Importing an orb expands trusted pipeline code, so use an organization allowlist, pin reviewed versions and inspect source/permissions.

```yaml
version: 2.1
orbs:
  platform:
    commands:
      verify-release:
        parameters:
          manifest: {type: string}
        steps:
          - run:
              name: Verify release
              command: ./scripts/verify-release.sh << parameters.manifest >>
```

Use local commands when reuse is inside one config, an inline orb for a larger local namespace, and a private registry orb for versioned cross-repository standards. Keep application-specific logic in scripts/components that can be tested without CircleCI.

## Workflows, dependencies, filters and approvals

`requires` creates fan-in/fan-out dependencies. Branch/tag filters are applied to job invocations inside workflows; if an upstream required job is filtered out incorrectly, dependent behavior can surprise you. Test tag releases explicitly.

Approval jobs hold downstream work but do not themselves allocate an executor. Restrict the downstream context and cloud role; approval alone does not prevent a changed artifact or expired evidence, so verify digest and gate freshness after approval.

`serial-group` can serialize jobs across pipelines for one deployment target. Use a stable organization/project/environment key, understand cancellation/queue semantics and keep deployment idempotent in case a worker dies after a remote side effect.

## Environment variables, contexts, secrets and OIDC

Environment variables may exist at project, context, job, executor, container or step scope with defined precedence. Contexts share protected variables across projects and can be restricted with security groups/expressions. A context grants its values to a job's steps; any untrusted command in that job can exfiltrate them.

Prefer OIDC tokens (`CIRCLE_OIDC_TOKEN_V2` where appropriate) to exchange for short-lived cloud credentials. Restrict the cloud trust policy using issuer, audience and stable organization/project/job/context claims. Decode claims in a sandbox without printing the bearer token and prove that another project/branch/context cannot assume the role.

Do not put secrets in config, cache, workspace, artifacts, test reports, command echo or debug output. Secret masking is best-effort, not an authorization boundary.

## Cache, workspace, artifacts and test results

| Mechanism | Lifetime/use | Interview trap |
|---|---|---|
| Cache | Best-effort reuse across jobs/pipelines by immutable key prefix | Restored cache can be stale or influenced by less-trusted builds; never treat as a promoted release. |
| Workspace | Files passed among jobs in one workflow | Layer attachment/order and reruns matter; use unique paths and checksums. |
| Artifact | Retained downloadable build/evidence output | Retention and access do not prove integrity; verify digest/provenance. |
| Test results | JUnit-style data used by UI/Insights | A report upload does not change the test command's exit status. |

## CLI, validation and debugging

```bash
circleci version
circleci config validate .circleci/config.yml
circleci config process .circleci/config.yml
circleci config pack .circleci/src > /tmp/packed-config.yml
circleci local execute --job test
circleci orb validate path/to/orb.yml
circleci orb info NAMESPACE/ORB
```

Local execution is not an exact CircleCI Cloud/Server simulation: contexts, remote caches, workflows, approvals, machine images, OIDC and infrastructure behavior differ. Use it for fast job/command feedback, then verify a disposable remote pipeline.

Troubleshoot in this order: VCS trigger/project integration → pipeline parameter/config compilation → workflow `when`/filters → dependency/approval → context/security restriction → executor/resource availability → checkout/dependency/cache → application command → workspace/artifact → cloud/deployment. Compare the compiled config, not only source YAML.

Rerun/SSH debug can expose runtime state and credentials; authorize it, time-bound it, audit it and avoid privileged production jobs. Use Insights/API/audit logs to investigate queue time, duration, failures, credits and changes.

## Security and senior architecture checklist

- Separate untrusted PR validation from jobs with restricted contexts, OIDC or self-hosted network access.
- Pin and review images/orbs/dependencies; generate SBOM/provenance and promote one artifact digest.
- Use least-privileged contexts and short-lived federated identity; restrict external trust claims.
- Validate dynamic config so parameters cannot synthesize a privileged job.
- Serialize deployment targets, use approvals with evidence freshness and make retries idempotent.
- Bound job time, parallelism, resource class and credit spend; alert on queue/capacity/failure trends.
- Treat runner fleets as production: ephemeral isolation, patching, egress policy, no ambient credentials and tenant separation.
- Preserve workflow, approval, artifact digest, OIDC/cloud and deployment verification in one audit lineage.

## Hands-on lab

1. Install the CircleCI CLI and create a disposable repository/project. Add `version: 2.1`, one executor, reusable install command and lint/test jobs.
2. Validate/process locally, then run remotely. Intentionally introduce invalid indentation and a missing required job; compare compile-time versus run-time failure.
3. Add a database service container, cache, JUnit results and artifact. Explain which data persists to which scope.
4. Build once, persist a digest through a workspace, deploy to a sandbox context and verify the digest/user path.
5. Add an approval, production-style restricted context and serial group. Replace a static test cloud key with OIDC and prove negative trust cases.
6. Extract reuse into an inline/private orb or packed config, test it, inspect the processed output, then delete sandbox deployments and disable/remove project credentials and contexts created for the lab.

## Documentation and videos

Official documentation:

- [CircleCI configuration reference](https://circleci.com/docs/reference/configuration-reference/)
- [Workflow orchestration](https://circleci.com/docs/guides/orchestrate/workflows/)
- [Reusable configuration reference](https://circleci.com/docs/reference/reusing-config/)
- [Orbs overview](https://circleci.com/docs/orbs/use/orb-intro/)
- [Contexts](https://circleci.com/docs/guides/security/contexts/)
- [OpenID Connect tokens](https://circleci.com/docs/guides/permissions-authentication/openid-connect-tokens/)
- [Dynamic configuration](https://circleci.com/docs/guides/orchestrate/dynamic-config/)
- [CircleCI CLI](https://circleci.com/docs/guides/toolkit/local-cli/)

Video resources:

- [CircleCI's official YouTube channel—getting started and configuration videos](https://www.youtube.com/@CircleCIvideos/search?query=getting%20started%20config)
- [CircleCI's official YouTube channel—security and OIDC videos](https://www.youtube.com/@CircleCIvideos/search?query=OIDC%20security)

## Interview traps

- A pipeline is not a workflow, and a workflow is not a job.
- `commands` are reusable steps; `jobs` own executors; workflows invoke jobs.
- A workspace is not a cache and neither is a secure artifact registry.
- Context masking does not stop a malicious authorized step from exfiltrating values.
- Local execution cannot reproduce every remote workflow/security feature.
- Dynamic config is a privileged code-generation path and needs the same review/policy as ordinary config.
