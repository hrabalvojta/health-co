# ====================================
# Discovery Packet v1 — Full-stack Development Engineer (FDE)
## Student: SEBASTIAN MICHALOWSKI
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1:
“You already have ServiceNow + Moveworks. What are the top 3 things you *cannot* do today with ServiceNow alone that triggered this engagement (governance, auditability, cross-department scaling, regulatory adaptation)?”

**Why this matters:** It forces clarity on the real “industrialization gap” so we don’t rebuild L1 chatbot features you already have and instead focus on what must be production-grade in 6 months for €180K.  
**Red flag (bad answer):** “We just want a better chatbot” / “We’ll figure the gaps out later.”  
**KAF component:** Agentic Core  

---

### Question 2:
“When you say ‘on‑prem only,’ what exactly must be on‑prem (LLM inference, retrieval store/vector DB, logs/traces, ticket text), and what data is allowed to cross the boundary between the on‑prem platform and ServiceNow?”

**Why this matters:** “On‑prem” drives the architecture, network boundaries, latency, security controls, and even which integration patterns are feasible.  
**Red flag (bad answer):** Conflicting answers across stakeholders (e.g., “no cloud ever” but also “use a cloud LLM API”).  
**KAF component:** Agentic Core  

---

### Question 3:
“Which specific policies must be *enforceable in code* from Day 1 (data access, tool/action permissions, prohibited outputs, language requirements, PII handling), and where do you want enforcement to happen (gateway, orchestration layer, or tool boundary)?”

**Why this matters:** This defines the Policy‑as‑Code design: what we enforce, how we enforce it, and where we can reliably stop unsafe actions.  
**Red flag (bad answer):** Policies exist only as documents/training; enforcement is manual or ‘best effort.’  
**KAF component:** Policy-as-Code  

---

### Question 4:
“If EU AI Act guidance or internal policy changes, what is your target SLA to update guardrails across *all* active AI workflows (hours/days/weeks), and who owns sign‑off, release, and rollback?”

**Why this matters:** Regulatory readiness isn’t a document—it’s a change-management capability. This drives policy CI/CD, versioning, testing, and ownership.  
**Red flag (bad answer):** “It takes months” / “No single owner or approval path.”  
**KAF component:** Policy-as-Code  

---

### Question 5:
“What are the authoritative sources for helpdesk resolution (ServiceNow KB, runbooks, Confluence, CMDB, monitoring/alerts), who owns them, and what coverage exists today in EN/DE/CZ?”

**Why this matters:** Retrieval quality is limited by knowledge quality and ownership; multilingual support changes ingestion, indexing, and validation requirements.  
**Red flag (bad answer):** “Docs are scattered/outdated with no owners” / “Translation is ad hoc.”  
**KAF component:** Agentic Ingestion  

---

### Question 6:
“The brief says ‘no employee PII in training data.’ Does that also prohibit using historical ticket text for embeddings/fine‑tuning/evaluation—and what redaction/anonymization is required for traces, logs, and audit exports?”

**Why this matters:** Defines what data we can legally/ethically use and what PII controls must exist across ingestion, evaluation, and observability.  
**Red flag (bad answer):** “We’ll just use ticket history as‑is” / “We don’t distinguish training vs retrieval vs logging.”  
**KAF component:** Agentic Ingestion  

---

### Question 7:
“Beyond ServiceNow, which systems must the agent interact with to actually resolve tickets (IAM/AD, endpoint mgmt, VPN, email, monitoring), and what are your standards for authN/authZ and secrets at each tool boundary (least privilege, service accounts, approvals)?”

**Why this matters:** Tool access is where most complexity and risk lives; this question defines integration scope, identity boundaries, and the safe automation surface.  
**Red flag (bad answer):** “We’ll give it broad admin access” / “Integrations come after the PoC.”  
**KAF component:** Interop (MCP/A2A)  

---

### Question 8:
“If an auditor/regulator asks for one ticket’s end‑to‑end explanation within 24 hours, what exact evidence must we produce (model + version, retrieved sources, policy checks, tool calls, human approvals), and what retention and access controls are required?”

**Why this matters:** Converts ‘audit trail required’ into specific traceability, logging schema, storage, and evidence-export requirements.  
**Red flag (bad answer):** “We can’t reconstruct decisions end‑to‑end” / “Logs are fragmented by tool.”  
**KAF component:** Run Safe (Digital Trust)  

---

### Question 9:
“Which ticket categories/actions can be fully automated vs must require human confirmation (e.g., access changes), and what is the escalation path to L2/L3 inside ServiceNow?”

**Why this matters:** Sets safe autonomy boundaries and defines where Human‑in‑the‑Loop checkpoints must appear to prevent harmful actions.  
**Red flag (bad answer):** “Everything can be automated” or “We don’t know what must be approved by a human.”  
**KAF component:** Human-in-the-Loop (HITL)  

---

### Question 10:
“In 6 months, what does ‘production‑ready’ mean for you: SLOs/availability, monitoring + alerting expectations, on‑call ownership, and KPI gates to scale beyond IT after the Phase 1 pilot?”

**Why this matters:** Ensures we build an operable system (not a demo) with clear reliability and success criteria within the €180K/6‑month constraint.  
**Red flag (bad answer):** “Success is subjective” / “No SLOs, monitoring standards, or on‑call ownership.”  
**KAF component:** Run Safe (Digital Trust)  

---

## Part 2: KAF Mapping (mini)

| KAF Component             | Covered by Q# | Notes |
|--------------------------|---------------|-------|
| Agentic Core             | 1, 2          | ServiceNow gap + on‑prem boundary |
| Agentic Ingestion        | 5, 6          | Sources/ownership + PII constraints |
| Policy-as-Code           | 3, 4          | Enforceable rules + change SLA |
| Digital Trust / Run Safe | 8, 10         | Audit evidence + production operations |
| Human-in-the-Loop        | 9             | Autonomy boundaries + escalation |
| Interop (MCP/A2A)        | 7             | Tool integrations + identity boundaries |

---

## Part 3: Assumptions / Risks / Open Items (3-5)

1. Shadow AI exists outside ServiceNow and is not fully registered, logged, or governed (compliance risk).  
2. “On‑prem only” may conflict with current ServiceNow deployment/integration patterns; network/data-flow constraints must be clarified early.  
3. Ticket text and operational logs likely contain personal data; anonymization/redaction requirements may be non-trivial and impact timeline.  
4. Least-privilege tool access (AD/IAM/VPN/etc.) may require new service accounts, approvals, and segmentation work that must be budgeted.  

---

## Part 4: What We Will Measure (3 KPI proposals)

1. **L1 auto-resolution rate (Phase 1 IT dept):** ≥ 50% of L1 tickets resolved end-to-end without human handling.  
2. **Misroute reduction:** misrouted tickets reduced from ~10% to ≤ 2%.  
3. **Audit evidence SLA:** 100% of automated decisions produce exportable evidence (model/version, sources, policy checks, tool calls, approvals) within 24 hours.  

---

## Part 5: Agent Classification

- **Governance tier:** Enterprise  
- **Registry/reuse potential:** Reusable “governed on‑prem agentic control plane integrated with ServiceNow” pattern for regulated EU enterprise clients.  

---

## Dependencies on Other Roles:

- AI-SEC: security posture, threat model, incident response requirements, access control standards  
- AI-DS: evaluation approach + golden dataset design, KB quality checks, multilingual retrieval validation  
- AI-DA: KPI definitions + dashboards, reporting requirements for board/Q3 2026 readiness  
- AI-PM: stakeholder alignment (incl. works council), scope/roadmap, acceptance criteria for pilot → scale  

---

## Questions I Deliberately Did NOT Ask (and why):

- “Which specific LLM vendor/model are you using?” — premature until on‑prem boundary, data constraints, and audit requirements are locked.  
- “What is the exact end-user UI design?” — important, but better led by AI‑FE once HITL checkpoints are defined.  
- “What chunk sizes/embedding model will we use?” — tactical ingestion details to decide after we confirm authoritative sources and PII constraints.  

