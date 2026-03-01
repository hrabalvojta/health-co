# Discovery Packet v4 — AI Software Engineer (AI-SE)

## Date: February 2026

## Author: Vojtech Hrabal

## Client: EuroHealth Insurance AG

## Engagement: AI Industrialization (On-Prem, EU AI Act Ready, 6 Months / €180K)

## Role: AI Software Engineer (AI-SE)

---

# Part 1 — AI-SE Discovery Questions (10)

---

## Q1. Where does your current ServiceNow + Moveworks setup break from an engineering control perspective?

**Question:**
What cannot be versioned, tested, monitored, or rolled back today?

**Why this matters:**
AI industrialization starts where vendor-native governance ends.

**Red flag:**
“We manage that manually.”

**KAF:** Core / Run Safe

---

## Q2. Do you have a centralized, version-controlled AI registry?

**Question:**
Can you provide a technical registry of models, prompts, workflows, owners, risk tier, and deployment environments?

**Why this matters:**
No registry = no enforceable governance.

**Red flag:**
“We track that in spreadsheets.”

**KAF:** Core / Digital Trust

---

## Q3. What does your AI deployment pipeline look like?

**Question:**
Do you have dev/test/prod separation for AI artifacts (models, prompts, policies)? Is CI/CD enforced?

**Why this matters:**
AI must follow software engineering discipline.

**Red flag:**
Changes made directly in production.

**KAF:** Run Safe

---

## Q4. What is your rollback strategy?

**Question:**
If an AI update causes routing errors or compliance violations, how fast can you revert to a known-good version?

**Why this matters:**
Rollback defines operational maturity.

**Red flag:**
“We fix it manually.”

**Target:** <30 minutes rollback time.

**KAF:** Run Safe

---

## Q5. Can you reconstruct an AI decision end-to-end?

**Question:**
Can you trace input → retrieval → prompt → model version → tool calls → policy checks → human approval → output?

**Why this matters:**
EU AI Act defensibility requires replayable execution chains.

**Red flag:**
Only output logs exist.

**KAF:** Digital Trust / Run Safe

---

## Q6. Which governance rules are technically enforced vs documented?

**Question:**
Which AI policies are embedded in runtime enforcement (Policy-as-Code), and which exist only as guidelines?

**Why this matters:**
Engineering must convert policy into code.

**Red flag:**
“We rely on teams to follow governance documentation.”

**KAF:** Policy-as-Code

---

## Q7. How are AI agents authenticated and authorized?

**Question:**
Do agents operate with user impersonation, service identities, or shared credentials? Is least-privilege enforced?

**Why this matters:**
Identity defines blast radius and auditability.

**Red flag:**
Shared admin accounts.

**KAF:** Interop / Run Safe

---

## Q8. How is AI behavior monitored in production?

**Question:**
Do you track drift, misrouting rate, escalation rate, abnormal actions, or policy violations in real time?

**Why this matters:**
Enterprise AI requires unified observability.

**Red flag:**
Monitoring limited to uptime.

**KAF:** Run Safe

---

## Q9. How is data ingestion governed?

**Question:**
How do you technically ensure no PII enters training, fine-tuning, retrieval pipelines, prompts, or logs?

**Why this matters:**
Most AI compliance breaches occur in ingestion and logging.

**Red flag:**
“We instruct teams not to upload PII.”

**KAF:** Ingestion / Policy-as-Code

---

## Q10. What bottleneck will break first if we scale from 3 AI use cases to 25 across departments and 8 EU countries?

**Why this matters:**
Scaling exposes weaknesses in connectors, monitoring, IAM, and deployment automation.

**Red flag:**
“We haven’t evaluated cross-department scaling.”

**KAF:** Core / Interop

---

# Part 2 — KAF Coverage (AI-SE Lens)

| KAF Component            | Covered by Q#                      |
| ------------------------ | ---------------------------------- |
| Agentic Core             | 1, 2, 10                           |
| Agentic Ingestion        | 9                                  |
| Policy-as-Code           | 6, 9                               |
| Digital Trust / Run Safe | 3, 4, 5, 8                         |
| Human-in-the-Loop        | (validated via traceability in Q5) |
| Interop (MCP/A2A)        | 7, 10                              |

---

# Part 3 — Engineering Assumptions / Risks / Open Items

1. No centralized AI registry exists today.
2. CI/CD for AI artifacts is immature or absent.
3. Rollback process is manual and slow.
4. Audit trail is incomplete outside ServiceNow.
5. Policy updates follow quarterly release cycles.
6. IAM for AI agents lacks strict least-privilege enforcement.
7. Shadow AI systems may bypass monitoring stack.
8. On-prem LLM lifecycle governance is undefined.

---

# Part 4 — AI-SE KPI Targets (Industrialization Metrics)

## Governance & Compliance

* 100% AI systems registered.
* ≥99% end-to-end trace coverage.
* Policy update propagation ≤ 5 business days.

## Operational Maturity

* Rollback time objective < 30 minutes.
* Incident detection time < 15 minutes.
* 100% AI changes via version-controlled CI/CD.

## Production Performance

* Drift detection implemented for all production agents.
* Monitoring unified across ServiceNow + shadow AI.
* Audit reconstruction SLA ≤ 24 hours.

---

# Part 5 — Target Architecture Characteristics

An industrialized AI platform must include:

* Central AI registry (models, prompts, workflows, risk tier).
* Policy-as-Code enforcement layer.
* CI/CD pipelines with validation gates.
* Versioned configuration management.
* Unified logging & telemetry.
* Identity propagation with least-privilege enforcement.
* Kill switch & rollback automation.
* Environment separation (dev/test/prod).
* On-prem LLM lifecycle governance (patching, versioning, performance testing).

---

# Part 6 — Agent Classification

* **Governance Tier:** Enterprise
* **Regulatory Exposure:** High (EU AI Act + GDPR)
* **Autonomy Level:** Controlled Agent with enforced HITL boundaries
* **Registry Reuse Potential:** Enterprise Governance Blueprint reusable across regulated EU clients

---

# Dependencies (AI-SE View)

* **AI-SEC:** Risk classification, IAM boundary validation, threat modeling.
* **FDE:** Infrastructure readiness, GPU capacity, network segmentation.
* **AI-DS:** Data quality, PII classification, evaluation baselines.
* **AI-DA:** Monitoring dashboards and telemetry instrumentation.
* **AI-PM:** Executive prioritization and scope discipline.

---

# Questions I Deliberately Did NOT Ask

* Business ROI prioritization → AI-PM scope.
* Legal interpretation of EU AI Act → AI-SEC scope.
* Knowledge taxonomy & annotation details → AI-DS scope.
* UX / UI workflow design → AI-FE scope.

My focus as AI-SE is:

> Engineering enforceable, observable, version-controlled AI systems that are compliant by design.

Prepared for: CIO Discovery Meeting\
Prepared by: AI Solutions Engineer (Kyndryl AI Consulting)