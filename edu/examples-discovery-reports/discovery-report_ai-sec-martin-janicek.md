# Discovery Report - AI-SEC
## Student: Marin Janicek
## Date: February 24, 2026
## Client: EuroHealth Insurance AG

---

## Executive Summary

EuroHealth Insurance is not initiating a greenfield AI deployment - it is attempting to industrialize already fragmented AI capabilities across IT, HR, and Claims under significant board and regulatory pressure. The CIO’s objective is threefold: reduce remaining helpdesk costs by 30%, unify AI initiatives under a single governance framework, and demonstrate EU AI Act readiness before the August 2026 deadline.

From a security perspective, EuroHealth likely already operates unregistered AI systems without centralized auditability or formal risk classification. The existence of shadow AI (HR chatbot and Claims LangChain prototype), combined with a non-negotiable on-premises hosting constraint, creates immediate governance exposure.

AI-SEC must prioritize:
- Enterprise-wide AI system inventory
- Formal EU AI Act risk classification
- Policy-as-Code runtime enforcement
- End-to-end audit trail architecture
- Secure on-prem LLM infrastructure
- Human-in-the-loop governance controls

Security is not a support function in this engagement - it is the structural foundation enabling regulatory defensibility, board credibility, and scalable AI industrialization.

---

## 1. Stakeholder Analysis (Security & Compliance Perspective)

### Hans Muller - CIO (Executive Sponsor)

Hans is under board pressure to demonstrate measurable AI ROI (30% cost reduction) and deliver a compliance-ready AI platform before the August EU AI Act milestone. His statement “If I can show the board a compliance-ready platform before the August deadline, I keep my job” reveals personal accountability tied directly to regulatory readiness.

**Security implication:** Compliance is not a secondary control layer - it is a board-level survival metric. AI-SEC must provide early, demonstrable governance artifacts (AI registry, risk classification, audit trail completeness) that Hans can confidently present to the board.

---

### Stefan Weber - CISO (Compliance Gatekeeper)

Stefan is actively pushing EU AI Act compliance (“keeps emailing about it”). He holds veto power over AI deployment decisions, especially regarding PII handling, audit trails, and model hosting.

**Security implication:** Early alignment with CISO is mandatory. AI-SEC cannot treat compliance as a Phase 2 activity - it is a Day 1 workstream.

---

### Katarina Novak - IT Operations Lead (Infrastructure Owner)

Owns on-prem infrastructure and ServiceNow environment. The “on-prem only” constraint implies security ownership remains internal. GPU provisioning, network isolation, logging, and monitoring fall under her authority.

**Security implication:** Security architecture must integrate into existing on-prem controls, SIEM, and SOC workflows.

---

### Jan Kovar + 12 Helpdesk Agents (Operational Users)

Team fears job displacement. From a security standpoint, disengaged users increase shadow IT behavior, bypassing governance controls and undermining audit traceability.

**Security implication:** Human-in-the-loop controls must be designed transparently to build trust, not surveillance anxiety.

---

### Shadow AI Owners (HR & Claims)

HR chatbot and Claims LangChain prototype operate without central governance. These systems may already process sensitive insurance data.

**Security implication:** EuroHealth likely already operates AI systems without formal risk classification or audit logging. Immediate AI inventory and risk assessment required.

---

## 2. Key Findings & Implications for AI-SEC

### Finding 1: This Is an Industrialization Engagement, Not a Chatbot Project

EuroHealth already operates multiple AI systems (Moveworks within ServiceNow, HR chatbot, Claims LangChain prototype) without centralized governance. The problem is fragmentation and lack of control - not absence of AI capability.

**Security Implication:**  
There is currently no unified AI control plane, no enforceable Policy-as-Code layer, and no centralized audit trail. Shadow AI systems may already process sensitive insurance data without formal risk classification under EU AI Act. Immediate AI system inventory and classification is required before expanding functionality.

---

### Finding 2: EU AI Act Readiness Is a Board-Level Priority

Hans explicitly linked compliance readiness to his credibility with the board and the August deadline. Compliance is not merely regulatory - it is politically critical.

**Security Implication:**  
AI-SEC must prioritize:
- Formal AI system registry
- Risk tier classification (likely high-risk under EU AI Act given insurance context)
- Documented human-in-the-loop mechanisms
- Technical enforcement of data handling rules
- Complete, exportable audit trails

Compliance artifacts must be board-presentable, not only technically implemented.

---

### Finding 3: On-Prem Constraint Shifts Full Security Responsibility to EuroHealth

Cloud deployment is non-negotiable. All model hosting, inference logging, and monitoring will run within EuroHealth’s data center.

**Security Implication:**  
Security controls must cover:
- GPU isolation and model access control
- Network segmentation for LLM inference services
- Secure logging pipelines (no PII leakage into monitoring tools)
- Integration with existing SIEM/SOC systems
- Patch and vulnerability management of open-source LLM stacks

There is no shared cloud security boundary - accountability remains internal.

---

### Finding 4: Knowledge Base Quality Creates Security Risk

~30% of Confluence content is outdated and lacks ownership. AI responses generated from stale content can produce incorrect or non-compliant guidance.

**Security Implication:**  
This is not only a quality issue - it is a liability issue. Incorrect AI-generated instructions may:
- Violate internal policy
- Create audit inconsistencies
- Trigger regulatory scrutiny

AI-SEC must require documented knowledge governance ownership and version tracking as part of compliance controls.

---

### Finding 5: Helpdesk Fear Increases Shadow IT Risk

Jan’s team fears replacement. Distrust in the AI system may lead to workarounds, bypassing logging mechanisms or reintroducing unofficial tools.

**Security Implication:**  
Human-in-the-loop controls must be transparent and traceable. Override actions must be logged and reviewed to prevent compliance blind spots. Adoption risk is a governance risk.

---

## 3. Technical / Functional Requirements (Security Workstream)

Based on the discovery findings, the following security requirements must be investigated and validated before architecture finalization:

---

### 3.1 AI System Inventory & Risk Classification

- Conduct enterprise-wide AI inventory across IT, HR, Claims, and Finance.
- Identify all existing AI systems (Moveworks, HR chatbot, Claims LangChain prototype).
- Classify each system under EU AI Act risk tiers.
- Determine whether helpdesk AI qualifies as high-risk AI (likely given insurance context and potential employment impact).

**Objective:** Establish formal AI registry as the foundation for governance and board reporting.

---

### 3.2 Policy-as-Code Enforcement Layer

Security policies must be technically enforceable, not documented only.

Required controls:
- PII filtering rules (no employee directory ingestion into model training).
- Data routing restrictions across 8 EU countries.
- Model usage restrictions (approved models only).
- Prompt injection protection patterns.
- Output validation filters for sensitive content.

**Objective:** Implement runtime guardrails that prevent policy violations before output is delivered.

---

### 3.3 Audit Trail & Traceability Architecture

AI-assisted decisions must be fully reconstructable.

Required logging:
- Model version used
- Prompt context (sanitized)
- Retrieved knowledge documents (IDs)
- Confidence score (if used)
- Human override events
- Final output delivered to user
- Timestamp and user identity

Audit logs must:
- Be immutable
- Integrate into existing SIEM/SOC
- Support board-level compliance reporting

**Objective:** Achieve 100% end-to-end traceability for AI-assisted actions.

---

### 3.4 On-Prem LLM Security Controls

Given the non-negotiable on-prem constraint:

Security investigation areas:
- GPU isolation model (dedicated vs shared clusters)
- Network segmentation for inference services
- Secure containerization (Docker/Podman hardening)
- Patch management process for open-source LLM frameworks
- Secrets management for API tokens and connectors
- Access control for model administration interfaces

**Objective:** Treat LLM hosting as critical infrastructure, not experimental tooling.

---

### 3.5 Human-in-the-Loop Governance Controls

For L2 autonomy level:

- Define mandatory human confirmation thresholds.
- Log all override actions with reviewer identity.
- Implement periodic review of override patterns.
- Define escalation pathways for ambiguous cases.

**Objective:** Ensure human oversight strengthens compliance rather than becoming an audit blind spot.

---

### 3.6 Shadow AI Decommissioning / Integration Strategy

Existing unauthorized AI deployments must be:
- Brought under governance framework OR
- Decommissioned under formal change management

Security considerations:
- Data migration risk
- Historical log preservation
- Access revocation for deprecated tools

**Objective:** Eliminate uncontrolled AI systems before scaling new platform.

---

## 4. Risk Assessment (AI-SEC)

The following risks are specific to EuroHealth’s current state and must be addressed early in the engagement.

---

### Risk 1: Unregistered High-Risk AI Systems Already in Operation

Shadow AI systems (HR chatbot, Claims LangChain prototype) are operating without centralized governance or formal risk classification.

**Impact:**
- Potential violation of EU AI Act registration and documentation requirements.
- Lack of audit trail for historical AI-assisted decisions.
- Regulatory exposure if discovered during audit.

**Mitigation:**
- Immediate AI inventory within first 2 weeks.
- Temporary freeze on new AI deployments until registry is established.
- Retroactive documentation of existing AI use cases.

---

### Risk 2: Incomplete Auditability Undermines Board-Level Compliance Claims

Current ServiceNow logging does not capture model-level decision context (prompt, retrieved knowledge, override actions).

**Impact:**
- Inability to demonstrate end-to-end traceability.
- Board reporting becomes narrative-based rather than evidence-based.
- Compliance claims become legally vulnerable.

**Mitigation:**
- Define mandatory logging schema before build.
- Implement immutable log storage with retention policy aligned to insurance regulations.
- Run mock audit simulation by Month 3.

---

### Risk 3: On-Prem Infrastructure May Be Inadequate for Secure LLM Hosting

The €180K budget may not account for GPU procurement and hardened hosting environment.

**Impact:**
- Latency >2s may drive users to bypass AI system.
- Security shortcuts may be taken to meet deadline.
- Emergency procurement may exceed budget mid-project.

**Mitigation:**
- Week 1 infrastructure readiness assessment.
- Costed GPU sizing report delivered to AI-PM.
- Explicit separation of hardware cost from governance workstream.

---

### Risk 4: Knowledge Base Quality Creates Legal Liability

30% outdated Confluence content introduces risk of AI-generated incorrect guidance.

**Impact:**
- Incorrect employee instructions.
- Potential policy violations.
- Erosion of trust in AI system.
- Regulatory scrutiny if misinformation affects regulated processes.

**Mitigation:**
- Knowledge audit Phase 0.5 before large-scale rollout.
- Define content ownership model.
- Introduce version tracking and content freshness scoring.

---

### Risk 5: Human Override Without Oversight Becomes Compliance Blind Spot

If helpdesk agents override AI decisions without structured logging and review, governance breaks at the human layer.

**Impact:**
- Loss of traceability.
- Inconsistent enforcement of policy.
- AI Act compliance gap in high-risk classification.

**Mitigation:**
- Mandatory override logging with reviewer ID.
- Monthly override pattern review.
- Threshold triggers for anomaly detection.

---

### Risk 6: Timeline Compression Encourages Governance Retrofits

The 6-month deadline combined with board pressure may incentivize prioritizing visible functionality over invisible controls.

**Impact:**
- Security implemented after go-live.
- Technical debt in audit architecture.
- Increased remediation cost in Phase 2.

**Mitigation:**
- Parallel security workstream from Day 1.
- Governance milestones included in project dashboard.
- Board-facing compliance progress reporting.

---

## 5. Recommended Next Steps (First 2 Weeks)

Given the regulatory pressure, shadow AI exposure, and on-prem constraint, the security workstream must begin immediately and run in parallel with technical architecture.

---

### Week 1: Immediate Control & Visibility

#### 5.1 Launch AI System Inventory (Enterprise-Wide)

- Conduct structured interviews with IT, HR, Claims, and Finance to identify all AI use cases.
- Document system purpose, data sources, autonomy level, and integration points.
- Produce initial AI Registry v0.1 for executive visibility.

**Deliverable:** Draft AI System Registry with preliminary EU AI Act risk classification.

---

#### 5.2 EU AI Act Risk Classification Workshop

- Conduct workshop with CISO (Stefan), Legal, and IT Operations.
- Determine whether helpdesk agent qualifies as high-risk AI.
- Define documentation requirements for compliance readiness by August.

**Deliverable:** Formal risk classification decision + compliance control checklist.

---

#### 5.3 Infrastructure Security Readiness Assessment

- Assess current GPU availability and hosting architecture.
- Review network segmentation and container hardening policies.
- Identify logging pipeline integration points with SIEM/SOC.

**Deliverable:** Infrastructure Security Readiness Memo with identified gaps.

---

### Week 2: Governance Architecture Foundation

#### 5.4 Define Logging & Audit Schema Before Build

- Finalize required logging fields (model version, prompt context, override logs, etc.).
- Define retention policy aligned with insurance regulatory standards.
- Ensure logs are tamper-resistant and reviewable.

**Deliverable:** Approved Audit Logging Specification v1.0.

---

#### 5.5 Define Policy-as-Code Control Framework

- Identify enforceable runtime policies (PII filtering, output validation, routing controls).
- Align with FDE and AI-SE to determine enforcement points.
- Define ownership of policy updates post go-live.

**Deliverable:** Policy-as-Code Control Framework draft.

---

#### 5.6 Shadow AI Containment Strategy

- Determine whether HR and Claims prototypes are to be:
  - Integrated into governance framework, or
  - Decommissioned.
- Freeze expansion of unofficial AI systems until registry established.

**Deliverable:** Shadow AI Governance Decision Document.

---

### Executive Reporting Milestone (End of Week 2)

Prepare a board-facing one-page summary for Hans including:
- AI Registry status
- Risk classification outcome
- Infrastructure readiness status
- Identified security risks & mitigation roadmap

This ensures compliance progress is visible early and aligned with Hans’s board-level commitments.

---

## 6. Dependencies on Other Roles

AI-SEC’s workstream depends on early alignment across multiple roles. Security controls cannot be designed in isolation.

---

### Dependency on FDE (Full-Stack Developer Engineer)

**Need:**  
- On-prem LLM hosting architecture details (model selection, GPU sizing, network topology).
- Enforcement points for runtime guardrails.
- ServiceNow integration design (read/write permissions).

**Why it matters:**  
Security controls such as Policy-as-Code enforcement, network segmentation, and audit logging integration depend on architectural decisions. Without confirmed infrastructure topology, AI-SEC cannot finalize threat modeling or access control boundaries.

---

### Dependency on AI-SE (AI Software Engineer)

**Need:**  
- CI/CD pipeline structure for on-prem deployment.
- Logging integration points.
- Container hardening and patch management workflows.

**Why it matters:**  
Security must be embedded into deployment pipelines from Day 1. If logging, secret management, and validation controls are not built into CI/CD, governance becomes reactive rather than preventative.

---

### Dependency on AI-DS (AI Data Scientist)

**Need:**  
- Knowledge base audit methodology and sampling results.
- Evaluation metrics for hallucination and answer accuracy.
- Data preprocessing and anonymization approach.

**Why it matters:**  
Data quality directly impacts compliance exposure. AI-SEC must understand how hallucination risk is measured and mitigated to properly classify system risk level under EU AI Act.

---

### Dependency on AI-DA (AI Data Analyst)

**Need:**  
- Current baseline metrics (ticket resolution accuracy, escalation rate).
- Definition of board-facing compliance KPIs.
- Monitoring dashboard structure.

**Why it matters:**  
Compliance progress must be measurable. AI-SEC depends on AI-DA to define reporting metrics that demonstrate audit completeness and governance maturity to the board.

---

### Dependency on AI-PM (AI Project Manager)

**Need:**  
- Budget allocation for infrastructure vs governance.
- Timeline phasing decisions (Phase 1 vs Phase 2 scope).
- Stakeholder alignment plan with CISO and Legal.

**Why it matters:**  
Security controls cannot be postponed to later phases due to political and regulatory pressure. AI-SEC requires governance milestones explicitly included in project plan.

---

### Dependency on AI-FE (AI Front-End Developer)

**Need:**  
- Human-in-the-loop UI design (override buttons, confidence indicators).
- User transparency features (source attribution, explanation layer).
- Multi-language UI implications for compliance messaging.

**Why it matters:**  
Compliance is not only backend logging - it includes user transparency. The design of override interfaces and explanation layers directly affects auditability and user trust.