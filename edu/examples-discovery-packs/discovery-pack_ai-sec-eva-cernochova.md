# EuroHealth Insurance — AI Governance Discovery Brief
**Kyndryl AI Consulting | Security & Compliance Engagement**

**Client:** EuroHealth Insurance (EU-based)  
**Scope:** Industrialize fragmented AI landscape → governed, production-grade, auditable platform  
**Budget:** €180K / 6 months | **Deadline:** Q3 2026 board framework | **EU AI Act:** Dec 2027  
**Stakeholder:** CIO (first meeting) | **AI-SEC Focus:** Governance, compliance, threat posture  

---

## Framing Statement for CIO

*"You're not calling us to build AI—you're calling us to make the AI you already have defensible. ServiceNow with Moveworks works for L1, but it's created fragmentation, shadow AI, and zero audit trail. Over the next 6 months, we need to prove that Kyndryl can unify your AI landscape into a governed, production-grade, compliance-ready platform that scales company-wide. These questions unlock what that means for EuroHealth."*

---

# ▶ PART 1: Discovery Questions (10)

---

### **Q1: Autonomy Boundaries & Human-in-the-Loop Checkpoints**

**Question:**  
*What actions are your AI agents currently allowed to execute autonomously in ServiceNow/Moveworks, and which decisions require human confirmation before execution or logging? Specifically: ticket routing, resolution suggestions, escalations, data exports, and cross-system updates—which are auto-approved vs. requiring HITL sign-off?*

**Why it matters:**  
Defines the HITL surface area and risk appetite. Autonomous execution without audit checkpoints = compliance liability. This tells us where governance must intervene and which workflows need redesign for auditability.

**Red flag:**  
"Everything runs autonomously—we trust Moveworks" OR vague answers like "we review logs after the fact." Both indicate no explicit HITL policy and weak governance mindset.

**KAF Component:** **HITL** (Human-in-the-Loop)  
**Secondary:** Core (policy definition), Run Safe (monitoring)

---

### **Q2: Code-Enforceable Rules vs. Documentation Gap**

**Question:**  
*Which specific rules must be programmatically enforced—not just documented—to meet your EU AI Act readiness by Dec 2027? Examples: PII masking, data residency, model output filtering, access controls, language/content boundaries, decision explainability. What are the current gaps preventing ServiceNow/Moveworks from codifying these today?*

**Why it matters:**  
EU AI Act (and internal audit) demands machine-enforceable governance, not narrative policy. This question surfaces the Policy-as-Code gap and tells us the technical scope for the PoV. Answers reveal whether they have a compliance baseline or are starting from scratch.

**Red flag:**  
"We have policies documented" (but not in code) OR "Moveworks doesn't support policy enforcement" OR "We haven't thought about Dec 2027 yet." All three indicate regulatory debt and potential scope creep.

**KAF Component:** **Policy-as-Code**  
**Secondary:** Core (governance framework), Run Safe (enforcement)

---

### **Q3: Governance Adaptation Velocity & Change Readiness**

**Question:**  
*When a regulation changes (e.g., GDPR reinterpretation, a new AI Act guideline) or an internal policy is updated, how fast can you adapt your AI systems? Days? Weeks? Months? Do you have a change-control process, and can you push policy updates without code deployment?*

**Why it matters:**  
Regulatory agility = operational maturity. If policy changes require code redeploy, you're months from compliance. This reveals whether the platform must support dynamic policy injection (critical for EU AI Act compliance by Dec 2027) and governance handoff readiness.

**Red flag:**  
"Weeks or months" OR "policy changes require code release cycles" OR "no formal change control." Indicates brittle architecture and high re-arch cost.

**KAF Component:** **Policy-as-Code**  
**Secondary:** Core (ops maturity)

---

### **Q4: Auditability, Defensibility & Code-Enforceable Governance**

**Question (PRIMARY DISCOVERY DRIVER):**  
*When this engagement is finished, what must be true for you to confidently say, "Yes, our AI is under control and defensible"—regardless of how we technically achieve it? Specifically:*
- *What immutable audit artifacts does the board/CISO require (decision traces, model versioning, data lineage), and for how long must they be retained (legal hold window)?*
- *Where does ServiceNow + Moveworks hit the wall today in providing this traceability?*
- *Which narrative rules (access controls, data governance, PII handling) are you prepared to convert to machine-enforceable policy files within the €180K/6-month scope?*

**Why it matters:**  
This is the north star. The CISO went to the board because there's NO audit trail. Everything else flows from this answer. Auditability is the board's pain; Policy-as-Code is the technical solution; HITL checkpoints enforce it operationally.

**Red flag:**  
"We're not sure what audit means" OR "Moveworks already logs everything" (without clarifying how/retention) OR "we need 10 years retention for everything" (unrealistic). All three suggest governance immaturity and scope explosion risk.

**KAF Component:** **HITL** (Human-in-the-Loop audit & attestation)  
**Secondary:** Policy-as-Code (rule enforcement), Run Safe (logging & monitoring), Core (framework definition)

---

### **Q5: ServiceNow + Moveworks Integration Constraints**

**Question:**  
*What does your current ServiceNow + Moveworks setup do well, and where does it hit the wall? Specifically: audit logging, data lineage, policy enforcement, cross-system integration (e.g., HR systems, finance), model versioning, and re-trainability. Are these integrations contractually locked in, or do you have flexibility to evolve them?*

**Why it matters:**  
Defines the Interop surface. If Moveworks is contractually immutable + lacks audit APIs, we need a governance wrapper (not replacement). If they have flexibility, we can re-architect. This tells us whether the PoV is a "thin governance layer" or "wholesale platform re-design."

**Red flag:**  
"Moveworks can do anything" (inflated expectations) OR "we can't touch it / it's a black box" (no integration path) OR "vendor won't give us logs/data access." First = scope explosion; second & third = need governance bridge architecture.

**KAF Component:** **Interop** (Integration & connector strategy)  
**Secondary:** Core (governance boundary)

---

### **Q6: Data Governance, Classification & PII Handling**

**Question:**  
*Walk me through a typical helpdesk ticket flow: what data enters (customer demographics, policy numbers, medical info?), how is it classified (PII, confidential, restricted?), which AI systems touch it, and what rules govern retention, deletion, and export? Do you have a data governance policy today, and is it actively enforced in your current setup?*

**Why it matters:**  
Ingestion hygiene is foundational. EU insurance + healthcare intersection = strict data rules. This reveals whether data classification is a control or a gap, and it tells us the Ingestion + Policy-as-Code scope.

**Red flag:**  
"We don't classify data" OR "PII handling is informal" OR "we haven't thought about GDPR for AI" (given insurance + EU context). All indicate data governance debt and high compliance risk.

**KAF Component:** **Ingestion** (data classification, governance mapping)  
**Secondary:** Policy-as-Code (PII rules), Core (compliance baseline)

---

### **Q7: Model Lifecycle, Versioning & Approval Gates**

**Question:**  
*Do you have a model registry or change-control process for your AI systems? Specifically: how are new models tested, approved, and deployed? How do you track model versions and performance baselines? If a model regresses, how do you detect and roll back? Can you certify that every model in production has been validated?*

**Why it matters:**  
Model governance = compliance cornerstone. EU AI Act requires risk-based validation. This tells us whether they have a model ops discipline or whether every model change is ad-hoc, which is a board-level compliance gap.

**Red flag:**  
"No formal testing / approval process" OR "Moveworks pushes models auto-magically" (no control) OR "we don't track versions." All indicate zero model governance and are unacceptable for Dec 2027 EU AI Act compliance.

**KAF Component:** **Policy-as-Code** (model certification gates, approval workflow)  
**Secondary:** Run Safe (monitoring), HITL (approval checkpoints)

---

### **Q8: Observability, Drift Detection & Run-Safe Monitoring**

**Question:**  
*Today, do you monitor your AI systems for performance drift, data drift, anomalous access patterns, or security threats? What metrics do you track (accuracy, fairness, latency, PII leakage)? If an AI system starts making bad decisions or accessing sensitive data unexpectedly, how fast can you detect it, alert, and respond?*

**Why it matters:**  
Run Safe = operational risk mitigation. Silent model drift or security anomalies = undetected compliance failure. This tells us whether monitoring is a gap and what the alert/response SLA must be for the platform.

**Red flag:**  
"We don't monitor our AI" OR "we only check manually / with ad-hoc reports" OR "we have no data drift detection." All indicate operational blind spots and are high-risk for production AI.

**KAF Component:** **Run Safe** (monitoring, anomaly detection, observability)  
**Secondary:** HITL (alert escalation), Policy-as-Code (SLA definition)

---

### **Q9: Compliance & Regulatory Readiness (EU AI Act, GDPR, Insurance-Specific)**

**Question:**  
*Which regulatory and compliance frameworks apply to your AI today (GDPR, EU AI Act Annex III, insurance-specific rules)? What audit findings or gaps do you expect from external auditors? By Q3 2026, what governance artifacts does the board need to see (policy frameworks, audit reports, model certifications)? What would drive a board decision to say yes?*

**Why it matters:**  
This locks in the compliance acceptance criteria and board-level success definition. Tells us whether the PoV is an audit defense or a strategic enabler. Surfaces regulatory debt and board expectations.

**Red flag:**  
"We haven't done a compliance audit of our AI" OR "we don't know if we're ready for EU AI Act" OR board has no defined success criteria. All indicate governance strategy is missing, not just tooling.

**KAF Component:** **Core** (governance framework, compliance baseline)  
**Secondary:** Policy-as-Code (policy templating), HITL (audit & attestation)

---

### **Q10: MVP Scope, Budget Trade-offs & Success Metrics**

**Question:**  
*Given the €180K / 6-month constraint and on-prem deployment: what is your minimum viable governance platform (core components, not features)? What would you de-scope if budget tightens? How will you measure success—audit coverage %, policy codification %, compliance readiness %, operational maturity %, time-to-remediate? What would make you confident enough to scale this company-wide?*

**Why it matters:**  
Locks in realistic scope, budget trade-offs, and success metrics. Prevents scope creep and sets expectations for post-PoV scaling. Tells us where the real pain is (audit vs. scaling vs. compliance).

**Red flag:**  
"We want everything" (unrealistic scope) OR vague metrics ("we'll know when we see it") OR no willingness to de-scope. All indicate stakeholder alignment issues and high delivery risk.

**KAF Component:** **Core** (platform definition, success criteria)  
**Secondary:** All (integrates all components into a coherent narrative)

---

# ▶ PART 2: KAF Mapping & Cross-Cutting Insights

---

## Cross-Cutting Insights: What to Listen For

### **Governance Maturity Signals**
- ✅ Good answers: "We have a change-control process," "we track models in a registry," "we need 3-year audit retention"
- 🚩 Bad answers: "We don't have time for governance," "vendors handle it," "we review logs after incidents"

### **Budget/Scope Reality Check**
- €180K / 6 months for on-prem, EU AI Act-ready governance = focused platform, not feature-rich
- Likely includes: Policy-as-Code framework + audit logging + HITL gates + monitoring dashboard, **NOT** full model retraining or new AI capabilities

### **Red Flags Trigger Re-Scope**
- If they say "we need 10+ custom integrations," budget drops to wiring + config (core platform shrinks)
- If they say "Dec 2027 is a hard board deadline," timeline risk is high (early wins = critical)
- If they say "we have no data governance today," Ingestion work expands (data classification upfront)

### **Q4 is the Anchor**
- All other questions feed into Q4 (auditability = north star)
- If they can't articulate defensibility criteria, ask them to co-define it in the meeting → ownership

---

## Red Flags Summary (Across All 10 Questions)

| Red Flag | Severity | Implication |
|----------|----------|-------------|
| "Everything is autonomous, we don't review" | Critical | Compliance liability; HITL architecture required |
| "Policies documented, not in code" | Critical | Policy-as-Code is core, not optional |
| "Policy changes take weeks" | High | Architecture is brittle; re-design needed |
| "No audit trail / Moveworks logs everything" (unclear how) | Critical | Auditability is the entire PoV driver |
| "Moveworks is a black box" | High | Governance wrapper strategy, not integration |
| "We don't classify data" | High | GDPR/compliance baseline missing |
| "No model versioning/approval" | Critical | Model governance must be built |
| "We don't monitor AI" | High | Run Safe observability is foundational |
| "No compliance audit planned" | High | Board acceptance criteria undefined |
| "We want everything in 6 months" | Medium | Scope creep risk; clarify MVP early |

---

## Assumptions & Risks (PoV Planning)

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| Moveworks/ServiceNow APIs don't support audit logging | Medium | High | Test integrations Week 1; plan governance wrapper |
| Data classification rules not ready → delays Ingestion phase | Medium | High | Assign data governance owner in kickoff |
| No executive sponsorship for policy enforcement → adoption failure | High | High | Secure CIO buy-in + board commitment in discovery |
| EU AI Act guidelines shift mid-PoV → scope creep | Low | Medium | Lock Dec 2027 compliance baseline in Q3 2026 framework delivery |
| Budget overrun due to custom integrations | Medium | High | Define "core only" MVP in Week 2; de-scope early |

---

### KAF Component Mapping (All 10 Questions)

| Q | Component | Why | Secondary |
|---|-----------|-----|-----------|
| Q1 | HITL | Defines human checkpoints | Core, Run Safe |
| Q2 | Policy-as-Code | Code-enforceable rules | Core, Run Safe |
| Q3 | Policy-as-Code | Regulatory agility | Core |
| Q4 | HITL | Audit trail & defensibility | Policy-as-Code, Run Safe, Core |
| Q5 | Interop | Vendor lock-in, integration options | Core |
| Q6 | Ingestion | Data governance baseline | Policy-as-Code, Core |
| Q7 | Policy-as-Code | Model certification gates | Run Safe, HITL |
| Q8 | Run Safe | Observability & anomaly detection | HITL, Policy-as-Code |
| Q9 | Core | Compliance framework & board criteria | Policy-as-Code, HITL |
| Q10 | Core | MVP scope & success metrics | All |

---

# ▶ PART 3: Assumptions / Risks / Open Items

---

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|----------|
| Moveworks/ServiceNow APIs don't support audit logging | Medium | High | Test integrations Week 1; plan governance wrapper |
| Data classification rules not ready → delays Ingestion phase | Medium | High | Assign data governance owner in kickoff |
| No executive sponsorship for policy enforcement → adoption failure | High | High | Secure CIO buy-in + board commitment in discovery |
| EU AI Act guidelines shift mid-PoV → scope creep | Low | Medium | Lock Dec 2027 compliance baseline in Q3 2026 framework delivery |
| Budget overrun due to custom integrations | Medium | High | Define "core only" MVP in Week 2; de-scope early |

---

# ▶ PART 4: What We Will Measure (3 KPI proposals)

---

## 3 KPI Proposals for the €180K PoV

### **KPI #1: Audit Coverage & Traceability (Target: 80%)**
- Metric: % of AI-driven helpdesk decisions with an immutable audit trail (decision ID, user, timestamp, data inputs, model version, approval chain, outcome)
- Success: Board/CISO can pull a random ticket, trace the decision → see full lineage within 5 minutes
- Tied to: Q4 (auditability), HITL component
- Board message: *"We went from zero audit trail to full decision traceability—defensible AI."*

### **KPI #2: Governance Compliance Score (Target: 90%)**
- Metric: % of deployed models with certified model cards, change-control approvals, validated metrics (baseline, drift thresholds, SLA targets), and zero policy violation incidents
- Success: Zero unvetted model changes in prod; all policy violations trigger incident tickets & alerting within SLA
- Tied to: Q7 (model lifecycle), Policy-as-Code component
- Board message: *"Every model in production has been validated and certified—audit-ready."*

### **KPI #3: Risk Reduction & Incident Response Time (Target: 50% improvement)**
- Metric: Mean time to detect + respond to anomalous access / data exfil attempts / model drift (baseline → target: <30 minutes; escalation chain: <5 minutes)
- Success: Security team has actionable alerts; no audit findings on AI monitoring post-pilot
- Tied to: Q8 (monitoring), Run Safe component
- Board message: *"We detect and respond to AI security risks in minutes, not days."*

---

# ▶ PART 5: Agent Classification & Role Dependencies

---

## Part 5A: Agent Classification

**Governance tier:**  
Enterprise (requires board approval, multi-department handoff, compliance audit trail, regulatory alignment)

**Registry/reuse potential:**  
This discovery framework is **reusable across Kyndryl's Fortune 500 insurance clients** in EU/EMEA with similar AI governance gaps. The 10 questions are sector-agnostic enough for healthcare, financial, telecom. Post-engagement, we register the governance platform itself (not the discovery questions) as a reusable "AI Governance Accelerator" that other consulting teams can deploy to insurance/highly-regulated verticals. Package it as a Kyndryl product module.

---

## Part 5B: Dependencies on Other Roles

- **I need [Data Governance role] to ask about [data classification & retention policies]** because Eva (AI-SEC) focuses on rules enforcement & audit trails, not the actual data ownership/lifecycle management. Data Governance owns the baseline policy; AI-SEC owns the code-enforceable version.

- **I need [Infrastructure/Cloud Architect] to ask about [on-prem deployment constraints, API gateway options, data residency]** because Eva asks "what rules must be enforceable," but the infrastructure team must confirm "can we actually run this on-prem without data leaving the EU data center."

- **I need [Model Ops / MLOps role] to ask about [model registry, MLOps tooling, retraining pipelines, performance monitoring]** because Eva focuses on governance gates (who approves model changes), but MLOps owns the operational mechanics (how models are versioned, deployed, monitored).

- **I need [Integration/API Architect] to ask about [MCP connector development, Moveworks API coverage, legacy system bridging]** because Eva identifies the Interop gap (Q5) but doesn't design the connectors; Interop Architect does.

---

## Part 5C: Questions I Deliberately Did NOT Ask (and why)

- **"What is your current AI use case backlog?"** — That's for Product Management / AI Strategy role, not AI-SEC. Eva is focused on governance + compliance, not feature roadmap.

- **"How many L1 tickets do you resolve per day?"** — That's for Service Delivery / Operations role. Eva asks "what rules govern ticket resolution," not "how many tickets."

- **"Do you have a staff / budget for an AI governance team?"** — That's for Engagement Manager / Program Office. Eva's job is to surface the governance need; staffing/budget is a delivery execution question, not discovery.

- **"What LLM model do you want to use?"** — That's for AI Engineering / Model Selection role. Eva assumes "you already have models (ServiceNow/Moveworks); now make them defensible." Model choice is secondary.

- **"What is your incident response SLA?"** — That's more Security Operations / IR team's territory. Eva asks "how fast can you detect AI anomalies" (operability question) vs. "how fast can you respond to a data breach" (IR question). Related but different roles.

---

# ▶ APPENDIX: Implementation Path & CIO Meeting Flow

---

## Conversation Flow (CIO Meeting)

1. **Opening (Framing):** "You already have AI working—what you need is AI you can defend. These 10 questions unlock how we do that together."
2. **Deep Dive:** Q1 → Q4 (HITL + auditability anchor), then Q5 (integration reality), then Q2-Q3 (Policy-as-Code), then Q6-Q9 (compliance + ops)
3. **Closing:** Q10 (scope lock + success metrics) + co-define board deliverables for Q3 2026
4. **Next Step:** "Let's take your answers, map them to a 6-month roadmap, and come back with a statement of work."

---

## For the Kyndryl Proposal (Post-Discovery)

Once you have answers to all 10 Qs:
- **Week 2 kickoff:** Confirm data governance owner, secure board commitment, finalize Dec 2027 compliance baseline
- **Phase 1 (Weeks 1–8):** Policy-as-Code framework + Ingestion baseline → first governance rules codified
- **Phase 2 (Weeks 9–16):** HITL gates + Run Safe monitoring → live in ServiceNow test environment
- **Phase 3 (Weeks 17–26):** Full audit trail + board-ready certifications + scale roadmap → board presentation Q3 2026
- **Post-PoV:** Company-wide rollout plan (product licensing, ops handoff, compliance automation)



**Document Version:** 1.0 Discovery Pack (AI-SEC role)  
**Prepared by:** Eva Černochová, Kyndryl AI Consulting  
**Date:** February 23, 2026
