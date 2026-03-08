# CI/CD Governance Gates
## EuroHealth AI Helpdesk - AI-SE Control Plan

**Owner:** AI-SE
**Purpose:** Prevent non-compliant changes from reaching production.

---

## Release Gates

| Gate | What Is Checked | Pass Criteria | Blocking |
| --- | --- | --- | --- |
| Policy syntax gate | YAML parsing + schema shape | All policy files parse and match required fields | Yes |
| Policy regression gate | Known risky prompts against policy engine | All expected block/escalate/redact outcomes pass | Yes |
| Audit schema gate | Runtime audit payload compatibility with `audit-log-schema.json` | Sample payload validates against schema | Yes |
| Unit test gate | Core runtime and policy tests | All tests pass | Yes |
| Artifact integrity gate | Built image hash + dependency lock review | Reproducible image metadata recorded | Yes |
| Deployment smoke gate | Startup + basic request path + logging path | Service starts and emits valid audit event | Yes |

---

## Rollback Criteria

Trigger rollback if any of the following occurs within first hour after deployment:

- policy evaluation failures exceed threshold
- missing audit events for active requests
- critical escalation flow unavailable

Rollback method:

1. stop current release
2. switch to last known-good image
3. verify policy and logging health checks
4. publish incident note

---

## Approval Flow

1. AI-SE prepares release evidence
2. AI-SEC signs off policy and compliance gates
3. AI-PM confirms release window and stakeholder notice
4. Deploy only after all blocking gates pass

