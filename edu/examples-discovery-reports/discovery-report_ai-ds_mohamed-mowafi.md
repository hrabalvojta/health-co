# EuroHealth Insurance AG
# AI Discovery Report – AI Data Scientist Perspective 
# Mohamed Mowafi

---

# 1. Executive Summary

EuroHealth’s CIO, Hans Muller, was very clear about what he needs from this initiative. His goals are straightforward:

1. **Cut the remaining helpdesk costs by 30%**
2. **Bring all scattered AI efforts under one governed platform**
3. **Be fully aligned with the EU AI Act by August 2026**

But underneath these goals, the discovery session surfaced some realities we can’t ignore:

- We cannot use cloud in this phase. This can be brough later after we pass phase 1 and gain the client trust.
- About 30% of the knowledge base is outdated, and no one feels responsible for fixing it.
- HR and Claims have their own AI experiments running in silos.
- Jan’s helpdesk team is worried the AI will replace them.
- Timeline and budget for phase 1 (6 months / €180K) are very tight.
- Basic tickets are already handled by Moveworks/ServiceNow.

From an AI-DS point of view, the big takeaway is this: **the hardest problems here are human and structural, not technical**.  
If we don’t tackle data quality, ownership, and adoption early, even the best-performing model won’t deliver the promised savings.

---

# 2. Stakeholder Analysis (AI-DS Lens)

## 2.1 Executive Sponsor – CIO (Hans Muller)

**What he cares about**
- A single platform instead of department-level experiments
- Numbers he can confidently take to the board. He is clearly under a pressure that he might lose his job if we cannot help him to reduce cost
- A solution that won’t get them in trouble with auditors

**What this means for AI-DS**
- We need success metrics that are defensible, not just “the model seems good”
- Every evaluation must stand up to compliance rules
- Business impact needs to be quantified, not assumed  
 - This includes showing where AI *shouldn’t* be used—because avoiding risk is also value.

---

## 2.2 Helpdesk Lead (Jan) + 12 Agents

**Current feeling**
- Nervous. Worried. Bracing for headcount cuts.

**Why it matters**
- Their behavior during evaluation can influence results more than the model itself.
- If they escalate too often “just to be safe,” the AI will look less effective than it really is.


**How to work with them**
- Frame AI as support, not replacement  
- Pull them into dataset creation so they feel ownership  
- Track override and escalation reasons to understand where friction really is
- We can try to bring OCM team at early discussion cycles if the budget allows it.

---

## 2.3 HR & Claims (Shadow AI Owners)

**What’s happening**
- HR runs an ungoverned chatbot
- Claims built a LangChain prototype that could be risky if used in place of human decision makers

**Why it matters**
- These parallel tools are symptoms of deeper fragmentation
- They introduce compliance questions we will need to address (sooner better than later)

**AI-DS need**
- Consistent data + evaluation standards across departments, otherwise, we struggle to validate three different worlds instead of one.

---

## 2.4 Compliance & Legal

They will be essential partners for:

- EU AI Act classification
- Traceability and auditability requirements
- Human-in-the-loop policies


---

## 2.5 Missing Stakeholder: Knowledge Owner

Right now, the knowledge base effectively belongs to no one.

This affects:
- Accuracy of answers
- Reliability of retrieval
- Ability to defend the system to auditors
- No clear responsibiliy nor accountabillity

- We need to clarify and set crisp clear rules for responsibiliy and accountabillity

---

# 3. Key Findings & Implications for AI Workstream

## Finding 1: Existing AI Already Solves “Easy Wins”

Moveworks/ServiceNow handle the straightforward tickets.  
What’s left are:
- Odd edge cases  
- Policy decisions  
- Multi-step flows  
- Tickets that will require human intervension 

**Implication:** The ROI threshold is higher than typical helpdesk automation.  
We need to identify *repeatable patterns* inside the complexity.

---

## Finding 2: KB ~30% Outdated, No Ownership

If we skip cleanup:
- The model will hallucinate more often  
- Agents may receive wrong policy guidance  
- We’ll blame the model for what is actually a content problem, especially by Help Desk team as they are feeling a thread of losing their jobs

---

## Finding 3: On-Prem Only

This means:
- Limited model size  
- Bigger hardware costs  
- Slower iteration cycles  
- Careful benchmarking before any commitments

- We need to revisit that decision after the project deployment and success. Hans could then be more flexible after we gain his trust
---

## Finding 4: Budget & Timeline Constraints

With €180K over 6 months, we need:
- Clear evaluation gates  
- Quick validation of feasibility  

- We should focus on success metrices and mandatory requirements not on the optional or nice to have features

---

# 4. Knowledge Base Audit Methodology (2,000 Pages)

## 4.1 Sampling Strategy

To understand the real state of the KB:
- Review ~200 pages (10%)
- Sample across:
  - Departments
  - Usage frequency
  - Last update time
  - Language (EN/DE/CZ), This can be a critical point if we neglect it. Bad translation between languages can raise issues and the company will use the same KB accross countries

---

## 4.2 Data Quality Scoring

Each page must be scored on level 1–5 on:
- **Freshness**
- **Accuracy**
- **Completeness**

Composite score determines:
- 4.0+ → good for RAG
- 3.0–3.9 → needs updates
- <3.0 → exclude from retrieval

---

# 5. Golden Dataset Design for RAG Evaluation

## 5.1 Structure

Per category:
- 20+ Q&A pairs  
- Across all three languages  
- Include tricky and ambiguous queries  
- Add “out-of-scope” traps to test guardrails

(~100 Q&A pairs minimum)

---

## 5.2 Annotation Requirements

Each pair includes:
- Ground-truth answer  
- Source link / doc ID  
- Allowed vs disallowed responses  
- Risk level (low/medium/high)  
- This helps us detect “silent failures” that may look accurate but can create compliance risk.

---

# 6. Baseline Metrics vs AI Target

## 6.1 What We Need from ServiceNow

- Ticket categories & volume  
- Current accuracy  
- First-contact resolution rate  
- Escalation patterns  
- Cost per ticket  
- Language distribution
- CSAT NLP score accross departments and countries

---

## 6.2 Proposed AI Targets

| Metric | Current | Target |
|--------|---------|--------|
| Containment Rate | Current% | +20% |
| Critical Error Rate | Unknown | <2% |
| Language parity gap | Unknown | <5% |
| CSAT NLP  | Unknown | 65

Savings model:

**Savings = Deflected Tickets × Cost per Ticket  
− Verification Overhead − Rework Costs**

---

# 7. LLM Selection Criteria (On-Prem)

Candidates:
- Llama 3 70B  
- Mistral Large  
- Smaller 7B–13B models

**How we'll judge them**
1. Accuracy on golden dataset  
2. Latency under on-prem constraints  
3. Memory footprint  
4. Multilingual strength  
5. Fine-tuning options  
6. Licensing + compliance
7. CSAT NLP accross departments and countries

---

# 8. Evaluation Framework

## 8.1 Automated (RAGAS)

We measure:
- Retrieval precision/recall  
- Faithfulness  
- Relevance

This helps separate “bad retrieval” from “bad generation.”

---

## 8.2 Human Evaluation

Panel:
- 2 SMEs  
- 1 Compliance reviewer  

Scores 1–5:
- Correctness  
- Compliance  
- Actionability  
- Clarity 
- Time saved 

Critical errors flagged when:
- Policy advice is wrong  
- Output is unsafe  
- Content is invented

---

## 8.3 Production Monitoring

- Track escalation reasons, especially the ones raised by Jan's team  
- Log overrides  
- Monitor drift  
- Break down performance by language

---

# 9. Risks Specific to AI-DS

## 9.1 Content Risk  
Outdated KB → wrong answers.

## 9.2 Adoption Risk  
Agent fear → skewed evaluation.

## 9.3 Compliance Risk  
Shadow AI patterns contaminate production.

## 9.4 Multilingual Risk  
DE strong / CZ weak → inconsistent user experience.

## 9.5 On-Prem Risk  
Latency too high → nobody uses it.

---

# 10. Recommended Next Steps (First 2 Weeks)

## Week 1
1. Pull baseline ServiceNow metrics 
2- Define RACI Matrix 
3. Run KB sample audit  
4. Define what AI can and cannot decide  
5. Draft success metrics  
6. Confirm hardware boundaries

## Week 2
6. Build golden dataset  
7. Run model bake-off  
8. Execute RAGAS evaluation  
9. Conduct SME scoring  
10. Present results + ROI model

---

# 11. Dependencies on Other Roles

| Role | Dependency |
|------|------------|
| Solution Architect | On-prem infra feasibility |
| Compliance Lead | EU AI Act classification |
| PM | Scope and budget alignment |
| Change Lead | Adoption strategy |
| Data Engineer | Ticket data pipeline |
| Content Owner (TBD) | KB governance |

---

# 12. Critical Insight

The model is not the make-or-break factor here.

What will decide success is:

- How reliable and current the content is  
- Whether the success metrics are realistic and aligned  
- How well human oversight is designed  
- How effectively we manage expectations and adoption  
- How early we confront the constraints, not work around them  

**Without this foundation, even a high-performing model will fail once it meets the real world.**

