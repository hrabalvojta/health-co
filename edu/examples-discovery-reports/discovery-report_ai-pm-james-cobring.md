# Discovery Report (Day 12--13)

**Client:** EuroHealth Insurance AG\
**Perspective:** AI-PM (Discovery Lead)\
**Student:** James Cobring\
**Date:** February 23, 2026

------------------------------------------------------------------------

# 1. Stakeholder Analysis (Day 12 Perspective)

## Executive Sponsor

**Hans Muller -- CIO** - Under board pressure to demonstrate governance
readiness by August 2026\
- 6-month ROI expectation\
- On-prem hosting and EU AI Act readiness are non-negotiable

## Compliance Authority

**Stefan Weber -- CISO** - Requires FRIA alignment\
- Demands robust data controls and auditable logs\
- Enforces multilingual (EN/DE/CZ) governance compliance

## Operational Owner

**Katarina Novak -- IT Operations Director** - Needs feasible on-prem
integration with ServiceNow\
- Requires centralized governance without operational disruption

## Adoption Risk Owner

**Jan Kovar -- Helpdesk Lead (12 agents)** - Fears job displacement\
- Requires Human-in-the-Loop (HITL), retraining, and transparent
rollout\
- Critical for adoption across \~300 users

## End Users (\~300 across EN/DE/CZ)

-   Expect faster resolutions\
-   Require consistent multilingual knowledge\
-   Depend on reliable, unified platform behavior

## Shadow AI Stakeholders (HR, Claims, Finance)

-   Currently operating siloed AI tools\
-   Must be integrated into centralized governance\
-   Represent both compliance risk and scaling opportunity

------------------------------------------------------------------------

# 2. Key Findings & Implications for AI-PM Workstream

## Governance Is the Anchor

A centralized **policy-as-code backbone** with FRIA-aligned data lineage
is mandatory for: - Board-ready August 2026 reporting\
- Defensible compliance posture\
- Cross-department AI consolidation

## FRIA & EU AI Act Drive Architecture

Architecture must support: - Auditable logs\
- Risk controls\
- Multilingual governance artifacts\
- Board-ready compliance narrative

## Data Quality Is a Gating Factor

-   \~30% of Confluence KB is outdated\
-   Explicit ownership and remediation targets must precede workflow
    automation\
-   Governance without data quality will fail adoption

## On-Prem Is the Core Constraint

-   No cloud fallback available\
-   Gateway + ServiceNow integration must operate within €180K\
-   Renewal plan required from Day 1

## Change Management Is a Gating Risk

-   HITL framework required\
-   Transparent communication plan mandatory\
-   Retraining program needed to preserve morale and adoption

## ROI Depends on Governance Stabilization

The 30% cost reduction KPI is achievable **only after**: - Governance
consolidation\
- FRIA artifacts completion\
- Policy enforcement backbone stabilization

------------------------------------------------------------------------

# 3. Technical & Functional Requirements to Investigate

## 3.1 Policy Backbone

-   Centralized policy-as-code repository\
-   Cross-tool enforcement (Moveworks, ServiceNow, shadow AI)\
-   Auditable change history\
-   Real-time audit logs with export capability\
-   FRIA-aligned data processing map suitable for board review

## 3.2 FRIA & Governance Artifacts

-   Risk mapping tied to multilingual data flows\
-   Board-ready FRIA documentation pack\
-   Governance dashboard for executive reporting

## 3.3 Data Quality & Knowledge Governance

-   Baseline KB assessment across EN/DE/CZ\
-   8-week remediation target: \<10% outdated content\
-   Ownership matrix (claims, policy, customer support)\
-   End-to-end data lineage across all LLM components

## 3.4 On-Prem Gateway & Integrations

-   EN/DE/CZ language-capable gateway\
-   Certified ServiceNow connectors\
-   Hardware/licensing plan within €180K\
-   6-month renewal/upgrade roadmap\
-   Explicit confirmation: cloud not permitted

## 3.5 Compliance & Auditability

-   EU AI Act Art. 9--15 mapping\
-   Audit log schema and retention policy\
-   Incident response runbooks\
-   On-prem testing plan

## 3.6 Change Management & Enablement

-   Defined HITL framework\
-   Retraining plan for helpdesk agents\
-   Stakeholder communication cadence aligned with board milestones

------------------------------------------------------------------------

# 4. Risks (Day 12--13 Perspective)

-   **Regulatory Risk:** Failure to demonstrate FRIA alignment by August
    2026 could compromise compliance posture.\
-   **Governance Drift Risk:** Without centralized enforcement, shadow
    AI proliferation may persist across departments.\
-   **Data Quality Risk:** 30% outdated KB threatens automation accuracy
    and multilingual user trust.\
-   **On-Prem Risk:** Hardware miscalculation or licensing gaps could
    delay deployment and exceed €180K budget.\
-   **Change Management Risk:** Helpdesk resistance may reduce adoption
    without clear HITL and retraining.\
-   **Data Protection Risk:** Incomplete FRIA mapping across EN/DE/CZ
    could expose PII leakage vulnerabilities.\
-   **Interoperability Risk:** ServiceNow connector dependencies may
    introduce operational fragility.\
-   **Auditability Risk:** Incomplete logging or unclear runbook
    ownership may undermine board demonstrations.

------------------------------------------------------------------------

# 5. Next Steps (First 2 Weeks)

## Week 1

-   Confirm FRIA scope with CIO and CISO\
-   Lock risk categories for governance blueprint\
-   Draft centralized policy-as-code blueprint\
-   Develop initial data-flow maps\
-   Finalize on-prem gateway concept + hardware/licensing plan\
-   Establish KB remediation targets (\<10% outdated in 8 weeks)\
-   Define HITL and retraining plan for helpdesk

## Week 2

-   Produce FRIA-aligned risk control artifacts\
-   Draft governance dashboard prototype\
-   Create Phase 1 governance runbook\
-   Define auditable log schema\
-   Refine ROI narrative linking 30% cost reduction to auto-resolve
    targets\
-   Prepare Day 13 architecture artifacts (L4--L5 policy design, data
    lineage diagrams, ServiceNow integration specs)\
-   Develop stakeholder communication materials

------------------------------------------------------------------------

# 6. Cross-Role Dependencies

## AI-SEC

Required for: - EU AI Act classification guidance\
- FRIA artifacts (risk box, data maps)\
- Audit/logging standards

Impact: Defines governance scope and compliance boundaries driving
L4--L5 policy design.

## AI-FDE

Required for: - On-prem GPU sizing\
- Hardware cost validation\
- Licensing and renewal plan within €180K

Impact: Validates feasibility of 6-month ROI target and Phase 1 scope
realism.

## AI-DS

Required for: - KB quality assessment\
- Data remediation roadmap\
- Multilingual data lineage mapping

Impact: Anchors automation reliability and reduces FRIA/data-quality
risk exposure.
