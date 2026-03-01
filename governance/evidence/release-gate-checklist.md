# Release Gate Checklist - AI-SE
## Date: February 26, 2026
## Scope: EuroHealth AI Helpdesk on-prem release governance
## Owner: AI-SE

This checklist defines mandatory controls before promoting any release to production.
A single failed gate blocks deployment.

---

## 1. Gate Matrix

| Gate ID | Control | Owner | Evidence | Pass Criteria | Block Severity |
|---|---|---|---|---|---|
| RG-01 | Policy schema validation | AI-SE + AI-SEC | `governance/evidence/audit-log-schema.json` and CI log | All policy files parse and pass schema checks | Critical |
| RG-02 | Policy regression tests | AI-DS + AI-SEC | `tests/test_policies.py` CI results | Required tests pass: PII block, confidence escalation, out-of-scope handling | Critical |
| RG-03 | Audit field completeness | AI-SE + AI-DA | Sample event validation report | Required fields present for all policy decisions | Critical |
| RG-04 | Release traceability | AI-SE | Release note + artifact hash list | Release includes version, commit, policy bundle hash, approvers | High |
| RG-05 | Rollback readiness | AI-SE + FDE | Rollback dry-run log | Rollback to prior stable version verified in test env | Critical |
| RG-06 | Human escalation readiness | AI-FE + AI-PM | Override path evidence | Override protocol exists and escalation contacts are active | High |
| RG-07 | Security exception check | AI-SEC | Risk waiver register | No unresolved critical exception for target release | Critical |

---

## 2. Pass/Fail Template (per release)

- Release version:
- Environment target:
- Gate reviewer set:
- Final decision: PASS / FAIL

| Gate ID | Status (PASS/FAIL) | Reviewer | Notes |
|---|---|---|---|
| RG-01 | | | |
| RG-02 | | | |
| RG-03 | | | |
| RG-04 | | | |
| RG-05 | | | |
| RG-06 | | | |
| RG-07 | | | |

---

## 3. Non-negotiable Blocking Rules

1. Do not deploy if policy validation fails.
2. Do not deploy if required audit fields are missing.
3. Do not deploy if rollback was not validated for this release train.
4. Do not deploy if critical security exceptions remain unresolved.

---

## 4. Sign-off

- AI-SE sign-off:
- AI-SEC sign-off:
- AI-PM sign-off:
- Deployment timestamp (UTC):

