# EU AI Act — Risk Classification Assessment
## EuroHealth AI Helpdesk System

**Assessor:** AI-SEC
**Date:** <!-- -->
**Regulation:** EU AI Act (Regulation 2024/1689)

---

## 1. System Description

| Field | Value |
|-------|-------|
| System name | EuroHealth AI IT Helpdesk |
| Purpose | Automated L1 ticket resolution + intelligent routing |
| Users | 12 helpdesk agents + ~5,000 employees (end users) |
| Data processed | IT knowledge base, ticket metadata, employee queries |
| Deployment | On-premises (EuroHealth data center) |
| Autonomy level | Human-in-the-loop (agent reviews before escalation) |

## 2. Risk Tier Assessment

### 2.1 Is this an Unacceptable Risk system? (Article 5)

| Criterion | Applies? | Evidence |
|----------|---------|---------|
| Social scoring | ☐ No | System does not score individuals |
| Subliminal manipulation | ☐ No | System provides information, not persuasion |
| Exploitation of vulnerabilities | ☐ No | Employees are not a vulnerable group in this context |
| Real-time biometric identification | ☐ No | No biometric data processed |

**Conclusion:** ☐ NOT unacceptable risk

### 2.2 Is this a High-Risk system? (Article 6 + Annex III)

| Annex III Category | Applies? | Reasoning |
|-------------------|---------|-----------|
| Biometric systems | ☐ No | |
| Critical infrastructure | ☐ Possibly | <!-- Insurance is regulated; IT helpdesk may be operational support --> |
| Education/vocational training | ☐ No | |
| Employment & worker management | ☐ Possibly | <!-- Handles employee queries; could affect access to IT resources --> |
| Essential services access | ☐ Possibly | <!-- Employees depend on IT access for their work --> |
| Law enforcement | ☐ No | |
| Migration/border control | ☐ No | |
| Administration of justice | ☐ No | |

**Assessment:**
<!-- AI-SEC: Is this High-Risk? Justify your determination. -->
<!-- Consider: the system handles employee PII, makes routing decisions, affects service access -->

### 2.3 If High-Risk — Required Obligations

| Obligation | Article | Status | Implementation |
|-----------|---------|--------|---------------|
| Risk management system | Art. 9 | ☐ | Risk register + monitoring |
| Data governance | Art. 10 | ☐ | KB quality audit + PII controls |
| Technical documentation | Art. 11 | ☐ | Solution Design + Governance Charter |
| Record-keeping (logging) | Art. 12 | ☐ | Audit logger + retention policy |
| Transparency | Art. 13 | ☐ | User notification ("AI-assisted") |
| Human oversight | Art. 14 | ☐ | HITL protocol + override |
| Accuracy, robustness, security | Art. 15 | ☐ | Golden dataset + security testing |

## 3. GPAI (General Purpose AI) Considerations

| Question | Answer |
|----------|--------|
| Are we using a GPAI model? | <!-- Yes — on-prem LLM (e.g., Llama) --> |
| Is the GPAI provider compliant? | <!-- Provider obligations vs. deployer obligations --> |
| Do we need to document model capabilities/limitations? | <!-- --> |

## 4. Timeline to Compliance

| Milestone | Target Date | Owner |
|----------|------------|-------|
| Risk classification confirmed | <!-- Week 1 --> | AI-SEC |
| Evidence pack scope defined | <!-- Week 2 --> | AI-SEC + AI-PM |
| Technical documentation complete | <!-- Month 3 --> | ALL |
| Audit trail operational | <!-- Month 2 --> | AI-SE |
| Human oversight protocol active | <!-- Month 2 --> | AI-PM + AI-FE |
| Board-ready evidence pack | <!-- Month 5 --> | AI-PM + AI-SEC |

## 5. Sign-off

| Role | Determination | Name | Date |
|------|-------------|------|------|
| AI-SEC | Risk tier: <!-- High / Limited / Minimal --> | | |
| CISO | Review | Stefan Weber | |
| AI-PM | Acknowledged | | |
