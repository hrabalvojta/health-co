# Discovery Packet v1 --- AI-DA (AI Data Analyst)

## Student: Eva Závodská

## Date: February 23, 2026

## Client: EuroHealth Insurance AG

------------------------------------------------------------------------

# Part 1: Discovery Questions (10)

## Question 1:

**What AI performance and risk metrics are currently reported to the
board, and how frequently are they reviewed?**

**Why this matters:**\
Board-level visibility determines governance maturity. If AI metrics are
not part of executive reporting, EU AI Act oversight requirements are
unlikely to be operationalized.

**Red flag (bad answer):**\
"We don't have AI-specific reporting yet." → AI is operational but not
governed at enterprise level.

**KAF component:** Run Safe

------------------------------------------------------------------------

## Question 2:

**Beyond L1 ticket deflection and CSAT, what KPIs define AI success for
you --- cost reduction, risk exposure, auditability, regulatory
agility?**

**Why this matters:**\
ServiceNow optimizes operational efficiency, but industrialization
requires compliance and governance metrics. This reveals whether AI is
measured strategically or tactically.

**Red flag:**\
"We mainly track ticket volume and resolution time." → Governance,
compliance, and risk are not embedded in performance measurement.

**KAF component:** Core

------------------------------------------------------------------------

## Question 3:

**Do you maintain a centralized AI system registry covering all
departments (IT, HR, Claims, Finance)?**

**Why this matters:**\
EU AI Act requires inventory and classification of AI systems. Shadow AI
already exists; this tests formal governance maturity.

**Red flag:**\
"We have informal awareness but no official registry." → Regulatory and
audit exposure.

**KAF component:** Policy-as-Code

------------------------------------------------------------------------

## Question 4:

**When regulatory guidance changes (e.g., EU AI Act updates), how long
does it take to update AI-related processes and controls?**

**Why this matters:**\
Current adaptation time is \~3 months. Industrialization target is \<2
weeks. This measures operational agility and policy automation
readiness.

**Red flag:**\
"It depends --- usually several months." → Manual governance processes,
no enforceable policy layer.

**KAF component:** Policy-as-Code

------------------------------------------------------------------------

## Question 5:

**Which AI-assisted decisions today are fully traceable end-to-end ---
and which are not?**

**Why this matters:**\
ServiceNow has partial auditability. Shadow AI tools likely do not. EU
AI Act requires traceability for high-risk systems.

**Red flag:**\
"Only ServiceNow actions are logged." → Fragmented audit trail,
compliance gap.

**KAF component:** Run Safe

------------------------------------------------------------------------

## Question 6:

**At which decision points must a human explicitly approve, validate, or
override AI actions?**

**Why this matters:**\
Human-in-the-Loop checkpoints are mandatory for high-risk workflows.
Oversight cannot be reactive.

**Red flag:**\
"Humans step in only when issues occur." → No designed oversight
mechanism.

**KAF component:** Human-in-the-Loop

------------------------------------------------------------------------

## Question 7:

**Which governance policies (data access, cross-border data, escalation
rules, model usage limits) must become enforceable system guardrails
rather than documented procedures?**

**Why this matters:**\
Policy-as-Code differentiates Kyndryl from platform vendors. Governance
must move from PDFs to executable constraints.

**Red flag:**\
"Our policies are documented and approved already." → Governance exists
on paper, not in execution.

**KAF component:** Policy-as-Code

------------------------------------------------------------------------

## Question 8:

**How are AI-related incidents detected, categorized, escalated, and
reported today?**

**Why this matters:**\
Industrial AI requires AI-specific monitoring integrated with security
operations. This tests Digital Trust maturity.

**Red flag:**\
"We don't classify AI incidents separately." → AI risk not embedded in
operational monitoring.

**KAF component:** Run Safe

------------------------------------------------------------------------

## Question 9:

**For L2/L3 workflows, what systems beyond ServiceNow must an enterprise
agent interact with (legacy monitoring, backup, policy databases)?**

**Why this matters:**\
Industrialization requires orchestration across fragmented systems. This
reveals MCP connector requirements and integration complexity.

**Red flag:**\
"We haven't mapped cross-system dependencies." → No clear agentic
workflow architecture.

**KAF component:** Interop (MCP)

------------------------------------------------------------------------

## Question 10:

**If we implemented an executive AI governance dashboard in Q3 2026,
what five indicators must it display on day one?**

**Why this matters:**\
Anchors the engagement in measurable governance outcomes. Ensures
alignment between architecture and board-level accountability.

**Red flag:**\
"I'm not sure." → No defined AI oversight framework.

**KAF component:** Core + Run Safe

------------------------------------------------------------------------

# Part 2: KAF Mapping (mini)

  -----------------------------------------------------------------------------
  KAF Component                        Covered by Q#           Notes
  ------------------------------------ ----------------------- ----------------
  Agentic Core                         2, 10                   Strategic KPIs +
                                                               dashboard
                                                               alignment

  Agentic Ingestion                    9                       Cross-system
                                                               data integration

  Policy-as-Code                       3, 4, 7                 Registry +
                                                               adaptation
                                                               speed +
                                                               enforceable
                                                               rules

  Digital Trust                        1, 5, 8, 10             Auditability +
                                                               monitoring +
                                                               executive
                                                               oversight

  Human-in-the-Loop                    6                       Explicit
                                                               oversight
                                                               checkpoints

  Interop (MCP/A2A)                    9                       Tool/system
                                                               integration
  -----------------------------------------------------------------------------

------------------------------------------------------------------------

# Part 3: Assumptions / Risks / Open Items

1.  Shadow AI expansion risk across additional departments.
2.  Governance deadline (Q3 2026) may outpace operational readiness.
3.  AI success may still be defined primarily by efficiency rather than
    compliance.
4.  Fragmented monitoring beyond ServiceNow.
5.  EU AI Act classification may not yet be formally assessed.

------------------------------------------------------------------------

# Part 4: What We Will Measure (3 KPI Proposals)

1.  **AI Registry Coverage:** 100% of AI systems registered and
    classified within 6 months.
2.  **Regulatory Adaptation Cycle Time:** Reduce from \~3 months to \<2
    weeks.
3.  **Audit Traceability Coverage:** 100% of AI-assisted decisions
    logged with full traceability.

------------------------------------------------------------------------

# Part 5: Agent Classification

-   **Governance tier:** Enterprise Agent\
-   **Registry/reuse potential:** Governance accelerator reusable for
    regulated EU enterprises.

------------------------------------------------------------------------

# Dependencies on Other Roles

-   AI-SEC: Threat modeling and compliance controls\
-   FDE: On-prem infrastructure feasibility\
-   AI-SE: Monitoring instrumentation\
-   AI-PM: Stakeholder alignment and board reporting

------------------------------------------------------------------------

# Questions I Deliberately Did NOT Ask

-   LLM vendor selection --- premature before governance clarity.\
-   Overall IT budget --- AI-PM scope.\
-   Detailed hosting architecture --- FDE scope.
