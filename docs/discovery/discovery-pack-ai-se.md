# Discovery Packet v1 - AI-SE
## Student: Vojtech Hrabal
## Date: February 26, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: Where is the complete inventory of AI systems and who owns each system?
**Why this matters:** EuroHealth already has Moveworks plus shadow AI in HR and Claims. Without an owner-based inventory, we cannot unify governance or define release accountability.
**Red flag (bad answer):** "We do not have a single list; teams run what they need."
**KAF component:** Agentic Core / Digital Trust

### Question 2: What does your current deployment topology look like across dev, test, and prod?
**Why this matters:** On-prem only is a hard constraint. AI-SE needs environment separation, deployment controls, and rollback design before any scale-up.
**Red flag (bad answer):** "Most changes are made directly in production."
**KAF component:** Agentic Core / Run Safe

### Question 3: How are model, prompt, and policy changes promoted today?
**Why this matters:** AI artifacts need CI/CD controls, approvals, and release evidence to avoid undocumented behavior drift.
**Red flag (bad answer):** "We update prompts manually and copy settings between systems."
**KAF component:** Run Safe

### Question 4: Which governance policies are already enforceable in code versus only documented in slides?
**Why this matters:** Day 13-14 requires Policy-as-Code, not paper policy. We need machine-enforceable rules for PII, scope limitation, and escalation.
**Red flag (bad answer):** "Policies exist in PDF documents, teams follow them manually."
**KAF component:** Policy-as-Code

### Question 5: Can you reconstruct one AI decision end-to-end in under 24 hours?
**Why this matters:** EU AI Act readiness depends on traceable logs across query, retrieval, model version, policy decision, and human override.
**Red flag (bad answer):** "We only keep generic infrastructure logs."
**KAF component:** Digital Trust / Run Safe

### Question 6: How do you prevent PII from entering ingestion, prompts, responses, and logs?
**Why this matters:** The knowledge base is known to be low quality (~30 percent outdated). Data controls must be enforced at ingestion and runtime.
**Red flag (bad answer):** "Users are told not to upload sensitive files."
**KAF component:** Agentic Ingestion / Policy-as-Code

### Question 7: What interoperability contracts exist for ServiceNow APIs and future MCP/A2A integration?
**Why this matters:** AI-SE must design stable contracts for cross-system actions, error handling, and fallback if dependent systems fail.
**Red flag (bad answer):** "The API exists, but nobody has tested external integration."
**KAF component:** Interop (MCP/A2A) / Agentic Core

### Question 8: Where are Human-in-the-Loop checkpoints mandatory and what are the override SLAs?
**Why this matters:** High-risk operations need explicit handoff rules and accountability for human override paths.
**Red flag (bad answer):** "We prefer full automation and decide ad hoc when to involve humans."
**KAF component:** Human-in-the-Loop / Run Safe

### Question 9: Which SLOs and operational alerts are required for AI runtime reliability?
**Why this matters:** Adoption fails when latency, escalation behavior, and policy decision health are not monitored continuously.
**Red flag (bad answer):** "We only monitor server uptime."
**KAF component:** Run Safe

### Question 10: What budget and hardware limits define feasible model choices for Phase 1?
**Why this matters:** EuroHealth has a tight EUR 180K / 6-month window. AI-SE needs costed infra assumptions for realistic delivery planning.
**Red flag (bad answer):** "Pick the best model first; we will discuss cost later."
**KAF component:** Agentic Core / Interop

---

## Part 2: KAF Mapping (mini)

| KAF Component | Covered by Q# | Notes |
|---|---|---|
| Agentic Core | 1, 2, 7, 10 | Ownership, deployment topology, integration strategy, scaling constraints |
| Agentic Ingestion | 6 | Data quality and PII control in ingestion pipeline |
| Policy-as-Code | 4, 6 | Runtime guardrails plus ingestion safety controls |
| Digital Trust | 1, 5 | Registry accountability and replayable evidence |
| Human-in-the-Loop | 8 | Human escalation and override protocol |
| Interop (MCP/A2A) | 7, 10 | API contracts, dependency handling, feasible rollout scope |

---

## Part 3: Assumptions / Risks / Open Items (3-5)

1. ServiceNow APIs are available but not yet production-proven for external AI orchestration.
2. AI system ownership is fragmented; shadow AI may be broader than current CIO awareness.
3. Budget may not include full on-prem GPU expansion, which can force a smaller model strategy.
4. Logging exists, but not in a schema suitable for compliance reconstruction.
5. Helpdesk adoption risk is high if override and escalation UX is unclear.

---

## Part 4: What We Will Measure (3 KPI proposals)

1. **Change control maturity:** 100 percent of AI changes (model/prompt/policy) released through CI/CD with approval trail.
2. **Audit readiness:** 95 percent+ of production interactions have complete trace fields required for reconstruction.
3. **Operational safety:** Mean time to policy-related incident detection below 15 minutes with enforced escalation path.

---

## Part 5: Agent Classification

- **Governance tier:** Enterprise
- **Registry/reuse potential:** High; deployment and policy guardrail pattern can be reused for regulated clients.

---

## Dependencies on Other Roles:

- **FDE:** Runtime topology, GPU sizing, network constraints, and performance envelopes.
- **AI-SEC:** Rule taxonomy, threat model, and governance control requirements.
- **AI-DS:** Data quality gates and evaluation methodology for multilingual content.
- **AI-DA:** Compliance and reliability dashboard definitions.
- **AI-PM:** Scope lock, timeline risk decisions, and stakeholder escalation path.

## Questions I Deliberately Did NOT Ask (and why):

- "What is final business case priority by department?" (AI-PM ownership)
- "What are exact legal interpretations per article?" (AI-SEC and legal ownership)
- "What UX copy and trust labels should users see?" (AI-FE ownership)
