# Discovery Report — AI-SE (Environment & Deployment Assessment)
## Team AI-SE
## Client: EuroHealth Insurance AG
## Date: February 24, 2026

---

## 1. Stakeholder Analysis (AI-SE Perspective)

**Hans Müller (CIO) — Primary Sponsor**
- Under board pressure to show measurable AI ROI within 6 months (30% cost reduction target).
- Needs a *unified, governed, auditable* AI landscape (not another chatbot).
- Personal credibility/job security is tied to demonstrating a compliance-ready platform before the August 2026 deadline.

**Jan + 12 Helpdesk Agents — Operational Owners**
- Concerned about being replaced; adoption risk is real.
- Need clear human-in-the-loop controls, escalation paths, and visible override mechanisms to keep autonomy at L2 (constrained).

**Stefan Weber (CISO) — Governance/Risk Owner**
- Flagged shadow AI to the board; wants enforceable controls, auditability, and traceability across *all* AI tools (not only ServiceNow).

**Technical Stakeholders**
- **IT Ops (e.g., Katarina)**: Owns legacy monitoring (Nagios/custom scripts); needs unified visibility and incident readiness.
- **HR / Claims / Finance**: Running ungoverned prototypes today; Phase 2 demand depends on Phase 1 proving governance + ops discipline.
- **Works Council**: Headcount fixed; change must be framed as tool augmentation + safer escalations, not replacement.

---

## 2. Key Findings (What Hans Said → What It Means Technically)

**Finding 1 — Fragmentation is the core problem (not tooling).**  
Hans already has ServiceNow + Moveworks working for basic tickets, but shadow AI is spreading (HR chatbot, Claims LangChain, Finance GPT usage).  
**Implication for AI-SE:** We need a single governed control plane: unified runtime boundaries, deployment standards, telemetry, and audit trails across all AI systems.

**Finding 2 — “On‑prem only” is non‑negotiable.**  
No cloud option due to compliance (and likely data residency constraints across 8 EU countries).  
**Implication:** On-prem hosting, on-prem monitoring, on-prem CI/CD discipline (rollback, approvals, version pinning) must be feasible within budget.

**Finding 3 — Governance today is slow and manual.**  
Regulatory/process updates take ~3 months; AI decisions outside ServiceNow are not auditable.  
**Implication:** Policy-as-Code + automated validation gates are required for consistent, repeatable enforcement across ServiceNow extensions and departmental tools.

**Finding 4 — Knowledge base quality is a material delivery risk.**  
~30% outdated KB; no owner to maintain it.  
**Implication:** RAG ingestion must be versioned and measurable (freshness signals, evaluation gates) or trust will collapse during rollout.

**Finding 5 — Helpdesk adoption is a delivery dependency, not a nice-to-have.**  
Jan’s team is “adjusting,” which signals anxiety and resistance.  
**Implication:** L2 autonomy + HITL UX must be explicit: confidence signals, “why” explanations, escalation, and reversibility.

---

## 3. Technical & Functional Requirements (AI-SE Focus)

### 3.1 Platform Unification & Control Plane
- Central inventory/registry of AI systems (ServiceNow + departmental tools) with ownership, environment, and risk tier.
- One governed deployment model (standards for packaging, release approvals, and rollback).
- Unified monitoring + audit logging across ServiceNow AI, legacy tools (Nagios/scripts), and departmental AI prototypes.

### 3.2 On‑Prem Deployment Architecture (Phase 1)
- Containerized runtime (Docker/Podman) suitable for restricted networks / firewalls.
- On‑prem CI/CD with:
  - version pinning (model/prompt/policy)
  - automated tests + evaluation gates
  - blue/green or staged rollout
  - rollback and incident playbooks
- No external endpoints; all integrations/connectors must run inside EuroHealth’s boundary.

### 3.3 Policy‑as‑Code Enforcement
- Executable guardrails (not wiki pages) covering:
  - PII exclusion and data boundary rules
  - cross-border/data residency constraints
  - approval gates for high-impact actions
  - model/prompt/policy version governance
- Policies stored as YAML and/or a policy registry with versioning and audit trails.
- Enforcement at both runtime (request/response/tool use) and release time (CI/CD gates).

### 3.4 Monitoring & Observability (On‑Prem)
- On‑prem observability stack (e.g., Prometheus + Loki + Grafana or equivalent).
- Structured logs for:
  - user intent, tool calls, policy triggers, outcomes
  - latency, error rates, throughput, fallback usage
- Drift signals:
  - KB freshness and retrieval quality trends
  - escalation rate trends (confidence/coverage proxy)

### 3.5 Human‑in‑the‑Loop Controls (L2 Autonomy)
- Explicit checkpoints for:
  - policy exceptions
  - access changes
  - uncertain or high-impact recommendations
- Reversible actions + clear escalation ownership.
- Explainability basics: what sources/inputs were used and why the system escalated.

### 3.6 Interoperability (MCP/A2A / Connectors)
- Secure connectors for:
  - ServiceNow API (read/write where approved)
  - identity provider / RBAC boundaries
  - ticketing workflow actions
  - legacy monitoring tools and alerts
- Access control aligned with GDPR and “no employee PII in training data.”

---

## 4. Risks (AI-SE Specific)

1. **On‑prem compute / monitoring constraints may slow delivery** (no cloud APM, limited GPU/CPU capacity).
2. **Shadow AI inventory may be incomplete** (hidden tools and data flows could break governance design).
3. **Observability blind spots** across ServiceNow + legacy monitoring + shadow tools may hide failures and undermine trust.
4. **Policy changes not encoded in executable controls** → compliance drift as regulations evolve.
5. **Adoption risk from Jan’s team** → low usage means no measurable cost reduction and no board confidence.

---

## 5. Recommended Next Steps (First 2 Weeks)

### Week 1 — Establish the Deployment Reality
- Inventory *all* AI systems across departments (owner, purpose, data sources, environment).
- Map integrations, identity boundaries, and where data flows today.
- Assess monitoring signals available from ServiceNow, Nagios, and scripts.
- Draft initial Policy-as-Code categories (PII boundary, residency, approvals, versioning).

### Week 2 — Prove the Governed Platform Path
- Define unified CI/CD architecture and release gates (tests + policy + eval).
- Prototype observability pipeline (logs + dashboards + alerts) in on‑prem constraints.
- Align audit logging/retention needs with CISO (what must be recorded and how).
- Run HITL discovery with Jan’s team (override needs, escalation, trust signals).
- Validate multilingual workflow constraints (EN/DE/CZ) for tickets and governance artifacts.

**Deliverable target by Day 14:** Platform Architecture Draft + Governance Enforcement Model (Policy-as-Code + audit + ops).

---

## 6. Dependencies on Other Roles

**AI‑SEC**
- EU AI Act risk classification for this use case and required audit depth.
- Security controls for shadow AI containment/migration and threat model priorities.
- Residency + data boundary enforcement rules.

**AI‑DS**
- KB quality scoring and remediation approach (impacts ingestion + evaluation gates).
- Golden dataset + evaluation rubric for release gating.

**FDE**
- On‑prem model hosting options and feasibility (performance vs cost trade-offs).
- Infrastructure constraints to hit acceptable latency and throughput targets.

**AI‑PM**
- Scope control inside €180K / 6 months and stakeholder alignment plan.
- Change management approach for Jan’s team and works council sensitivities.

**AI‑DA**
- KPI definitions for board reporting (cost, CSAT, deflection, misroutes, MTTR).
- Monitoring dashboard requirements and data pipeline constraints.

**AI‑FE**
- Multi-language UX and trust indicators (sources, confidence, escalation, override).
- UI patterns for L2 autonomy (monitor + override) and safe error states.
