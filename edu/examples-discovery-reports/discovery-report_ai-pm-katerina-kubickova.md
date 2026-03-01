# Discovery Report — Katerina Kubickova (Role: AI-PM)

**Date:** 2026-02-24  
**Client:** EuroHealth Insurance AG (Frankfurt, 8 EU countries, ~3,000 employees)


## A) Roleplay comparison (Day 11 selected questions vs. what Hans answered)

### Question 1: “Within the €180K and 6-month window, which outcome must be visible to the board…?”
**Answered.** Hans defined success as a 3-part outcome:
- **30% remaining helpdesk cost reduction** (in 6 months)
- **Unify AI under one platform** (stop fragmentation)
- **EU AI Act compliance readiness by Aug 2026** (“…I keep my job.”)

### Question 2: “If we succeed in IT, what would prevent scaling this governance model…?”
**Partially answered (implicitly).** Hans revealed the blocker: **shadow AI already exists** (HR bot, Claims LangChain prototype) and **nobody governs any of it**, which is exactly why scaling is hard. But you still don’t have the mechanics of scaling (operating model, standards, funding).

### Question 3: “To move from ticket response to full resolution, which enterprise systems must the AI agent orchestrate…?”
**Partially answered.** You learned ServiceNow is the backbone (“tickets, CMDB, change management”), and APIs exist but aren’t used externally / untested. You did not get the full list of downstream systems or owners.

### Not answered yet (OPEN governance/compliance “hard questions”)
- “What specifically can you NOT enforce today with ServiceNow + Moveworks…before Q3 2026?”
  - You know they can do “basic tickets,” but not what enforcement gaps exist (policy controls, agent autonomy boundaries, audit logging, etc.).
- “If the EU AI Act required a full audit trail of one resolved ticket tomorrow…?”
  - Hans only said Stefan is pushing compliance; nothing about traceability, model lineage, prompt versioning, approvals.
- “When regulation or internal AI risk policy changes, what is the path from policy decision to production behavior change — and how long?”
  - No governance pipeline described (policy-to-code, approval workflow, release cadence).

---

## B) Structured discovery report

## 1. STAKEHOLDER MAP:

- **Decision makers (approve budget / direction)**
  - **Hans Muller (CIO, Sponsor):** Wants fast, visible results in 6 months; main goals: -30% helpdesk cost, one governed AI platform, EU AI Act readiness by Aug 2026.
- **Control / veto stakeholders**
  - **CISO / Security:** Can block solutions that aren’t secure or auditable (especially because this must be on-prem, not cloud).
- **Compliance / Risk (incl. EU AI Act owners)**
  - Needs traceability: who approved what, which model was used, what data it used.
- **Operational owners (make it work in reality)**
  - **ServiceNow / IT Ops owner:** Owns workflows + integrations. Key issue: current tools don’t enforce enough; integration feasibility is unknown.
- **Knowledge base owners (IT / Process owners)**
  - KB quality is mixed; some content is outdated.
- **End users (adoption success)**
  - **Helpdesk lead + agents:** Need to trust the system and not feel replaced; adoption risk is real.
- **“Shadow AI” stakeholders (risk + scope)**
  - HR chatbot team, Claims prototype team: already building AI outside governance → must be inventoried and brought under control.

---

## 2. USE CASE LIST: (prioritized) 

- **P1 — AI governance + “one controlled way to use AI” (must start first):**
  - List of AI tools/bots (ServiceNow/Moveworks, HR bot, Claims prototype, etc.), assigned owners, approval steps, clear definition of participating roles.
- **P2 — Audit trail + EU AI Act readiness (prove what happened, anytime)**
- **P3 — Safe helpdesk automation for cost reduction (6-month business result):**
  - Let AI handle the first level: suggest answers, guide users, and resolve only when it’s clearly safe.
- **P4 — ServiceNow + system integrations to move from “answer” to “resolve”:**
  - Make sure AI can safely do actions inside ServiceNow (read/update/close tickets).
- **P5 — Knowledge + language quality so the solution scales:**
  - Improving knowledge base, adding multilingual support.

---

## 3. KEY FINDINGS FROM MEETING:

- This is an **industrialization** engagement, not a chatbot build.
- EuroHealth already has **ServiceNow + Moveworks**, but lacks strong control over how AI is used.
- The main problem is **governance**: clear rules and enforceable controls, not “getting more AI.”
- EU AI Act readiness has a fixed deadline: **August 2026**, so auditability must start now.
- Today they likely **cannot** produce a complete audit trail for one AI-influenced resolved ticket.
- Some AI controls must be **impossible to bypass**, even by administrators.
- Not every ticket is safe to automate, so “never automate / needs human approval” rules are required.
- To move from answering to resolving, AI must integrate with ServiceNow and other enterprise systems.
- Policy changes must translate into production behavior faster.
- Today, that path seems unclear/slow → high governance risk.
- Some actions could create legal/reputation risk → must define “red lines.”

---

## 4. RISKS:

### Governance / compliance risks
- **Shadow AI:** teams use AI tools without approval or clear rules.
- **No audit proof:** cannot clearly show what the AI did and why → risks EU AI Act readiness.
- **Rules can be bypassed:** if admins or teams can override controls, governance won’t work.

### Delivery risks
- **Scope too big:** 8 countries, many languages, and many systems may be too much for 6 months.
- **Integrations harder than expected:** ServiceNow and other system connections may take longer than planned.

### Quality / adoption risks
- **Bad knowledge base:** outdated articles can lead to wrong AI answers.
- **Low adoption:** helpdesk agents may not use it if they don’t trust it or fear job loss.

### Cost risks
- **On-prem cost:** on-prem infrastructure can become expensive if not planned in phases.

---

## 5. NEXT STEPS

### Week 1 — 3 most important steps
- Align with **CIO + Security + ServiceNow owner** on success goals, on-prem limits, and what “EU AI Act ready” means.
- Inventory all existing AI (**ServiceNow/Moveworks, HR bot, Claims prototype, others**) with owner, data used, and risk level.
- Run a one-ticket **“audit replay”** test to confirm what evidence is missing (model/version, prompts, data sources, approvals, edits).

### Week 2 — 3 most important steps
- Choose MVP scope by selecting **3–5 high-volume, low-risk** ticket types to automate first.
- Define simple AI rules for:
  - what AI can do
  - what needs human approval
  - what is never automated
- Agree governance v1 with owners: approval steps, model/prompt versioning, and required logging.

---

## 6. DEPENDENCIES ON OTHER ROLES

- **AI-SEC:** define mandatory audit + non-bypassable control requirements for EU AI Act readiness.
- **FDE:** confirm on-prem architecture and infrastructure sizing that fits performance and budget.
- **AI-DS:** set quality guardrails (confidence thresholds + human-review rules) to prevent wrong answers from weak KB content.
- **AI-DA:** baseline and define success metrics to prove impact (cost per ticket, containment, time to resolve, reopen rate).
