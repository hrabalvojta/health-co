# Discovery Packet v1 — AI Software Engineer (AI-SE)

**Client:** EuroHealth Insurance AG  
**Focus:** Industrializing AI (On-Prem, EU AI Act Ready, 6 Months / €180K)

---

# Part 1 — Discovery Questions (10)

---

## Q1. Where does your current ServiceNow + Moveworks setup hit the wall from a governance, scaling, or operational standpoint?

**Why it matters:**  
Identifies the true enterprise limitation and clarifies why vendor-native AI is insufficient for industrialization.

**Red flag:**  
“We’re not hitting any limitations.” → Signals low governance visibility or underestimation of risk.

**Assumptions / Risks / Open Items:**
- Vendor-native controls may not extend beyond IT.
- Governance gaps likely emerge in cross-department scaling.
- Operational maturity may be inconsistent across business units.
- Lack of enterprise-wide AI operating model.

**KAF:** Core / Policy-as-Code / Run Safe

---

## Q2. Can you walk us through every AI-driven system currently running — including departmental prototypes — and clarify which are production versus experimental?

**Why it matters:**  
Industrialization requires full AI inventory and environment classification.

**Red flag:**  
“We don’t have a complete overview.” → Indicates shadow AI and lack of governance registry.

**Assumptions / Risks / Open Items:**
- No centralized AI registry.
- Inconsistent environment labeling (prod vs test).
- Unknown risk exposure from experimental systems.
- Unmonitored access to sensitive systems.

**KAF:** Ingestion / Interop / Run Safe

---

## Q3. How are AI updates deployed today — do you have dev, staging, and production separation?

**Why it matters:**  
Environment separation is foundational for safe release management and regulatory validation.

**Red flag:**  
“We update directly in production.” → No AI DevOps maturity.

**Assumptions / Risks / Open Items:**
- No CI/CD pipeline for AI artifacts.
- Manual deployment processes.
- Lack of rollback discipline.
- Inconsistent change management documentation.

**KAF:** Run Safe

---

## Q4. If an AI update caused misrouting, compliance issues, or instability, how quickly could you revert to a known-good state?

**Why it matters:**  
Rollback capability defines production resilience and operational readiness.

**Red flag:**  
“We fix issues manually when they appear.” → No version control or recovery framework.

**Assumptions / Risks / Open Items:**
- No versioned configuration management.
- No automated rollback mechanism.
- High operational downtime risk.
- No rollback time objective defined.

**KAF:** Run Safe

---

## Q5. What unified monitoring and observability do you have across ServiceNow, legacy tools, and departmental AI solutions?

**Why it matters:**  
Enterprise AI requires centralized monitoring for governance and risk detection.

**Red flag:**  
“Each department monitors independently.” → Fragmented oversight.

**Assumptions / Risks / Open Items:**
- No unified logging layer.
- Lack of cross-system alerting.
- Delayed incident detection.
- No single pane of glass for AI operations.

**KAF:** Run Safe / Interop

---

## Q6. Can you trace an AI-assisted decision end-to-end — including inputs, policy checks, tool calls, and final outcomes?

**Why it matters:**  
Traceability is essential for EU AI Act defensibility and audit compliance.

**Red flag:**  
“We only log final outputs.” → Insufficient audit depth.

**Assumptions / Risks / Open Items:**
- Partial logging.
- No decision chain transparency.
- No model/version linkage in logs.
- No policy enforcement trace evidence.

**KAF:** Run Safe / Policy-as-Code

---

## Q7. Which governance or compliance rules today are documented but not technically enforced?

**Why it matters:**  
Identifies gap between narrative policies and enforceable guardrails.

**Red flag:**  
“We rely on process compliance.” → No Policy-as-Code layer.

**Assumptions / Risks / Open Items:**
- Policies exist only in documentation.
- No automated policy enforcement.
- Risk of human inconsistency.
- Audit defensibility gaps.

**KAF:** Policy-as-Code

---

## Q8. How are AI systems authenticated and authorized when accessing internal systems?

**Why it matters:**  
Enterprise agents must operate within strict IAM boundaries.

**Red flag:**  
Shared service accounts or unclear IAM model.

**Assumptions / Risks / Open Items:**
- Lack of least-privilege model.
- Weak access boundary enforcement.
- Potential cross-department data exposure.
- No centralized access review.

**KAF:** Interop / Run Safe

---

## Q9. Given the on-prem constraint, what is your strategy for LLM hosting, lifecycle management, and patching?

**Why it matters:**  
On-prem AI requires disciplined infrastructure and model lifecycle governance.

**Red flag:**  
“No formal lifecycle process.” → Security and operational risk.

**Assumptions / Risks / Open Items:**
- Unclear model version governance.
- No patching cadence.
- No performance validation cycle.
- Infrastructure scaling constraints.

**KAF:** Core / Run Safe

---

## Q10. As you scale AI across departments and languages (EN/DE/CZ), what bottlenecks or integration limitations are emerging?

**Why it matters:**  
Scaling complexity reveals architectural and governance weaknesses.

**Red flag:**  
“We haven’t evaluated cross-department scaling.” → No enterprise architecture planning.

**Assumptions / Risks / Open Items:**
- Language model inconsistencies.
- Integration bottlenecks.
- Localized governance differences.
- Increased operational overhead.

**KAF:** Core / Ingestion / Interop

---

# KAF Coverage Summary

| KAF Component      | Covered By |
|--------------------|------------|
| Core               | Q1, Q9, Q10 |
| Ingestion          | Q2, Q10 |
| Policy-as-Code     | Q1, Q6, Q7 |
| Run Safe           | Q1–Q9 |
| HITL               | (Indirect — governance & escalation design) |
| Interop            | Q2, Q5, Q8, Q10 |

---

# Agent Classification

- **Tier:** Enterprise Agent  
- **Reason:** Cross-department use, regulated environment, EU AI Act exposure  
- **Governance:** Full registry, audit, monitoring, and enforcement required

---

# What We Will Measure (AI-SE KPIs)

1. **Rollback Time Objective:** < 30 minutes to revert AI configuration changes.
2. **End-to-End Trace Coverage:** 100% AI-assisted decisions traceable.
3. **Deployment Discipline:** 100% AI changes via version-controlled CI/CD (no direct production edits).

---

# Dependencies on Other Roles

- **AI-SEC:** Regulatory interpretation, control enforcement scope.
- **AI-DS:** Data quality, evaluation metrics, KB design.
- **AI-DA:** Dashboarding and KPI instrumentation.
- **AI-PM:** Budget prioritization and phase scope.
- **AI-FE:** HITL workflow and escalation UX design.

---

# Questions I Deliberately Did NOT Ask (and Why)

- Detailed data modeling strategy → AI-DS scope.
- Business ROI calculations → AI-PM scope.
- Detailed threat modeling → AI-SEC scope.
- UI accessibility specifics → AI-FE scope.
- Legal interpretation of EU AI Act → AI-SEC / Legal scope.

---