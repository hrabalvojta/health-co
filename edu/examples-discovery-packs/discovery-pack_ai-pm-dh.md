# Discovery Packet v3 — AI Product Manager (AI-PM)
## Student: Daniel Hort
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: At board level, what outcome remains unsatisfactory despite achieving ~35% L1 ticket deflection?
**Why this matters:** Clarifies whether this engagement is about operational efficiency or enterprise governance transformation.  
**Red flag (bad answer):** “We just want better ticket routing.”  
**KAF component:** Agentic Core

---

### Question 2: How are your AI systems currently classified under EU AI Act risk categories, and who signs off on that classification?
**Why this matters:** Risk tier determines governance depth, conformity assessment obligations, and documentation requirements.  
**Red flag (bad answer):** No formal classification exists.  
**KAF component:** Policy-as-Code / Run Safe

---

### Question 3: If an EU AI Act audit occurred tomorrow, what evidence could you produce within 48 hours?
**Why this matters:** Tests operational compliance maturity and audit readiness.  
**Red flag (bad answer):** “We would need time to prepare documentation.”  
**KAF component:** Run Safe

---

### Question 4: Are you prepared to shut down non-compliant AI tools—even if they are popular internally?
**Why this matters:** Governance without enforcement authority fails in practice.  
**Red flag (bad answer):** Hesitation or political avoidance.  
**KAF component:** Policy-as-Code

---

### Question 5: What identity and authorization boundaries exist between ServiceNow, legacy monitoring tools, and departmental AI solutions?
**Why this matters:** Secure MCP/A2A orchestration requires explicit identity, authentication, and authorization design.  
**Red flag (bad answer):** Shared service accounts or unclear ownership.  
**KAF component:** Interop (MCP/A2A) / Run Safe

---

### Question 6: Across 8 EU countries, are there differences in data residency, regulatory interpretation, or language handling that must be enforced at policy level?
**Why this matters:** Multinational complexity impacts policy-as-code implementation and data governance design.  
**Red flag (bad answer):** Assumption of uniformity across countries.  
**KAF component:** Agentic Ingestion / Policy-as-Code

---

### Question 7: What is your target AI governance model—centralized (CISO-led) or federated with centrally enforced policy templates?
**Why this matters:** Determines approval workflows, registry ownership, and long-term scalability.  
**Red flag (bad answer):** Undefined or shared ownership.  
**KAF component:** Policy-as-Code / Human-in-the-Loop

---

### Question 8: If tradeoffs are required within €180K and 6 months, which creates more board value this year: deeper audit instrumentation or broader cross-department rollout?
**Why this matters:** Forces prioritization and protects Phase 1 scope from overcommitment.  
**Red flag (bad answer):** “Everything is priority.”  
**KAF component:** Agentic Core

---

### Question 9: If Phase 1 proves regulatory readiness and unified monitoring, is expansion funding for HR and Claims pre-committed for 2027?
**Why this matters:** Determines whether to architect for pilot isolation or enterprise scale from Day 1.  
**Red flag (bad answer):** No visibility on future investment.  
**KAF component:** Agentic Core / Interop

---

### Question 10: If this program were to fail, what would most likely cause it—budget constraints, political resistance, technical complexity, or regulatory uncertainty?
**Why this matters:** Surfaces hidden delivery risks and organizational friction early.  
**Red flag (bad answer):** Inability to identify credible failure modes.  
**KAF component:** Agentic Core / Human-in-the-Loop

---

> Minimum coverage achieved:
> - Policy-as-Code: Q2, Q4, Q6, Q7  
> - Interoperability (MCP/A2A): Q5, Q9  
> - Human-in-the-Loop: Q7, Q10  

---

## Part 2: KAF Mapping (mini)

| KAF Component        | Covered by Q# | Notes |
|----------------------|---------------|-------|
| Agentic Core         | 1, 8, 9, 10   | Strategic direction & prioritization |
| Agentic Ingestion    | 6             | Multinational data & policy ingestion |
| Policy-as-Code       | 2, 4, 6, 7    | Governance enforcement & classification |
| Digital Trust (Run Safe) | 2, 3, 5 | Audit, identity, regulatory readiness |
| Human-in-the-Loop    | 7, 10         | Governance ownership & risk awareness |
| Interop (MCP/A2A)    | 5, 9          | Cross-system orchestration |

---

## Part 3: Assumptions / Risks / Open Items (3–5)

1. €180K may be insufficient if identity integration and registry enforcement are more complex than anticipated.
2. Governance ownership between CIO and CISO may be unclear, slowing decision-making.
3. Shadow AI resistance from HR or Claims could create political friction.
4. EU AI Act interpretation differences across countries may increase policy-as-code complexity.
5. Works council engagement may affect role redesign timelines.

---

## Part 4: What We Will Measure (3 KPI proposals)

1. **AI Registry Coverage:** 0% → 100% of AI systems registered within 6 months.
2. **Regulatory Adaptation Time:** ~3 months → <14 days for policy update deployment.
3. **Audit Evidence Readiness:** Ability to produce compliance documentation within 48 hours.

(Leading indicators: % workflows mapped to policy rules by Month 2; shadow AI detection time <7 days.)

---

## Part 5: Agent Classification

- **Governance tier:** Enterprise Agent  
- **Registry/reuse potential:** Policy-as-Code governance framework reusable for HR and Claims Phase 2; candidate template for regulated EU insurers.

---

## Dependencies on Other Roles:

- **AI-SEC:** Risk classification, threat modeling, and audit control definition.
- **FDE:** On-prem LLM hosting feasibility and API boundary validation.
- **AI-SE:** CI/CD, deployment lifecycle, monitoring integration.
- **AI-DS:** Multilingual knowledge base structure and evaluation methodology.
- **AI-DA:** Executive compliance dashboard and KPI reporting framework.
- **AI-FE:** Accessibility and multilingual UI compliance validation.

---

## Questions I Deliberately Did NOT Ask (and why):

- “Which LLM vendor do you prefer?” — Tactical, not strategic at CIO level.
- Detailed infrastructure specifications — FDE territory.
- Ticket taxonomy structure — AI-DS responsibility.
