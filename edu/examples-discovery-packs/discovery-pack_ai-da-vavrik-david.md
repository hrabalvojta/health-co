# Discovery Packet v1 — AI-DA
## Student: David Vavřík
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: When regulation changes, what exactly takes three months — legal review, policy updates, technical enforcement, or deployment?
**Why this matters:** You need to isolate the bottleneck. Industrialization means reducing regulatory adaptation to days.
**Red flag (bad answer):** “It depends on each department.” → No standardized AI change lifecycle.
**KAF component:** Run Safe

### Question 2: If we were to introduce an enterprise agentic platform, what enterprise systems must it orchestrate across — Claims DB, IAM, HRIS, Finance ERP?
**Why this matters:** Shows we’re thinking about orchestration, not chatbots. Identifies MCP/API maturity and integration scope.
**Red flag (bad answer):** “Most systems don’t expose secure APIs.” → Integration cost and timeline risk within €180K.
**KAF component:** Interop

### Question 3: What human checkpoints are enforced before an AI action affects a customer policy, payment, or employment record?
**Why this matters:** Identifies high-risk AI boundaries under EU AI Act and required Human-in-the-Loop controls.
**Red flag (bad answer):** “Humans review only when escalated.” → Reactive compliance model.
**KAF component:** HITL

### Question 4: What executive metrics would convince the board that AI is under control — not just productive?
**Why this matters:** Industrialization requires governance dashboards: AI inventory coverage %, audit completeness %, compliance SLA, risk heatmap.
**Red flag (bad answer):** “We mainly track ticket deflection and CSAT.” → No governance KPI layer.
**KAF component:** Core

### Question 5: Today, what technical mechanism enforces AI guardrails across systems — or are controls implemented separately in each tool?
**Why this matters:** You want to surface whether policies (PII restrictions, logging, access control, prompt filtering) are centralized and enforceable in code.
**Red flag (bad answer):** “Each team configures their own safeguards.” → No unified Policy-as-Code layer; scaling will multiply risk.
**KAF component:** Policy-as-Code

### Question 6: If a regulator requested a full audit of every AI-driven decision impacting customers in the last 12 months, how long would it take you to deliver that?
**Why this matters:** EU AI Act enforcement will require demonstrable traceability. This tests audit completeness across governed and shadow AI.
**Red flag (bad answer):** “We would need time to gather information from departments.” → No centralized audit trail; board exposure.
**KAF component:** Run Safe

### Question 7: Is there a standardized knowledge base structure across HR, Claims, and IT — or does each AI system use different data foundations?
**Why this matters:** Scaling requires normalized knowledge architecture.
**Red flag (bad answer):** “Each department maintains its own KB.” → Fragmented data governance; scaling inefficiency.
**KAF component:** Ingestion + Interop

### Question 8: How are data quality thresholds (accuracy, completeness, bias tolerance) encoded — are they documented expectations or machine-enforced validation gates?
**Why this matters:** Industrialization requires automated data validation before models act. Otherwise governance is theoretical.
**Red flag (bad answer):** “We rely on periodic reviews.” → No automated data guardrails; reactive quality control.
**KAF component:** Ingestion + Policy-as-Code

### Question 9: At what confidence level does an AI output trigger automatic action versus human review — and is that threshold standardized?
**Why this matters:** HITL should be tied to measurable model confidence or risk classification. This exposes whether decisions are systematic or arbitrary.
**Red flag (bad answer):** “Humans review only if users complain.” → No structured HITL gating logic.
**KAF component:** Run Safe + HITL

### Question 10: When a human overrides an AI decision, is that event captured as structured data for trend analysis?
**Why this matters:** HITL isn’t just approval — overrides are signals of model drift, bias, or process gaps. This is critical for continuous improvement.
**Red flag (bad answer):** “Overrides are handled in tickets, not tracked separately.” → No feedback loop into governance metrics.
**KAF component:** Run Safe + HITL

---

## Part 2: KAF Mapping (mini)
| KAF Component       | Covered by Q# | Notes                                                        |
|---------------------|---------------|--------------------------------------------------------------|
| Agentic Core        |             4 | Board KPIs • Governance visibility                           |
| Agentic Ingestion   |          7, 8 | Data standardization • Quality gates                         |
| Policy-as-Code      |          5, 8 | Centralized guardrails • Enforced thresholds                 |
| Digital Trust       |   1, 6, 9, 10 | Audit readiness • Regulatory agility • Traceable decisions   |
| Human-in-the-Loop   |      3, 9, 10 | Defined checkpoints • Confidence gating • Override analytics |
| Interop (MCP/A2A)   |          2, 7 | System orchestration • API maturity                          |

---

## Part 3: Assumptions / Risks / Open Items (3-5)
Regulatory adaptation remains structurally slow (~3 months)
→ Risk that EU AI Act readiness by Q3 2026 is unrealistic without operating model redesign.

Audit trail is fragmented outside ServiceNow
→ High exposure if regulator requests cross-department AI traceability.

Policy enforcement is partially documented but not centrally codified
→ Scaling beyond IT will multiply inconsistency and compliance gaps.

Human-in-the-Loop controls are reactive rather than threshold-driven
→ Risk of either over-automation (compliance exposure) or over-escalation (operational inefficiency).

Knowledge base and data standards are inconsistent across departments
→ Limits enterprise agent orchestration and cross-functional scalability.

---

## Part 4: What We Will Measure (3 KPI proposals)
1. Regulatory Adaptation SLA: 3 months → ≤ 2 weeks
(Time from policy change approval to technical enforcement across AI systems)

2. AI Audit Coverage: 100% of high-risk AI workflows + ≥75% total AI systems integrated into centralized, queryable audit layer
(Including shadow AI detection and logging integration)

3. Threshold-Based Escalation Rate: ≥95% of escalations triggered automatically by confidence or risk scoring logic.
(% of AI decisions escalated based on predefined confidence/risk thresholds (not manual complaints).)

---

## Part 5: Agent Classification
- **Governance tier:** Enterprise
- **Registry/reuse potential:** Register the enterprise agent as a versioned SDE Solution Catalogue Accelerator and publish the code, policy-as-code, MCP connectors and HITL runbooks in the Agent Builder repo—backed by Responsible AI sign-off—so delivery teams can instantiate a compliant, audit-ready agent quickly across Kyndryl. <<< THIS WAS GENERATED BY chatGPT WITH ACCESS TO COMPANY KNOWLEDGE

---

## Dependencies on Other Roles:
- I need AI-PM to ask about regulatory adaptation & board KPIs because Q1 and Q4 depend on knowing process ownership, decision velocity, and which executive metrics the board will accept.
- I need AI-SE to ask about technical enforcement, logging and instrumentation because Q1, Q5, Q6, Q9 and Q10 require CI/CD/ops detail: how policies are pushed, how audit/log/override data are captured, and how confidence gating is implemented.
- I need AI-DS to ask about KB structure, data validation and confidence modelling because Q7, Q8 and Q9 depend on standardized KB schemas, machine-enforced data quality gates, and how model confidence is defined and measured.


## Questions I Deliberately Did NOT Ask (and why):
- “Which on-prem LLM hosting architecture (cluster topology, orchestration, model versioning and compute sizing) will we standardize on for production?” — because that’s FDE territory.
- “What is the prioritized product roadmap (ROI targets, go/no-go criteria, and stakeholder trade-offs) for scaling the agentic platform across business units?” — because that’s AI-PM territory.
- “What runtime defenses exist against prompt-injection, model-abuse, and data-exfiltration — e.g., input/output sanitization, model-behavior anomaly detection, rate limiting, and automated session quarantining?” — because that’s AI-SEC territory.

