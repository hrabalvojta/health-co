# Discovery Packet v1 — AI-SEC
## Student: Martin Janicek
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: What specifically can’t you govern, control, or scale today with ServiceNow + Moveworks that made this a board-level AI industrialization initiative?

**Why this matters:**  
This validates that the problem is governance and enterprise scaling — not chatbot optimization. It surfaces structural gaps beyond L1 deflection.

**Red flag (bad answer):**  
“It’s mostly about improving routing accuracy.” → Signals feature tuning, not governance transformation.

**KAF component:** Agentic Core

---

### Question 2: Do you maintain a centralized AI system registry that inventories all AI use cases across HR, Claims, Finance, and prototypes — or is visibility limited to IT-managed systems?

**Why this matters:**  
EU AI Act readiness requires full AI inventory and risk classification. Without centralized visibility, governance cannot scale.

**Red flag (bad answer):**  
“We track what IT deploys; departments manage their own tools.” → Indicates shadow AI exposure.

**KAF component:** Agentic Ingestion

---

### Question 3: Which AI governance rules must be technically enforced in code — such as PII blocking, country-based routing across EU states, or model version restrictions — rather than documented in policy?

**Why this matters:**  
Policy-as-Code requires runtime enforcement inside the agent pipeline. Documentation alone does not satisfy regulatory compliance.

**Red flag (bad answer):**  
“Our compliance policies are documented and reviewed annually.” → Governance is static, not executable.

**KAF component:** Policy-as-Code

---

### Question 4: When EU AI Act guidance changes, what technical steps are required to translate that change into updated AI system controls — and how much of that process is automated today?

**Why this matters:**  
The board expects EU AI Act readiness by Q3 2026. Manual regulatory translation will not scale across departments.

**Red flag (bad answer):**  
“It requires cross-functional workshops and manual reconfiguration.” → No compliance automation pipeline.

**KAF component:** Policy-as-Code

---

### Question 5: Can you reconstruct any AI-assisted decision end-to-end — including model version, prompt context, retrieved knowledge, system integrations used, human overrides, and final output?

**Why this matters:**  
Enterprise-tier AI requires forensic-grade traceability for audit, regulators, and incident response.

**Red flag (bad answer):**  
“We log outcomes, not model-level interactions.” → Incomplete auditability for high-risk AI.

**KAF component:** Digital Trust

---

### Question 6: In helpdesk and future Claims workflows, which decisions legally require mandatory human confirmation before execution — regardless of AI confidence level?

**Why this matters:**  
Compliance-based oversight must be explicitly defined in regulated insurance environments. Confidence-based escalation is insufficient.

**Red flag (bad answer):**  
“The AI escalates when unsure.” → Oversight is probabilistic, not policy-driven.

**KAF component:** Human-in-the-Loop

---

### Question 7: When a human overrides an AI recommendation, how is that override logged, reviewed, and audited — and who is accountable for those decisions?

**Why this matters:**  
Human-in-the-loop can become a compliance blind spot if overrides are not traceable and systematically reviewed.

**Red flag (bad answer):**  
“Overrides are manual and not centrally reviewed.” → Loss of traceability and governance breakdown.

**KAF component:** Human-in-the-Loop

---

### Question 8: When AI agents access backend systems (ServiceNow, HR tools, Claims platforms), how are identity, authentication, and authorization enforced? Are permissions tied to the end user, the agent, or shared service accounts?

**Why this matters:**  
MCP/A2A interoperability requires strict least-privilege and traceability controls at every integration boundary.

**Red flag (bad answer):**  
“The agent uses a shared integration account.” → Breaks audit chain and increases insider risk.

**KAF component:** Interop (MCP/A2A)

---

### Question 9: How is AI-specific security integrated into production operations — including PII separation (no PII in training), prompt injection monitoring, abnormal agent behavior detection, and SOC-level threat response?

**Why this matters:**  
AI introduces new attack surfaces. It must be embedded into Cyber Defense Operations, not treated as a standard application.

**Red flag (bad answer):**  
“We treat it like any other application.” → AI-specific risks are not addressed.

**KAF component:** Digital Trust

---

### Question 10: If a new AI use case is launched in HR or Claims next quarter, what formal security, compliance, and risk-tier approval gates must be passed before go-live?

**Why this matters:**  
Industrialization requires standardized AI onboarding and enterprise governance gates across departments.

**Red flag (bad answer):**  
“They inform IT and proceed.” → No enterprise AI control plane.

**KAF component:** Agentic Ingestion

---

> Minimum coverage satisfied:
> - Policy-as-Code: Q3, Q4
> - Interop (MCP/A2A): Q8
> - Human-in-the-Loop: Q6, Q7

---

## Part 2: KAF Mapping (mini)

| KAF Component        | Covered by Q# | Notes |
|----------------------|---------------|--------|
| Agentic Core         | Q1            | Strategic governance gap |
| Agentic Ingestion    | Q2, Q10       | AI onboarding & registry |
| Policy-as-Code       | Q3, Q4        | Executable regulatory controls |
| Digital Trust        | Q5, Q9        | Audit, monitoring, production safety |
| Human-in-the-Loop    | Q6, Q7        | Mandatory checkpoints & override accountability |
| Interop (MCP/A2A)    | Q8            | Identity & boundary enforcement |

---

## Part 3: Assumptions / Risks / Open Items (3–5)

1. Shadow AI may exist outside IT visibility, creating compliance exposure.
2. Regulatory updates likely require manual interpretation and system reconfiguration.
3. Helpdesk and Claims workflows may qualify as high-risk AI under EU AI Act.
4. AI telemetry may not yet be integrated into SOC monitoring.
5. On-prem model hosting may lack production-grade isolation and lifecycle controls.

---

## Part 4: What We Will Measure (3 KPI proposals)

1. Reduce regulatory control update cycle from ~90 days to <14 days.
2. Achieve 100% enterprise-wide AI system registry coverage (zero unregistered AI in production).
3. Ensure 100% of AI-assisted decisions are traceable end-to-end for audit purposes.

---

## Part 5: Agent Classification

- **Governance tier:** Enterprise
- **Registry/reuse potential:**  
  Register within centralized AI Governance Registry with risk classification metadata. Governance framework reusable for HR, Claims, and Finance use cases and portable as a Kyndryl enterprise blueprint.

---

## Dependencies on Other Roles

- I need AI-FDE to validate on-prem model hosting architecture and infrastructure isolation.
- I need AI-SE to assess CI/CD automation for guardrail deployment.
- I need AI-DS to validate knowledge base segregation and evaluation controls.
- I need AI-DA to define executive compliance dashboards and reporting metrics.
- I need AI-PM to confirm regulatory timelines, stakeholder alignment, and budget constraints.

---

## Questions I Deliberately Did NOT Ask (and why)

- “Which LLM vendor are you using?” — Infrastructure selection belongs primarily to AI-FDE at this stage.
- “What is your CSAT target?” — Operational KPI optimization is AI-DA / AI-PM scope.
- “How many tickets per category?” — Workflow tuning is not the core governance industrialization challenge.