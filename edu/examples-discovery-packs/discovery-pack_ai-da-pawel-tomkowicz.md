# Discovery Packet v1 --- AI-DA

## Student: \[Paweł Tomkowicz\]

## Date: February 23, 2026

## Client: EuroHealth Insurance AG

------------------------------------------------------------------------

## Context

EuroHealth already operates ServiceNow with AI (Moveworks) in
production.\
They are not seeking new AI features --- they need **AI
industrialization**:

-   Governance
-   EU AI Act readiness (Dec 2027)
-   Cross-department scaling
-   Production-grade monitoring
-   Policy-as-Code enforcement
-   Auditability
-   On-prem constraints
-   No PII in training data

Budget: €180K / 6 months (Phase 1: IT department, 300 users)

------------------------------------------------------------------------

# Part 1 --- Discovery Questions (AI-DA Focus)

## Q1: What specific governance limitations have you encountered with ServiceNow AI that it cannot address out-of-the-box?

**Why it matters:**\
We must understand what gaps exist beyond platform capabilities ---
especially in cross-department governance and regulatory traceability.

**Red flag:**\
"We haven't assessed governance gaps formally." → Indicates reactive
compliance and board exposure.

**KAF Component:** Core

------------------------------------------------------------------------

## Q2: Do you maintain a centralized AI inventory across departments (HR, Claims, Finance), including shadow AI tools?

**Why it matters:**\
Without a registry, scaling AI governance and enforcing Policy-as-Code
is impossible.

**Red flag:**\
"Each department manages its own AI tools." → Fragmentation and
compliance risk.

**KAF Component:** Core

------------------------------------------------------------------------

## Q3: Which AI-related policies today exist only as documents (PDFs) and are not enforceable in code?

**Why it matters:**\
Policy-as-Code readiness depends on converting documented governance
into executable guardrails.

**Red flag:**\
"We rely on training and awareness, not technical enforcement." →
Governance theatre, not control.

**KAF Component:** Policy-as-Code

------------------------------------------------------------------------

## Q4: What regulatory or policy changes have occurred in the last 12 months, and how long did it take to reflect them in production systems?

**Why it matters:**\
Operational maturity is measured by regulatory adaptation speed (days vs
months).

**Red flag:**\
"It took several months to implement changes." → Indicates process
rigidity incompatible with EU AI Act timeline.

**KAF Component:** Run Safe

------------------------------------------------------------------------

## Q5: What audit logs are currently stored for AI-assisted decisions (input context, prompt, model version, override, output)?

**Why it matters:**\
EU AI Act compliance requires traceability and reproducibility.

**Red flag:**\
"We only log final outputs." → Insufficient audit trail for regulatory
review.

**KAF Component:** Run Safe

------------------------------------------------------------------------

## Q6: What measurable KPIs do you track for AI governance --- beyond ticket deflection (e.g., override rate, policy violation rate, compliance incidents)?

**Why it matters:**\
Industrial AI requires governance dashboards, not just operational
metrics.

**Red flag:**\
"We measure productivity, not compliance." → No governance observability
layer.

**KAF Component:** Run Safe

------------------------------------------------------------------------

## Q7: Which AI decisions today require mandatory human confirmation, and where is full automation currently allowed?

**Why it matters:**\
Defines Human-in-the-Loop boundaries and risk classification tier.

**Red flag:**\
"Most decisions are automated without structured review checkpoints." →
Elevated regulatory exposure.

**KAF Component:** HITL

------------------------------------------------------------------------

## Q8: If an agent needs to orchestrate workflows beyond ServiceNow (e.g., claims systems, HR platforms), what integration layer is available (APIs, MCP-compatible connectors)?

**Why it matters:**\
Agentic scaling depends on interoperability standards and secure tool
connections.

**Red flag:**\
"Integrations are manual or ad-hoc." → No scalable agentic orchestration
model.

**KAF Component:** Interop

------------------------------------------------------------------------

## Q9: How do you currently validate that no PII is included in training data for AI systems?

**Why it matters:**\
Strict constraint: no PII in training data. Validation must be automated
and auditable.

**Red flag:**\
"We rely on manual review." → High data governance risk.

**KAF Component:** Ingestion

------------------------------------------------------------------------

## Q10: If the board requested an EU AI Act readiness report tomorrow, what dashboards or artifacts could you present?

**Why it matters:**\
This reveals governance maturity and readiness for Q3 2026 board review.

**Red flag:**\
"We would present project slides." → No structured governance framework.

**KAF Component:** Core + Run Safe

------------------------------------------------------------------------

# Part 2 --- KAF Coverage Mapping

  KAF Component       Covered by Q#
  ------------------- ---------------
  Agentic Core        1, 10
  Agentic Ingestion   9
  Policy-as-Code      3
  Run Safe            4, 5, 6, 10
  Human-in-the-Loop   7
  Interop (MCP/A2A)   8

------------------------------------------------------------------------

# Part 3 --- Assumptions / Risks

1.  Shadow AI exists beyond ServiceNow (HR, Claims, Finance).
2.  No unified AI registry or cross-department governance model.
3.  Audit logging is incomplete for non-ServiceNow systems.
4.  Regulatory adaptation cycles exceed 2 months.
5.  Compliance metrics are not dashboarded at executive level.

------------------------------------------------------------------------

# Part 4 --- Proposed Governance KPIs (AI-DA Focus)

1.  **AI Registry Coverage Rate**\
    Target: 100% of AI systems registered and classified by governance
    tier.

2.  **Policy Enforcement Rate**\
    % of AI workflows governed by executable Policy-as-Code controls.\
    Target: ≥95% in Phase 1.

3.  **Regulatory Adaptation Time**\
    Time from regulatory update to production enforcement.\
    Target: ≤14 days.

4.  **AI Audit Completeness Index**\
    % of AI decisions with full traceability (input → model → output →
    override).\
    Target: 100%.

------------------------------------------------------------------------

# Part 5 --- Agent Classification

-   Governance Tier: **Enterprise Agent**
-   Registry Required: Yes
-   Audit Trail Required: Yes
-   Policy-as-Code Mandatory: Yes
-   HITL Boundaries Required: Yes

------------------------------------------------------------------------

# Dependencies on Other Roles

-   AI-SEC → Security posture validation and threat modeling.
-   AI-SE → Deployment architecture and monitoring stack.
-   AI-PM → Stakeholder prioritization and budget constraints.
-   FDE → ServiceNow + agent orchestration technical feasibility.

------------------------------------------------------------------------

# Questions Deliberately Not Asked

-   Detailed LLM hosting architecture (AI-SE territory)
-   UI/UX accessibility (AI-FE territory)
-   Budget negotiation tactics (AI-PM territory)
