# EuroHealth AI Helpdesk Platform

## Discovery Report -- AI-FE (AI Front-End Engineer)

------------------------------------------------------------------------

# Executive Summary

This engagement is not a chatbot deployment. It is a governed AI
platform industrialization initiative with a fixed August board
deadline.

Hans's explicit KPI is a 30% helpdesk cost reduction within six months.\
His implicit KPI is board-defensible control: a unified, auditable, EU
AI Act--ready AI platform replacing fragmented shadow tools.

UX decisions directly influence:

-   Adoption rate (primary driver of the 30% cost target)
-   Governance visibility (board confidence KPI)
-   Regulatory defensibility (August milestone)
-   Perception of platform unification across 8 EU countries

If agents do not trust or use the system, auto-resolution will not
scale.\
If governance is not visibly demonstrable in the interface, board
confidence will not materialize.

Therefore, AI-FE is not delivering a chat window.\
AI-FE is delivering the visible proof of control, compliance, and
measurable AI performance.

------------------------------------------------------------------------

# 1. Stakeholder & Power Analysis

## Primary Operational Stakeholder

**Jan + 12 Helpdesk Agents** - Fear displacement - Control daily L2
monitoring and overrides - Adoption behavior directly determines 30% KPI
outcome

## Executive Sponsor

**Hans Muller (CIO)** - August board milestone - Needs repeatable
governance narrative - Personal credibility tied to compliance readiness

## Veto Authority

**Stefan (CISO)** - EU AI Act classification authority - Can halt
rollout if explainability or logging insufficient

## Operational Gatekeeper

**Katarina (IT Ops)** - Owns ServiceNow environment - Controls rollout
feasibility and operational readiness

## Political Resistance Vector

**Shadow AI Owners (HR / Claims)** - May resist consolidation due to
loss of autonomy - Risk of silent non-adoption or parallel tool
continuation

Strategic implication: platform unification creates internal friction.\
UX must reinforce "official unified platform" legitimacy.

------------------------------------------------------------------------

# 2. Structural Discovery Insights & Implications

## 2.1 Platform Fragmentation → Identity & Governance Surface

Hans: "Everyone's doing their own thing."

Implication: The interface must clearly communicate:

-   Which AI system is responding
-   Whether it is approved
-   Which policy/version governs it

Architectural requirement: Multi-agent metadata contract exposing: -
Agent ID - Policy version - Approval status - Ownership

This transforms UX into governance instrumentation.

------------------------------------------------------------------------

## 2.2 ServiceNow Integration → Trust Through State Clarity

Integration exists but is untested.

UX must clearly separate: - "AI Suggested Resolution" - "Official Ticket
Record"

Required backend contracts: - API acknowledgment responses - Error codes
exposed to FE - p95 latency benchmarks - Streaming protocol agreement

Failure-state design directly impacts adoption trust.

------------------------------------------------------------------------

## 2.3 Knowledge Base Quality → Golden Dataset Dependency

Hans: "About a third of the knowledge base is garbage."

Primary risk: early trust erosion.

Mitigation must be systemic, not cosmetic:

UI must display: - Source citation - Last updated timestamp - Confidence
indicator - "Report incorrect answer" trigger

Critical addition: Confidence indicators must be grounded in a validated
golden dataset benchmark.

Without benchmarked accuracy: - Confidence scores are cosmetic -
Governance dashboards lack credibility - Board reporting becomes weak

Dependency: AI-DS must define golden dataset, benchmark accuracy
thresholds, and scoring schema powering UI indicators.

------------------------------------------------------------------------

## 2.4 On-Prem Constraint → Latency & Perception Management

On-prem architecture introduces potential latency variability.

UX must handle: - Progressive token streaming - Explicit loading
states - Timeout recovery - Double-submit prevention

Required technical inputs: - p95 token latency - Maximum response
payload size - Streaming chunk format

Streaming UX is perception engineering --- it shapes perceived
intelligence and reliability.

------------------------------------------------------------------------

## 2.5 30% Cost Reduction → Behavioral Design Lever

Cost reduction is not model performance.\
It is adoption performance.

Adoption requires: - Co-pilot framing - One-click override - Minimal
cognitive load - Clear human-in-control signaling

UX adoption metrics must align with AI-DA baseline ROI model.

------------------------------------------------------------------------

# 3. Regulatory Tier Conditional Design

If classified as High-Risk under EU AI Act:

UI must support: - Mandatory human confirmation before resolution -
Expanded audit trace visibility - Model and policy version exposure -
Explicit override logging

If Limited-Risk: - Suggestion-based interaction may be configurable

Frontend must remain adaptable to final classification.

------------------------------------------------------------------------

# 4. Multi-Surface Architecture

To balance governance and usability, the platform must separate:

1.  Agent Operational UI
    -   Fast L2 monitoring\
    -   Suggestion + override workflow
2.  Governance/Admin Dashboard
    -   Audit logs\
    -   Escalation routing metrics\
    -   Knowledge quality indicators
3.  Executive / Board View
    -   Auto-resolution rate vs baseline\
    -   Accuracy trend (golden dataset validated)\
    -   Governance coverage status\
    -   Compliance artifact readiness

Separation prevents governance overload while preserving transparency.

------------------------------------------------------------------------

# 5. Multilingual UX as Industrialization Lever

EN/DE/CZ support across 8 countries is not localization.\
It is a unification signal.

UI must: - Show answer language indicator - Expose source language
metadata - Allow controlled translation toggle - Surface cross-language
retrieval disclosure

Impact: Supports EU-wide governance optics and August board narrative.

------------------------------------------------------------------------

# 6. Go / No-Go Conditions

Preliminary delivery protection triggers:

-   If golden dataset benchmark accuracy \< agreed threshold →
    suggestion-only mode.
-   If p95 latency \> acceptable threshold → auto-resolution scope
    reduced.
-   If classified High-Risk → mandatory human confirmation enforced.

These protect adoption, ROI, and compliance timeline.

------------------------------------------------------------------------

# 7. Measurable AI-FE Success Criteria

Success for AI-FE means:

-   80% agent adoption by Month 3

-   Clear reduction in manual resolution handling time

-   Visible compliance artifact completeness by August

-   Confidence indicators validated against golden dataset benchmark

-   Governance dashboard reflecting measurable accuracy trend

UX must directly support board-reportable outcomes.

------------------------------------------------------------------------

# 8. Explicit Cross-Role Dependencies

AI-SEC: - Risk tier confirmation - Required visible compliance artifacts

FDE / AI-SE: - p95 latency benchmark - Streaming protocol contract -
Logging retention policy

AI-DS: - Golden dataset establishment - Confidence scoring schema -
Knowledge quality metrics

AI-DA: - Cost baseline definition - ROI measurement formula - Board KPI
structure

------------------------------------------------------------------------

# Conclusion

This engagement is a governed AI product launch with a fixed August
credibility deadline.

AI-FE ensures:

-   Governance visibility
-   Trust protection
-   Regulatory adaptability
-   ROI-aligned UX metrics
-   Multilingual unification
-   Board-defensible performance transparency

UX is not decoration.\
UX is commercial and political infrastructure.
