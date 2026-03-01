# Discovery Packet v1 --- AI-SE

## Student: Radek Jelinek

## Role: AI Software Engineer

## Date: February 23, 2026

## Client: EuroHealth Insurance AG

------------------------------------------------------------------------

## Part 1: Discovery Questions (10)

### Question 1: How are AI-related configurations currently deployed and versioned across ServiceNow and shadow AI tools?

**Why this matters:** Industrialization requires controlled releases,
version tracking, and rollback capability. **Red flag:** Direct
production edits with no version control. **KAF component:** Run Safe /
Agentic Core

### Question 2: What environments exist today (dev/test/prod) for AI systems?

**Why this matters:** Governance gates require environment separation.
**Red flag:** Testing directly in production. **KAF component:**
Policy-as-Code / Run Safe

### Question 3: How are AI decisions currently monitored beyond uptime (e.g., routing accuracy, escalation rate)?

**Why this matters:** Behavioral monitoring is required for compliance
and optimization. **Red flag:** Only server uptime is tracked. **KAF
component:** Digital Trust

### Question 4: If EU AI Act guidance changes, how are guardrails updated technically?

**Why this matters:** Regulatory adaptation speed is a board-level KPI.
**Red flag:** Policy updates are manual document changes. **KAF
component:** Policy-as-Code

### Question 5: Is there a centralized registry of AI agents in production?

**Why this matters:** Shadow AI indicates governance gaps. **Red flag:**
No inventory exists. **KAF component:** Policy-as-Code / Run Safe

### Question 6: How is identity and authentication managed across ServiceNow and other AI tools?

**Why this matters:** Secure interoperability requires identity
propagation. **Red flag:** Separate credentials with no unified control.
**KAF component:** Interop (MCP/A2A)

### Question 7: Where are human-in-the-loop checkpoints enforced technically?

**Why this matters:** L2 autonomy requires override mechanisms. **Red
flag:** No enforced escalation workflow. **KAF component:**
Human-in-the-Loop

### Question 8: What is the rollback strategy if an AI update causes routing errors?

**Why this matters:** Production-safe AI must support rapid rollback.
**Red flag:** Manual reconfiguration only. **KAF component:** Run Safe

### Question 9: What on-prem infrastructure constraints apply to LLM hosting (GPU, HA, latency)?

**Why this matters:** On-prem constraint + €180K budget impacts
feasibility. **Red flag:** No capacity planning done. **KAF component:**
Agentic Core / Ingestion

### Question 10: How are audit logs correlated across AI systems?

**Why this matters:** Unified audit trail required for EU AI Act
readiness. **Red flag:** Logs exist in silos. **KAF component:** Digital
Trust / Interop

------------------------------------------------------------------------

## Part 2: KAF Mapping

  KAF Component       Covered by Q#
  ------------------- ---------------
  Agentic Core        1, 9
  Agentic Ingestion   9
  Policy-as-Code      2, 4, 5
  Digital Trust       3, 10
  Human-in-the-Loop   7
  Interop (MCP/A2A)   6, 10

------------------------------------------------------------------------

## Part 3: Assumptions / Risks

1.  Shadow AI may resist central governance integration.
2.  GPU capacity may be insufficient for enterprise LLM hosting.
3.  ServiceNow integration complexity underestimated.
4.  Regulatory updates may require architectural refactoring.
5.  Budget may not include infrastructure procurement.

------------------------------------------------------------------------

## Part 4: KPI Proposals

1.  Regulatory adaptation time: 3 months → \< 14 days.
2.  AI deployment rollback time: \< 30 minutes.
3.  Unified audit coverage: 100% AI systems registered and logged.

------------------------------------------------------------------------

## Part 5: Agent Classification

**Governance Tier:** Enterprise Agent\
**Registry Potential:** Governed Helpdesk Agent Blueprint reusable for
EU-regulated clients.

------------------------------------------------------------------------

## Dependencies on Other Roles

-   AI-SEC: EU AI Act classification and compliance guardrails.
-   FDE: LLM hosting topology and API architecture.
-   AI-DS: Knowledge base audit and data quality validation.
-   AI-DA: Monitoring metrics and dashboard requirements.
-   AI-PM: Budget allocation and hardware procurement approval.

------------------------------------------------------------------------

## Questions I Deliberately Did NOT Ask

-   Overall AI strategy (AI-PM responsibility).
-   Detailed knowledge taxonomy (AI-DS responsibility).
