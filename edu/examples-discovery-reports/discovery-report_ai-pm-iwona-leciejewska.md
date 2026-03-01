Discovery Report — AI-PM

**Student:** Iwona Leciejewska  
**Date:** 24.02.2026  
**Client:** EuroHealth Insurance AG  
**Role:** AI Program Manager  
**Engagement:** AI Helpdesk Industrialization Initiative

---------------------------------------------------------------------



1. **EuroHealth Stakeholder Map (AI-PM View)**



1️⃣ Sponsor \& Decision Power
Hans (CIO) – Budget owner, under board pressure
→ Needs ROI + compliance story
→ Risk: pushes unrealistic timeline
Board – Indirect decision power
→ Cares about measurable results + regulatory safety



2️⃣ Control \& Veto
CISO (Stefan) – Compliance gatekeeper
→ Can block deployment
→ Must be aligned in Week 1



3️⃣ Execution \& Adoption
IT Ops Lead (Katarina) – Infra feasibility
→ Risk: performance / GPU constraints

Helpdesk Lead (Jan) – Adoption influencer
→ Risk: team resistance

12 Agents – Daily users
→ If they reject the tool, KPIs fail



4️⃣ Political Risk (Shadow AI)
HR \& Claims AI Owners
→ Built their own tools
→ May resist central governance



-----------------------------------------------------



2. **Translation Layer: What Hans Said vs What It Means**



“Everyone's doing their own thing.”| This is a governance program, not a feature build. Reframe scope to platform unification.
Multiple AI tools across departments|	Manage shadow AI politics and cross-department alignment.
“On-prem only.”|	Hard constraint → validate infra feasibility immediately.
“Knowledge base is 30% garbage.”|	Data quality is critical risk → audit before scaling.
“Cut costs by 30%.”|	Define clear KPIs and baseline now.
“I keep my job.”|	Sponsor pressure → board-ready reporting required.
Helpdesk fears replacement|	High adoption risk → structured change management needed.
EU AI Act emails|	Compliance is strategic → embed governance from Day 1.



-------------------------------------------------------------------------------------------



3. **Key Findings \& Implications for AI-PM**



1️⃣ The Real Problem Is Governance, Not Technology

Finding: Multiple AI tools exist across departments with no unified oversight.
Implication for PM: This must be positioned as an AI industrialization and governance program, not a chatbot build. Scope, roadmap, and success metrics must reflect consolidation and policy control.

2️⃣ Success Is Politically Sensitive

Finding: Hans’ credibility (and job security) is tied to visible results.
Implication for PM: Establish board-ready KPIs, monthly reporting cadence, and early governance wins to protect sponsor narrative and maintain executive support.

3️⃣ Data Quality Is the Primary Delivery Risk

Finding: ~30% of the knowledge base is outdated and unowned.
Implication for PM: Introduce a Phase 0.5 data audit/remediation workstream before committing to automation targets. Without this, adoption and accuracy will fail.

4️⃣ Infrastructure Feasibility Is Unverified

Finding: On-prem deployment is mandatory; budget is tight (€180K).
Implication for PM: Validate GPU capacity, latency expectations, and infra cost in Week 1. Prevent unrealistic commitments before architecture lock-in.

5️⃣ Adoption Risk Is High

Finding: Helpdesk team fears replacement.
Implication for PM: Embed change management, communication workshops, and human-in-the-loop controls to avoid silent resistance that would undermine KPI targets.

6️⃣ Compliance Is Both Constraint and Opportunity

Finding: EU AI Act compliance is a board priority.
Implication for PM: Run a parallel compliance workstream and frame governance readiness as a competitive advantage, not just regulatory overhead.

7️⃣ The Engagement Has Expansion Potential

Finding: Other departments (e.g., Claims) want similar capability.
Implication for PM: Design Phase 1 with scalability and reusability, enabling structured Phase 2 expansion (land-and-expand strategy).

PM-Level Synthesis

The project’s critical risks are unclear KPIs, weak data quality, infrastructure assumptions, adoption resistance, and compressed timeline.
Success depends more on governance alignment and structured phasing than on model selection.



----------------------------------------------------------------------------------------



4. **Technical / Functional Requirements to Investigate (AI-PM)**



1️⃣ Infrastructure Feasibility

On-prem GPU capacity and latency targets

Does €180K include hardware?

CI/CD and rollback capability

👉 No architecture commitment before infra validation.



2️⃣ Integration Scope

ServiceNow API (read/write complexity)

Confluence ingestion scope

Multi-language requirements (Phase 1 vs later)

Role-based access \& audit logging

👉 Integration complexity impacts timeline realism.



3️⃣ Data \& KPI Baseline

Validate “35% automation” claim

Assess knowledge base quality

Define measurable success baseline (30% of what?)

👉 No ROI projection without verified baseline.



4️⃣ Autonomy \& Guardrails (L2 Design)

Which tickets auto-resolve vs escalate

Override \& human-in-the-loop controls

Confidence thresholds

👉 Prevent scope creep toward risky autonomy.



5️⃣ Compliance Requirements

EU AI Act classification

Logging, explainability, governance artifacts

Post-go-live compliance ownership

👉 Compliance must be designed in from Day 1.



-----------------------------------------------------------------------



5. **Key Risks (AI-PM)**



Risk -	Owner - Mitigation
Outdated knowledge base (30%)	- AI-DS / PM -	Launch Week 1 data audit; define KB ownership before scaling
On-prem infra insufficient -	FDE / IT Ops - Validate GPU capacity \& latency in Week 1 before locking architecture
KPI baseline unclear (30% of what?) -	AI-DA / PM -	Confirm baseline metrics before committing ROI targets
Helpdesk resistance -	PM / Helpdesk Lead - Structured change plan + early wins + clear role positioning
EU AI Act compliance risk - AI-SEC -	Confirm classification early; embed logging \& governance from Day 1
Budget (€180K) too tight -	PM - Phase scope carefully; separate infra/compliance from pilot

-------------------------------------------------------------------------------



6. **Recommended Next Steps (First 2 Weeks)**



**Week 1 – Validation \& Alignment**

* Infrastructure Feasibility Check
  Validate on-prem GPU capacity, latency expectations, and budget assumptions with FDE and IT Ops.
* KPI Baseline Confirmation
  Confirm current helpdesk metrics (cost, MTTR, automation rate) with AI-DA to define the 30% reduction baseline.
* EU AI Act Risk Classification
  Align with AI-SEC and CISO on risk category and required governance artifacts.
* Stakeholder Alignment Meeting
  Conduct workshop with CIO, IT Ops, and Helpdesk Lead to align on autonomy level (L2), scope boundaries, and change expectations.



**Week 2 – De-Risk \& Structure Phase 1**

* Knowledge Base Audit Kickoff (Phase 0.5)
  Start data quality assessment with AI-DS; define KB ownership model.
* Define Phase 1 Scope \& Exclusions
  Lock ticket categories for auto-resolution and confirm phased rollout (e.g., IT EN/DE first).
* Change Management Plan Draft
  Outline communication, training, and human-in-the-loop workflow for helpdesk team.
* Board Reporting Framework
  Define monthly reporting template and governance milestones for CIO updates.Phased Delivery Model



--------------------------------------------------------------------------------------



7. **Cross-Role Dependencies (AI-PM)**



1️⃣ AI - FDE (Full-Stack / Infra)

Confirm on-prem GPU feasibility and latency targets

Validate model size vs hardware constraints

Provide infra cost assumptions

👉 My scope and timeline depend on infra realism.



2️⃣ AI-SEC (Security / Compliance)

Confirm EU AI Act risk classification

Define required logging, audit, and governance artifacts

Validate data handling constraints (PII boundaries)

👉 Compliance scope directly affects delivery timeline and reporting.



3️⃣ AI-DS (Data Science)

Validate 35% automation baseline

Assess knowledge base quality

Define evaluation framework and accuracy targets

👉 ROI projections depend on data reliability.



4️⃣ AI-DA (Data Analyst)

Define KPI baseline and measurement method

Design board-ready reporting metrics

Establish tracking for adoption and drift

👉 Without clear measurement, success cannot be proven.



5️⃣ AI-FE (Front-End / UX)

Define human-in-the-loop controls

Design override \& escalation experience

Assess adoption friction points

👉 Adoption risk mitigation depends on UX clarity.

