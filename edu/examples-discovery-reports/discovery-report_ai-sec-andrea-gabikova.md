There are 2 versions of Discovery report below for AI-SEC role:

 **1-slide executive version** 

---

# AI Consolidation – Security & EU AI Act Readiness

## 1️⃣ Current Situation

* AI already live: Moveworks/ServiceNow + HR chatbot + Claims prototype
* No centralized AI governance or system registry
* On-prem mandate in place, but logging & data flows not yet validated
* Target: 30% helpdesk cost reduction + unified AI platform + EU AI Act compliance (Aug 2026)

---

## 2️⃣ Critical Unknowns (Immediate Exposure)

* **Has the Claims prototype processed real claims data?**
  → Potential High-Risk AI classification

* **Do embeddings contain special category health data?**
  → Deletion & retention complexity

* **Where are AI logs stored (incl. Moveworks telemetry)?**
  → Possible residency / audit gap

* **Will platform unification increase breach blast radius?**
  → One entry point ≠ one trust zone

* **Does cost reduction conflict with required human oversight?**
  → Automation limits under EU AI Act

---

## 3️⃣ Business Risk Framing

If unmanaged:

* Regulatory exposure could exceed projected helpdesk savings
* Late reclassification of Claims AI in 2026 = compressed remediation cost
* Consolidation without segmentation = amplified incident impact

This is a timing issue, not a capability issue.

---

## 4️⃣ 14-Day Stabilization Plan

**Week 1 – Contain Unknowns**

* AI system inventory + data flow mapping
* Claims prototype triage (data used, logs, embeddings, retention)
* Logging & residency validation (incl. vendor telemetry)

**Week 2 – Define Guardrails**

* EU AI Act pre-classification (with Legal)
* Threat modeling (Claims + unified platform)
* Secure consolidation principles (segmentation, RBAC, centralized logging)

---

## 5️⃣ Decisions Required

1. Pause Claims expansion until triage complete?
2. Centralize AI governance under CIO authority?
3. Approve “one platform, multiple trust zones” as consolidation principle?
4. Align cost target with mandatory human oversight thresholds?

---

**Bottom Line:**
You can achieve cost reduction and compliance — but only if governance catches up to innovation in 2025.

Stabilize now → scale safely → avoid 2026 correction.

--------------------------------------------------------------------------------------------------------------
# AI Security Discovery Brief

**To:** Hans Muller, CIO (EuroHealth Insurance AG)
**From:** AI Security Lead, Kyndryl AI Consulting
**Subject:** AI Consolidation: Hidden Compliance & Security Exposures to Address Now
**Date:** Day 12 – Roleplay Discovery Summary

---

## Executive Bottom Line

EuroHealth can hit the stated outcomes (30% remaining helpdesk cost reduction, unified AI platform, EU AI Act compliance by **August 2026**) — but the current AI footprint contains **latent exposures** that can turn into an expensive 2026 “compliance catch-up” if not addressed in early 2025.

The most important point: **you already have an AI estate, not a single system**. Shadow AI plus unclear data handling means risk may already exist in production workflows, particularly if the Claims prototype touched real claims data.

This brief highlights **second-order risks** that are easy to miss in cost-driven consolidation initiatives — and proposes a two-week plan to regain control without derailing savings.

---

## What We Heard (Your Success Criteria)

* AI is already deployed via **Moveworks/ServiceNow** for basic tickets
* Shadow AI exists: **HR chatbot** + **Claims LangChain prototype**, no governance
* Success = **30% reduction** in remaining helpdesk cost + **single unified AI platform**
* **On-prem only** (non-negotiable)
* Knowledge base ~**30% outdated**, no owner
* Helpdesk team fears replacement (Jan + 12 agents)
* Budget: **€180K / 6 months** (tight)

---

## Security & Compliance Reality Check (Deeper Risk Exposures)

### 1) If the Claims prototype has already processed real claims…

This is the single highest-risk unknown.

If real claim narratives, medical codes, attachments, or policy determinations were used in prompts or retrieval:

* You may already have **regulated processing** occurring without a DPIA-style assessment
* You may have **uncontrolled retention** in logs, vector stores, or tracing tools
* You may have inadvertently crossed into **High-Risk AI territory** (if outputs influence claim outcomes)

**Implication:** Consolidation becomes secondary until we confirm whether regulated processing is already underway.

**Immediate ask:** Confirm whether the Claims prototype used **production data**, even “just for testing.”

---

### 2) If embeddings contain special category health data…

Insurance claims data often qualifies as **special category personal data** (health). If the Claims prototype uses RAG with a vector database, embeddings may:

* Encode sensitive information in a way that is difficult to fully purge
* Be replicated across environments (dev/test/prod)
* Persist beyond intended retention windows
* Become accessible to broader roles if access control is weak

**Second-order risk:** Even if you delete original documents, the vector store may still contain recoverable signals.

**Implication:** Any “unify under one platform” strategy must include **vector governance** (classification, encryption, access controls, retention, deletion guarantees).

---

### 3) If Moveworks/ServiceNow logs are stored differently than on-prem requirements allow…

You stated “on-prem only” is non-negotiable. The risk here is not the inference layer alone — it’s the **telemetry and logging**:

* Prompt logs, conversation transcripts, and troubleshooting traces are often stored in vendor-managed locations or formats.
* Even if the primary platform is “on-prem compatible,” audit logs or support diagnostics could be handled differently.

**Second-order risk:** You could be “on-prem for processing” but “not on-prem for evidence,” which breaks audit and compliance posture.

**Implication:** We must validate **where** logs live, **how long** they persist, and **who** can access them — before treating the current environment as compliant-by-design.

---

### 4) If unifying platforms increases blast radius instead of reducing it…

Unification sounds like risk reduction, but it often increases risk if done without segmentation:

* A single AI entry point with broad connectors can turn one compromised identity into access across HR + IT + Claims
* Prompt injection or malicious content in one source can pollute downstream outputs across multiple workflows
* Centralizing knowledge and tools can create a **single point of failure** operationally and from an incident-response standpoint

**Implication:** “One platform” should not mean “one trust zone.” We’ll need **segmented domains**, strict RBAC, and isolation of Claims/HR/IT data.

---

### 5) If cutting helpdesk cost conflicts with EU AI Act human oversight…

Your cost target is clear. But EU AI governance expectations (especially for high-risk use cases) typically require:

* Human oversight, escalation thresholds, and documented decision accountability
* The ability to explain outputs and trace the basis for actions
* Controls to prevent harmful automation (especially where outcomes affect individuals)

**Second-order risk:** Aggressive cost cutting can unintentionally remove human review that regulators expect — turning savings into compliance exposure.

**Implication:** We need to define which use cases can be safely automated end-to-end vs. which require **human-in-the-loop** (and how that affects the cost model).

---

## Preliminary EU AI Act Exposure (Working View)

| AI Use Case            | Likely Category              | Why it matters                                          |
| ---------------------- | ---------------------------- | ------------------------------------------------------- |
| IT Helpdesk automation | Likely “limited risk”        | Transparency, logging, security controls still required |
| HR chatbot             | Limited → potentially higher | Employee data + potential workplace impact              |
| Claims prototype       | Potential **high-risk**      | If it influences decisions affecting customers          |

**Critical unknown:** Whether Claims AI is informational support vs. outcome-influencing. That distinction changes everything.

---

## Key Security Findings (Condensed)

1. **Shadow AI exists without governance** → unknown exposure and inconsistent controls
2. **On-prem requirement** narrows options and increases need for internal logging/audit capability
3. **Knowledge base quality** is a security and integrity risk (hallucinations + wrong guidance)
4. **Human factors** (helpdesk fear) create operational resistance + insider risk
5. **Budget constraint** requires ruthless prioritization toward controls that reduce regulatory exposure fast

---

## Recommended Next Steps (First 2 Weeks)

### Week 1 — Visibility & Containment (Stop Unknowns)

1. **AI Inventory + Data Flow Mapping (Workshop)**

* List every AI system (Moveworks/ServiceNow, HR bot, Claims prototype, anything else)
* Identify owners, environments, connectors, and where data/logs live

2. **Claims Prototype Rapid Triage**

* Did it process real claims? Y/N
* What data types? (health data, attachments, IDs)
* Where are prompts, traces, and embeddings stored?
* What deletion is possible and verified?

3. **Logging & Residency Verification (Moveworks/ServiceNow)**

* Confirm where prompt logs, transcripts, and diagnostics are stored
* Confirm retention windows and access paths
* Confirm audit-export capability for regulators/internal audit

4. **Shadow AI Containment**

* Temporary control: no new AI deployments without registration + security review
  (Framed as “risk containment,” not “innovation shutdown.”)

---

### Week 2 — Risk Classification & Secure Consolidation Guardrails

5. **EU AI Act Pre-Classification (with Legal/Compliance)**

* Classify each use case and define obligations
* Identify documentation requirements and deadlines backward from Aug 2026

6. **Threat Modeling (Priority: Claims + Unified Platform)**

* Prompt injection, data exfiltration, tool misuse, lateral movement across domains

7. **Secure Consolidation Principles (Non-negotiables)**

* “One platform, multiple trust zones”
* Segmented connectors (Claims/HR/IT)
* RBAC + least privilege
* Centralized logging to on-prem SIEM
* Vector DB governance (encryption, retention, deletion, access)

---

## Decisions Needed From You (CIO)

1. **Claims prototype freeze until triage complete?**
   If it has touched real claims data, we should pause expansion until classification + logging are verified.

2. **Confirm AI governance authority**
   Centralized under CIO (recommended) vs. distributed ownership (current reality).

3. **Agree the guardrail principle**
   Unify platforms only if segmentation prevents blast-radius expansion.

4. **Align cost target with oversight obligations**
   Define where automation is allowed vs. where human review remains mandatory.

---

## Closing Perspective

You’re aiming to reduce cost and risk simultaneously. That’s achievable — but only if we eliminate “unknown unknowns” now.

The biggest hidden risk is not model quality; it’s **uncontrolled data handling** (prompts, logs, embeddings) plus **unclear classification** of Claims AI under EU AI Act.

If we validate these points in the next two weeks, we can keep your consolidation plan moving — without creating a 2026 compliance surprise.