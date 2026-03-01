# Discovery Packet v1 — [DS]
## Student: [Amanda Jelinkova]
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: Who in your organization is responsible for decisions and risk when using AI tools across departments (IT, Security, Compliance, Care), and how do you ensure there’s one accountable owner?
**Why this matters:** Clarifies accountability for governance (Policy-as-Code + HITL) and reduces blind spots.
**Red flag (bad answer):** No single owner or overlapping roles with unclear accountability.
**KAF component:** L4 Policy-as-Code / L5 Human-in-the-Loop

### Question 2: Which policy rules would you expect to be automatically enforced by the system (for example, who can access data, how long it’s kept, and how content is handled in multiple languages), as opposed to just being documented?
**Why this matters:** Tests readiness for automated governance and compliance checks.
**Red flag (bad answer):** All rules are manual or merely documented; nothing automated.
**KAF component:** L4 Policy-as-Code 

### Question 3: If a new regulation or internal rule comes in, how quickly do you want changes reflected in the AI system, and what would stop you from updating it faster?
**Why this matters:** Gauges operational maturity and speed of policy adaptation (days vs months).
**Red flag (bad answer):** Change cycles measured in months with no clear process or rollback plan.
**KAF component:** L3 AI Core / L4 Policy-as-Code

### Question 4: Can you share the current KB quality metrics (e.g., age distribution, last-update timestamps) and how you prioritize updates across EN/DE/CZ languages?
**Why this matters:** Directly ties to data quality for L1 data ingestion and multilingual evaluation.
**Red flag (bad answer):** No dataset drift monitoring; stale pages >30% is your risk anchor.
**KAF component:** L1 Data Ingestion

### Question 5: Beyond ServiceNow, where else is AI being used across departments — and how centrally visible are those initiatives?
**Why this matters:** Industrialization requires cross-department governance. Shadow AI = major governance risk
**Red flag (bad answer):** “We’re not sure” or “Each department runs its own pilots.” → No centralized AI portfolio oversight.
**KAF component:** Core + Interop

### Question 6: How is your knowledge base structured (taxonomy, metadata, versioning), and how do you evaluate answer quality or content drift?
**Why this matters:** AI reliability depends on data quality, structured KB, and evaluation loops. Governance without evaluation is superficial.
**Red flag (bad answer):** We rely on user complaints.” → No evaluation metrics, no systematic quality measurement.
**KAF component:** Ingestion + Run Safe

### Question 7: Which decisions or workflow steps must always require human confirmation, and how are those checkpoints defined?
**Why this matters:** Defines Human-in-the-Loop boundaries and risk tiering. Critical for high-risk AI classification under EU AI Act.
**Red flag (bad answer):** “We haven’t defined that formally.” → No risk-tier mapping or HITL governance.
**KAF component:** HITL + Run Safe

### Question 8: If an AI system were to autonomously handle a full claim or IT workflow, what systems would it need to access (ERP, CRM, document systems), and under what constraints?
**Why this matters:** Reveals agentic workflow complexity and integration landscape (MCP connectors, RBAC, tool constraints).
**Red flag (bad answer):** “It would need broad access to everything.” → No least-privilege design; governance risk.
**KAF component:** Interop + Policy-as-Code

### Question 9: What KPIs do you use to evaluate AI systems — accuracy, hallucination rate, bias testing, drift detection, operational impact?
**Why this matters:** Industrialization requires measurable performance + risk metrics. If they don’t measure, they can’t govern.
**Red flag (bad answer):** “We look at ticket resolution time only.” → No model-level evaluation or safety metrics.
**KAF component:** Run Safe + Ingestion

### Question 10: How do you technically ensure that PII is excluded from AI training and prompts — automated scanning, anonymization pipelines, access controls?
**Why this matters:** This tests enforceability vs. intention. On-prem + no PII means robust ingestion controls are mandatory.
**Red flag (bad answer):** “We instruct teams not to upload PII.” → No automated controls.
**KAF component:** Ingestion + Policy-as-Code


---

## Part 2: KAF Mapping (mini)
| KAF Component      | Covered by Q# | Notes                  |
|---------------------|---------------|------------------------|
| Agentic Core        |    3 5        |                        |
| Agentic Ingestion   | 4 6 9 10      |                        |
| Policy-as-Code      | 1 2 3 8 10    |                        |
| Digital Trust       |    6 7 9      |                        |
| Human-in-the-Loop   |   1     7     |                        |
| Interop (MCP/A2A)   |     5 8       |                        |

---

## Part 3: Assumptions / Risks / Open Items (3-5)
1. Assumption: Data sources used by the agent can be accessed without triggering PII exposure in training data.
2. High-risk scenarios lack HITL coverage; potential for unsafe autonomous actions.
3. Finalize HITL checkpoints and approval workflow (who approves what and how changes are tested).

---

## Part 4: What We Will Measure (3 KPI proposals)
1. Policy Compliance Coverage (PCC): 70% codified in Policy-as-Code in 6 months
2. Regulatory Change Implementation Time: educe AI policy update cycle to ≤ 14 days (from current baseline)
3. AI Audit Readiness Score: Target: Produce full AI audit evidence package within 72 hours

---

## Part 5: Agent Classification
- **Governance tier:** Team
- **Registry/reuse potential:** We would register the Team agent in a centralized AI registry with a unique ID, defined business and technical owners, risk classification, approved data sources, guardrails (RBAC, logging, HITL), and evaluation metrics. Before sharing, we ensure the agent logic is decoupled from client data, policies are configurable, and integrations are modular to allow safe reuse. It is then published internally as a governed reusable pattern (not a client-specific solution) with deployment, risk, and control templates attached.

---

## Dependencies on Other Roles:
- I need CISO to ask about data access and PII controls so the AI governance layer can enforce data privacy, tracing, and compliance (Policy-as-Code + Run Safe). Without explicit PII controls, training/ingestion could violate EU Act timelines.
- I need Security Architect to ask about threat modeling and integrations to design safe default permissions, secure connectors, and incident response pathways that align with high-risk governance.

## Questions I Deliberately Did NOT Ask (and why):
- “Which ML model or algorithm is powering the agent’s decision at runtime?” — because that’s the AI Core / Data Science lead’s territory.
- “What specific third-party licenses and vendor contracts govern the Moveworks/ServiceNow integrations?” — because that’s the Legal and Procurement territories.
- “What is the end-to-end risk score calculation algorithm used in the risk governance framework?” — because that’s the AI-DS Evaluation Lead’s territory.