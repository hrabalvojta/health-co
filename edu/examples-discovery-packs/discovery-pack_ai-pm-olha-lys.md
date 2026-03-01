# Discovery Packet v2 — AI-PM (AI Product Manager)

## Student: Olha Lys  
## Date: February 23, 2026  
## Client: EuroHealth Insurance AG  

---

# Part 1: Discovery Questions (10)

---

## Question 1 — Delegation & Risk Boundary

**Question:**  
What business-critical decisions are you prepared to let AI influence or automate by 2027 — and where must human accountability remain non-negotiable?

**Why this matters:**  
Defines EU AI Act risk classification, Human-in-the-Loop enforcement depth, monitoring requirements, and liability exposure.

**Red flag (bad answer):**  
No defined delegation boundary → AI may already influence decisions without formal governance.

**KAF component:** Core / HITL

---

## Question 2 — Industrialization Gap Beyond ServiceNow

**Question:**  
Where does ServiceNow + Moveworks stop today in terms of enforceable governance, auditability, or cross-department scaling — and what cannot be solved within that platform alone?

**Why this matters:**  
Separates feature tuning from enterprise governance transformation. Clarifies why industrialization is needed.

**Red flag:**  
Focus only on accuracy or UX improvements.

**KAF component:** Interop / Policy-as-Code

---

## Question 3 — Board-Level Definition of “Controlled AI” (Q3 2026)

**Question:**  
By Q3 2026, what measurable governance or risk-reduction evidence must exist for the board to consider EuroHealth’s AI environment controlled and defensible?

**Why this matters:**  
Aligns €180K / 6-month scope with executive expectations and prevents scope creep.

**Red flag:**  
“All of the above” (cost, CSAT, compliance) without prioritization.

**KAF component:** Core

---

## Question 4 — Non-Negotiable Policy-as-Code Controls

**Question:**  
Which AI-related rules must be technically impossible to bypass — even by administrators — across all AI systems?

*(e.g., no PII in training data, mandatory approval for sensitive actions, retention enforcement, restricted tool calls)*

**Why this matters:**  
Distinguishes documented governance from enforceable runtime controls.

**Red flag:**  
“We rely on process discipline and internal guidelines.”

**KAF component:** Policy-as-Code

---

## Question 5 — Regulatory Agility

**Question:**  
When regulatory guidance or internal AI risk policy changes, how long does it take to update controls across all active AI workflows — days, weeks, or months?

**Why this matters:**  
Industrial AI requires rapid policy propagation, especially before Dec 2027 EU AI Act enforcement.

**Red flag:**  
Requires a separate project or quarterly release cycle for every change.

**KAF component:** Policy-as-Code / Run Safe

---

## Question 6 — Auditability Under Challenge

**Question:**  
If a regulator challenged a specific AI-assisted decision tomorrow, could you produce — within 24 hours — the model version, data source, tool calls, policy checks, and approval chain involved?

**Why this matters:**  
Tests Digital Trust maturity, audit ownership, and operational readiness.

**Red flag:**  
“We would reconstruct it manually” or “The vendor handles that.”

**KAF component:** Run Safe

---

## Question 7 — Data Boundary & On-Prem Interpretation

**Question:**  
Under your on-prem mandate, what data categories are allowed to cross infrastructure boundaries — and what enforcement mechanisms guarantee that constraint?

**Why this matters:**  
Clarifies integration feasibility and enforces “no PII in training data” constraint operationally.

**Red flag:**  
Blanket “no cloud” without data classification or enforcement logic.

**KAF component:** Ingestion / Policy-as-Code

---

## Question 8 — Cross-Department Scaling Authority

**Question:**  
Are you prepared to mandate a centralized AI governance control layer across HR, Claims, Finance, and IT — or will departments retain autonomy?

**Why this matters:**  
Industrialization requires structural authority to eliminate shadow AI and unify enforcement.

**Red flag:**  
Departments manage AI independently without central oversight.

**KAF component:** Core / Interop

---

## Question 9 — Runtime Monitoring & Production Safety

**Question:**  
Beyond uptime, what runtime signals must trigger automatic blocking, escalation, or human review in production?

*(e.g., policy violations, anomalous tool usage, drift, misuse attempts)*

**Why this matters:**  
Industrial AI requires behavioral observability and enforcement, not static deployment.

**Red flag:**  
Monitoring limited to vendor dashboards or availability metrics.

**KAF component:** Run Safe

---

## Question 10 — Program Ownership & Decision Cadence

**Question:**  
Who owns enterprise AI risk today, and what is the decision cadence for approving governance rules, integrations, and policy updates?

**Why this matters:**  
Prevents governance bottlenecks and ensures sustainable enterprise AI control beyond this 6-month engagement.

**Red flag:**  
No clear executive sponsor or fragmented veto authority.

**KAF component:** Core

---

# Part 2: KAF Mapping (Mini)

| KAF Component        | Covered by Q# | Notes |
|----------------------|---------------|-------|
| Agentic Core         | 1, 3, 8, 10   | Risk boundary, board mandate, scaling authority |
| Agentic Ingestion    | 7             | Data boundary & PII enforcement |
| Policy-as-Code       | 2, 4, 5, 7    | Enforceable governance & propagation speed |
| Digital Trust (Run Safe) | 5, 6, 9 | Auditability & runtime monitoring |
| Human-in-the-Loop    | 1             | Accountability & decision checkpoints |
| Interop (MCP/A2A)    | 2, 8          | Cross-system scaling & governance centralization |

---

# Part 3: Assumptions / Risks / Open Items

1. Governance may currently rely heavily on vendor capabilities rather than enterprise-level enforcement.
2. Policy updates likely follow traditional IT release cycles (slow regulatory adaptation risk).
3. Board-level AI oversight may not yet be formalized.
4. Departmental AI initiatives may operate outside centralized governance.
5. Budget constraint (€180K / 6 months) requires strict prioritization.

---

# Part 4: KPI Proposals (3)

1. **Mean Time to Evidence (MTTE): ≤ 24 hours**  
   Ability to reconstruct full AI decision trace on demand.

2. **Governed Workflow Coverage: ≥ 80% of in-scope AI systems under centralized Policy-as-Code enforcement within Phase 1.**

3. **Policy Update Propagation Time: < 5 business days from governance approval to production enforcement.**

---

# Part 5: Agent Classification

- **Governance tier:** Enterprise  
- **Registry / Reuse Potential:**  
  Establish centralized AI Governance Control Layer template reusable across HR, Claims, Finance, and future EU-regulated deployments.

---

# Dependencies on Other Roles

- **AI-SEC:** Risk classification, regulatory posture, enforcement validation.
- **FDE:** On-prem hosting feasibility and enforcement insertion points.
- **AI-SE:** CI/CD integration and monitoring infrastructure.
- **AI-DS:** Knowledge quality and evaluation framework.
- **AI-DA:** Executive reporting and governance dashboards.

---

# Questions I Deliberately Did NOT Ask (and Why)

- Detailed LLM hosting architecture → FDE domain.
- CI/CD implementation specifics → AI-SE domain.
- Model evaluation metrics → AI-DS domain.
- Vendor selection discussion → premature before governance scope clarity.

---

## Positioning Statement for the Meeting

We are not here to make your AI smarter.  
We are here to make it governable, enforceable, auditable, and scalable under EU AI Act pressure — within 6 months and €180K.
