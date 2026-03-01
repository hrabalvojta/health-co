# ====================================
# Discovery Packet v1 — Full-stack Development Engineer (FDE)
## Student: VLADIMIR FABER
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1:
“You achieved a 35% reduction in L1 tickets with ServiceNow AI and Moveworks. What governance or control gaps emerged after that acceleration?”

**Why this matters:** Rapid AI scaling often exposes monitoring, audit, and policy weaknesses.  
**Red flag (bad answer):** “We haven’t evaluated governance impact yet.”  
**KAF component:** Agentic Core  

---

### Question 2:
“Is there today a single control plane where all AI-assisted decisions across ServiceNow, Moveworks, and departmental tools are traceable end-to-end?”

**Why this matters:** Fragmented logging prevents regulatory traceability and enterprise visibility.  
**Red flag:** Logs exist per tool but are not centralized.  
**KAF component:** Run Safe  

---

### Question 3:
“If an EU regulator requested a full AI decision trace affecting a customer in one of your 8 EU countries, how quickly could you provide it?”

**Why this matters:** Tests EU AI Act operational readiness and cross-border compliance.  
**Red flag:** “We would need to manually gather logs.”  
**KAF component:** Digital Trust  

---

### Question 4:
“Do you maintain an enterprise-wide AI registry capturing ownership, risk classification, and lifecycle status of every AI-enabled workflow?”

**Why this matters:** Shadow AI without registry equals unmanaged compliance exposure.  
**Red flag:** Department-level tracking only.  
**KAF component:** Policy-as-Code  

---

### Question 5:
“Among the HR chatbot, Claims PoC, and Finance GPT, which operate outside centralized governance controls, and have they been formally risk-classified?”

**Why this matters:** Claims systems likely process high-risk health data under EU AI Act.  
**Red flag:** Informal or undocumented classification.  
**KAF component:** Policy-as-Code  

---

### Question 6:
“When AI agents trigger cross-system actions, how is identity propagation and role-based authorization enforced?”

**Why this matters:** Prevents privilege escalation and unauthorized automation.  
**Red flag:** Shared service accounts with broad permissions.  
**KAF component:** Interop (MCP/A2A)  

---

### Question 7:
“How are new AI tools ingested, validated, and approved before deployment into production?”

**Why this matters:** Defines lifecycle governance and onboarding discipline.  
**Red flag:** Pilot tools deployed without formal approval workflow.  
**KAF component:** Agentic Ingestion  

---

### Question 8:
“What is your incident response protocol if an AI system produces an incorrect or harmful customer-facing decision?”

**Why this matters:** Determines rollback capability and accountability structure.  
**Red flag:** No defined AI-specific playbook.  
**KAF component:** Human-in-the-Loop  

---

### Question 9:
“How are AI policies updated across systems when regulatory requirements change?”

**Why this matters:** Their KPI includes reducing regulatory adaptation time to under two weeks.  
**Red flag:** Manual, tool-by-tool configuration changes.  
**KAF component:** Policy-as-Code  

---

### Question 10:
“Where does AI telemetry live today, and who owns centralized monitoring across all AI platforms?”

**Why this matters:** Clarifies operational ownership and monitoring maturity.  
**Red flag:** Split responsibility between departments with no unified dashboard.  
**KAF component:** Run Safe  

---

## Part 2: KAF Mapping (mini)

| KAF Component      | Covered by Q# | Notes |
|--------------------|---------------|--------|
| Agentic Core       | 1             | Scaling impact on orchestration |
| Agentic Ingestion  | 7             | Onboarding shadow AI |
| Policy-as-Code     | 4, 5, 9       | Registry + classification + policy updates |
| Digital Trust      | 3             | Regulatory traceability |
| Human-in-the-Loop  | 8             | Incident escalation |
| Interop (MCP/A2A)  | 6             | Cross-system identity propagation |
| Run Safe           | 2, 10         | Observability & monitoring |

---

## Part 3: Assumptions / Risks / Open Items

1. At least one shadow AI tool processes sensitive PII without centralized logging.  
2. Policy enforcement is tool-specific rather than centralized.  
3. Audit trace retrieval likely exceeds regulatory expectations.  
4. Identity boundaries between systems may not enforce least privilege.  

---

## Part 4: What We Will Measure (3 KPI proposals)

1. % of AI systems formally registered in enterprise AI registry (Target: 100%)  
2. Regulatory trace retrieval time (Target: <24 hours)  
3. % of AI interactions covered by centralized audit logging (Target: 95%+)  

---

## Part 5: Agent Classification

- Governance tier: Enterprise  
- Registry/reuse potential: Governed Enterprise AI Control Plane pattern reusable for regulated EU insurance clients.

---

## Dependencies on Other Roles

- AI-SEC → Threat modeling and compliance validation  
- AI-DA → Data residency and PII governance  
- AI-PM → Roadmap alignment with Q3 2026 governance target  

---

## Questions I Deliberately Did NOT Ask (and why)

- “Which LLM provider are you using?” — Premature implementation detail.  
- “What embedding model or vector DB is deployed?” — Tactical engineering topic for later workshop.  
- “What is the chatbot UI stack?” — Not governance-critical at executive stage.  