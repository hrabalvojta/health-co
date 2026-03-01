# Rollback and Incident Playbook - AI-SE
## Date: February 26, 2026
## Scope: EuroHealth AI Helpdesk runtime and release incidents
## Owner: AI-SE

This playbook defines deterministic actions when a release introduces unsafe behavior,
policy enforcement failure, or unacceptable service degradation.

---

## 1. Incident Classes

| Severity | Trigger | Target Response Time | Business Impact |
|---|---|---|---|
| SEV-1 | PII leak risk, policy bypass, widespread incorrect decisions | 15 minutes | Regulatory and board-level exposure |
| SEV-2 | Escalation path broken, high error rate, major latency regression | 30 minutes | Service instability with user impact |
| SEV-3 | Non-critical defect with workaround | 4 hours | Limited impact |

---

## 2. First 15 Minutes (SEV-1)

1. Declare incident in operations channel and open incident ticket.
2. Freeze new deployments.
3. Shift traffic to last known stable release.
4. Force fail-safe policy mode (block/escalate) if decision integrity is uncertain.
5. Notify AI-PM, AI-SEC, FDE, AI-DA using escalation matrix.
6. Start evidence capture window (logs, timestamps, release IDs).

---

## 3. Rollback Procedure (release failure)

### Preconditions

- Previous stable image/version is available.
- Rollback command was dry-run tested in test environment.
- Incident commander assigned.

### Execution Steps

1. Identify bad release: version tag, commit ID, deployment timestamp.
2. Stop progressive rollout for bad release.
3. Deploy previous stable release package.
4. Run smoke checks:
   - policy engine decision path responds,
   - audit event writing succeeds,
   - escalation endpoint reachable.
5. Confirm key KPI recovery (error rate, decision latency, escalation health).
6. Publish rollback completion record.

### Rollback Completion Criteria

- User-facing error rate back within baseline.
- Policy decision engine healthy.
- Audit fields complete in new events.
- Incident owner and AI-SEC approve stabilization.

---

## 4. Evidence Capture Requirements

For every SEV-1 or rollback event, capture:

- incident_id
- release_version (failed and restored)
- decision impact summary
- start/end UTC timestamps
- affected environments
- mitigation actions with actor names
- validation evidence after rollback

Evidence locations:

- `audit.log`
- release gate report for impacted release
- incident ticket export

---

## 5. Communication Matrix

| Role | Responsibility during incident |
|---|---|
| AI-SE | Incident command for release/rollback actions |
| AI-SEC | Security/compliance risk assessment and containment |
| FDE | Runtime infrastructure validation and recovery |
| AI-DA | Monitoring confirmation and KPI recovery evidence |
| AI-PM | Stakeholder communication and decision escalation |

---

## 6. Post-Incident Review (within 24 hours)

1. Root cause category (policy, code, infra, process, data).
2. Why release gates did not block this failure.
3. Corrective action owner and due date.
4. Required gate or schema update before next release.
5. Board-facing summary (if compliance-impacting).

---

## 7. Guardrail Policy

No emergency exception allows bypass of policy validation or audit capture.
If uncertain, prioritize block/escalate over permissive response.

