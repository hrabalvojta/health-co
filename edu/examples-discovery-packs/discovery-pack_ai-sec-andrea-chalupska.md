# Discovery Packet v1 — AI‑SEC (AI Security Consultant)
## Student: Andrea Chalupská
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: What ServiceNow + Moveworks cannot do today
**Question text:**  
“You already run ServiceNow with Moveworks in production. From a security and governance perspective, what are the **top things you still cannot do today** that made you reach out to Kyndryl?”

**Why this matters:**  
This anchors discovery on **real gaps**, not features. It tells us where ServiceNow stops being sufficient for regulated, cross‑department AI.

**Red flag (bad answer):**  
“We just want more automation or a smarter chatbot.” → Signals misunderstanding of the industrialization problem.

**KAF component:** Core

---

### Question 2: Shadow AI visibility and stop authority
**Question text:**  
“You mentioned departmental AI experiments (HR chatbot, Claims prototype). How do you **currently detect** these, and who has the **authority to approve, quarantine, or shut them down**?”

**Why this matters:**  
Without discovery and enforcement authority, AI governance is advisory only and shadow AI will continue.

**Red flag (bad answer):**  
“Each department decides; security can only recommend.” → No enforceable governance.

**KAF component:** Core

---

### Question 3: What ‘defensible AI’ means to the board
**Question text:**  
“When the board or an auditor asks you to *prove* AI is under control, what **evidence** must you be able to show—not policies, but technical proof?”

**Why this matters:**  
Defines whether the target state is **audit‑ready Digital Trust** or document‑based compliance theatre.

**Red flag (bad answer):**  
“A governance framework deck should be enough.” → Paper compliance only.

**KAF component:** Run Safe

---

### Question 4: Policy‑as‑Code — non‑negotiable runtime rules
**Question text:**  
“If we translate governance into **Policy‑as‑Code**, what are the **non‑negotiable rules** that must be enforced automatically at runtime (data access, forbidden actions, escalation thresholds)?”

**Why this matters:**  
Separates documented intent from **machine‑enforced control**, which is the core differentiator for AI security.

**Red flag (bad answer):**  
“We’ll write policies and rely on teams to follow them.”

**KAF component:** Policy‑as‑Code

---

### Question 5: Speed of governance change (real example)
**Question text:**  
“When EU AI Act guidance or an internal policy changed recently, how long did it take to **update your AI controls**—days, weeks, or months? Are those updates live yet?”

**Why this matters:**  
Reveals operational maturity and whether governance can adapt at regulatory speed.

**Red flag (bad answer):**  
“Quarterly updates” or “we’re not sure.” → Too slow for AI regulation.

**KAF component:** Policy‑as‑Code

---

### Question 6: Identity and least‑privilege model for agents
**Question text:**  
“How should AI agents be authorized to act—**as the user**, via **service identities**, or hybrid—and what are the **hard least‑privilege boundaries**, especially across countries?”

**Why this matters:**  
Defines trust boundaries, blast radius, and auditability of agent actions.

**Red flag (bad answer):**  
“Shared admin accounts are fine.” → Major security exposure.

**KAF component:** Interop

---

### Question 7: ‘No PII in training’ — what about prompts and logs?
**Question text:**  
“You’ve set ‘no PII in training data.’ What data is allowed in **retrieval (RAG)**, **prompts**, and **logs**, and what must be automatically blocked or masked?”

**Why this matters:**  
Most real data leaks happen via prompts, retrieval, and logs—not model training.

**Red flag (bad answer):**  
“We’ll rely on user discipline.” → No technical protection.

**KAF component:** Ingestion

---

### Question 8: Agentic workflows and human checkpoints
**Question text:**  
“For 2–3 workflows you want to industrialize beyond IT helpdesk, which **steps must require human approval**, and which can be autonomous?”

**Why this matters:**  
Human‑in‑the‑loop must be **designed per step**, not added later as a blanket rule.

**Red flag (bad answer):**  
“Full autonomy is fine” or “we haven’t thought about approvals.”

**KAF component:** HITL

---

### Question 9: Tool integrations and MCP governance
**Question text:**  
“What is your governance model for **adding new tools or integrations** (HR, Claims, legacy systems)? Do you want a **standard connector approach** with centralized policy enforcement?”

**Why this matters:**  
Prevents uncontrolled agent access to systems and enables scalable, auditable interoperability.

**Red flag (bad answer):**  
“Teams can integrate whatever they need.” → Fragmented risk surface.

**KAF component:** Interop

---

### Question 10: Run Safe — monitoring, audit logs, kill switch
**Question text:**  
“What must be logged for **every AI action**, where do those logs live, and what are the **triggers to pause or roll back** AI behavior?”

**Why this matters:**  
Defines production safety, incident response, and forensic readiness.

**Red flag (bad answer):**  
“We don’t need detailed logs” or “we’ll handle incidents ad‑hoc.”

**KAF component:** Run Safe

> Minimum coverage check:
> - Policy‑as‑Code: Q4, Q5 ✅  
> - MCP/A2A Interop: Q9 ✅  
> - Human‑in‑the‑Loop: Q8 ✅

---

## Part 2: KAF Mapping (mini)

| KAF Component        | Covered by Q# | Notes |
|---------------------|---------------|-------|
| Agentic Core        | 1, 2          | Scope, ownership, ServiceNow gaps |
| Agentic Ingestion   | 7             | Data controls beyond training |
| Policy‑as‑Code      | 4, 5          | Runtime enforcement & change speed |
| Digital Trust       | 3, 10         | Auditability, monitoring, incidents |
| Human‑in‑the‑Loop   | 8             | Explicit approval checkpoints |
| Interop (MCP/A2A)   | 6, 9          | IAM + integration governance |

---

## Part 3: Assumptions / Risks / Open Items (3–5)
1. Governance is currently advisory, not enforceable.
2. Policy changes take weeks/months, not days.
3. “No PII in training” does not yet cover prompts and logs.
4. Ownership of AI as a system of record is unclear.
5. Shadow AI discovery is incomplete or manual.

---

## Part 4: What We Will Measure (3 KPI proposals)
1. **AI inventory coverage:** ≥95% of AI systems registered with owner and risk tier.
2. **Policy change lead time:** ≤5 business days from rule change to enforcement.
3. **Audit trace completeness:** ≥99% of AI actions with end‑to‑end trace.

---

## Part 5: Agent Classification
- **Governance tier:** Enterprise
- **Registry/reuse potential:** High — reusable governance patterns and policy packs across Kyndryl engagements.

---

## Dependencies on Other Roles:
- I need **AI‑PM** to confirm business priorities and board success criteria.
- I need **FDE / AI‑SE** to validate on‑prem constraints and CI/CD controls.
- I need **AI‑DS** to cover evaluation strategy and knowledge base structure.

---

## Questions I Deliberately Did NOT Ask (and why):
- “What’s your tech stack?” — already known from the brief (ServiceNow + Moveworks).
- “Which LLM do you want?” — solutioning too early; controls come first.