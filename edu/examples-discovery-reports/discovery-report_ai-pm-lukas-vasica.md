# Discovery Report  
## EuroHealth Insurance AG – AI Helpdesk Industrialization  
**Role:** AI-PM (AI Project Manager)  
**Date:** Day 12 – Post-Roleplay  
**Sponsor:** Hans Muller (CIO)

---

# 0. Executive Summary

EuroHealth is not starting an AI initiative from zero. Basic ticket automation is already in place via Moveworks/ServiceNow, while parallel “shadow AI” initiatives exist in HR and Claims without unified governance.

The CIO’s stated success criteria are:

- Reduce remaining helpdesk costs by **30%**
- Consolidate AI initiatives under **one unified platform**
- Achieve **EU AI Act compliance readiness by August 2026**
- Deliver within **EUR 180K / 6 months**
- Operate **on-prem only (non-negotiable)**

This engagement is not a chatbot project. It is an **AI industrialization and governance program** with a hard board-level milestone in August 2026.

Primary risks include:
- On-prem infrastructure feasibility
- Undefined KPI baselines for “30% cost reduction”
- Knowledge base quality (~30% outdated, no owner)
- Helpdesk adoption resistance
- Scope creep driven by compliance reinterpretation

The immediate need is a **phased, board-defensible roadmap** with validated feasibility before scope commitment.

---

# 1. Stakeholder Analysis (AI-PM Perspective)

## Executive Sponsor
**Hans Muller – CIO**
- Under board pressure to demonstrate AI ROI.
- Needs a compliance-ready narrative by August 2026.
- Success is political, financial, and regulatory.

## Operational Owner
**Jan Kovar – Helpdesk Lead (12 agents)**
- Concerned about workforce impact.
- Adoption risk if automation perceived as replacement.

## Governance & Control Functions
**CISO / Security / Compliance**
- Implicit veto power.
- Responsible for EU AI Act interpretation.
- Critical for on-prem and audit requirements.

## Shadow AI Stakeholders
**HR Bot Owner / Claims Prototype Team**
- Already operating independent AI solutions.
- Potential resistance to central governance.
- Represent Phase 2 expansion opportunity.

## Platform & Vendor Stakeholders
**ServiceNow / Moveworks Owners**
- Existing automation footprint.
- Integration vs replacement decision impacts scope and budget.

## Knowledge Owners (Currently Undefined)
- 2,000 Confluence pages.
- ~30% outdated.
- No defined ownership or governance workflow.

**Implication for AI-PM:**  
The engagement requires coordinated stakeholder alignment, formalized decision rights, and a defined operating model for AI governance.

---

# 2. Key Findings & Implications for AI-PM Workstream

## Finding A: AI Already Exists in Production
- Moveworks/ServiceNow handles basic tickets.

**Implication:**  
Phase 1 must address *remaining* cost drivers without duplicating existing automation.

**Second-Order Risk:**  
Competing automation tools create confusion and adoption decline.

---

## Finding B: Shadow AI Without Governance
- HR chatbot and Claims LangChain prototype.
- No unified oversight or compliance standard.

**Implication:**  
The program must establish governance before expanding functionality.

**Second-Order Risk:**  
Fragmented AI creates regulatory exposure and inconsistent risk posture.

---

## Finding C: Success Defined as Board Milestone (August 2026)
- Compliance readiness + cost reduction.

**Implication:**  
Roadmap must be backward-planned from August milestone.
Monthly board-ready reporting required.

**Second-Order Risk:**  
Undefined KPI baselines create vulnerability in board narrative.

---

## Finding D: On-Prem Only (Non-Negotiable)
- No cloud usage permitted.

**Implication:**  
Week 1 feasibility validation required (GPU, latency, security controls).

**Second-Order Risk:**  
Infrastructure delays eliminate early visible wins.

---

## Finding E: Knowledge Base Quality Gap
- ~30% outdated content.
- No assigned owner.

**Implication:**  
Knowledge governance is a prerequisite to automation scaling.

**Second-Order Risk:**  
Poor content quality leads to hallucinations and user distrust.

---

## Finding F: Helpdesk Fear & Adoption Risk
- Team concerned about replacement.

**Implication:**  
Change management and augmentation messaging required.

**Second-Order Risk:**  
Passive resistance reduces usage → KPI underperformance → perceived failure.

---

## Finding G: Tight Budget (EUR 180K / 6 months)

**Implication:**  
Strict scope prioritization required.
Focus on compliance-ready foundation + measurable early value.

**Second-Order Risk:**  
Budget may not account for infrastructure costs.

---

# 3. Technical & Functional Areas Requiring Investigation

## KPI & Measurement Definition
- Baseline metrics:
  - Current ticket volume
  - AHT (Average Handle Time)
  - Escalation rate
  - Staffing cost
  - Vendor automation coverage
- Monthly board dashboard requirements.

## Platform Definition
- Clarify meaning of “one unified platform”:
  - Integration layer?
  - Governance framework?
  - Vendor consolidation?
- Decision rights model for new AI initiatives.

## Infrastructure & Deployment
- GPU availability and procurement timeline.
- On-prem latency benchmarks (<2s target).
- Monitoring, logging, and audit capabilities.
- PII exclusion strategy.

## Knowledge Governance
- Content inventory and freshness scoring.
- Ownership assignment and editorial workflow.
- Acceptance criteria for KB remediation.

## Adoption & Operating Model
- Agent workflow integration.
- Human-in-the-loop override design.
- Training and communication strategy.

---

# 4. Risk Register (AI-PM)

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| On-prem infra delays | High | Critical | Week 1 feasibility sprint |
| Budget not covering hardware | Medium-High | Critical | Separate infra cost validation |
| Undefined KPI baseline | High | High | Baseline workshop Week 1 |
| Knowledge base quality | High | High | Assign KB owner + remediation plan |
| Adoption resistance | Medium | High | Change management + augmentation framing |
| Compliance scope drift | Medium | High | Early alignment with AI-SEC |
| Tool sprawl / integration conflict | Medium | Medium-High | Platform decision workshop |

---

# 5. Recommended Next Steps (First 2 Weeks)

## Week 1 – Definition & Feasibility

1. KPI Baseline Workshop (CIO + Finance + Helpdesk).
2. Platform Strategy Workshop (integration vs consolidation).
3. On-Prem Feasibility Sprint kickoff.
4. EU AI Act classification session with AI-SEC.
5. Assign Knowledge Base Owner.

## Week 2 – Scope & Alignment

6. Freeze Phase 1 scope aligned to August milestone.
7. Define board-ready dashboard structure.
8. Publish governance charter draft.
9. Initiate change management plan with Helpdesk team.

---

# 6. Cross-Role Dependencies

| Role | Required Input |
|------|----------------|
| FDE | GPU sizing, infra feasibility, latency benchmarks |
| AI-SEC | EU AI Act classification, audit controls |
| AI-DS | Model evaluation thresholds, hallucination mitigation |
| AI-DA | KPI baseline design, dashboard framework |
| ServiceNow SMEs | Current automation scope & integration constraints |

---

# Phase 1 Success Definition (AI-PM Framing)

By August 2026, EuroHealth must have:

- A defined AI governance framework
- On-prem AI deployment validated
- Documented EU AI Act readiness
- Board-ready KPI dashboard
- Demonstrable progress toward 30% cost reduction

---

# Conclusion

This engagement is a governance-led industrialization program, not a feature build.  

The primary AI-PM responsibility is to:

- Protect the sponsor’s board narrative
- Validate feasibility before commitment
- Define measurable success early
- Structure Phase 1 to enable scalable Phase 2

Success will be measured not only by automation rate, but by executive confidence, compliance defensibility, and controlled expansion capability.