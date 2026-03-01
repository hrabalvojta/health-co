# Discovery Packet v1 — AI-PM  
## Student: [Kateřina Kubíčková]  
## Date: February 23, 2026  
## Client: EuroHealth Insurance AG  

---

# Part 1: Discovery Questions (10)

---

### Question 1  
**What specifically can you NOT enforce today with ServiceNow + Moveworks that you believe must be enforceable before Q3 2026?**

**Why this matters:**  
Clarifies governance and enforceability gaps. Moves the discussion from feature optimization to industrial AI control.

**Red flag (bad answer):**  
“It’s mostly about improving accuracy.” → Indicates tuning mindset, not governance transformation.

**KAF component:** Core / Policy-as-Code

---

### Question 2  
**Which AI-related controls must be technically impossible to bypass — even by administrators?**

*(e.g., no PII in training, mandatory human approval before ticket closure, restricted system actions)*

**Why this matters:**  
Defines non-negotiable guardrails that must be enforced in code, not policy documents.

**Red flag:**  
“We rely on process discipline and internal guidelines.” → No technical enforcement.

**KAF component:** Policy-as-Code

---

### Question 3  
**If the EU AI Act required a full audit trail of one resolved ticket tomorrow, could you reconstruct the model version, prompt logic, data source, and approval chain?**

**Why this matters:**  
Tests Digital Trust maturity and deterministic auditability.

**Red flag:**  
“We would need to ask the vendor for logs.” → Lack of enterprise ownership.

**KAF component:** Run Safe

---

### Question 4  
**When regulation or internal AI risk policy changes, what is the path from policy decision to production behavior change — and how long does that take?**

**Why this matters:**  
Measures governance-to-production latency. Industrial AI requires rapid policy propagation.

**Red flag:**  
“It goes through quarterly release cycles.” → Too slow for regulatory adaptation.

**KAF component:** Policy-as-Code / Run Safe

---

### Question 5  
**Which helpdesk decisions would materially increase legal or reputational risk if executed autonomously?**

**Why this matters:**  
Defines Human-in-the-Loop boundaries based on risk exposure rather than convenience.

**Red flag:**  
“IT helpdesk is low risk.” → Underestimation of identity and access implications.

**KAF component:** Human-in-the-Loop (HITL)

---

### Question 6  
**To move from ticket response to full resolution, which enterprise systems must the AI agent orchestrate — and who owns those integrations?**

*(IAM, Active Directory, SAP HR, endpoint management, monitoring tools, etc.)*

**Why this matters:**  
Identifies scope of agentic workflows and cross-department dependencies (MCP connectors).

**Red flag:**  
“We haven’t mapped that yet.” → No clear end-to-end automation vision.

**KAF component:** Interop

---

### Question 7  
**Who at board level is accountable for AI risk, and what operational AI metrics do they currently review?**

**Why this matters:**  
Ensures executive accountability and governance visibility.

**Red flag:**  
“AI is part of general IT reporting.” → No explicit AI oversight.

**KAF component:** Run Safe / Core

---

### Question 8  
**How do you technically verify that no employee PII enters model training, fine-tuning, or prompt logs?**

**Why this matters:**  
Validates ingestion controls and enforceable data governance under EU AI Act constraints.

**Red flag:**  
“We instruct teams not to upload PII.” → No ingestion safeguards.

**KAF component:** Ingestion / Policy-as-Code

---

### Question 9  
**If we succeed in IT, what would prevent scaling this governance model to Claims, HR, or Customer Support?**

**Why this matters:**  
Surfaces structural blockers to cross-department AI scaling.

**Red flag:**  
“Each department manages AI independently.” → No enterprise AI framework.

**KAF component:** Core / Interop

---

### Question 10  
**Within the €180K and 6-month window, which outcome must be visible to the board: cost reduction, compliance readiness, risk mitigation, or enterprise AI foundation?**

**Why this matters:**  
Forces prioritization under budget constraints and prevents scope expansion.

**Red flag:**  
“All of the above.” → Unrealistic expectations within constraints.

**KAF component:** Core

---

# Part 2: KAF Mapping (mini)

| KAF Component        | Covered by Q#        | Notes |
|----------------------|----------------------|-------|
| Agentic Core         | 1, 7, 9, 10          | Business mandate, executive ownership, scaling |
| Agentic Ingestion    | 8                    | PII enforcement & data governance |
| Policy-as-Code       | 1, 2, 4, 8           | Non-bypassable controls, propagation speed |
| Digital Trust (Run Safe) | 3, 4, 7        | Auditability, regulatory readiness |
| Human-in-the-Loop    | 5                    | Risk-based autonomy boundaries |
| Interop (MCP/A2A)    | 6, 9                 | Enterprise orchestration & scaling |

---

# Part 3: Assumptions / Risks / Open Items

1. Current governance may rely heavily on vendor capabilities rather than enterprise-level enforcement.
2. Policy updates likely follow traditional IT release cycles (slow adaptation risk).
3. Board-level AI oversight may not yet be formalized.
4. Integration ownership across departments could slow scaling.
5. Budget constraint (€180K / 6 months) limits scope — prioritization is critical.

---

# Part 4: What We Will Measure (3 KPI Proposals)

1. **L1 Auto-Resolution Rate:** Target 50% within Phase 1 (300 IT users)
2. **Audit Readiness SLA:** 100% reconstructable AI decision trace within 24 hours
3. **Policy Update Propagation Time:** Reduce from weeks/months to < 5 business days

---

# Part 5: Agent Classification

- **Governance Tier:** Enterprise  
- **Registry / Reuse Potential:**  
  The governance framework, Policy-as-Code guardrails, and audit mechanisms should be registered as reusable enterprise AI components for future departmental agents.

---

# Dependencies on Other Roles

- Need **AI-SEC** to validate regulatory classification and security posture.
- Need **FDE** to assess on-prem LLM hosting and integration feasibility.
- Need **AI-SE** to evaluate CI/CD and monitoring infrastructure.
- Need **AI-DS** to assess knowledge base quality and training constraints.
- Need **AI-DA** to define reporting dashboards and board metrics.

---

# Questions I Deliberately Did NOT Ask (and Why)

- Detailed LLM hosting architecture — FDE responsibility.
- Monitoring stack implementation — AI-SE responsibility.
- Model evaluation metrics — AI-DS responsibility.

Focus of AI-PM: executive alignment, governance industrialization, prioritization under constraints.

