# Hyperparameter tuning and experiment search — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JN-01

- [ ] **Question:** What is Search space, and why does it matter in Hyperparameter tuning and experiment search?

**Answer:** type/range/scale/conditional relationships encode valid candidate configurations. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JN-02

- [ ] **Question:** What is Random/grid/Bayesian, and why does it matter in Hyperparameter tuning and experiment search?

**Answer:** exploration strategy trades coverage, parallelism and sample efficiency. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JN-03

- [ ] **Question:** What is Objective, and why does it matter in Hyperparameter tuning and experiment search?

**Answer:** metric/dataset/slice/direction/aggregation must represent the production goal. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JN-04

- [ ] **Question:** What is Multi-objective, and why does it matter in Hyperparameter tuning and experiment search?

**Answer:** quality, latency, memory and cost create a Pareto frontier rather than one magic scalar. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JN-05

- [ ] **Question:** What is Early stopping, and why does it matter in Hyperparameter tuning and experiment search?

**Answer:** prunes poor trials only when partial metrics are comparable and not systematically biased. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JN-06

- [ ] **Question:** What is Trial isolation, and why does it matter in Hyperparameter tuning and experiment search?

**Answer:** data split, seed, resources and artifact paths cannot collide across parallel trials. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JN-07

- [ ] **Question:** What is Budget, and why does it matter in Hyperparameter tuning and experiment search?

**Answer:** maximum trials/time/GPU-hours and concurrency prevent search from starving production. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JN-08

- [ ] **Code:** **Question:** What does `mlflow runs list --experiment-id EXPERIMENT_ID` help you verify for Hyperparameter tuning and experiment search?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: ASHA/HyperBand-style resource allocation needs fair checkpoints and monotonic resource semantics.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JN-09

- [ ] **Code:** **Question:** What does `kubectl get experiments,trials -A` help you verify for Hyperparameter tuning and experiment search?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: repeated tuning against one validation set overfits the evaluation process.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe experiment NAME -n NS` help you verify for Hyperparameter tuning and experiment search?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: rerun finalist with locked config/seeds and independent evaluation before registry approval.

## Junior — procedural and command questions

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JP-01

- [ ] **Code:** **Question:** A basic Search space check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get experiments,trials -A` and capture exact status/reason/request ID. type/range/scale/conditional relationships encode valid candidate configurations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JP-02

- [ ] **Question:** A basic Random/grid/Bayesian check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe experiment NAME -n NS` and capture exact status/reason/request ID. exploration strategy trades coverage, parallelism and sample efficiency. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JP-03

- [ ] **Question:** A basic Objective check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python tune.py --smoke-test --max-trials 4` and capture exact status/reason/request ID. metric/dataset/slice/direction/aggregation must represent the production goal. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JP-04

- [ ] **Code:** **Question:** A basic Multi-objective check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow runs list --experiment-id EXPERIMENT_ID` and capture exact status/reason/request ID. quality, latency, memory and cost create a Pareto frontier rather than one magic scalar. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JP-05

- [ ] **Question:** A basic Early stopping check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get experiments,trials -A` and capture exact status/reason/request ID. prunes poor trials only when partial metrics are comparable and not systematically biased. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JP-06

- [ ] **Question:** A basic Trial isolation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe experiment NAME -n NS` and capture exact status/reason/request ID. data split, seed, resources and artifact paths cannot collide across parallel trials. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JP-07

- [ ] **Code:** **Question:** A basic Budget check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python tune.py --smoke-test --max-trials 4` and capture exact status/reason/request ID. maximum trials/time/GPU-hours and concurrency prevent search from starving production. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JP-08

- [ ] **Question:** A basic Scheduler check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow runs list --experiment-id EXPERIMENT_ID` and capture exact status/reason/request ID. ASHA/HyperBand-style resource allocation needs fair checkpoints and monotonic resource semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JP-09

- [ ] **Question:** A basic Selection bias check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get experiments,trials -A` and capture exact status/reason/request ID. repeated tuning against one validation set overfits the evaluation process. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-JP-10

- [ ] **Code:** **Question:** A basic Promotion check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe experiment NAME -n NS` and capture exact status/reason/request ID. rerun finalist with locked config/seeds and independent evaluation before registry approval. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MN-01

- [ ] **Question:** Compare Search space with Random/grid/Bayesian. When would each change your design?

**Answer:** Search space: type/range/scale/conditional relationships encode valid candidate configurations. Random/grid/Bayesian: exploration strategy trades coverage, parallelism and sample efficiency. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MN-02

- [ ] **Question:** Compare Random/grid/Bayesian with Objective. When would each change your design?

**Answer:** Random/grid/Bayesian: exploration strategy trades coverage, parallelism and sample efficiency. Objective: metric/dataset/slice/direction/aggregation must represent the production goal. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MN-03

- [ ] **Question:** Compare Objective with Multi-objective. When would each change your design?

**Answer:** Objective: metric/dataset/slice/direction/aggregation must represent the production goal. Multi-objective: quality, latency, memory and cost create a Pareto frontier rather than one magic scalar. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MN-04

- [ ] **Configuration review:** **Question:** Compare Multi-objective with Early stopping. When would each change your design?

**Answer:** Multi-objective: quality, latency, memory and cost create a Pareto frontier rather than one magic scalar. Early stopping: prunes poor trials only when partial metrics are comparable and not systematically biased. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MN-05

- [ ] **Question:** Compare Early stopping with Trial isolation. When would each change your design?

**Answer:** Early stopping: prunes poor trials only when partial metrics are comparable and not systematically biased. Trial isolation: data split, seed, resources and artifact paths cannot collide across parallel trials. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MN-06

- [ ] **Question:** Compare Trial isolation with Budget. When would each change your design?

**Answer:** Trial isolation: data split, seed, resources and artifact paths cannot collide across parallel trials. Budget: maximum trials/time/GPU-hours and concurrency prevent search from starving production. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MN-07

- [ ] **Configuration review:** **Question:** Compare Budget with Scheduler. When would each change your design?

**Answer:** Budget: maximum trials/time/GPU-hours and concurrency prevent search from starving production. Scheduler: ASHA/HyperBand-style resource allocation needs fair checkpoints and monotonic resource semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MN-08

- [ ] **Question:** Compare Scheduler with Selection bias. When would each change your design?

**Answer:** Scheduler: ASHA/HyperBand-style resource allocation needs fair checkpoints and monotonic resource semantics. Selection bias: repeated tuning against one validation set overfits the evaluation process. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MN-09

- [ ] **Question:** Compare Selection bias with Promotion. When would each change your design?

**Answer:** Selection bias: repeated tuning against one validation set overfits the evaluation process. Promotion: rerun finalist with locked config/seeds and independent evaluation before registry approval. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MN-10

- [ ] **Configuration review:** **Question:** Compare Promotion with Search space. When would each change your design?

**Answer:** Promotion: rerun finalist with locked config/seeds and independent evaluation before registry approval. Search space: type/range/scale/conditional relationships encode valid candidate configurations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Search space; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get experiments,trials -A` plus recent events/changes, then correlate the service-specific SLI. type/range/scale/conditional relationships encode valid candidate configurations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MP-02

- [ ] **Question:** Production is degraded around Random/grid/Bayesian; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe experiment NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. exploration strategy trades coverage, parallelism and sample efficiency. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Objective; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python tune.py --smoke-test --max-trials 4` plus recent events/changes, then correlate the service-specific SLI. metric/dataset/slice/direction/aggregation must represent the production goal. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MP-04

- [ ] **Question:** Production is degraded around Multi-objective; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow runs list --experiment-id EXPERIMENT_ID` plus recent events/changes, then correlate the service-specific SLI. quality, latency, memory and cost create a Pareto frontier rather than one magic scalar. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Early stopping; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get experiments,trials -A` plus recent events/changes, then correlate the service-specific SLI. prunes poor trials only when partial metrics are comparable and not systematically biased. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MP-06

- [ ] **Question:** Production is degraded around Trial isolation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe experiment NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. data split, seed, resources and artifact paths cannot collide across parallel trials. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Budget; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python tune.py --smoke-test --max-trials 4` plus recent events/changes, then correlate the service-specific SLI. maximum trials/time/GPU-hours and concurrency prevent search from starving production. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MP-08

- [ ] **Question:** Production is degraded around Scheduler; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow runs list --experiment-id EXPERIMENT_ID` plus recent events/changes, then correlate the service-specific SLI. ASHA/HyperBand-style resource allocation needs fair checkpoints and monotonic resource semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Selection bias; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get experiments,trials -A` plus recent events/changes, then correlate the service-specific SLI. repeated tuning against one validation set overfits the evaluation process. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-MP-10

- [ ] **Question:** Production is degraded around Promotion; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe experiment NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. rerun finalist with locked config/seeds and independent evaluation before registry approval. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SN-01

- [ ] **Question:** Design a production Hyperparameter tuning and experiment search capability where Search space, Multi-objective and Budget are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: type/range/scale/conditional relationships encode valid candidate configurations. quality, latency, memory and cost create a Pareto frontier rather than one magic scalar. maximum trials/time/GPU-hours and concurrency prevent search from starving production. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Hyperparameter tuning and experiment search capability where Random/grid/Bayesian, Early stopping and Scheduler are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exploration strategy trades coverage, parallelism and sample efficiency. prunes poor trials only when partial metrics are comparable and not systematically biased. ASHA/HyperBand-style resource allocation needs fair checkpoints and monotonic resource semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SN-03

- [ ] **Question:** Design a production Hyperparameter tuning and experiment search capability where Objective, Trial isolation and Selection bias are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: metric/dataset/slice/direction/aggregation must represent the production goal. data split, seed, resources and artifact paths cannot collide across parallel trials. repeated tuning against one validation set overfits the evaluation process. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Hyperparameter tuning and experiment search capability where Multi-objective, Budget and Promotion are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: quality, latency, memory and cost create a Pareto frontier rather than one magic scalar. maximum trials/time/GPU-hours and concurrency prevent search from starving production. rerun finalist with locked config/seeds and independent evaluation before registry approval. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SN-05

- [ ] **Question:** Design a production Hyperparameter tuning and experiment search capability where Early stopping, Scheduler and Search space are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prunes poor trials only when partial metrics are comparable and not systematically biased. ASHA/HyperBand-style resource allocation needs fair checkpoints and monotonic resource semantics. type/range/scale/conditional relationships encode valid candidate configurations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Hyperparameter tuning and experiment search capability where Trial isolation, Selection bias and Random/grid/Bayesian are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: data split, seed, resources and artifact paths cannot collide across parallel trials. repeated tuning against one validation set overfits the evaluation process. exploration strategy trades coverage, parallelism and sample efficiency. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SN-07

- [ ] **Question:** Design a production Hyperparameter tuning and experiment search capability where Budget, Promotion and Objective are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: maximum trials/time/GPU-hours and concurrency prevent search from starving production. rerun finalist with locked config/seeds and independent evaluation before registry approval. metric/dataset/slice/direction/aggregation must represent the production goal. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Hyperparameter tuning and experiment search capability where Scheduler, Search space and Multi-objective are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ASHA/HyperBand-style resource allocation needs fair checkpoints and monotonic resource semantics. type/range/scale/conditional relationships encode valid candidate configurations. quality, latency, memory and cost create a Pareto frontier rather than one magic scalar. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SN-09

- [ ] **Question:** Design a production Hyperparameter tuning and experiment search capability where Selection bias, Random/grid/Bayesian and Early stopping are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: repeated tuning against one validation set overfits the evaluation process. exploration strategy trades coverage, parallelism and sample efficiency. prunes poor trials only when partial metrics are comparable and not systematically biased. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Hyperparameter tuning and experiment search capability where Promotion, Objective and Trial isolation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: rerun finalist with locked config/seeds and independent evaluation before registry approval. metric/dataset/slice/direction/aggregation must represent the production goal. data split, seed, resources and artifact paths cannot collide across parallel trials. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Search space. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get experiments,trials -A` as one read-only checkpoint, not the whole diagnosis. type/range/scale/conditional relationships encode valid candidate configurations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Random/grid/Bayesian. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe experiment NAME -n NS` as one read-only checkpoint, not the whole diagnosis. exploration strategy trades coverage, parallelism and sample efficiency. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Objective. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python tune.py --smoke-test --max-trials 4` as one read-only checkpoint, not the whole diagnosis. metric/dataset/slice/direction/aggregation must represent the production goal. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Multi-objective. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow runs list --experiment-id EXPERIMENT_ID` as one read-only checkpoint, not the whole diagnosis. quality, latency, memory and cost create a Pareto frontier rather than one magic scalar. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Early stopping. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get experiments,trials -A` as one read-only checkpoint, not the whole diagnosis. prunes poor trials only when partial metrics are comparable and not systematically biased. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Trial isolation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe experiment NAME -n NS` as one read-only checkpoint, not the whole diagnosis. data split, seed, resources and artifact paths cannot collide across parallel trials. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Budget. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python tune.py --smoke-test --max-trials 4` as one read-only checkpoint, not the whole diagnosis. maximum trials/time/GPU-hours and concurrency prevent search from starving production. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Scheduler. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow runs list --experiment-id EXPERIMENT_ID` as one read-only checkpoint, not the whole diagnosis. ASHA/HyperBand-style resource allocation needs fair checkpoints and monotonic resource semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Selection bias. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get experiments,trials -A` as one read-only checkpoint, not the whole diagnosis. repeated tuning against one validation set overfits the evaluation process. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### HYPERPARAMETER-TUNING-AND-EXPERIMENT-SEARCH-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Promotion. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe experiment NAME -n NS` as one read-only checkpoint, not the whole diagnosis. rerun finalist with locked config/seeds and independent evaluation before registry approval. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
