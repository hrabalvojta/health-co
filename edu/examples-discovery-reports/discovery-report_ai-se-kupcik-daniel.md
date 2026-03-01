# Discovery Report — EuroHealth Insurance AG (EuroHealth)
**Role:** AI Software Engineer (AI-SE), Kyndryl AI Consulting Team  
**Client stakeholder interviewed:** Hans Muller (CIO)  
**Session format:** 10-minute roleplay discovery discussion  

---

## 0. Executive summary (AI-SE lens)

EuroHealth already uses Moveworks/ServiceNow for basic ticket automation, but is facing fragmentation (“shadow AI” in HR and Claims) with no governance. Hans’ success criteria are business-led: **30% remaining helpdesk cost reduction in 6 months**, **unification under one platform**, and **EU AI Act compliance readiness by August 2026**, under a hard constraint of **on-prem only** and a **tight €180K/6-month budget**. A major technical blocker is **knowledge base quality** (~30% outdated) with **no ownership**, plus adoption risk from a helpdesk team that fears replacement.

This is an **industrialization** engagement: governed platform foundations + measurable workflow outcomes, not a greenfield chatbot build.

---

## 1. Task 1 — Analysis of the CIO ↔ AI-SE discussion

### 1.1 What Hans communicated (pattern)
Hans spoke in **outcomes + constraints**, not implementation details:
- 30% cost reduction (6 months)
- Unify AI under one platform
- EU AI Act compliant by Aug 2026
- On-prem only (non-negotiable)
- KB is ~30% outdated; no owner
- Helpdesk fears replacement
- Budget €180K / 6 months (tight)

**AI-SE implication:** translate business signals into deployable architecture and delivery constraints (integration, CI/CD, observability, governance hooks).

### 1.2 What was *not* provided (gaps to close)
Not covered in the roleplay, but critical for buildability:
- ServiceNow version, API readiness, auth patterns, integration restrictions
- SDLC maturity: CI/CD, environments, rollback, change windows
- Data governance: PII handling, retention, residency, audit logging requirements
- Concrete agent task list (what actions can be executed vs recommended)
- Baseline metrics definition for “30% cost reduction” (the denominator)

### 1.3 Hidden risks / second-order effects (project killers)
- **KB rot → wrong answers → trust collapse → more tickets (“double work”) → ROI failure**
- **Helpdesk fear → passive resistance → no KB updates/feedback → adoption failure**
- **Shadow AI → compliance incident → security clampdown → program blocked**
- **Budget + on-prem constraints → underpowered infra → latency/quality issues → bypass behavior**

---

## 2. Day 11 questions vs what Hans answered

### Q1 — Inventory of AI systems + governance/audit controls  
**Status:** Partially answered  
**Answered:** Moveworks/ServiceNow exists; HR chatbot + Claims LangChain prototype exist; “no governance” (shadow AI).  
**Open:** Complete inventory across org/countries; owners; where hosted; what data touched; access controls; audit logging; approval workflow; incident response.

### Q2 — Limits of current ServiceNow/Moveworks deployment  
**Status:** Minimally answered  
**Answered:** Handles “basic tickets.”  
**Open:** Deflection rate; escalation reasons; ticket categories failing; multilingual coverage; CMDB/KB linkage; integration gaps; what actions are blocked today.

### Q3 — Ingest/cleanse data to exclude PII and ensure quality across eight countries  
**Status:** Not answered (risk signals emerged)  
**Answered:** Only constraints implying sensitivity (on-prem + compliance) and KB quality alarm.  
**Open:** PII detection/redaction workflow; data classification; retention; residency rules; DSAR; fine-tune vs RAG-only approach; quality gates.

### Q4 — Multi-step agent tasks + systems to integrate with  
**Status:** Not answered  
**Answered:** Business goal implies automation is needed, but no task list.  
**Open:** Top workflows; allowed actions; approval gates; required system integrations (IAM, endpoint mgmt, monitoring, backups, HR, CMDB, SIEM, etc.).

### Q5 — Deployment pipeline (CI/CD, testing, rollback, drift monitoring)  
**Status:** Not answered  
**Answered:** On-prem only + tight timeline/budget (delivery risk).  
**Open:** Environments; promotion workflow; testing; model registry; rollback; monitoring; evaluation harness; drift strategy.

### New issues that emerged (not explicit in Day 11 questions)
- Knowledge base ownership vacuum (~30% outdated)
- Change management risk (helpdesk fear)
- Shadow AI governance gap (active proliferation)
- Budget realism vs on-prem infra cost
- Industrialization framing (platform + governance is the scope)

---

## 3. Stakeholder analysis (AI-SE perspective)

| Stakeholder                             | Role in outcome                           | What they care about                        | Influence on AI-SE work                                       | Risk/Opportunity |
|-----------------------------------------|-------------------------------------------|---------------------------------------------|---------------------------------------------------------------|------------------|
| Hans Muller (CIO) | Sponsor / budget    | ROI story, unification, compliance, speed | Sets scope constraints & success definition | May push timeline over feasibility; needs board-ready metrics |
| Katarina Novak (IT Ops Lead — implied)  | Delivery gatekeeper                       | Stability, ops readiness, change windows    | Controls runtime constraints, access, operating model         | If not aligned early, deployment will stall |
| ServiceNow/Moveworks Owner              | Integration gatekeeper                    | Platform stability, workflow governance     | Controls API access, auth patterns, write permissions         | Integration may be “available” but practically blocked |
| Stefan Weber (CISO) + DPO               | Veto power                                | On-prem enforcement, auditability, PII risk | Defines logging, access control, compliance gates             | Late engagement = rework or block |
| Jan Kovar (Helpdesk lead) + 12 agents   | Adoption power                            | Job security, workload, trust               | Determines usage, KB upkeep, feedback quality                 | Passive resistance can kill ROI |
| HR + Claims “shadow AI” owners          | Platform tenants / political risk         | Local speed & autonomy                      | Their prototypes influence platform requirements              | Risk of bypassing governance unless given a “paved road” |

---

## 4. Key findings and implications for AI-SE workstream

1) **Baseline ITSM AI exists; “what’s left” drives ROI**  
   - Implication: identify current failure modes and target high-volume, low-risk extensions.

2) **Shadow AI with no governance**  
   - Implication: implement minimum viable governance patterns (authN/Z, logging, approvals) and register all systems.

3) **KB quality + no ownership**  
   - Implication: build KB ingestion + quality gates and propose an ownership model; otherwise RAG will regress.

4) **On-prem only, non-negotiable**  
   - Implication: architecture must assume restricted egress, internal registries, internal monitoring, and hardened runtime.

5) **Budget/time constraints**  
   - Implication: thin-slice platform + 1–2 workflows; avoid broad platform rebuild; confirm whether budget includes hardware.

---

## 5. Technical / functional requirements to investigate (AI-SE)

### 5.1 On-prem deployment & infrastructure
- Standard runtime (K8s vs VMs), GPU availability, procurement lead times
- Network segmentation and egress restrictions
- Internal container/model registries, SBOM requirements
- Secrets management, TLS/cert standards

### 5.2 ServiceNow / Moveworks integration
- ServiceNow version + API enablement (read/write), auth model (OAuth/SAML/mTLS)
- What actions can be automated safely (ticket updates, KB suggestions, IAM actions)
- Rate limits, audit requirements, change windows

### 5.3 RAG & knowledge pipeline
- Knowledge sources (ServiceNow KB, Confluence/SharePoint, file shares)
- Ingestion + chunking strategy, metadata taxonomy, access controls
- Freshness SLAs, approvals, and rollback of incorrect articles

### 5.4 CI/CD and quality gates for AI services
- Environments and promotion workflow
- Automated tests: prompt-injection suite, regression eval sets, retrieval quality checks
- Rollback plan for prompts/configs/models

### 5.5 Observability and auditability
- Central logging schema: who asked, what retrieved, what answered, what tool/actions executed
- Metrics: latency, deflection, escalation, tool-call success rate, answer quality sampling
- Incident playbooks for unsafe outputs or suspected data leakage

---

## 6. AI-SE risks (with second-order effects)

1) **RAG failure from stale KB** → trust collapse → increased tickets → cost target missed  
2) **Shadow AI persists** → fragmentation continues → “unified platform” fails politically  
3) **Budget vs on-prem infra mismatch** → underpowered models → latency/quality issues → low adoption  
4) **Undefined autonomy boundaries** → security blocks tool actions → agent becomes “chat-only” → ROI miss  
5) **Helpdesk resistance** → low KB upkeep + biased feedback → silent failure mode  
6) **Late security involvement** → rework or deployment veto

---

## 7. Recommended next steps (first 2 weeks)

### Week 1 — Feasibility + control the blast radius
1) **AI system inventory (“AI registry sprint”)**: owners, data touched, hosting, controls, risk level  
2) **ServiceNow integration spike**: validate auth + read/write in sandbox; document constraints & approvals  
3) **On-prem runtime feasibility**: confirm K8s/VM, GPU capacity, internal registries, network rules  
4) **Observability minimum**: define logging schema + retention and where logs live

### Week 2 — Thin-slice platform + pick ROI workflows
5) **Define autonomy boundaries**: allowed actions vs recommendations; human-in-loop checkpoints  
6) **Select 1–2 workflows** (high volume, low risk, measurable) to drive 6-month ROI  
7) **CI/CD blueprint**: repo structure, environments, promotion/rollback, evaluation gates  
8) **KB ownership proposal**: nominate owner(s), freshness SLA, “KB fix queue” tied to escalations

**Week-2 output:** deployable thin-slice architecture + prioritized backlog + success metrics definition.

---

## 8. Dependencies on other roles (cross-role requirements)

- **AI-SEC:** EU AI Act posture + risk classification; logging/retention; threat model & red-team plan  
- **FDE:** on-prem hosting constraints, GPU sizing/cost, network segmentation, storage, runtime hardening  
- **AI-DS:** KB audit methodology; eval set design; RAG quality metrics + acceptance thresholds  
- **AI-DA:** baseline metrics for ROI (cost per ticket, deflection, MTTR, escalation rate)  
- **AI-PM:** phased scope plan, budget allocation, confirmation whether €180K includes hardware/licensing

---

## 9. Shallow-analysis checks (self-challenge)

Before final submission, validate these assumptions explicitly:
- What exactly is “30% cost reduction” measured against? (define the denominator)
- Who has authority to stop or absorb shadow AI into the platform?
- Who owns the KB after go-live, and what is the freshness SLA?
- Does the €180K include infrastructure (GPU hardware) or only services?
- What actions are permitted for agents (write access) vs prohibited?

