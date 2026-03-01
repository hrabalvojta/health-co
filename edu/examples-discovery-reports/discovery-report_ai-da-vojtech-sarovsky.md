# Discovery Report — AI-DA  
## Metrics Baseline & Monitoring Schema  
Client: EuroHealth Insurance AG  
Role: AI Data Analyst (AI-DA)  
Date: 2026-02-24  

---

# 1. Executive Framing (AI-DA Perspective)

This engagement is not a chatbot deployment.  
It is a measurable operational transformation under three board-visible objectives:

1. 30% reduction in remaining helpdesk costs (within 6 months)  
2. Unification of fragmented AI systems under governed monitoring  
3. EU AI Act–ready, audit-capable AI platform before August 2026  

From an AI-DA standpoint, success depends on establishing:

- A defensible **baseline**
- A unified **metric taxonomy**
- An on-prem compliant **monitoring architecture**
- A board-ready **monthly reporting layer**
- A drift detection + quality assurance mechanism

If it cannot be measured, it cannot be defended at board level.

---

# 2. Current Helpdesk KPI Baseline (Pre-AI Expansion)

## 2.1 Existing Operational KPIs

Current measurable indicators (to validate via ServiceNow extraction):

- **MTTR (Mean Time To Resolution)**
- **CSAT: 3.2 (target 3.6)**
- **First Contact Resolution Rate (FCR)**
- Ticket volume per month
- L1 vs L2 vs L3 distribution
- Reopen rate
- Escalation rate
- Cost per ticket (to be defined with Finance)

## 2.2 Immediate Baseline Actions (Week 1)

1. Extract last 8–12 weeks of ticket data from ServiceNow.
2. Validate:
   - True automation rate (currently claimed 35%)
   - Actual L1 volume remaining
   - Real MTTR distribution (median, not average only)
3. Define financial baseline:
   - What counts toward the “30% reduction”?
     - Headcount cost?
     - Vendor cost?
     - Ticket handling cost?

**Risk:** If baseline definition is weak, 30% becomes politically disputable.

---

# 3. Proposed AI KPI Framework (Post-Deployment)

## 3.1 Core AI Performance KPIs

### 1. Auto-Resolve Rate
% of tickets fully resolved by AI without human intervention.

### 2. Escalation Accuracy
% of AI-escalated tickets that required escalation (not false positives).

### 3. Human Override Rate
% of AI decisions manually overridden by agents.

### 4. Reopen Rate (AI vs Human comparison)
AI-resolved reopen rate must not exceed human baseline.

### 5. User Trust Score
Composite metric including:
- End-user CSAT (AI-resolved vs human-resolved)
- Agent override frequency
- Feedback signals (thumbs up/down, if implemented)

## 3.2 Financial Impact Model

Cost reduction must be derived from:

Cost per ticket × Reduction in human-handled L1 volume  
+ Avoided escalation cost  
– Infrastructure + maintenance overhead

This model must be approved by AI-PM + Finance.

---

# 4. Dashboard Requirements (Board vs Operational Views)

## 4.1 Monthly Board Dashboard (Hans-Facing)

Maximum 5 KPIs:

1. Automation Rate (trend line)
2. Cost Reduction YTD vs Target
3. CSAT Trend (AI vs baseline)
4. Compliance Readiness Status (RAG indicator)
5. Shadow AI Decommissioning Progress

Exportable PDF, monthly cadence.

## 4.2 Operational Dashboard (IT + AI Team)

- Real-time automation %
- Escalation distribution
- Reopen rate heatmap
- Override trend
- Knowledge usage frequency
- Policy triggers activated

Separation of executive and operational dashboards is mandatory.

---

# 5. Data Pipeline Architecture (On-Prem Constraint)

Cloud tools are not allowed.

## 5.1 Data Sources

- ServiceNow ticket lifecycle events
- Moveworks logs
- Shadow AI systems (HR, Claims)
- AI agent telemetry (model version, prompt ID, retrieval source, override flag)

## 5.2 Required Architecture Components

- On-prem event ingestion layer
- Centralized log storage (immutable)
- Metric aggregation service
- Self-hosted dashboard solution
- Role-based access control

## 5.3 Critical Design Rule

Telemetry must be captured at decision time.  
Audit logs cannot be reconstructed retroactively.

---

# 6. Drift Detection & Knowledge Base Monitoring

The knowledge base is ~30% outdated.

## 6.1 Drift Indicators

- Increase in reopen rate for AI-resolved tickets
- Drop in CSAT for AI cases
- Increase in override rate
- Increased retrieval from low-confidence documents
- Knowledge article age distribution shifts

## 6.2 Knowledge Health Index (New KPI)

Composite score including:

- Freshness
- Usage frequency
- Contradiction signals
- Last review timestamp

Without KB ownership, AI performance metrics will become unstable.

---

# 7. A/B Testing Design (AI vs Human Quality)

## 7.1 Experimental Structure

Group A: Human-handled L1 tickets  
Group B: AI-handled L1 tickets  

Compare:

- MTTR
- CSAT
- Reopen rate
- Escalation downstream cost
- Agent workload distribution

## 7.2 Statistical Requirements

- Minimum sample size defined with AI-DS
- Control for ticket category
- Weekly comparison reporting
- Stop conditions if quality degrades

This prevents “AI looks good in demo but fails in production.”

---

# 8. Key Risks (AI-DA Specific)

1. Baseline ambiguity → political KPI conflict  
2. Telemetry underinvestment → compliance failure  
3. On-prem observability complexity → hidden cost  
4. Knowledge staleness → artificial performance decay  
5. Metric gaming by fearful agents  

---

# 9. First 2 Weeks — AI-DA Deliverables

Week 1:
- KPI glossary v1
- Baseline extraction
- Financial definition workshop
- Telemetry field specification

Week 2:
- AI inventory + metric taxonomy
- Board dashboard mockup
- Drift detection framework draft
- A/B test design document

---

# 10. Cross-Role Dependencies

- AI-PM → Confirm financial baseline definition and success hierarchy
- FDE → Confirm which tickets are technically eligible for auto-resolution
- AI-SEC → Define mandatory audit fields and compliance evidence requirements
- AI-DS → Define evaluation methodology and sample sizing
- IT Ops → Confirm ServiceNow API feasibility and data model access
- OCM → Align adoption metrics with change strategy

---

# Final Statement (AI-DA Position)

The agent is successful only if it delivers durable cost savings  
without degrading service quality,  
while producing audit-ready, board-defensible evidence  
under strict on-prem constraints.

Anything less is a pilot, not a platform.
