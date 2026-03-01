\# Discovery Packet v1 — \AI-SE

\## Student: Oleksandr Krutko

\## Date: February 23, 2026

\## Client: EuroHealth Insurance AG



---



\## Part 1: Discovery Questions (10)



\### Question 1: Where does AI execution break down when it moves beyond ServiceNow and the Company have to use additional ungoverned (shadow AI) tools?

\*\*Why this matters:\*\* ServiceNow is governed and production-safe, but HR chatbot, Claims LangChain PoC, and Finance GPT usage are not. Understanding where execution, control, or oversight fails outside the governed environment reveals architectural gaps in enforcement, integration, and monitoring.

\*\*Red flag (bad answer):\*\* Those systems are separate, so they follow their own standards.

\*\*KAF component:\*\* Agentic Core 



\### Question 2: Do you have a technical AI registry — something version-controlled that tracks models, prompts, workflows, risk class, and owners?

\*\*Why this matters:\*\* Governance requires metadata. As AI-SE, I need this to automate policy enforcement and CI/CD gates.

\*\*Red flag (bad answer):\*\* We track this in spreadsheets

\*\*KAF component:\*\* Digital Trust



\### Question 3: How are AI models, prompts, and workflows deployed into production today? Is there CI/CD with validation gates?

\*\*Why this matters:\*\* Industrial AI requires automated deployment with compliance checks. Manual releases mean uncontrolled risk.

\*\*Red flag (bad answer):\*\* Deployment is project-based and manual.

\*\*KAF component:\*\* Agentic Core



\### Question 4: If the CISO requires new logging or oversight requirements next month, how would you technically enforce them across all AI systems?

\*\*Why this matters:\*\* Regulatory agility depends on centralized enforcement. Policies should be updated in code and propagated automatically - not reimplemented by each team.

\*\*Red flag (bad answer):\*\* Each team would need to update their system.

\*\*KAF component:\*\* Digital Trust



\### Question 5: For shadow AI systems (HR chatbot, etc.), how is access to sensitive data technically controlled and audited?

\*\*Why this matters:\*\* HR likely involve high-risk AI under EU AI Act. Access control, least-privilege enforcement, and auditability must be engineered - not assumed.

\*\*Red flag (bad answer):\*\* They use shared credentials or internal trust.

\*\*KAF component:\*\* Policy-as-Code



\### Question 6: Can you reconstruct an AI-driven decision end-to-end today (input data, prompt, model version, output, human approval)?

\*\*Why this matters:\*\* Audit replayability is critical in insurance (e.g., claims disputes). Without full traceability, regulatory defensibility is weak.

\*\*Red flag (bad answer):\*\* We log outputs but not the full chain.

\*\*KAF component:\*\* Digital Trust



\### Question 7: What is the data ingestion process for all existing AI models?

\*\*Why this matters:\*\* Data ingestion is the primary risk surface - especially with shadow AI accessing HR data and claims policy databases. Industrialization requires standardized ingestion pipelines with PII filtering, access control, logging, and validation before inference.

\*\*Red flag (bad answer):\*\* Each team pulls data directly from the source system as needed.

\*\*KAF component:\*\* Agentic Ingestion



\### Question 8: How are integrations standardized across countries — do AI systems use a shared connector framework or country-specific implementations?

\*\*Why this matters:\*\* Agentic platform requires governed connectors (MCP-style abstraction). Fragmented integrations block scaling.

\*\*Red flag (bad answer):\*\* Each country built its own integration layer.

\*\*KAF component:\*\* MCP/A2A



\### Question 9: Are AI governance controls enforced directly in system logic (policy engine, validation layer, etc.), or are they documented as guidelines/PDF instructions for teams and end-users?

\*\*Why this matters:\*\* If policies are only documented, they cannot be consistently enforced, monitored, or audited across shadow AI systems.

\*\*Red flag (bad answer):\*\* We have documented AI usage guidelines that teams are expected to follow.

\*\*KAF component:\*\* Policy-as-Code



&nbsp;### Question 10: Where in your AI workflows is human oversight technically enforced, and how is that enforcement implemented?

\*\*Why this matters:\*\* EU AI Act requires meaningful human oversight — not optional review. In insurance (claims, HR), approval thresholds, override capability, and escalation paths must be built into the workflow logic and auditable.

\*\*Red flag (bad answer):\*\* Humans can step in if something goes wrong.

\*\*KAF component:\*\* Human-in-the-Loop



---



\## Part 2: KAF Mapping (mini)

| KAF Component       | Covered by Q# | Notes                  |

|---------------------|---------------|------------------------|

| Agentic Core        |Q1, Q3         |                        |

| Agentic Ingestion   |Q7             |                        |

| Policy-as-Code      |Q9, Q5         |                        |

| Digital Trust       |Q4, Q6, Q2     |                        |

| Human-in-the-Loop   |Q10            |                        |

| Interop (MCP/A2A)   |Q8             |                        |



---



\## Part 3: Assumptions / Risks / Open Items

1. There is executive mandate to centralize AI governance (CIO + CISO alignment)
2. Shadow AI systems are more widespread than currently visible
3. EU AI Act risk classification status for existing AI use cases



---



\## Part 4: What We Will Measure (3 KPI proposals)

1. % of AI Systems Under Centralized Governance Control
2. Policy Change Deployment Time: Months <= 5 business days target
3. Full Decision Traceability Coverage (High-Risk AI): <20% baseline -> 100% target





---



\## Part 5: Agent Classification

\*\*Governance tier:\*\* Enterprise

\*\*Registry/reuse potential:\*\* We will use Kyndryl approved container registry and approved code version control system



\## Dependencies on Other Roles:

I need AI-SEC to ask about risks of touching the current shadow AI tools





\## Questions I Deliberately Did NOT Ask (and why):



I need AI-PM to ask about feasibilities of goals of this project

