# Discovery Report --- AI-SE

## Student: Radek Jelinek

## Role: AI Software Engineer

## Client: EuroHealth Insurance AG

## Context: Post-Roleplay (Hans Muller, CIO)

------------------------------------------------------------------------

## 1. Stakeholder Analysis (AI-SE Perspective)

**Hans Muller (CIO)** - Under board pressure to deliver 30% cost
reduction in 6 months. - Needs platform unification + EU AI Act
readiness. - Requires stable rollout and measurable progress reporting.

**Katarina Novak (IT Ops Lead)** - Owns infrastructure and ServiceNow
environment. - Key partner for on-prem deployment feasibility and CI/CD
integration.

**Stefan Weber (CISO)** - EU AI Act compliance driver. - Defines
logging, audit, and policy enforcement requirements.

**Jan Kovar (Helpdesk Lead) + 12 Agents** - Fear job displacement. -
Adoption risk if override mechanisms and transparency are weak.

------------------------------------------------------------------------

## 2. Key Findings from Roleplay

1.  This is an industrialization engagement, not a chatbot build.
2.  AI tools already exist (Moveworks, HR bot, Claims prototype) but
    lack governance.
3.  On-premises constraint is non-negotiable.
4.  Knowledge base quality (\~30% outdated) is a production risk.
5.  Regulatory readiness is both compliance requirement and board
    narrative.
6.  Budget (€180K / 6 months) may not include GPU hardware.

------------------------------------------------------------------------

## 3. Technical / Functional Requirements (AI-SE Workstream)

### Deployment Architecture

-   On-prem LLM hosting (model selection pending feasibility)
-   Containerized services (Docker/Podman)
-   Dev / Test / Prod separation
-   Internal container registry
-   ServiceNow API v2 integration (read + write)

### CI/CD

-   On-prem Git-based repository
-   Controlled environment promotion
-   Policy validation before deployment
-   Version tagging for auditability

### Monitoring & Logging

-   Prompt and output logging
-   Escalation tracking
-   Latency monitoring (\<2s target)
-   Immutable audit logs for compliance

### Rollback Strategy

-   Blue-green or canary deployment
-   Version snapshotting
-   One-click rollback capability

------------------------------------------------------------------------

## 4. AI-SE Risk Register

-   GPU capacity may be insufficient for target LLM size.
-   ServiceNow API integration may require custom middleware.
-   Logging architecture may not satisfy EU AI Act audit standards.
-   Knowledge base quality could degrade AI performance.
-   Budget may not cover infrastructure procurement.

------------------------------------------------------------------------

## 5. Recommended Next Steps (First 2 Weeks)

Week 1: - Validate ServiceNow API integration. - Conduct GPU and infra
feasibility check. - Draft logging and audit architecture. - Align with
AI-SEC on compliance classification.

Week 2: - Define CI/CD topology. - Select LLM hosting strategy. -
Produce hardware cost estimate for AI-PM. - Define rollback protocol and
deployment guardrails.

------------------------------------------------------------------------

## 6. Cross-Role Dependencies

-   AI-SEC: EU AI Act classification and logging requirements.
-   FDE: LLM model selection and hosting topology.
-   AI-DS: Knowledge base audit results.
-   AI-DA: KPI definition for monitoring dashboards.
-   AI-PM: Budget allocation and procurement approvals.

------------------------------------------------------------------------

## Autonomy Level

EuroHealth helpdesk = L2 (Constrained Agent) - Auto-resolves L1 tickets
within policy guardrails. - Human monitors and overrides when
necessary. - Never L3 (Autonomous) under EU AI Act context.

------------------------------------------------------------------------

## Summary

This engagement requires engineering a governed, production-safe,
on-prem AI deployment model that unifies fragmented AI systems under
enforceable compliance guardrails within strict budget and timeline
constraints.
