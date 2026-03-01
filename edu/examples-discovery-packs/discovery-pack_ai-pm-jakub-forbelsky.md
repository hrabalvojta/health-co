# Discovery Packet v1 --- AI-PM

## Student: \Jakub Forbelsky

## Date: February 23, 2026

## Client: EuroHealth Insurance AG

------------------------------------------------------------------------

## Part 1: Discovery Questions (10)

### Question 1: Where is ServiceNow + Moveworks falling short today --- governance, scaling, or regulatory readiness?

**Why this matters:** If AI capabilities already exist, we must identify
the governance or scaling gaps preventing enterprise-wide
industrialization. **Red flag (bad answer):** "We're mostly fine, just
optimizing." → Indicates unclear strategic objective. **KAF component:**
Core / Run Safe

### Question 2: Who owns AI governance today, and is it operationalized or just documented?

**Why this matters:** EU AI Act readiness requires clear accountability
and enforceable controls. **Red flag:** "IT handles it." → No defined AI
governance structure. **KAF component:** Policy-as-Code

### Question 3: Which AI rules must be technically enforced in code (e.g., no PII usage, approval before auto-resolution)?

**Why this matters:** Determines scope of Policy-as-Code and automation
guardrails. **Red flag:** "We rely on teams to follow policy." →
Compliance risk. **KAF component:** Policy-as-Code

### Question 4: How long does it take to implement regulatory or policy changes in production systems?

**Why this matters:** Measures operational maturity and EU AI Act
adaptability. **Red flag:** "Usually months." → Slow adaptation risk.
**KAF component:** Run Safe

### Question 5: Beyond IT, which departments are next for AI rollout --- and what could block scaling?

**Why this matters:** Industrialization requires cross-department
readiness. **Red flag:** "We'll decide later." → No scaling roadmap.
**KAF component:** Core / Interop

### Question 6: What audit depth does the board expect --- full conversation replay, decision traceability, model version logs?

**Why this matters:** Determines Digital Trust architecture needs. **Red
flag:** "Basic logs are enough." → Likely insufficient for regulatory
audits. **KAF component:** Run Safe

### Question 7: Where must humans remain in the loop, and at what risk threshold?

**Why this matters:** Prevents over-automation in regulated workflows.
**Red flag:** "We want full automation." → Compliance exposure risk.
**KAF component:** HITL

### Question 8: What systems must the AI agent integrate with beyond ServiceNow?

**Why this matters:** Defines interoperability (MCP connectors) and
agentic workflow scope. **Red flag:** "We'll integrate later." →
Underestimated complexity. **KAF component:** Interop

### Question 9: What are the board-level success metrics --- cost reduction, compliance readiness, CSAT?

**Why this matters:** Aligns program with strategic priorities. **Red
flag:** Only operational metrics mentioned. **KAF component:** Core

### Question 10: How is the €180K budget structured --- pilot funding or transformation funding?

**Why this matters:** Determines scalability and governance investment
capacity. **Red flag:** Fixed budget with flexible scope. **KAF
component:** Core

------------------------------------------------------------------------

## Part 2: KAF Mapping (mini)

  KAF Component       Covered by Q#   Notes
  ------------------- --------------- ----------------------------
  Agentic Core        1,5,9,10        Business alignment & scale
  Agentic Ingestion   8               Integration landscape
  Policy-as-Code      2,3             Governance enforceability
  Digital Trust       6               Audit & traceability
  Human-in-the-Loop   7               Risk threshold control
  Interop (MCP/A2A)   8               Tool integration

------------------------------------------------------------------------

## Part 3: Assumptions / Risks / Open Items (3)

1.  **Risk: Governance exists on paper, not in enforceable controls.**\
    Without Policy-as-Code, EU AI Act readiness is unrealistic.

2.  **Risk: Regulatory adaptation is slow.**\
    If system changes take months, compliance cannot keep pace with
    evolving EU requirements.

3.  **Assumption: Board priority is risk reduction, not only cost
    savings.**\
    If incorrect, positioning and KPIs must shift toward ROI narrative.

------------------------------------------------------------------------

## Part 4: What We Will Measure (3 KPI Proposals)

1.  **L1 Auto-Resolution Rate**\
    Target: 50% of L1 tickets automated.

2.  **Governance Coverage (Policy-as-Code Implementation)**\
    Target: 100% of production AI workflows governed by enforceable
    controls.

3.  **Regulatory Adaptation Speed**\
    Target: \<14 days to implement approved policy changes in production
    workflows.

------------------------------------------------------------------------

## Part 5: Agent Classification

-   **Governance tier:** Enterprise\
-   **Registry/reuse potential:** Register as governed enterprise AI
    agent template for future Kyndryl regulated clients.

------------------------------------------------------------------------

## Dependencies on Other Roles:

-   Need AI-SEC to validate compliance and security posture.
-   Need FDE to assess on-prem infrastructure and integration
    feasibility.
-   Need AI-SE to confirm deployment and monitoring maturity.
-   Need AI-DS to validate data quality and knowledge base readiness.

## Questions I Deliberately Did NOT Ask (and why):

-   Detailed infrastructure architecture --- FDE responsibility.
-   Model evaluation metrics --- AI-DS responsibility.
-   Security threat modeling depth --- AI-SEC responsibility.

## Master single question for the CEO before project start:

- When you say you want to industrialize the AI helpdesk — not just deploy another chatbot — what business outcome and governance outcome must be  true in 6 months for you to personally tell the board this succeeded, specifically in terms of eliminating shadow AI and establishing a single,  auditable standard across EN, DE, and CZ?