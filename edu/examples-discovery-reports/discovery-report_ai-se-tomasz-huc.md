# DISCOVERY REPORT — AI-SE  
# STUDENT Tomasz Huc
# DATE 24.02.2026
# Client: EuroHealth Insurance AG  
# Role: AI Software Engineer  
# Engagement: AI Helpdesk Industrialization Initiative  

---

## 1. STAKEHOLDER MAP

### Hans Muller — CIO (Decision Sponsor)
- Accountable for 30% cost reduction.
- Under board pressure to demonstrate control and compliance.
- Requires visible, stable milestones.

### Stefan Weber — CISO (Compliance Gatekeeper)
- Focused on EU AI Act readiness.
- Requires enforceable governance, logging, and traceability.

### Jan Kovar + 12 Helpdesk Agents (Primary Users)
- Concerned about job security.
- Adoption and trust directly affect automation success.

### HR & Claims Departments (Shadow AI Owners)
- Operating independent AI tools.
- Currently outside centralized governance.

---

## 2. USE CASE LIST (Prioritized)

### P1 — Auto-Resolution of L1 Tickets
- Password resets
- Basic configuration issues
- FAQ-type queries

### P2 — Smart Routing & Escalation Support
- Reduce misrouting
- Improve classification accuracy

### P3 — Governance & Observability Layer
- Centralized logging
- Decision traceability
- Model version tracking

### P4 — Multi-Language Support (EN / DE / CZ)
- Required for 8-country operation
- Phase 2 candidate if needed

---

## 3. KEY FINDINGS FROM MEETING

1. This is not a helpdesk feature project — it is a governance recovery initiative.
2. AI deployments exist without standardized CI/CD or lifecycle control.
3. On-prem constraint significantly impacts architecture feasibility.
4. Automation baseline (35%) is unvalidated.
5. Knowledge base quality (30% outdated) introduces reliability risk.
6. Adoption risk is real due to helpdesk team concerns.
7. Six-month deadline is politically driven and requires phased delivery.
8. Shadow AI indicates absence of centralized AI runtime governance.

---

## 4. RISKS

### Operational Risks
- No unified deployment discipline across departments.
- Unknown GPU capacity for on-prem LLM hosting.
- ServiceNow API limitations may restrict automation.
- Logging infrastructure may not support audit requirements.

### Compliance Risks
- Insufficient traceability for EU AI Act.
- Shadow AI operating outside governance controls.

### Financial Risks
- €180K budget may not include hardware procurement.
- Infrastructure costs may exceed expectations.

### Adoption Risks
- Helpdesk distrust could undermine measurable automation.
- KB inaccuracies could damage system credibility.

---

## 5. NEXT STEPS

### Week 1 — Validation
1. Conduct infrastructure audit (GPU, containerization, hosting capability).
2. Validate ServiceNow integration capabilities and permissions.
3. Verify automation baseline metrics.
4. Align with AI-SEC on compliance logging requirements.

### Week 2 — Foundation Setup
1. Design minimal CI/CD pipeline for AI services.
2. Define centralized logging and observability schema.
3. Draft rollback strategy (blue/green deployment).
4. Propose phased architecture roadmap (Phase 1 → Phase 2).

---

## 6. DEPENDENCIES ON OTHER ROLES

- I need **AI-SEC** to define audit logging, retention, and compliance traceability requirements.
- I need **FDE** to confirm infrastructure feasibility and runtime architecture constraints.
- I need **AI-DS** to validate automation baselines and knowledge base quality.
- I need **AI-DA** to define telemetry metrics required for board reporting.
- I need **AI-PM** to clarify infrastructure budget allocation and phased scope boundaries.



---
# AI-SE Translation Table  
## What Hans Said → What He Didn’t Say → What It Means for AI-SE → Risk Category

| What Hans Said | What He Didn’t Say | What This Means for My AI-SE Role | Risk Category |
|----------------|-------------------|------------------------------------|---------------|
| “Cut costs by 30%.” | The board is watching and expects proof. | I must implement measurable automation with clear telemetry proving cost impact and stability. | Political |
| “Six months.” | The timeline may not be technically realistic. | Architecture must be phased and MVP-focused to deliver visible results early. | Operational |
| “35% automated already.” | That metric may not be validated. | I must verify automation baselines before designing scaling improvements. | Operational |
| “Everyone’s doing their own thing.” | There is no centralized AI governance or runtime control. | I must design a unified deployment layer with centralized logging and policy enforcement. | Operational |
| “HR built their own chatbot.” | Departments deploy AI without governance. | I must assume low deployment discipline and design onboarding controls for shadow AI. | Compliance |
| “On-prem only.” | Infrastructure capability is unverified. | I must validate GPU capacity, container orchestration, and model lifecycle feasibility immediately. | Financial |
| “Budget is €180K.” | Infrastructure cost may exceed available funding. | I must design a lean Phase 1 architecture and separate infra validation from feature scope. | Financial |
| “30% knowledge base outdated.” | Data governance is weak. | I must ensure ingestion pipelines include freshness controls to protect system reliability. | Adoption |
| “Jan’s team is adjusting.” | Adoption resistance is likely. | I must design explainability, overrides, and high system stability to protect trust. | Adoption |
| “EU AI Act compliance before deadline.” | Auditability is currently insufficient. | Logging, traceability, and model version control must be built in from Day 1. | Compliance |
| “If this works for IT, Claims wants it too.” | This is a scalability test. | Architecture must be modular and reusable across departments. | Financial |

# AI-**Role**
## What Hans Said → What He Didn’t Say
| ROLE   | "My #1 finding from Hans: [something NOT in the brief]" |
|--------|----------------------------------------------------------|
| FDE    | My #1 finding from Hans: This isn’t a tool integration project — it’s about rebuilding architectural control over fragmented AI systems. |
| AI-SE  | My #1 finding from Hans: This isn’t a helpdesk improvement project — it’s an AI governance recovery initiative requiring controlled deployment and observability. |
| AI-DS  | My #1 finding from Hans: The real risk isn’t model accuracy — it’s unreliable, unmanaged data driving uncontrolled automation. |
| AI-DA  | My #1 finding from Hans: Success isn’t defined by automation rates — it’s defined by defensible, board-ready proof that AI is under control. |
| AI-PM  | My #1 finding from Hans: The six-month deadline is a political milestone, not a technically validated delivery plan. |
| AI-FE  | My #1 finding from Hans: The biggest risk isn’t UI complexity — it’s loss of human trust in AI-driven decisions. |
| AI-SEC | My #1 finding from Hans: The issue isn’t missing documentation — it’s the absence of enforceable AI governance across departments. |