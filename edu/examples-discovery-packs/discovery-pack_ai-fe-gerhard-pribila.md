# Discovery Packet v1 — AI-FE (Front-End / UX / Channels)
## Student: Gerhard Pribila
## Date: February 23, 2026
## Client: EuroHealth Insurance AG (Frankfurt) — CIO: Hans Muller
## Context anchor: ServiceNow + Moveworks already live; ask is AI industrialization (governance, compliance, scaling, ops) — NOT “build a chatbot”.
## Phase 1 scope: IT department (~300 users), 6 months, €180K. On-prem. EN/DE/CZ from Day 1. No employee PII in training data. Audit trail required. Board wants EU AI Act governance framework by Q3 2026.

---

## Part 1: Discovery Questions (10)

### Question 1 — “What can’t you do with ServiceNow + Moveworks today that made you call Kyndryl?”
**Ask:** “You’ve already reduced L1 volume ~35% with ServiceNow + Moveworks and improved CSAT (3.2 → ~3.6). When you try to scale beyond L1 (L2/L3) and beyond IT into other departments, what breaks first: governance, auditability, cross-country consistency, or production operations?”
**Why this matters:** This isolates the *real gap* (governance/ops/scaling) vs. adding another assistant. It also frames success as enterprise readiness, not features.
**Red flag (bad answer):** “We just want more automation” with no examples of governance/ops pain, or “We don’t know—just make it compliant,” implying unclear outcomes and scope risk.
**KAF component:** Core

### Question 2 — “Which user journeys and channels are in-scope for Phase 1—and which must be supported later?”
**Ask:** “For the 300 IT users in Phase 1, which entry points must be first-class: ServiceNow portal, ServiceNow mobile, Microsoft Teams, intranet, VDI/call-center desktops? What’s explicitly out of scope for 6 months—and what must be ready for Phase 2 (HR/Claims/Finance)?”
**Why this matters:** As AI-FE, channel/device scope drives UX design, accessibility constraints, telemetry strategy, and adoption. It prevents ‘accidental omnichannel’ scope creep.
**Red flag (bad answer):** “All channels, all at once” with no prioritization; or “We’ll figure channels later,” which usually means delayed adoption and rework.
**KAF component:** Core

### Question 3 — “EN/DE/CZ from Day 1: how do you govern language quality, legal text, and domain terminology?”
**Ask:** “You require EN/DE/CZ from Day 1. How do you want translations handled for: (a) UI labels and system messages, (b) AI output, (c) policy/legal disclaimers? Who signs off terminology (insurance/IT terms), and do you require human review for certain message types?”
**Why this matters:** Multilingual isn’t just translation—it’s governance (approved phrasing), user trust, and legal consistency across 8 EU countries.
**Red flag (bad answer):** “The model will translate,” with no ownership for legal language and no plan for country-specific variants.
**KAF component:** Ingestion

### Question 4 — “What UI/experience rules must be enforceable as Policy-as-Code?”
**Ask:** “List the rules the end-user experience must enforce automatically (not ‘training users’). Examples: mandatory disclaimers for certain tasks, ‘show sources’ requirements, prohibited actions by role, country-based restrictions, retention banners, and required escalation steps.”
**Why this matters:** This turns UX governance into enforceable controls, versioned and testable—critical for EU AI Act readiness and enterprise scaling.
**Red flag (bad answer):** “We’ll publish guidelines,” or “Users can decide,” which indicates policy will be bypassed and auditability will be weak.
**KAF component:** Policy-as-Code

### Question 5 — “How will you prevent sensitive data entry at the UI layer—without killing usability?”
**Ask:** “Your constraint is no employee PII in training data, and you’re on-prem. At runtime, users may still paste sensitive info into prompts. What must the UI do: warn, block, redact, or route to a secure workflow? Which data types are ‘hard stop’ (e.g., health/claims identifiers) vs ‘allowed with logging’?”
**Why this matters:** The front-end is the main leak vector. We need agreement on user friction tradeoffs, and what’s enforced automatically vs guided.
**Red flag (bad answer):** “We’ll just tell people not to paste PII,” or “We won’t log anything,” which creates either leakage risk or audit blind spots.
**KAF component:** Policy-as-Code

### Question 6 — “What audit trail must exist for the *user experience*, not just the model?”
**Ask:** “For audit and internal investigation, what must we be able to reconstruct: what the user asked, what sources were shown, what the model answered, what the user clicked/approved, and what final action occurred in ServiceNow or downstream tools? Do you need ‘replayability’ (who saw what, when) and immutable retention?”
**Why this matters:** In regulated operations, audits often hinge on the *decision interface*—not only the model output. This also defines telemetry architecture on-prem.
**Red flag (bad answer):** “ServiceNow logs are enough” without confirming they cover all interactions/tools; or “We don’t know what auditors need,” indicating governance immaturity.
**KAF component:** Run Safe

### Question 7 — “Where must humans be in the loop—and what must the UI show to approve safely?”
**Ask:** “Which steps require mandatory human confirmation (e.g., routing to L2/L3, policy changes, access changes, customer-facing messages)? For each checkpoint, what evidence must be displayed in the UI (citations, retrieved snippets, policy checks, diff/summary, risk flags), and how are overrides recorded?”
**Why this matters:** HITL is only effective if the UI makes it easy to validate and safe to approve. It also determines ‘approval’ vs ‘acknowledgement’ patterns.
**Red flag (bad answer):** “No approvals needed” for high-impact actions, or “Approvals happen outside the system,” leading to broken audit chains.
**KAF component:** HITL

### Question 8 — “Which workflows should become agentic—and how transparent must the agent be in the UI?”
**Ask:** “Pick the top 2–3 workflows to make agentic (plan + execute), starting from IT helpdesk. For each: what tools must be called (ServiceNow modules, CMDB, monitoring tools, IAM), and what should the UI expose—step plan, tool call trace, ‘why this action,’ and pre-execution confirmation?”
**Why this matters:** Agentic design requires explicit tool boundaries and UI transparency expectations—especially with cross-system actions and works council constraints.
**Red flag (bad answer):** “The agent should just do it end-to-end” without tool boundaries, permissions, or user confirmation design.
**KAF component:** Interop

### Question 9 — “What does ‘Run Safe’ mean in the UI: monitoring signals, user feedback loops, and incident paths?”
**Ask:** “What front-end signals do you want for production safety: user feedback (thumbs up/down + reason codes), ‘report issue’ that opens a ServiceNow incident, confidence/grounding indicators, and escalation UX? Who watches these metrics, and what triggers a rollback/kill switch?”
**Why this matters:** Most early failures are detected via UX signals first. A structured feedback + incident loop is how you operationalize safety, not just measure it.
**Red flag (bad answer):** “We’ll monitor later,” or “Users can email support,” indicating no closed-loop ops and slow response to failures.
**KAF component:** Run Safe

### Question 10 — “Accessibility + adoption: what standards must the experience meet and how will success be measured?”
**Ask:** “What are your accessibility requirements (e.g., WCAG level, keyboard-only, screen readers, color/contrast) across the target devices (VDI, mobile, Teams)? And what adoption/trust targets do you want for Phase 1 (e.g., weekly active usage among 300 IT users, task success, CSAT trajectory to 4.2+)?“
**Why this matters:** Scaling fails if the experience isn’t usable and trusted. Accessibility is also a governance indicator: consistent, defensible UX across countries and roles.
**Red flag (bad answer):** “Accessibility isn’t a priority,” or “We don’t measure adoption,” which usually means poor uptake and reputational risk.
**KAF component:** Core

---

## Part 2: KAF Mapping (mini)

| KAF Component         | Covered by Q#         | Notes |
|----------------------|-----------------------|------|
| Core                 | 1, 2, 10              | Scope, scaling gaps, channel strategy, adoption |
| Ingestion            | 3                     | Multilingual governance + terminology ownership |
| Policy-as-Code       | 4, 5                  | Enforceable UX rules + PII prevention at UI |
| Run Safe             | 6, 9                  | Audit trail + monitoring/feedback/incident loop |
| Human-in-the-Loop    | 7                     | Approval UX + evidence + override traceability |
| Interop (MCP/A2A)    | 8                     | Tool boundaries + UI transparency for tool calls |

---

## Part 3: Assumptions / Risks / Open Items (5)

1) **Scope risk:** “Omnichannel” expectations (Teams + portal + mobile + VDI) could exceed a €180K / 6-month Phase 1 unless prioritized.
2) **Multilingual risk:** EN/DE/CZ “from Day 1” may require controlled terminology + legal copy sign-off, not just translation.
3) **Data leakage risk:** Even if training excludes PII, the UI can still accept PII at runtime unless we implement detection + policy enforcement.
4) **Audit completeness risk:** If any AI interactions happen outside ServiceNow (shadow HR/Claims/Finance tools), audit trails may remain fragmented.
5) **Works council constraints:** UX changes that alter workflows or monitoring of employees may require consultation and could affect telemetry design.

---

## Part 4: What We Will Measure (3 KPI proposals)

1) **Phase 1 adoption:** ≥70% weekly active usage among the 300 IT users by month 4, with ≥50% of targeted intents completed in the AI-assisted flow.
2) **Trust + traceability:** ≥99% of AI interactions have complete trace records (user ID, request, sources shown, output, policy checks, approvals/overrides).
3) **Experience outcome:** Helpdesk CSAT improves from ~3.6/5 to ≥4.2/5 (client success criterion), with measurable reduction in “misroute” complaints.

---

## Part 5: Agent Classification

- **Governance tier:** Enterprise agent (cross-country, regulated insurer context, audit required, scaling beyond IT planned).
- **Why:** Even Phase 1 is a production system inside a regulated org; Phase 2 expands to HR/Claims/Finance.
- **Registry/reuse potential:** Establish a governed “experience pattern” (channels + disclaimers + approvals + logging) that becomes the reusable template for every department rollout.

---

## Dependencies on Other Roles

- **AI-SEC:** Define PII handling, UI-layer data loss prevention expectations, identity/RBAC constraints, and audit retention requirements.
- **FDE:** Confirm on-prem constraints for UI telemetry collection, log storage, and any gateway/proxy constraints for tool calls.
- **AI-SE:** Define CI/CD and release governance for front-end changes (especially when policy/regulatory updates require UX changes).
- **AI-DS:** Define knowledge source structure, citation formatting, and multilingual KB strategy to support “show sources” UX.
- **AI-PM:** Confirm Phase 1 vs Phase 2 scope boundaries, stakeholder sign-offs, and success metrics.

---

## Questions I Deliberately Did NOT Ask (and why)

- **“Which LLM vendor/model are you using?”** — model selection is secondary to governance/ops; better owned by FDE/AI-SE with security input.
- **“Describe your full infra topology and GPU capacity.”** — too deep for AI-FE; I only need the constraints that affect UX channels, latency, and telemetry.
- **“Provide your security threat model and pen test plan.”** — critical, but best led by AI-SEC; I will consume resulting UX requirements (warnings, blocks, auth UX).