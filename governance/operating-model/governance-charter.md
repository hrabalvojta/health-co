# Governance Charter - EuroHealth AI Helpdesk
## Version: 1.0.0
## Date: February 26, 2026
## Context: Day 14 governance deliverable (AI-SE contribution)

---

## 1. Purpose

Define decision rights, escalation paths, and control ownership for a high-risk,
on-prem AI helpdesk platform operating under EU AI Act obligations.

---

## 2. Governance Scope

- AI release lifecycle (model, prompt, policy, deployment config)
- Policy enforcement and runtime decision integrity
- Record-keeping and evidence readiness
- Human oversight and incident escalation

---

## 3. Decision Rights Matrix

| Decision Area | Decides | Consulted | Informed | SLA | EU AI Act Link |
|---|---|---|---|---|---|
| Production release approval | AI-PM | AI-SE, AI-SEC, FDE | AI-DA, AI-DS, AI-FE | <= 4h from gate completion | Art. 11, Art. 12 |
| Technical release gate status | AI-SE | AI-SEC, AI-DS | AI-PM, FDE | <= 1h after CI completion | Art. 11 |
| Policy schema acceptance | AI-SEC | AI-SE | AI-PM, FDE | <= 1 business day | Art. 9, Art. 12 |
| Emergency rollback trigger | AI-SE | FDE, AI-SEC | AI-PM, AI-DA | <= 15 min (SEV-1) | Art. 12, Art. 14 |
| Incident severity classification | AI-SEC | AI-SE, AI-PM | All role leads | <= 30 min | Art. 14 |
| Audit schema version update | AI-SE | AI-DA, AI-SEC | AI-PM | <= 2 business days | Art. 12 |

---

## 4. AI-SE Specific Governance Obligations

1. Enforce mandatory release gates before production deployment.
2. Maintain audit schema and ensure required fields are emitted.
3. Maintain rollback readiness and run periodic dry-runs.
4. Keep release traceability package for each promoted version.
5. Block release when policy validation or audit completeness is non-compliant.

---

## 5. Incident Response Protocol (charter level)

### SEV-1 Trigger Examples

- PII leakage risk detected
- Policy engine unavailable or bypassed
- Missing required audit evidence in production

### Escalation Chain

1. AI-SE opens incident and freezes deployments.
2. AI-SEC assesses compliance exposure.
3. FDE validates runtime stability and rollback target.
4. AI-PM coordinates stakeholder communications.
5. AI-DA confirms metric stabilization post-remediation.

---

## 6. Policy Change Process

1. Change request created with rule rationale and risk impact.
2. AI-SEC reviews policy intent and compliance implications.
3. AI-SE validates schema and CI compatibility.
4. Regression tests executed before merge.
5. Change promoted with release evidence and approver record.
6. Post-deploy monitoring confirms no regression.

No emergency policy change may skip logging or release traceability.

---

## 7. Human Oversight Integration

- Any uncertain or non-compliant runtime decision must route to human escalation.
- Override actions require identity, reason, and timestamp logging.
- Override frequency is reviewed weekly with AI-PM and AI-DA.

---

## 8. Review Cadence

- Weekly: release gates, incidents, override trends
- Bi-weekly: policy coverage and audit evidence quality
- Monthly: governance effectiveness review with CIO/CISO representation

---

## 9. Approval Block

- AI-PM:
- AI-SE:
- AI-SEC:
- FDE:
- Effective date:

