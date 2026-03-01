# Discovery Report — EuroHealth Insurance AG (Phase 1: IT Helpdesk)
## Role: Full-Stack Development Engineer (FDE) — Technical Feasibility Assessment
**Author:** Sebastian Michalowski  
**Date:** 2026-02-24  
**Inputs:** Day 11 EuroHealth brief + Day 12 roleplay (Hans Muller, CIO)

---

## 1) Stakeholder analysis (from FDE perspective)

- **Hans Muller (CIO) — Decision maker / budget owner**
  - Motivation: visible board results in ~6 months; personal credibility (“I keep my job”).
  - So what (for delivery): he will reward a plan that is **measurable + defensible** (benchmarks, options, risks), not “AI buzzwords.”
  - What he needs from FDE: 2–3 **on‑prem architecture options** with explicit hardware assumptions, latency/cost ranges, and a Week 1 validation plan.
- **Katarina Novak (IT Operations Lead) — Day-to-day owner / key influencer**
  - Motivation: reduce operational chaos; avoid outages; keep ServiceNow as the ITSM backbone.
  - So what (for delivery): if integration adds friction or instability, helpdesk will bypass it and the project dies.
  - What she needs from FDE: operability by design (monitoring/alerts, runbooks, rollback), plus **idempotent** ServiceNow actions (retries/backoff, failure handling).
- **Stefan Weber (CISO) — Compliance gate / potential blocker**
  - Motivation: EU AI Act readiness by ~Aug 2026; stop “shadow AI” risk; auditability.
  - So what (for delivery): “compliance” must be implemented as **system features** (not slideware) and be auditable on demand.
  - What he needs from FDE: provable controls (policy-as-code, logging, data boundaries) + a repeatable **evidence export** package (model/version, sources, tool calls, human overrides).
- **Jan Kovar + 12 helpdesk agents — End users / adoption gate**
  - Motivation: job security; workflow that doesn’t slow them down; trust in answers.
  - So what (for delivery): adoption depends on speed + trust; one week of wrong/stale answers will kill usage.
  - What they need from FDE: fast responses (target <2s where feasible), clear escalation/handoff, and an “override-first” workflow that keeps humans in control (L2 constrained).
- **Secondary stakeholders (Phase 2 pull)**
  - **HR / Claims / Finance**: already running ungoverned AI; will pressure for reuse if Phase 1 succeeds.
  - **Works council** (implied): headcount sensitivity; requires messaging and controls that show “augmentation + safety,” not replacement.

---

## 2) Key findings and implications for my workstream (FDE)

1. **The “30% cost reduction” is a metric; the real problem is ungoverned AI sprawl.**
   - Implication: build a *platform foundation* (governance + integration + audit), not a point chatbot.
   - Context: EuroHealth operates across **8 EU countries** (~**3,000 employees**). “Unified platform” decisions must scale beyond one team.
2. **On‑prem is non‑negotiable, but feasibility is unverified (GPU capacity + latency + cost).**
   - Implication: Week 1 infrastructure audit is mandatory; architecture decisions depend on it.
   - Risk tension: **€180K / 6 months** may not cover on‑prem GPU hardware (budget scope unclear).
3. **ServiceNow is the operational source of truth, but external API integration is unproven.**
   - Implication: prioritize a ServiceNow API v2 spike (read/write, auth, rate limits, sandbox access).
4. **Knowledge base quality is a first-order constraint (≈2,000 Confluence pages, ~30% outdated; no owner).**
   - Implication: a RAG system without a KB audit will fail in week one (hallucinations from stale content).
5. **This is an L2 (constrained) agent use case — never L3 — under EU AI Act high-risk expectations.**
   - Implication: implement guardrails + human monitoring/override as core workflow, not as “nice to have”.
6. **Timeline math doesn’t add up without phasing (on‑prem + 3 languages + governance + change mgmt).**
   - Implication: propose Phase 1 scope tight enough to ship (IT-only + governance core), then expand.
7. **Phase 1 is a door-opener; architecture must support Phase 2 scaling (HR/Claims/Finance).**
   - Implication: design for 10x scale (multi-dept, more tools, more data sources) even if Phase 1 is smaller.
8. **The helpdesk is not greenfield: ServiceNow/Moveworks already removed a material chunk of L1 volume.**
   - Implication: the next ROI step is governed L2 automation + reliable routing, not “another chatbot.”
   - Candidate early win: **L1 password resets (~40% of volume)** + safe auto-actions with audit trail.
9. **Baseline volumes/metrics must be validated (inputs drive sizing).**
   - Context to validate: historical **~15,000 tickets/month**, CSAT **~3.2/5**, and **~270K tickets/18 months** available for evaluation.
   - So what: sizing (GPU + concurrency), ROI math, and the autonomy matrix are guesswork until these are confirmed from ServiceNow reporting.

**Day 11 questions vs. Hans answers (quick check)**
- **Partially answered:** on‑prem constraint; existence of shadow AI; KB quality issue; budget/timeline pressure.
- **Still open (must discover next):** exact on‑prem boundary/data flows; enforceable policies; audit evidence format;
  ServiceNow integration constraints; autonomy boundaries by ticket category; SLOs/ops ownership.
  - So what: this list is the **Week 1 discovery backlog**; without it we cannot credibly commit to scope, latency, or automation levels.

---

## 3) Technical / functional requirements to investigate (FDE)

### 3.1 On‑prem LLM + infrastructure feasibility
- Confirm **available GPU capacity** (model sizes feasible, concurrency, batch/kv-cache strategy) vs **<2s latency** target.
- Decide candidate models for on‑prem inference (e.g., Llama/Mistral class) and quantify HW requirements/cost.
- Clarify whether **€180K includes hardware** or is services-only; if services-only, identify hardware funding path.

### 3.2 ServiceNow integration (API v2)
- Define read/write flows:
  - Ingest ticket + context; write back proposed resolution; update status; create/route tasks; escalation to L2/L3.
- AuthN/AuthZ pattern for tools (service accounts, least privilege, secrets management, approvals).
- Validate ServiceNow constraints: rate limits, network segmentation, available endpoints, sandbox/test environment.

### 3.3 Retrieval + ingestion (Confluence + ServiceNow KB)
- Build an ingestion pipeline with:
  - Source connectors (Confluence/KB), incremental sync, versioning, and “knowledge freshness” metadata.
  - Multilingual handling (EN/DE/CZ) and language-aware retrieval.
- Define a **KB quality gate** (sampling audit; owner assignment; stale-content detection) before production rollout.
- Plan for **ticket-history evaluation** (≈270K tickets/18 months) with a PII-safe sampling/redaction approach.

### 3.4 Governance + auditability (EU AI Act readiness)
- Implement policy-as-code guardrails (prompt/input/output constraints, tool permissions, forbidden actions).
- Define the **audit trail** schema: model/version, retrieved sources, policy checks, tool calls, human overrides.
- Retention, access controls, and evidence export requirements (for Stefan/auditors within 24h expectation).

### 3.5 Autonomy + workflow (L2 constrained agent)
- Ticket-category autonomy matrix:
  - Fully automated (safe, reversible), auto-suggest + human approve, and “never automate” categories.
- Human monitoring + override UX requirements (coordinate with AI-FE) and escalation path inside ServiceNow.

---

## 4) Risks specific to my area (with mitigations)

1. **On‑prem LLM performance / hardware shortfall (HIGH)**
   - Mitigation: Week 1 infra audit + latency benchmarking; size model to hardware reality; phase features.
2. **Budget ambiguity (services vs hardware) (HIGH)**
   - Mitigation: contract clarification early; provide 2–3 architecture options with cost bands.
3. **KB quality (~30% outdated, no owner) (HIGH)**
   - Mitigation: Phase 0.5 knowledge audit; implement freshness scoring; require content ownership workflow.
4. **ServiceNow API v2 integration risk (MEDIUM–HIGH)**
   - Mitigation: integration spike in Week 1; define minimal viable endpoints; fallback/manual workflow.
5. **PII leakage via tickets/logs/embeddings despite “no PII in training data” rule (MEDIUM–HIGH)**
   - Mitigation: PII redaction pipeline; strict logging policy; security review with AI‑SEC.
6. **Adoption resistance from Jan’s team (MEDIUM)**
   - Mitigation: design for speed + transparency; include agents in UAT; measure time-to-resolution and trust.

---

## 5) Recommended next steps (first 2 weeks)

### Week 1 (discovery-to-feasibility)
1. **Infrastructure + network audit (on‑prem):** GPU availability, storage, network path to ServiceNow/Confluence.
2. **ServiceNow API v2 spike:** prove read/write flows in a sandbox; document auth, rate limits, failure modes.
3. **KB inventory + sampling audit:** sample ~200 of ~2,000 Confluence pages; quantify staleness categories + owners.
4. **Define audit & policy baseline with AI‑SEC:** minimum viable evidence log, retention, access controls, guardrails.

### Week 2 (prototype-to-decision)
5. **Vertical-slice prototype:** on‑prem LLM + small RAG corpus + policy checks + audit log + ServiceNow ticket loop.
6. **Latency + cost benchmarks:** measure against <2s target; produce a feasibility memo with 2–3 model/HW options.
7. **Autonomy matrix draft:** propose which ticket categories can be L2 (auto) vs require human approval.
8. **Phase plan proposal:** Phase 1 (IT helpdesk + governance core) vs Phase 2 (CZ + other departments + scale).

---

## 6) Dependencies on other roles in the team

- **Checkpoint 2 dependency (posted):** I need **AI‑SEC** to tell me the **EU AI Act classification + minimum required audit evidence** (and **PII rules for tickets/logs/embeddings**) because my **on‑prem architecture + guardrail/logging design** depends on it.

- **AI‑SEC:** EU AI Act classification + required controls; PII handling rules for tickets/logs/embeddings; threat model.
- **AI‑PM:** phase scope decisions; budget split (services vs hardware); stakeholder/change management plan for Jan’s team.
- **AI‑DS:** evaluation plan (golden set from ticket history), KB quality metrics, multilingual retrieval validation.
- **AI‑DA:** KPIs + dashboards (board-ready monthly reporting; CSAT, automation rate validation, cost reduction proxy).
- **AI‑FE:** human-in-the-loop workflow UX (override, explanations, escalation) that fits ServiceNow daily usage.
- **AI‑SE:** integration implementation details (connectors, CI/CD on‑prem, reliability patterns).
