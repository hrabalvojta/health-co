# Discovery Packet v1 — AI-SE
## Student: Daniel Kupcik
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: Where are the limits of your current ServiceNow/Moveworks deployment?
**Why this matters:** Moveworks excels at automating structured IT and HR tickets but often needs custom configuration and vendor support to cover finance, claims or other domains:contentReference[oaicite:0]{index=0}. Understanding what the client cannot automate or govern today reveals gaps for our agentic platform.  
**Red flag (bad answer):** If the CIO says Moveworks covers every department or that they do not encounter governance limitations, it suggests undiscovered shadow AI and unrealistic expectations.  
**KAF component:** Core / Interop

### Question 2: Can you provide a complete inventory of AI systems in use or planned across your organization, and what governance or audit controls each has?
**Why this matters:** EuroHealth currently lacks a formal AI registry, with shadow AI in HR, claims and finance and only partial audit trails in ServiceNow:contentReference[oaicite:1]{index=1}. We need to know where AI lives to unify governance and eliminate unapproved tools.  
**Red flag (bad answer):** The CIO cannot list all AI applications or admits that some teams use unapproved tools; this signals high risk and missing governance.  
**KAF component:** Core / Run Safe / Ingestion

### Question 3: Which regulatory and internal policies must your AI solutions comply with, and which should be codified into Policy-as-Code rules?
**Why this matters:** The EU AI Act requires risk management, high-quality datasets, logging and human oversight:contentReference[oaicite:2]{index=2}; PaC converts such obligations into machine-readable rules, delivering automation, consistency and auditability:contentReference[oaicite:3]{index=3}.  
**Red flag (bad answer):** Policies exist only in documents or legal memos; there is no plan to express them in code, meaning manual enforcement and high compliance risk.  
**KAF component:** Policy-as-Code / Run Safe

### Question 4: When regulations or internal policies change, how quickly can you adapt AI models and workflows, and what is your target adaptation time?
**Why this matters:** EuroHealth currently updates processes roughly every three months:contentReference[oaicite:4]{index=4}, yet EU AI Act obligations apply by Aug 2026/2027:contentReference[oaicite:5]{index=5} and the board wants a governance framework by Q3 2026. PaC and automated pipelines can reduce adaptation from months to days:contentReference[oaicite:6]{index=6}.  
**Red flag (bad answer):** Model and workflow updates take months, rely on manual approvals or vendor intervention, or there is no defined process; this shows poor operational maturity.  
**KAF component:** Policy-as-Code / Core

### Question 5: How do you ingest and cleanse training and inference data to exclude PII and ensure quality across eight countries?
**Why this matters:** The AI Act requires high-quality datasets and logging:contentReference[oaicite:7]{index=7}, and EuroHealth prohibits employee PII in training. A robust ingestion pipeline is necessary to enforce these constraints and maintain data lineage.  
**Red flag (bad answer):** Data is cleansed manually with no automated checks for PII, there is no lineage tracking, or they cannot describe where data comes from; this raises compliance and bias risks.  
**KAF component:** Ingestion / Run Safe

### Question 6: For typical helpdesk and IT operations workflows, what are the multi-step tasks you expect an AI agent to perform, and which systems (e.g., monitoring tools, backup, HR) must it integrate with?
**Why this matters:** Moveworks automates IT helpdesk tasks but cross-department workflows will require additional connectors to legacy monitoring tools, backup systems and other applications:contentReference[oaicite:8]{index=8}. Understanding required steps and integrations ensures the agent’s plan covers the whole process.  
**Red flag (bad answer):** The CIO cannot articulate the workflow steps or assumes connectors exist for everything; this indicates hidden manual tasks and integration gaps.  
**KAF component:** Interop / Core

### Question 7: What level of audit trail, logging and monitoring do you require for AI decisions, and how do you currently achieve it?
**Why this matters:** High-risk AI systems must log activities and provide traceability:contentReference[oaicite:9]{index=9}. EuroHealth’s audit trail is currently limited to ServiceNow, leaving other AI tools unlogged:contentReference[oaicite:10]{index=10}. Clear requirements guide our monitoring and digital trust design.  
**Red flag (bad answer):** They rely on generic infrastructure logs or cannot reconstruct AI decisions; or only ServiceNow logs are kept, meaning incomplete audit trails.  
**KAF component:** Run Safe / Digital Trust

### Question 8: Which decisions or tasks require human-in-the-loop checkpoints, and where would these human approvals occur within workflows?
**Why this matters:** The AI Act mandates appropriate human oversight:contentReference[oaicite:11]{index=11}. Defining HITL points (e.g., claim approval, high-value transactions) balances automation and compliance.  
**Red flag (bad answer):** The CIO wants to remove human approval entirely, risking non-compliance, or inserts humans at every step, undermining automation; both signal misunderstanding of HITL.  
**KAF component:** HITL / Run Safe

### Question 9: What does your deployment pipeline look like for AI models and agents (CI/CD, testing, rollback and monitoring for drift)?
**Why this matters:** PaC encourages shift-left governance by embedding checks into CI/CD pipelines:contentReference[oaicite:12]{index=12}. A mature pipeline ensures version control, automated testing, drift monitoring and rollbacks, all critical for safe on-prem deployment.  
**Red flag (bad answer):** Deployments are manual, there is no version control or testing, and model drift is not monitored; this indicates low operational maturity and compliance risk.  
**KAF component:** Core / Run Safe

### Question 10: Beyond the IT helpdesk, what are your priorities and success metrics for extending agentic AI to HR, claims and finance, and how will you handle multi-language support and cross-country requirements?
**Why this matters:** EuroHealth serves 3,000 employees across eight EU countries with multiple languages, and plans to expand beyond the IT department in later phases:contentReference[oaicite:13]{index=13}. Understanding metrics (e.g., CSAT target ≥ 4.2) and constraints guides scalable architecture design.  
**Red flag (bad answer):** The CIO lacks a clear vision for scaling, or assumes one metric (e.g., ticket deflection) suffices; they overlook language requirements and cross-country differences.  
**KAF component:** Core / Interop / Ingestion

---

## Part 2: KAF Mapping (mini)
| KAF Component      | Covered by Q#                          | Notes                                                     |
|--------------------|----------------------------------------|-----------------------------------------------------------|
| Agentic Core       | Q1, Q2, Q4, Q6, Q9, Q10                | Assess current capabilities, scaling limitations and CI/CD maturity. |
| Agentic Ingestion  | Q2, Q5, Q10                            | Explore data ingestion pipelines, PII exclusion and cross-country data issues. |
| Policy-as-Code     | Q3, Q4, Q9                            | Identify policies to codify and readiness to embed governance in pipelines. |
| Digital Trust      | Q7                                    | Focus on audit trail, logging and monitoring requirements. |
| Human-in-the-Loop  | Q8                                    | Define human oversight checkpoints for high-risk decisions. |
| Interop (MCP/A2A)   | Q1, Q6, Q10                           | Identify integration gaps and required connectors across ServiceNow, monitoring, backup and future departments. |

---

## Part 3: Assumptions / Risks / Open Items (3–5)
1. **Assumption:** ServiceNow and Moveworks license terms permit the integration of custom agents and third-party connectors within the on-prem environment.  
   **Risk:** If licensing or API restrictions prevent integration, additional tools or license upgrades may be needed.  
2. **Assumption:** Data from HR, claims and finance can be centrally governed and accessed for training without violating GDPR or national regulations.  
   **Risk:** Cross-border data transfer restrictions or differing local policies may complicate ingestion pipelines; we may need localized PaC rules.  
3. **Assumption:** EuroHealth’s IT team has some CI/CD infrastructure for applications that can be extended to AI models.  
   **Risk:** If no existing pipeline exists, building one may exceed the six-month timeline and budget.  
4. **Open item:** Confirm the availability of MCP (Managed Connector Platform) connectors for legacy monitoring tools and backup systems; custom connector development may be required.  
5. **Open item:** Determine which internal policies beyond the EU AI Act (e.g., corporate ethics, ESG goals) must be encoded in policy-as-code.  

---

## Part 4: What We Will Measure (3 KPI proposals)
1. **Ticket deflection rate (L1):** Target a 50 % or higher deflection rate for IT helpdesk requests in Phase 1, up from the current ~35 %:contentReference[oaicite:14]{index=14}.  
2. **Regulatory adaptation time:** Reduce time to update AI processes after a policy change from ~3 months to under 2 weeks, aligning with the board’s success criteria:contentReference[oaicite:15]{index=15}.  
3. **Customer satisfaction (CSAT) improvement:** Increase CSAT scores for IT support from 3.6/5 to at least 4.2/5 in Phase 1:contentReference[oaicite:16]{index=16}.  

---

## Part 5: Agent Classification
- **Governance tier:** **Enterprise** — the agent will orchestrate cross-departmental workflows and must comply with high-risk AI regulations (EU AI Act), requiring enterprise-level governance and registry.  
- **Registry/reuse potential:** The agent will be registered in Kyndryl’s internal AI registry as a reusable pattern for regulated industries. Its policy-as-code guardrails and on-prem deployment model can be templated for other healthcare and insurance clients.  

---

## Dependencies on Other Roles:
- **Data Engineer:** To assess data quality, build ingestion pipelines and implement PII scrubbing across eight countries.  
- **AI Governance/Legal SME:** To interpret EU AI Act obligations, create policy-as-code rules and conduct risk assessments.  
- **Business Analyst (HR/Claims/Finance):** To map departmental workflows, define success metrics and identify HITL checkpoints.  
- **Identity & Access Management (IAM) Engineer:** To ensure connectors authenticate securely and enforce least privilege.  

## Questions I Deliberately Did NOT Ask (and why):
- **Detailed licensing or procurement questions:** These fall under the responsibility of vendor management and legal teams, not the AI-SE.  
- **End-user training plans:** While important, training design is typically led by change management specialists and adoption leads.  
- **User interface/UX details:** As an AI-SE I focus on backend deployment, CI/CD and governance; UI decisions are better handled by UX designers and product owners.  