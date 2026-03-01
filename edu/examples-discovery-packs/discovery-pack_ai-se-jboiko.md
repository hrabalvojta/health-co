# Discovery Packet v1 — AI-SE (AI Software Engineering)
## Student: Julia Boiko
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1 (PRIMARY)
**You already use ServiceNow with Moveworks. What specifically can’t you do today—technically or operationally—that made you reach out to Kyndryl?**

**Why this matters:**  
This question surfaces the real gap between platform capabilities and enterprise-grade AI operations. It determines whether the problem is governance, compliance, scaling, auditability, or operational control—and prevents solving the wrong problem.

**Red flag (bad answer):**  
“We just want to use AI more” or “Everyone else is doing it” → no clear value driver, executive pressure without problem clarity.

**KAF component:** Policy-as-Code (primary), Run Safe (secondary)

---

### Question 2
**Which AI-driven decisions today cannot be reconstructed end-to-end for audit or regulatory review?**

**Why this matters:**  
EU AI Act readiness depends on traceability of decisions, not just partial logs inside one tool.

**Red flag:**  
“We log some things in ServiceNow” → fragmented, non-compliant audit trail.

**KAF component:** Run Safe

---

### Question 3
**How do you currently detect, govern, or shut down shadow AI solutions built outside the IT organization?**

**Why this matters:**  
Shadow AI represents the highest compliance and security risk and is already flagged by the CISO.

**Red flag:**  
“We rely on policy reminders or guidelines” → governance is not enforceable.

**KAF component:** Policy-as-Code

---

### Question 4
**When regulations or internal AI policies change, how long does it take to update controls across all AI systems—days, weeks, or months?**

**Why this matters:**  
Regulatory adaptation speed is a board-level concern and a core success metric for this engagement.

**Red flag:**  
“We review changes quarterly” → governance is procedural, not operational.

**KAF component:** Run Safe

---

### Question 5
**Which rules must be enforced directly in code to prevent AI agents from accessing restricted data or tools?**

**Why this matters:**  
Policy-as-Code ensures agents cannot violate rules, rather than hoping developers follow documentation.

**Red flag:**  
“We document rules and trust teams to follow them” → non-enforceable governance.

**KAF component:** Policy-as-Code

---

### Question 6
**What steps should an enterprise agent be allowed to plan autonomously, and where must execution be restricted or validated?**

**Why this matters:**  
Unbounded agent autonomy creates unacceptable risk in regulated environments.

**Red flag:**  
“The agent can decide everything” → lack of control model.

**KAF component:** Agentic Core

---

### Question 7
**Which AI-driven actions require mandatory human approval before execution?**

**Why this matters:**  
Human-in-the-loop checkpoints are mandatory for enterprise-tier agents under EU AI Act expectations.

**Red flag:**  
“Humans can review later if needed” → no enforced checkpoints.

**KAF component:** Human-in-the-Loop (HITL)

---

### Question 8
**Which systems must the agent integrate with beyond ServiceNow, and how is access governed across those integrations?**

**Why this matters:**  
Cross-system orchestration without identity and authorization controls introduces hidden security risks.

**Red flag:**  
“We’ll just connect it” → unmanaged interoperability.

**KAF component:** Interoperability (MCP / A2A)

---

### Question 9
**How is AI behavior monitored in production today, and how quickly can non-compliant behavior be detected?**

**Why this matters:**  
Monitoring determines whether AI incidents are detected in minutes or during audits.

**Red flag:**  
“We manually review logs” → reactive operations.

**KAF component:** Run Safe

---

### Question 10
**If an external auditor reviewed your AI systems tomorrow, which finding would concern you most?**

**Why this matters:**  
This exposes hidden risks and unspoken executive concerns that drive real buying decisions.

**Red flag:**  
“We haven’t thought about that yet” → governance immaturity.

**KAF component:** Run Safe

---

## Part 2: KAF Mapping

| KAF Component | Covered by Questions | Notes |
|--------------|---------------------|------|
| Agentic Core | Q6 | Agent autonomy boundaries |
| Agentic Ingestion | Q8 | Tool and system access |
| Policy-as-Code | Q1, Q3, Q5 | Enforceable governance |
| Digital Trust / Run Safe | Q2, Q4, Q9, Q10 | Audit, monitoring, compliance |
| Human-in-the-Loop | Q7 | Mandatory approvals |
| Interoperability (MCP/A2A) | Q8 | Cross-system orchestration |

---

## Part 3: Assumptions / Risks / Open Items

1. Shadow AI usage is broader than currently documented.
2. Audit trails outside ServiceNow are incomplete or inconsistent.
3. Regulatory adaptation relies on manual processes.
4. On-prem constraints may slow tooling changes.

---

## Part 4: What We Will Measure (KPI Proposals)

1. **Regulatory adaptation time:** ~3 months → < 2 weeks  
2. **AI systems under governance:** < 50% → 100% registered  
3. **Audit completeness:** Partial → Full end-to-end traceability  

---

## Part 5: Agent Classification

- **Governance tier:** Enterprise  
- **Registry / reuse potential:** Central AI registry reusable across IT, HR, Claims in Phase 2  

---

## Dependencies on Other Roles

- AI-SEC: threat modeling, regulatory interpretation  
- FDE: on-prem hosting constraints  
- AI-DA: operational dashboards and metrics  

## Questions Deliberately Not Asked

- UI/UX specifics — covered by AI-FE  
- Business prioritization — covered by AI-PM
