# Architecture Specification - AI-SE
## Student: Vojtech Hrabal
## Date: February 26, 2026
## Client: EuroHealth Insurance AG
## Deliverable: Day 13 `architecture-[role].md`

---

## 1. Component Objective (AI-SE)

Design and operate the deployment/release backbone for EuroHealth AI helpdesk so that:
- on-prem runtime is reliable,
- policy controls are enforced before release and at runtime,
- audit evidence is reconstructable,
- delivery remains feasible within EUR 180K / 6 months.

---

## 2. Inputs and Hard Constraints

- On-prem only (no cloud fallback for production traffic).
- Existing fragmented AI landscape (Moveworks + shadow AI systems).
- Knowledge base quality risk (~30 percent outdated).
- Multi-language support (EN/DE/CZ) across 8 countries.
- Tight budget and timeline pressure.

---

## 3. AI-SE Component Specification

### 3.1 Responsibilities

1. Define runtime packaging and environment configuration.
2. Define CI/CD gates for model/prompt/policy changes.
3. Ensure policy validation is part of release criteria.
4. Ensure audit logging schema is complete and consistent.
5. Define rollback and incident response entry points.

### 3.2 File/Component mapping in this project

- `Dockerfile` -> runtime image baseline.
- `docker-compose.yml` -> local/on-prem service orchestration baseline.
- `src/policy_engine.py` -> PDP/PEP runtime enforcement implementation.
- `policies/*.yaml` -> policy rules loaded by PDP.
- `audit.log` -> append-only decision log output.
- `tests/test_policies.py` -> policy behavior test entry point.

---

## 4. Deployment Architecture (AI-SE view)

```text
User Query
  -> Agent Runtime (src/agent.py)
  -> Retriever (src/retriever.py)
  -> Draft Response
  -> PEP check (src/policy_engine.py + policies/*.yaml)
     -> allow | block | redact | escalate
  -> Final Response
  -> audit.log (structured event)
```

Release flow:

```text
Git commit (code/prompt/policy)
  -> CI checks (lint/test/policy schema)
  -> policy regression tests
  -> image build (Dockerfile)
  -> environment deploy (compose/on-prem)
  -> smoke test + rollback guard
```

---

## 5. Policy Enforcement Placement

- **Runtime PEP location:** between response generation and response delivery.
- **Fail-safe rule:** if policy evaluation is unavailable, default to block/escalate (not allow).
- **Required decision outputs:** `decision`, `policy`, `rule_id`, `reason`, `timestamp`, `query_hash`.
- **Policy lifecycle:** policy files are versioned and validated in CI before deployment.

---

## 6. Interface Contracts (Checkpoint 2 ready)

### Contract A: AI-SE <-> FDE (Deployment and runtime)
- **Format:** YAML + env config + deployment manifest.
- **AI-SE sends:** image tag, release metadata, health probe config, rollback instructions.
- **AI-SE receives:** infrastructure limits, runtime topology, resource envelope.
- **Error handling:** failed deploy auto-reverts to last known good image.

### Contract B: AI-SE <-> AI-SEC (Policy compliance in delivery pipeline)
- **Format:** YAML policy schema and CI validation report.
- **AI-SE sends:** policy validation outcome, build gate status, deployment evidence.
- **AI-SE receives:** rule schema updates, mandatory control checks, risk exceptions.
- **Error handling:** invalid policy schema blocks release.

### Contract C: AI-SE <-> AI-DA (Operational/compliance telemetry)
- **Format:** structured JSON log event schema.
- **AI-SE sends:** deployment version, policy decision events, release timestamps.
- **AI-SE receives:** monitoring threshold updates and dashboard requirements.
- **Error handling:** missing required telemetry fields triggers non-compliant release alert.

### Contract D: AI-SE <-> AI-PM (Scope and governance traceability)
- **Format:** release evidence packet + milestone status.
- **AI-SE sends:** release notes, risks, gate pass/fail, rollback readiness.
- **AI-SE receives:** scope priority changes and board reporting deadlines.
- **Error handling:** unresolved critical risk escalates before release approval.

---

## 7. Observability and Audit Requirements

Minimum structured fields per policy decision event:
- `timestamp_utc`
- `environment`
- `release_version`
- `query_hash`
- `decision`
- `policy`
- `rule_id`
- `reason`
- `escalated_to`

Operational targets:
- Decision log coverage: >= 95 percent of interactions.
- Policy engine error alerting: under 5 minutes.
- Reconstruct one incident trail: under 24 hours.

---

## 8. CI/CD Governance Gates (AI-SE ownership)

A release is blocked if any gate fails:

1. Policy YAML schema validation fails.
2. Policy regression tests fail (PII block, low confidence escalation, out-of-scope handling).
3. Required audit fields are missing from test output.
4. Rollback procedure is not validated for the target environment.

---

## 9. Risks and Mitigations

- **Risk:** CI/CD exists but does not gate policy changes.
  - **Mitigation:** enforce policy validation as mandatory release gate.
- **Risk:** Log schema incomplete for compliance evidence.
  - **Mitigation:** define and validate required event fields in CI tests.
- **Risk:** On-prem performance bottlenecks delay releases.
  - **Mitigation:** include deployment smoke tests and clear rollback thresholds.
- **Risk:** Contract mismatch between roles.
  - **Mitigation:** use explicit interface contract fields and confirm in checkpoint reviews.

---

## 10. Delivery Plan (Day 13 to Day 14 bridge)

- Finalize interface contracts with FDE, AI-SEC, and AI-DA.
- Run self-check on PEP placement, logs, and constraints.
- Carry unresolved gaps into Day 14 governance artifacts.

---

## 11. Day 13 Self-Review Checklist

- [x] PEP is explicitly placed before response delivery.
- [x] Audit log requirements are defined.
- [x] At least 2 interface contracts are specified (4 included).
- [x] On-prem, budget, and language constraints are addressed.
- [x] CI/CD policy validation gate is mandatory.
