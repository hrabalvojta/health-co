# Solution Design — EuroHealth AI Helpdesk
## Architecture Blueprint (Co-Design Phase Deliverable)

**Version:** 0.1 DRAFT
**Date:** <!-- date -->
**Primary Authors:** FDE, AI-SE
**Contributors:** All roles
**Status:** Under development (Day 13)

**Prerequisite:** [Consolidated Discovery Report](../discovery/consolidated-discovery-report.md)

---

## 1. System Overview

### 1.1 What We Are Building

<!-- FDE: 2-3 sentences. What is the system, who uses it, what does it do? -->

### 1.2 Design Principles

<!-- Derived from discovery findings. Examples: -->
<!-- - Governance-first: every AI response passes through policy enforcement -->
<!-- - On-prem only: no data leaves EuroHealth infrastructure -->
<!-- - Auditability: every decision is logged and reconstructable -->
<!-- - Incremental: Phase 1 handles L1 tickets only -->

### 1.3 Out of Scope (Phase 1)

<!-- Explicitly list what we are NOT building. This prevents scope creep. -->

---

## 2. Architecture Overview

### 2.1 High-Level Pipeline

```
┌─────────┐    ┌───────────┐    ┌───────────┐    ┌─────────┐    ┌──────────┐
│  User    │───▶│ Retriever │───▶│ Generator │───▶│   PEP   │───▶│ Response │
│  Query   │    │ (RAG)     │    │ (LLM)     │    │ (Policy │    │          │
└─────────┘    └───────────┘    └───────────┘    │  Check) │    └──────────┘
                    │                               │    ▲         │
                    ▼                               │    │         ▼
              ┌───────────┐                    ┌────┴────┐   ┌──────────┐
              │ Vector DB │                    │   PDP   │   │  Audit   │
              │ (Confluence│                   │ (Policy │   │   Log    │
              │  2000 docs)│                   │  Rules) │   │          │
              └───────────┘                    └─────────┘   └──────────┘
                                                    ▲
                                                    │
                                              ┌─────────┐
                                              │ YAML    │
                                              │ Policies│
                                              └─────────┘
```

### 2.2 Component List

| Component | Owner | Technology | Status |
|-----------|-------|-----------|--------|
| User Interface | AI-FE | <!-- web app, Teams integration, etc. --> | Design |
| API Gateway | FDE | <!-- --> | Design |
| Retriever (RAG) | FDE | <!-- vector DB, embedding model --> | Design |
| Generator (LLM) | FDE + AI-SE | <!-- on-prem LLM selection --> | Pending infra validation |
| Policy Engine (PDP) | AI-SEC + AI-SE | YAML rules + Python evaluator | Design |
| Policy Enforcement (PEP) | FDE + AI-SEC | Pipeline middleware | Design |
| Audit Logger | AI-SE | <!-- structured logging --> | Design |
| Monitoring Dashboard | AI-DA | <!-- Grafana, custom, etc. --> | Design |
| Golden Dataset | AI-DS | JSON question/answer pairs | Design |
| ServiceNow Integration | AI-SE | <!-- REST API --> | Pending API validation |

---

## 3. Component Specifications

### 3.1 Retriever (RAG Pipeline) — FDE

<!-- 
FDE: Describe the retrieval system.
- Source: 2,000 Confluence pages (EN/DE/CZ)
- Chunking strategy: how do you split documents?
- Embedding model: which one, why? (must run on-prem)
- Vector store: which one, why?
- Top-K retrieval: how many chunks per query?
- Relevance threshold: minimum confidence score?
-->

### 3.2 Generator (LLM) — FDE + AI-SE

<!--
- Model selection: which LLM, why? (must run on-prem)
- Hardware requirements: GPU, RAM, storage
- Context window: how much context per request?
- Temperature / sampling: settings and rationale
- Prompt template: system prompt structure
- Language handling: EN/DE/CZ strategy
-->

### 3.3 Policy Engine (PDP/PEP) — AI-SEC + FDE

<!--
AI-SEC: Describe the governance enforcement layer.
- PDP: How are policy rules evaluated?
- PEP: Where exactly in the pipeline does enforcement happen?
- Policy format: YAML structure and rule types
- Actions: block, redirect, escalate, redact, allow
- Fallback behavior: what happens if PDP is unreachable?
- Refer to: governance/policies/*.yaml
-->

### 3.4 Audit & Logging — AI-SE

<!--
- What gets logged: every PEP decision, every query, every response
- Log format: structured JSON (refer to governance/evidence/audit-log-schema.json)
- Retention: how long, where stored
- Reconstruction: how to answer "what happened on March 15 at 14:32?"
- EU AI Act Article 12 requirements
-->

### 3.5 Monitoring & Metrics — AI-DA

<!--
- KPI definitions: auto-resolve rate, escalation accuracy, override rate, etc.
- Collection points: where in the pipeline are metrics captured?
- Dashboard views: operational vs. board-level
- Alerting: when does a human get paged?
- Refer to: monitoring/dashboard-spec.md
-->

### 3.6 Evaluation Framework — AI-DS

<!--
- Golden dataset: size, coverage, language split
- Evaluation metrics: accuracy, precision, recall, F1
- Bias testing: cross-language performance comparison
- Drift detection: how to identify degradation over time
- Refer to: tests/golden_dataset/
-->

### 3.7 User Interface — AI-FE

<!--
- Interface type: web app / Teams integration / both
- Streaming: real-time response display
- Confidence indicators: how does the user see trust?
- HITL controls: override button, escalation trigger
- Policy block UX: what does the user see when PEP blocks?
- Accessibility: WCAG requirements
- Refer to: governance/operating-model/human-override-protocol.md
-->

---

## 4. Interface Contracts

> Detailed contracts in [interface-contracts.md](interface-contracts.md)

Summary of cross-component interfaces:

| From | To | Data | Format | Protocol |
|------|----|------|--------|----------|
| UI | API Gateway | User query + session | JSON | REST/WebSocket |
| API Gateway | Retriever | Query text + language | JSON | Internal |
| Retriever | Generator | Query + retrieved chunks | JSON | Internal |
| Generator | PEP | Draft response + metadata | JSON | Internal |
| PEP | PDP | Response + policy context | JSON | Internal |
| PDP | PEP | Decision (allow/block/redirect) | JSON | Internal |
| PEP | Audit Logger | Decision record | JSON | Async |
| PEP | UI | Final response OR block message | JSON | REST/WebSocket |
| All components | Monitoring | Metrics + traces | <!-- --> | <!-- --> |

---

## 5. Deployment Model — AI-SE

### 5.1 On-Premises Topology

<!-- 
- Container orchestration: Docker Compose / Kubernetes
- Network topology: which components talk to which
- Storage: where does vector DB live, where do logs go
- Scaling: can we handle 12 concurrent helpdesk agents?
-->

### 5.2 CI/CD Pipeline

<!--
- Source control: Git repository structure
- Policy validation: YAML lint on every commit
- Testing: unit tests, integration tests, golden dataset eval
- Deployment: blue/green or rolling update strategy
- Rollback: how to revert to previous version
-->

---

## 6. Constraints & Assumptions

| Constraint | Source | Impact on Architecture |
|-----------|--------|----------------------|
| On-premises only | Hans Müller (CIO) | LLM must run on local GPU |
| €180K total budget | Board-approved | Limits hardware procurement |
| 6-month timeline | Board review August 2026 | Phased delivery required |
| EU AI Act compliance | Regulatory | Audit trail mandatory |
| 3 languages (EN/DE/CZ) | 8-country operation | Multilingual embedding + generation |
| 2,000 Confluence pages | Existing knowledge base | ~30% outdated, needs quality filter |

## 7. Architecture Decision Records

| # | Decision | Alternatives Considered | Rationale |
|---|----------|------------------------|-----------|
| ADR-001 | <!-- e.g., "Use YAML for policy format" --> | <!-- JSON, Rego, Markdown --> | <!-- Why YAML won --> |
| ADR-002 | <!-- e.g., "PEP after generation, not before" --> | <!-- Pre-generation filter --> | <!-- Why post-gen is better --> |
| ADR-003 | | | |

> Full ADR details in [architecture-decisions.md](architecture-decisions.md)

---

## 8. Risk Assessment (Architecture-Specific)

| Risk | Probability | Impact | Mitigation | Owner |
|------|------------|--------|-----------|-------|
| On-prem GPU insufficient for chosen LLM | Medium | Critical | Validate before model selection | FDE |
| ServiceNow API doesn't support required operations | Medium | High | API audit in Week 1 | AI-SE |
| Policy engine adds >500ms latency | Low | Medium | Performance testing in Sprint 1 | FDE + AI-SEC |
| Knowledge base quality degrades results | High | High | Quality filter + confidence threshold | AI-DS |

---

## Appendices

- [Interface Contracts — Detailed](interface-contracts.md)
- [Architecture Decision Records](architecture-decisions.md)
- [Data Flow Diagram](data-flow-diagram.md)
- [Deployment Model](deployment-model.md)
