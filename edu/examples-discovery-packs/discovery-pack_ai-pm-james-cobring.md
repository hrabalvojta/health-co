# Discovery Packet v1 --- AI-PM (Discovery Lead)

## Student

James Cobring

## Date

February 23, 2026

## Client

EuroHealth Insurance AG

------------------------------------------------------------------------

# Part 1: Discovery Questions (10)

## Question 1

**You already have ServiceNow with Moveworks. Specifically, what
governance, policy, or cross-department limitations do you hit when
trying to scale AI across claims, policy, and customer-support teams
that you can't solve with Moveworks alone?**

**Why this matters:**\
Pinpoints gaps beyond the existing chatbot and frames industrialization
(governance, cross-department orchestration).

**Red flag (bad answer):**\
Only cites feature gaps or onboarding issues; no mention of policy
enforcement, auditability, or cross-tool orchestration.

**KAF component:** Policy-as-Code / Interop

------------------------------------------------------------------------

## Question 2

**Which rules must be codified as policy-as-code (e.g., data access
controls, PII handling, retention, model usage constraints), and who
must approve each rule before it can be enforced automatically?**

**Why this matters:**\
Tests readiness for machine-enforceable controls and establishes clear
governance ownership.

**Red flag (bad answer):**\
Policies exist only in documents; no automation or formal approvals.

**KAF component:** Policy-as-Code / Interop

------------------------------------------------------------------------

## Question 3

**When regulations or internal policies change, how quickly can your
organization implement the change in AI governance and workflows---days,
weeks, or months? What has limited speed in the past?**

**Why this matters:**\
Measures operational maturity and speed to compliance before Dec 2027.

**Red flag (bad answer):**\
Responses framed as politics or meetings rather than process lead times
or concrete bottlenecks.

**KAF component:** Run Safe / Policy-as-Code

------------------------------------------------------------------------

## Question 4

**For a typical service request, can you walk me through the end-to-end
agent planning steps and decision gates, including the exact tools and
integrations required (and which MCP connectors you'll rely on)?**

**Why this matters:**\
Reveals concrete execution plan and integration dependencies.

**Red flag (bad answer):**\
Vague steps; reliance on "whatever tools we have" without defined MCP
connectors.

**KAF component:** Interop / Agent Builder

------------------------------------------------------------------------

## Question 5

**What are your mandatory audit, logging, and monitoring requirements
for the AI platform, and who owns the runbooks and incident-response
procedures? How will these be tested on-prem?**

**Why this matters:**\
Directly ties to Run Safe, accountability, and on-prem constraints.

**Red flag (bad answer):**\
Logs exist but ownership or testability is unclear; monitoring is
fragmented.

**KAF component:** Run Safe / Interop

------------------------------------------------------------------------

## Question 6

**Where do you want human-in-the-loop checkpoints to occur (risk
decisions, data-exception handling, customer-impact events), and which
roles or teams should perform them?**

**Why this matters:**\
Establishes concrete HITL governance and avoids ambiguity about
responsibility.

**Red flag (bad answer):**\
HITL is implied but no assigned roles or escalation paths.

**KAF component:** HITL / Interop

------------------------------------------------------------------------

## Question 7

**From an infrastructure perspective, what are your required hosting
models, on-prem constraints, and API integration constraints that would
limit AI model deployment and renewal?**

**Why this matters:**\
Targets concrete hosting and API constraints early; aligns with on-prem
mandate.

**Red flag (bad answer):**\
Vague hosting preferences or unbounded API expectations.

**KAF component:** Core / Interop

------------------------------------------------------------------------

## Question 8

**What are your current CI/CD, deployment guardrails, and monitoring
requirements for AI components in production, given on-prem and audit
needs?**

**Why this matters:**\
Pins down deployment automation and governance fit; critical for
production readiness.

**Red flag (bad answer):**\
No defined gates or measurable monitoring metrics.

**KAF component:** Policy-as-Code / Run Safe

------------------------------------------------------------------------

## Question 9

**Which three success metrics would you need to see to declare the
EuroHealth AI platform industrialized (governed, auditable, on-prem, EU
Act-ready) and deliver measurable business value? Tie to the brief:
CSAT, deflection, misroutes, productivity.**

**Why this matters:**\
Directly links governance progress to business outcomes and provides
clear exit criteria.

**Red flag (bad answer):**\
Vague or internally focused metrics without tying to customer outcomes
or the budget.

**KAF component:** Interop / Run Safe

------------------------------------------------------------------------

## Question 10

**How would you ensure production safety and user trust when introducing
an on-prem AI platform in claims/support workflows (auditable prompts,
transparency indicators, and escalation readiness)?**

**Why this matters:**\
Addresses Digital Trust and customer-facing safety requirements in the
EU context.

**Red flag (bad answer):**\
Trust features are "nice to have" or not testable pre-production.

**KAF component:** Run Safe / Policy-as-Code

------------------------------------------------------------------------

> **Minimum coverage ensured:**\
> - ≥ 2 questions on Policy-as-Code\
> - ≥ 1 on MCP/A2A interoperability\
> - ≥ 1 on Human-in-the-Loop\
> - ≥ 1 on Run Safe / Digital Trust\
> - Explicit business outcomes KPIs in Question 9

------------------------------------------------------------------------

# Part 2: KAF Mapping (Mini)

  ---------------------------------------------------------------------------
  KAF Component                       Covered by Q#            Notes
  ----------------------------------- ------------------------ --------------
  Agentic Core                        4, 7                     End-to-end
                                                               workflow &
                                                               hosting

  Agentic Ingestion                   4                        MCP connector
                                                               expectations

  Policy-as-Code                      2, 8, 10                 Codified rules
                                                               & audit
                                                               guardrails

  Digital Trust                       5, 10                    Audit,
                                                               monitoring &
                                                               transparency

  Human-in-the-Loop                   6                        Decision
                                                               checkpoints &
                                                               escalation

  Interop (MCP/A2A)                   1, 4, 9                  Cross-tool
                                                               governance &
                                                               connectors
  ---------------------------------------------------------------------------

------------------------------------------------------------------------

# Part 3: Assumptions / Risks / Open Items

-   **Assumption:** Moveworks will continue to handle day-to-day chatbot
    tasks; value lies in governance and industrialization across tools.\
-   **Risk:** Policy-as-Code approvals may become a bottleneck if
    ownership is unclear.
    -   *Mitigation:* Predefine RACI in ADR.\
-   **Open Item:** Identify MCP connectors required for critical flows
    (claims, policy, support) and define SSO identity boundaries
    on-prem.

------------------------------------------------------------------------

# Part 4: What We Will Measure (KPI Proposals)

-   **Deflection rate:** ≥ 40--50% for Tier-1 inquiries after
    industrialization.\
-   **Misroute reduction:** ≤ 5--10% escalations due to policy
    violations or misinterpretations.\
-   **CSAT delta:** Improve from 3.2--3.6 to 4.0+ within 6 months.

**Notes:**\
Tie KPIs to the client brief:\
- On-prem requirement\
- 8-week delivery\
- €180K budget\
- EU AI Act readiness by Dec 2027\
- Cross-department scaling\
- Governance industrialization

------------------------------------------------------------------------

# Part 5: Agent Classification

-   **Governance tier:** Enterprise\
-   **Registry/reuse potential:** Register as
    `EuroHealth-Prod-Industrialization-01`; reusable across lines after
    governance validation under policy gate with audit trails.

------------------------------------------------------------------------

# Dependencies on Other Roles

-   I need **AI-SEC** to discuss policy controls and threat-model
    boundaries (policy enforcement & audit obligations drive
    Policy-as-Code).\
-   I need **AI-PM** to align KPI targets with business priorities and
    budget constraints.\
-   I need **AI-FE** to validate user-experience implications of trust
    indicators and accessibility in the UI.

------------------------------------------------------------------------

# Questions I Deliberately Did NOT Ask (and why)

-   "What tech stack do you use beyond ServiceNow?" --- Already known;
    focus is governance, connectors, and industrialization, not stack
    inventory.

------------------------------------------------------------------------

# Notes for the Day 11--12 Discovery Sprint

-   Use these questions in a 1:1 with CIO Hans Muller.\
-   Map responses into ADRs (Architecture Decision Records) and FRIA
    where applicable.\
-   Surface shadow AI risks (HR chatbot, Claims PoC, Finance GPT) to
    align with CISO concerns and the board's governance narrative.\
-   Convert findings into a go/no-go decision input for Day 15.
