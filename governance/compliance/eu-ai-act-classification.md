# EU AI Act Classification - EuroHealth AI Helpdesk
## Date: February 26, 2026
## Classification Owner: AI-SE (with AI-SEC consultation)

---

## 1. Final Classification

**Proposed classification: HIGH-RISK**

Rationale:
- The system operates in an employee/workplace context and influences work-related ticket routing and outcomes.
- It supports decisions that can materially affect employees and service quality at scale.
- It runs across multiple EU countries and languages, increasing operational and compliance complexity.

---

## 2. Applicable Requirement Mapping (Art. 9-15 and Art. 50)

| Article | Requirement Theme | Primary Owner | Supporting Roles | Evidence Target |
|---|---|---|---|---|
| Art. 9 | Risk management | AI-SEC | AI-PM, AI-SE | Risk register and mitigation review trail |
| Art. 10 | Data and data governance | AI-DS | AI-SE, FDE | Data quality controls and evaluation evidence |
| Art. 11 | Technical documentation | AI-PM | AI-SE, FDE | Architecture docs and release traceability |
| Art. 12 | Record-keeping | AI-SE | AI-DA, AI-SEC | Audit log schema and event completeness evidence |
| Art. 13 | Transparency | AI-PM | AI-FE | User-facing and stakeholder transparency artifacts |
| Art. 14 | Human oversight | AI-FE | AI-SE, AI-PM | Override protocol and escalation traces |
| Art. 15 | Accuracy/robustness/cybersecurity | FDE | AI-SE, AI-SEC, AI-DS | Test evidence, reliability thresholds, incident controls |
| Art. 50 | AI system disclosure/transparency duties | AI-PM | AI-FE, AI-SEC | Disclosure and communication controls |

---

## 3. AI-SE Governance Gaps Identified

1. Audit schema is now defined but runtime emission is not yet fully aligned.
2. Release gate checklist exists but must be integrated into pipeline execution.
3. Rollback protocol exists but requires dry-run evidence cadence.

---

## 4. Immediate Actions

1. Validate runtime logs against `governance/evidence/audit-log-schema.json`.
2. Enforce release gates before next production promotion.
3. Execute rollback drill and store evidence in governance records.

