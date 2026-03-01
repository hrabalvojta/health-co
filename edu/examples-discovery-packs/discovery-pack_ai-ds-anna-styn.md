# Discovery Packet v1 — AI Data Scientist (AI-DS)
## Student: Anna Styn
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

# Part 1: Clear Understanding of the Situation (in simple words)

EuroHealth already has AI (ServiceNow + Moveworks).  
It reduced ticket volume by ~35%.

But the real problems are:

- No unified AI governance
- Shadow AI in HR, Claims, Finance
- No full audit trail of AI decisions
- Slow regulatory adaptation (~3 months)
- Fragmented monitoring systems
- Multilingual requirement (EN/DE/CZ)
- On‑prem only deployment
- No employee PII allowed in training data

This is NOT a chatbot project.  
It is an AI industrialization + governance transformation.

---

# Part 2: Discovery Questions (10)

## Question 1 — Decision Impact & Risk Tolerance

**Question:**  
Which business decisions will this AI system directly influence in Phase 1, and what error rate (misroute, wrong resolution, incorrect escalation) is acceptable before it becomes operational or regulatory risk?

**Why this matters:**  
If we don’t define acceptable error, we cannot define evaluation thresholds, human checkpoints, or automation boundaries.

**Red flag:**  
“We haven’t defined acceptable error.”

**KAF Component:** Agentic Core + Run Safe

---

## Question 2 — Single Source of Truth

**Question:**  
What will be the single source of truth for knowledge (KB articles, SOPs, policies), and who owns keeping it accurate for the next 2+ years?

**Why this matters:**  
AI quality depends on clean, authoritative knowledge. Conflicting documents cause hallucinations and audit failures.

**Red flag:**  
“Everyone has their own documents.”

**KAF Component:** Ingestion

---

## Question 3 — Multilingual Quality (EN/DE/CZ)

**Question:**  
Do you expect equal AI quality across EN/DE/CZ, and how do you currently measure routing or understanding errors by language?

**Why this matters:**  
Hidden performance gaps often appear in non-English languages.

**Red flag:**  
“We will focus on English first.”

**KAF Component:** Ingestion + Run Safe

---

## Question 4 — Data Boundaries & Privacy

**Question:**  
Given that no employee PII can be used in training data, what data is legally allowed for evaluation and monitoring, and how will it be anonymized?

**Why this matters:**  
Without clear legal data boundaries, evaluation and improvement pipelines cannot be built safely.

**Red flag:**  
“We’ll decide later.”

**KAF Component:** Ingestion + Run Safe

---

## Question 5 — Policy-as-Code (Hard Stops)

**Question:**  
Which governance rules must be enforced directly in code (e.g., PII restrictions, escalation rules), and what happens if a rule is violated?

**Why this matters:**  
Policies must be enforceable, not just documented.

**Red flag:**  
“Our policies are in PDFs.”

**KAF Component:** Policy-as-Code

---

## Question 6 — Regulatory Adaptation Speed

**Question:**  
What is your current workflow when regulation changes, and what prevents reducing adaptation time from 3 months to under 2 weeks?

**Why this matters:**  
Industrialization means fast policy updates.

**Red flag:**  
“Multiple committees with no clear SLA.”

**KAF Component:** Policy-as-Code + Run Safe

---

## Question 7 — Audit Trail Requirements

**Question:**  
What exactly must be logged for every AI-assisted decision (inputs, retrieved documents, model version, approvals, actions)?

**Why this matters:**  
Full auditability is a core success requirement.

**Red flag:**  
“ServiceNow logs are enough.”

**KAF Component:** Run Safe

---

## Question 8 — Human-in-the-Loop

**Question:**  
Which decisions require mandatory human approval, and what is the required turnaround time?

**Why this matters:**  
Defines safe automation boundaries.

**Red flag:**  
“No human oversight needed.”

**KAF Component:** Human-in-the-Loop

---

## Question 9 — System Integrations

**Question:**  
Which systems must the AI agent integrate with in Phase 1 (ServiceNow, monitoring, identity systems), and what integration method is allowed on-prem?

**Why this matters:**  
Without integrations, AI cannot act — only suggest.

**Red flag:**  
“No integrations allowed.”

**KAF Component:** Interop (MCP/A2A)

---

## Question 10 — Shadow AI Governance

**Question:**  
How will shadow AI tools be identified and brought into a centralized AI registry, and who is the executive owner?

**Why this matters:**  
Without registry completeness, governance is incomplete.

**Red flag:**  
“Departments manage their own tools.”

**KAF Component:** Run Safe + Core

---

# Part 3: KAF Mapping Table

| KAF Component | Covered by Questions |
|---------------|---------------------|
| Agentic Core | 1, 10 |
| Ingestion | 2, 3, 4 |
| Policy-as-Code | 5, 6 |
| Run Safe | 1, 4, 6, 7, 10 |
| Human-in-the-Loop | 8 |
| Interop | 9 |

---

# Part 4: Proposed KPIs (Explained Clearly)

## KPI 1 — Audit Coverage KPI

Audit Coverage =  
(Number of AI decisions with complete audit log)  
/  
(Total AI-assisted decisions)

Target: 100%

Example:

If AI handled 10,000 tickets in a month,  
all 10,000 must have:

- Input stored
- Model version stored
- Retrieved documents logged
- Policy checks logged
- Human approvals logged (if required)

If 9,800 are logged → Audit Coverage = 98% (not acceptable).

---

## KPI 2 — AI Registry Completeness

AI Registry Completeness =  
(Number of AI systems officially registered)  
/  
(Number of AI systems actually running)

Target: 100%

Example:

If HR chatbot + Claims tool + Finance GPT + ServiceNow AI exist → all must be registered.

If 3 out of 4 are registered → 75% → governance failure.

---

## KPI 3 — Regulatory Adaptation Speed

Regulatory Adaptation Time =  
Time from policy change request  
to policy implemented in production

Current: ~3 months  
Target: < 14 days

Example:

If EU rule changes on March 1,  
new policy must be active before March 15.

---

## KPI 4 — Helpdesk Outcome KPI

CSAT improvement from 3.6 → 4.2+

---

# Part 5: Risks & Blockers

## Data Risk
Evaluation may be blocked due to privacy constraints.

Mitigation:
Build anonymization + synthetic datasets.

## Governance Risk
No executive owner for AI registry.

Mitigation:
Assign board-level sponsor.

## Integration Risk
On-prem infrastructure limitations.

Mitigation:
Early technical validation sprint.

---

# Part 6: My Focus as AI-DS

My primary responsibility:

- Define measurable AI quality thresholds
- Design multilingual evaluation framework
- Build privacy-safe evaluation datasets
- Define audit logging schema
- Monitor drift and performance degradation
- Ensure compliance metrics are trackable

Without AI-DS:

- Governance is theoretical
- Compliance is paperwork
- AI quality is guesswork

With AI-DS:

- AI becomes measurable
- Risk becomes quantifiable
- Decisions become defendable

---

End of Discovery Packet v1
