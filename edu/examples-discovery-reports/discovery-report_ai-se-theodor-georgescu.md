# DISCOVERY REPORT  
## EuroHealth Insurance AG  
**Role:** AI Software Engineer (AI-SE)  
**Consultant:** Theodor Georgescu  
**Date:** 2026-02-24  
**Engagement Type:** AI Industrialization & Platform Consolidation  

---

# 1. STAKEHOLDER MAP

## Executive Sponsor  
**Hans Muller — CIO**  
- Budget authority: €180K / 6 months  
- Board-level visibility  
- Success metrics:
  - 30% helpdesk cost reduction  
  - Unified AI governance platform  
  - EU AI Act compliance by August 2026  
- Personal driver: measurable early ROI tied to credibility  

## Operational Owner  
**Head of IT Operations (Katarina)**  
- Owns ServiceNow environment  
- Controls infrastructure feasibility  
- Critical for integration velocity  

## Compliance Gatekeeper  
**CISO (Stefan)**  
- Determines EU AI Act classification  
- Influences logging depth, explainability, and audit requirements  
- Potential veto authority  

## End Users  
**Helpdesk Lead (Jan) + 12 Agents**  
- Adoption risk due to job displacement fears  
- Workflow integration determines real ROI realization  

## Shadow AI Stakeholders  
- HR internal chatbot  
- Claims LangChain prototype  
- Moveworks in ServiceNow  

**Implication:**  
This is not a greenfield chatbot build. It is an AI runtime consolidation and governance mandate across fragmented initiatives.

---

# 2. PRIORITIZED USE CASES (WITH ROI LINKAGE)

### Baseline
- Current auto-resolution: 35%  
- Estimated target: ~60% automation required to achieve 30% cost reduction  

### P1 — Password Reset Auto-Resolution  
Highest ticket volume → direct, measurable ROI driver.

### P2 — ServiceNow Read/Write Automation  
Mandatory for cost deflection measurement and workflow embedding.

### P3 — Intelligent Ticket Routing  
Reduces misrouting (~10%) → efficiency improvement.

### P4 — Unified AI Gateway  
Consolidates fragmented AI tools → governance + compliance ROI.

### P5 — Multi-Language Support (EN/DE/CZ)  
Adoption enabler, not primary ROI driver.

---

# 3. KEY FINDINGS (BUSINESS → ENGINEERING TRANSLATION)

## 3.1 Industrialization, Not Prototyping  
AI tools already exist. Fragmentation and lack of governance are the core problems.

**AI-SE Implication:**  
Architecture must enforce consolidation through a centralized runtime layer.

---

## 3.2 ROI Is Non-Negotiable  
Cost reduction and board-level reporting drive decision velocity.

**AI-SE Implication:**  
Instrumentation and measurable automation metrics are first-class system requirements.

---

## 3.3 On-Prem Constraint  
Cloud usage prohibited.

**AI-SE Implication:**  
- On-prem LLM hosting  
- GPU capacity planning  
- Hardware-performance tradeoff decisions  

---

## 3.4 Knowledge Base Quality Risk (~30% outdated)  
Unstructured KB increases hallucination probability.

**AI-SE Implication:**  
RAG reliability depends on retrieval precision, filtering strategy, evaluation thresholds, and version traceability.

---

## 3.5 ServiceNow Integration = Primary Execution Risk  
Integration feasibility directly impacts automation delivery.

**AI-SE Implication:**  
Integration spike must precede model optimization.

---

# 4. ARCHITECTURAL IMPLICATIONS (AI-SE SPECIFIC)

## 4.1 Central AI Runtime Layer

**Core Responsibilities:**
- Unified inference gateway (FastAPI-based runtime)
- Prompt registry + version control
- Policy-as-code enforcement (OPA or equivalent)
- RBAC enforcement
- Immutable audit logs

**Candidate Model Families (On-Prem):**
- Llama 3 70B  
- Mistral 7B / 8x7B  

Evaluation criteria:
- Latency under ticket SLA constraints  
- Hardware efficiency  
- Accuracy under constrained context windows  

---

## 4.2 Vector Store Evaluation

Options:
- Qdrant (lightweight, strong filtering)
- Milvus (scalable, GPU acceleration)
- PostgreSQL + pgvector (cost-efficient fallback)

Evaluation Criteria:
- Query latency
- Operational simplicity
- On-prem maturity
- Fine-grained metadata filtering support

---

## 4.3 Observability & Governance Stack

- Prometheus + Grafana (self-hosted)
- Structured logging (OpenTelemetry-compatible)
- Model version tagging
- Prompt version tagging
- Retrieval trace logging

**Rationale:**  
If it cannot be measured, it cannot be defended to the board.

---

## 4.4 Evaluation & Containment Telemetry (NEW)

Cross-role discovery highlights that the 30% cost reduction target may be constrained by automation ceiling, multilingual variance, and adoption behavior.

Therefore, the runtime must instrument:

- Ticket classification (L1 vs L2/L3)
- Auto-resolution vs assist vs escalation
- Human override events
- Escalation reason codes
- Re-open rate tracking
- Language-level performance metrics (EN/DE/CZ)

Additionally, the architecture must support:

- Golden dataset replay capability
- Confidence + retrieval score logging
- Drift detection triggers
- Language parity monitoring (flag >5% performance gap)

Automation must be measurable and defensible — not assumed.

---

# 5. RISK DEPTH (CASCADE ANALYSIS)

## 5.1 Primary Risk — ServiceNow Integration Delay

Integration delay  
→ Automation rollout stalls  
→ ROI not visible  
→ Board confidence declines  
→ Shadow AI regains credibility  
→ Consolidation mandate weakens  

**Mitigation:**  
Mandatory Week 1 integration spike.

---

## 5.2 Financial–Technical Coupling Risk

Hardware budget constraint  
→ Smaller model selection  
→ Lower answer quality  
→ Reduced trust  
→ Lower adoption  
→ Missed ROI target  

**Mitigation:**  
Phase 1 narrowed to high-confidence, high-volume use case.

---

## 5.3 Data Quality Risk

Outdated KB  
→ Hallucinated responses  
→ Agent distrust  
→ Low adoption  

**Mitigation:**  
Strict retrieval filtering + evaluation gate before expansion.

---

## 5.4 Automation Ceiling & Financial Realization Risk (NEW)

The 30% cost reduction target assumes sufficient remaining automatable workload after Moveworks’ existing L1 automation.

Risks:

- Remaining L1 volume may be insufficient
- High override rates may reduce containment
- Multilingual performance variance may fragment automation success
- Workload reduction may not directly convert to financial savings due to fixed cost structure

**Mitigation:**

- Validate L1 share and containment ceiling by Week 2
- Instrument deflection vs assist vs escalation separately
- Monitor override frequency and re-open rates
- Expand ROI modeling beyond pure auto-resolution (routing accuracy, time saved)

Without structured containment telemetry, the 30% target cannot be validated or defended.

---

# 6. STRATEGIC 6-MONTH DELIVERY ARC

**Month 1**  
Infra validation + integration spike + logging framework.

**Month 2–3**  
Deploy P1 password reset automation (single language).

**Month 4**  
Expand automation + introduce intelligent routing.

**Month 5**  
Multi-language rollout.

**Month 6**  
Compliance validation + board-ready reporting package.

---

# 7. NEXT STEPS (FIRST 2 WEEKS)

## Week 1
- ServiceNow integration spike  
- GPU benchmarking  
- Shadow AI inventory  
- Logging schema finalization  

## Week 2
- Model benchmarking  
- Vector DB proof-of-concept  
- KPI baseline confirmation  
- Phase 1 scope lock  
- Validate automation ceiling assumptions  

---

# 8. CROSS-ROLE ARCHITECTURAL DEPENDENCIES (UPGRADED)

| Role | Dependency | Architectural Impact |
|------|------------|---------------------|
| AI-SEC | EU AI Act risk-tier classification | Defines autonomy gating model and logging depth |
| AI-SEC | Audit evidence fields & retention | Determines audit schema and redaction layer |
| FDE | GPU sizing & infra topology | Defines viable model class and latency budget |
| FDE | ServiceNow API feasibility | Validates integration boundary and write authority |
| FDE | Audit trace reconstruction (<24h target) | Requires full decision-chain logging capability |
| AI-DS | Retrieval evaluation thresholds | Defines automation gating logic |
| AI-DS | Golden dataset design | Requires evaluation hooks within runtime |
| AI-DS | Automation ceiling modeling | Requires containment telemetry instrumentation |
| AI-DA | Baseline cost structure & realization model | Defines ROI instrumentation granularity |
| AI-PM | Minimum Governance Baseline scope | Defines enforceable Phase 1 control set |
| AI-PM | Scope sequencing | Defines segmentation and modular runtime design |

AI-SE acts as the enforcement and telemetry convergence layer across all roles.

---

# 9. DISTINCTION INSIGHT

If hardware budget constraints force aggressive model downsizing prematurely, underperformance may erode trust among helpdesk agents and board stakeholders.

Therefore, Phase 1 must prioritize narrow, high-confidence automation scenarios to guarantee early measurable success before scaling complexity.

Additionally, automation feasibility must be continuously validated against containment telemetry and multilingual performance stability to avoid overcommitting to unrealistic ROI targets.

---

# CONCLUSION

The AI-SE mandate is not to build a chatbot.

It is to engineer a governed, enforceable AI runtime platform that:

- Delivers measurable ROI  
- Protects sponsor credibility  
- Survives on-prem constraints  
- Meets compliance requirements  
- Scales beyond Phase 1 without architectural rework  

The Control Plane must not only enforce governance — it must continuously validate automation feasibility, multilingual stability, and financial realization under evolving technical and regulatory constraints.

Industrialization, not experimentation, defines success in this engagement.