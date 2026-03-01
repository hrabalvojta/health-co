Discovery Packet v1 — AI Product Manager
Student: Petra Dosbabová
Date: February 24, 2026
Client: EuroHealth Insurance AG
________________________________________
Part 1: Discovery Questions (10)
Question 1: Where do ServiceNow and Moveworks fall short for enterprise-wide governance, compliance, and multi-department scaling?
Why this matters: Identifies gaps we must solve beyond chatbot functionality; surfaces governance and scaling blockers.
Red flag: “ServiceNow should handle everything.”
KAF component: Core
________________________________________
Question 2: Which regulatory or internal policies must be enforced automatically in code rather than documented or trained?
Why this matters: Determines Policy as Code scope for compliance automation.
Red flag: “We don’t have defined enforceable rules.”
KAF component: Policy-as-Code
________________________________________
Question 3: How long does it take today to update workflows when regulations or internal policies change?
Why this matters: Reveals operational agility and EU AI Act readiness.
Red flag: “It takes several months.”
KAF component: Run Safe
________________________________________
Question 4: How should AI agents interoperate with your existing systems—specifically via MCP connectors or agent-to-agent (A2A) communication—to support end-to-end automation beyond ServiceNow?
Why this matters: Clarifies interoperability architecture and MCP/A2A connector requirements.
Red flag: “We only need integration with ServiceNow.”
KAF component: Interop (MCP/A2A)
________________________________________
Question 5: What level of auditability do Risk/Compliance require: event logs, reasoning trails, or full decision lineage?
Why this matters: Ensures we meet traceability and audit obligations for a regulated environment.
Red flag: “Standard logs should be enough.”
KAF component: Run Safe
________________________________________
Question 6: What actions should the agent be allowed to execute autonomously, and where must its autonomy be constrained?
Why this matters: Defines agent boundaries, risk controls, and governance tiering.
Red flag: “Let it handle anything automatically.”
KAF component: Core
________________________________________
Question 7: Where must human approvals or verifications occur before an AI agent proceeds with an action?
Why this matters: Establishes mandatory HITL checkpoints for regulated or high impact workflows.
Red flag: “We want zero human approvals.”
KAF component: HITL
________________________________________
Question 8: How is non PII operational and knowledge data structured, governed, and validated today—especially data used for grounding and retrieval?
Why this matters: Determines ingestion readiness and the quality of the foundation we can build on.
Red flag: “We don’t have a consistent KB structure.”
KAF component: Ingestion
________________________________________
Question 9: What AI specific security constraints must the solution meet beyond ‘no PII in training’—model isolation, on prem boundaries, threat patterns?
Why this matters: Defines security posture for on prem LLMs and agentic workflows.
Red flag: “Same as any other system.”
KAF component: Run Safe
________________________________________
Question 10: Which business outcomes must this AI industrialization deliver within the 6 month, €180K scope?
Why this matters: Ensures that industrialization effort is directly tied to measurable financial impact rather than feature expansion.
Red flag: “We want everything improved.”
KAF component: Core
________________________________________
Minimum coverage check:
✓ Policy-as-Code: Q2, Q3, Q5
✓ MCP/A2A interoperability: Q4
✓ Human-in-the-loop: Q7
________________________________________
Part 2: KAF Mapping (mini)
KAF Component	Covered by Q#	Notes
Agentic Core	Q1, Q6, Q10	Governance boundaries, scope, value alignment
Agentic Ingestion	Q8	Data structure, KB governance
Policy-as-Code	Q2, Q3, Q5	Regulatory automation, enforceable rules
Digital Trust / Run Safe	Q3, Q5, Q9, Q10	Audit, monitoring, compliance, safety
Human-in-the-Loop	Q7	Mandatory approvals
Interop (MCP/A2A)	Q4	Cross-system orchestration
________________________________________
Part 3: Assumptions / Risks / Open Items
1.	Shadow AI usage is broader than formally declared.
2.	Audit trails outside ServiceNow are inconsistent or unavailable.
3.	Regulatory updates rely heavily on manual workflows.
4.	On prem constraints may slow deployment of new connectors or policy as code pipelines.
5.	Departmental silos may block cross-domain model/agent reuse.
________________________________________
Part 4: What We Will Measure (3 KPI proposals)
1.	Regulatory adaptation cycle: ~3 months → < 2 weeks
2.	Coverage of AI systems under governance registry: <50% → 100% registered
3.	Audit completeness: Partial → Full end to end traceability incl. reasoning logs
4. Discovery Packet v1 — AI Product Manager
Student: Petra Dosbabová
Date: February 24, 2026
Client: EuroHealth Insurance AG
________________________________________
Part 1: Discovery Questions (10)
Question 1: Where do ServiceNow and Moveworks fall short for enterprise-wide governance, compliance, and multi-department scaling?
Why this matters: Identifies gaps we must solve beyond chatbot functionality; surfaces governance and scaling blockers.
Red flag: “ServiceNow should handle everything.”
KAF component: Core
________________________________________
Question 2: Which regulatory or internal policies must be enforced automatically in code rather than documented or trained?
Why this matters: Determines Policy as Code scope for compliance automation.
Red flag: “We don’t have defined enforceable rules.”
KAF component: Policy-as-Code
________________________________________
Question 3: How long does it take today to update workflows when regulations or internal policies change?
Why this matters: Reveals operational agility and EU AI Act readiness.
Red flag: “It takes several months.”
KAF component: Run Safe
________________________________________
Question 4: How should AI agents interoperate with your existing systems—specifically via MCP connectors or agent-to-agent (A2A) communication—to support end-to-end automation beyond ServiceNow?
Why this matters: Clarifies interoperability architecture and MCP/A2A connector requirements.
Red flag: “We only need integration with ServiceNow.”
KAF component: Interop (MCP/A2A)
________________________________________
Question 5: What level of auditability do Risk/Compliance require: event logs, reasoning trails, or full decision lineage?
Why this matters: Ensures we meet traceability and audit obligations for a regulated environment.
Red flag: “Standard logs should be enough.”
KAF component: Run Safe
________________________________________
Question 6: What actions should the agent be allowed to execute autonomously, and where must its autonomy be constrained?
Why this matters: Defines agent boundaries, risk controls, and governance tiering.
Red flag: “Let it handle anything automatically.”
KAF component: Core
________________________________________
Question 7: Where must human approvals or verifications occur before an AI agent proceeds with an action?
Why this matters: Establishes mandatory HITL checkpoints for regulated or high impact workflows.
Red flag: “We want zero human approvals.”
KAF component: HITL
________________________________________
Question 8: How is non PII operational and knowledge data structured, governed, and validated today—especially data used for grounding and retrieval?
Why this matters: Determines ingestion readiness and the quality of the foundation we can build on.
Red flag: “We don’t have a consistent KB structure.”
KAF component: Ingestion
________________________________________
Question 9: What AI specific security constraints must the solution meet beyond ‘no PII in training’—model isolation, on prem boundaries, threat patterns?
Why this matters: Defines security posture for on prem LLMs and agentic workflows.
Red flag: “Same as any other system.”
KAF component: Run Safe
________________________________________
Question 10: Which business outcomes must this AI industrialization deliver within the 6 month, €180K scope?
Why this matters: Ensures prioritization and scope alignment for ROI and timeline feasibility.
Red flag: “We want everything improved.”
KAF component: Core
________________________________________
Minimum coverage check:
✓ Policy-as-Code: Q2, Q3, Q5
✓ MCP/A2A interoperability: Q4
✓ Human-in-the-loop: Q7
________________________________________
Part 2: KAF Mapping (mini)
KAF Component	Covered by Q#	Notes
Agentic Core	Q1, Q6, Q10	Governance boundaries, scope, value alignment
Agentic Ingestion	Q8	Data structure, KB governance
Policy-as-Code	Q2, Q3, Q5	Regulatory automation, enforceable rules
Digital Trust / Run Safe	Q3, Q5, Q9, Q10	Audit, monitoring, compliance, safety
Human-in-the-Loop	Q7	Mandatory approvals
Interop (MCP/A2A)	Q4	Cross-system orchestration
________________________________________
Part 3: Assumptions / Risks / Open Items
1.	Shadow AI usage is broader than formally declared.
2.	Audit trails outside ServiceNow are inconsistent or unavailable.
3.	Regulatory updates rely heavily on manual workflows.
4.	On prem constraints may slow deployment of new connectors or policy as code pipelines.
5.	Departmental silos may block cross-domain model/agent reuse.
6. Knowledge base quality directly impacts automation ROI; without structured ownership and cleanup, cost reduction targets may not be achievable.
________________________________________
Part 4: What We Will Measure (3 KPI proposals)
1.	Regulatory adaptation cycle: ~3 months → < 2 weeks
2.	Coverage of AI systems under governance registry: <50% → 100% registered
3.	Audit completeness: Partial → Full end to end traceability incl. reasoning logs
4. Helpdesk cost per ticket reduction: Baseline → -30% within 6 months (through deflection + AHT reduction)
________________________________________
Part 5: Agent Classification
•	Governance tier: Enterprise (regulated domain + cross-system impact)
•	Registry/reuse potential: High — reusable across ITSM, HR, Claims, and contracting workflows in Phase 2
________________________________________
Dependencies on Other Roles
•	AI SEC: Threat modelling, compliance interpretation, isolation requirements
•	FDE: On prem hosting, infra constraints, connector feasibility
•	AI DA: Monitoring dashboards, operational KPIs
•	AI SE: CI/CD pipelines for policies, models, and evaluation workflows
________________________________________
Questions I Deliberately Did NOT Ask (and why)
•	UI/UX specifics — owned by AI-FE
•	Model selection or architecture — premature before governance + ingestion interviews
•	End user device or accessibility considerations — out of scope for first CIO meeting
________________________________________
Part 5: Agent Classification
•	Governance tier: Enterprise (regulated domain + cross-system impact)
•	Registry/reuse potential: High — reusable across ITSM, HR, Claims, and contracting workflows in Phase 2
________________________________________
Dependencies on Other Roles
•	AI SEC: Threat modelling, compliance interpretation, isolation requirements
•	FDE: On prem hosting, infra constraints, connector feasibility
•	AI DA: Monitoring dashboards, operational KPIs
•	AI SE: CI/CD pipelines for policies, models, and evaluation workflows
________________________________________
Questions I Deliberately Did NOT Ask (and why)
•	UI/UX specifics — owned by AI-FE
•	Model selection or architecture — premature before governance + ingestion interviews
•	End user device or accessibility considerations — out of scope for first CIO meeting

