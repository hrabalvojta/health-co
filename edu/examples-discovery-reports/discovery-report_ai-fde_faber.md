# Discovery Report — FDE Workstream  
##       VLADIMIR FABER  
## Role: Full-stack Development Engineer (FDE)  
## Client: EuroHealth Insurance AG  
## Date: February 24, 2026  

---

# Executive Interpretation

Hans stated the objective as “cut remaining helpdesk costs by 30% in six months.”  
However, based on the roleplay discussion, the structural problem is not ticket volume — it is fragmented, ungoverned AI deployment across departments.

EuroHealth already operates:
- ServiceNow AI + Moveworks
- HR chatbot
- Claims LangChain prototype

These systems operate without centralized governance, unified logging, or enforceable policy controls.

From my perspective as FDE, this engagement is not a chatbot build — it is an AI industrialization program. The technical objective is to establish an on-prem, audit-ready AI control plane capable of unifying all AI systems under enforceable policy guardrails before the August 2026 EU AI Act milestone.

---

# 1. Stakeholder Analysis (FDE Lens)

## Hans Muller — CIO (Sponsor)
- Under board pressure to show measurable AI ROI.
- Needs governance consolidation + compliance narrative.
- Personal credibility tied to project outcome.

**Implication:** Early deliverables must visibly demonstrate governance maturity (registry, logging, traceability), not just automation.

---

## Stefan Weber — CISO (Implied Gatekeeper)
- Driving EU AI Act compliance.
- Holds veto authority over AI deployment.

**Implication:** Policy enforcement and audit traceability must be architectural primitives, not add-ons.

---

## Katarina Novak — IT Operations
- Owns on-prem infrastructure.
- Responsible for maintainability.

**Implication:** Stack must be supportable internally — no experimental tooling.

---

## Jan Kovar + 12 Helpdesk Agents
- Fear job displacement.
- Adoption risk.

**Implication:** Human-in-the-loop must be visible and enforceable.

---

## HR & Claims AI Owners
- Built shadow AI outside governance.
- Likely to resist centralized onboarding.

**Second-Order Risk:**  
If governance onboarding is slower than departmental experimentation cycles, shadow AI will persist outside the control plane and undermine unification.

---

# 2. Key Findings & Technical Implications

## Finding A: “Everyone’s doing their own thing.”

This reveals absence of:
- Unified AI registry
- Centralized logging
- Policy enforcement layer
- Cross-system traceability

### Technical Conclusion

Phase 1 must deliver a Governance Control Plane MVP that includes:
- Enterprise AI registry
- Trace ID generation + propagation
- Policy enforcement gateway
- Centralized audit logging
- Shadow AI onboarding workflow

Without this layer, cost reduction will occur without compliance control — which fails the board-level objective.

---

## Finding B: On-Prem Only (Non-Negotiable)

Eliminates:
- OpenAI API
- Azure OpenAI
- SaaS observability stacks
- Cloud vector DBs

### Architectural Implications

- On-prem LLM hosting required
- On-prem vector storage
- On-prem logging + SIEM integration
- GPU feasibility validation mandatory

### Budget Tension

€180K may not cover:
- Consulting scope
- Infrastructure upgrades
- GPU procurement

Infrastructure feasibility must be validated in Week 1 before committing to LLM selection.

---

## Finding C: Knowledge Base 30% Outdated

This is a structural blocker.

### Second-Order Effect Chain

Stale KB → Incorrect AI answers → Agent distrust → Increased overrides → No automation gain → KPI failure.

### Requirement

Knowledge audit and ownership assignment must precede large-scale automation.

---

## Finding D: Human Fear = Architectural Requirement

“Jan is nervous” is not a soft HR issue.

Architecture must include:
- Human override checkpoints
- Confidence scoring
- Clear escalation routing
- Explicit audit trail (AI vs human decision)

HITL must be enforceable at the policy layer.

---

# 3. Technical Requirements to Investigate

## Infrastructure Validation

- Confirm GPU availability and upgrade path.
- Validate container orchestration environment.
- Assess <2s latency feasibility under on-prem constraints.

---

## Enterprise AI Registry (Governance Core Component)

EuroHealth requires an authoritative enterprise AI registry functioning as the control-plane inventory for all AI-enabled workflows.

The registry must capture structured metadata including:

- Business owner (HR / Claims / IT)
- Data classification (PII / non-PII / sensitive health data)
- EU AI Act risk tier
- LLM model + version (including fine-tuning status)
- Integration endpoints
- Applied policy tier
- Human-in-the-loop configuration
- Last compliance review date
- Audit retention status
- Lifecycle state (pilot / approved / production / deprecated)

This registry enables:
- Shadow AI containment
- Regulatory traceability
- Controlled onboarding
- Cross-department expansion

---

## Policy Enforcement Architecture

- Define enforcement entry point (LLM gateway or orchestration layer).
- Generate trace ID at gateway level.
- Propagate trace ID across:
  - ServiceNow
  - Moveworks
  - HR chatbot
  - Claims prototype
- Enforce action-level policy checks before execution.
- Log every policy decision with immutable audit record.

---

## Observability & Audit

- Centralized log aggregation (SIEM compatible).
- Standardized log schema.
- Regulator-ready export format.
- Action-level audit for AI-triggered operations.

---

# 4. FDE Risk Register

## High Risks

1. On-prem LLM performance insufficient.
2. GPU infrastructure not covered by budget.
3. Absence of cross-system traceability.
4. KB staleness undermines trust.
5. Governance friction leads to shadow AI persistence.

## Medium Risks

1. 6-month timeline unrealistic without phased scope.
2. Privilege escalation via shared service accounts.
3. Audit retention misalignment with EU AI Act requirements.

---

# 5. Phased Strategy (Technical Reality Check)

Given constraints, Phase 1 must prioritize governance over aggressive automation.

## Phase 1 Focus
- Governance control plane
- Registry implementation
- Logging + traceability
- Controlled onboarding of one shadow AI tool
- Limited automation expansion

## Phase 2 (Post-Governance)
- Expand automation depth
- Scale to HR and Claims
- Optimize latency and model performance

Governance foundation must precede automation scale to protect Hans’s board narrative.

---

# 6. Recommended Next Steps (First 2 Weeks)

## Week 1
- Full AI ecosystem inventory.
- Infrastructure readiness validation.
- Registry data model design.
- Logging standard selection.
- KB ownership gap analysis.

## Week 2
- Governance MVP prototype.
- Trace ID propagation proof-of-concept.
- Policy enforcement entry design.
- HITL workflow architecture.
- Architecture diagram for cross-role review.

Deliverable:
Governance MVP capable of registering and auditing at least one existing AI system.

---

# 7. Dependencies on Other Roles

- AI-SEC → EU AI Act classification + enforcement rules.
- AI-DA → Knowledge audit + data classification mapping.
- AI-PM → Budget phasing + stakeholder comms.
- AI-SE → On-prem deployment pipeline.

---

# Final Strategic Assessment

Ticket reduction is the measurable KPI.  
Platform unification and compliance readiness are the structural objectives.

If governance is not established first, automation gains may be achieved but regulatory exposure and organizational fragmentation will persist.

This engagement should be framed as:

Phase 1: Govern and unify.  
Phase 2: Scale and optimize.

This is not a €180K chatbot project.  
It is the foundation of EuroHealth’s enterprise AI governance platform.