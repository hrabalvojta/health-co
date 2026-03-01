# Discovery Report — AI-PM  
**Student:** Janaki Luke  
**Date:** 24.02.2026  
**Client:** EuroHealth Insurance AG  
**Role:** AI Program Manager  
---

## Executive summary
EuroHealth Insurance AG uses Moveworks/ServiceNow AI for basic IT tickets but has growing **shadow AI** (HR chatbot, Claims LangChain prototype) with **no governance**. Hans (CIO) wants to (1) reduce remaining helpdesk costs by **30%**, (2) **unify AI under one platform**, and (3) achieve **EU AI Act compliance by August 2026**, under a strict **on-prem-only** constraint and a **tight €180k / 6-month** budget. A major operational blocker is an **outdated knowledge base (~30%) with no clear owner**, plus change resistance from a helpdesk team worried about replacement.

### What this means for my AI-PM workstream
We need to rapidly (a) **map and contain AI sprawl**, (b) design a **minimal, enforceable AI governance baseline** (especially for on-prem), and (c) deliver **measurable ticket deflection** without poisoning trust via outdated knowledge.

---

## 1) Stakeholder analysis (from my AI-PM role)

**Hans Muller (CIO) — Economic buyer + risk owner**  
- Goals: cost reduction, platform unification, compliance readiness, on-prem control.  
- Likely bias: may underestimate KB + change management effort; may overestimate “platform” as solution.

**Helpdesk lead “Jan” + 12 agents — primary users + adoption gatekeepers**  
- Fear: replacement / loss of role identity.  
- Power: can make the program succeed or fail through participation in KB hygiene, feedback loops, routing discipline.

**HR function — shadow AI owner (HR chatbot)**  
- Likely goal: responsiveness and privacy; may have built quick solution without compliance.  
- Risk: HR PII exposure + untracked model behavior.

**Claims function — shadow AI owner (LangChain prototype)**  
- Likely goal: faster triage/summaries; may be near high-stakes decisions.  
- Risk: health/claims data sensitivity + potential regulated AI classification.

**Security / Risk / Compliance (incl. DPO, Legal)**  
- Need: defensible controls, auditability, data handling guarantees, vendor risk clarity.

**ServiceNow / Moveworks admins + ITSM process owners**  
- Need: maintain service stability, avoid workflow disruption.  
- Risk: platform constraints may force shadow AI to persist.

**Kyndryl internal roles (my team dependencies)**  
- AI architect/platform engineer: feasibility under on-prem constraint  
- Governance/compliance lead: EU AI Act mapping + policy-as-code  
- Knowledge/content lead: KB remediation + ownership model  
- Change management lead: comms, training, agent enablement

---

## 2) Key findings and implications for my workstream

### Finding A: AI is fragmented; governance is absent
**Implication:** My workstream must start with **visibility and control** (inventory + guardrails) or the “unify” goal becomes unattainable.

### Finding B: On-prem-only constraint is non-negotiable
**Implication:** I must validate **platform options, model hosting, vector DB, logging, and access controls** that work fully on-prem and still meet cost/time constraints.

### Finding C: Knowledge base quality/ownership is a major dependency
**Implication:** Ticket deflection and user trust will be limited unless we establish **KB ownership + remediation pipeline** quickly. AI will amplify bad content.

### Finding D: Helpdesk fears replacement
**Implication:** We need **agent-centered rollout**: reposition AI as “copilot + deflection of repetitive tasks,” define new roles (KB curator, automation specialist), and measure outcomes transparently.

### Finding E: Success metrics are ambitious relative to budget
**Implication:** I must propose **sequenced outcomes**: prove cost reduction in narrow scope first, while laying foundation for compliance and platform consolidation.

---

## 3) Technical/functional requirements to investigate (AI-PM discovery backlog)

### Platform & architecture (on-prem)
- Approved runtime environment: Kubernetes / VMs / air-gapped?  
- Model approach: local LLMs vs constrained vendor models on-prem; support for RAG and tool calling.
- Integration: ServiceNow and Moveworks APIs, identity (SSO), ticket taxonomy, CMDB, KB ingestion.
- Observability: audit logs, prompt/response logging policy, retention, redaction.

### Governance & controls
- AI inventory mechanism: registry of systems, owners, data classes, model versions.  
- Approval workflow: who can launch prototypes; how to decommission them.  
- Policy enforcement: access controls, data boundaries, model usage policies, evaluation gating.

### Knowledge base & content ops
- Define KB ownership: accountable role + process.  
- Content lifecycle: freshness SLAs, review workflow, source-of-truth hierarchy.  
- Grounding strategy: how AI cites/links KB; how to prevent hallucinations and stale answers.

### Adoption & change
- Agent workflow changes: where AI fits into ticket lifecycle.  
- Training plan: agents + HR + Claims on safe usage and escalation.
- Metrics definition: deflection rate, resolution time, CSAT, re-open rate, “wrong answer” rate.

---

## 4) Risks specific to my area (AI product + governance)

**R1. Shadow AI persists (or grows) because “one platform” can’t meet HR/Claims needs on-prem**  
- *Why it matters:* If the sanctioned path is slow or technically blocked, teams will route around it. Governance becomes performative.  
- *Early indicator:* New “prototype” requests show up outside IT intake; undocumented agents/scripts running on departmental servers.

**R2. Knowledge base debt causes wrong answers, rework, and trust collapse**  
- *Why it matters:* With ~30% outdated content and no owner, AI will confidently serve stale guidance → escalations + user backlash + higher ticket load.  
- *Early indicator:* Re-open rates rise, agents override AI suggestions, user complaints about “AI being wrong.”

**R3. EU AI Act readiness risk: evidence is missing and hard to reconstruct later**  
- *Why it matters:* If transparency/audit artifacts aren’t designed in from day one (logging, change control, model cards/system docs), retrofitting is costly and may fail deadlines.  
- *Early indicator:* No agreed inventory, no owner for documentation, no traceability of prompt/version/data changes.

**R4. On-prem constraint introduces delivery and cost risks that can blow the 6-month plan**  
- *Why it matters:* Compute provisioning, security reviews, integration approvals, and vendor constraints can dominate schedule; budget is tight.  
- *Early indicator:* Infra lead times exceed weeks; security requires additional controls; integration endpoints not available.

**R5. Data handling risk: HR PII and claims data exposure via prompts, logs, embeddings, or dev copies**  
- *Why it matters:* Even on-prem, prompt/response logs and vector stores can become new sensitive-data repositories without retention/redaction rules.  
- *Early indicator:* Engineers ask to “log everything for debugging,” no clear retention policy, unclear encryption/access controls.

**R6. Adoption/people risk: helpdesk fear of replacement sabotages quality loops**  
- *Why it matters:* Agents are critical to KB hygiene, workflow tuning, and feedback labeling. Fear drives passive resistance and silent failure.  
- *Early indicator:* Low participation in training, no KB updates, poor tagging/feedback compliance.

**R7. KPI misalignment: “30% cost reduction” becomes a blunt instrument**  
- *Why it matters:* If interpreted as headcount reduction, it spikes resistance and incentivizes risky automation. Better framed as “capacity reallocation + deflection.”  
- *Early indicator:* Messaging focuses on “reducing agents” rather than “reducing repetitive load.”

---

## 5) Recommended next steps (first 2 weeks)

### Week 1 — Containment + clarity (get the facts, stop the bleeding)
1) **AI inventory sprint (official + shadow)**  
   - Output: initial registry of all AI systems (Moveworks/ServiceNow, HR chatbot, Claims LangChain, any copilots/plugins), owners, hosting location, data classes, and current controls.  
2) **Boundary & accountability mapping (ServiceNow vs Moveworks vs “everything else”)**  
   - Output: simple boundary diagram + “where risk begins” list (unowned prototypes, unmanaged logs, unknown data flows).  
3) **On-prem feasibility check (reality test)**  
   - Output: confirmed deployment constraints (compute, network, security controls, approved runtimes), integration access (ServiceNow APIs, KB, identity), and any hard blockers.  
4) **KB triage for top ticket categories**  
   - Output: top 10 ticket intents, % of KB articles stale/duplicative for those intents, and a short proposal for KB ownership.

### Week 2 — Minimum viable governance + pilot definition (commit to a winnable slice)
5) **Define a Minimum Governance Baseline (MGB) that can go live immediately**  
   - Components: system registry, named owners, intake/approval for new AI, logging/redaction/retention policy, access controls, and a basic evaluation gate for releases.  
   - Output: v0 governance pack + implementation plan (what’s policy vs what’s enforced in tooling).  
6) **Select a narrow pilot aligned to the 30% goal (but safe)**  
   - Criteria: high volume, low ambiguity, low-risk data, KB relatively fixable, measurable deflection.  
   - Output: pilot scope (1–2 ticket categories), success metrics, and rollout plan.  
7) **Agent enablement kickoff (reduce fear, create co-ownership)**  
   - Output: messaging + training plan framing AI as “tier-0 deflection + tier-1 copilot,” plus proposed role shifts (KB steward, automation analyst).  
8) **Instrumentation & measurement plan (before changes ship)**  
   - Output: baseline metrics capture (deflection, AHT, reopen rate, CSAT), plus “wrong answer” tracking and escalation workflows.

*End-of-week-2 deliverables from my role:* inventory draft, boundary map, on-prem feasibility notes, KB triage summary, MGB v0, pilot charter, metrics plan.

---

## 6) Dependencies on other roles in the team

**AI Architect / Platform Engineer**  
- Confirm on-prem reference architecture (runtime, model hosting, vector store, observability).  
- Validate integration patterns with ServiceNow/Moveworks and security constraints.

**ServiceNow / ITSM SME**  
- Current workflow mapping, routing logic, catalog structure, CMDB/KB architecture.  
- Identify best pilot ticket categories and change windows.

**Security, Risk, Compliance lead (incl. DPO/Legal liaison)**  
- EU AI Act interpretation for planned use cases, classification guidance (especially Claims).  
- Logging/redaction/retention requirements; access control standards; audit evidence needs.

**Knowledge Management / Content Ops lead**  
- Establish KB ownership model, review cadence, and quality gates.  
- Prioritize KB cleanup for pilot intents; define content lifecycle SLAs.

**Change Management / Adoption lead**  
- Helpdesk comms plan to address fear; training and enablement; feedback loops.  
- Role evolution plan for Jan’s team and incentives for KB contributions.

**Program / Engagement manager**  
- Scope control to fit €180k/6 months; manage tradeoffs between unification, compliance, and ROI.  
- Vendor/procurement coordination (if any on-prem components need licensing/hardware).

**Client-side owners we must identify quickly (dependency risk until named)**  
- Named owner for HR chatbot and Claims prototype (business + technical).  
- Executive sponsor for KB ownership (so it doesn’t die as “everyone’s job”).
