# Discovery Packet v1 — AI Product Manager

## Student: Sebastien Vallon

## Date: February 23, 2026

## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: Where do you believe your current ServiceNow + Moveworks setup will fall short in meeting EU AI Act governance and audit expectations by 2027?

**Why this matters:** This anchors the discussion on board-level regulatory risk rather than feature improvement. It surfaces governance gaps and creates urgency for industrialization.
**Red flag (bad answer):** “ServiceNow already handles compliance.” → Indicates governance overconfidence and possible audit blind spots.
**KAF component:** Policy-as-Code / Run Safe / Interop

---

### Question 2: When this engagement is finished, what must be true for you to confidently say: “Our AI is under control and defensible”?

**Why this matters:** Defines success in terms of risk, accountability, and auditability—not performance metrics alone.
**Red flag (bad answer):** Success defined only by CSAT or automation rate.
**KAF component:** Run Safe / Policy-as-Code

---

### Question 3: What formal inventory exists today of all AI systems in production (ServiceNow, HR chatbot, Claims PoC, Finance GPT), and who formally owns that registry?

**Why this matters:** Governance begins with visibility and ownership. Without an inventory, compliance cannot scale.
**Red flag (bad answer):** No centralized registry or unclear ownership.
**KAF component:** Ingestion / Policy-as-Code

---

### Question 4: Which regulatory, internal, and security rules must be enforceable as policy-as-code today (not just documented)?

**Why this matters:** Identifies what must move from PDF policy into executable guardrails to achieve EU AI Act readiness.
**Red flag (bad answer):** Governance exists only in documentation, not enforceable controls.
**KAF component:** Policy-as-Code

---

### Question 5: Which audit artifacts are required by the board or CISO (immutable logs, model versioning, decision traces, data lineage), and for how long must they be retained?

**Why this matters:** Defines audit architecture and storage implications early under budget constraint.
**Red flag (bad answer):** No defined retention policy or unclear audit expectations.
**KAF component:** Run Safe

---

### Question 6: Which AI-driven decisions require mandatory human confirmation—and how is that technically enforced?

**Why this matters:** Clarifies risk delegation boundaries and ensures Human-in-the-Loop is intentional, not reactive.
**Red flag (bad answer):** Escalation only occurs when something fails.
**KAF component:** HITL / Policy-as-Code

---

### Question 7: How do you monitor AI systems in production beyond uptime—drift, bias, hallucination, misuse?

**Why this matters:** Industrialization requires operational AI monitoring, not just system availability.
**Red flag (bad answer):** Monitoring limited to uptime or infrastructure metrics.
**KAF component:** Run Safe

---

### Question 8: Is AI formally integrated into your enterprise cyber risk framework, or governed as a separate initiative?

**Why this matters:** Determines whether AI governance is embedded into enterprise risk management or treated as experimental.
**Red flag (bad answer):** AI treated as innovation initiative outside formal risk oversight.
**KAF component:** Run Safe / Policy-as-Code

---

### Question 9: Given the on-prem restriction and €180K/6-month limit, what is your minimum viable governance platform you are prepared to fund—and what would you consciously de-scope?

**Why this matters:** Forces prioritization under constraint and prevents scope creep.
**Red flag (bad answer):** Refusal to prioritize or unwillingness to de-scope.
**KAF component:** Core

---

### Question 10: To reduce governance complexity and maintenance risk, would you support consolidating AI interactions into a single enterprise-grade governed layer—even if that requires re-architecting existing bots?

**Why this matters:** Tests appetite for structural change versus incremental optimization.
**Red flag (bad answer):** Desire for centralized governance without architectural change.
**KAF component:** Core / Interop / Run Safe

---

> Minimum coverage satisfied:
>
> * Policy-as-Code: Q1, Q2, Q4, Q6, Q8
> * Interop (MCP/A2A): Q1, Q10
> * Human-in-the-Loop: Q6

---

## Part 2: KAF Mapping (mini)

| KAF Component     | Covered by Q# | Notes                                   |
| ----------------- | ------------- | --------------------------------------- |
| Agentic Core      | 9, 10         | Platform scope & consolidation decision |
| Agentic Ingestion | 3             | AI inventory & ownership                |
| Policy-as-Code    | 1, 2, 4, 6, 8 | Governance enforcement                  |
| Digital Trust     | 1, 2, 5, 7, 8 | Auditability & monitoring               |
| Human-in-the-Loop | 6             | Delegation boundaries                   |
| Interop (MCP/A2A) | 1, 10         | Cross-system orchestration              |

---

## Part 3: Assumptions / Risks / Open Items (3-5)

1. EuroHealth currently lacks a centralized AI registry.
2. Governance rules are partially documented but not codified.
3. Audit retention requirements may exceed current infrastructure capacity.
4. Budget constraints may limit full consolidation in Phase 1.
5. Board pressure is primarily regulatory rather than performance-driven.

---

## Part 4: What We Will Measure (3 KPI proposals)

1. AI Registry Coverage: 0% → 100% of AI systems inventoried
2. Regulatory Adaptation Speed: ~3 months → < 2 weeks
3. Full Audit Traceability: 100% of AI-assisted decisions logged

---

## Part 5: Agent Classification

* **Governance tier:** Enterprise
* **Registry/reuse potential:** Register as enterprise-governed KAF template for reuse across regulated clients requiring on-prem AI governance foundation.

---

## Dependencies on Other Roles:

* I need AI-SEC to detail enforcement mechanisms for policy-as-code and audit logging.
* I need AI-SE to assess monitoring, CI/CD, and model version control implications.
* I need FDE to evaluate on-prem LLM hosting and integration feasibility.

---

## Questions I Deliberately Did NOT Ask (and why):

* “Which LLM vendor should we use?” — Because that is architectural and premature before governance scope is defined.
* “What UI improvements do you need?” — Because this engagement is governance-led, not interface-led.

---
