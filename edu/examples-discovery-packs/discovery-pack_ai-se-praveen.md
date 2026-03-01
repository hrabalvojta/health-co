# Discovery Packet v1 — AI-SE (AI Systems Engineer)
## Team AI-SE
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1
When EU AI Act guidance changes, how long does it take before those changes are technically enforced across ServiceNow and departmental AI tools — not just documented, but actually running in production?

**Why this matters:** Their current regulatory adaptation speed is ~3 months. We must design automation and Policy-as-Code enforcement to reduce this to <2 weeks.

**Red flag:** Legal updates are handled via documentation and manual process updates only.

**KAF component:** Policy-as-Code

---

### Question 2
What specific governance rules must be enforced in executable code (e.g., no PII in training data, cross-border data limits, approval gates for high-risk workflows), and where should those rules live (policy registry, CI/CD gates, centralized governance layer)?

**Why this matters:** Identifies which legal and operational controls must become automated guardrails instead of wiki pages.

**Red flag:** We rely on awareness and training, not technical enforcement.

**KAF component:** Policy-as-Code

---

### Question 3
What prevents you today from having a single, governed inventory of all AI systems across departments (ServiceNow, HR chatbot, Claims LangChain, Finance GPT usage)?

**Why this matters:** Success criteria require 100% AI registry coverage and elimination of shadow AI.

**Red flag:** We don’t have visibility into departmental tools.

**KAF component:** Agentic Ingestion

---

### Question 4
How are AI systems currently deployed, versioned, tested, monitored, and rolled back in production?

**Why this matters:** We must integrate CI/CD, model version control, and release governance for a production-grade platform.

**Red flag:** Manual deployments or no rollback strategy.

**KAF component:** Run Safe / Digital Trust

---

### Question 5
What monitoring gaps exist between ServiceNow, legacy tools (Nagios/custom scripts), and departmental AI tools? What failures go unseen today?

**Why this matters:** Unifying monitoring is an explicit success criterion.

**Red flag:** We don’t know when departmental AI fails.

**KAF component:** Run Safe

---

### Question 6
Where in the helpdesk or AI-assisted workflow must human approval be mandatory (e.g., escalations, access changes, high-impact recommendations)?

**Why this matters:** We must design Human-in-the-Loop checkpoints into orchestration.

**Red flag:** Everything should be fully autonomous.

**KAF component:** Human-in-the-Loop

---

### Question 7
What integrations or connectors must the governed platform support (ServiceNow APIs, monitoring tools, identity providers, HR/Claims systems), and how are authentication boundaries enforced today?

**Why this matters:** Defines MCP/A2A interoperability boundaries and identity enforcement in an on-prem environment.

**Red flag:** Unclear which systems AI tools currently access.

**KAF component:** Interop (MCP/A2A)

---

### Question 8
What are the on-prem infrastructure constraints (network segmentation, DMZ, firewall rules, patch cycles, identity federation) that could affect deployment of a unified agentic platform?

**Why this matters:** Deployment must comply with on-prem only constraint and GDPR boundaries.

**Red flag:** Infrastructure boundaries cannot be adapted at all.

**KAF component:** Agentic Core + Interop

---

### Question 9
What metrics do you trust today (misroutes, auto-resolution %, CSAT), and where are the biggest blind spots preventing confident AI decisions?

**Why this matters:** We must baseline and improve CSAT from 3.6 → 4.2+ and measure governance impact.

**Red flag:** No clear measurement baseline.

**KAF component:** Run Safe / Ingestion

---

### Question 10
When this engagement is finished, what must be true for you to confidently say: “Our AI landscape is governed, auditable, and defensible” — regardless of technical implementation?

**Why this matters:** Aligns technical architecture to executive success criteria and board expectations.

**Red flag:** Unclear definition of “AI under control.”

**KAF component:** Agentic Core

---

## Part 2: KAF Mapping

| KAF Component              | Covered by Q# | Notes |
|----------------------------|---------------|-------|
| Agentic Core               | 8, 10        | Architecture + executive alignment |
| Agentic Ingestion          | 3, 9         | AI registry + telemetry |
| Policy-as-Code             | 1, 2         | Regulatory enforcement |
| Digital Trust / Run Safe   | 4, 5, 9      | Monitoring + CI/CD |
| Human-in-the-Loop          | 6            | Escalation gates |
| Interop (MCP/A2A)          | 7, 8         | Connectors + authentication |

---

## Part 3: Assumptions / Risks / Open Items

1. Shadow AI tools may have unknown production access to sensitive systems.
2. Regulatory updates are currently process-based, not technically enforced.
3. Monitoring fragmentation could hide compliance violations.
4. On-prem constraints may limit connector flexibility.
5. Board expectations may exceed €180K scope unless phased properly.

---

## Part 4: KPI Proposals

1. Regulatory adaptation time: ~3 months → <2 weeks
2. AI registry coverage: 0% unified → 100% governed inventory
3. CSAT improvement: 3.6 → 4.2+ within 6 months

---

## Part 5: Agent Classification

- Governance tier: Enterprise
- Registry/reuse potential: Governed Agentic Platform template reusable across EU-regulated insurers within Kyndryl.

---

## Dependencies on Other Roles

- AI-SEC → threat modeling & EU AI Act risk classification
- AI-DS → data quality & knowledge base structure
- AI-PM → stakeholder alignment & budget prioritization
- AI-DA → reporting dashboards & KPI instrumentation

---

## Questions I Deliberately Did NOT Ask

- Detailed ROI modeling → AI-PM scope
- End-user UX workflows → AI-FE scope
- Data annotation specifics → AI-DS scope
