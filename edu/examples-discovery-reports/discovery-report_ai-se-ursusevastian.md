# Discovery Report — AI-SE

Client: EuroHealth Insurance AG
Role: AI Solution Engineer (AI-SE)
Scope: Phase 1 – IT Helpdesk
Autonomy Level: L2 (Constrained)
Deployment: On-Prem
Compliance Target: EU AI Act (August 2026 Board Review)
===

1️⃣ Structural Position

------------------------------------

EuroHealth’s risk is not AI malfunction.

It is ungoverned AI scale.

Without an enforceable control plane, AI proliferation creates:

Cross-domain data exposure

Non-reconstructable decisions

Regulatory misclassification

Autonomy escalation risk

Phase 1 establishes a defensible AI operating model, not feature expansion.

2️⃣ AI Registry \& Risk Governance (Article 9)

---------------------------------------

A centralized AI Registry is implemented as:

Unique system ID

Defined intended purpose

Risk classification methodology

Business owner + technical owner

Deployment environment

Change history log

Version traceability

Risk classification follows documented criteria aligned to EU AI Act risk definitions.

Registry updates require:

Governance board approval (CIO + CISO)

Mandatory entry before production release

Detection controls for unregistered AI endpoints

Shadow AI detection enforced via:

Network-level monitoring

Integration approval gates

Change management audits

Registry stored in version-controlled repository with audit trail.

3️⃣ Runtime Enforcement Layer (Article 14 + Drift Prevention)

--------------------------------------------------------------

Autonomy containment is enforced at execution layer:

Execution order:

RBAC validation

Risk-tier check

Tool allowlist validation

Policy-as-Code evaluation

HITL gate (if high-impact)

Logging

No action executes before passing all guardrails.

Policy engine cannot be bypassed by prompt content, as tool invocation requires validated middleware token.

Irreversible actions require mandatory human confirmation.

This prevents L2 → L3 drift structurally.

4️⃣ Logging \& Forensic Traceability (Article 12)

------------------------------------------------

Each decision stores:

Prompt hash (not raw PII if applicable)

Prompt version ID

Model version ID

Retrieval document ID + timestamp

Tool execution record

Risk classification tag

Human approval record

Immutable event ID

Controls:

Logs stored in tamper-evident storage

Retention policy defined per compliance requirement

Access role-restricted

Sensitive fields pseudonymized when required

Cross-system correlation enabled via shared trace ID

Reconstruction validated under 10 minutes in audit simulation.

Logging is structured for regulatory export.

5️⃣ CI/CD \& Adaptability (Articles 15 \& 61)

--------------------------------------------

All AI artifacts (model configs, prompts, policies) are:

Version-controlled

Peer-reviewed

Tested against golden dataset

Validated via policy compliance checks

Approved before release

Deployed via blue-green method

Rollback validated <30 minutes

Regulatory update workflow:

Policy amendment drafted

Risk review conducted

Automated validation tests executed

Staging deployment

Production release

Audit log updated

Deployment cycle target: <14 days.

6️⃣ Data Governance (Article 10)

-------------------------

Controls:

No employee PII in training data

Prompt-level PII detection

Retrieval boundary enforcement

Departmental data segmentation

Employee directory access restricted via tool-based queries

Logs redacted for sensitive fields

Logs do not become uncontrolled PII dataset.

7️⃣ Observability \& Continuous Monitoring (Article 61)

----------------------------------

On-prem monitoring stack includes:

Latency tracking

Error rate tracking

Override rate tracking

Escalation anomaly detection

KB freshness indicators

Tool invocation anomalies

Drift signals

AI-specific incident category established.

Kill-switch defined and tested.

8️⃣ Annex IV Conformity Preparation

-----------------------------------

For each registered AI system:

Intended purpose documentation

System architecture overview

Risk assessment record

Validation test results

Logging schema documentation

Governance workflow documentation

Monitoring controls

Change management history

Technical documentation repository maintained under version control.

9️⃣ Budget Discipline

-------------------------

Phase 1 prioritizes:

Registry

Runtime guardrails

Logging

CI/CD discipline

Excludes:

Enterprise-wide KB remediation

Cross-department AI redesign

Full cultural transformation

Scope discipline protects regulatory defensibility.

🔧 AI-SE — Environment \& Deployment Assessment (Upgraded Version)

1️⃣ Quantified Technical Constraints (Board-Defensible)

----------------------------------------------

1.1 Latency Constraint (User Adoption Threshold)



To maintain adoption by Jan’s team, system responsiveness must meet:



p95 end-to-end response time ≤ 2 seconds



Streaming must begin within < 800ms



Hard timeout at 5 seconds, triggering fallback state



Breakdown target:



Component	Target

Retrieval (vector search)	≤ 300ms

LLM first token	≤ 800ms

Full response generation	≤ 2s p95

ServiceNow write acknowledgment	≤ 400ms



If latency exceeds 2s p95:



Override frequency increases



Trust declines



Cost reduction KPI becomes unstable



Latency is not a UX preference — it is an ROI safeguard.



1.2 GPU Infrastructure Sizing (On-Prem Feasibility)



Phase 1 Scope: L1 Auto-Resolution + Routing



Model options considered:



Llama 3 70B (requires multi-GPU cluster)



Mistral 7B/8x7B (more feasible on-prem)



Minimum Viable Hosting Scenario (Phase 1)



If using 7B–13B parameter model:



1–2× A100 (40GB) or equivalent



OR 2–3× L40S class GPUs



Estimated concurrent throughput target:



15–20 parallel ticket evaluations



Sustained 5–10 RPS



If 70B model required:



4–8 GPUs minimum



Likely exceeds €180K infrastructure allowance



Conclusion:



Phase 1 architecture should assume 7B–13B class model optimized for retrieval + routing, not full 70B generative reasoning.



This is a feasibility gate before automation scale.



1.3 ServiceNow API Contract (Read/Write Boundary)



Integration must support:



Read Operations



Ticket ID



Category



Assignment group



Historical resolution notes



Escalation status



SLA timer



Write Operations (Restricted)



AI may:



Suggest resolution (draft comment)



Suggest reclassification



Flag escalation recommendation



AI may NOT:



Close ticket autonomously (Phase 1)



Modify SLA



Reassign outside L1/L2 without human confirmation



API Performance Constraint



Read call ≤ 250ms



Write acknowledgment ≤ 400ms



All writes require confirmation event logging



All write actions must return:



Confirmation ID



Timestamp



Policy version applied



This enables audit reconstruction.



2️⃣ Concrete ServiceNow Ticket Lifecycle Example

-----------------------------------------------

Example: Password Reset Ticket (Phase 1)

Step 1 — Ticket Created



Employee submits ticket:

Category: Password Reset

Priority: P3



System logs:



Ticket ID



Timestamp



Source system



Step 2 — AI Evaluation Triggered



System performs:



Retrieval from KB (vector search)



Confidence scoring



Escalation risk classification



Captured metadata:



Model version (e.g., mistral-7b-v2)



Prompt template version



Retrieved document IDs



Confidence score (0.82)



Policy version



Latency target: <2s p95



Step 3 — AI Suggestion Generated



AI returns:



“Reset your password using portal link X.”



UI shows:



Confidence: HIGH



Source: KB-PasswordReset-v3 (updated Jan 2026)



“Approve \& Send”



“Override \& Escalate”



Step 4 — HITL Enforcement



Because confidence > 0.75 AND category = low-risk:



AI suggestion is eligible for L1 resolution.



However:



Ticket remains in “Pending Approval” state.



Jan’s team must click “Approve.”



No auto-close allowed in Phase 1.



Step 5 — Agent Approval



Agent clicks Approve.



System performs:



ServiceNow comment write



Status update to “Resolved”



Logs human approval flag



Audit entry stored:



Ticket ID



AI suggestion



Human approval timestamp



Model + policy version



Reconstruction possible in <24h.



3️⃣ Human-in-the-Loop (HITL) Technical Enforcement Model

--------------------------------------------------------

HITL is not UX — it is runtime policy enforcement.



3.1 Enforcement Architecture

-----------------------------------

HITL implemented as:



Policy-as-Code rule engine between:



LLM output



ServiceNow write endpoint



AI output cannot directly execute write.



All actions pass through:



Policy Gateway Layer.



3.2 HITL Rules (Phase 1)

-----------------------------

Condition	Action

Confidence ≥ 0.75 AND Category = Low Risk	Require human approval

Confidence < 0.75	Force escalation suggestion

Category = Financial / Claims	Mandatory escalation

Policy version mismatch	Block execution

SLA < 30 mins remaining	Force human review



No direct execution allowed.



3.3 Override Logging Requirements

------------------------------------------

When agent overrides:



System logs:



Original AI suggestion



Override action



Agent ID



Timestamp



Reason category (dropdown)



Override rate feeds AI-DA metrics.



3.4 Kill-Switch Capability



CISO may trigger:



System-wide AI suggestion disable



Category-specific disable



Model rollback to previous version



Kill-switch must execute within <60 seconds.



4️⃣ Deployment \& Rollback Strategy

-------------------------------------

Blue-Green Deployment:



Model v1 and v2 run in parallel



10% traffic to v2



Monitor:



Override rate



Escalation accuracy



Latency



If override rate increases >15% week-over-week → automatic rollback.



Rollback time target: <5 minutes.



5️⃣ Governance \& Audit Reconstruction SLA

------------------------------------------

System must support:



Full decision reconstruction within 24 hours



Log retention aligned with compliance requirements



Immutable log store



Role-based access



Audit reconstruction must answer:



Which model version?



Which KB source?



What confidence?



Who approved?



Which policy applied?





