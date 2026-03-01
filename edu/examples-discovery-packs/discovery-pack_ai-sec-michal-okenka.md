# Discovery Packet v1 — AI SEC
## Student: Michal Okenka
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: Do you have a complete, continuously updated inventory of all AI systems in production and experimentation (including HR, Claims, and prototypes)?
**Why this matters:** Without a centralized AI registry, governance, risk classification, and EU AI Act compliance cannot be enforced. Shadow AI creates regulatory, operational, and security blind spots.
**Red flag (bad answer):** “We don’t have full visibility” or “Departments manage their own AI independently.”
**KAF component:** Core / Ingestion

### Question 2: What governance capabilities are currently missing in ServiceNow/Moveworks (e.g., decision traceability, model versioning, bias monitoring, risk classification)?
**Why this matters:** Identifies gaps that ServiceNow alone cannot address and clarifies where additional governance and control layers are required.
**Red flag (bad answer):** “We assume ServiceNow handles compliance and governance for us.”
**KAF component:** Core / Run Safe

### Question 3: Which AI-related policies today are documented but not technically enforced (e.g., PII restrictions, approval workflows, escalation rules)?
**Why this matters:** EU AI Act compliance requires enforceable controls. Policies must be translated into Policy-as-Code to ensure consistent execution.
**Red flag (bad answer):** “Policies exist in documentation, but enforcement depends on teams following them manually.”
**KAF component:** Policy-as-Code

### Question 4: When a new regulation or internal AI policy is introduced, how long does it take to operationalize it across systems?
**Why this matters:** The board expects regulatory adaptation within weeks, not months. This reveals current operational agility and governance maturity.
**Red flag (bad answer):** “It usually takes 2–3 months to implement regulatory updates.”
**KAF component:** Core / Policy-as-Code

### Question 5: Can you reconstruct, end-to-end, how a specific AI-assisted decision was made — including input data, model version, rules applied, and human approvals?
**Why this matters:** Full traceability is essential for auditability, dispute resolution, and EU AI Act compliance.
**Red flag (bad answer):** “We can see the final outcome, but not the intermediate reasoning or applied rules.”
**KAF component:** Run Safe

### Question 6: How are AI systems monitored today across ServiceNow, legacy tools, and departmental experiments? Is monitoring centralized?
**Why this matters:** Fragmented monitoring creates security gaps, inconsistent logging, and delayed incident detection.
**Red flag (bad answer):** “Each system has its own dashboard; there’s no unified monitoring.”
**KAF component:** Run Safe / Interop

### Question 7: In your target state, which AI decisions should be fully automated, and where must human confirmation always be required?
**Why this matters:** Defines automation boundaries, risk tolerance, and mandatory Human-in-the-Loop checkpoints aligned with compliance requirements.
**Red flag (bad answer):** “We haven’t clearly defined automation thresholds or escalation triggers.”
**KAF component:** HITL / Core

### Question 8: Which enterprise systems must the future agentic platform securely integrate with (e.g., IAM, claims systems, HR tools, CMDB, SIEM)?
**Why this matters:** Identifies integration scope, connector requirements, and security architecture considerations for scalable operations.
**Red flag (bad answer):** “Departments build their own integrations without centralized standards.”
**KAF component:** Interop

### Question 9: How are AI-specific security risks addressed today (e.g., prompt injection, data leakage, unauthorized API access, model manipulation)?
**Why this matters:** AI introduces new threat vectors that require dedicated controls beyond traditional IT security practices.
**Red flag (bad answer):** “We treat AI systems like standard applications without additional controls.”
**KAF component:** Run Safe

### Question 10: Have you formally classified your AI use cases under EU AI Act risk categories, and is there clear accountability assigned per system?
**Why this matters:** Risk classification and ownership are foundational for enforceable governance and scalable compliance.
**Red flag (bad answer):** “We have not mapped AI systems to EU AI Act risk levels or assigned accountability.”
**KAF component:** Core / Policy-as-Code

---

## Part 2: KAF Mapping (mini)

| KAF Component        | Covered by Q# | Notes |
|----------------------|---------------|--------|
| Agentic Core         | Q1, Q2, Q4, Q7, Q10 | Governance foundation, risk classification, regulatory agility, automation boundaries, and ownership model for scalable agentic architecture. |
| Agentic Ingestion    | Q1            | Central AI registry and onboarding control to eliminate shadow AI and ensure 100% system coverage. |
| Policy-as-Code       | Q3, Q4, Q10   | Translation of documented policies into enforceable rules; regulatory change propagation in <2 weeks; codified risk-based controls. |
| Digital Trust        | Q5, Q6, Q9    | Full audit trail, unified monitoring, AI-specific threat controls (prompt injection, leakage), and production-safe logging. |
| Human-in-the-Loop    | Q7, Q5        | Defined escalation checkpoints and human validation for high-risk decisions and dispute reconstruction. |
| Interop (MCP/A2A)    | Q6, Q8        | Unified monitoring across fragmented tools and secure integrations with IAM, HR, Claims, CMDB, SIEM for scalable agent workflows. |

---

## Part 3: Assumptions / Risks / Open Items (3–5)

1. **Assumption: Executive sponsorship remains strong through implementation.**  
   The CIO and CISO alignment continues beyond discovery and governance enforcement is supported at board level — including shutting down shadow AI where required.

2. **Risk: Shadow AI expansion outpaces governance rollout.**  
   Departments (HR, Claims, Finance) may continue building AI prototypes without central onboarding, making 100% AI registry coverage difficult within 6 months.

3. **Risk: Regulatory interpretation ambiguity (EU AI Act).**  
   Final technical standards and supervisory guidance may evolve before 2027, requiring architectural flexibility to avoid rework.

4. **Open Item: Current security posture of AI integrations is unknown.**  
   It is unclear whether AI systems have undergone AI-specific threat modeling (prompt injection, data leakage, model abuse), which may increase remediation scope.

5. **Assumption: €180K budget is sufficient for governance foundation, but not full enterprise-scale rollout.**  
   Phase 1 likely covers registry, Policy-as-Code foundation, unified monitoring blueprint, and ServiceNow enhancement — Phase 2 scaling may require additional funding.

---

## Part 4: What We Will Measure (3 KPI proposals)

1. **AI Registry Coverage: 100% of AI systems inventoried and risk-classified**  
   Target: Eliminate shadow AI by achieving full registration and EU AI Act risk classification of all production and experimental AI systems within 6 months.

2. **Regulatory Adaptation Lead Time: < 2 weeks (from policy change to technical enforcement)**  
   Target: Reduce current ~3-month adaptation cycle to under 14 days through Policy-as-Code implementation and centralized governance controls.

3. **End-to-End AI Decision Auditability: 100% traceable decisions**  
   Target: Every AI-assisted action (e.g., ticket routing, claim triage, HR chatbot interaction) produces reconstructable logs including inputs, model version, applied policies, and human approvals.

---

## Part 5: Agent Classification

- **Governance tier:** Enterprise  
  The target platform impacts multiple business units (IT, HR, Claims, Finance) and operates under EU AI Act regulatory scope. Governance, auditability, and Policy-as-Code enforcement must be centrally managed and board-visible.

- **Registry/reuse potential:**  
  The governance framework, AI registry model, and Policy-as-Code enforcement layer should be registered in the Kyndryl Agent Catalog as a reusable "AI Governance & Compliance Accelerator" for regulated industries (insurance, healthcare, banking).  

  Core reusable components:
  - AI system registry template (risk classification + ownership model)
  - Policy-as-Code enforcement patterns (PII controls, escalation logic, HITL checkpoints)
  - Unified audit logging architecture blueprint
  - AI security control checklist (prompt injection, data leakage, model abuse)
  
  This enables replication across EU clients preparing for EU AI Act compliance before the 2027 enforcement deadline.

---

## Dependencies on Other Roles:

- I need the **AI Solution Architect** to ask about target reference architecture, on-prem infrastructure constraints, and scalability patterns because the agentic platform design and connector strategy must align with enterprise architecture standards.

- I need the **Data Governance / Privacy Lead** to ask about data lineage, PII classification, retention policies, and DPIA requirements because EU AI Act compliance and “no PII in training data” enforcement depend on formal data governance controls.

- I need the **ServiceNow Platform Owner** to clarify native capabilities and roadmap (Moveworks integration, logging, APIs) because we must avoid rebuilding functionality that already exists.

- I need the **Legal / Compliance Officer** to interpret EU AI Act risk classification and accountability requirements because regulatory interpretation drives Policy-as-Code implementation boundaries.

- I need the **Change & Adoption Lead** to assess organizational readiness and works council implications because governance enforcement (especially shutting down shadow AI) requires cultural and procedural alignment.

---

## Questions I Deliberately Did NOT Ask (and why):

- “What specific LLM or vendor should we use going forward?” — because tool/vendor selection belongs primarily to the Architecture and Procurement roles; my focus is governance and secure operationalization.

- “What training data should we fine-tune on?” — because model development strategy is owned by the Data/AI Engineering team; my concern is enforcing PII and risk controls regardless of model choice.

- “What is the expected ROI from automation?” — because financial modeling and business case ownership sits with the CIO/Finance stakeholders; my focus is compliance, risk reduction, and production safety.

- “How should the Service Desk workflows be redesigned?” — because detailed process redesign is the responsibility of ITSM/process owners; my role is to ensure AI decisions within those workflows are auditable and secure.

- “What UX should the HR or Claims chatbot have?” — because user experience design is not an AI-SEC responsibility; governance and risk controls apply independently of interface design.