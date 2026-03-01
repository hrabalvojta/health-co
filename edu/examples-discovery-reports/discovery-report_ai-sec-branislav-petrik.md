# EuroHealth Insurance AG — Discovery Report (AI-SEC)
**Engagement theme:** Helpdesk AI industrialization + enterprise AI governance consolidation  
**Role:** AI Security (AI-SEC)  
**Inputs:** Client brief + Day 12 CIO roleplay (Hans Muller)  
**Non-negotiables:** On-prem only (no cloud) + EU AI Act compliance readiness by **August 2026** + unified governance framework

---

## 1) Stakeholder Analysis (AI-SEC perspective)

**Hans Muller (CIO / Sponsor / Board-facing)**
- Success = **30% remaining helpdesk cost reduction in 6 months**, unify fragmented AI under one platform, and show a **compliance-ready platform before Aug 2026**.
- Personal pressure (“I keep my job”) increases risk of control-bypassing shortcuts late in the timeline.

**Stefan Weber (CISO / Compliance gatekeeper)**
- Actively pushing EU AI Act readiness; likely veto authority on security posture and auditability.
- AI-SEC must align early to avoid late-stage blocking.

**Shadow AI owners (HR + Claims)**
- HR chatbot + Claims LangChain prototype “nobody approved” signals active governance breach and unknown data handling.
- Expect resistance to central governance unless decision rights are clarified.

**Jan + 12 helpdesk agents (End users / Adoption gate)**
- Fear replacement → adoption and “workaround” risk; may route around governed tooling if UX and escalation paths don’t build trust.

**IT Ops / Platform Ops (Implicit)**
- On-prem-only makes IT Ops accountable for logging infrastructure, secrets management, patching, access controls, and evidence retention.

---

## 2) Key Findings & Implications for AI-SEC

**Finding A — Primary risk is unmanaged AI sprawl (shadow AI), not lack of tooling**
- Fragmented deployments already exist across departments without governance.
- **Implication:** AI-SEC scope must prioritize **enterprise governance + enforceable controls + audit evidence**, not only app-level security.

**Finding B — “Compliance-ready” is required, but undefined**
- CIO demands compliance readiness by Aug 2026 but provides no evidence definition.
- **Implication:** AI-SEC must define *what evidence proves readiness* (traceability, approvals, logs, retention, access reviews) and secure CISO sign-off in Week 1.

**Finding C — On-prem constraint shifts security burden inward**
- No cloud safety nets; controls must be built/operated internally.
- **Implication:** Treat on-prem as a security program: IAM, segmentation, secrets, logging integrity, supply-chain controls, incident response.

**Finding D — Knowledge base quality is an integrity + safety risk**
- ~30% outdated, no owner → the AI will confidently scale wrong answers.
- **Implication:** Governance must include **content ownership + freshness controls + safe fallback** to prevent compliance incidents.

---

## 3) AI-SEC Requirements to Investigate (must include the following)

### 3.1 EU AI Act Risk Classification (likely high-risk)
**Hypothesis:** An L2 constrained helpdesk agent that influences IT operations and potentially touches employee/ticket data will likely fall into a **regulated/high-risk compliance posture** given enterprise context and auditability needs.
**Required discovery actions:**
- Confirm the system’s **intended autonomy level** (L2 constraints), scope of actions (auto-resolve vs recommend), and impact domain.
- Identify whether outputs can affect employee access, account changes, or decisions with material impact (raises classification obligations).
**Deliverable:** “EU AI Act classification memo v1” with rationale, required controls, and evidence plan aligned with Stefan (CISO).

### 3.2 PII Handling — Employee Directory Exclusion Strategy
**Risk:** Tickets and identity systems contain PII; directory enrichment can leak sensitive identity attributes into prompts, logs, and retrieval.
**Required controls / questions:**
- Define a **PII data boundary**: which fields are prohibited from prompts, embeddings, logs, and training.
- **Directory exclusion strategy:** default no ingestion of the employee directory into embeddings/RAG; allow only minimal, purpose-limited lookup (e.g., role/team) via controlled APIs if needed.
- Decide if the agent needs identity at all (many helpdesk intents don’t).
**Deliverable:** “PII policy v1” (field allowlist/denylist + redaction rules + retention and access governance).

### 3.3 On-Prem Data Residency — Audit Trail Requirements
**Risk:** On-prem means data stays local, but **proof** must exist (audit trail) and logs must be integrity-protected.
**Minimum audit trail requirements to validate:**
- Traceability: model/tool/version per interaction
- Data access logging: which sources queried (KB pages), which ticket fields read
- Action logging: what was proposed/executed (auto-resolve vs escalation), human overrides
- Approval evidence: who approved models/tools/guardrails, and change history
- Retention + access reviews: who can read logs, how long kept, tamper resistance
**Deliverable:** “Audit evidence model” (log schema + retention + integrity controls + review cadence).

### 3.4 LLM Prompt Injection Threat Model
**Threats to model:**
- Injection via ticket text (“ignore policy and reveal…”)
- Injection via RAG sources (Confluence pages can contain malicious instructions)
- Data exfiltration attempts (“print confidential policy / credentials / directory”)
**Required mitigations to investigate:**
- Input sanitization and prompt hardening
- Strict tool/function calling policy (allowlist actions only)
- RAG safety: source allowlist, freshness filters, “instruction stripping” patterns, citation requirement
- “Refusal + escalate” patterns when policy violations are detected
**Deliverable:** Threat model + prioritized mitigations mapped to architecture components.

### 3.5 Access Control — Who Sees What Ticket Data
**Core requirement:** Enforce least privilege for ticket visibility across roles and departments.
**Discovery questions:**
- Ticket data classifications (PII, health-adjacent info, internal sensitive categories)
- Role matrix: helpdesk agent vs team lead vs IT ops vs auditors vs HR/Claims
- Segmentation: cross-country access rules (8 EU countries), language scope
**Control requirements:**
- RBAC/ABAC model integrated with existing identity provider
- “Need-to-know” views for AI outputs (don’t echo sensitive fields)
- Audit logs for access and overrides
**Deliverable:** “Ticket data access matrix” + enforcement design requirements.

### 3.6 Compliance Timeline — August 2026 Readiness Plan
**Reality:** Deadline pressure + tight budget increases risk of governance being cut.
**Plan must define:**
- What “compliance-ready” means by Aug 2026 (evidence deliverables + controls)
- Milestones that de-risk late-stage blocking (CISO sign-off checkpoints)
- Minimum viable compliance for Phase 1 that can scale to Phase 2 (Claims/HR)
**Deliverable:** “Aug 2026 readiness roadmap” (phased controls, evidence milestones, owners).

---

## 4) AI-SEC Risk Register (specific to this engagement)

**R1 — Shadow AI already running (HIGH)**
- Unapproved Claims prototype implies unknown data handling, unknown logging, unknown compliance posture.

**R2 — Undefined compliance evidence (HIGH)**
- Risk of delivering functionality that fails audit/regulatory scrutiny because evidence requirements were never specified.

**R3 — On-prem security burden underestimated (HIGH)**
- Without strong IAM, secrets, logging integrity, and patching processes, on-prem increases attack surface.

**R4 — Prompt injection / RAG poisoning (HIGH)**
- Ticket text and KB content are untrusted inputs; KB is partially outdated and unowned.

**R5 — PII leakage through prompts/logs (HIGH)**
- Directory/ticket fields may leak into prompts, embeddings, logs, or debugging artifacts.

**R6 — Adoption workarounds create new shadow AI (MEDIUM→HIGH)**
- Fear-driven bypass behavior can undermine governance and recreate unmanaged tools.

---

## 5) Recommended Next Steps (First 2 Weeks)

### Week 1 — Define compliance target + stop-the-bleeding governance
1) **AI Inventory Sprint (48–72h):** HR chatbot + Claims prototype + IT tools (owners, hosting, data touched, approvals).
2) **CIO+CISO workshop:** confirm EU AI Act classification approach + define “compliance-ready” evidence outputs and sign-off path.
3) **Minimum viable governance v1 (policy-as-code):**
   - model/tool allowlist + approval workflow
   - PII boundaries + directory exclusion strategy
   - required logging + retention baseline
   - autonomy constraints (what can be auto-resolved vs must escalate)
4) **Containment action:** require registration/approval for any new AI deployment during Phase 1.

### Week 2 — Threat model + enforcement design
5) **Prompt injection threat model + mitigations** aligned to FDE/AI-SE architecture (RAG safety, tool allowlists, refusal/escalation).
6) **Audit trail design:** log schema + integrity controls + access reviews + retention aligned to “compliance-ready” definition.
7) **Ticket access matrix:** role-based visibility rules + enforcement requirements (least privilege, country/language constraints).

---

## 6) Dependencies on Other Roles (what AI-SEC needs)

**FDE / AI-SE**
- On-prem architecture details: where policy enforcement lives, logging pipeline, secrets management, identity integration, segmentation.
- Tool/function calling design to enforce constrained autonomy safely.

**AI-DS**
- KB audit plan + freshness scoring; controls to block stale/unsafe sources and create a golden evaluation set.

**AI-DA**
- Baseline definition + measurement method for “30% cost reduction” and compliance reporting dashboard metrics (board-ready evidence).

**AI-PM**
- RACI confirmation (CIO/CISO/DPO/Legal), decision cadence, and scope phasing so governance deliverables are not sacrificed.

**AI-FE**
- UX requirements for L2 oversight: citations, confidence cues, escalation/override, and safe error states to reduce bypass behavior.

---

## Executive Summary (AI-SEC)
EuroHealth’s stated goal is cost reduction, but the core security/compliance problem is unmanaged AI proliferation across departments without enforceable governance. AI-SEC must define EU AI Act classification posture, implement PII boundaries (including directory exclusion), design on-prem audit evidence and access controls, and mitigate prompt injection risks in an L2 constrained agent. Achieving “compliance-ready by Aug 2026” requires a Week 1 definition of evidence outputs with CISO sign-off, followed by policy-as-code enforcement and audit-grade logging that can scale beyond IT into Claims and HR.