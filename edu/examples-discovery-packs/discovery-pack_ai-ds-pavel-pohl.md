# Discovery Packet v1 — AI-DS (Data Scientist)
## Student: Pavel Pohl
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: Risk-Tiered Error Thresholds
**Question:**  
For each AI-driven decision you plan to delegate (e.g., ticket resolution, routing, policy interpretation), what is the maximum acceptable error rate — and how is that threshold linked to risk classification?

**Why this matters:**  
Delegating AI authority without quantified error tolerance creates uncontrolled enterprise risk. Industrialization requires mapping risk tiers to measurable performance thresholds.

**Red flag:**  
No defined error tolerance per decision type; one global accuracy metric.

**KAF component:** Core / Human-in-the-Loop

---

### Question 2: Statistical Confidence in Reported Performance
**Question:**  
When reporting AI performance (e.g., 95% accuracy or 4.2 CSAT), what statistical confidence interval and sample size support those claims?

**Why this matters:**  
Board-level governance requires statistically defensible metrics, not point estimates without rigor.

**Red flag:**  
Percentages reported without methodology, confidence intervals, or sampling transparency.

**KAF component:** Run Safe

---

### Question 3: Golden Evaluation Dataset (No-PII Compliant)
**Question:**  
Do you maintain an anonymized, versioned “golden dataset” for AI evaluation that fully complies with the “no PII in training data” constraint?

**Why this matters:**  
Evaluation without controlled datasets risks GDPR violations and non-reproducible results.

**Red flag:**  
Using historical tickets containing unverified PII as evaluation baseline.

**KAF component:** Ingestion / Policy-as-Code

---

### Question 4: Model Confidence Calibration
**Question:**  
Is the model’s confidence score calibrated against real-world accuracy, or does it reflect only internal probability outputs?

**Why this matters:**  
Displaying uncalibrated confidence undermines Digital Trust and can mislead users and auditors.

**Red flag:**  
Confidence is exposed in UI but never empirically validated.

**KAF component:** Core / Run Safe

---

### Question 5: Multilingual Semantic Consistency
**Question:**  
How do you measure semantic consistency of AI responses across EN/DE/CZ, beyond surface-level translation checks?

**Why this matters:**  
Regulatory interpretation drift across languages is a hidden enterprise risk.

**Red flag:**  
Reliance on machine translation without semantic alignment evaluation.

**KAF component:** Core / Run Safe

---

### Question 6: Stale Knowledge Risk Detection
**Question:**  
How do you detect and quantify the probability that an AI answer was generated from outdated policy or knowledge base content?

**Why this matters:**  
Outdated regulatory guidance is a primary AI compliance risk.

**Red flag:**  
No document version tracking tied to AI outputs.

**KAF component:** Ingestion / Run Safe

---

### Question 7: Distribution Shift When Scaling Beyond IT
**Question:**  
How does model performance change when scaling from IT helpdesk use cases to HR, Claims, and Finance domains?

**Why this matters:**  
Performance often degrades under domain shift; assuming transferability is unsafe.

**Red flag:**  
Assumption that one evaluation baseline applies to all departments.

**KAF component:** Core

---

### Question 8: Human Override as a Risk Signal
**Question:**  
How is human override behavior analyzed quantitatively, and is it used as a leading indicator of model risk?

**Why this matters:**  
Override frequency is a powerful signal of hidden reliability issues.

**Red flag:**  
Overrides logged but not incorporated into evaluation metrics.

**KAF component:** Human-in-the-Loop / Core

---

### Question 9: Regression Testing After Policy Changes
**Question:**  
After regulatory or policy updates, how do you ensure no unintended performance degradation occurs in other AI workflows?

**Why this matters:**  
Industrialization requires regression evaluation to prevent silent failures.

**Red flag:**  
Policy updates deployed without cross-use-case regression testing.

**KAF component:** Run Safe / Core

---

### Question 10: Audit Reproducibility Sampling
**Question:**  
If we randomly sample 100 AI decisions from the past 6 months, what percentage would pass full reproducibility validation (model version, data lineage, prompt, policy state) without manual reconstruction?

**Why this matters:**  
Governance maturity is proven by reproducible evidence, not theoretical capability.

**Red flag:**  
Evidence exists only for selected cases, not random samples.

**KAF component:** Run Safe

---

## Part 2: KAF Mapping (Mini)

| KAF Component        | Covered by Q# |
|----------------------|--------------|
| Agentic Core         | 1, 4, 5, 7, 8 |
| Agentic Ingestion    | 3, 6         |
| Policy-as-Code       | 3            |
| Digital Trust (Run Safe) | 2, 4, 6, 9, 10 |
| Human-in-the-Loop    | 1, 8         |
| Interoperability     | — (covered by other roles) |

---

## Part 3: Assumptions / Risks / Open Items

1. Evaluation methodology may not yet be statistically formalized.
2. Shadow AI tools may contaminate evaluation datasets.
3. Multilingual drift risk likely unmeasured.
4. Governance may exist at process level but not be quantifiable in model behavior.
5. Confidence metrics may not be calibrated or validated.

---

## Part 4: What We Will Measure (3 KPI Proposals)

1. Risk-tiered decision accuracy ≥ defined threshold with ≥95% statistical confidence  
2. % AI decisions with full reproducible audit evidence ≥ 100%  
3. Regulatory update performance degradation ≤ 2% across non-affected workflows  

---

## Part 5: Agent Classification

- **Governance tier:** Enterprise Agent  
- **Registry/reuse potential:**  
  Must be registered in centralized AI registry with model-level evaluation tracking and cross-department performance monitoring.

---

## Dependencies on Other Roles:

- AI-FDE: Policy enforcement architecture definition  
- AI-SE: CI/CD regression evaluation gates  
- AI-SEC: Audit retention requirements  
- AI-DA: Board-level reporting structure  

---

## Questions I Deliberately Did NOT Ask (and why):

- Enforcement location of policies (covered by AI-FDE)  
- CI/CD architecture details (covered by AI-SE)  
- Business ROI framing (covered by AI-PM)  
- UI trust indicators (covered by AI-FE)  