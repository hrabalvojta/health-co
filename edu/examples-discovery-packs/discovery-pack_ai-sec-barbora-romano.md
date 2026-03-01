### **Discovery Packet v1 — AI SEC**

### **Student: Barbora Romano**

### **Date: February 23, 2026**

### **Client: EuroHealth Insurance AG**



**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**







1️⃣ AI System Inventory \& Risk Classification

Question:
“Do you maintain a centralized inventory of all AI use cases, with EU AI Act risk classification and ownership assigned?”

Why it matters:
EU AI Act requires traceability, risk-tiering, and accountability. Without an inventory, governance cannot scale beyond isolated tools like ServiceNow.

Red flag:
“We track use cases informally in each department” or “We rely on ServiceNow tickets to know what’s running.”

KAF Component: Core

2️⃣ ServiceNow Governance Gaps

Question:
“Where does ServiceNow’s AI governance stop — especially across non-IT departments like underwriting, claims, or HR?”

Why it matters:
ServiceNow may govern IT workflows, but cross-department AI scaling requires enterprise-wide policy enforcement and model lifecycle controls.

Red flag:
“ServiceNow handles everything” (without clarity on lifecycle, approval gates, or external integrations).

KAF Component: Interop

3️⃣ Policy-as-Code Enforcement

Question:
“Which AI controls must be automatically enforced in code rather than documented — for example PII blocking, confidence thresholds, approval routing, or logging rules?”

Why it matters:
EU AI Act compliance and security cannot rely on documentation alone; controls must be programmatically enforced and auditable.

Red flag:
“Our policies are documented and teams are expected to follow them.”

KAF Component: Policy-as-Code

4️⃣ PII Boundary Enforcement (AI-SEC)

Question:
“Given the ‘no PII in training data’ rule, how is that technically enforced and evidenced?”

Why it matters:
In insurance, accidental PII ingestion is a regulatory and reputational risk. Enforcement must include detection, filtering, logging, and audit evidence.

Red flag:
“We instruct teams not to use PII” or “We trust data owners to sanitize data.”

KAF Component: Ingestion + Policy-as-Code

5️⃣ Change Velocity \& Regulatory Adaptation

Question:
“If a new EU regulation required additional explainability or logging tomorrow, how long would it take to update AI systems in production?”

Why it matters:
Operational maturity is measured by adaptability. Industrialized AI must adapt in weeks, not quarters.

Red flag:
“That would require a new project and funding cycle.”

KAF Component: Core + Run Safe

6️⃣ AI Production Monitoring (Run Safe)

Question:
“How do you monitor AI systems in production beyond uptime — drift, bias, hallucination, misuse?”

Why it matters:
Traditional IT monitoring is insufficient for AI risk. Regulators expect post-market monitoring and ongoing validation.

Red flag:
“We monitor system availability and incident tickets only.”

KAF Component: Run Safe

7️⃣ AI Threat Model \& Red Teaming (AI-SEC)

Question:
“Have you defined an AI-specific threat model — including prompt injection, model extraction, data poisoning, and agent privilege escalation?”

Why it matters:
AI introduces new attack vectors not covered by traditional AppSec. Without a threat model, scaling AI increases systemic risk.

Red flag:
“Our cybersecurity framework already covers that” (without AI-specific assessment).

KAF Component: Core + Run Safe

8️⃣ Agentic Workflow Scope \& Tool Access

Question:
“If an AI agent can orchestrate workflows across systems, what steps can it autonomously plan, and what systems can it invoke?”

Why it matters:
Agentic AI changes the risk profile. Each integration (MCP connector) expands the attack surface and compliance exposure.

Red flag:
“We haven’t defined limits yet” or “The agent can call any approved API.”

KAF Component: Interop + Policy-as-Code

9️⃣ Least Privilege \& Action Guardrails (AI-SEC)

Question:
“How do you ensure AI agents operate under least-privilege principles and cannot execute high-risk actions without validation?”

Why it matters:
Agent autonomy must be bounded by enforceable authorization, confidence thresholds, and role-based constraints.

Red flag:
“The agent runs under a service account with broad access.”

KAF Component: Policy-as-Code + HITL

🔟 Human-in-the-Loop (HITL) Checkpoints

Question:
“Which AI-driven decisions require mandatory human confirmation — and how is that enforced technically?”

Examples to anchor:

Claim denial recommendations

Underwriting risk scoring

Customer communications

Policy changes

Why it matters:
EU AI Act high-risk systems require oversight and override capability. HITL must be embedded, not optional.

Red flag:
“Humans can override if needed” (without workflow-level enforcement).

KAF Component: HITL

🎯 What These 10 Questions Reveal
Dimension	What You’re Diagnosing
Governance gaps	Whether ServiceNow is a tool vs enterprise AI control plane
Policy-as-Code	Whether controls are enforceable or aspirational
Operational maturity	Regulatory adaptability speed
Agentic readiness	Workflow planning + tool boundary clarity
Digital Trust	Auditability, monitoring, explainability
AI-SEC	Threat model maturity + least privilege enforcement

