# Discovery Packet v1 - AI Product Manager

## Student: Lenka Hudcova

## Date: February 23, 2026

## Client: EuroHealth Insurance AG

------------------------------------------------------------------------

## Part 1: Discovery Questions (10)

### Question 1: You already have ServiceNow + Moveworks. What specifically can't you do today that made you call Kyndryl?

**Why this matters:** Forces clarity on the real gap --- governance,
scaling, regulatory readiness --- not just performance tuning.\
**Red flag (bad answer):** "We just want better ticket automation." →
Industrialization problem not understood.\
**KAF component:** Agentic Core / Ingestion

------------------------------------------------------------------------

### Question 2: Today, how many AI systems are running in production across EuroHealth --- and is there a formal AI registry?

**Why this matters:** Industrialization starts with visibility. Shadow
AI cannot be governed if it is not inventoried.\
**Red flag (bad answer):** "We're not sure." → No governance baseline,
high regulatory exposure.\
**KAF component:** Run Safe / Ingestion

------------------------------------------------------------------------

### Question 3: If the EU AI Act classification guidance changed tomorrow, how long would it take you to update your AI processes across all departments?

**Why this matters:** Measures regulatory adaptation speed.
Industrialization should reduce adaptation time from months to weeks.\
**Red flag (bad answer):** "Probably a quarter." → Governance not
operationalized.\
**KAF component:** Policy-as-Code

------------------------------------------------------------------------

### Question 4: Which AI-related rules today exist only in documentation, and which are technically enforced in systems?

**Why this matters:** Tests Policy-as-Code maturity. Governance in PDFs
≠ enforceable governance.\
**Red flag (bad answer):** "All governance is documented." → No
technical guardrail layer.\
**KAF component:** Policy-as-Code

------------------------------------------------------------------------

### Question 5: What AI-related incident would wake up your board tomorrow morning?

**Why this matters:** Surfaces executive-level risk perception and true
strategic driver.\
**Red flag (bad answer):** Vague answer → Risk not clearly modeled at
board level.\
**KAF component:** Run Safe

------------------------------------------------------------------------

### Question 6: Where in your current AI workflows is a human required to approve, override, or validate decisions?

**Why this matters:** Identifies Human-in-the-Loop checkpoints critical
for EU AI Act readiness.\
**Red flag (bad answer):** "We trust the system unless it breaks." → No
defined oversight boundaries.\
**KAF component:** Human-in-the-Loop

------------------------------------------------------------------------

### Question 7: For Phase 1 (IT -- 300 users), what business outcome must improve to justify expansion to HR and Claims?

**Why this matters:** Defines measurable success criteria and expansion
trigger beyond CSAT.\
**Red flag (bad answer):** "We'll see how it goes." → No defined scaling
logic.\
**KAF component:** Agentic Core

------------------------------------------------------------------------

### Question 8: How is AI ownership structured today --- who has authority to approve, pause, or decommission an AI system?

**Why this matters:** Governance requires clear RACI and decision
rights.\
**Red flag (bad answer):** "It depends on the department." → No
centralized AI governance authority.\
**KAF component:** Run Safe / Policy-as-Code

------------------------------------------------------------------------

### Question 9: What integration constraints do we face on-prem --- especially regarding identity management, logging, and cross-system auditability?

**Why this matters:** On-prem constraints directly affect feasibility,
cost, and architecture.\
**Red flag (bad answer):** "We haven't mapped that." → Infrastructure
readiness risk.\
**KAF component:** Interop (MCP/A2A) / Run Safe

------------------------------------------------------------------------

### Question 10: By Q3 2026, what must you show the board to say: "We are EU AI Act governance-ready"?

**Why this matters:** Forces definition of a concrete board-level
deliverable (registry, framework, reporting dashboard, risk model).\
**Red flag (bad answer):** "We just need documentation." → Compliance
treated as paperwork, not operational capability.\
**KAF component:** Policy-as-Code / Run Safe

> Minimum coverage satisfied: - Policy-as-Code: Q3, Q4, Q8, Q10\
> - Interoperability (MCP/A2A): Q9\
> - Human-in-the-Loop: Q6

------------------------------------------------------------------------

## Part 2: KAF Mapping (mini)

  -----------------------------------------------------------------------------
  KAF Component                       Covered by Q#            Notes
  ----------------------------------- ------------------------ ----------------
  Agentic Core                        1, 7                     ServiceNow
                                                               boundary & phase
                                                               success

  Agentic Ingestion                   1, 2                     AI inventory &
                                                               platform gap

  Policy-as-Code                      3, 4, 8, 10              Enforceable
                                                               governance & EU
                                                               AI Act

  Digital Trust                       2, 5, 8, 9,10            Audit,
                                                               ownership, risk
                                                               visibility

  Human-in-the-Loop                   6                        Decision
                                                               checkpoints &
                                                               accountability

  Interop (MCP/A2A)                   9                        On-prem
                                                               integration &
                                                               IAM boundaries
  -----------------------------------------------------------------------------

------------------------------------------------------------------------

## Part 3: Assumptions / Risks / Open Items (3-5)

1.  €180K may be insufficient if enterprise-wide governance (HR, Claims,
    Finance) is included in Phase 1.
2.  Shadow AI usage may be larger than currently visible to CIO.
3.  Regulatory adaptation currently process-driven, not technically
    enforced.
4.  On-prem integration complexity may extend timeline beyond 6 months.
5.  Success criteria may not yet be quantified at board level.

------------------------------------------------------------------------

## Part 4: What We Will Measure (3 KPI proposals)

1.  Regulatory adaptation time: Reduce from \~3 months → \< 2 weeks.
2.  \% of AI systems registered in formal AI inventory: Target 100% in
    IT domain (Phase 1).
3.  CSAT improvement: 3.6 → 4.2+ with governed AI support model.

------------------------------------------------------------------------

## Part 5: Agent Classification

-   **Governance tier:** Enterprise\
-   **Registry/reuse potential:** Register as an Enterprise Agent under
    KAF registry with reusable Policy-as-Code framework and audit
    architecture template for regulated EU clients.

------------------------------------------------------------------------

## Dependencies on Other Roles:

-   I need **AI-SEC** to assess specific EU AI Act risk classification
    and security control maturity.
-   I need **AI-FDE** to validate on-prem LLM hosting feasibility and
    IAM integration constraints.
-   I need **AI-DS** to assess KB quality, evaluation metrics, and model
    performance baseline.
-   I need **AI-SE** to evaluate CI/CD and monitoring readiness.

------------------------------------------------------------------------

## Questions I Deliberately Did NOT Ask (and why):

-   "Which exact PII filters are applied in the retrieval pipeline?" ---
    Technical detail (AI-SEC / FDE territory).
-   "Which LLM provider will be selected?" --- Premature architecture
    discussion (FDE).
-   "Exact latency targets per API call?" --- Operational performance
    tuning (AI-SE).
