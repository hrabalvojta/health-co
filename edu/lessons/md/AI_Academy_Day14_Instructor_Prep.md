# AI Academy 2026 — Day 14 Instructor Preparation
# "Governance Day — EU AI Act Meets Reality"

**Date:** Thursday, February 26, 2026
**Theme:** EU AI Act Compliance + Role-Specific Governance Deliverables
**Day in sequence:** Day 14 (Week 4, Day 4)

---

## Day Overview

| Time | Slot | Duration | Style |
|------|------|----------|-------|
| 9:00–9:03 | Bridge from Day 13 (3 Pillars + architecture → governance) | 3 min | Lecturer live, 200 people |
| 9:03–9:15 | **Hans Before the Board** — WOW Role-Play (Scene A, B, C) | 12 min | Lecturer live, role-play |
| 9:15–9:30 | Sprint 1: EU AI Act Classification — Is EuroHealth High-Risk? | 15 min | Team decision with AI Tutor |
| **9:30–9:35** | **⚡ Checkpoint 1: "EuroHealth is [HIGH-RISK / LIMITED RISK] because..."** | **5 min** | **Mandatory post in role channel** |
| 9:35–9:55 | Sprint 2: Policy-as-Code + Role-Specific Governance Artifact | 25 min | Individual with AI Tutor |
| **9:55–10:00** | **⚡ Checkpoint 2: "For [ROLE]'s governance to work, they need MY component to..."** | **5 min** | **Mandatory post in role channel** |
| 10:00–10:15 | Sprint 3: Continue, Refine & Cross-Reference | 15 min | Individual (continue Sprint 2 work) |
| 10:15–10:30 | Plenary Wrap-Up: Auditor Returns + Key Message + Day 15 preview | 15 min | Interactive + screen share |

**OFFLINE (after session, at home):**

| Time | Activity | Duration |
|------|----------|----------|
| Offline Block 1 | Cross-role governance review (recommended pairings) | 30 min |
| Offline Block 2 | Finalize governance deliverable + align with Day 13 architecture | 30 min |
| Offline Block 3 | Cert prep | 30 min |

---

## STORY ARC: DAY 10 → 11 → 12 → 13 → 14

```
Day 10 (Friday):    WHAT NOT TO DO
                    HealthCare Co. — audit a failed prototype
                    Lesson: skipping discovery = governance failures

Day 11 (Monday):    ASK THE RIGHT QUESTIONS
                    EuroHealth Insurance — write discovery questions
                    Lesson: your role determines what you notice

Day 12 (Tuesday):   LISTEN TO THE ANSWERS
                    EuroHealth Insurance — CIO answers, write report
                    CP2: "I need [ROLE] for [TOPIC]" (abstract dependency)

Day 13 (Wednesday): BUILD IT TOGETHER
                    EuroHealth Insurance — architecture from discovery
                    CP2: interface contracts (concrete specs)

Day 14 (Thursday):  GOVERN IT  ← YOU ARE HERE
                    EuroHealth Insurance — governance for your component
                    CP1: "My architecture is MISSING [governance gap]"
                    CP2: "For [ROLE]'s governance to work, they need MY component to..."
```

**The checkpoint evolution across the week:**
| Day | CP2 Theme | Abstraction Level |
|-----|-----------|-------------------|
| Day 11 | "I stole this from [peer]" | Peer influence (intra-role) |
| Day 12 | "I need [ROLE] for [TOPIC]" | Abstract dependency |
| Day 13 | Interface contract (format, send, receive, error) | Concrete technical spec |
| **Day 14** | **"For [ROLE]'s governance, they need MY component to..."** | **Governance requirement on YOUR component** |

---

## PLENARY OPENING (9:00–9:15)

### 1. Bridge from Day 13 — Three Pillars (3 min)

> **Say:** "Good morning. Let me connect the dots — one more time."

> "Day 10: you saw what happens without governance. Day 11: you asked the right questions. Day 12: the CIO answered. Day 13: you built Pillar 1 — discovery and architecture in `docs/`."

> "Today you build **Pillar 2** — the `governance/` folder. Tomorrow: **Pillar 3** — `src/`, the code that enforces your policies."

> "Today's principle: **Every EU AI Act article maps to a file in your project. If the file doesn't exist, you're not compliant.**"

### 2. "Hans Before the Board" — WOW Role-Play (12 min)

**PERFORMANCE SCRIPT — Play two characters live:**
- **Hans Müller** (CIO) — nervous, fidgeting with notes, apologetic
- **EU AI Act Auditor** — cold, methodical, clipboard in hand

---

**SCENE A: Hans WITHOUT Governance (4 min)**

> *Set the stage:* "August 2026. EuroHealth board room. Hans Müller, the CIO, presents the AI helpdesk project. Five board members. Five questions."

**Board Member 1:** "Who is responsible for the AI system in HR?"
> **Hans:** "I... we have an HR chatbot, but I'm not sure who manages it exactly."

**Board Member 2:** "What happened on March 15th at 14:32 when an employee complained?"
> **Hans:** "I would need to ask IT. We don't have a centralized log."

**Board Member 3:** "How do you prevent the AI from leaking salary data?"
> **Hans:** "We... told the developers to be careful with the training data."

**Board Member 4:** "Show us the compliance documentation."
> **Hans:** "We have internal notes... I can compile something by next week."

**Board Member 5:** "The fine is up to €15 million. Who takes responsibility?"
> **Hans:** *Silence.*

> *Pause. Let the silence sit for 3 seconds.* **"€15M risk exposure. CIO credibility damaged."**

---

**SCENE B: EU AI Act Auditor Arrives (4 min)**

> *Switch character — stand straighter, colder voice:* "Now an auditor arrives. Clipboard. No emotion. Five checks."

| Check | EU AI Act Article | Result | Penalty |
|-------|------------------|--------|---------|
| AI System Registry | Art. 49 — Registration | ✗ No registry | €2M |
| Risk Classification | Art. 6 — Classification | ✗ Not determined | €3M |
| Technical Documentation | Art. 11 — Documentation | ✗ No architecture doc | €3M |
| Audit Trail / Logging | Art. 12 — Record-keeping | ✗ No structured logs | €3M |
| Human Oversight | Art. 14 — Human oversight | ✗ No override protocol | €4M |

> *Read each row aloud. After each "✗", write the cumulative total on the board/screen.*

> **"€15M — or 3% of annual turnover."**

---

**SCENE C: Hans WITH Your Governance Folder (4 min)**

> *Switch back to Hans, but confident now:* "Same board room. Same questions. But this time Hans has the `governance/` folder your team built today."

**Q1: "Who is responsible?"**
> Hans opens `governance/compliance/ai-inventory.md` — every system registered with owner, risk level, deployment date.

**Q2: "March 15th at 14:32?"**
> Hans pulls up `governance/evidence/audit-log-schema.json` — structured query returns the exact interaction.

**Q3: "Salary data leakage?"**
> Hans shows `governance/policies/pii-protection.yaml` — rule_id, condition, action, log fields.

**Q4: "Compliance documentation?"**
> Hans opens `governance/compliance/eu-ai-act-classification.md` + `governance/operating-model/governance-charter.md`.

**Q5: "Who takes responsibility?"**
> Hans shows the charter's decision rights table — named owners for every article.

> **"Zero findings. Board confidence restored."**

---

> *Pause. Then:* **"The difference between Scene A and Scene C is one folder: `governance/`. Today you fill it."**

### 3. Digital Omnibus Reality Check (2 min)

> **Say:** "Now — a real-world update. Some of you may have heard: the EU has a legislative package called the Digital Omnibus on the table. It may push the EU AI Act enforcement for high-risk systems from August 2026 to late 2027."

> *Pause. Let it sink in.*

> "Some companies are celebrating. 'We have more time!' But remember what Hans said on Day 12? 'If I can show the board a compliance-ready platform before the August deadline, I keep my job.' Hans's board didn't delay their expectations. The August evidence pack is still due."

> "And here's the GDPR lesson: GDPR was adopted in 2016 with a 2-year preparation window. Many companies celebrated the runway. When enforcement hit in May 2018, unprepared companies paid tens of millions. The companies that prepared early? They turned compliance into a competitive advantage — winning contracts because they were already certified while competitors scrambled."

> **"The requirements didn't change. The fines didn't change. The articles didn't change. Only the enforcement clock shifted. What you do with that extra time separates junior consultants from senior ones. Today we prepare as if the deadline is tomorrow."**

### 4. Launch Work (1 min)

> **Say:** "Three sprints, two checkpoints. Sprint 1: classify EuroHealth. Sprint 2: fill your governance file. Sprint 3: governance charter. Prompts are in Teams chat. Go."

---

## PRE-WRITTEN BROADCAST MESSAGES

### Launch (paste at 9:15):
```
🚀 GOVERNANCE SPRINT — STARTING NOW

Sprint 1 (9:15–9:30): EU AI Act Classification — Is EuroHealth high-risk?
  → Fill: governance/compliance/eu-ai-act-classification.md
⚡ Checkpoint 1 at 9:30: "EuroHealth is [HIGH-RISK / LIMITED RISK] because [reasoning]. My role owns: [requirements]."
Sprint 2 (9:35–9:55): Policy-as-Code + Role-Specific Governance Artifact
  → Each role fills their specific file in governance/ (see table in HTML)
⚡ Checkpoint 2 at 9:55: "For [ROLE]'s governance to work, they need MY component to [capability]"
Sprint 3 (10:00–10:15): Continue, Refine & Cross-Reference
  → Review Sprint 2 artifact, add Decision Rights entry to governance-charter.md

📌 WHERE TO SUBMIT:
  → Checkpoint text posts (CP1, CP2): your role's MS Teams channel
  → Governance files: ZIP your entire governance/ folder → shared OneDrive/SharePoint folder
  → ZIP naming: day14-[role]-governance.zip (e.g. day14-FDE-governance.zip)

Open your Day 13 docs/architecture/ alongside your work today.
Today's principle: Every EU AI Act article maps to a file. If the file doesn't exist, you're not compliant.
```

### Checkpoint 1 (paste at 9:30):
```
⚡ CHECKPOINT 1 — EU AI ACT CLASSIFICATION

Post in your role's Teams channel:
"EuroHealth is [HIGH-RISK / LIMITED RISK] because [reasoning].
My role owns: [specific requirements from Art. 9-15 + Art. 50]."

Examples:
- FDE: "EuroHealth is HIGH-RISK because it routes employee tickets (Annex III,
  Cat. 4). My role owns: Art. 10 data governance (supporting) + Art. 12
  record-keeping (supporting). My Day 13 architecture is MISSING structured audit logs."
- AI-SE: "HIGH-RISK. I own Art. 11 technical documentation + Art. 12 record-keeping.
  My CI/CD pipeline is MISSING a policy validation gate."
- AI-DA: "HIGH-RISK. I own Art. 12 logging + Art. 14 human oversight (dashboard).
  My monitoring is MISSING compliance KPIs."
- AI-FE: "HIGH-RISK. I own Art. 14 human oversight (UI) + Art. 50 transparency.
  My UI is MISSING AI disclosure label."

This is NOT a failure. This is how architecture and governance iterate.
Read 3 peer posts. React to 1.
```

### Checkpoint 2 (paste at 9:55):
```
⚡ CHECKPOINT 2 — CROSS-ROLE GOVERNANCE REQUIREMENT

Post in your role's Teams channel:
"For [OTHER ROLE]'s governance to work, they need MY component to [specific capability]."

Examples:
- FDE: "For AI-DA's compliance dashboard to work, they need MY PEP to log
  every policy decision with timestamp, rule_id, action, and query_hash."
- AI-SEC: "For FDE's guardrails to work, they need MY policy YAML files
  to follow a parseable schema with rule_id, condition, action, and log fields."
- AI-DS: "For AI-PM's FRIA to be evidence-based, they need MY evaluation results
  with per-language accuracy scores (EN/DE/CZ) and bias metrics."
- AI-FE: "For AI-PM's transparency compliance, they need MY UI to show
  AI disclosure label, confidence score, and 'talk to human' button."

Notice: today's CP2 is the REVERSE of Day 12-13.
Then: "I need YOU." Now: "YOU need ME to provide [X]."
This shift = ownership of YOUR component's governance obligations.
```

### Wrap-up transition (paste at 10:15):
```
⏰ SPRINTS COMPLETE — WRAP-UP TIME

Make sure your governance/ files are saved and uploaded.

What counts as "done" today:
✅ eu-ai-act-classification.md has a risk determination with reasoning
✅ Your role-specific governance file has content (not empty template)
✅ You posted Checkpoint 1 AND Checkpoint 2 messages

That's three real deliverables. Everything else is refinement.
We're about to run the auditor's checklist again — let's see how you did.
```

---

## AI TUTOR STARTING PROMPTS

**Three prompts for three sprints — post each at sprint start in Teams chat:**

### Sprint 1 Prompt (post at 9:15):
```
EuroHealth Insurance operates across 8 EU countries. Their AI
helpdesk processes IT support queries from 12,000+ employees in
English, German, and Czech. It routes tickets, answers policy
questions, and escalates complex issues.

Help me classify this system under the EU AI Act:
1. Is it in Annex III? Which category?
2. Does it make decisions affecting workers?
3. What is the cross-border complexity?
4. Final classification: HIGH-RISK or LIMITED RISK?
5. Map Articles 9-15 + Art. 50 to roles: FDE, AI-SE, AI-DS,
   AI-DA, AI-PM, AI-FE, AI-SEC.

I'm a [ROLE]. For each article assigned to my role, identify:
- What evidence I need to produce
- Where in my Day 13 architecture that evidence comes from
- What governance gaps exist

Output as governance/compliance/eu-ai-act-classification.md
```

### Sprint 2 Prompt (post at 9:35):
```
EuroHealth Insurance's AI helpdesk is classified as HIGH-RISK
under EU AI Act Annex III (workplace AI system). The board requires
governance artifacts before go-live. EU AI Act requirements
(Art. 9-15) apply. I'm a [YOUR ROLE]. Help me create my governance
artifact for the governance/ folder:

- FDE: Fill governance/operating-model/governance-charter.md
  (pipeline/PEP section). PDP/PEP configuration for 3 policy types
  (PII protection, scope limitation, escalation). What gets blocked,
  redacted, logged.
- AI-SE: Fill governance/evidence/audit-log-schema.json. Define
  the logging schema: every query, response, policy decision with
  timestamp, rule_id, action, query_hash. Plus CI/CD gate criteria.
- AI-DS: Fill governance/compliance/eu-ai-act-classification.md
  (evaluation/bias section). Bias detection plan for EN/DE/CZ +
  fairness metrics. Test methodology for equal quality across langs.
- AI-DA: Fill monitoring/dashboard-spec.md. 5 compliance KPIs with
  thresholds. Policy violations, audit completeness, incident
  tracking, human override frequency.
- AI-PM: Fill governance/operating-model/governance-charter.md.
  FRIA + decision rights matrix + incident response protocol +
  policy change process.
- AI-FE: Fill governance/operating-model/human-override-protocol.md.
  Trust UI patterns: AI disclosure label, confidence indicator,
  human escalation button, feedback mechanism, language indicator.
- AI-SEC: Fill governance/policies/*.yaml. Write YAML policy rules
  for PII protection, scope limitation, escalation. Each rule:
  rule_id, condition, action, log fields. Plus red team plan (10
  attack scenarios).

My Day 13 architecture includes these interface contracts:
[paste your Day 13 Checkpoint 2 interface contract here]

Challenge me if my governance document is generic — push for
EuroHealth specifics, article numbers, and concrete thresholds.
```

### Sprint 3 Prompt (post at 10:00):
```
I'm contributing to EuroHealth's governance charter at:
governance/operating-model/governance-charter.md

My role is [ROLE]. Help me write my section:
1. Decision Rights Matrix — who approves, overrides, is notified
2. Incident Response — escalation path for MY component
3. Policy Change Process — how changes get approved
4. Human Override Protocol — how a human overrides MY component

Reference specific EU AI Act articles. Be concrete about
thresholds, SLAs, and named roles.
```

---

## INDIVIDUAL WORK — SPRINT STRUCTURE (9:15–10:15)

### Sprint 1: EU AI Act Classification (9:15–9:30, 15 min)

**Students:**
1. Open Day 13 architecture documents in `docs/architecture/` alongside new work (2 min)
2. Paste Sprint 1 AI Tutor prompt — ALL roles contribute to classification (3 min)
3. Fill `governance/compliance/eu-ai-act-classification.md`: Is EuroHealth high-risk? Map 8 requirements to roles (10 min)
4. Focus on REASONING: why this classification, which articles apply, what evidence is needed

**Mentors:**
- If student just writes "HIGH-RISK" without reasoning, DM: "WHY is it high-risk? Which Annex III category? What decisions does it make that affect workers?"
- Ensure students map each article to a specific role owner — this sets up Sprint 2
- If a student argues LIMITED RISK, don't shut it down — push for documented reasoning: "If the auditor challenges your classification, what evidence supports it?"

### ⚡ Checkpoint 1 (9:30) — "EuroHealth is [HIGH-RISK / LIMITED RISK] because..."

**Lecturer pastes broadcast message at 9:30.**

**What happens:** Each role channel fills with classification reasoning + role-specific requirement ownership. Students also declare gaps from Day 13.

**Why this is pedagogically powerful:**
- Forces students to articulate REASONING, not just labels
- Public declaration of requirement ownership = accountability
- Mentors see which articles are under-covered (no role claiming ownership)
- Creates the Day 13→14 iterative loop: architecture informs governance, governance reveals gaps

**Mentors at Checkpoint 1:**
- React to 3-4 posts within 2 minutes
- If reasoning is too vague ("it's high-risk because it uses AI"), DM: "Which Annex III category? What SPECIFIC decisions does it make that affect workers?"
- Note common patterns: which articles are nobody claiming? Flag to Lecturer
- If a student says "no gaps in my Day 13 work," DM: "Does your architecture log every policy decision? Can a human override any response? Check again."

### Sprint 2: Policy-as-Code + Role-Specific Artifact (9:35–9:55, 25 min)

**This is where the real work happens.** Each role fills their specific governance file:

| Role | File to Fill |
|------|-------------|
| AI-SEC | `governance/policies/*.yaml` (YAML policy rules) |
| AI-PM | `governance/operating-model/governance-charter.md` |
| FDE | `governance/operating-model/governance-charter.md` (pipeline/PEP section) |
| AI-SE | `governance/evidence/audit-log-schema.json` |
| AI-DA | `monitoring/dashboard-spec.md` |
| AI-DS | `governance/compliance/eu-ai-act-classification.md` (evaluation/bias section) |
| AI-FE | `governance/operating-model/human-override-protocol.md` |

**Students:**
5. Read 3 peer Checkpoint 1 posts — incorporate relevant classification insights
6. Paste Sprint 2 AI Tutor prompt — role-specific, referencing exact governance/ files
7. Fill their specific file with EU AI Act article references, thresholds, test cases
8. Think about Checkpoint 2: what does YOUR component need to provide for OTHER roles?

**Mentors:**
- This is the busiest moment — watch for unanswered cross-role questions
- DM coaching: "You're an FDE. The AI-DA needs compliance data from your PEP. What log format are you sending? Does it include rule_id?"
- If AI-SEC has only 3-4 attack scenarios: "The plan says 10. Think beyond prompt injection."
- Push YAML specificity: "Show me the actual rule_id, condition, action fields."

### ⚡ Checkpoint 2 (9:55) — "For [ROLE]'s governance, they need MY component to..."

**Lecturer pastes broadcast message at 9:55.**

**What happens:** Students REVERSE the dependency direction. Instead of "I need you" (Day 12-13), they declare "YOU need ME to provide X." This is the ownership flip.

**Why this matters:**
- Most mature cross-role thinking in the program so far
- Students articulating what OTHER roles need from THEM = systems-level governance awareness
- These declarations feed into Sprint 3's refinement and cross-reference work

**Mentors at Checkpoint 2:**
- If a student can't think of what others need, DM: "Look at the requirements table. Which rows have YOUR role in the 'Supporting Role' column?"
- Read posts from other channels mentioning YOUR role — does it align?
- Note: specific, actionable declarations here = strong hackathon team leads

### Sprint 3: Continue, Refine & Cross-Reference (10:00–10:15, 15 min)

**Individual work.** Students continue refining their Sprint 2 artifacts and add a Decision Rights entry to the governance charter.

**Students:**
9. Review Sprint 2 artifact: does it reference specific EU AI Act articles? Are owners named? Are thresholds concrete?
10. Open `governance/operating-model/governance-charter.md`
11. Add ONE entry to the Decision Rights Matrix for YOUR domain: "For [decision in my area], [role] decides, [role] is consulted, [role] is informed."
12. Save all files to `governance/` folder

**ADVANCED (if finished early):**
- Write an incident response scenario for YOUR component: "If [my component] fails, then [escalation path]"
- Read 2 peer Checkpoint 2 posts — does your artifact provide what they said they need from you?
- Add cross-role dependency to the charter

**Realistic expectation:** If students completed Sprint 1 classification AND Sprint 2 role artifact, they've produced real governance output. Sprint 3 polish is bonus — don't stress if they only get partway through.

**Mentors:**
- If students are stuck, redirect to Checkpoint 2 posts: "What did other roles say they need from you? Is it in your artifact?"
- Push for specifics in the Decision Rights entry: "WHO can approve a policy change? What is the SLA? Who gets notified?"
- If a student says they're "done," check: does their governance doc reference specific EU AI Act articles? Are thresholds concrete?

---

## PLENARY WRAP-UP (10:15–10:30)

### 1. "The Auditor Returns" — Interactive Checklist (5 min)

> **Say:** "Remember the auditor from the opening? Let's run that audit again — but now with YOUR work."

> "Type in chat if your team has it:"

| Audit Check | EU AI Act Article | File | Ask |
|-------------|------------------|------|-----|
| AI System Inventory | Art. 49 — Registration | `governance/compliance/ai-inventory.md` | "Who filled this?" |
| Risk Classification | Art. 6 — Classification | `governance/compliance/eu-ai-act-classification.md` | "Who has this?" |
| Technical Documentation | Art. 11 — Documentation | `docs/architecture/` (Day 13 Pillar 1) | "This was Day 13" |
| Audit Trail / Logging | Art. 12 — Record-keeping | `governance/evidence/audit-log-schema.json` | "Who designed this?" |
| Human Oversight | Art. 14 — Human oversight | `governance/operating-model/human-override-protocol.md` | "Who filled this?" |

> **Say:** "If any row is empty — that's tonight's homework. The auditor doesn't wait."

> "Notice: this morning Hans had ZERO. Now you have [count how many hands go up]. That's the difference one day of focused governance work makes."

### 2. "What Counts as Done" Reassurance (2 min)

> **Say:** "Three deliverables today. That's it."

> "✅ `eu-ai-act-classification.md` has a risk determination with reasoning."
> "✅ Your role-specific governance file has content — not an empty template."
> "✅ You posted Checkpoint 1 AND Checkpoint 2 messages."

> "That's three real deliverables. Everything else is refinement. If any row in the audit table is empty — that's tonight's homework. The auditor doesn't wait."

### 3. Key Message + Tomorrow Preview (8 min)

> **Say:** "Compliance is not a checkbox exercise that happens after you build. It's a design requirement that shapes your architecture from day one. The EU AI Act doesn't just tell you what to document — it tells you what to BUILD."

> "And it doesn't end at go-live. The operational cost of staying compliant is real, ongoing, and — for Kyndryl — a managed services opportunity worth more than the initial build."

> "The checkpoint evolution this week tells the story: Day 12 — 'I need you.' Day 13 — 'Here's our contract.' Day 14 — 'You need ME.' That shift from asking for help to owning your obligations is the mark of a systems thinker."

> **Say:** "Status check. Your 3-pillar project:"

```
eurohealth-helpdesk/
├── docs/           ← Pillar 1 (Day 11-13) ✅ DONE
├── governance/     ← Pillar 2 (Day 14)    ✅ TODAY
└── src/            ← Pillar 3 (Day 15)    ⬜ TOMORROW
```

> **Say:** "Tomorrow — Day 15 — Pillar 3. The `src/` folder comes alive. Your YAML policies from today will be loaded by the policy engine you write tomorrow. The code ENFORCES these policies."

> "Tonight: align your Pillar 1 and Pillar 2 files. Fix Checkpoint 1 gaps. Verify Checkpoint 2 obligations are in your governance artifacts. If someone asks 'what does compliance cost per month?' — have an answer (review the Operational Cost table)."

---

## POST-SESSION: COPILOT TRACKING

### In each role channel:
```
Summarize all messages posted in this channel today.
Create a table with columns:
- Name
- Checkpoint 1: Architecture governance gap declared
- Checkpoint 2: Cross-role governance obligation declared
- Cross-role responses: Did they respond to requests from other roles?
- Other posts (blockers, reactions, etc.)

List channel members who did not post anything today.
```

### Cross-role governance dependency map:
```
From ALL role channels, extract all Checkpoint 2 posts.
Create a table:
- Student name | Their role | Role that needs them | What they must provide
- Also: cross-reference with Day 13 CP2 interface contracts — are they consistent?

Additionally compile Checkpoint 1 gap patterns:
- Most common gap per role
- Students who found no gaps (potential blind spots)
```

**The governance dependency map + gap patterns become input for Day 15 Go/No-Go preparation.**

---

## MENTOR ACTIVITY — Day 14

### Before session:
- [ ] Review Day 13 Checkpoint 2 interface contract posts from your role channel
- [ ] Read the EU AI Act requirements-to-role mapping table
- [ ] Understand checkpoint timing: Checkpoint 1 (9:35), Checkpoint 2 (9:55)

### During session:
- [ ] Watch plenary opening (EU AI Act classification + requirements mapping)
- [ ] **At Checkpoint 1 (9:35):** React to 3-4 gap posts within 2 min. Push vague gaps to be specific (WHICH article?).
- [ ] **During Sprint 2 (9:40-9:55):** DM coaching focused on "translate governance requirement into your architecture." If AI-SEC has <7 attack scenarios, push harder.
- [ ] **At Checkpoint 2 (9:55):** Read obligation posts. Cross-reference: does what role A says they provide match what role B says they need?
- [ ] DM students who missed checkpoints

### After session:
- [ ] Review 5-8 governance/ folder submissions per student
- [ ] Focus: do governance files reference specific EU AI Act articles? Are thresholds concrete? Is there classification reasoning?
- [ ] Check: do governance artifacts align with Day 13 architecture in `docs/architecture/`? (If architecture says "PEP before response" but no PEP rules in governance → misalignment)
- [ ] Flag common quality issues to Lecturer: "My [role]s mostly have [gap]"
- [ ] **CRITICAL — Junior/Senior assessment input:** By end of Day 14, provide preliminary sorting:
  - **Junior tier:** Discovery + Architecture + Governance form a coherent story. Shows cross-role awareness. Checkpoint posts are specific and actionable.
  - **Senior tier:** Documents exist but may not be connected. Focuses only on own role without integration. Checkpoint posts are vague or missing.
- [ ] Report preliminary tier sorting to Lecturer by end of Day 14

### What mentors should flag:
- Students whose CP1 gap + CP2 obligation show deep systems thinking → strong hackathon leads
- Students who wrote "no gaps" at CP1 → likely missing something, need review
- Students whose governance doc contradicts their architecture doc → need alignment help before Day 15

---

## OFFLINE ASSIGNMENTS (90 min total)

### Block 1: Cross-Role Governance Review (30 min)

**Recommended pairings — same logic as before, but now governance-specific:**

| Your role | Review with | What to check |
|-----------|------------|---------------|
| FDE | AI-SEC | "Do my guardrails match your policy rules? Anything I'm missing?" |
| AI-SEC | FDE | "Are my policy rules technically enforceable in your architecture?" |
| AI-PM | AI-SEC | "Does my FRIA align with your red team findings? Any gaps?" |
| AI-DS | FDE | "Does my eval plan cover the scenarios in your guardrails spec?" |
| AI-DA | AI-PM | "Does my compliance dashboard track what your FRIA checklist requires?" |
| AI-FE | AI-PM | "Do my trust UI patterns satisfy the transparency requirements in your checklist?" |
| AI-SE | AI-SEC | "Does my CI/CD pipeline enforce the policy validation you need?" |

### Block 2: Finalize + Align Documents (30 min)
- Incorporate peer review feedback
- **CRITICAL:** Ensure consistency across all three pillars:
  - `docs/discovery/` → `docs/architecture/` → `governance/` (Pillar 1 → Pillar 2)
  - Does your discovery report's stakeholder analysis appear in your governance FRIA?
  - Does your architecture's PEP design match your governance guardrails spec?
  - Do your Day 13 CP2 interface contracts appear in your governance dependencies?
- Fix any Checkpoint 1 gaps you declared today
- Prepare for tomorrow: Pillar 3 (`src/`) will enforce your policies in code

### Block 3: Cert Prep (30 min)

### Videos (optional):

| ID | Title | Cat | Length | For whom |
|----|-------|-----|--------|----------|
| B9 | FRIA Walkthrough — Fundamental Rights Impact Assessment | B | 8-10 min | PM+SEC |
| B19 | How Much Does AI Cost — TCO for Non-Finance People | B | 12-15 min | ALL (PM+DA) |
| A11 | "The Client Says NO" — Objection Handling for Technical People | A | 10-12 min | ALL |
| C10 | GDPR + AI — Practical Compliance (YouTube) | C | ext | PM+SEC |

**Recommended by role:**
- **AI-PM:** B9 + B19 + A11 (~35 min) — prepare for tomorrow's Go/No-Go
- **AI-SEC:** B9 + C10 (~20 min)
- **FDE/AI-SE:** B19 (~15 min) — understand cost implications
- **ALL:** A11 (~12 min) — critical for tomorrow's presentation

---

## INSTRUCTOR PREP CHECKLIST

### Before Day 14:

**Content:**
- [ ] EU AI Act risk classification flowchart ready
- [ ] Requirements-to-role mapping table on screen
- [ ] FRIA example ready (show in HTML, not as separate handout)
- [ ] Videos B9, B19, A11, C10 published and linked

**Sprint infrastructure:**
- [ ] 4 broadcast messages pre-written (launch, Checkpoint 1, Checkpoint 2, wrap-up transition)
- [ ] Timer/alarm set for 9:30 (CP1), 9:55 (CP2), 10:15 (wrap-up)
- [ ] Role channels from Day 11-13 still active
- [ ] Hans + Auditor script rehearsed (12 min role-play opening)

**Removed from v1:**
- ~~Peer Activity: "Pair up with someone from a different role" for 10-min paired review~~ → replaced by CP1 (gap declaration) + CP2 (governance obligation) + offline cross-role review
- ~~Monolithic 60 min (Exercise 1: 45 min + Exercise 2: 15 min)~~ → 3 sprints with 2 checkpoints. Gap Analysis is now CP1.

### Screen shares needed:
1. Hans + Auditor scene cards (in HTML — show on projector during role-play)
2. Audit table from Scene B (5-item penalty table)
3. Requirements-to-role mapping table
4. Role → governance file mapping table (Sprint 2)
5. Sprint AI Tutor prompts (3 prompts for 3 sprints)
6. "Auditor Returns" interactive checklist (wrap-up)
7. "What Counts as Done" checklist (wrap-up)
8. 3-pillar project structure (tomorrow preview)

### Timing notes:
- **Opening role-play is 12 min.** Rehearse beforehand. The WOW moment needs performance energy.
- **Checkpoint broadcasts at 9:30 and 9:55 are non-negotiable. Set alarms.**
- Sprint 2 (25 min) is the longest and most important — resist extending the opening into sprint time.
- Sprint 3 (15 min) is individual polish — students continue refining Sprint 2 work and add Decision Rights entries.
- "Auditor Returns" in wrap-up should take 5 min max — keep it interactive, not lecturing.

---

## KEY TEACHING MOMENTS

> **Central message:**
> "Compliance is not a checkbox exercise that happens after you build. It's a design requirement that shapes your architecture from day one. The EU AI Act doesn't just tell you what to document — it tells you what to BUILD."

> **Cross-role message:**
> "Day 12: 'I need you.' Day 13: 'Here's our contract.' Day 14: 'You need ME to provide X.' That's the shift from individual contributor to systems thinker."

> **Operational cost:**
> "And it doesn't end at go-live. The operational cost of staying compliant is real, ongoing, and — for Kyndryl — a managed services opportunity worth more than the initial build."

> **Architecture-governance loop:**
> "Today's Checkpoint 1 — where you found gaps in yesterday's architecture — is not a failure. It's exactly how real projects work. Architecture and governance iterate. You design, you govern, you redesign."

---

*Document Version: 4.0*
*Updated: February 25, 2026*
*Changes from v3: Sprint 3 changed from "Governance Charter — AI-PM leads" (20 min, collaborative) to "Continue, Refine & Cross-Reference" (15 min, individual). Sprint 2 AI Tutor prompt expanded with per-role detail (specific file content descriptions for each role). Wrap-up simplified: replaced FRIA/Red Team showcase with "What Counts as Done" reassurance note. Added realistic expectations guidance for Sprint 3. Updated broadcast messages to match new Sprint 3 structure.*
*For: AI Academy 2026 — Day 14 Instructor Materials*
