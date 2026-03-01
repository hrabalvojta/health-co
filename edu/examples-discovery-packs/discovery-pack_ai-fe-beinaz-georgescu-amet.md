# Discovery Packet v1 --- AI-FE

## Student: Beinaz Georgescu-Amet

## Date: February 23, 2026

## Client: EuroHealth Insurance AG

------------------------------------------------------------------------

# Part 1: Discovery Questions (10)

### Question 1: Where does ServiceNow + Moveworks stop today?

**Question:**\
Which AI use cases are currently live in ServiceNow/Moveworks, and where
do governance, scaling, or cross-department consistency break down?

**Why this matters:**\
Identifies the delta between feature-level AI and enterprise AI
governance. Reveals fragmentation and shadow AI risk.

**Red flag (bad answer):**\
"We rely on ServiceNow defaults." / "Each department manages its own
AI."

**KAF component:** Agentic Core / Run Safe

------------------------------------------------------------------------

### Question 2: Which AI-supported decisions fall under EU AI Act high-risk classification?

**Question:**\
Which AI-supported decisions require explainability, auditability, or
regulatory reporting under EU AI Act guidance?

**Why this matters:**\
Determines risk classification and sets control, logging, and governance
requirements.

**Red flag:**\
"We haven't mapped use cases to EU AI Act risk categories."

**KAF component:** Policy-as-Code / Run Safe

------------------------------------------------------------------------

### Question 3: Which policies must be enforceable in code?

**Question:**\
Which internal controls must be technically enforced (data residency,
PII masking, model approval, access control, logging retention) rather
than handled through process documentation?

**Why this matters:**\
Tests Policy-as-Code maturity. Governance must be machine-enforceable
--- especially on-prem.

**Red flag:**\
"Compliance is handled through guidelines and training."

**KAF component:** Policy-as-Code

------------------------------------------------------------------------

### Question 4: How quickly can AI systems adapt to regulatory change?

**Question:**\
If EU AI guidance or internal policy changes tomorrow, how long would it
take to update models, workflows, approvals, and user-facing controls?

**Why this matters:**\
Tests operational agility and DevSecOps maturity.

**Red flag:**\
"It would require a large transformation project."

**KAF component:** Agentic Core / Run Safe

------------------------------------------------------------------------

### Question 5: What systems must AI orchestrate beyond ServiceNow?

**Question:**\
Which systems (claims, underwriting, CRM, ERP, document management, IAM)
must AI workflows integrate with? Are APIs standardized and governed?

**Why this matters:**\
Defines interoperability scope and MCP connector needs.

**Red flag:**\
Integrations are manual, email-based, or inconsistently owned.

**KAF component:** Interop (MCP/A2A)

------------------------------------------------------------------------

### Question 6: Which workflow steps require dynamic AI planning vs deterministic automation?

**Question:**\
In processes such as claims handling or policy updates, which steps
require contextual AI reasoning versus rule-based automation?

**Why this matters:**\
Differentiates RPA from agentic workflows.

**Red flag:**\
No clear distinction between automation and AI reasoning.

**KAF component:** Agentic Core / Interop

------------------------------------------------------------------------

### Question 7: Where must humans remain in the loop?

**Question:**\
At which decision thresholds must human review, override, or
confirmation occur (e.g., high-value claims, compliance flags)?

**Why this matters:**\
Defines HITL checkpoints required for high-risk AI systems.

**Red flag:**\
"Full automation is the goal."

**KAF component:** Human-in-the-Loop / Run Safe

------------------------------------------------------------------------

### Question 8: What level of audit depth is required?

**Question:**\
Do you log prompts, model versions, outputs, overrides, and decision
rationales? Who requires access to these logs?

**Why this matters:**\
Defines Digital Trust architecture and regulator readiness.

**Red flag:**\
"We log system events only."

**KAF component:** Run Safe

------------------------------------------------------------------------

### Question 9: How are models validated before production?

**Question:**\
What validation framework exists before promoting AI systems to
production (bias testing, robustness checks, performance thresholds,
legal review)?

**Why this matters:**\
Industrialization requires structured lifecycle controls.

**Red flag:**\
"Business owner approval is sufficient."

**KAF component:** Run Safe / Policy-as-Code

------------------------------------------------------------------------

### Question 10: How do end users interact with AI across devices?

**Question:**\
Which devices and interfaces expose AI capabilities (desktop portals,
mobile apps, dashboards)? Are accessibility standards and works council
constraints enforced?

**Why this matters:**\
From an AI-FE perspective, governance must extend to UX, accessibility
(WCAG), device security, and user trust.

**Red flag:**\
No defined UX standards or accessibility policies.

**KAF component:** Agentic Core / Ingestion / Human-in-the-Loop

------------------------------------------------------------------------

# Part 2: KAF Mapping (mini)

  ----------------------------------------------------------------------------
  KAF Component                      Covered by Q#            Notes
  ---------------------------------- ------------------------ ----------------
  Agentic Core                       1, 4, 6, 10              Planning,
                                                              orchestration,
                                                              UX exposure

  Agentic Ingestion                  10                       User/device
                                                              constraints

  Policy-as-Code                     2, 3, 9                  Governance
                                                              enforcement

  Digital Trust                      1, 4, 7, 8, 9            Audit,
                                                              monitoring,
                                                              lifecycle

  Human-in-the-Loop                  7, 10                    Escalation +
                                                              confirmation

  Interop (MCP/A2A)                  5, 6                     Cross-system
                                                              orchestration
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

# Part 3: Assumptions / Risks / Open Items

1.  Governance policies may exist only in documentation and not in
    machine-enforced controls.
2.  EU AI Act risk mapping has not been formally completed.
3.  Shadow AI indicates usability or governance friction.
4.  €180K / 6 months may require phased industrialization.
5.  On-prem + no PII constraint may limit model selection and
    architecture flexibility.

------------------------------------------------------------------------

# Part 4: What We Will Measure (3 KPI Proposals)

1.  Regulatory adaptation time reduced to \<30 days for AI policy
    updates.
2.  100% AI use cases mapped to EU AI Act risk categories and
    registered.
3.  Full audit coverage (prompt, model version, output, override)
    implemented for enterprise-tier systems.

------------------------------------------------------------------------

# Part 5: Agent Classification

-   **Governance tier:** Enterprise\
-   **Registry/reuse potential:** This helpdesk agent must be registered
    in the enterprise AI registry and structured for reuse across HR,
    Claims, and Finance in Phase 2.

------------------------------------------------------------------------

# Dependencies on Other Roles:

-   I need AI-SEC to assess security posture and threat model gaps.
-   I need FDE to confirm on-prem LLM hosting and API feasibility.
-   I need AI-SE to evaluate CI/CD and monitoring maturity.
-   I need AI-PM to clarify stakeholder alignment and budget
    constraints.

------------------------------------------------------------------------

# Questions I Deliberately Did NOT Ask (and why):

-   "Which LLM should we use?" --- This is FDE territory.
-   "What is your deployment pipeline maturity?" --- AI-SE focus.
-   "What dashboards do you need?" --- AI-DA focus.
