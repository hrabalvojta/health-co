# discovery-report-ai-ds-Francisco-Ramon.md

## Client: EuroHealth Insurance AG  
## Sponsor: Hans Müller, CIO  
## Workstream: AI Data Science  
## Date: [Insert Date]

---

# 1. Executive Summary

EuroHealth’s CIO mandate is clear: move from fragmented AI experiments to a unified, governed, on-prem platform that delivers measurable helpdesk cost reduction (30% within 6 months) and demonstrable EU AI Act readiness before August 2026.

From an AI Data Science perspective, the primary risk is not model capability — it is uncontrolled data quality, lack of evaluation standards, and absence of measurable performance baselines. With approximately 30% of the knowledge base described as “garbage” and no ownership model in place, scaling AI without first establishing a rigorous evaluation and data-quality framework would systematically amplify errors, undermine auditability, and jeopardize ROI.

The immediate priority is to establish a measurable, audit-ready performance spine that links data quality, grounded AI behavior, multilingual robustness (EN/DE/CZ), and operational metrics directly to cost reduction outcomes.

---

# 2. Current State Assessment (Based on CIO Feedback)

## 2.1 Strategic Context

- Fragmented AI landscape (Moveworks, ServiceNow AI, HR chatbot, Claims LangChain prototype)
- No unified governance model
- On-prem only (non-negotiable)
- Political pressure and board visibility
- Hard deadline: EU AI Act readiness by August 2026
- Budget constraint: €180K over 6 months

## 2.2 Operational Issues Identified

- ~30% of knowledge base outdated and unmanaged
- No clear ownership of knowledge quality
- Helpdesk team concerned about automation impact
- Shadow AI development outside governance structure
- No defined evaluation metrics for AI performance or ROI

---

# 3. Key Discovery Insights (AI Data Science Lens)

## Insight 1: Cost Reduction Target Lacks Baseline Definition

The 30% cost reduction goal is not currently tied to measurable operational baselines (deflection rate, AHT, escalation rate, cost per ticket). Without baseline metrics, success cannot be objectively validated.

**Implication:** Immediate need to establish operational baselines before scaling AI.

---

## Insight 2: Data Quality is the Primary Risk Multiplier

With one-third of the knowledge base outdated, AI systems will:

- Amplify incorrect content
- Increase escalation rates
- Reduce user trust
- Create audit inconsistencies

No model architecture can compensate for systematically poor source data.

**Implication:** Data quality control must precede automation expansion.

---

## Insight 3: Governance and Auditability Are Board-Level Requirements

Hans explicitly requires:

- Unified AI control
- Full audit traceability
- Grounded answers from a defined “Golden Source”
- Compliance-readiness demonstration

This translates technically into:

- Traceable retrieval pipelines
- Logged prompt–response–source chains
- Confidence scoring with escalation logic
- Multilingual evaluation validation

---

## Insight 4: Remaining Helpdesk Tickets Are Likely Higher Complexity

Basic tickets are already automated via Moveworks/ServiceNow AI.

The remaining workload is likely:
- More complex
- Lower frequency
- Less structured
- Higher business risk

**Implication:** 30% cost reduction may depend more on AHT reduction and assistive AI than full deflection.

---

# 4. Success Criteria (AI Data Science Workstream)

Success will be defined by the ability to prove, with measurable and auditable evidence, that AI:

1. Improves cost efficiency (deflection and/or AHT reduction)
2. Maintains high-confidence grounded responses
3. Operates reliably under on-prem constraints
4. Demonstrates multilingual consistency (EN/DE/CZ)
5. Produces audit-ready logs aligned with compliance expectations

Success is not “AI deployed.”  
Success is “AI performance proven and defensible.”

---

# 5. Required Core Data Inputs (Unified AI Baseline)

To establish feasibility and measurable performance, the following data inputs are required:

## 5.1 Operational Data
- 12–24 months of helpdesk tickets
- Resolution outcomes
- Escalation paths
- Agent handling time
- Ticket categorization schema

## 5.2 Financial Data
- Cost per L1 ticket
- Cost per L2 escalation
- Agent hourly cost
- Current deflection rate

## 5.3 Knowledge Base Data
- Article inventory
- Last update timestamps
- Ownership metadata
- Usage frequency
- Duplicate/conflict detection

## 5.4 System Telemetry
- Current AI system logs
- Query patterns
- Escalation triggers

---

# 6. Metrics Framework (To Declare Success or Failure)

## 6.1 Business Metrics

- Deflection Rate (% automated resolution)
- Average Handling Time (AHT)
- Escalation Rate
- Cost per Ticket
- Net Cost Reduction %

## 6.2 Model Performance Metrics

- Retrieval Precision@k
- Groundedness Score
- Hallucination Rate
- Confidence Calibration Accuracy
- Multilingual Performance Parity
- Latency under on-prem constraints

## 6.3 Data Quality Metrics

- % KB articles with assigned owner
- Freshness Index
- Coverage of Top 50 Intents
- Duplicate/Contradiction Rate
- High-volume article quality score

---

# 7. Risks Identified

## 7.1 Scaling on Uncontrolled Data
High probability of performance degradation and audit exposure.

## 7.2 Unrealistic “Zero Hallucination” Expectation
Technically unachievable. Must implement confidence thresholds and human-in-loop fallback instead.

## 7.3 On-Prem Infrastructure Constraints
Limited compute may restrict model size and experimentation velocity.

## 7.4 Political Pressure vs Technical Reality
Board-level deadlines may incentivize premature scaling before performance validation.

## 7.5 Misaligned Cost Target
If remaining tickets are too complex, 30% reduction may require hybrid assistive strategy rather than pure automation.

---

# 8. Recommended Immediate Next Steps (First 2 Weeks)

## Week 1: Establish Baseline & Evaluation Spine

- Extract and profile 12 months of ticket data
- Define operational baseline metrics
- Create gold-standard evaluation dataset (200–500 tickets)
- Perform knowledge base quality sampling
- Quantify impact of outdated articles on top-volume intents

Deliverable: Baseline & Feasibility Assessment Report

---

## Week 2: Controlled Performance Validation

- Build offline RAG evaluation harness
- Measure groundedness and retrieval precision
- Calibrate confidence thresholds for automation vs escalation
- Model cost impact scenarios (deflection vs AHT reduction)

Deliverable: Cost-Impact & Risk Feasibility Model

---

# 9. Dependencies

- Knowledge Management Lead (KB ownership model)
- Platform Architect (on-prem LLM + vector DB infrastructure)
- Governance Lead (audit log requirements)
- Security (data masking, logging retention policies)
- Change Management (agent feedback loop)

---

# 10. Conclusion

EuroHealth’s challenge is not primarily model capability — it is system discipline.

To meet the 30% cost reduction target and demonstrate compliance readiness before the board deadline, AI must be measurable, grounded, auditable, and data-quality controlled before scaling.

The AI Data Science workstream will focus on transforming chaotic, unmanaged data into a controlled performance framework that links AI outputs directly to measurable business and compliance outcomes.

Only once that measurable spine is established can AI expansion be justified and defensible.

---