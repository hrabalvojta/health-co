AI Security Consultant – Discovery Report 
Client: EuroHealth Insurance AG
Date: 24 Feb 2026
Role: AI Security Consultant, Kyndryl AI Team
Context: CIO Meeting (Hans Müller) + Client Brief

1. Day 11 AISEC Discovery Questions (Top 4)
Q1. What AIrelated security policies exist today (PII, retention, access, acceptable use, vendor onboarding), and are they systemenforced or only documented?
Q2. What technical controls protect current AI deployments (DLP, prompt filtering, allowlists, model gateways, secrets management, segmentation, PAM)?
Q3. What AI systems—official and shadow—are running today, who owns them, and what sensitive data do they access?
Q4. What audit evidence and governance artifacts must EuroHealth produce for EU AI Act readiness by August 2026?

2. What Hans Answered vs. Remaining Gaps
✔ Answered
• Several shadow AI tools exist (HR bot, Claims LangChain).
• Moveworks/SNOW is already covering basic helpdesk tasks.
• Onprem only, strict “no cloud.”
• KB ~30% outdated; no clear owner.
• EU AI Act compliance target: Aug 2026.
• Helpdesk fears job loss.
• Tight budget: €180K / 6 months.
❌ Still Open
• No detail on existing AI governance policies (PII, retention, acceptable use, approvals).
• No evidence of technical guardrails (DLP, filtering, PAM, segmentation).
• No audit trail specifications.
• No risk classification under EU AI Act.
• No clarity on access boundaries (ticket visibility, HR vs Claims segregation).
⚠ New Issues Identified
• Shadow AI more extensive than expected.
• Outdated KB is now a security liability, not just operational.
• Governance must be centralized — not a chatbot project.
• Workers’ fear → accelerates shadow AI creation.

3. Stakeholder Analysis (AISecurity Perspective)
CIO – Hans Müller
• Focus: Compliance, cost reduction, platform unification.
• Risk: Underestimates governance and technical debt.
Compliance & Legal
• Focus: EU AI Act obligations.
• Risk: Not yet aware of shadow AI exposure; no risk classification.
Claims Department
• Focus: Faster claims triage.
• Risk: Claims model likely HighRisk AI → strict oversight required.
HR
• Focus: Chatbot prototypes & automation.
• Risk: Handling employee data → PII requirements and directory exclusion mandatory.
IT Infra
• Focus: Onprem enforcement, minimal change.
• Risk: Onprem guardrails must be selfbuilt; higher complexity.
Helpdesk Team
• Focus: Job security.
• Risk: May circumvent controls if automation threatens roles.

4. Key Findings & Implications (AISecurity)

Finding 1 — Shadow AI is widespread and ungoverned
HR chatbot, Claims LangChain prototype, and Moveworks AI operate with:
• No risk assessments
• No audit logs
• Unknown access levels
• No record of data flows
Implication:
Security posture cannot be validated → high regulatory exposure.

Finding 2 — EU AI Act HighRisk Classification Required
Claims adjudication and HR actions fall under:
• HighRisk AI (automated decisions, employment, benefits)
• Requires: 
o Documentation
o Logging
o Human oversight
o Traceability
o Testing
o Evidence of risk controls
Implication:
EuroHealth has zero of these in place today.

Finding 3 — PII Handling & Employee Directory Exclusion Not Defined
“No PII in training” is stated, but:
• Embeddings, logs, and prompts likely include PII.
• HR tools may unintentionally ingest directory or claims data.
Implication:
You need a PII exclusion strategy:
• filtering
• context allowlisting
• prompt sanitization
• vector store encryption
• dedicated HR vs non-HR model contexts

Finding 4 — No Technical Guardrails (DLP, Gateway, Filtering, Segmentation)
Hans confirmed: “No governance.”
We assume no:
• DLP
• Prompt filtering
• Allowlist/denylist
• Secrets vault
• Segmented networks
• PAM
• Model gateway
Implication:
High likelihood of:
• prompt injection
• data leakage
• unauthorized access
• uncontrolled model evolution

Finding 5 — No Audit Trail Despite OnPrem Residency Constraint
Audit trail must cover:
• prompts
• responses
• model version
• training data lineage
• humanintheloop confirmation
• approval history
Implication:
EU AI Act readiness impossible until logging is standardized.

Finding 6 — Access Control Gaps (Ticket Visibility & Agent Privilege)
No clarity on:
• Which agents can see which ticket types
• Whether HR data is segregated from IT tickets
• Service account governance
• Whether shadow bots use admin credentials
Implication:
High risk of unauthorized access to claims notes or employee data.

Finding 7 — Stale Knowledge Base = Integrity Risk
30% outdated → models hallucinate or give wrong guidance.
Implication:
This is both a security and compliance risk.

5. Technical & Functional Requirements to Investigate Further
EU AI Act Compliance
• Classify all AI systems into risk categories.
• Define mandatory evidence (logs, documentation, HITL, approvals).
• Build policyascode enforcement pipeline.
PII & Sensitive Data Controls
• Employee directory exclusion strategy.
• PII stripping/obfuscation during inference.
• Vector store encryption + retention rules.
Prompt Injection Threat Model
Must include:
• Direct injection
• Indirect (documentborne) injection
• Retrieval poisoning
• Crosstenant contamination
• Output manipulation
Controls required:
• templatebased prompting
• context allowlisting
• inbound/outbound filters
• “safe prompt” enforcement
• model gateway
Access Control
• RBAC per ticket category (IT, HR, Claims).
• Service accounts with least privilege.
• JIT access for administrative tasks.
• Segmentation of Claims vs HR vs IT LLM contexts.
Audit & Logging
• Centralized onprem log pipeline
• Prompt/response logging
• Traceability: inputs → model → outcome
• HITL approval logging
• Immutable storage (WORM) for audit records

6. Risks Specific to AISecurity
1. Regulatory NonCompliance (High Impact)
Highrisk workflows without:
• oversight
• documentation
• testing
• logs
→ failure to meet EU AI Act by Aug 2026.
2. Data Leakage (High Likelihood)
Shadow tools with unfiltered prompts could leak:
• claims data
• employee directory
• medical notes
3. Prompt Injection Exposure
Without filtering:
• users can alter agent behavior
• model can leak memory/context
• claims decisions could be manipulated
4. Overprivileged / Shared Credentials
Shadow bots may use admin tokens.
Blast radius extremely high.
5. Stale KB → Integrity & Safety Failure
Models give incorrect answers → causes financial & operational harm.
6. People Risk → Shadow AI Growth
Helpdesk fears displacement → more unsanctioned tools appear.

7. Recommended Next Steps (First 2 Weeks)
Week 1 — Stabilize and Discover Reality
1. Shadow AI Inventory (tools, owners, data, infra).
2. Audit trail gap analysis.
3. Data flow mapping (HR, Claims, IT).
4. PII exposure test (prompts, logs, embeddings).
5. Segmentation & identity review.
Week 2 — Minimum Viable Governance (MVG)
1. EU AI Act risk classification & evidence requirements.
2. PolicyasCode baseline (access rules, approvals).
3. PII exclusion & sanitization pipeline design.
4. Prompt injection threat model + mitigations.
5. Draft onprem model gateway architecture.
6. Define HITL checkpoints for claims & HR.

8. Dependencies on Other Roles
• AI-PM: Prioritization & stakeholder alignment.
• AI-FDE: Model gateway, segmentation, logging infra.
• AI-SE: CI/CD guardrails, model registry, deployment controls.
• AI-DS: KB quality, evaluation metrics, testing protocol.
• AI-DA: Compliance dashboards & audit evidence.
• Change / HR: Workforce impact mitigation (reduce shadow AI incentives).

