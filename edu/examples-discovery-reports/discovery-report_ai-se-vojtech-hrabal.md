# AI-SE Discovery & Delivery Plan

## Date: February 2026

## Author: Vojtech Hrabal

## Role: AI Software Engineer (AI-SE)

## Client: EuroHealth Insurance AG

## Engagement: AI Industrialization (On-Prem, EU AI Act Ready, 6 Months / €180K)

---

# 1 — Executive summary (one paragraph)

EuroHealth must shift from **fragmented, shadow AI** to a **governed on-prem AI runtime** that delivers measurable helpdesk ROI while meeting EU AI Act auditability. Phase-1 must be a narrow, high-confidence automation slice (L1 auto-resolution → HITL approvals) that proves containment, telemetry, and financial impact within the €180K / 6-month political window. This plan synthesizes the key findings and concrete technical guardrails so the AI-SE can deliver a board-defensible platform rather than another prototype.  

---

# 2 — One-page stakeholder map (who matters & why)

* **Hans Müller — CIO (Sponsor):** budget authority, board narrative → expects measurable 30% cost reduction. 
* **Stefan Weber — CISO (Gatekeeper):** EU AI Act classification, audit depth, kill-switch authority. 
* **Katarina (IT Ops):** integration, infra, on-prem constraints & GPU sizing.
* **Jan + 12 Helpdesk Agents:** adoption owners; trust & HITL UX determine real automation. 
* **Shadow AI owners (HR, Claims):** political risk; must be discovered and folded into registry. 

---

# 3 — Prioritized use cases (business → measurable metric)

1. **P1 — L1 Auto-Resolution (password resets, FAQs)** — metric: deflection % and approvals-per-day → direct cost deflection. 
2. **P2 — ServiceNow read/write automation (suggest + human approve)** — metric: agent time saved / ticket MTTR. 
3. **P3 — Intelligent routing (misrouting reduction)** — metric: reduction in misroutes %. 
4. **P4 — Unified AI Gateway / Registry / Governance** — metric: % of AI endpoints registered & audited. 
5. **P5 — Multi-language parity (EN/DE/CZ)** — metric: QoS parity gap ≤ 5%. 

---

# 4 — Core constraints & assumptions (from discovery)

* **On-prem only** (no cloud egress). 
* **Budget:** €180K for 6 months — likely tight for new multi-GPU procurement. Validate whether that includes hardware. 
* **KB quality:** ~30% outdated — must be remediated or gated for RAG to be safe. 
* **Existing automation:** Moveworks + ServiceNow present — must interoperate, not replace. 

---

# 5 — Architectural blueprint (AI-SE view, minimal + defensible)

## 5.1 High-level components

* **AI Registry (Control Plane):** unique IDs, owners, risk tier, version history, change approvals (mandatory before production). 
* **Runtime Gateway (FastAPI / middleware):** enforces RBAC, policy-as-code, prompt registry, prompt + model versioning, immutable trace IDs.
* **Vector store + retrieval layer:** Qdrant / Milvus (preferred) with pgvector fallback. Index metadata must include source id + freshness. 
* **Model hosting (on-prem):** 7B–13B class models for Phase-1 (Mistral 7B / similar). Llama-3 70B is high-quality but likely unaffordable under current budget.
* **Observability:** Prometheus + Grafana + structured logs (OpenTelemetry style) + tamper-evident immutable store for audit.
* **CI/CD & model registry:** Git-based, policy validation gates, golden dataset tests, blue/green or canary deployments. 

## 5.2 ServiceNow contract (Phase-1 limits)

* **Read:** ticket ID, history, assignment, KB links.
* **Write (restricted):** draft comment or resolution suggestion only — *no autonomous close or cross-domain reassigns*. All writes require human approval and apply policy version tagging.

## 5.3 HITL enforcement rules (runtime)

* Confidence ≥ 0.75 & low-risk → suggestion eligible for L1 with human approve.
* Confidence < 0.75 → force escalation.
* Financial/Claims tickets → mandatory escalation.
* All overrides logged with reason dropdown; override rate is a core KPI. 

## 5.4 Latency & infra SLOs (adoption-critical)

* **p95 end-to-end ≤ 2s**, streaming first token <800ms, hard timeout 5s. If exceeded, fallback to escalation. These targets are non-negotiable for agent adoption. 

## 5.5 Minimum viable infra sizing (Phase-1)

* **Target models:** 7B–13B; recommended 1–2× A100(40GB) or 2–3× L40S for sustained throughput (~15–20 parallel ticket evaluations). 70B class requires multi-GPU (4–8 GPUs) and likely exceeds budget. Validate procurement ASAP. 

---

# 6 — Observability & compliance (must-have)

* **Structured event for every request:** trace_id, timestamp, user_id (pseudonymized when required), model_version, prompt_version, retrieved_doc_ids + timestamps, confidence, policy_version, action (suggest/write), human_approval_flag. 
* **Tamper-evident immutable log store** with RBAC and export for audits (reconstruction SLA: <24 hours). 
* **Drift & KB freshness signals:** automated alerts when retrieval quality degrades or KB items’ last-updated > SLA threshold. 

---

# 7 — Risk register (top / mitigations)

1. **ServiceNow integration delay → ROI stall.**
   *Mitigate:* Week-1 integration spike + sandbox read/write test; require API contract doc.

2. **Under-sized infra (GPU) → model underperformance.**
   *Mitigate:* Use retrieval+smaller LLMs (7B–13B) for Phase-1; prepare hardware cost estimate; propose temporary cloud-equivalent appliance if allowed. 

3. **KB rot → hallucinations → trust collapse.**
   *Mitigate:* Ingestion gating, versioned KB, owner assignment, "KB fix" queue tied to escalations. 

4. **Shadow AI (ungoverned) → compliance exposure.**
   *Mitigate:* Rapid AI inventory sprint; network detection + registry mandatory entry for production release.

5. **Adoption resistance (helpdesk fear).**
   *Mitigate:* Constrain autonomy (L2), show explainability, approval UI, and early agent success stories. 

---

# 8 — Delivery roadmap (6 months, phased & measurable)

## Phase 0 — Week 0 (Immediate)

* Kickoff, governance board alignment (CIO + CISO), confirm budget scope (does €180K include hardware?). 

## Phase 1 — Weeks 1–2 (Critical feasibility)

* **Week 1:** AI inventory sprint (discover shadow AI), ServiceNow integration spike (sandbox read + write test), infra audit (GPU, network), logging schema finalization.
* **Week 2:** Vector DB PoC, model benchmark (7B/13B), baseline KPI confirmation (current deflection %, MTTR, agent time), lock Phase-1 scope (password resets + suggestions).

## Phase 2 — Month 2–3 (MVP build)

* Deploy runtime gateway + registry, CI/CD for prompts/models, observability pipeline, ServiceNow HITL flows for P1. Begin golden dataset testing. 

## Phase 3 — Month 4 (Expand)

* Add intelligent routing, expand KB connectors, start limited multi-language tests. Monitor override/reopen metrics. 

## Phase 4 — Month 5 (Scale)

* Broaden L1 categories, increase throughput, tighten drift detection, prepare Annex IV artifacts for conformity. 

## Phase 5 — Month 6 (Board readiness)

* Compliance validation, board-ready reporting package (cost deflection, adoption, audit readiness). Deliverable: executive dashboard + reconstructed audit trails.

---

# 9 — Success metrics (the five KPIs you must report weekly)

1. **Deflection rate (auto suggest → approved / total tickets).** 
2. **Override rate (% of suggestions overridden by agent).** 
3. **Mean time to resolution (MTTR) delta vs baseline.** 
4. **Audit reconstruction SLA (time to reconstruct a decision) — goal <24h.** 
5. **Percentage of AI endpoints registered (shadow AI reduction).** 

---

# 10 — Minimal deliverables to produce in the next 14 days (concrete)

1. **ServiceNow integration report** — endpoints validated, auth method, example read/write response times. 
2. **Infra sizing & procurement note** — recommendation for 7B–13B hosting vs cost estimate for 70B (if requested). 
3. **AI Registry seed** — CSV/registry with discovered systems + owners. 
4. **Logging schema + sample event** — includes required fields for EU AI Act audits. 
5. **Phase-1 scope lock** — signed off by CIO + CISO (password reset + routing suggestions). 

---

# 11 — Quick-wins (to build trust with Hans & Jan)

* **Show one reproducible password-reset suggestion** in ServiceNow sandbox with full audit trail and agent approve flow. (demo within Week-3). 
* **Publish a “shadow AI amnesty” registration window** — invite departments to register existing tools with a fast-track governance checklist. 

---

# 12 — Appendix — source contributions (for traceability)

* Theodor Georgescu — industrialization, telemetry, ServiceNow integration emphasis. 
* Praveen (day12) — environment & deployment assessment, stakeholder alignment. 
* Oleksandr Krutko — governance backbone, shadow AI discovery, KB questions. 
* Radek Jelinek (RJ) — operational constraints, CI/CD recommendations. 
* Tomasz Huc — use-case prioritization, next-step sequencing. 
* Ursu Sevastian (upgraded) — registry + Article-compliant logging and detailed latency/GPU SLOs. 

---

# Final recommended immediate actions (short checklist)

* [ ] Confirm whether €180K includes hardware; if not, get procurement hold. 
* [ ] Run Week-1 ServiceNow integration spike (read/write sandbox). 
* [ ] Run AI inventory sprint and create AI Registry entries. 
* [ ] Start model benchmarks (Mistral-class 7B) on available infra. 
* [ ] Ship a demo of password-reset suggestion with full audit trail to build board confidence.
