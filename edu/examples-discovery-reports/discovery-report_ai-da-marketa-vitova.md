# Discovery Report

## EuroHealth Insurance AG

### Role: AI Data Analyst (AI-DA)

### Date: 2026-02-24

------------------------------------------------------------------------

# Executive Summary

## 1.1 Purpose
Translate Hans Muller’s goals into a data-driven discovery for EuroHealth’s AI-enabled helpdesk program.
* 1.2 Scope
On-prem, EU Act–compliant, ServiceNow–integrated AI helpdesk with unified governance.
* 1.3 Desired Outcomes
Define measurable ROI, governable data pipelines, and auditable metrics that stakeholders can trust.
Stakeholder Analysis (from the Data Analyst perspective)

## 2.1 Primary Sponsor
Hans Muller (CIO): Demands auditable ROI, governance, and regulatory readiness; on-prem constraint is non-negotiable.
* 2.2 Secondary Stakeholders
Stefan Weber (CISO): Security-first, drives logging, policy enforcement, PII controls.
Katarina Novak (IT Ops Director): Wants reliable, maintainable on-prem architecture and SLA realization.
Jan Kovar (Helpdesk Lead): Frontline user advocate; concerns about team displacement and adoption.
Shadow-AI Owners: HR, Claims, Finance leads with existing, ungoverned tools (PoCs).
* 2.3 Governance/Gatekeepers
Data Stewards: KB owner, ServiceNow data steward, IT Ops steward, Shadow-AI owners.
* 2.4 Interdependencies
ServiceNow integration, KB health, policy-as-code, audit capabilities, and on-prem infrastructure readiness.
Day 11 Discovery Questions (Top 3–5 Prompts Used or Relevant)

## 3.1 Discovery Questions (Data Analyst lens)
How do we measure ROI today, and what data would prove a 30% cost reduction if we unify governance and AI?
What data sources will feed the ROI dashboards, and how will we ensure end-to-end data lineage for audits?
What governance controls must be in place before we deploy a unified on-prem AI platform (policy, logging, PII handling)?
How will we handle shadow AI tools to avoid governance gaps without stalling progress?
What are the constraints and acceptance criteria for on-prem GPUs and latency, given the 6-month window?
Hans Muller’s Roleplay Learnings (Synthesis)

## 4.1 Confirmed Points
Moveworks/ServiceNow handles basic tickets.
Shadow AI presence (HR chatbot, Claims PoC) with governance gaps.
Success metrics: 30% cost reduction, unified platform, EU Act compliance by Aug 2026.
Constraints: On-prem only; cloud not allowed.
Data quality gap: KB ~30% outdated; ownership unclear.
Change management risk: Jan’s team fears replacement.
Budget/time: EUR 180K for 6 months, tight.
* 4.2 Open Questions / New Issues Emerged
Exact KPIs, data sources, and cadence to prove 30% reduction.
Concrete scope for “unified platform” (gateway model, policy enforcement, L2 autonomy).
On-prem infrastructure plan (GPU sizing, storage, network, DR).
Specific pre/post generation governance policies to implement at launch.
KB ownership and remediation ownership for 30% outdated content.
Change management plan for frontline staff (Jan’s team).
Detailed governance plan for shadow AI (risk register, mitigation backlog).
Multilingual data handling (EN/DE/CZ) routing and analytics implications.
Data Inventory and Quality (Foundational Inputs)

## 5.1 Data Sources
ServiceNow tickets (languages: EN/DE/CZ), ticket types, SLAs, resolution times.
Confluence KB pages (2,000; 30% outdated) with metadata (last update, owner).
Employee directory with PII-restricted fields.
On-prem logs and infrastructure telemetry (GPU sizing, latency, CPU/memory).
Shadow AI footprints (HR chatbot, Claims LangChain PoC, Finance GPT) and usage data.
* 5.2 Data Quality Risks
KB stale rate target: <5% within 6–8 weeks.
Ticket data gaps: missing multilingual routing fields, mislabelled categories.
PII handling gaps: logs may expose PII if not masked.
* 5.3 Ownership
KB owners (business/product), ServiceNow data steward, IT Ops steward, Shadow-AI owners (HR/Claims/Finance).
Data Lineage and Observability

## 6.1 End-to-End Data Flow
Source: ServiceNow tickets and KB content.
Transform: AI layer for retrieval, augmentation, triage.
Target: final resolution outcomes + metrics (auto-resolve, escalations).
Consumption: executive dashboards (board-ready) and operator dashboards (operational).
* 6.2 Data Storage and Lineage Guarantees
On-prem vector store/index with explicit lineage tags.
Versioned KB snapshots; ticket-history lineage preserved.
* 6.3 Reliability Metrics
Data freshness, completeness, deduplication rate, schema stability across sprints.
KPI Framework and Success Metrics

## 7.1 Primary Business KPIs (Linked to 30% Cost Reduction)
Auto-resolve rate (L1 tickets resolved without human handoff).
First-contact resolution rate improvement.
Average handle time reductions attributable to AI.
Deflection rate of repetitive inquiries.
CSAT delta (target +0.9 to reach 4.2+ from 3.6).
* 7.2 Governance/Compliance KPIs
Audit log completeness and queryability (EU AI Act Art.12).
Policy enforcement hits (pre- and post-generation).
PII filtering hits and masking coverage.
* 7.3 Shadow AI Tracking
Shadow AI usage volume, per-tool ownership, risk indicators, remediation status.
* 7.4 KB Health Metrics
Staleness rate, remediation cadence, ownership accountability.
* 7.5 Data Lineage Health
End-to-end traceability score, data quality gates pass rate.
Governance and Policy Alignment

## 8.1 Policy-as-Code Strategy (PDP/PEP)
Pre-generation: input validation, data scope restrictions, PII screening.
Post-generation: content filtering, escalation triggers, audit event logging.
* 8.2 Data Governance Controls
Access controls, data minimization, masking rules, retention schedules.
* 8.3 Compliance Mapping
EU AI Act alignment: Art.12, Art.14, Art.15, Art.50.
* 8.4 Auditability Design
Immutable logs, tamper-evident logs, exportable audit trails.
Architecture Alignment and Constraints

## 9.1 On-Prem Constraints
No cloud transit; latency budgets; GPU sizing assumptions; sovereign data custody.
* 9.2 Autonomy Model
L2 Constrained Autonomy: auto-resolve L1 tickets within guardrails; human oversight.
* 9.3 Integrations
ServiceNow as primary source; KB search/index; LDAP/HR data with masking.
* 9.4 Shadow-AI Governance Placement
Central policy enforcement and auditing across shadow tools.
Risks and Mitigations (Data Analyst Lens)

## 10.1 Data and Governance Risks
KB quality risk impedes ROI realization; mitigated by a KB health sprint.
Shadow AI governance gaps risk regulatory exposure; mitigated by PDP/PEP and logging.
* 10.2 Operational Risks
On-prem latency and GPU capacity risk; mitigated by phased rollout and performance testing.
Change management risk with Jan’s team; mitigated by inclusive training and early win stories.
* *0.3 Compliance Risks
EU AI Act non-compliance risk; mitigated by mapping to Art.12–Art.50 and auditable trails.
Recommended Next Steps (First 2 Weeks)

## 11.1 Data & Governance Foundations
Complete KB health assessment; assign owners; initiate remediation plan.
Define data lineage maps for ServiceNow tickets and KB-to-resolution flow.
Draft initial PDP/PEP policy templates for pre/post generation.
* 11.2 KPI and Dashboard Design
Lock in KPI definitions (auto-resolve rate, CSAT delta, deflection, FCR) and data sources.
Prototyping: design a minimal executive dashboard prototype showing ROI signals.
* 11.3 On-Prem Infra & Security Readiness
Validate GPU sizing plan and latency budgets; confirm on-prem storage/throughput feasibility.
Run a data masking and PII risk assessment on logs and ticket data.
* 11.4 Stakeholder Engagement
Schedule alignment sessions with Hans, Stefan, Katarina, and Jan to confirm priorities and ownership.
Establish shadow-AI governance charter and incident-response touches.
* 11.5 Risk Mitigation Planning
Create a risk register focusing on data quality, governance gaps, and change management.
Dependencies on Other Roles

## 12.1 With AI/DS (Data Scientist)
Data pipelines, feature definitions, and ROI modeling inputs.
* 12.2 With AI/PM (Product/Program Manager)
Alignment on milestones, governance milestones, and deliverables.
* 12.3 With AI/SEC (Security)
Logging, PII controls, policy enforcement, and audit readiness.
* 12.4 With FDE (Field/Delivery Ecosystem)
Logging norms, runbooks, incident response, and monitoring integration.
* 12.5 With Stakeholders
Hans (sponsor ROI), Stefan (security/compliance), Katarina (ops), Jan (adoption).
Attachments and Artifacts (to be developed)
Data lineage diagrams (ServiceNow → AI layer → resolution).
KB health scorecard and ownership map.
Draft KPI definitions and data source inventory.
Initial PDP/PEP policy templates (on-prem deployment).
Shadow-AI risk register draft.

Final Considerations
This discovery report should feed Day 12 planning: translate these findings into architecture decisions, policy designs, and initial dashboards.
Ensure language remains business-facing for Hans while preserving data rigor for the governance and compliance narrative.
Prepare to update the report with stakeholder feedback and early data findings from sprint work.







