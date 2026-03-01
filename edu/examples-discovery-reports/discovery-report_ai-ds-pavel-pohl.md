# Observation Report  
## AI Data Scientist Perspective  
### EuroHealth Insurance AG – Discovery Phase  

Author: Pavel Pohl  
Date: 24/02/2026  
Status: Observational Assessment 

---

# 1. Executive Observation

The stated objective of the initiative is a **30% cost reduction in helpdesk operations within 6 months**.

However, based on the CIO discussion and contextual signals, this initiative appears to be about more than operational efficiency.

Key observation:

> The project is simultaneously a financial target, a governance stabilization effort, and a regulatory risk mitigation initiative.

The 30% saving is the KPI.  
AI control and regulatory safety are the strategic drivers.

Additional structural signals:

- Shadow AI already exists across departments.
- Knowledge governance is weak.
- Adoption risk is real.
- Timeline and budget are tight (€180K / 6 months).
- Basic tickets are already partially handled by Moveworks.

This is not a chatbot experiment.  
It is a board-visible leadership test.

---

# 2. Explicit Statements vs. Implied Signals

## 2.1 "Cut helpdesk costs by 30%."

Explicit:
- Board-level measurable KPI.
- Fixed timeline.

Implied:
- Formal commitment likely communicated upward.
- Limited tolerance for partial success.
- Financial defensibility required.

Observation:
Financial feasibility must be validated before architectural commitments.

---

## 2.2 "Bring all AI under one platform."

Explicit:
- Unification of Moveworks, HR chatbot, Claims LangChain.

Implied:
- AI initiatives are fragmented.
- IT governance is currently weak.
- Power asymmetry between departments may exist.
- Loss of centralized control.

Observation:
The core issue is lack of centralized AI governance.

---

## 2.3 "Compliance-ready platform before August 2026."

Explicit:
- EU AI Act readiness required.

Implied:
- Regulatory risk is board-visible.
- Compliance is politically sensitive.
- Audit defensibility is mandatory.
- Incident tolerance is extremely low.

Observation:
Traceability and logging are non-negotiable design constraints.

---

## 2.4 "Jan is nervous."

Explicit:
- Helpdesk team fears replacement.

Implied:
- Adoption risk.
- Defensive escalation behavior.
- Evaluation distortion risk.

Observation:
Containment metrics must be analyzed alongside override patterns.

---

## 2.5 "Absolutely not. No cloud."

Explicit:
- On-prem constraint.

Implied:
- Strong compliance posture.
- Possible CISO dominance.
- Political sensitivity around vendor exposure.

Observation:
On-prem performance must be validated early to protect ROI feasibility.

---

# 3. Stakeholder Observations

## 3.1 CIO (Executive Sponsor)

Concerns:
- Board-facing credibility.
- Clear measurable ROI.
- Regulatory defensibility.
- Leadership stability.

Observation:
Metrics must be defensible under board scrutiny.

---

## 3.2 Helpdesk Lead (Jan) & Team

Risks:
- Escalation bias.
- Passive resistance.
- Evaluation contamination.

Mitigation Observations:
- Clear AI decision boundaries.
- Transparent confidence thresholds.
- Escalation reason logging.

---

## 3.3 HR & Claims (Shadow AI Owners)

Parallel AI systems introduce:
- Governance fragmentation.
- Compliance inconsistency.
- Evaluation divergence.

Observation:
Unified evaluation and logging standard required.

---

## 3.4 Missing Stakeholder: Knowledge Owner

Currently undefined.

Observation:
Without ownership, KB remediation cannot be sustained.

---

# 4. Data Observations

## 4.1 Knowledge Base Quality

- ~2,000 pages.
- ~30% outdated.
- No clear ownership.

Risk:
Hallucination driven by stale content.

Required:
Mandatory KB audit before RAG scale.

---

## 4.2 Historical Ticket Volume

- 270,000 tickets (18 months).

Unknown:
- L1 share.
- Repeatability ratio.
- Misrouting rate.
- Language distribution.
- Average handling time.

Observation:
30% feasibility depends entirely on L1 distribution and automation ceiling.

---

# 5. Explicit Feasibility Risk Section

## 5.1 Mathematical Automation Threshold

If L1 workload = 60%:

0.60 × Automation Rate ≥ 0.30  
Automation Rate ≥ 50%

Minimum safe automation ≥50% of L1 tickets required.

If L1 share <55%, 30% becomes mathematically improbable without scope expansion.

---

## 5.2 Ceiling Risk

Moveworks already handles basic tickets.

Remaining L1 likely includes:
- Edge cases.
- Policy-dependent flows.
- Multi-step workflows.

Observation:
Automation ceiling may be materially lower than assumed.

---

## 5.3 Cost Realization Risk

Workload reduction ≠ cost reduction.

Potential constraints:
- Fixed salary contracts.
- Low attrition.
- Limited workforce elasticity.
- Outsourcing agreements.

Observation:
Savings realization pathway must be defined explicitly.

---

## 5.4 Adoption Bias Risk

If helpdesk escalates defensively:
- Containment drops.
- ROI degrades.
- Board perception shifts.

Override metrics must be monitored.

---

## 5.5 On-Prem Infrastructure Risk

On-prem constraint introduces:
- Model size limits.
- Latency risk.
- GPU capacity uncertainty.

Performance validation must precede scaling commitments.

---

## 5.6 Multilingual Risk

EuroHealth operates in EN / DE / CZ.

Risk:
Uneven model performance across languages.

Observation:
Parity gap >5% may fragment ROI and adoption.

---

# 6. Knowledge Audit Methodology

Sampling:
- 200-page stratified sample.
- Cross-department.
- Cross-language.
- Usage-frequency weighted.

Scoring dimensions:
- Freshness.
- Accuracy.
- Completeness.
- Policy alignment.

Threshold:
<3 excluded from retrieval.

---

# 7. Golden Dataset Design

Minimum:
- 100+ Q&A pairs.
- ≥20 per major category.
- Multilingual variants.
- Ambiguous and edge cases.
- Out-of-scope traps.

Each pair:
- Ground truth.
- Source reference.
- Risk classification.
- Allowed/disallowed patterns.

Purpose:
Detect silent compliance failures.

---

# 8. Evaluation Framework

## 8.1 Automated Evaluation

- Retrieval precision/recall.
- Faithfulness.
- Relevance.

## 8.2 Human Evaluation

Panel:
- 2 SMEs.
- 1 Compliance reviewer.

Scoring:
- Correctness.
- Compliance.
- Actionability.
- Clarity.
- Time saved.

Critical errors flagged immediately.

---

## 8.3 Production Monitoring

- Escalation reason tracking.
- Override logging.
- Drift detection.
- Language performance breakdown.

---

# 9. Financial Realization Observation

Baseline assumption:
- 12 FTE.
- Approx. 540,000€ annual cost.

30% target:
162,000€ annually.

Critical validation required:
- What portion is variable?
- What portion is fixed?
- Is attrition available?
- Is workload reduction convertible to financial reduction?

Without realization model, 30% remains theoretical.

---

# 10. Validation Gates (Milestone Framing)

Week 2:
- Confirm L1 share.
- Confirm automation ceiling.
- Confirm infra feasibility.

Week 6:
- Achieve ≥15–20% containment (validated).

Week 12:
- Achieve ≥25–30% containment (validated).

If ceiling <30%:
Scope expansion required (routing, misclassification correction, productivity gains).

---

# 11. Critical Open Questions

1. What is the true L1 workload share?
2. How much L1 is already automated by Moveworks?
3. What portion of helpdesk cost is variable vs fixed?
4. Has there been prior AI-related incident?
5. Is cloud prohibition regulatory or political?
6. What is the real language distribution?
7. Is 30% a board directive or CIO proposal?
7a. Internal consideration: How stable is the CIO’s position?

These must be validated before scaling commitments.

---

# 12. Summary of Core Observations

- 30% saving is mandatory.
- Governance is structural.
- Compliance readiness is board-visible.
- Data quality is insufficient without remediation.
- Adoption risk is significant.
- On-prem constraint threatens performance ceiling.
- Financial realization risk is non-trivial.
- Multilingual parity may affect ROI stability.
- Automation ceiling must be validated mathematically before scaling.

Final Observation:

> This initiative is not a chatbot optimization project.  
> It is a governance stabilization and board-level legitimacy project with a financial KPI attached.
