# Discovery Report — AI-FE (Front-End / UX / Channels)
## Client: EuroHealth Insurance AG (Frankfurt) — CIO: Hans Muller
## Author: Gerhard (AI-FE, Kyndryl AI Consulting Team)
## Date: 24 Feb 2026
## Engagement scope (Phase 1): IT department (~300 users), 6 months, €180K (tight)
## Working assumption: L2 (Constrained) autonomy — AI can auto-resolve within guardrails; humans monitor/override

---

## 0) Context summary (what we learned)
EuroHealth already runs **Moveworks + ServiceNow** for basic ticket handling. However, AI usage has proliferated into **shadow AI** (an HR chatbot and a Claims LangChain prototype) with **no governance**.

Hans defines success as:
- **30% reduction** of remaining helpdesk costs (within 6 months)
- **Unify AI** under one platform / operating model
- Be **EU AI Act compliant by Aug 2026**
- **On-prem only** (no cloud — non-negotiable)
- **Knowledge base ~30% outdated** with **no clear owner**
- Helpdesk team (**Jan + 12 agents**) fears replacement
- Budget is **€180K / 6 months** (very tight)

**AI-FE headline:** Adoption + compliance outcomes will be won or lost in the **experience layer**: unified “front door”, consistent trust patterns, enforceable UI guardrails, and a feedback loop to improve knowledge quality.

---

## 1) Day 11 discovery questions — coverage vs. roleplay answers

### Summary
- **Answered (high-level):** Q1 (why they called Kyndryl / what breaks today)
- **Partially answered:** Q4 (need governance → implies UI policy requirements, but specifics missing)
- **Not answered:** Q2, Q3, Q5 (channels, multilingual governance, and UI-layer sensitive-data controls)

### Detailed mapping

#### Q1 — “What can’t you do with ServiceNow + Moveworks today that made you call Kyndryl?”
**Answered (core), but still needs examples.**

**What Hans answered:**
- ServiceNow + Moveworks covers basic tickets already.
- Shadow AI exists across HR + Claims with no governance.
- They want unification + EU AI Act readiness.

**Still open for AI-FE:**
- Concrete “day-in-the-life” examples of what fails: trust, escalation, inconsistency, auditability, cross-country language issues?
- 2–3 “near-miss” stories from shadow AI to drive guardrail priorities.

---

#### Q2 — “Which user journeys and channels are in-scope for Phase 1—and which later?”
**Not answered (critical open risk).**

**Impact if unresolved:** FE scope creep (“accidental omnichannel”) will break budget + timeline.

**To confirm in Week 1:**
- Primary surface(s): ServiceNow portal? Agent Workspace? Teams?
- Secondary: mobile, intranet, VDI/call-center desktops?
- What is explicitly out-of-scope in Phase 1?

---

#### Q3 — “EN/DE/CZ from Day 1: how do you govern language quality, legal text, and domain terminology?”
**Not answered (high compliance + trust risk).**

**To investigate:**
- Who owns terminology (IT + insurance) and who approves legal disclaimers per language?
- Human review requirements for certain message types (security, HR policy, regulated content).
- Whether “DE” means DE-DE only, or variants (DE-AT, etc.) later.

---

#### Q4 — “What UI/experience rules must be enforceable as Policy-as-Code?”
**Partially answered (governance need confirmed, rules unspecified).**

**What Hans answered:**
- Governance and EU AI Act compliance are strategic requirements.
- Unification is a success criterion.

**Still open:**
- Which rules must the UI enforce (disclosures, citations, prohibited actions, RBAC restrictions, escalation thresholds, retention banners)?
- Who defines/approves the rules (CISO Stefan, Legal, HR, IT Ops)?

---

#### Q5 — “How will you prevent sensitive data entry at the UI layer—without killing usability?”
**Not answered (major risk area).**

**To clarify:**
- Which data types are “hard stop” vs. “allowed with logging” vs. “warn only”?
- Should UI block, redact, or route to secure workflows?
- How will we prevent policy friction from pushing users back to shadow AI?

---

## 2) Stakeholder analysis (AI-FE perspective)

### Stakeholder map (power × influence × adoption)
| Stakeholder | Role | Power type | Primary concerns | AI-FE implications |
|---|---|---|---|---|
| Hans Muller | CIO / sponsor | Budget + board narrative | ROI (30% cost), unification, compliance by Aug 2026 | Needs a “board-safe” experience: unified, explainable, governable |
| Stefan (CISO) | Security/compliance gate | Veto power | Audit trail, data handling, EU AI Act posture | UI must support transparency, logging intent, RBAC cues, policy disclosures |
| Jan (Helpdesk lead) + 12 agents | Daily operators | Adoption gatekeepers | Job security, workload, control | If agents don’t trust/like UX, adoption fails even if tech works |
| ServiceNow platform owner/admin (to identify) | Platform owner | Operational power | Stability, integration safety | Prefer extensions to existing surfaces vs net-new UI |
| HR chatbot owner (shadow AI) | Local champion | Department influence | Speed, autonomy | Will resist centralization unless new experience is clearly better |
| Claims prototype owner (shadow AI) | Local champion | Department influence | Claims workflows | Early alignment needed for future Phase 2 journeys |
| Knowledge Base “owner” (currently none) | Missing owner | Structural risk | No one owns “truth” | UX must surface freshness + feedback loop; ownership must be assigned |
| (To confirm) Works council / employee reps | Potential blocker | Governance power | Monitoring, job impact, transparency | UX + telemetry design may require negotiation and clear boundaries |

**AI-FE conclusion:** Jan can kill adoption silently; Stefan can kill go-live explicitly.

---

## 3) Key findings and implications for AI-FE workstream

### Finding A — Existing ITSM AI already deployed (ServiceNow + Moveworks)
**Implication:** Do not build a “new chatbot”. FE strategy should be:
- Extend **existing channels/surfaces**
- Provide a **unified interaction model** and consistent trust/guardrails

### Finding B — Shadow AI sprawl across HR and Claims
**Implication:** Design reusable UX patterns that scale:
- “AI disclosure”
- Citations/sources
- Escalation and handoff
- Feedback and correction loops
- RBAC-aware actions and messaging

### Finding C — Knowledge base is ~30% outdated, no owner
**Implication:** Trust UX becomes a core feature:
- show sources + last-updated signals (where possible)
- “Report wrong/outdated” flow with a triage destination
- safe fallbacks when confidence is low

### Finding D — Helpdesk fears replacement
**Implication:** Choose “augmentation-first” experience patterns:
- agent-assist (“suggest → approve/override”)
- explicit controls and visibility
- “credit” agents in dashboards for successful use (avoid perceived replacement)

### Finding E — On-prem only, no cloud
**Implication:** FE architecture must avoid hidden cloud dependencies:
- analytics/telemetry must be on-prem
- no cloud translation services
- careful handling of logs and audit trails

### Finding F — Budget/timeline are tight
**Implication:** MVP must be aggressively scoped:
- one primary channel (or a narrow set)
- top 2–3 journeys only
- strict out-of-scope list (protects delivery)

---

## 4) Technical / functional requirements to investigate (AI-FE-owned)

### 4.1 Channel and journey scope (MVP definition)
- Confirm Phase 1 primary entry points (employee + agent)
- Define top journeys by volume/ROI (e.g., password reset, access requests, common IT issues)
- Confirm what channels are out-of-scope for 6 months

### 4.2 UX governance / Policy-as-Code integration
- UX requirements that must be enforceable (not “training users”)
  - AI disclosure banners
  - citation rules (when required)
  - prohibited intents by role
  - escalation rules (when to handoff)
  - retention/audit notices where needed

### 4.3 Sensitive data prevention at the UI layer
- Determine enforcement model: warn vs block vs redact vs route
- Define hard-stop patterns (claims IDs, health identifiers, employee PII, etc.)
- Provide safe alternatives (secure forms, ticket templates, handoff)

### 4.4 Trust indicators and transparency UX
- Source attribution display patterns (snippets, links, confidence signals)
- “Why this answer?” (retrieval summary) for regulated contexts
- User feedback loops:
  - “Helpful / Not helpful”
  - “Outdated”
  - “Escalate”

### 4.5 Agent workflow UX (L2 constrained autonomy)
- Monitoring and override UI for agents
- Clear “what did the AI do” history view
- Undo/rollback patterns (where feasible)
- Escalation UX that fits current ServiceNow operations

### 4.6 Multi-language UX governance (EN/DE/CZ)
- UI strings localization workflow
- AI output language policy:
  - approved disclaimers per language
  - terminology governance (glossary ownership)
  - human review requirements for certain response types

### 4.7 Accessibility + enterprise UX requirements
- Accessibility baseline (e.g., WCAG 2.1 AA)
- Browser/device constraints (desktop/VDI, mobile, etc.)
- Performance expectations (latency budgets) and how to reflect “loading/uncertainty” safely

### 4.8 Telemetry and measurement (on-prem)
- Define FE event taxonomy with AI-DA:
  - deflection attempts, resolution rate, escalation rate
  - override rate, time-to-resolution
  - trust signals (repeat usage, “wrong answer” rate)
- Ensure telemetry aligns with compliance constraints (data minimization)

---

## 5) Risks (AI-FE-specific) + mitigations

### R1 — Adoption failure due to helpdesk fear
**Risk:** Agents avoid using AI features; negative sentiment spreads.
- **Second-order effect:** Cost reduction KPI fails even if model works.
**Mitigation:** agent-first co-pilot UX + explicit control points + training + clear internal comms.

### R2 — Trust collapse due to outdated knowledge base
**Risk:** Wrong answers in first weeks destroy credibility.
- **Second-order:** Ticket volume increases; users bypass platform.
**Mitigation:** citations + freshness cues + “report outdated” workflow + safe fallbacks.

### R3 — Omnichannel scope creep (budget killer)
**Risk:** Late requests for Teams + portal + mobile parity.
**Mitigation:** Week 1 channel decision + written out-of-scope list + phased roadmap.

### R4 — Overly strict PII blocking drives shadow AI relapse
**Risk:** Users circumvent governance to get work done.
**Mitigation:** progressive enforcement + safe alternatives + clear explanations and routing.

### R5 — On-prem constraints reduce iteration speed
**Risk:** Harder A/B testing + limited analytics toolchains.
**Mitigation:** lightweight on-prem telemetry + fast feedback with agents + prototype testing.

### R6 — “No cloud” ambiguity vs existing SaaS tools
**Risk:** “No cloud” may mean “no LLM processing/logging outside on-prem”, not “no SaaS at all”.
**Mitigation:** clarify compliance boundary in Week 1 and design UX + logging accordingly.

### R7 — Works council / employee monitoring concerns (if applicable)
**Risk:** Telemetry design may be blocked or require negotiation.
**Mitigation:** data minimization + explicit transparency + separate “operational metrics” vs “employee monitoring”.

---

## 6) Recommended next steps (first 2 weeks)

### Week 1 — Lock MVP scope + de-risk adoption & compliance
1. **Channel & scope workshop (60 min)** — Hans + ServiceNow owner + Jan rep + AI-PM  
   **Output:** Phase 1 primary channels + explicit out-of-scope list.
2. **Contextual inquiry interviews** — Jan + 3 agents; 3 frequent ticket submitters  
   **Output:** top 3 journeys, friction points, and adoption blockers.
3. **Compliance UX requirements session** — Stefan (CISO) + AI-SEC + AI-FE  
   **Output:** UX compliance checklist v0 (disclosure, logging, RBAC cues, retention notice needs).
4. **KB trust assessment sprint** — with AI-DS + whoever can “own” KB triage  
   **Output:** proposed “feedback-to-triage” workflow + interim owner assignment.

### Week 2 — Prototype + validate with users
5. **Low-fidelity prototype (clickable)** of:
   - employee self-serve flow (with citations, escalation, safe fallback)
   - agent-assist flow (approve/override, audit view)
6. **PII / sensitive-data UX design v0**
   - warn/block/redact rules
   - secure workflow route
7. **Instrumentation plan** with AI-DA + AI-SE
   - event taxonomy
   - on-prem logging path
8. **Multi-language governance plan v0**
   - glossary ownership proposal
   - legal disclaimer approval workflow per language

---

## 7) Dependencies on other roles

### AI-PM
- Confirm MVP scope, success metrics baseline (“30% of what?”), project phasing, and stakeholder comms.

### AI-SEC
- EU AI Act implications translated into UI requirements (transparency, auditability, user disclosures).
- Sensitive data categories + enforcement policy.

### AI-SE / FDE
- ServiceNow integration approach and feasibility for chosen channels.
- Auth/SSO constraints, session management, logging pipeline on-prem, latency constraints.

### AI-DS
- KB audit results and confidence thresholds that determine FE behaviors (when to cite, when to refuse/escalate).
- Retrieval/citation format constraints that UI must support.

### AI-DA
- KPI definitions and dashboard needs (board-ready metrics).
- Event schema and measurement plan.

---

## 8) Open questions backlog (AI-FE follow-ups)

### Channel & scope
1. What is the **single** primary channel for Phase 1 (portal, agent workspace, Teams)?
2. Which channels are explicitly **out-of-scope** for 6 months?
3. What are the top 3 ticket journeys by volume and cost?

### Trust & KB
4. For each KB source, can we expose “last updated” metadata to the UI?
5. Where should “report outdated/wrong” feedback go (queue, owner, SLA)?

### Compliance / policy-as-code UX
6. What disclosures are required for users (AI usage notice, data usage notice)?
7. When are citations mandatory (always vs only for certain intents)?
8. Which actions/intents are restricted by role or country?

### Sensitive data enforcement
9. Which data types are “hard stop” vs “allowed with logging”?
10. Do we redact in UI, server-side, or both?
11. What is the approved “safe alternative” workflow when blocked?

### Change management
12. What specific fears does Jan’s team have (replacement vs workload vs accountability)?
13. Who owns training and rollout communications?

### On-prem constraints
14. What does “no cloud” mean precisely given current tool landscape?
15. Are there constraints on telemetry storage/retention and who can view it?

---

## Closing note (AI-FE perspective)
This engagement is not a chatbot build. It is an **industrialization** effort where the user experience must enforce governance, build trust despite imperfect knowledge, and drive adoption among a workforce that is anxious about displacement. The front-end layer is the primary control surface for policy-as-code, and the primary failure point if channel scope, trust patterns, and sensitive-data guardrails are not clarified in Week 1.
