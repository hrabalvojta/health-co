# Discovery Report  
**Client:** EuroHealth Insurance AG  
**Role:** AI Front End Developer – Kyndryl AI Consulting  
**Context:** Post-Roleplay Reflection (CIO – Hans Muller)

---

# I. Day 11 Question I  
## Which AI policies must be technically enforceable in code — and at which control point?

### What Hans Answered
- On-prem only (system boundary constraint)
- EU AI Act compliance required by August 2026
- Shadow AI exists (HR chatbot, Claims LangChain prototype)
- No unified governance platform

### Status  
❌ Not explicitly answered.

### What Remains Open
- Risk classification (especially claims use case)
- Defined policy owner
- Technical enforcement layer (gateway vs orchestration vs runtime)
- Mandatory human oversight controls

### New Issues Emerging
A. Fragmented AI stack without central enforcement  
B. Compliance deadline without governance architecture  
C. Possible high-risk AI classification (claims)

### Implication for My Role
I cannot design:
- Approval UI flows  
- Explainability components  
- Enforcement checkpoints  

Until governance control points are architecturally defined.

---

# II. Day 11 Question II  
## Could EuroHealth generate defensible traceability within 24 hours?

### What Hans Answered
- Multiple AI systems running independently
- Shadow AI prototypes
- On-prem infrastructure constraint

### Status  
❌ Not answered.

### Likely Reality
They likely cannot:
- Track model versions centrally  
- Capture prompts and tool calls uniformly  
- Reconstruct full decision lineage  

### New Issues Emerging
A. No unified audit trail  
B. Potential regulatory exposure  
C. Observability gaps across AI systems  

### Implication for My Role
Frontend must anticipate:
- Audit dashboards  
- Decision trace views  
- Approval logging  
- Evidence export features  

This is regulatory UX, not optional UI enhancement.

---

# III. Day 11 Question III  
## Which workflows will AI orchestrate, and where must human approvals be enforced?

### What Hans Answered
- AI handles basic helpdesk tickets
- Claims LangChain prototype exists
- HR chatbot exists
- 30% helpdesk cost reduction target

### Status  
🟡 Partially answered.

### What Remains Open
- Automation thresholds  
- Escalation rules  
- Mandatory human checkpoints  
- Risk classification per workflow  

### New Issues Emerging
A. Claims automation may fall under high-risk AI  
B. No defined human-in-the-loop enforcement  
C. Helpdesk resistance risk  

### Implication for My Role
UI must clearly:
- Surface AI suggestions vs autonomous actions  
- Make human approvals explicit  
- Log override decisions  

---

# A. Platform Fragmentation (New Discovery)

- Moveworks  
- ServiceNow AI  
- HR chatbot  
- Claims LangChain prototype  

### Impact
No unified orchestration or governance layer.

### Frontend Implication
Risk of building another disconnected interface instead of a consolidation layer.

---

# B. Knowledge Base (~30% outdated, no owner)

### Impact
- Weak RAG quality  
- Hallucination risk  
- Reduced agent trust  

### Frontend Implication
Must include:
- Source transparency  
- Feedback capture  
- KB issue flagging  

Second-order effect: Poor KB will undermine cost reduction goal.

---

# C. Organizational Resistance (Jan + 12 Agents)

### Impact
Fear of replacement → adoption resistance.

### Frontend Implication
Design must emphasize:
- Co-pilot model  
- Clear human control  
- Correction and override visibility  

Second-order risk: Silent sabotage or fallback to manual work.

---

# D. Budget Constraint (€180K / 6 months)

### Impact
Very tight scope.

### Frontend Implication
Cannot build:
- Fully custom AI console  
- Multiple bespoke interfaces  

Likely focus:
Governance wrapper + observability layer over existing tools.

---

# 1. Stakeholder Analysis (From My Role)

## CIO (Hans)
- Cost reduction (30%)  
- Compliance by 2026  
- Platform consolidation  
- On-prem constraint  

Frontend must demonstrate:
Control, auditability, compliance readiness.

---

## Helpdesk Lead (Jan) + Agents
- Fear of job loss  
- Knowledge holders  
- Adoption gatekeepers  

Frontend must:
- Show AI as assistive  
- Preserve visible human control  
- Capture structured feedback  

---

## Compliance / Legal
- EU AI Act accountability  

Frontend must:
- Display explainability  
- Surface risk classification  
- Enable evidence export  

---

## IT Infrastructure
- On-prem only  
- Likely legacy stack  

Frontend must account for:
- Latency constraints  
- Integration complexity  
- Limited scalability  

---

# 2. Key Findings & Implications for My Workstream

A. Governance undefined → UX risk  
B. Traceability gap → regulatory exposure  
C. Claims use case potentially high-risk  
D. KB quality undermines AI reliability  
E. Adoption risk due to organizational fear  
F. Budget forces prioritization of governance over features  

---

# 3. Technical / Functional Requirements to Investigate

A. Governance  
- Risk classification per use case  
- Policy definition ownership  
- Enforcement layer location  

B. Traceability  
- Prompt logging capability  
- Model version tracking  
- Tool-call capture  
- Audit export requirements  

C. Workflow  
- Top ticket categories  
- Automation thresholds  
- Escalation triggers  

D. UX / Oversight  
- Where human approvals mandatory?  
- Required explanation depth?  
- Confidence display needed?  

E. Data  
- KB ownership assignment  
- Metadata tagging maturity  
- RAG pipeline quality  

---

# 4. Risks Specific to My Area

A. Designing UI before governance defined  
B. High-risk AI classification increasing UX complexity  
C. Adoption resistance from helpdesk  
D. On-prem performance issues reducing trust  
E. KB reliability eroding confidence  

Second-order risk:
If agents distrust AI, 30% cost reduction fails regardless of model quality.

---

# 5. Recommended Next Steps (First 2 Weeks)

## Week 1
A. Governance workshop (risk mapping, control points)  
B. Architecture alignment (gateway vs orchestration)  
C. Logging capability assessment  

## Week 2
D. Ticket category cost analysis  
E. Automation threshold definition  
F. Co-design session with Jan + 2 agents  
G. Knowledge base triage prioritization  

---

# 6. Dependencies on Other Roles

A. AI Architect  
- Enforcement architecture  
- Orchestration design  
- Logging standards  

B. Compliance / Legal  
- Risk classification  
- Explainability requirements  
- Audit format expectations  

C. Data Engineering  
- KB cleanup  
- RAG improvement  
- Metadata standards  

D. Change Management  
- Adoption plan  
- Communication framing  
- Incentive alignment  

---

# Strategic Reflection

Given:
- Governance gaps  
- Fragmented AI landscape  
- Tight budget  
- Compliance deadline  

The realistic MVP may not be expanded AI capability.

It may be:

A unified governance and observability layer that consolidates existing AI systems under enforceable policy, traceability, and visible human oversight.

Without that, cost reduction, compliance, and adoption are all at risk.



-----------------------------------------------------------------------

My #1 finding from Hans: [something NOT in the brief]: 


Top 5 findings:
1. Multiple existing AI interfaces create a fragmented user experience that may require frontend unification or standardized interaction patterns.

2. Undefined human-in-the-loop enforcement points block the design of approval workflows, escalation triggers, and override controls in the UI.

3. The absence of centralized traceability requires the frontend to surface audit visibility, decision lineage, and compliance-relevant metadata.

4. Low knowledge base reliability necessitates source transparency, confidence indicators, and structured feedback capture to preserve user trust.

5. Lack of AI risk classification prevents proper implementation of explainability components, disclaimers, and mandatory control gates.

-----------------------------------------------------------------------

Below finding is from: Beinaz Georgescu-Amet

"
Discovery Insight (AI-FE): Multilingual UX is a Hidden Unification Lever
Hans didn’t emphasize multilingual support emotionally, but EN/DE/CZ is a hard requirement. That’s not just localization — it’s a structural adoption factor.
EuroHealth operates across Germany, Czech Republic, and broader EU contexts. Agents may:
Think in German
Write tickets in English
Use KB articles in Czech
If the UI handles language poorly (English-first, silent translation, no source language visibility), regional friction increases and shadow tools persist.
"

----------------------------------------------------------------------------




# EuroHealth Insurance AG – AI Discovery Report  
**Role:** AI Front End Developer (Kyndryl AI Consulting)  
**Context:** Post-Roleplay Reflection with CIO (Hans Muller)  
**Scope Lens:** Governance, Traceability, Multilingual UX (EN/DE/CZ), On-Prem Constraint  

---

# 1. Stakeholder Analysis (From AI-FE Perspective)

## CIO – Hans Muller

Hans is accountable for reducing remaining helpdesk operating costs by 30% while consolidating Moveworks, ServiceNow AI, and internal LangChain prototypes into a governed on-prem AI platform before EU AI Act enforcement in 2026.

From my AI-FE perspective:  
The interface must visibly demonstrate governance, multilingual consistency (DE/EN/CZ), audit traceability, and human oversight — otherwise consolidation cannot be defended at board or regulator level.

---

## Helpdesk Lead (Jan) + 12 Agents

Jan’s team handles complex, multilingual insurance-related tickets that Moveworks does not resolve and fears expanded AI may eliminate roles.

Agents frequently:
- Think in German,
- Write tickets in English (system standard),
- Use Czech or legacy KB content.

From my AI-FE perspective:  
If the UI defaults to English logic, hides source-language context, or makes overrides cumbersome, agents will revert to manual handling or shadow AI tools.

---

## Compliance / Legal (DE/CZ Regulatory Context)

EuroHealth must prepare for EU AI Act obligations, and claims-related AI decision support could be classified as high-risk AI.

From my AI-FE perspective:  
The UI may need to surface:
- Model/version used,
- Source-language KB retrieval,
- Translation visibility,
- Human approval rationale,
in a format defensible to German and Czech regulators.

---

## AI Architect / Platform Owner

Responsible for consolidating:
- Moveworks,
- ServiceNow AI,
- Claims LangChain prototype,
into a unified on-prem orchestration layer.

From my AI-FE perspective:  
If translation, logging, and enforcement are not standardized at orchestration level, frontend cannot guarantee language integrity or audit visibility.

---

# 2. Key Findings & Implications for My Workstream

## A. No Defined Enforcement Layer for Claims vs Helpdesk

EuroHealth has not defined where human approval is mandatory in insurance claim summarization, coverage eligibility suggestions, or complex policy interpretation.

Implication:  
I cannot design compliant approval UX states without knowing which decision points legally require human confirmation.

Second-order risk:  
Rework if claims become classified as high-risk AI.

---

## B. Traceability Is Fragmented Across AI Systems

Moveworks, ServiceNow, and the LangChain prototype log interactions differently, with no unified visibility of:
- Prompt language,
- Model version,
- Retrieval source,
- Human override rationale.

Implication:  
Frontend may be forced to normalize audit visibility unless backend consolidation occurs.

Second-order risk:  
UI complexity compensates for architectural fragmentation.

---

## C. Multilingual UX Is Structural, Not Cosmetic

EuroHealth operates across DE/EN/CZ contexts without a defined language-handling policy for AI interactions.

Implication:  
If Czech KB articles are silently translated into English UI and approved in German, semantic traceability may be legally ambiguous.

Second-order risk:  
Silent translation breaks audit defensibility and increases shadow AI behavior.

---

## D. 30% Outdated Knowledge Base Directly Impacts Insurance Decision Support

Outdated German or Czech policy interpretations may influence AI suggestions in claims or helpdesk workflows.

Implication:  
UI must display:
- Source language,
- Publication date,
- Confidence indicators,
- Structured feedback capture.

Second-order risk:  
Agents distrust AI and block automation expansion.

---

## E. 30% Cost Reduction Target Depends on Trust, Not Just Automation

Moveworks already handles basic tickets; the remaining cost reduction depends on higher-complexity, multilingual insurance cases.

Implication:  
If multilingual transparency and human oversight UX are weak, agents will not allow AI to handle more complex tickets.

Second-order risk:  
Cost target fails despite technical capability.

---

# 3. Technical / Functional Requirements to Investigate

## Governance & Enforcement
- Where are AI policy rules enforced (gateway, orchestration, runtime)?
- Which insurance workflows require mandatory human approval?
- Is claims AI potentially classified as high-risk?

---

## Traceability
- Are prompts stored pre- and post-translation?
- Is model version exposed per interaction?
- Are tool calls logged centrally?
- Is override reasoning structured and retrievable?

---

## Multilingual Architecture
- Where does translation occur (UI, middleware, model layer)?
- Is original prompt language preserved?
- Are retrieved KB articles tagged with language + jurisdiction?
- What language must audit exports use (DE vs CZ authority)?

---

## Workflow
- Top 5 helpdesk categories driving remaining 30% cost?
- Automation vs suggestion thresholds?
- Escalation triggers for claims-related outputs?

---

## Data Quality
- Who owns KB remediation?
- Are articles tagged by language and freshness?
- Is outdated insurance content programmatically flagged?

---

# 4. Risks Specific to AI Front End

## A. Designing Approval UX Before High-Risk Classification Is Clarified

Could require redesign of explainability and oversight components.

---

## B. Silent Translation Breaking Regulatory Audit Chain

If original language artifacts are not preserved, cross-border claims decisions may lack semantic defensibility.

---

## C. Reinforcing Fragmentation Instead of Enabling Consolidation

Building a separate FE layer for claims instead of integrating into ServiceNow ecosystem undermines unification.

---

## D. Multilingual Friction Increasing Shadow AI

If German and Czech agents distrust translation handling, they may revert to external tools.

---

## E. On-Prem Latency Undermining Trust

Delayed responses in claims assistance or translation may push agents back to manual workflows.

---

## F. Overcompensating in UI for Backend Gaps

Frontend complexity increases if orchestration and logging standards are undefined.

---

# 5. Recommended Next Steps (First 2 Weeks)

## Week 1 – Governance & Language Architecture Alignment

1. Workshop: Map claims vs helpdesk workflows to mandatory human oversight checkpoints.
2. Clarify potential high-risk AI classification for claims support.
3. Map full multilingual lifecycle:
   - Prompt origin language,
   - Retrieval language,
   - Translation layer,
   - Output language,
   - Approval language.
4. Assess current logging capability across Moveworks, ServiceNow, and prototype.

---

## Week 2 – Workflow & UX Grounding

5. Identify top 5 unresolved ticket categories driving cost.
6. Define automation vs suggestion thresholds.
7. Conduct co-design session with:
   - 1 German agent,
   - 1 Czech agent.
8. Prototype:
   - Source language label,
   - Translation toggle,
   - Structured override logging component.

---

# 6. Dependencies on Other Roles (Aligned with AI-FE as Governance Control Surface)

## A. AI Architect (Co-Design Dependency)

- Define enforcement control points.
- Standardize logging schema including:
  - Prompt language,
  - Translation artifacts,
  - Model version,
  - Tool calls,
  - Override metadata.

AI-FE must participate in logging schema design to ensure metadata is usable and visible in UI.

---

## B. Compliance / Legal (Design-Shaping Dependency)

- Confirm high-risk classification for claims AI.
- Define explainability depth requirements.
- Clarify audit export language standards (DE vs CZ).
- Define mandatory human oversight checkpoints.

AI-FE must co-design explainability and approval UX with compliance.

---

## C. Data Engineering (Multilingual & Traceability Dependency)

- Tag KB by language, jurisdiction, freshness.
- Preserve original-language content before translation.
- Expose RAG metadata for UI display.

Without metadata exposure, UI cannot ensure transparency.

---

## D. IT Infrastructure (On-Prem & Translation Dependency)

- Confirm translation service location.
- Define performance SLAs.
- Ensure storage for multilingual audit logs.

Frontend streaming and fallback UX depend on these constraints.

---

## E. Change Management (Adoption-Critical Dependency)

- Define positioning of AI as augmentation.
- Align microcopy with regional language expectations.
- Assign ownership for KB correction loops.

Frontend trust signals must align with organizational messaging.

---

# Strategic Positioning

At EuroHealth, AI Front End is not a presentation layer.

It is:
- A governance surface,
- A multilingual integrity layer,
- A human-oversight control interface,
- A unification lever across fragmented AI systems.

If frontend is excluded from early architectural decisions, governance may exist in logs but not in behavior — and adoption, compliance, and cost targets will fail.
