# Discovery Packet v1 — AI-DS (Data Scientist)
## Student: [Your Name]
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

# Part 1: Discovery Questions (10)

---

## Question 1: Decision & Risk Exposure
**Which operational or compliance decisions will this AI system directly influence, and what is the defined escalation path if a wrong recommendation occurs?**

**Why this matters:**  
Defines risk classification and determines required Human-in-the-Loop controls for high-risk insurance or compliance decisions.

**Red flag (bad answer):**  
Escalation is informal or not formally documented.

**KAF component:** Agentic Core + Human-in-the-Loop (HITL)

---

## Question 2: Auditability & Evidence
**When the AI agent makes a recommendation, what validation, logging, and audit mechanisms ensure that decision is traceable — and where is that evidence stored?**

**Why this matters:**  
EU AI Act readiness and board-level governance require full traceability of AI decisions across systems.

**Red flag:**  
Only partial logging in ServiceNow; other AI tools are unlogged.

**KAF component:** Run Safe + Policy-as-Code

---

## Question 3: Success Metrics & Multilingual Consistency
**What business outcomes define success for this agent in production, and how will those metrics be measured consistently across EN, DE, and CZ users?**

**Why this matters:**  
Multilingual inconsistencies can introduce hidden risk, bias, or performance drift.

**Red flag:**  
Performance is assumed to be uniform across languages without measurement.

**KAF component:** Agentic Core + Run Safe

---

## Question 4: Evaluation Maturity
**How do you currently evaluate AI output quality — structured test sets, human sampling, automated benchmarks — and how frequently is this reviewed?**

**Why this matters:**  
Distinguishes industrial AI operations from PoC experimentation.

**Red flag:**  
Only ticket deflection rate is tracked.

**KAF component:** Agentic Core + Run Safe

---

## Question 5: Source of Truth & Knowledge Governance
**What is the authoritative single source of truth for knowledge, policies, and operational logs the agent relies on — and how is that source versioned and maintained?**

**Why this matters:**  
Unstructured or fragmented knowledge bases increase hallucination and compliance risk.

**Red flag:**  
Each department maintains independent documentation without version control.

**KAF component:** Agentic Ingestion

---

## Question 6: Regulatory Adaptation Speed
**When policies or EU AI Act guidance change, how long does it take to update the AI system — and how is compliance validation performed after updates?**

**Why this matters:**  
Current adaptation time (~3 months) is incompatible with regulatory responsiveness targets.

**Red flag:**  
Manual document updates with no structured validation pipeline.

**KAF component:** Policy-as-Code + Run Safe

---

## Question 7: Shadow AI Governance & Executive Accountability
**How are departmental AI tools (HR, Claims, Finance) inventoried and governed today — and who has executive accountability for enforcing AI policy?**

**Why this matters:**  
Shadow AI without inventory or governance presents compliance and data leakage risks.

**Red flag:**  
No formal AI registry or ownership model exists.

**KAF component:** Policy-as-Code

---

## Question 8: Access Controls & Data Boundaries
**What role-based access controls must be enforced at the model and data level, particularly for sensitive policy or claims data?**

**Why this matters:**  
On-prem and GDPR constraints require strict data segmentation and model-level governance.

**Red flag:**  
Access control is handled only at application level, not at model/data layer.

**KAF component:** Policy-as-Code + Interoperability (MCP)

---

## Question 9: Non-Functional Production Constraints
**What non-functional constraints — latency thresholds, uptime SLAs, and on-prem hosting limitations — must the model adhere to in production?**

**Why this matters:**  
Industrial AI must meet measurable production SLAs, especially in an on-prem environment.

**Red flag:**  
No defined latency or availability thresholds.

**KAF component:** Agentic Core

---

## Question 10: Drift & Continuous Monitoring
**How do you detect model drift, performance degradation, or emerging bias over time — especially across different countries and departments?**

**Why this matters:**  
A 2+ year lifecycle requires continuous monitoring and structured re-evaluation.

**Red flag:**  
No formal drift detection or periodic re-evaluation process.

**KAF component:** Run Safe

---

# Part 2: KAF Mapping Summary

| KAF Component        | Covered by Q# | Notes |
|----------------------|---------------|-------|
| Agentic Core         | 1, 3, 4, 9    | Decision logic, evaluation, production SLAs |
| Agentic Ingestion    | 5             | Knowledge base governance |
| Policy-as-Code       | 2, 6, 7, 8    | Audit, regulatory adaptation, access control |
| Digital Trust (Run Safe) | 2, 3, 4, 6, 10 | Logging, evaluation, drift monitoring |
| Human-in-the-Loop    | 1             | Escalation & remediation |
| Interop (MCP/A2A)    | 8             | Access control & data boundaries |

---

# Part 3: Assumptions / Risks / Open Items

1. AI governance maturity is currently fragmented and reactive.
2. No centralized AI registry exists for shadow AI tools.
3. Multilingual performance is not independently evaluated.
4. Regulatory updates are manually propagated and slow.
5. Evaluation practices focus on volume reduction rather than quality assurance.

---

# Part 4: Proposed KPI Targets

1. **L1 Deflection Rate:** 35% → 50% (without quality degradation)
2. **Regulatory Adaptation Time:** ~3 months → <2 weeks
3. **CSAT Score:** 3.6 → 4.2+
4. **AI Registry Coverage:** 0% → 100% inventoried AI systems
5. **Drift Detection Cycle:** Quarterly evaluation with documented review

---

# Part 5: Agent Classification

- **Governance Tier:** Enterprise Agent  
- **Registry/Reuse Potential:**  
  This agent should be registered within a centralized AI governance registry with reusable policy modules (Policy-as-Code) for future Phase 2 expansion (HR, Claims, Finance).

---

# Dependencies on Other Roles

- AI-SEC: Detailed threat modeling and compliance validation.
- AI-SE: CI/CD and monitoring implementation design.
- FDE: On-prem hosting and infrastructure integration.
- AI-PM: KPI prioritization and board-level stakeholder alignment.
- AI-DA: Dashboarding and operational reporting framework.

---

# Questions I Deliberately Did NOT Ask (and why)

- “Which LLM vendor should we use?” — premature without governance clarity.
- “What is your tech stack?” — already defined in the brief (ServiceNow + on-prem).
- “Do you want a chatbot?” — this is an industrialization engagement, not a greenfield build.
