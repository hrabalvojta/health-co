# Discovery Packet v1 — AI-PM
## Student: Kamil Vintrlik
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: Do you have a complete, current inventory of all AI systems across ServiceNow, Moveworks, HR’s chatbot, Claims’ LangChain prototype, and other departmental tools?
**Why this matters:** Governance, auditability, and EU AI Act readiness depend on knowing *every* AI asset in the environment. Unknown systems = unmanageable risk.
**Red flag (bad answer):** “We think so, but not fully sure.”
**KAF component:** Ingestion / Policy-as-Code

### Question 2: Which AI systems today lack a unified audit trail or explanation layer — especially Moveworks and departmental prototypes?
**Why this matters:** EU AI Act requires traceability; scattered or missing logs block certification and safe operations.
**Red flag:** “Logs exist, but they’re in different places.”
**KAF component:** Run Safe

### Question 3: Beyond HR and Claims, how many other Shadow AI projects do you suspect exist, and why did teams bypass central IT?
**Why this matters:** Shadow AI introduces unmonitored, unvalidated tools that pose security and compliance risks.
**Red flag:** “We don’t track that.”
**KAF component:** Policy-as-Code

### Question 4: How aligned are Legal, Security, Compliance, and IT on EU AI Act classifications, risk tiers, and required controls for your AI systems?
**Why this matters:** Rule-as-Code requires cross‑functional alignment; inconsistent interpretations block governance.
**Red flag:** “Each team interprets it differently.”
**KAF component:** Policy-as-Code / Core

### Question 5: For on-prem deployment, what GPU/compute resources do you have, and have they been sized for multi-model or agentic workloads?
**Why this matters:** On-prem constraints shape the architecture; insufficient compute is a critical blocker.
**Red flag:** “We haven’t evaluated infra for AI workloads.”
**KAF component:** Core / Interop

### Question 6: When risk rules or compliance policies change, how long does it take to propagate updates across ServiceNow, HR tools, and Claims workflows?
**Why this matters:** CIO requires updates in days; current processes often take months.
**Red flag:** “It depends — usually several committees.”
**KAF component:** Policy-as-Code / Core

### Question 7: What telemetry and observability data do you collect today across all AI systems, and where are the biggest blind spots?
**Why this matters:** Without full observability, unsafe or incorrect AI actions cannot be detected or audited.
**Red flag:** “We use default logs from each system.”
**KAF component:** Run Safe

### Question 8: Which AI-driven actions must have human-in-the-loop approval, and which should be performed autonomously (routing, config changes, ticket closure)?
**Why this matters:** HITL boundaries define safe autonomy and compliance.
**Red flag:** “We haven’t classified actions by risk.”
**KAF component:** HITL / Policy-as-Code

### Question 9: Which cross-system workflows fail today due to interoperability gaps between ServiceNow, legacy monitoring tools, HR’s bot, and Claims’ prototype?
**Why this matters:** Broken interoperability blocks agent orchestration and MCP/A2A workflows.
**Red flag:** “We handle it manually; it works well enough.”
**KAF component:** Interop / Core

### Question 10: Given the €180K / 6‑month limit, which outcomes matter most — auditability, compliance, Shadow AI reduction, or operational stability?
**Why this matters:** Scope must be realistic; the budget requires ruthless trade-offs.
**Red flag:** “All of them equally.”
**KAF component:** Core / DA (metrics)

---

## Part 2: KAF Mapping (mini)

| KAF Component      | Covered by Q#         | Notes |
|---------------------|-----------------------|-------|
| Agentic Core        | 4, 5, 6, 9, 10        | Prioritization, infra, agility, integration |
| Agentic Ingestion   | 1                     | AI inventory + ingest governance |
| Policy-as-Code      | 1, 3, 4, 6, 8         | Policy enforcement focus |
| Digital Trust       | 2, 7                  | Logs + monitoring |
| Human-in-the-Loop   | 8                     | Mandatory governance requirement |
| Interop (MCP/A2A)   | 5, 9                  | ServiceNow, legacy, departmental AI |

---

## Part 3: Assumptions / Risks / Open Items (3–5)

1. Shadow AI volume is likely higher than currently disclosed, expanding scope and risk.
2. On-prem compute capacity may be insufficient for multi-model or agentic workloads.
3. EU AI Act interpretations differ across Legal, Security, and IT — governance cannot be codified until aligned.
4. Audit logs are fragmented across systems; unification may exceed budget or complexity expectations.
5. €180K cap may require deprioritizing non-essential features to avoid scope failure.

---

## Part 4: What We Will Measure (3 KPI proposals)

1. **AI Governance Coverage Rate**  
   % of AI systems under unified governance + auditability  
   *Target: 80% by Month 6*

2. **Policy Change Propagation Time**  
   Time to update all AI systems after a regulatory change  
   *Target: <10 business days*

3. **Auditability / Traceability Score**  
   % of AI actions fully logged (input → decision → action)  
   *Target: 95% by project end*

---

## Part 5: Agent Classification

- **Governance tier:** Enterprise  
- **Registry/reuse potential:** High — governance agents, audit agents, and policy propagation agents are reusable across regulated industries (healthcare, insurance, banking).

---

## Dependencies on Other Roles:

- **AI-SEC:** Validate risk tiers, security constraints, compliance obligations.  
- **AI-DS:** Confirm data quality, log structure, and knowledge sources.  
- **AI-SE:** Assess CI/CD, deployment, and monitoring maturity.  
- **FDE / Interop:** Map connectors for ServiceNow, legacy monitoring, and departmental AI systems.  
- **AI-DA:** Define dashboards and KPI reporting.

---

## Questions I Deliberately Did NOT Ask (and why):

- **“Which LLM do you prefer?”** — model selection depends on on‑prem infra readiness first.  
- **“Should we retrain Moveworks models?”** — vendor-managed; not relevant to governance design.  
- **“Do you want multi-agent orchestration?”** — cannot be discussed before HITL and risk boundaries are defined.