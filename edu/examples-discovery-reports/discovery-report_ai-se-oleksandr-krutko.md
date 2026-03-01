# Discovery Report AI-SE

Author: Oleksandr Krutko
Role: AI-SE
Client: EuroHealth Insurance AG
Date: Feb 24, 2026

## Observation
### ServiceNow already integrated with Moveworks.
1) Is REST APIs are exposed internally or can be open for external tool?

2) Is there any user directory (e.g, MS Windows AD)

It means: how we can use the potential of the existing tools?

### Shadow AI exists and is ungoverned
1) Which KB storage is used for each tool?

2) What is the API to interact with Shadow AU?

It means: I need to design a governance-friendly technical backbone: registry, versioning, access control, logs, evaluation evidence

### ~30% of Confluence pages are outdated
1) Which format is used for existing Knowledge base?

2) How it was ingested?

3) Who is responsible for update the KB?

It means: We can use the existing KB, RAG, documents. We can either extend the existing RAG or crate new one.

### Each team use its own AI tool
1) Which platform is used to run each tool?

2) Which tools are used to deploy a tool?

It means: We can use computation resources which are utilized by the existing AI tool. If no room to run existing resources the it is necessary to expand the budget.

## Risks
1) Platform Lock-In & Architectural Conflict (High) -> additional licenses are needed -> the budget expansion

2) Identity & RBAC Misalignment (High) -> AI responses might access data across domains (HR → Claims → IT) without proper separation -> that is a serious EU AI Act + GDPR exposure

3) Each Team Uses Its Own AI Tool -> the governance implies people education and limit of their freedom -> quietly sabotage

## Cross-role dependencies:
AI-SE - EU AI Act compliance

AI-PM - Budget exhaustion

FDE - Architectural decision
