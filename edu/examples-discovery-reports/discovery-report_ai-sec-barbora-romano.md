##### **AI-SEC Discovery Report**

##### 

##### **Client: EuroHealth Insurance AG**

##### **Sponsor: Hans Müller (CIO)**

##### **Workstream: AI Industrialization – Security \& Governance**

##### **Date: 24.2.2026**



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



**1. Executive Summary (AI-SEC Perspective)**



EuroHealth is in an early scaling phase of AI adoption with:



ServiceNow + Moveworks handling IT tickets



Shadow AI initiatives (HR chatbot, Claims LangChain prototype)



No unified governance or AI risk structure



Board mandate: EU AI Act ready by August 2026



Strong operational pressure: 30% helpdesk cost reduction



Strict on-prem constraint



The organization is optimizing for speed and cost efficiency, but governance, security enforcement, and traceability mechanisms are not yet industrialized.



From an AI-SEC standpoint, the core risk is:



AI capabilities are expanding faster than risk ownership, guardrails, and auditability controls.



**2. Status of Day 11 Discovery Questions**

Question	Status	Insight

Lightweight AI risk control plane?	Implicitly needed, not confirmed	Shadow AI confirms lack of central control plane

Structure for EU AI Act auditability?	Open	Compliance target exists, but no defined structure

Technical guardrails across systems?	Open	No evidence of tool-level or execution guardrails

Interpretation



Governance intent exists (board pressure), but enforcement architecture does not yet appear defined.



**3. Key Findings (AI-SEC Lens)**

**3.1 Shadow AI Presence**



HR chatbot operating outside central oversight



Claims LangChain prototype (unknown integration depth)



Implication:

No formal AI inventory, no risk-tier classification, no unified control layer.



Second-order risk:

Unregistered systems may already qualify as regulated systems under EU AI Act once scaled.



**3.2 “No PII in Training Data” Constraint**



Declared policy, but no evidence of:



Enforcement mechanism



Retrieval boundary control



Logging redaction strategy



Embedding/vector store governance



Critical risk:

Even if training excludes PII, prompts, outputs, and logs can still contain personal data.



**3.3 Knowledge Base Integrity Gap**



~30% outdated



No ownership assigned



From AI-SEC perspective, this is not content hygiene — it is a data integrity and operational risk surface.



Second-order effect:

AI amplifies outdated content at scale → incorrect operational decisions → regulatory exposure.



**3.4 On-Prem Only Constraint**



This significantly impacts:



Model gateway choices



Monitoring tooling



Logging infrastructure



Policy engines



Secret management



Scalability



Implication:

Control-plane architecture must be fully self-managed and operationally sustainable.



**3.5 Cultural / Organizational Signals**



Helpdesk fears replacement



Innovation is decentralized



Governance not centralized



Risk:

Resistance can drive further shadow AI and policy bypass behavior.



**4. AI-SEC Risk Assessment**

**4.1 Governance Risk**



No confirmed AI system inventory



No defined risk classification framework



No clarity on board reporting structure



Exposure:

Regulatory non-alignment if AI use cases expand without formal registration.



**4.2 Auditability Risk**



Unclear if logs capture:



Model version



Prompt metadata



Tool execution traces



KB version at time of response



Human approval checkpoints



Risk:

Inability to reconstruct decisions under regulatory review.



**4.3 Execution Guardrail Risk**



Claims LangChain prototype may:



Access internal systems



Execute automated steps



Operate with broad permissions



No evidence of:



Least privilege model



Policy-based action gating



Confidence threshold enforcement



Mandatory HITL enforcement



Blast radius risk:

Unified AI platform without guardrails increases systemic exposure.



**4.4 Logging Paradox Risk**



Audit trail required

But logs may contain PII



If logs are not filtered or classified:



Compliance risk shifts from training to logging



Audit solution becomes a new regulated dataset



**4.5 Operational Maturity Risk**



Unclear:



How quickly policies can be updated



Who owns AI incident response



Whether kill-switch capability exists



Whether EU AI Act classification can trigger control updates automatically



Current state suggests:

Controls are static or undefined, not adaptable.



**5. Gaps Identified**

Area	Current State	Required State

AI Inventory	Unknown / fragmented	Central registry with risk tiers

Risk Ownership	Implicit	Explicit, documented

Guardrails	Not evidenced	Enforced via Policy-as-Code

Logging	Standard IT logs	AI-specific forensic logging

Data Governance	Policy statement	Automated enforcement

KB Governance	Weak	Versioned, owned, controlled

Incident Response	Assumed	AI-specific playbooks



**6. Critical Questions Requiring Further Investigation**



Does Claims AI influence or recommend decisions affecting financial outcomes?



Does “no PII in training” also apply to:



Retrieval



Embeddings



Logs



How are AI identities authenticated and authorized?



Who can disable or suspend an AI system?



What SIEM / audit stack exists on-prem?



How does ServiceNow governance integrate with non-ServiceNow AI systems?



**7. First 2 Weeks – AI-SEC Recommended Actions**

**Week 1 – Stabilize \& Illuminate**



Conduct rapid AI system inventory (including shadow)



Perform high-level data flow mapping



Identify systems with tool execution capability



Assess logging coverage



Define minimum guardrail baseline



Deliverable:

AI Risk Exposure Snapshot (initial maturity assessment)



**Week 2 – Define Control Plane MVP**



Define AI Policy-as-Code control set (MVP scope)



Define audit log schema (what must be captured)



Define identity and permission model for AI systems



Define HITL enforcement points



Define KB governance minimum standard



Deliverable:

AI Security Industrialization Blueprint (MVP version)



**8. Dependencies on Other Workstreams**

Role	Dependency

Governance Lead	EU AI Act interpretation \& risk tier mapping

ServiceNow Architect	Workflow enforcement integration

Enterprise Architect	On-prem integration design

Data Privacy Officer	PII interpretation \& retention policy

SOC / Security Ops	Logging, SIEM integration, incident response

Change Management	Adoption \& shadow AI mitigation



**9. Budget \& Scope Reality Check**



Ambition:



Unified AI platform



Full EU AI Act readiness



Industrialized governance



Audit trail



On-prem enforcement



Shadow AI control



Budget:

€180K / 6 months



Risk:

Expectations may exceed feasible industrialization scope within budget.



Recommendation:

Prioritize:



Inventory + risk-tiering



Guardrails for execution



Audit logging architecture



Minimum viable control plane



Avoid attempting:



Full enterprise transformation in 6 months



Complete KB remediation in this phase



**10. Strategic Positioning**



EuroHealth does not currently have a security crisis.



They have a scaling risk.



AI adoption is ahead of governance maturity.



The objective is not to restrict innovation.



It is to:



Build embedded, automated guardrails that allow AI to scale safely under board-level scrutiny.



**Final Assessment (AI-SEC View)**



EuroHealth is:



Functionally progressing in AI



Structurally underprepared for regulatory-scale deployment



Politically sensitive to heavy governance



Operationally constrained by on-prem architecture



Budget-limited relative to ambition



Primary mission for AI-SEC:



Design invisible enforcement mechanisms that:



Do not slow innovation



Do not rely on documentation alone



Provide audit defensibility



Reduce systemic blast radius

