# AI SECURITY DISCOVERY REPORT  
**Client:** EuroHealth Insurance AG  
**Prepared by:** AI Security Consultant – Kyndryl  
**Engagement Type:** AI Industrialization & Governance (Not a Chatbot Build)

---

# 1. Executive Diagnosis – What This Engagement Really Is

EuroHealth does not have an AI capability gap.

They have:

- Multiple AI systems operating without a shared control layer  
- No authoritative inventory of AI systems  
- No unified audit trail  
- No clear EU AI Act risk classification  
- No owner for knowledge integrity  

The CIO’s stated objectives:

- 30% additional helpdesk cost reduction  
- Unified AI platform  
- EU AI Act readiness by August 2026  
- Delivery within 6 months and €180K  

The underlying tension:

> The faster AI autonomy expands, the higher the regulatory and operational exposure — and today that exposure is not measurable.

This is not a chatbot optimization engagement.  
This is the construction of EuroHealth’s AI control plane.

---

# 2. Confirmed Findings vs. Open Questions

## Confirmed During Discovery

- Moveworks handles L1 tickets autonomously.
- HR built a chatbot outside central governance.
- Claims runs a LangChain prototype without approval.
- No unified governance model exists.
- On-prem only architecture (non-negotiable).
- Knowledge base is ~30% outdated with no clear owner.
- Helpdesk team fears displacement.
- Budget and timeline are tight.

## Critical Gaps Still Open

- Can EuroHealth list every AI system currently operating?
- Which use cases qualify as High-Risk under the EU AI Act?
- Can any AI-assisted decision be reconstructed end-to-end?
- Are AI logs centralized or siloed within tools?
- What specific data is exposed to LLMs?
- How long does it take to technically enforce a new compliance rule?

These are material risks, not administrative gaps.

---

# 3. EU AI Act Risk Classification – Likely High-Risk Exposure

EuroHealth operates in insurance. If AI:

- Assists claims processing,
- Influences HR decisions,
- Impacts customer entitlements,

Then parts of the system are likely **High-Risk AI Systems** under the EU AI Act.

High-risk classification requires:

- Risk management framework  
- Technical documentation  
- Logging and traceability  
- Human oversight  
- Data governance controls  
- Accuracy and robustness testing  

Currently, EuroHealth cannot demonstrate:

- Complete AI inventory  
- Risk-tiered classification  
- Centralized logging  

EU AI Act readiness is therefore an architectural issue, not a documentation exercise.

---

# 4. PII Handling – Structural Exposure

The statement “No PII in training data” is insufficient.

Risk surface includes:

- Ticket content containing PII  
- Prompts containing PII  
- Retrieved KB documents containing PII  
- Audit logs storing prompts and outputs  

If audit logs retain raw prompts, a secondary regulated PII dataset is created.

Employee directory access remains undefined:

- Should LLMs access the full directory?
- Should lookups be tool-based instead of retrieval-based?
- Should attributes be tokenized or restricted?
- Should certain fields be excluded entirely?

Without a defined exclusion and minimization strategy, compliance risk increases significantly.

---

# 5. On-Prem Constraint – Architectural Trade-Off

On-prem only significantly narrows implementation choices.

Implications:

- Local model hosting  
- Local vector databases  
- Local logging and telemetry  
- No reliance on SaaS AI governance platforms  

Within €180K and 6 months, this requires strict prioritization.

The scope must focus on regulatory defensibility, not feature expansion.

---

# 6. LLM Prompt Injection – Current Blind Spot

There is no evidence that prompt injection risks are currently mitigated.

Given:

- RAG over knowledge base  
- Departmental prototypes  
- Increasing autonomy  

Likely vulnerabilities:

- Malicious ticket content  
- Poisoned KB documents  
- Tool invocation manipulation  
- Data exfiltration through retrieval  

If autonomy expands without:

- Tool allowlists  
- Context isolation  
- Output validation  
- Anomaly detection  

Then cost optimization increases systemic risk.

Centralization increases blast radius.

---

# 7. Access Control – Cross-Department Risk

If AI is unified under one platform:

- Can HR access Claims data?
- Can Claims query employee data?
- Can Moveworks access cross-department records?
- Who can modify prompts or policies?

Without strict segmentation and role-based enforcement, a single misconfiguration could expose sensitive information across departments.

Industrialization requires:

- Role-based data scoping  
- Tool-level allowlists  
- Departmental boundaries  
- Clear ownership per AI system  

---

# 8. Knowledge Base Integrity – Operational Multiplier

The knowledge base is ~30% outdated with no ownership.

If autonomy increases before KB governance improves:

AI will scale outdated procedures faster than any human process.

Potential impact:

- Incorrect resolutions  
- Policy violations  
- Security misconfigurations  
- Loss of trust in AI systems  

Knowledge governance is a safety control, not a documentation task.

---

# 9. Stakeholder Dynamics

## CIO (Hans Muller)

- Under board pressure to demonstrate AI ROI.
- Focused on cost reduction and consolidation.
- Likely underestimates regulatory documentation complexity.

## CISO (Stefan Weber)

- Concerned about shadow AI and governance gaps.
- Key ally for enforceable controls.
- Can mandate security baseline if aligned early.

## Helpdesk Lead (Jan)

- Team fears replacement.
- Risk of passive resistance.
- Human-in-the-loop design must reinforce team relevance.

## Department Heads (HR / Claims)

- Built shadow AI due to speed constraints.
- Will bypass governance if it adds friction.

## Works Council

- Logging and monitoring must consider employee privacy concerns.

---

# 10. Timeline Realism

Six months is sufficient to deliver:

- AI registry
- EU AI Act risk pre-classification
- Audit schema definition
- Baseline policy enforcement
- Threat model definition
- Logging standardization

Six months is not sufficient for:

- Full enterprise agentic redesign
- Deep KB remediation
- Full cultural transformation
- Mature continuous AI monitoring

Scope must prioritize regulatory defensibility over feature growth.

---

# 11. Explicit Risk Register (AI Security)

1. High-risk AI systems operating without classification.
2. Inability to reconstruct AI-assisted decisions.
3. Audit logs becoming uncontrolled PII repositories.
4. Prompt injection vulnerabilities in RAG workflows.
5. Cross-department data exposure after centralization.
6. Shadow AI persistence due to governance friction.
7. Knowledge base corruption scaling via automation.
8. Budget insufficient for full platform ambition.

---

# 12. Immediate Priorities – First 2 Weeks

1. AI Landscape Mapping Workshop  
   Deliverable: AI Registry v0  

2. EU AI Act Risk Pre-Classification  
   Identify likely High-Risk systems  

3. Define Audit Log Standard  
   Required fields, retention, redaction, access controls  

4. Draft LLM Threat Model  
   Prompt injection, data exfiltration, tool misuse  

5. Define Minimal AI Security Control Baseline  
   Controls required before autonomy expands  

---

# Final Conclusion

EuroHealth’s challenge is not AI capability.

It is governance velocity.

To meet the August 2026 board review, the organization must be able to answer at any time:

- What AI systems are running?
- What risk class are they?
- What data do they access?
- How was a specific decision made?
- Which policy was applied?
- Who approved it?

Today, they cannot.

That gap defines the business case for industrialization.