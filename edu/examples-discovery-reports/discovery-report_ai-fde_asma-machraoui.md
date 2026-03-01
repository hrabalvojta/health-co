# Discovery Report --- FDE

Client: EuroHealth Insurance AG\
Role: Field Delivery Engineer (FDE)\
Author: Asma Machraoui\
Date: Feb 24, 2026

------------------------------------------------------------------------

## 1. Executive Summary

Based on the EuroHealth brief and the CIO roleplay session, this
engagement is not simply about building an AI helpdesk assistant. It is
about industrializing and governing fragmented AI systems across the
organization.

During the roleplay, Hans emphasized: - Existing AI tools (Moveworks, HR
chatbot, Claims prototype) - 30% cost reduction target - Compliance
readiness by August 2026 - On-prem constraint (non-negotiable) - Team
morale concerns

From an FDE perspective, success means designing a governed, auditable,
on-prem AI runtime that reduces helpdesk costs while consolidating AI
experimentation into one controlled platform.

------------------------------------------------------------------------

## 2. Stakeholder Analysis

-   Hans Muller (CIO) -- Decision-maker; needs measurable cost reduction
    and visible compliance progress for board reporting.
-   Katarina Novak (IT Ops) -- Owns infrastructure and ServiceNow;
    critical for integration feasibility and procurement timelines.
-   Stefan Weber (CISO) -- Drives EU AI Act compliance; defines policy
    and audit expectations.
-   Jan Kovar (Helpdesk Lead) -- Adoption gate; team morale directly
    impacts automation success.
-   Shadow AI Owners (HR & Claims) -- Potential blockers if
    consolidation threatens autonomy.

Implication: Architecture decisions must satisfy technical feasibility,
compliance governance, and adoption stability simultaneously.

------------------------------------------------------------------------

## 3. Key Findings

### Finding 1 --- Fragmentation is the Core Problem

Hans revealed multiple ungoverned AI tools. Therefore, the primary
architectural objective is platform unification, not feature expansion.

### Finding 2 --- On-Prem Constraint Drives Architecture

"No cloud" requires GPU feasibility validation, orchestration maturity
assessment, and hardware budget alignment within €180K.

### Finding 3 --- ServiceNow API Is a Risk Area

API exists but is not externally used. A technical spike is required to
validate write permissions, rate limits, and identity model.

### Finding 4 --- KB Quality Limits Automation

With \~30% outdated KB, confidence thresholds and HITL gating are
mandatory before auto-resolution can scale safely.

### Finding 5 --- Compliance Is a Visible Success Metric

EU AI Act readiness must be demonstrable through traceability and
evidence generation within 24 hours.

------------------------------------------------------------------------

## 4. Technical Requirements to Validate

-   On-prem inference runtime with HA and peak-load resilience\
-   ServiceNow secure write integration with RBAC and throttling\
-   Centralized policy-as-code enforcement layer\
-   Full audit trail (model version, data source IDs, policy decisions)\
-   Automated PII detection/redaction\
-   HITL thresholds and safe degradation mode\
-   Multilingual support validation (EN/DE/CZ)

------------------------------------------------------------------------

## 5. Risk Assessment

  -----------------------------------------------------------------------
  Risk             Impact                Mitigation
  ---------------- --------------------- --------------------------------
  Hardware         Delays Phase 1        Week-1 feasibility assessment
  procurement                            
  exceeds budget                         

  ServiceNow write Operational           API spike + circuit breaker
  instability      disruption            

  Data drift from  Low automation        Confidence gating + KB audit
  outdated KB      accuracy              

  Shadow AI        Governance failure    Agent registration model
  persists                               

  Low adoption     ROI failure           Phased rollout + override
  from helpdesk                          monitoring
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 6. First 2 Weeks Plan

Week 1: - Infrastructure feasibility analysis (cost + HA)\
- ServiceNow API spike (read/write test)\
- Shadow AI inventory\
- KB + PII sampling

Week 2: - Audit logging prototype (demonstrate trace in \<24h)\
- Draft policy-as-code enforcement approach\
- HITL workflow workshop with Jan\
- Technical Go/No-Go risk review with Hans & Stefan

------------------------------------------------------------------------

## 7. Decision Gates

-   Gate 1: On-prem infrastructure viable within budget\
-   Gate 2: ServiceNow write boundary validated\
-   Gate 3: Audit trace demonstrable in \<24h\
-   Gate 4: HITL thresholds approved

------------------------------------------------------------------------

## 8. Dependencies

-   AI-SEC: EU AI Act classification and required evidence fields\
-   AI-PM: Procurement and budget allocation confirmation\
-   AI-DA: Baseline metrics (misroute %, CSAT 3.2 baseline, resolution
    time 4h)\
-   AI-DS: KB quality audit methodology\
-   AI-FE: UI explainability and escalation design\
-   IT Ops: ServiceNow sandbox + infra inventory

------------------------------------------------------------------------

## 9. KPIs (Aligned to Brief)

-   30% cost reduction within 6 months\
-   Reduce misroute rate from 10% toward \<3%\
-   Improve CSAT from 3.2 to \>4.0\
-   MTTE (audit trace) \< 24 hours\
-   Inference availability ≥ 99.5%

------------------------------------------------------------------------

## 10. 12--18 Month Outlook

If Phase 1 succeeds, this governed runtime can support additional AI use
cases across HR and Claims. Therefore, modular model design and
centralized policy enforcement are necessary to avoid recreating
fragmentation.
