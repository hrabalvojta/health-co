# Discovery Packet v1 — AI-PM (AI Product Manager)

## Student: Klaudia Olszewska

## Date: February 23, 2026

## Client: EuroHealth Insurance AG



---





## Part 1: Discovery Questions (10)

### Question 1: Where do you believe your current ServiceNow + Moveworks setup will not be sufficient to meet EU AI Act governance and audit expectations by 2027?



**Why this matters:** Anchors the conversation to board pressure and surfaces structural governance gaps beyond chatbot capability.

**Red flag (bad answer):** “We just need better tuning or documentation.” → Signals misunderstanding of enforceable governance vs feature improvement.

**KAF component:** Core / Policy-as-Code / Run Safe



### Question 2: If this initiative succeeds in 6 months, what measurable risk reduction or governance capability must exist for you to confidently tell the board EuroHealth’s AI is controlled and defensible?



**Why this matters:** Aligns scope to business risk and executive accountability, not technical outputs.

**Red flag (bad answer):** Focus only on automation rate or CSAT.

**KAF component:** Core



### Question 3: Are you prepared to mandate that all AI workflows — including HR, Claims, and Finance tools — must run through a single governed on-prem control layer with policy enforced in code and centralized audit logging?



**Why this matters:** Industrialization requires structural authority to centralize enforcement and eliminate shadow AI.

**Red flag (bad answer):** “Departments should stay autonomous.”

**KAF component:** Core / Interop / Policy-as-Code



### Question 4: Which regulatory and internal rules must be technically enforceable in code — not just documented — to satisfy your CISO and EU AI Act obligations?



**Why this matters:** Defines the Policy-as-Code surface (PII filtering, data residency, access control, retention, output filtering, model constraints).

**Red flag (bad answer):** “We rely on guidelines and awareness.”

**KAF component:** Policy-as-Code



### Question 5: If a regulator requested full traceability of an AI-driven decision tomorrow — model version, data source, prompt, tool calls, policy checks, approvals — could you produce defensible evidence within 24 hours?



**Why this matters:** Tests audit readiness and Digital Trust maturity.

**Red flag (bad answer):** “We could reconstruct it manually.”

**KAF component:** Run Safe



### Question 6: If EU AI Act guidance changes next quarter, how long would it take to update controls and propagate them across all active AI workflows?



**Why this matters:** Measures regulatory agility and governance propagation speed (days vs months).

**Red flag (bad answer):** Requires a separate project per workflow.

**KAF component:** Policy-as-Code / Interop



### Question 7: Which end-to-end business workflows do you expect AI agents to autonomously orchestrate beyond ServiceNow, and which systems must they integrate with?



**Why this matters:** Defines MCP/A2A interoperability scope and orchestration complexity (identity, HRIS, Claims DB, CMDB, monitoring tools).

**Red flag (bad answer):** No clear mapping of cross-system dependencies.

**KAF component:** Interop (MCP/A2A) / Core



### Question 8: At which risk-classified decision points must human approval be technically enforced — and how is that surfaced in the workflow or UI today?



**Why this matters:** Ensures Human-in-the-Loop checkpoints are enforced by system design, not informal process.

**Red flag (bad answer):** Approvals are procedural only, not system-enforced.

**KAF component:** HITL / Policy-as-Code



### Question 9: How do you monitor AI systems in production beyond uptime — including drift, policy violations, anomalous tool usage, or misuse attempts?



**Why this matters:** Industrial AI requires runtime observability and behavioral telemetry.

**Red flag (bad answer):** Monitoring limited to vendor dashboards or availability metrics.

**KAF component:** Run Safe



### Question 10: Given the on-prem constraint and €180K / 6-month timeline, what is the minimum viable governance platform you are prepared to fund — and what would you consciously de-scope?



**Why this matters:** Aligns ambition with budget reality and protects Phase 1 from scope inflation.

**Red flag (bad answer):** Expectation of full EU AI Act compliance within 6 months.

**KAF component:** Core



Minimum coverage satisfied:

• Policy-as-Code → Q1, Q3, Q4, Q6, Q8

• MCP/A2A Interoperability → Q7

• Human-in-the-Loop → Q8



---



## Part 2: KAF Mapping (mini)

| KAF Component      | Covered by Q#   | Notes                                               |

|--------------------|-----------------|-----------------------------------------------------|

|Agentic Core        |1,2,3,7,10       |Strategy, mandate, scope, budget                     |

|Agentic Ingestion   |4 (partial)      |PII/data governance enforcement at ingestion boundary|

|Policy-as-Code	     |1,3,4,6,8	       |Enforceable governance layer                         |

|Digital Trust       |3,5,9	       |Audit traceability & runtime observability           |

|Human-in-the-Loop   |8	               |Risk-tiered approval enforcement                     |

|Interop (MCP/A2A)   |3,6,7	       |Cross-system orchestration & propagation             |



---



## Part 3: Assumptions / Risks / Open Items (3-5)



1. Assumption: CIO has mandate authority to centralize AI governance across departments.

2. Risk: Departments resist consolidation, creating political friction.

3. Risk: Existing ServiceNow architecture may limit centralized enforcement insertion points.

4. Assumption: Board pressure is compliance-driven, not cost-cutting driven.

5. Open item: Current AI system inventory completeness and ownership clarity.



---



## Part 4: What We Will Measure (3 KPI proposals)



1. **Mean Time to Evidence (MTTE): ≤ 24 hours**

Ability to produce a complete, regulator-ready trace of any AI-assisted decision (model version, prompt, data source, policy checks, human approvals).

2. **Governed Workflow Coverage: ≥ 80% of AI workflows running through centralized Policy-as-Code layer within Phase 1 scope**

All in-scope AI systems (ServiceNow, HR chatbot, Claims PoC, Finance GPT) registered and enforced via a unified control plane.

3. **Operational Impact Metric** (choose based on CIO priority):

CSAT uplift: 3.2 → ≥ 4.0 within 12 months

OR

Misroute reduction: ≥ 50% reduction in escalations caused by missing policy/integration controls

OR

Escalation containment rate: ≥ 30% fewer L2 escalations attributable to governance or routing errors



---



## Part 5: Agent Classification



- **Governance tier:** Enterprise

- **Registry/reuse potential:** Register as Enterprise Governance Control Plane template within Kyndryl AI Framework (KAF); reusable for other EU-regulated clients requiring AI Act readiness and on-prem enforcement.



---



## Dependencies on Other Roles:

I need AI-SEC to validate risk posture, threat modeling, and AI-specific incident response requirements.

I need FDE to assess feasible enforcement insertion points (gateway vs orchestration vs runtime).

I need AI-SE to evaluate CI/CD integration for policy propagation.

I need AI-DS to assess KB quality, evaluation framework, and drift detection metrics.

I need AI-FE to review how HITL checkpoints and explainability are surfaced in the UI.



## Questions I Deliberately Did NOT Ask (and why):

“Where should policy enforcement technically reside (gateway vs runtime)?” — because that is FDE’s architectural design domain.

“Which LLM hosting stack will be used on-prem?” — because that is FDE / AI-SE territory.

“What specific telemetry instrumentation exists in logs?” — deeper observability details belong to AI-SE.

“What red-teaming methodology do you apply?” — belongs to AI-SEC.



## Positioning Statement for Meeting:

We are not here to make your AI smarter.

We are here to make it defensible, enforceable, and scalable under EU AI Act pressure — within 6 months and €180K.

