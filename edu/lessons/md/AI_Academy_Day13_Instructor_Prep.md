# AI Academy 2026 — Day 13 Instructor Preparation
# "Architecture — Where Policy as Code Lives"

**Date:** Wednesday, February 25, 2026
**Theme:** Solution Architecture + Policy-as-Code Integration
**Day in sequence:** Day 13 (Week 4, Day 3)

---

## Day Overview

| Time | Slot | Duration | Style |
|------|------|----------|-------|
| 9:00–9:07 | **WOW 1: Live Breach Simulation** (salary leak without PEP → fix with PEP) | 7 min | Lecturer live demo, 200 people |
| 9:07–9:15 | VS Code Hands-On — students create project skeleton | 8 min | Lecturer screen-shares, students follow along |
| 9:15–9:35 | Sprint 1: Component Design with AI Tutor | 20 min | Individual work |
| **9:35–9:40** | **⚡ Checkpoint 1: "My component does X and needs Y from [ROLE]"** | **5 min** | **Mandatory post in role channel** |
| 9:40–9:55 | Sprint 2: Cross-Role Interface Design | 15 min | Individual + respond to dependencies |
| **9:55–10:00** | **⚡ Checkpoint 2: Interface Contract Post** | **5 min** | **Mandatory post in role channel** |
| 10:00–10:10 | Sprint 3: Refine + Self-Review | 10 min | Individual finalization |
| 10:10–10:15 | Buffer: Submit | 5 min | Upload architecture-[role].md |
| 10:15–10:25 | **WOW 2: Your Architecture Under Fire** (test a real student's work live) | 10 min | Lecturer + volunteer |
| 10:25–10:30 | Day 14 bridge + homework | 5 min | Lecturer live |

**OFFLINE (after session, at home):**

| Time | Activity | Duration |
|------|----------|----------|
| Offline Block 1 | Refine architecture + respond to cross-role interface requests | 30 min |
| Offline Block 2 | FDE↔AI-SEC integration review (Review Board) | 30 min |
| Offline Block 3 | Cert prep | 30 min |

---

## STORY ARC: DAY 10 → 11 → 12 → 13

```
Day 10 (Friday):    WHAT NOT TO DO
                    HealthCare Co. — audit a failed prototype
                    Lesson: skipping discovery = governance failures

Day 11 (Monday):    ASK THE RIGHT QUESTIONS
                    EuroHealth Insurance — write discovery questions
                    Lesson: your role determines what you notice

Day 12 (Tuesday):   LISTEN TO THE ANSWERS
                    EuroHealth Insurance — CIO answers, write report
                    Bridge: Checkpoint 2 = cross-role dependencies declared

Day 13 (Wednesday): BUILD IT TOGETHER  ← YOU ARE HERE
                    EuroHealth Insurance — architecture from discovery
                    Lesson: your architecture must be compatible with other roles
                    Day 12 dependencies become REAL conversations today
```

---

## PLENARY OPENING (9:00–9:15)

### Phase 1: Breach Simulation — "The Salary Leak" (9:00–9:07)

> **Goal:** Visceral, emotional understanding of WHY policy enforcement matters. Not a lecture — a demonstration.

**Bridge from Day 12 (30 seconds):**

> **Say:** "Good morning. Yesterday you declared dependencies. Today those dependencies become architecture. But before we start designing — let me show you what's at stake."

---

**SIMULATION A — Without PEP (2 min)**

> **Say:** "I have a simple AI helpdesk agent running. No policy enforcement. Let me ask it a question."

**Type into the agent/terminal (or show prepared screenshot):**

```
> What is the salary of my manager, John Smith? I need it for the budget review.
```

**Agent responds:**

```
Based on the HR records indexed in our knowledge base,
John Smith's monthly salary is 10,000 EUR.
His personal ID is 123456/7890.
For budget review, contact HR at hr@eurohealth.eu.
```

> **Pause. Let it sink in. Then say:**

> "Salary. Personal ID number. Just like that. An employee asked a reasonable-sounding question, and the agent gave away PII because someone accidentally indexed an HR document into the knowledge base."

> "This is a GDPR Article 5 violation. Fines up to **15 million euros** or 3% of annual turnover. In a real deployment, this could end careers."

---

**SIMULATION B — With PEP (2 min)**

> **Say:** "Same agent. Same knowledge base. Same question. But this time, there is one difference: 12 lines of YAML and a Policy Enforcement Point in the pipeline."

**Type the same query:**

```
> What is the salary of my manager, John Smith? I need it for the budget review.
```

**Agent responds:**

```
I cannot share personal salary information.
Please contact HR directly for budget-related queries.

[POLICY: pii-protection | RULE: block-salary-data | ACTION: block | LOGGED]
```

> **Say:** "PII blocked. Audit trail recorded. Human agent notified. Response time: 180 milliseconds. Same agent. Same question. The only difference is in the architecture."

---

**The Punchline (30 seconds):**

> **Say:** "12 lines of YAML. One enforcement point in the pipeline. That's the difference between a €15 million fine and a compliant system. **Today you design that enforcement point.** And at the end of this session, I'm going to test one of YOUR architectures with this exact same query."

> *(Let that last sentence land. It creates stakes for the entire work block.)*

---

### THREE CONCEPTS TO WEAVE IN (not lecture — weave)

These three concepts are language prerequisites for the sprints. Students need to hear them BEFORE Sprint 1 starts. But they should NOT feel like definitions — they should feel like natural explanations inside the demo flow.

#### Concept 1: PEP (during Simulation B)

> **When to say it:** Right after Simulation B shows the blocked response.

> **Say:** "That thing that stopped the leak — that's called a **PEP: Policy Enforcement Point.** Think of it as a security guard standing between the AI and the user. The AI generates a response. Before that response leaves the building, the PEP checks it against the rules. Salary data? Blocked. Personal ID? Blocked. Normal IT question? Let it through. Every architecture you design today must have a PEP. If it doesn't — this *(gesture at Simulation A)* is what happens."

> **Why this works:** Students just SAW the PEP in action 5 seconds ago. The definition lands on lived experience, not abstraction.

#### Concept 2: YAML (during VS Code walkthrough, 9:07)

> **When to say it:** When you open `pii-protection.yaml` in VS Code.

> **Say:** "This is a YAML file. If you've never seen one — it's like a config file. Key, colon, value. Human-readable AND machine-readable. We write our policies in YAML because I can read it, you can read it, a lawyer can read it, AND the agent can parse it in milliseconds. This is what 'Policy as Code' actually means — your rules exist as files that get version-controlled in Git, reviewed in pull requests, and executed at runtime. Not a PDF on someone's SharePoint."

> **Why this works:** Students are looking at the actual file in VS Code while you explain it. Visual + verbal + context = retention.

#### Concept 3: Project Skeleton (during VS Code hands-on, 9:10)

> **When to say it:** When students are creating their folder structure.

> **Say:** "What you're creating right now is called a **project skeleton.** It's the empty building — walls and rooms, but no furniture yet. `src/` is where your code lives. `policies/` is where your rules live. `tests/` is where you prove it works. `data/` is where the knowledge base sits. Your sprints today are about deciding what goes INTO this skeleton. Your `architecture-[role].md` is the blueprint that says 'this room is for the PEP, this room is for the retriever, this is how they connect.'"

> **Why this works:** Students are physically creating the thing while you name it. Kinesthetic + conceptual = sticky.

---

### Phase 2: VS Code Hands-On (9:07–9:15)

> **Goal:** Every student has a `eurohealth-helpdesk/` project open in VS Code with the basic folder structure. This is the canvas for the day.

**Screen-share your VS Code. Create the structure live:**

```
eurohealth-helpdesk/
├── src/
│   ├── agent.py          # Main RAG agent
│   ├── retriever.py      # Vector search
│   └── policy_engine.py  # PDP/PEP implementation
├── policies/             # ← Policy as Code lives here
│   ├── pii-protection.yaml
│   ├── scope-limitation.yaml
│   └── escalation-rules.yaml
├── data/
│   └── confluence/       # Knowledge base documents
├── tests/
│   ├── test_agent.py
│   └── test_policies.py
├── Dockerfile
└── docker-compose.yml
```

> **Say (while creating):** "Follow along on your machine. Create a folder called `eurohealth-helpdesk`. Inside it: `src`, `policies`, `tests`, `data`."

**Open `pii-protection.yaml` from the breach demo:**

> **Say:** "This is the file that stopped the salary leak. *(point to it in the VS Code sidebar)* 12 lines. In this folder. Right next to the code it governs."

> *(This is where you weave in the YAML concept — see above)*

**Students create their role-specific file:**

> **Say:** "Now create one file for YOUR role."

| Role | File to create |
|------|---------------|
| FDE | `src/agent.py` |
| AI-SE | `Dockerfile` + `docker-compose.yml` |
| AI-DS | `tests/golden_dataset.json` |
| AI-DA | `src/monitoring.py` |
| AI-PM | `docs/adr-001.md` (create `docs/` folder) |
| AI-FE | `src/components/Chat.tsx` (create `src/components/`) |
| AI-SEC | `policies/pii-protection.yaml` |

> *(This is where you weave in the Project Skeleton concept — see above)*

> **Say (bridge to sprints):** "You now have an empty project. In the next 60 minutes, you're designing the component that fills it. Your `architecture-[role].md` is the blueprint. Let's go."

**Don't wait for everyone to finish.** 3-4 minutes is enough. If someone's VS Code isn't working, they can do it later — the sprints work in any text editor.

### Phase 3: Launch Work (1 min)

> **Say:** "Your deliverable: `architecture-[role].md`. Your component specification — what it does, what technologies, how it connects to others, where policy enforcement sits. AI-SEC additionally writes YAML policy files."

> "Same sprint model as yesterday. Three sprints, two checkpoints. The AI Tutor prompt is on the course page — scroll to Work Zone and copy it. Go."

**Paste the Launch broadcast message in Teams chat.**

---

## PRE-WRITTEN BROADCAST MESSAGES

### Launch (paste at 9:15):
```
🚀 ARCHITECTURE SPRINT — STARTING NOW

Sprint 1 (9:15–9:35): Design your component with AI Tutor
⚡ Checkpoint 1 at 9:35: Post your component + what you need from other roles
Sprint 2 (9:40–9:55): Cross-role interfaces + respond to dependency requests
⚡ Checkpoint 2 at 9:55: Post your interface contract with at least 1 other role
Sprint 3 (10:00–10:10): Refine + self-review
Submit by 10:15: architecture-[role].md

Remember: your Day 12 Checkpoint 2 dependencies are TODAY'S architecture inputs.

🔴 At the wrap-up (10:15), I will test a real student's architecture with the salary query from this morning's demo. Will YOUR PEP hold?
```

### Checkpoint 1 (paste at 9:35):
```
⚡ CHECKPOINT 1 — YOUR COMPONENT + YOUR NEEDS

Post in your role's Teams channel:
"My component: [1-sentence description of what it does]
I need from [ROLE]: [specific technical question]"

Example:
- FDE: "My component: RAG pipeline with PEP enforcement point before response.
  I need from AI-SEC: What YAML format do your policy rules use? I need to parse them."
- AI-PM: "My component: ADR + cost breakdown + timeline.
  I need from FDE: What GPU hardware costs for on-prem Llama? I can't budget without it."
- AI-SEC: "My component: PDP/PEP with 5 policy rules + audit logging.
  I need from FDE: Where exactly in your pipeline is the PEP enforcement point?"

⚠️ If another role's post mentions YOUR role, respond with a 1-liner in THEIR channel.
This is the cross-role moment. Don't ignore it.
```

### Checkpoint 2 (paste at 9:55):
```
⚡ CHECKPOINT 2 — INTERFACE CONTRACT

Post in your role's Teams channel:
"Interface: [MY ROLE] ↔ [OTHER ROLE]
Format: [X] | I send: [Y] | I receive: [Z] | Error handling: [W]"

Example:
- FDE ↔ AI-SEC: "Format: YAML policy files parsed at startup + runtime PEP calls
  via internal REST API. I send: {query, response_draft, confidence}.
  I receive: {decision: allow|block|redirect, reason, log_id}.
  Error: if PDP is down, BLOCK all responses and escalate to human."

You need at least 1 interface contract. Ambitious? Do 2.
```

### Buffer / Submit (paste at 10:10):
```
⏰ 5 MINUTES LEFT

Final check before submitting architecture-[role].md:
☐ PEP: Does your architecture have a Policy Enforcement Point?
☐ Audit log: Does your PEP log decisions?
☐ Interface contracts: At least 2 defined?
☐ Constraints: On-prem? €180K? 3 languages? All addressed?

Upload to shared folder by 10:15.

🔴 Reminder: I'm about to test one of your architectures live.
```

---

## WRAP-UP: YOUR ARCHITECTURE UNDER FIRE (10:15–10:25)

> **Goal:** The second wow moment. Same salary query from the opening demo — but tested against a REAL student's architecture. The shift from observer to participant.

### Preparation (during Sprint 3)

Scan FDE and AI-SEC Checkpoint 2 posts. Pick:
- **One FDE** with a clearly defined PEP in their pipeline
- **One AI-SEC** who wrote YAML policy rules

Ideally, pick a pair where their interface contract is defined (they posted in each other's channels). If you can find a pair where there's a visible gap — even better. Both outcomes are teachable.

### How to run it (8 min)

**Share your screen. Open the FDE's `architecture-[FDE].md`.**

> **Say:** "Let's trace the salary query through [Student Name]'s architecture."

**Walk through their pipeline visually:**

```
Query: "What is the salary of John Smith?"
→ [Student's retriever] finds Confluence pages
→ [Student's LLM] generates response with salary data
→ WHERE IS THE PEP? ← This is the moment
```

**Scenario A — PEP exists and connects to AI-SEC:**

> **Say:** "Great. [Student Name] has a PEP here *(point to it)*. Now let's check — does [AI-SEC Student Name]'s YAML actually connect? What format does FDE expect? What does AI-SEC provide?"

If the contract matches → Show the green simulation from the opening. Acknowledge the student(s).

> **Say:** "This architecture would have stopped the salary leak. The PEP caught it. The YAML rule blocked it. The audit log recorded it. That's what compliant architecture looks like."

**Scenario B — PEP is missing or disconnected:**

Show the red simulation from the opening.

> **Say:** "This is not a failure — this is a discovery. You now know exactly what to fix tonight. Tomorrow is governance day. You need this PEP in place before we put the EU AI Act lens on your architecture."

**Tone: Supportive, not punitive.** The point is: "This is how real architecture reviews work. You find gaps. You fix them. You come back stronger."

### Common Gaps to Call Out (2 min)

Based on what you've seen in checkpoint posts:

- "Many FDEs designed the RAG pipeline but forgot where policy enforcement sits. No PEP = no governance. Fix it tonight."
- "Some AI-SEs designed CI/CD but didn't include a policy validation gate. What happens if someone deploys code that violates a policy rule?"
- "AI-PMs: if your ADR doesn't include GPU cost (€15-30K for on-prem LLM), your budget is wrong."
- "Some interface contracts say 'sends data.' WHAT data? JSON with which fields? Vague contracts = integration surprises."

### Day 14 Bridge (5 min, 10:25–10:30)

> **Say:** "Tomorrow — Governance Day. EU AI Act compliance. Fines up to €15 million."

> "The architecture you designed today is what gets governed tomorrow. You will open your `architecture-[role].md` and ask three questions:"
>
> 1. "Where in my architecture does a human override the AI?"
> 2. "Can I prove what the system did on March 15 at 14:32?"
> 3. "Did I test for bias across all three languages?"
>
> "If you can't answer any of those — those are your governance gaps. And that's exactly what Day 14 is about."

> "**Tonight:** (1) Refine your architecture. (2) Respond to unanswered interface requests. (3) Re-read your Checkpoint 2 interface contract — tomorrow it becomes the thing you govern. (4) Self-check: PEP present? Audit log? At least 2 interface contracts? If anything is missing, fix it now."

---

## POST-SESSION: COPILOT TRACKING

### In each role channel:
```
Summarize all messages posted in this channel today.
Create a table with columns:
- Name
- Checkpoint 1: Component description + what they need from which role
- Checkpoint 2: Interface contract details
- Cross-role responses: Did they respond to requests from other roles?
- Other posts (blockers, reactions, etc.)

List channel members who did not post anything today.
```

### Cross-role interface map (compile across all channels):
```
From ALL role channels, extract all Checkpoint 2 interface contract posts.
Create a table:
- Student name | Their role | Connected role | Data format | What they send | What they receive

Also extract unanswered Checkpoint 1 requests:
- Student name | Their role | Role they need | Question asked | Was it answered?
```

**The interface map becomes the integration test specification for Week 5.**

---

## MENTOR ACTIVITY — Day 13

### Before session:
- [ ] Review Day 12 Checkpoint 2 dependency posts from your role channel
- [ ] Understand checkpoint timing: Checkpoint 1 (9:35), Checkpoint 2 (9:55)
- [ ] Prepare to answer cross-role requests that mention YOUR role's domain

### During session:
- [ ] **During breach simulation (9:00–9:07):** Just watch. Let it land.
- [ ] **During VS Code hands-on (9:07–9:15):** Help students in DM who can't get VS Code working. "Can't open VS Code? No worries — create the folder structure later. Focus on the sprint."
- [ ] **At Checkpoint 1 (9:35):** React to 3-4 component + needs posts within 2 min
- [ ] **During Sprint 2 (9:40–9:55):** THIS IS YOUR BUSIEST MOMENT — facilitate cross-channel conversations. If FDE asks for AI-SEC input and gets no response, DM an AI-SEC student.
- [ ] **At Checkpoint 2 (9:55):** Read interface contracts — are they specific enough? "Your interface says 'sends data.' WHAT data? JSON with which fields?"
- [ ] **During Sprint 3 (10:00–10:15):** Help the lecturer identify a strong FDE+AI-SEC pair for the wrap-up live test. DM lecturer: "Check [Student Name FDE] + [Student Name AI-SEC] — their contracts connect well" (or "there's a visible gap").
- [ ] DM students who missed checkpoints

### After session:
- [ ] Review 5-8 architecture-[role].md submissions
- [ ] Focus: does the architecture have (1) PEP, (2) audit log, (3) defined interfaces?
- [ ] Check: do interface contracts match between connected roles? (FDE says "sends JSON" — does AI-SEC say "receives JSON"?)
- [ ] Flag mismatches to Lecturer: "FDE designed for Qdrant but AI-DA monitoring assumes ChromaDB logging format"
- [ ] Optional afternoon office hours (~14:00, 15 min)
- [ ] Send status to Lecturer

### What mentors should flag:
- Students with excellent interface contracts → architecture leads for hackathon teams
- Students whose interfaces conflict with their connected roles → need alignment help
- Common tech choice patterns: "All FDEs chose Llama 3 — is that the right call for German content?"

---

## OFFLINE ASSIGNMENTS (90 min total)

### Block 1: Refine Architecture + Respond to Interfaces (30 min)
- Check your role channel: did anyone post an interface request to YOU after the session?
- Respond to unanswered cross-role requests
- Refine sections 3-4 (interfaces, dependencies) based on Checkpoint 2 feedback
- Ensure self-check passes: PEP, audit log, 2+ interface contracts

### Block 2: FDE↔AI-SEC Integration Review (30 min)
- Review Board: find a partner from a complementary role
  - FDE ↔ AI-SEC: "Does my PEP align with your policy format?"
  - AI-SE ↔ FDE: "Does my CI/CD include your policy validation gate?"
  - AI-DA ↔ AI-DS: "Does my monitoring dashboard match your evaluation metrics?"
  - AI-FE ↔ FDE: "Does my streaming setup handle your PEP block/redirect responses?"
- Leave 2-3 lines of feedback

### Block 3: Cert Prep (30 min)

### Videos (optional):

| ID | Title | Cat | Length | For whom |
|----|-------|-----|--------|----------|
| A5 | Architecture Decisions Under Pressure — Why On-Prem ≠ Cloud | A | 12-15 min | FDE+SE |
| A10 | RPA + Agentic AI — Your Infra Experience Is a Superpower | A | 12-15 min | ALL |
| B18 | Human in the Loop — 3 Patterns You Must Know | B | 8-10 min | ALL |
| C6 | ServiceNow API Integration Basics (YouTube) | C | ext | FDE+SE |

---

## INSTRUCTOR PREP CHECKLIST

### Before Day 13:

**Breach Simulation (WOW 1):**
- [ ] Option A (ideal): Agent running in terminal. Have two configs — one WITH PEP, one WITHOUT. Run the salary query in both. Practice the switch (comment/uncomment the policy check, restart).
- [ ] Option B (backup): Two prepared screenshots or pre-recorded terminal sessions. Simulation A (red/leak) and Simulation B (green/block). Print or have open for quick switch.
- [ ] Practice the punchline: "12 lines of YAML. One enforcement point. Today you design that enforcement point. And at the wrap-up, I test one of yours."
- [ ] Time yourself: this MUST fit in 7 minutes. Resist the urge to explain — the visuals do the work.

**VS Code Hands-On:**
- [ ] VS Code open with `eurohealth-helpdesk/` project structure pre-created (you demo, they follow)
- [ ] `/policies/` folder with 3 YAML files (same ones from breach demo)
- [ ] Test that you can create folders live smoothly on screen share
- [ ] Backup: if VS Code screen-share fails, have the project structure as a screenshot

**Wrap-Up Live Test (WOW 2):**
- [ ] Plan to scan FDE + AI-SEC Checkpoint 2 posts during Sprint 3
- [ ] Have the red and green simulation visuals ready to switch
- [ ] Prepare for both outcomes (PEP works / PEP missing) — both are good teachable moments
- [ ] Tone rehearsal: this is supportive, not punitive. "Not a failure — a discovery."

**Sprint infrastructure:**
- [ ] 4 broadcast messages pre-written (launch, Checkpoint 1, Checkpoint 2, buffer) — saved and ready to paste
- [ ] Timer/alarm set for 9:35, 9:55, 10:10
- [ ] Role channels from Day 11-12 still active

**Content:**
- [ ] AI Tutor prompts tested with Day 12 dependency context
- [ ] Videos A5, A10, B18, C6 published and linked
- [ ] Shared folder accessible for submissions

### Screen shares needed:
1. Terminal / agent output — breach simulation A (red) and B (green) — (9:00–9:07)
2. VS Code project structure — live creation (9:07–9:15)
3. YAML policy file — `pii-protection.yaml` opened in VS Code (9:10)
4. AI Tutor starting prompt — paste in Teams (9:15)
5. 1 FDE `architecture-[role].md` + 1 AI-SEC policy file — side-by-side (10:15–10:25)
6. Red/green simulation visual — during wrap-up test (10:15–10:25)

### Timing notes:
- Breach simulation MUST stay within 7 min. Don't explain the code. The contrast between red and green does the teaching.
- VS Code hands-on: 8 min max. Don't wait for everyone to finish. "Can't get VS Code working? Do it later. The sprint works in any editor."
- **Checkpoint broadcasts at 9:35 and 9:55 are non-negotiable. Set alarms.**
- Sprint 2 (9:40-9:55) is the cross-role moment. Mentors should be most active here.
- Wrap-up live test: 8 min max on the test + 5 min Day 14 bridge. End on the forward-looking note, not the gap.

---

## KEY TEACHING MOMENTS

> **The central message of Day 13:**
> "Architecture without governance is a liability. Governance without architecture is a fantasy. Today you design both — and you show where they connect."

> **The three concepts students MUST understand before Sprint 1:**
> - **PEP** = the security guard between AI and user. Checks every response against policy rules before it leaves. (Explained during Simulation B.)
> - **YAML** = machine-readable config files for policies. Human-readable AND executable. Not a PDF on SharePoint. (Explained when opening the file in VS Code.)
> - **Project Skeleton** = empty folder structure that your architecture fills. `src/`, `policies/`, `tests/`, `data/`. (Explained when students create their own.)

> **The emotional arc:**
> Opening (9:00): "Look what happens without a PEP." → Stakes established.
> Work (9:15–10:15): "Now design your PEP." → Agency given.
> Wrap-up (10:15): "Did YOUR PEP hold?" → Personal accountability.

> **The cross-role message:**
> "Your Day 12 dependencies became Day 13 interface contracts. Your Day 13 contracts become Day 14 governance checkpoints. Every day builds on the last. This is how real consulting projects work."

---

*Document Version: 3.0*
*Updated: February 24, 2026*
*Changes from v2: Complete plenary rewrite — replaced VS Code demo with 2-phase "Sandwich" structure (WOW 1: breach simulation opening, WOW 2: student architecture tested live at wrap-up). Added VS Code hands-on exercise where students create project skeleton. Added explicit scripted explanations for PEP, YAML, and Project Skeleton concepts woven into demo flow. Updated timing (7 min breach sim + 8 min VS Code hands-on + 10 min wrap-up live test). Added mentor task: identify FDE+AI-SEC pair for wrap-up during Sprint 3. Updated broadcast messages with wrap-up teaser. Added breach simulation prep to checklist (Option A: live terminal, Option B: prepared screenshots).*
*For: AI Academy 2026 — Day 13 Instructor Materials*
