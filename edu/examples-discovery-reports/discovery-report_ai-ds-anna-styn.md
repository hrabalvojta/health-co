# Day 12 — AI-DS Discovery Report  
## What Hans Didn’t Say — But Needs to Hear  
**Role:** AI Data Scientist (AI-DS)  
**Client:** EuroHealth Insurance AG  
**Context:** Post‑Roleplay Analysis (Day 12)

---

# 1️⃣ Executive Interpretation — What This Project Is REALLY About

Hans explicitly asked for:

- 30% cost reduction in 6 months  
- EU AI Act readiness before August 2026  
- On‑prem deployment  
- Unification of AI tools  

If our discovery report only repeats these statements, we fail Day 12.

Because what Hans *actually revealed* is this:

> AI already exists — but it is fragmented, unmeasured, ungoverned, and politically risky.

From AI‑DS perspective, this is not a chatbot optimization problem.  
It is a **measurement, traceability, and data foundation problem.**

The most important message Hans needs to hear is:

> We must prove AI quality, safety, and compliance with measurable, auditable evidence before scaling automation — otherwise cost reduction and compliance will fail together.

---

# 2️⃣ The Rule That Separates You From Everyone Else

Most teams ask:

> “What can the AI do?”

AI‑DS must ask:

> “How will we prove that the AI did it correctly, safely, and legally?”

This shifts the conversation from features to:

- Baseline measurement  
- Error thresholds  
- Audit traceability  
- Data quality validation  
- Multilingual parity  
- Drift monitoring  

That is industrial AI thinking.

---

# 3️⃣ Five Hidden Layers — Detailed Detective Analysis

## Hidden Layer 1 — Data Quality Is the Real Foundation

Hans said:

> “About a third of the knowledge base is garbage.”

What this really means:

- There is no structured quality scoring system.
- There is likely no clear ownership per article.
- There are probably duplicate or conflicting policies.
- Outdated content may still be retrieved by RAG.
- No one currently measures knowledge reliability.

Why this matters technically:

RAG systems do not evaluate truth — they retrieve what exists.

If 30% of knowledge is outdated:
- Retrieval precision decreases.
- Hallucination risk increases.
- Confidence scores become misleading.
- Compliance exposure rises.

---

## Hidden Layer 2 — Auditability Is Assumed, Not Proven

Hans said:

> “We need EU AI Act readiness.”

What he did NOT clarify:

- Can we reconstruct past AI decisions?
- Do logs capture retrieval IDs?
- Is model version stored?
- Are policy checks logged?
- Is human override traceable?

Compliance is not documentation — it is reproducible evidence.

Without structured logging:
- Board reporting becomes narrative, not proof.
- External audit may fail.
- High‑risk classification cannot be defended.

---

## Hidden Layer 3 — Cost Reduction Is Undefined

Hans said:

> “Cut costs by 30%.”

But:
- 30% of ticket volume?
- 30% of staff hours?
- 30% of operational cost?
- Measured monthly or annually?
- Verified by finance or IT?

If automation increases misroutes or escalations, cost may rise despite lower L1 volume.

Automation without measurement = financial illusion.

---

## Hidden Layer 4 — Privacy Limits Evaluation

Hans said:

> “No employee PII in training.”

Implications:

- Cannot fine‑tune on raw tickets.
- Cannot store full production logs without redaction.
- Cannot build evaluation datasets casually.
- Must separate training and evaluation pipelines.

Without legally approved evaluation data:
- Accuracy cannot be proven.
- Multilingual fairness cannot be validated.
- Drift cannot be measured.

---

## Hidden Layer 5 — Multilingual Risk Is Underestimated

EN / DE / CZ from Day 1 implies:

- Potential language performance asymmetry.
- Insurance terminology inconsistencies.
- Different regulatory phrasing per language.
- Confidence calibration differences.

Small performance gaps in CZ may go unnoticed but create regulatory exposure.

---

# 4️⃣ The “SO WHAT?” Section — Deep Impact Analysis

Below are key statements translated into operational consequences.

---

### “30% cost reduction.”

So what?

- We must define baseline cost per ticket.
- We must measure misroute rate before and after automation.
- We must measure escalation shift (L1 → L2).
- We must calculate cost-per-resolution delta.
- We must ensure automation does not shift hidden costs upward.

If cost reduction is not mathematically modeled, it cannot be defended.

---

### “EU AI Act readiness.”

So what?

- We must define traceability schema.
- We must log model version per decision.
- We must log retrieved documents.
- We must log policy checks.
- We must log human approval points.
- We must define reproducibility testing protocol.

Compliance is not about saying “we are compliant.”  
It is about proving it.

---

### “Knowledge base is 30% outdated.”

So what?

- Golden dataset becomes unreliable.
- Retrieval precision decreases.
- False answers scale.
- Audit reproducibility becomes weaker.
- Trust erosion occurs rapidly.

Before scaling AI, knowledge must be scored and triaged.

---

### “On‑prem only.”

So what?

- Model size constrained by GPU availability.
- Latency tradeoffs may reduce accuracy.
- Multilingual models may require more compute.
- Logging storage must be local.
- Drift monitoring must be locally hosted.

Model choice cannot be separated from hardware feasibility.

---

### “No PII in training.”

So what?

- Must design anonymization pipeline.
- Must design synthetic dataset strategy.
- Must define legal approval workflow.
- Must clearly separate evaluation vs training datasets.
- Must validate redaction effectiveness.

Without privacy-safe evaluation, quality cannot be measured legally.

---

### “6 months.”

So what?

- Baseline metrics must be defined immediately.
- Evaluation datasets must be created early.
- Knowledge audit must be front-loaded.
- Logging schema must be defined before scaling.
- Multilingual validation must start in Month 1, not Month 5.

Timeline pressure requires early measurement, not late validation.

---

# 5️⃣ Two‑Column Exercise (Expanded Version — Core Deliverable)

Below is the structured translation of Hans’ statements into AI‑DS implications.

| What Hans Said | What This Really Means for AI‑DS (Detailed Explanation) |
|---------------|---------------------------------------------------------|
| “30% cost reduction.” | Define baseline cost metrics, misroute thresholds, escalation shift, and automation gating criteria. Cost must be measurable and tied to performance data. |
| “EU AI Act readiness.” | Design audit trace schema capturing input, retrieval, model version, policy checks, and human oversight. Compliance requires reproducible evidence. |
| “On‑prem only.” | Validate model feasibility under hardware constraints. Model selection must balance accuracy, latency, and GPU capacity. |
| “30% outdated knowledge base.” | Conduct structured data quality audit. Poor retrieval quality undermines automation reliability. |
| “Unify AI tools.” | Create standardized evaluation metrics and logging schema across systems to ensure comparability. |
| “No PII in training.” | Implement anonymization workflow and synthetic evaluation fallback. Legal approval required for dataset use. |
| “Multilingual from Day 1.” | Build language-specific evaluation slices and define acceptable performance variance. |
| “Everyone doing their own thing.” | Define AI registry and evaluation scope boundaries to ensure enterprise-wide visibility. |
| “Reduce policy update time.” | Integrate evaluation regression tests for every policy change. Measurement must accompany governance updates. |
| “I keep my job.” | Metrics must be board-defensible, financially tied, and reproducible under audit conditions. |
| "We already have ServiceNow + other tools." | Map data flows + connectors. Confirm which tools can provide required logs and which cannot. Create an integration gap list for Architecture Day. |
| "Cut shadow AI." | Run a 2-week AI-inventory sprint producing a registry with owners, data used, risk tier, and integration surface. |
| "We decreased L1 but problems emerged." | Provide root-cause checklist: KB quality, hallucinations, misroutes, lack of escalation. Offer corrective experiments to run in Week 2. |

If the right column simply repeats the left — no value added.  

---

# 6️⃣ AI‑DS — Data Quality & Evaluation Plan

## 6.1 Confluence Knowledge Audit

- Sample 200 of 2000 pages.
- Score on freshness, accuracy, completeness, duplication, language consistency.
- Flag pages scoring <3/5 for remediation.

Purpose:
Prevent scaling flawed retrieval.

---

## 6.2 Data Quality Scoring Framework

Each article evaluated on:

- Freshness (1–5)
- Accuracy (1–5)
- Completeness (1–5)
- Consistency (1–5)

Output:
Quantified knowledge reliability index.

---

## 6.3 Golden Dataset Design

- 20–30 Q&A pairs per ticket category.
- 300 per language (EN/DE/CZ).
- Include edge cases and policy-sensitive scenarios.
- Anonymized and versioned.
- Approved by AI‑SEC.

---

## 6.4 Baseline Metrics

Measure current:

- Resolution accuracy
- Misroute rate
- Escalation percentage
- CSAT per language
- Average resolution time

These define ROI baseline.

---

## 6.5 Evaluation Framework

Automated:

- Accuracy
- Misroute rate
- Retrieval precision
- Hallucination rate
- Multilingual variance

Human:

- Policy-sensitive review
- Override tracking
- Escalation validation

Drift Monitoring:

- Monthly re-evaluation
- Regression after policy updates

---

# 7️⃣ Biggest Risk

> Knowledge base quality is the most dangerous systemic risk.

Without clean data:
- Automation scales errors.
- Compliance weakens.
- Trust erodes.
- ROI collapses.

---

# 8️⃣ AI‑DS Success Statement

> Deliver a measurable, multilingual, audit-ready evaluation framework that proves automation is accurate, compliant, and financially defensible before scaling the agent platform.

