# Discovery Packet v1 — AI-SEC
## Student: Branislav Petrík
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: From your perspective, what is the **business outcome** of “industrializing AI” in the next 6 months—and what would make you say this program *failed*?
**Why this matters:** Aligns on CIO-level success criteria (risk reduction + scale + time-to-compliance) so we don’t drift into feature work. It also helps scope what fits a €180K / 6-month runway.  
**Red flag (bad answer):** “We just want ‘more AI’ everywhere” or “Build us a chatbot.”  
**KAF component:** Core

### Question 2: Today, where does ServiceNow/Moveworks stop being enough—what **enterprise gaps** block you from scaling AI beyond isolated teams (governance, compliance evidence, operating model, integration constraints)?
**Why this matters:** Forces clarity on what they can’t do with the current platform alone—especially cross-department governance and production operations.  
**Red flag (bad answer):** “It’s mostly a licensing issue” or “We haven’t tried outside IT yet.”  
**KAF component:** Core

### Question 3: Who has **single-point accountability** for AI risk and compliance today (CIO, CISO, Risk, DPO, Legal), and what is the **decision path** when business wants speed but controls say “no”?
**Why this matters:** EU AI Act readiness and security posture depend on clear ownership and escalation. Without a decision path, controls will be bypassed or projects will stall.  
**Red flag (bad answer):** “No one owns it end-to-end” or “Each department decides for themselves.”  
**KAF component:** Run Safe

### Question 4: For Q3 2026 “governance-ready,” which AI guardrails must be **centrally enforced across the enterprise** (not left to local interpretation) — and who can **approve changes** to those guardrails within days?
**Why this matters:** This is Policy-as-Code at CIO altitude: what becomes enterprise-standard enforcement and how quickly it can evolve. It also reveals whether “days vs months” change agility is feasible.  
**Red flag (bad answer):** “We’ll define it later” or “Changes go through quarterly committees.”  
**KAF component:** Policy-as-Code

### Question 5: If we implement only **five ‘stop-the-line’ controls** in the next 6 months, which would you pick (e.g., on-prem only, no PII in training, mandatory trace logging, approval gates for high-impact actions, connector/tool allow-list)?
**Why this matters:** Converts broad compliance intent into a prioritized, fundable control set that can be encoded and audited. Helps fit the budget and timeline while reducing the biggest risks first.  
**Red flag (bad answer):** “No hard stops—just guidelines” or “We can’t prioritize controls.”  
**KAF component:** Policy-as-Code

### Question 6: What level of **audit evidence** do you need to confidently face regulators/board: traceability of model/tool/version, who approved what, what data was accessed, and how long evidence is retained?
**Why this matters:** Defines the audit trail and retention requirements that the entire operating model must produce, not just ServiceNow ticket history.  
**Red flag (bad answer):** “Logs are optional” or “We’ll figure evidence out during the audit.”  
**KAF component:** Run Safe

### Question 7: What are the **highest-impact decisions** you will *not* allow automation to make without explicit human confirmation (claims outcomes, access grants, policy exceptions, customer communications, data exports)?
**Why this matters:** Establishes Human-in-the-Loop boundaries for high-risk actions and prevents “agent drift” into prohibited territory. Also clarifies what “safe automation” means to leadership.  
**Red flag (bad answer):** “We want it fully autonomous end-to-end to maximize ROI.”  
**KAF component:** HITL

### Question 8: Given the on-prem constraint, what is your required **security posture** for AI runtime: identity/SSO, least-privilege access, network segmentation, secrets management, and outbound egress rules?
**Why this matters:** On-prem does not automatically mean secure. This question surfaces the non-negotiable enterprise security baseline needed before any agent can safely call tools or access systems.  
**Red flag (bad answer):** “If it’s inside the network, it’s fine” or “We don’t have egress controls.”  
**KAF component:** Run Safe

### Question 9: Which **systems and workflows** must be connected to realize value beyond ServiceNow (claims, policy admin, IAM, CMDB, monitoring, document stores), and do you have a standard approach for **MCP/A2A connectors** (allow-list, authZ model, logging, lifecycle)?
**Why this matters:** Scaling AI is fundamentally an interoperability problem: tool access, authorization, and connector governance determine feasibility and risk more than the model choice.  
**Red flag (bad answer):** “Teams can build connectors however they want” or “No standard for tool access.”  
**KAF component:** Interop

### Question 10: How do you prevent “no PII in training data” from becoming a paper rule—what is your stance on **retrieval-only patterns**, redaction/minimization, DLP enforcement, exception handling, and retention?
**Why this matters:** “No PII” is enforceable only through data handling controls and patterns. This question clarifies what approaches are acceptable and what enforcement is required.  
**Red flag (bad answer):** “We’ll rely on users not to include PII” or “We’ll anonymize later.”  
**KAF component:** Ingestion

> Minimum coverage: at least 2 questions on Policy-as-Code,
> at least 1 on MCP/A2A interoperability,
> at least 1 on Human-in-the-loop checkpoints.

---

## Part 2: KAF Mapping (mini)
| KAF Component      | Covered by Q#     | Notes                                                                 |
|---------------------|-------------------|-----------------------------------------------------------------------|
| Agentic Core        | 1, 2              | Outcome + gaps beyond ServiceNow/Moveworks; avoids “chatbot drift.”   |
| Agentic Ingestion   | 10                | Enforceable “no PII” patterns, DLP, exceptions, retention.            |
| Policy-as-Code      | 4, 5              | Enterprise guardrails + prioritised stop-the-line controls.           |
| Digital Trust       | 3, 6, 8           | Ownership/decision path + audit evidence + security baseline.         |
| Human-in-the-Loop   | 7                 | Explicit boundaries and approval gates for high-impact actions.       |
| Interop (MCP/A2A)   | 9                 | Connector governance, authZ model, logging and lifecycle standards.   |

---

## Part 3: Assumptions / Risks / Open Items (3-5)
1. **Assumption:** EuroHealth wants enterprise standards (not a single-team pilot) and will empower a central owner/RACI for enforcement.  
2. **Risk:** “No PII in training data” may conflict with business expectations unless retrieval-only and strong minimization/redaction patterns are formally accepted.  
3. **Risk:** Audit evidence requirements (trace + retention) may exceed current logging maturity, increasing scope if not prioritized early.  
4. **Open item:** Exact EU AI Act scope (which systems are “high-risk,” roles as provider/deployer) and how that translates into internal control tiers.  
5. **Open item:** Tool/connector governance model (who approves connectors, what’s the allow-list process, how exceptions are handled).

---

## Part 4: What We Will Measure (3 KPI proposals)
1. **Policy change-to-enforcement lead time:** target **≤ 10 business days** from approval to enforced control in production.  
2. **Audit trace completeness:** target **≥ 95%** of AI-assisted actions produce complete trace evidence (actor, model/tool/version, data access, outcome, approvals).  
3. **HITL compliance rate for high-impact actions:** target **100%** of defined high-impact actions gated with human approval and recorded rationale.

---

## Part 5: Agent Classification
- **Governance tier:** Enterprise  
- **Registry/reuse potential:** Register as an “Enterprise AI Controls & RunSafe Pattern” reusable across departments: control library (policy-as-code), connector governance standard (MCP/A2A), and audit evidence blueprint that Kyndryl can apply across regulated clients.

---

## Dependencies on Other Roles:
- I need **AI-PM** to ask about business priorities, stakeholder map, governance cadence, and what decisions the CIO can sponsor to unblock change velocity.  
- I need **AI-SE** to ask about deployment pipelines, runtime monitoring stack, alerting/on-call model, and rollback strategy for controls and connectors.  
- I need **FDE** to ask about on-prem hosting constraints, network zones, identity integration, and integration architecture for critical systems.  
- I need **AI-DS** to ask about knowledge sources, retrieval strategy, evaluation sets that avoid PII, and quality gates for content ingestion.  
- I need **AI-DA** to ask about reporting requirements for board/regulators and dashboards for control compliance + operational health.

## Questions I Deliberately Did NOT Ask (and why):
- “Which exact model/vendor should we choose?” — because model choice is downstream of governance, on-prem constraints, and control requirements (FDE/AI-SE).  
- “What should the UI/UX look like?” — because this program is not chatbot-first and UI decisions are **AI-FE** territory.  
- “What’s the detailed data taxonomy for every department?” — because deep content structure is **AI-DS** territory and should follow the agreed retrieval + PII controls.