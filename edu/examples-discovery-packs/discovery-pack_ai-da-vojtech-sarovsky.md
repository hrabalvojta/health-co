# Discovery Packet v1 --- AI Data Analyst (AI-DA)
## Student: Vojtech Sarovsky
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

------------------------------------------------------------------------

## Part 1: Discovery Questions (10)

### Question 1:

**If you had to defend one AI-driven decision to the board tomorrow,
what specific metric would you present as proof of success --- and can
you currently demonstrate full data lineage behind it within 24
hours?**\
**Why this matters:** This reveals what truly defines value at board
level and whether traceability exists today.\
**Red flag:** No single outcome defined, or inability to demonstrate
lineage and provenance.\
**KAF component:** Run Safe

------------------------------------------------------------------------

### Question 2:

**What data-driven outcomes can ServiceNow currently not measure or
validate that limit your ability to trust AI-assisted ticket
decisions?**\
**Why this matters:** Identifies gaps beyond L1 deflection ---
especially in governance, explainability, and cross-tool visibility.\
**Red flag:** "We rely on ServiceNow dashboards only" without
cross-system reconciliation.\
**KAF component:** Agentic Ingestion

------------------------------------------------------------------------

### Question 3:

**Which governance signals must be automatically captured in code (e.g.,
model version, input source, routing logic, policy rules triggered) for
analytics to be considered board-trustworthy?**\
**Why this matters:** Determines Policy-as-Code readiness and what must
be technically enforceable.\
**Red flag:** Governance described only in documentation, not
system-level enforcement.\
**KAF component:** Policy-as-Code

------------------------------------------------------------------------

### Question 4:

**How long does it currently take to update dashboards, KPIs, and
compliance reporting when regulatory guidance changes?**\
**Why this matters:** Measures operational agility and regulatory
adaptation speed.\
**Red flag:** Manual spreadsheet updates or 2--3 month adaptation
cycles.\
**KAF component:** Run Safe

------------------------------------------------------------------------

### Question 5:

**Across ServiceNow, legacy monitoring tools, and shadow AI prototypes,
do you have a unified AI registry with consistent metrics
definitions?**\
**Why this matters:** Without a single metric taxonomy, cross-department
scaling is impossible.\
**Red flag:** Different departments define "resolution," "escalation,"
or "AI-assisted" differently.\
**KAF component:** Interop

------------------------------------------------------------------------

### Question 6:

**At which decision points must AI-generated recommendations require
human confirmation before being logged as final outcomes?**\
**Why this matters:** Clarifies Human-in-the-Loop checkpoints and how
they affect reporting integrity.\
**Red flag:** No distinction between AI-suggested and AI-approved
actions.\
**KAF component:** HITL

------------------------------------------------------------------------

### Question 7:

**What model monitoring metrics are currently tracked (accuracy, drift,
hallucination rate, misrouting), and how are alerts escalated?**\
**Why this matters:** Determines Digital Trust maturity and production
safety readiness.\
**Red flag:** No real-time monitoring or drift detection beyond
anecdotal feedback.\
**KAF component:** Run Safe

------------------------------------------------------------------------

### Question 8:

**What non-functional requirements must analytics dashboards meet
(latency, multilingual reporting EN/DE/CZ, audit export capability)?**\
**Why this matters:** Ensures board-level reporting works in on-prem,
multilingual, compliance-sensitive context.\
**Red flag:** Reporting requirements undefined or assumed "nice to
have."\
**KAF component:** Agentic Core

------------------------------------------------------------------------

### Question 9:

**Which cross-department AI workflows (IT, HR, Claims) should feed into
a single performance and risk dashboard by Q3 2026?**\
**Why this matters:** Identifies scaling expectations and required data
integrations (MCP connectors).\
**Red flag:** Each department manages AI reporting in isolation.\
**KAF component:** Interop

------------------------------------------------------------------------

### Question 10:

**Who has formal authority to stop an AI workflow if monitoring
thresholds are breached, and how is that decision captured in analytics
logs?**\
**Why this matters:** Links governance accountability to measurable
reporting signals.\
**Red flag:** No defined owner for AI performance thresholds or incident
escalation.\
**KAF component:** Policy-as-Code

------------------------------------------------------------------------

## Part 2: KAF Mapping (Mini)

  KAF Component       Covered by Q#   Notes
  ------------------- --------------- -------------------------------
  Agentic Core        8               Dashboard NFR alignment
  Agentic Ingestion   2               ServiceNow metric gaps
  Policy-as-Code      3, 10           Enforceable governance rules
  Digital Trust       1, 4, 7         Audit, adaptation, monitoring
  Human-in-the-Loop   6               Decision checkpoints
  Interop (MCP/A2A)   5, 9            Cross-system data unification

------------------------------------------------------------------------

## Part 3: Assumptions / Risks / Open Items

1.  No unified AI registry exists across departments.
2.  Governance is partially documented but not automated.
3.  Regulatory reporting is semi-manual.
4.  Shadow AI metrics are not centrally monitored.
5.  Board expectations for "production-ready" are not formally defined.

------------------------------------------------------------------------

## Part 4: What We Will Measure (3 KPI Proposals)

1.  **AI Traceability Coverage:** 100% of AI-assisted decisions
    traceable end-to-end within 24 hours.
2.  **Regulatory Adaptation SLA:** Reporting update cycle reduced from
    \~3 months to \<2 weeks.
3.  **Cross-Department AI Registry Coverage:** 100% of AI systems
    registered with standardized metrics.

------------------------------------------------------------------------

## Part 5: Agent Classification

-   **Governance Tier:** Enterprise\
-   **Registry / Reuse Potential:** Standardized AI governance dashboard
    reusable across other regulated Kyndryl insurance clients.

------------------------------------------------------------------------

## Dependencies on Other Roles

-   AI-SEC: Security event logging standards and compliance mapping.
-   FDE: Integration feasibility and data pipeline architecture.
-   AI-SE: Monitoring and CI/CD instrumentation.
-   AI-PM: Stakeholder alignment on board-level KPIs.

------------------------------------------------------------------------

## Questions I Deliberately Did NOT Ask

-   Detailed LLM hosting architecture --- FDE territory.
-   CI/CD pipeline maturity specifics --- AI-SE responsibility.
-   Threat modeling specifics --- AI-SEC responsibility.
