# Discovery Report - AI-SE
## Student: Vojtech Hrabal
## Date: February 26, 2026
## Client: EuroHealth Insurance AG
## Source: Day 12 CIO roleplay + Day 11 discovery packet

---

## 1. Stakeholder Analysis (AI-SE perspective)

- **Hans Muller (CIO):** Sponsor with board pressure; success means 30 percent cost reduction, platform unification, and compliance readiness.
- **Katarina Novak (IT Ops):** Critical for deployment feasibility, on-prem constraints, and runtime operations.
- **Stefan Weber (CISO):** Governance gate; drives EU AI Act readiness and security controls.
- **Jan Kovar + Helpdesk team:** Adoption gate; resistance risk if human override and role clarity are weak.
- **Shadow AI owners (HR, Claims):** High governance risk unless systems are inventoried and folded into one operating model.

---

## 2. Key Findings and Implications for My Workstream

- EuroHealth is not starting from zero; AI already exists but is fragmented and weakly governed.
- On-prem only is non-negotiable, so architecture and delivery plans must assume no cloud fallback.
- Knowledge base quality is a known issue (~30 percent outdated), making retrieval quality and ingestion gating first-order concerns.
- Budget and timeline are tight (EUR 180K / 6 months), so scope must be thin-slice and measurable.
- The engagement is industrialization, not a greenfield chatbot project.

**AI-SE implication:** prioritize controllable platform foundations (release control, auditability, policy enforcement, integration reliability) over feature breadth.

---

## 3. Technical / Functional Requirements to Investigate

1. **Deployment maturity:** Current dev/test/prod separation, release approvals, and rollback process for AI artifacts.
2. **ServiceNow integration contract:** API readiness, auth model, write boundaries, and failure behavior.
3. **Policy enforcement path:** Exact placement of PEP in runtime flow and CI/CD policy validation gates.
4. **Audit logging schema:** Required fields to reconstruct decisions and satisfy compliance evidence needs.
5. **Data safety controls:** PII filters in ingestion, response, and logs; ownership of KB freshness and remediation.
6. **Runtime SLOs:** Latency, policy decision availability, escalation response times, and incident alerting.

---

## 4. Risks Specific to My Area

1. **Pipeline risk:** Manual releases can bypass policy updates and create undocumented behavior changes.
2. **Integration risk:** ServiceNow API assumptions may fail in production, delaying measurable outcomes.
3. **Data quality risk:** Stale KB content drives wrong answers and quickly erodes trust.
4. **Compliance risk:** Incomplete logs or missing schema fields make forensic reconstruction impossible.
5. **Adoption risk:** If override/escalation workflow is unclear, teams will bypass the system.
6. **Capacity risk:** On-prem hardware limits can force model downgrades and quality trade-offs.

---

## 5. Recommended Next Steps (first 2 weeks)

### Week 1
- Run AI inventory sprint (all active AI systems, owners, data touched, control status).
- Execute ServiceNow integration spike in sandbox (read/write boundaries and auth validation).
- Baseline release process and define minimum CI/CD gate requirements for AI artifacts.
- Define logging schema v1 and map fields to compliance/audit expectations.

### Week 2
- Finalize thin-slice scope for Phase 1 (high-volume, low-risk workflows with clear KPI linkage).
- Draft deployment blueprint for on-prem runtime, including rollback and incident response path.
- Define policy validation stage in CI/CD and connect to policy file lifecycle.
- Establish KB quality ownership and freshness SLA proposal.

---

## 6. Dependencies on Other Roles in the Team

- **Need AI-SEC:** EU AI Act classification depth and required control evidence by article.
- **Need FDE:** Infrastructure constraints (GPU, networking, storage, runtime scale assumptions).
- **Need AI-DS:** Data quality audit method and multilingual evaluation criteria.
- **Need AI-DA:** Baseline metrics and dashboard design for compliance and operational KPIs.
- **Need AI-PM:** Scope lock, budget decisions, and stakeholder escalation chain.

---

### Day 13 bridge note
These dependencies become Day 13 interface contracts and must be explicit in `architecture-ai-se.md`.
