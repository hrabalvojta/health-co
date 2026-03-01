# Discovery Report

## EuroHealth Insurance AG

### Role: AI Data Analyst (AI-DA)

### Date: 2026-02-24

------------------------------------------------------------------------

# 1. Executive Summary

EuroHealth Insurance AG has already implemented AI tools
(Moveworks/ServiceNow AI) to automate basic helpdesk tickets. However,
governance is fragmented, shadow AI systems exist (HR chatbot, Claims
LangChain prototype), and there is no unified AI control framework.

The CIO's success criteria combine: - 30% reduction in remaining
helpdesk costs within 6 months - Consolidation under one AI governance
platform - On-premises-only deployment (non-negotiable) - EU AI Act
compliance by August 2026

From an AI-DA perspective, the central challenge is not model
performance --- it is measurement, auditability, governance evidence,
and adoption control.

------------------------------------------------------------------------

# 2. Stakeholder Analysis (AI-DA Perspective)

## Primary Sponsor

**Hans Muller (CIO)** - Needs measurable ROI - Must demonstrate
board-ready results - Under political pressure tied to project success

## Operational Stakeholders

**Jan (Helpdesk Lead) + 12 Agents** - Fear replacement - Critical for
adoption and KB quality - Potential data quality risk if disengaged

**HR Chatbot Owner** - Shadow AI system - Potential high-risk domain
(employee data)

**Claims Prototype Team** - Running LangChain prototype - Potential
regulatory exposure if decision-adjacent

## Governance & Assurance

-   Compliance / Legal / DPO
-   Security
-   Enterprise Architecture

------------------------------------------------------------------------

# 3. Key Findings & Implications

## 3.1 Shadow AI Proliferation

Multiple AI tools operating without central governance. **Implication:**
Immediate AI inventory and governance framework required.

## 3.2 On-Prem Only Constraint

No cloud services allowed. **Implication:** All logging, monitoring,
governance must function on-prem.

## 3.3 Knowledge Base Degradation (\~30% outdated)

No content owner. **Implication:** Automation scale will amplify
incorrect answers without remediation.

## 3.4 Workforce Resistance Risk

Helpdesk agents fear replacement. **Implication:** Adoption metrics must
be tracked alongside cost metrics.

------------------------------------------------------------------------

# 4. Technical / Functional Requirements (AI-DA Scope)

## Governance KPIs

-   Override rate
-   Escalation accuracy
-   Policy violation rate
-   Audit completeness
-   AI inventory coverage

## Operational KPIs

-   Automation rate by category
-   MTTR
-   First-contact resolution
-   Reopen rate
-   User trust score

## Audit Logging Requirements

Each AI decision must log: - Input context - Prompt template + version -
Model + version - Retrieved sources - Output - Confidence level - Human
override (if applicable) - Ticket outcome

Logs must be: - Retained per compliance requirements - Immutable -
Role-access controlled - Exportable for audits

------------------------------------------------------------------------

# 5. Risks (AI-DA Specific)

  Risk                             Impact
  -------------------------------- -----------------------------------
  Over-optimization on cost KPIs   Governance gaps and audit failure
  Knowledge base decay             Incorrect automation at scale
  Shadow AI growth                 Fragmented compliance exposure
  On-prem tooling limitations      Logging/monitoring gaps
  Workforce disengagement          Data quality degradation

------------------------------------------------------------------------

# 6. Recommended Next Steps (First 2 Weeks)

## Week 1

1.  Complete AI system inventory across departments.
2.  Assess existing logging capabilities per system.
3.  Define autonomy levels and human-in-the-loop rules.
4.  Assign interim knowledge base ownership.

## Week 2

1.  Define Minimum Viable Governance KPI framework.
2.  Design on-prem logging architecture.
3.  Propose shadow AI registration policy.
4.  Align change management plan with helpdesk leadership.

------------------------------------------------------------------------

# 7. Dependencies on Other Roles

-   **AI-SEC:** Log integrity, access controls, compliance alignment.
-   **AI-SE:** On-prem deployment feasibility, logging pipeline
    implementation.
-   **AI-PM:** Scope control, milestone alignment, stakeholder
    communication.
-   **FDE:** Target governance architecture design.
-   **AI-DS:** Evaluation methodology and quality validation framework.

------------------------------------------------------------------------

# 8. Conclusion

EuroHealth's challenge is not building new AI --- it is industrializing
and governing existing AI.\
The AI-DA workstream provides the measurement layer that transforms AI
from experimentation into a controllable, auditable, and defensible
business asset.
