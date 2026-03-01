# Discovery Report — Customer Requirements (AI-PM Perspective) — EuroHealth Insurance (v1)

## 1) Stakeholder Map
- **Decision maker (economic buyer):** Hans Muller (CIO) — wants order, ROI, board confidence (“keep my job” driver)
- **Key influencers / operators:**
  - Katarina — ITSM/ServiceNow operator (knowledge base quality view; platform details; owns “how it really works”)
  - Jan — Helpdesk lead/manager (frontline adoption + morale gatekeeper; can make or break rollout)
  - HR team lead — owns HR chatbot (shadow/parallel capability)
  - Claims team lead — owns Claims LLM prototype (“LangChain thing nobody approved”)
- **Security/Compliance veto owner:** Compliance team + Stefan (EU AI Act pressure; governance expectations)
- **End users:** Helpdesk agents; employees submitting IT tickets; potentially broader internal users later
- **Hidden stakeholders:**
  - Board (expects cost reduction + compliance readiness signal)
  - Country/regional IT leads (8 countries) and language/localization owners (3 languages)
  - Works council / labor relations (implied risk via “replacement” fear)

## 2) Use Cases (Prioritized)

### P1 (Must-have): Unified IT Helpdesk AI under ServiceNow (industrialized, governed)
- **Problem it solves:** Fragmented tools + inconsistent experience; need measurable cost reduction
- **Who benefits:** CIO/board (ROI + control), IT Ops (standardized workflow), Helpdesk (assistive automation)
- **Success metrics (initial):**
  - 30% reduction in remaining helpdesk costs in 6 months
  - Reduction in ticket handle time / deflection rate improvements (baseline required)
  - Adoption: % of agents using AI assist daily; CSAT not degraded
- **Constraints / assumptions:**
  - **No cloud** — must run in EuroHealth data center in phase 1
  - ServiceNow is core; Moveworks exists today inside ServiceNow for basic tickets
  - Knowledge base is partially outdated; can’t fully clean before starting

### P2: Governance + “Shadow AI” consolidation program (stop the sprawl)
- **Problem it solves:** HR chatbot + Claims prototype + other experiments “nobody approved” → uncontrolled risk and duplicate spend
- **Who benefits:** CIO, compliance/security, IT platform owners
- **Success metrics:**
  - Complete inventory of AI tools/use cases + owners + data touchpoints
  - Defined standards: approval path, model use policy, logging, monitoring, review cadence
- **Constraints:** Must be presented as enabling innovation and control (avoid political backlash)

### P3: EU AI Act readiness (compliance as a selling point)
- **Problem it solves:** Compliance deadline pressure; reduce regulatory and reputational risk
- **Who benefits:** Compliance, CIO/board, security
- **Success metrics:**
  - EU AI Act readiness package for the platform by August 2026 (evidence + documentation + controls)
- **Constraints:** Depends on use-case classification + governance design decisions (needs AI-SEC + Legal/Compliance)

## 3) Key Findings from the Meeting

### What we heard (business reality)
- “We already have AI tools… nobody governs it.” (Moveworks + HR chatbot + Claims prototype)
- “Absolutely not” to cloud — data center only
- Knowledge base: ~1/3 outdated/garbage; no time to clean first
- Success: 30% cost reduction in 6 months + unify experiments + compliance-ready before August 2026
- Helpdesk team is nervous about replacement (adoption risk)
- ServiceNow is central; API exists but external use is unclear/untested
- EU AI Act pressure is actively coming from Stefan

### What it means for delivery (requirements)
- This is **not** a “build a chatbot” project — it’s a **platform + operating model + rollout** program
- The “MVP” must include **governance + measurement + adoption plan**, not just features
- “On-prem only” drives vendor shortlist, architecture path, and timeline feasibility
- Data quality cannot be deferred: we need **a pragmatic content audit + refresh loop** in parallel with phase 1
- Compliance is part of the product story: **controls and documentation are deliverables**
- Integration risk (ServiceNow/API) must be de-risked early via feasibility tests

### Non-negotiables
- No cloud
- ServiceNow-centered reality (even if unified layer is built around it)
- ROI target + timeline pressure
- Compliance readiness expectation

### Still ambiguous / needs validation
- Baseline metrics (current cost, handle time, deflection, CSAT) — required to prove 30%
- Budget details (we heard €180K referenced) vs. true infra cost (GPU/on-prem LLM) — likely gap
- ServiceNow version / integration feasibility and ownership boundaries
- Exact scope boundaries for “unification” (what stays vs. what gets replaced: Moveworks? HR chatbot? Claims prototype?)
- Country/language rollout scope for Phase 1 (avoid boiling the ocean)

## 4) Risks (with mitigations)
- **Scope creep risk (8 countries, 3 languages):**
  - *Mitigation:* Phase-gate rollout (1–2 countries + 1 language first), explicit Phase 1 boundaries
- **Data/knowledge quality risk (~30% outdated):**
  - *Mitigation:* Week 1–2 audit + “content refresh sprint” loop; measure KB freshness KPIs
- **Adoption / change management risk (Jan’s team fears replacement):**
  - *Mitigation:* Position as “agent assist,” define HITL flows, involve helpdesk champions, training + comms plan
- **Governance risk (shadow AI continues in parallel):**
  - *Mitigation:* Inventory + lightweight intake/approval process; enforce “single front door” for new AI use cases
- **Timeline risk (6 months for unify + build + operate):**
  - *Mitigation:* De-risk early (ServiceNow API test, on-prem LLM decision by Week 2), strict MVP
- **Budget risk (€180K may not cover on-prem infra):**
  - *Mitigation:* Early TCO + hardware sizing with FDE; options for smaller models / phased infra investment
- **Compliance risk (EU AI Act readiness by Aug 2026):**
  - *Mitigation:* Start classification + controls now; bake documentation, logging, and review into “definition of done”

## 5) Next Steps (Time-boxed, measurable)

### Week 1
- Stakeholder alignment session: Hans + Katarina + Stefan + Jan (confirm non-negotiables, decision rights)
- Baseline metrics pull (current helpdesk cost + handle time + deflection + CSAT)
- Shadow AI inventory kickoff: list tools, owners, data touchpoints, current usage

### Week 1–2
- Knowledge audit: sample ~200 of ~2,000 Confluence pages; tag freshness + criticality + owner
- ServiceNow API feasibility test (external integration + authentication + rate limits + data access)
- Draft Phase 1 scope + rollout plan (countries/languages + pilot group definition)

### Week 2
- Architecture/product decision checkpoint:
  - On-prem LLM approach shortlist + rough TCO
  - Confirm target experience: “agent assist” vs “end-user deflection” split
- Draft governance MVP: intake workflow, logging/monitoring expectations, model usage policy

### End of Month 1
- Pilot readiness review: metrics baseline locked, first KB refresh loop running, pilot cohort trained, reporting cadence set for board updates

## 6) Dependencies on Other Roles / Teams
- **AI-SEC / Compliance:** EU AI Act classification guidance + required controls + documentation checklist
- **FDE / Platform/Infra:** On-prem LLM feasibility, GPU sizing, cost/TCO, deployment constraints
- **AI-DS:** Evaluation plan (quality metrics, hallucination/error testing), audit methodology for KB sampling
- **AI-DA / Analytics:** Baseline metrics extraction and ongoing KPI dashboarding
- **ServiceNow owner (Katarina/ITSM):** API feasibility, workflow integration design, operational constraints
- **Change management / HR:** Training + comms plan; managing “replacement anxiety”