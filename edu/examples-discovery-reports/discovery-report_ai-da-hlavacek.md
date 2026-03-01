# Discovery Report
**Role:** AI Data Analyst (AI-DA)
**Client:** EuroHealth Insurance AG

## 1. Stakeholder analysis (from AI-DA perspective)
* **Hans Muller (CIO):** Is under extreme board pressure. He is not interested in technical details like LLM parameters; he needs a monthly, board-ready dashboard proving ROI (30% cost reduction) and EU AI Act compliance before the August deadline to secure his position.
* **Jan Kovar (Helpdesk Lead):** His team of 12 agents fears replacement. Our metrics must be explicitly framed around "assisting agents" (e.g., reducing MTTR, improving CSAT from 3.2 to 3.6) rather than "replacing headcount" to ensure user adoption.

## 2. Key findings and implications for my workstream
* **Knowledge Base Quality is a Blocker:** Hans admitted that ~30% of the 2,000 Confluence pages are "garbage" and outdated. For the AI-DA role, this is a critical risk. An AI trained on stale knowledge will hallucinate, causing user trust and CSAT metrics to plummet in week one.
* **Shadow AI Proliferation:** Different departments (HR, Claims, IT) are currently using isolated, ungoverned AI tools. This means there is no unified metric baseline. We must establish a single source of truth for all AI interactions to prove the required 30% cost deflection.

## 3. Technical/functional requirements I need to investigate
* **Phase 0.5 Data Quality Audit:** Before deploying any RAG model, we must mandate a data quality scoring framework (evaluating freshness and accuracy) to clean the outdated Confluence data.
* **Board-Ready KPI Dashboard:** Design a monthly reporting schema specifically for Hans to present to the board. It must securely track:
  * *Auto-resolve rate* (to prove the 30% cost reduction).
  * *User Trust Score & CSAT* (to ensure quality remains high).
  * *Escalation accuracy* (to prove compliance and safety).
* **On-Prem Data Pipeline:** Investigate the ServiceNow API v2 integration feasibility to securely extract ticket data into our monitoring schema, strictly adhering to the non-negotiable on-premise constraints.
## 4. Risks specific to my area
* **Baseline Skew due to Garbage Data (HIGH):** Since ~30% of the Confluence knowledge base is outdated, any initial A/B testing comparing human agents vs. the AI agent will likely show a severe drop in the CSAT score. If Jan's helpdesk team sees the AI failing early, they will reject the tool entirely.
* **Fragmented Shadow AI Metrics (MEDIUM):** HR and Claims are running their own unapproved AI prototypes. If we cannot pipe the telemetry data from these existing shadow deployments into a unified tracking schema, we will fail to establish an accurate baseline to prove Hans's required 30% cost reduction.
* **On-Premises Data Extraction (HIGH):** The strict on-premises compliance constraint means we cannot use standard cloud-based APM (Application Performance Monitoring) tools to track agent behavior. Building a custom on-prem dashboard might delay the August deadline.

## 5. Recommended next steps (first 2 weeks)
* **Step 1: Phase 0.5 Knowledge Audit Execution:** Collaborate with the AI Data Scientist to sample 200 of the 2,000 Confluence pages and establish a baseline Data Quality Score (measuring freshness and accuracy) before any models are trained .
* **Step 2: Define the KPI Dashboard Schema:** Draft the mock-up of the monthly board-ready dashboard for Hans, securing early sign-off on the specific metrics (Auto-resolve rate, MTTR reduction, User Trust Score) 
* **Step 3: ServiceNow API Mapping:** Map the specific fields in the ServiceNow API v2 that need to be continuously extracted to feed our on-premise monitoring database.

## 6. Dependencies on other roles in the team (Checkpoint 2)
As an AI-DA, establishing an accurate baseline and delivering the board-ready dashboard requires critical inputs from all 6 other roles:

* **Dependency on AI-PM (Project Manager):** I need you to finalize the success criteria and the change management strategy for Jan's helpdesk team. If the human agents actively boycott the tool, my baseline A/B testing metrics will be completely skewed.
* **Dependency on AI-SEC (Security Specialist):** I need clear guidelines on PII handling and EU AI Act constraints. Before I extract ServiceNow data, I must know which ticket fields I am legally allowed to display on Hans's dashboard without violating data privacy.
* **Dependency on AI-FE (Front-End Developer):** I need you to implement explicit trust indicators and telemetry in the UI (e.g., confidence scores, explicit "thumbs up/down" buttons). Without front-end tracking, I cannot calculate the User Trust Score and CSAT metrics.
* **Dependency on AI-DS (Data Scientist):** I need you to define the Golden Dataset evaluation metrics ASAP. My production drift detection KPIs must perfectly align with your pre-deployment testing baseline, otherwise we will report conflicting numbers.
* **Dependency on AI-SE (Software Engineer):** I strictly depend on your architecture for the ServiceNow API v2 integration. Since cloud APM tools are forbidden, I need you to build a secure, local data pipeline to feed my monitoring schema.
* **Dependency on FDE (Full-Stack Developer Engineer):** I need you to unify the fragmented shadow AI tools (HR, Claims) into a single architecture. I cannot prove a 30% company-wide cost reduction unless there is a single source of truth for all AI interactions.