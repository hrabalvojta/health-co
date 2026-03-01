# Discovery Packet v2 --- AI Solutions Engineer (AI-SE)

## Date: February 23, 2026

## Client: EuroHealth Insurance AG

## Engagement: AI Industrialization (Governance, Scaling, Production Ops)

------------------------------------------------------------------------

# Part 1: Discovery Questions (10)

## Question 1: What AI-related risks are currently preventing you from scaling beyond your existing ServiceNow/Moveworks deployments?

**Why this matters:** Identifies governance and operational blockers
limiting scale. Reveals what ServiceNow alone cannot solve. **Red
flag:** "We're not sure" or "Security is reviewing it" → no centralized
AI risk ownership. **KAF component:** Core / Run Safe

------------------------------------------------------------------------

## Question 2: If the EU AI Act audit occurred tomorrow, where would you lack documentation, traceability, or explainability?

**Why this matters:** Tests readiness for lifecycle logging, risk
classification, and compliance automation. **Red flag:** "We'll prepare
closer to the deadline." **KAF component:** Core / Run Safe

------------------------------------------------------------------------

## Question 3: Which AI governance policies are documented but NOT technically enforceable in your systems today?

**Why this matters:** Surfaces Policy-as-Code opportunities (confidence
thresholds, approval gates, PII controls). **Red flag:** Governance
exists only in PDFs/manual workflows. **KAF component:** Policy-as-Code

------------------------------------------------------------------------

## Question 4: When regulations or internal compliance policies change, how long does it take to update AI workflows in production?

**Why this matters:** Measures deployment agility and CI/CD maturity for
policy updates. **Red flag:** "Several months" → brittle deployment
model. **KAF component:** Core / Run Safe

------------------------------------------------------------------------

## Question 5: What human approval checkpoints are mandatory before an AI-driven action is executed?

**Why this matters:** Defines HITL boundaries and accountability under
EU AI Act. **Red flag:** No defined human-in-the-loop governance model.
**KAF component:** Human-in-the-Loop

------------------------------------------------------------------------

## Question 6: What systems beyond ServiceNow must AI workflows integrate with to complete end-to-end processes?

**Why this matters:** Identifies MCP connector needs, API maturity, and
orchestration complexity. **Red flag:** Legacy systems without APIs.
**KAF component:** Interop

------------------------------------------------------------------------

## Question 7: How do you currently monitor AI performance in production (confidence tracking, drift detection, incident response)?

**Why this matters:** Industrial AI requires monitoring comparable to
critical IT systems. **Red flag:** Sole reliance on vendor monitoring.
**KAF component:** Run Safe

------------------------------------------------------------------------

## Question 8: How do you ensure no PII enters training or retrieval pipelines, especially in an on-prem environment?

**Why this matters:** Critical for GDPR compliance and auditability.
**Red flag:** Manual anonymization processes without logging. **KAF
component:** Ingestion / Policy-as-Code

------------------------------------------------------------------------

## Question 9: Do you use CI/CD pipelines for AI prompts, policies, workflows, and configurations --- or are changes made directly in production?

**Why this matters:** Ensures versioning, rollback, environment
separation, and deployment governance. **Red flag:** Direct changes in
production without approval workflows. **KAF component:** Core / Run
Safe

------------------------------------------------------------------------

## Question 10: If we scale from 3 AI use cases to 25 across departments, what operational bottleneck would fail first?

**Why this matters:** Reveals constraints in governance, infrastructure,
skill capacity, or budget. **Red flag:** No scaling roadmap defined.
**KAF component:** Core / Interop

------------------------------------------------------------------------

# Part 2: KAF Coverage Summary

  KAF Component       Covered by Questions
  ------------------- ----------------------
  Agentic Core        1, 2, 4, 9, 10
  Agentic Ingestion   8
  Policy-as-Code      3, 8
  Digital Trust       1, 2, 4, 7, 9
  Human-in-the-Loop   5
  Interop (MCP/A2A)   6, 10

------------------------------------------------------------------------

# Part 3: Assumptions / Risks / Open Items

1.  Current governance framework may not meet EU AI Act audit standards.
2.  Policy updates may not be deployable via automated CI/CD.
3.  Integration maturity of legacy systems is unclear.
4.  PII filtering may not be technically enforceable today.
5.  Monitoring and incident response processes may rely heavily on
    vendors.

------------------------------------------------------------------------

# Part 4: Proposed KPIs

1.  Policy update deployment time: \< 5 business days
2.  Full AI action audit traceability: 100%
3.  Production incident detection time: \< 15 minutes
4.  Governance rule enforcement coverage: 100% automated
5.  Scale readiness: Support 10x use case growth without infra redesign

------------------------------------------------------------------------

# Part 5: Agent Classification

-   Governance Tier: Enterprise
-   Registry/Reuse Potential: Reusable AI governance and monitoring
    framework deployable across EU-regulated clients.

------------------------------------------------------------------------

# Dependencies on Other Roles

-   I need **AI-SEC** to assess current security posture, IAM controls,
    and threat modeling because deployment governance depends on
    enforceable security baselines.
-   I need **AI-DS** to validate knowledge base quality and PII
    classification mechanisms because ingestion governance affects
    deployment safety.
-   I need **FDE** to clarify infrastructure constraints (on-prem LLM
    hosting, API gateways, network segmentation) because CI/CD
    architecture depends on infra readiness.
-   I need **AI-PM** to confirm board-level governance expectations and
    budget flexibility because rollout phasing impacts deployment
    sequencing.
-   I need **AI-DA** to define reporting dashboards for audit logs and
    KPIs because monitoring instrumentation must align with reporting
    requirements.

------------------------------------------------------------------------

# Questions I Deliberately Did NOT Ask (and Why)

-   "What business KPIs define success?" --- AI-PM territory (business
    prioritization).
-   "How clean and structured is your knowledge base?" --- AI-DS
    territory (data quality focus).
-   "What is your threat landscape and incident history?" --- AI-SEC
    territory (security risk).
-   "What UI experience do end users expect?" --- AI-FE territory
    (front-end & accessibility).
-   "What detailed infrastructure topology do you run today?" --- FDE
    territory (hosting & networking deep-dive).

------------------------------------------------------------------------

Prepared for: CIO Discovery Meeting\
Prepared by: AI Solutions Engineer (Kyndryl AI Consulting)
