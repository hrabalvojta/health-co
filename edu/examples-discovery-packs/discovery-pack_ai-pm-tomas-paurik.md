# Discovery Packet v1 — AI Product Manager (AI-PM)
## Student: Tomas Paurik
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: Success definition (outcomes + governance)
**Question:** If this initiative is successful in 6 months, what **measurable business outcome** and **governance/audit outcome** must be true (e.g., reduced ticket cost/volume, higher CSAT, elimination of shadow AI, full auditability across EN/DE/CZ) — and what **budget and trade-offs** are you willing to commit to make that happen?  
**Why this matters:** Forces alignment on “what good looks like” and prevents building “a chatbot” without measurable value or audit readiness. Anchors scope, timeline, and funding to outcomes.  
**Red flag (bad answer):** “We just want something like ChatGPT” / “Make it smart” / no numbers, no accountability, or a mismatch between ambition and budget.  
**KAF component:** Agentic Core

### Question 2: Why now (trigger + pain)
**Question:** What **specific pain or risk** is driving this now (service desk cost/quality, compliance exposure, fragmented tools, lack of auditability, shadow AI) — and what happens if we do nothing for 12 months?  
**Why this matters:** Clarifies urgency, surfaces the real buying trigger, and helps prioritize use cases that reduce measurable pain or risk fast.  
**Red flag (bad answer):** Vague “innovation” rationale with no cost, risk, or operational consequence; unclear sponsor motivation.  
**KAF component:** Agentic Core

### Question 3: In-scope users and channels (Phase 1 reality)
**Question:** Who is **in scope for Phase 1** (IT-only, 300 users) and through which **channels** (ServiceNow portal, Teams, email, phone deflection) should the assistant operate on day one?  
**Why this matters:** Defines adoption surface area and integration complexity early; prevents late-stage “oh, also Teams + email” surprises.  
**Red flag (bad answer):** “Everyone, everywhere” for Phase 1, or no ownership of channel strategy.  
**KAF component:** Interop (MCP/A2A)

### Question 4: Top use cases (value-first prioritization)
**Question:** What are the **top 5 ticket categories** you want the assistant to handle first, and do we have **volumes, handling time, and cost per ticket** so we can size impact and ROI?  
**Why this matters:** Converts ambition into a prioritized backlog with an ROI model; drives a pragmatic MVP sequence.  
**Red flag (bad answer):** “Handle everything” or no operational data to quantify value.  
**KAF component:** Agentic Core

### Question 5: Boundary of automation (human-in-the-loop)
**Question:** Where must the assistant **stop and hand off to a human** (security actions, access requests, policy exceptions, low confidence, regulated topics) — and who owns the handoff experience?  
**Why this matters:** Establishes safe operating boundaries and accountability; reduces incident risk and user frustration.  
**Red flag (bad answer):** “No handoffs” / “Fully autonomous” without governance, or unclear human ownership.  
**KAF component:** Human-in-the-Loop (HITL)

### Question 6: Current-state landscape (what exists + what breaks)
**Question:** What is running today (ServiceNow, Moveworks, legacy KBs, HR/Claims/Finance bots, PoCs), and where does it **fail** (integrations, content quality, policy controls, audit trails, language coverage)?  
**Why this matters:** Identifies what to reuse, what to retire, and the “edge of failure” where industrialization adds value (governed scale, not another tool).  
**Red flag (bad answer):** “Everything works fine” while shadow AI is rising; or they can’t articulate failure modes.  
**KAF component:** Interop (MCP/A2A)

### Question 7: Data + knowledge readiness (source of truth)
**Question:** What are the **authoritative knowledge sources** (KBs, runbooks, SOPs, identity systems), who owns them, and what is the current **quality / freshness / approval workflow** for content?  
**Why this matters:** The assistant is only as reliable as its knowledge and ownership model; weak content governance creates hallucinations and inconsistent answers.  
**Red flag (bad answer):** “We’ll figure content later” / no single source of truth / no update or approval process.  
**KAF component:** Agentic Ingestion

### Question 8: Security, privacy, and compliance constraints (non-negotiables)
**Question:** What are the **non-negotiable requirements** for PII handling, data residency, retention, access controls, and logging — and what does “**no employee PII in training data**” mean in practice for runtime and telemetry?  
**Why this matters:** Converts policy statements into enforceable controls and design constraints from day one; avoids rework caused by late security/legal escalation.  
**Red flag (bad answer):** “Security will review later” / unclear interpretation of PII at runtime / no decision on residency or retention.  
**KAF component:** Policy-as-Code (Digital Trust)

### Question 9: Auditability definition (evidence required)
**Question:** When you say “**full audit trail**,” what evidence must be produced (prompt/response history, retrieval sources, tool calls, policy checks, handoffs), who audits it (Security, DPO, Internal Audit), and how often?  
**Why this matters:** Defines “audit-ready” in operational terms and determines what telemetry, logging, and governance artifacts must exist for board confidence.  
**Red flag (bad answer):** “Just log everything” (without privacy/retention rules) or “We don’t know who audits.”  
**KAF component:** Policy-as-Code (Digital Trust)

### Question 10: Stakeholders + decisioning (governance and speed)
**Question:** Who is the **exec sponsor**, who is the **product owner**, and who can **approve / block** (CISO, DPO, Legal, Works Council, country IT leads)? What is the **decision cadence** and escalation path to avoid delays and scope creep?  
**Why this matters:** Establishes delivery governance, accelerates decisions, and prevents “death by committee” in a multi-country regulated environment.  
**Red flag (bad answer):** No clear owner, unclear veto power, or decisions deferred to “later committees.”  
**KAF component:** Agentic Core

---

## Part 2: KAF Mapping (mini)

| KAF Component            | Covered by Q#      | Notes |
|--------------------------|--------------------|------|
| Agentic Core             | 1, 2, 4, 10         | Outcomes, prioritization, ROI, stakeholder governance |
| Agentic Ingestion        | 7                  | Knowledge sources + content ownership |
| Policy-as-Code (Trust)   | 8, 9               | PII, residency, retention, audit evidence |
| Digital Trust            | 8, 9               | Audit trail + enforceable controls |
| Human-in-the-Loop        | 5                  | Handoff rules + accountability |
| Interop (MCP/A2A)        | 3, 6               | Channels + ecosystem integration boundaries |

---

## Part 3: Assumptions / Risks / Open Items (3–5)

1. **Success criteria ambiguity risk:** Outcomes and KPIs may not be quantified, leading to scope creep.  
2. **Content readiness risk:** KB/runbooks may be outdated or fragmented across countries/languages, impacting answer quality.  
3. **Governance bottleneck risk:** Security/DPO/Works Council approvals may not have a clear cadence, delaying delivery.  
4. **Runtime PII ambiguity:** “No PII in training” may be interpreted inconsistently across stakeholders, causing rework.  
5. **Channel expansion creep:** Phase 1 may start as ServiceNow but quickly expand to Teams/email without resourcing.

---

## Part 4: What We Will Measure (3 KPI proposals)

1. **L1 deflection / auto-resolution rate (in-scope intents):** target **X%** by month 6 (baseline established in month 1).  
2. **Cost and time reduction:** reduce average handle time (AHT) for top 5 categories by **Y%** or reduce cost per ticket by **€Z**.  
3. **Trust & governance evidence:** **100%** of assistant interactions have auditable logs (retrieval sources + policy checks + handoffs) aligned to agreed retention rules.

---

## Part 5: Agent Classification

- **Governance tier:** **Enterprise**  
- **Registry/reuse potential:** Register as an enterprise “Helpdesk Agent” blueprint with reusable policy pack (PII + audit + access controls) and reusable integration patterns (ServiceNow + channels), then clone per domain (HR, Claims, Finance) with controlled extensions.

---

## Dependencies on Other Roles:

- I need **Security/CISO** to confirm enforceable controls (PII handling, residency, retention, access control, logging) and acceptable risk posture.  
- I need **Legal/DPO** to validate privacy interpretation for runtime data, telemetry, and auditability requirements.  
- I need **ServiceNow platform owner** to confirm Moveworks boundaries, integration feasibility, and channel roadmap.  
- I need **Operations / Service Desk lead** to provide ticket taxonomy, volumes, costs, CSAT baselines, and handoff processes.

---

## Questions I Deliberately Did NOT Ask (and why):

- “Which LLM vendor/model do you want?” — premature before scope, governance, and data constraints are defined (Engineering/Security alignment needed first).  
- “What exact architecture should we use?” — solutioning comes after discovery; engineering-led once constraints and outcomes are agreed.  
- “Can we use customer claims data in the assistant?” — outside Phase 1 IT helpdesk scope; requires separate regulatory and data governance discovery.