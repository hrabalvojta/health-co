# AI Academy 2026 — Day 11 Instructor Preparation

## "Welcome Back — The World Moved While You Were Away"

**Date:** Monday, February 23, 2026
**Theme:** Discovery + Orientation — Return from Spring Break
**Day in sequence:** Day 11 (Week 4, Day 1)

---

## Day Overview

| Time | Slot | Duration | Style |
| --- | --- | --- | --- |
| 9:00–9:15 | Plenary Opening | 15 min | Lecturer live, 200 people, 1 Teams call |
| 9:15–9:35 | Sprint 1: Individual Discovery | 20 min | Student alone with AI Tutor, role channel open |
| **9:35–9:40** | **⚡ Checkpoint 1: Post #1 Question** | **5 min** | **Mandatory post in role channel** |
| 9:40–9:55 | Sprint 2: Continue + Peer Reactions | 15 min | Individual work + reading/reacting in channel |
| **9:55–10:00** | **⚡ Checkpoint 2: What Did You Steal?** | **5 min** | **Mandatory post in role channel** |
| 10:00–10:10 | Sprint 3: Refine + Self-Review | 10 min | Individual finalization |
| 10:10–10:15 | Buffer: Submit | 5 min | Upload discovery-pack-[role].md |
| 10:15–10:30 | Plenary Wrap-Up | 15 min | Lecturer live, 200 people, screen shares |

**OFFLINE (after session, at home):**

| Time | Activity | Duration |
| --- | --- | --- |
| Offline Block 1 | Watch E2E video V0 (mandatory if not yet watched) | 30 min |
| Offline Block 2 | Refine discovery questions based on wrap-up feedback | 30 min |
| Offline Block 3 | Cert prep (study guide + practice questions) | 30 min |

---

## Operating Model Reminder

```text
This is the FIRST day of the new operating model:

Lecturer sets direction        → 10% of time (plenary)
AI Tutor teaches            → 70% of time (individual work)
Peers validate              → 15% of time (channel checkpoints)
Mentor catches mistakes     → 5% of time (DM coaching, async)

Students work INDIVIDUALLY. They are NOT in group calls during work time.
Peer interaction happens via STRUCTURED CHECKPOINTS in role channels.
Cross-role collaboration is DEFERRED to Day 12-13 (after CIO meeting
reveals inter-role dependencies naturally).
```

---

## PLENARY OPENING (9:00–9:15)

### What to say (talking points, not script)

#### 1. Welcome Back + Energy Reset (3 min)

> **Say:** "Welcome back. I hope you practiced during break. If you didn't — that's OK, we start fresh today. But if you DID — you're ahead and you'll feel it immediately."
> "From today, everything changes. No more exercises. No more 'learn this concept.' From today, you produce REAL artifacts for a REAL client brief. What you create this week could be a template you use on your first client engagement."

#### 1b. Day 10 → Day 11 Bridge (1 min)

> **Say:** "Before we go further — remember Friday? HealthCare Co. Twelve hospitals. Flawed prototype. Drug dosage errors. You audited that system and found governance failures that could have harmed patients."
> "Today you meet a new client — EuroHealth Insurance. Different company, different problem. But notice the pattern: on-premises, EU AI Act, tight budget, European enterprise. This is the Kyndryl client profile. You will see it again and again."
> "But here's the deeper point. HealthCare Co. runs hospitals. EuroHealth insures the people IN those hospitals. In the real world, these clients share data flows, regulatory environments, and operational dependencies. A Kyndryl team that sees BOTH engagements can spot opportunities that neither client sees alone — connecting a clinical decision support system to an insurance claims workflow, or using helpdesk resolution patterns to inform clinical FAQ priorities. This cross-domain thinking — building an ecosystem of agentic solutions, not isolated chatbots — is what makes Kyndryl's approach different from a single-client consulting firm. Keep that in mind as you work this week."

#### 2. Three Things That Happened During Break (5 min)

> **Say:** "Three things happened during spring break that change how you'll work:"
> **Show on screen:**

```text
1. KYNDRYL POLICY AS CODE (Feb 11, 2026)
   Our agents now run inside policy guardrails.
   If it's not in the code, the agent can't do it.
   This is our differentiator.

2. EU AI ACT FEBRUARY GUIDANCE
   The Commission published high-risk AI use case clarification.
   August 2026 deadline is 6 months away.
   Our clients are nervous.

3. AGENT INTEROPERABILITY IS REAL
   MCP connects agents to tools.
   A2A connects agents to agents.
   150+ orgs in the ecosystem.
```

> **Say:** "In 3 weeks, you'll deliver a complete AI project. Today we start. Your assignment is on the screen."

#### 3. The Client — EuroHealth Insurance (3 min)

> **Say:** "This is your client for the next 3 weeks. Not a case study. Not an exercise. A simulation that mirrors what you'd face at a real Kyndryl engagement."

**Show on screen — EuroHealth Brief Summary:**

```text
CLIENT:       EuroHealth Insurance AG, Frankfurt
SIZE:         3,000 employees, 8 EU countries
PROBLEM:      15,000 IT helpdesk tickets/month
              40% repetitive L1, 30% L2, 20% L3, 10% misrouted
              CSAT: 3.2/5, Avg resolution: 4 hours
              Cost: €2.4M/year (12 FTE)
WANT:         AI helpdesk assistant
              Auto-resolve 50% of L1
              Smart routing for rest
              ServiceNow integration
              3 languages (EN/DE/CZ)
              Full audit trail
CONSTRAINTS:  €180K / 6 months
              On-premises only (GDPR + internal policy)
              EU AI Act compliant (August 2026 deadline)
              No employee PII in training data
              Phase 1: IT dept (300 users)
```

> **Say:** "Read this brief carefully during your work time. Every detail matters. The constraints are where the real challenges hide."

#### 4. Today's Deliverable + Sprint Structure (4 min)

> **Say:** "Today's deliverable is simple but important: 10 discovery questions from your role's perspective. These are the questions you would ask in the FIRST client meeting with Hans Muller, the CIO of EuroHealth."
> **Say:** "But you won't work in silence for 60 minutes. We're doing 3 sprints with 2 mandatory checkpoints."

**Show on screen — Sprint Schedule:**

```text
SPRINT 1 (9:15–9:35) — Individual Discovery
  Work alone with AI Tutor. Draft first 5 questions.
  ⚡ CHECKPOINT 1 at 9:35: Post your #1 question in role channel.

SPRINT 2 (9:40–9:55) — Continue + React
  Draft remaining questions. Read 3 peer questions. React to 1.
  ⚡ CHECKPOINT 2 at 9:55: "I stole this from [name]: [idea]"

SPRINT 3 (10:00–10:10) — Refine + Self-Review
  Finalize all 10 questions. Add KAF mapping + KPIs.

BUFFER (10:10–10:15) — Submit
  Upload discovery-pack-[role].md to shared folder.
```

**Show on screen — AI Tutor Starting Prompt:**

```text
I'm a [YOUR ROLE] in a Kyndryl AI consulting team. We just received
a client brief for EuroHealth Insurance — they want an AI helpdesk
assistant. I need to prepare 10 discovery questions that I would ask
in the first client meeting. My questions should focus on:

- FDE: technical infrastructure, LLM hosting options, API integrations
- AI-SE: deployment environment, CI/CD maturity, monitoring infrastructure
- AI-DS: data quality, knowledge base structure, evaluation criteria
- AI-DA: current metrics, reporting needs, dashboard requirements
- AI-PM: business priorities, budget allocation, stakeholder dynamics
- AI-FE: user devices, accessibility needs, UI expectations
- AI-SEC: security posture, compliance gaps, threat landscape

Help me write questions that show the client I understand their problem.
```

> **Say:** "Copy this prompt. Replace [YOUR ROLE] with your actual role. Open ChatGPT or Claude. Start now. You have 60 minutes. I'll signal checkpoints in the main chat."

**Also show on screen:**

```text
LINKS:
📹 E2E Video V0 — watch if you haven't (MANDATORY)
📄 EuroHealth Brief — full document (SharePoint)
📁 Shared folder for submissions
```

### Materials needed for opening

- [ ] Slide with 3 trends (Policy as Code, EU AI Act, MCP/A2A)
- [ ] EuroHealth brief summary on screen
- [ ] Sprint schedule on screen
- [ ] AI Tutor starting prompts tested for all 7 roles
- [ ] **3 pre-written broadcast messages** ready to paste (see below)
- [ ] Links to E2E video, full brief, shared folder posted in Teams channel
- [ ] Teams chat channels created for all 7 roles (`#role-fde`, etc.)
- [ ] Mentors briefed on checkpoint timing and their role during sprints

---

## PRE-WRITTEN BROADCAST MESSAGES

### Checkpoint 1 (paste at 9:35)

```text
⚡ CHECKPOINT 1 — POST YOUR #1 QUESTION NOW

Go to your role's Teams channel.
Post your BEST discovery question — the one you're most proud of.
Just the question + one sentence on why it matters.

You have 5 minutes. Everyone posts. No exceptions.
Then: read 3 questions from your peers before continuing.
```

### Checkpoint 2 (paste at 9:55)

```text
⚡ CHECKPOINT 2 — WHAT DID YOU STEAL?

In your role's Teams channel, post:
"I stole this from [name]: [the question or idea you got from a peer]"

This is NOT copying — this is learning from your team.
The best consultants build on each other's thinking.
Then: continue refining your full discovery packet.
```

### Sprint 3 / Buffer (paste at 10:10)

```text
⏰ 5 MINUTES LEFT

Save your file as discovery-pack-[role].md
Upload to shared folder: [link]

If you're not done — upload what you have. You'll refine tonight.
Done early? Read a peer's submission and leave 1 line of feedback in the channel.
```

---

## INDIVIDUAL WORK (9:15–10:15)

### What students do (by sprint)

**Sprint 1 (9:15–9:35):**

1. Read EuroHealth brief carefully (10 min)
2. Work with AI Tutor to develop first 5 discovery questions (10 min)
3. At 9:35 — post #1 question into role channel (Checkpoint 1)

**Sprint 2 (9:40–9:55):**
4. Read 3 peer questions in role channel, react to at least 1
5. Continue drafting remaining 5 questions with AI Tutor
6. Post any blockers: "🔴 I don't know how to ask about X..."
7. At 9:55 — post "I stole this from [name]" (Checkpoint 2)

**Sprint 3 (10:00–10:10):**
8. Refine all 10 questions based on peer input
9. Fill in KAF mapping table
10. Add assumptions/risks and 3 KPI proposals
11. Self-review against 5-point KAF checklist

**Buffer (10:10–10:15):**
12. Save as `discovery-pack-[role].md` and upload to shared folder
13. If done early: read a peer's submission, leave feedback in channel

### Deliverable specification

```text
File: discovery-pack-[role].md

Structure:
# Discovery Packet v1 — [Role Name]
## Student: [Name]
## Date: February 23, 2026
## Client: EuroHealth Insurance AG

---

## Part 1: Discovery Questions (10)

### Question 1: [Question text]
**Why this matters:** [1-2 sentences explaining why]
**Red flag (bad answer):** [What a bad answer tells us]
**KAF component:** [Core / Ingestion / Policy-as-Code /
  Run Safe / HITL / Interop]

### Question 2: ...
(repeat for all 10 questions)

> Minimum coverage: at least 2 questions on Policy-as-Code,
> at least 1 on MCP/A2A interoperability,
> at least 1 on Human-in-the-loop checkpoints.

---

## Part 2: KAF Mapping (mini)
| KAF Component      | Covered by Q# | Notes                  |
|---------------------|---------------|------------------------|
| Agentic Core        |               |                        |
| Agentic Ingestion   |               |                        |
| Policy-as-Code      |               |                        |
| Digital Trust       |               |                        |
| Human-in-the-Loop   |               |                        |
| Interop (MCP/A2A)   |               |                        |

---

## Part 3: Assumptions / Risks / Open Items (3-5)
1. [Assumption or risk]
2. ...

---

## Part 4: What We Will Measure (3 KPI proposals)
1. [e.g., L1 deflection rate: 50% target]
2. [e.g., Misroute reduction: 80% target]
3. [e.g., CSAT delta: 3.2 → 4.0+]

---

## Part 5: Agent Classification
- **Governance tier:** Personal / Team / Enterprise
- **Registry/reuse potential:** [How would we register
  and share this agent across Kyndryl?]

---

## Dependencies on Other Roles:
- I need [Role X] to ask about [topic] because...

## Questions I Deliberately Did NOT Ask (and why):
- [Question] — because that's [other role]'s territory
```

### What mentor should watch for during sprints

| Sprint | Situation | Intervention |
| --- | --- | --- |
| Sprint 1 | Student hasn't started after 10 min | DM: "Have you pasted the prompt into your AI Tutor? Start there." |
| Sprint 1 | Questions are too generic | DM: "A CIO hears that from every vendor. What specifically do YOU need to know for YOUR role?" |
| Checkpoint 1 | Student didn't post | Wait 2 min, then DM: "I don't see your question in the channel. Post your best one — even if it's rough." |
| **Checkpoint 1** | **Questions appear in channel** | **React fast to 3-4 questions** (👍, "strong," "CIO would push back on this"). This kickstarts conversation. |
| Sprint 2 | Student copies AI Tutor output verbatim | DM: "That's the AI's version. Which of these would YOU actually ask first, and why?" |
| Sprint 2 | Student posts a blocker | If no peer answers in 3 min, mentor answers in channel (not DM — others may have same question) |
| Checkpoint 2 | Student says "I didn't steal anything" | DM: "That's fine — but name one peer question that made you think differently about yours. What was it?" |
| Sprint 3 | Only 5 questions after 45 min | DM: "Ask your tutor: 'What am I missing? What would a senior [role] ask that a junior would forget?'" |
| Buffer | Student finished early | "Good. Read a peer's submission. Leave one line of feedback in the channel." |
| Sprint 3 | Student struggles with brief | DM: "Start with: 'What in this brief would keep me up at night from my role's perspective?'" |

### Mentor engagement during checkpoints (CRITICAL)

```text
Checkpoint 1 (9:35–9:40):
Mentor's PRIMARY job: React to 3-4 questions in the channel within
the first 2 minutes. Quick reactions: 👍 "good direction" / 🤔 "a CIO
would ask 'so what?'" / "this is specific — I like it."

WHY: Without the first mentor reactions, the channel stays silent.
Students wait for someone else to go first. Mentor breaks the ice.

Checkpoint 2 (9:55–10:00):
Mentor reads "stolen" posts. If a student is frequently "stolen from,"
that's a strong performer — note for wrap-up showcase suggestion.
```

---

## PLENARY WRAP-UP (10:15–10:30)

### Structure

#### 1. Student Showcase (10 min)

> **Say:** "I'm going to pick one student per role — 7 total, about 1 minute each. Share your BEST question. The one you're most proud of."

**Pick students based on checkpoint data:**

- Who got the most reactions at Checkpoint 1 (peer-validated quality)
- Who was "stolen from" most at Checkpoint 2 (influenced others)
- If data isn't clear, pick students who posted first (shows initiative)

**For each student, ask:**

- "What's your best question?"
- "Why would this matter to the CIO?"

**After each, comment briefly:**

- "This is a good question because..." (validates)
- "But watch out — a CIO would push back and say..." (challenges)
- "Notice how this connects to what [other role] would ask..." (cross-role)

**Spend no more than 90 seconds per student. Move fast.**

#### 2. Common Patterns + Gaps (3 min)

> **Say:** "From what I see in the channels today, here are patterns:"

Typical patterns to call out:

- "Many of you asked about technology choices but forgot to ask about PEOPLE. Who at EuroHealth will use this? Who will resist it?"
- "FDEs asked about infrastructure but didn't ask about data quality. Your pipeline is only as good as the Confluence pages."
- "AI-PMs asked about budget but not about stakeholder dynamics. Hans Muller may sign, but Katarina Novak can kill your project."
- "AI-SECs asked about compliance but not about the existing security posture. You can't add security to a system you don't understand."

**Then bridge to cross-role (Day 12-13):**

> **Say:** "I also noticed something great at Checkpoint 2 — many of you 'stole' ideas from peers. That's how consulting teams work. Nobody has the full picture alone. Starting tomorrow, when I play the CIO, you'll see the gaps between roles in real time. By Day 13, we'll create structured cross-role collaboration. Today was about mastering YOUR role. Tomorrow is about seeing how roles fit together."

#### 3. Tomorrow Preview (2 min)

> **Say:** "Tomorrow, we simulate the first client meeting. I'm going to play Hans Muller, the CIO. I'll answer your questions live for 10 minutes. Then you write your discovery report. Bring your best questions — and be ready to think on your feet when the client's answer isn't what you expected."

### Post in Teams channel after wrap-up

- Tomorrow's schedule (Day 12)
- Reminder: "Finalize your discovery questions tonight. Submit to shared folder."
- Link to E2E video for those who haven't watched
- Reminder: "Your checkpoint posts in the channel are your participation record for today."

---

## POST-SESSION: COPILOT TRACKING

### Immediately after session, in each role channel ask Copilot

```text
Summarize all messages posted in this channel today.
Create a table with columns:
- Name
- Checkpoint 1: Their #1 question
- Checkpoint 2: What they "stole" and from whom
- Other posts (blockers, feedback, etc.)

Also list any channel members who did not post anything today.
```

**Save the output.** This is your:

- Attendance record (who participated)
- Engagement quality record (what they posted)
- Peer influence map (who got "stolen from" = thought leaders)
- Gap identification (who didn't post = may need mentor follow-up)

No need for Forms, no manual tracking, no separate spreadsheet.

---

## OFFLINE ASSIGNMENTS (90 min total)

### Block 1: E2E Video (30 min) — MANDATORY if not yet watched

> **Video A1 (V0):** "From Client Call to Production: A Complete AI Project with KAF"
>
> - 25-30 min
> - Critical section 25:00-28:00: "Where is YOUR role in all of this"
> - Students should watch this BEFORE Day 12

### Block 2: Refine Discovery Questions (30 min)

> Based on wrap-up feedback and checkpoint discussions:
>
> - Add questions you heard from peers that inspired you (Checkpoint 2 "steals")
> - Remove questions that were too generic
> - Strengthen the "why this matters" explanations
> - Ensure dependencies on other roles are documented

### Block 3: Cert Prep (30 min)

> Study guide + practice questions for your role's target certification
> (See certification matrix in plan — AI-102, AZ-400, DP-100, PL-300, etc.)

---

## VIDEO ASSIGNMENTS FOR DAY 11

### Available for offline study (students choose based on role relevance)

| ID | Title | Cat | Length | For whom | Priority |
| --- | --- | --- | --- | --- | --- |
| A1 | V0: From Client Call to Production with KAF | A | 25-30 min | ALL (mandatory) | CRITICAL |
| A2 | Welcome Back — From Exercises to Client Project | A | 8-10 min | ALL | High |
| A9 | What to Demand from the Client | A | 15-18 min | ALL (PM+FDE) | High |
| A4 | Discovery That Actually Works | A | 12-15 min | ALL (PM) | High |
| B1 | Policy as Code — Technical Deep-Dive | B | 12-15 min | FDE+SEC | High |
| B2 | MCP + A2A: How Agents Talk | B | 12-15 min | FDE | Medium |
| B3 | EuroHealth Brief Walkthrough | B | 8-10 min | ALL | High |
| B6 | Peer Review Guide | B | 5-7 min | ALL | High |
| C7 | Andrew Ng: AI Agents Overview (YouTube) | C | ext | ALL | Optional |

> **Note:** Day 11 is the heaviest video day (~65 min total). Students should watch what's relevant for their role. Real per-person load is ~25-40 min.

**Recommended by role:**

- **FDE:** A1 + A9 + B1 + B2 (~65 min)
- **AI-SE:** A1 + A9 + B1 (~55 min)
- **AI-DS:** A1 + A9 + B3 (~50 min)
- **AI-DA:** A1 + A9 + B3 (~50 min)
- **AI-PM:** A1 + A4 + A9 + B3 (~65 min)
- **AI-FE:** A1 + A9 + B3 (~50 min)
- **AI-SEC:** A1 + A9 + B1 (~55 min)
- **ALL:** B6 (Peer Review Guide, 5-7 min) — watch before using peer feedback

---

## MENTOR ACTIVITY — Day 11

### Before session

- [ ] Watch video A3 (Mentor Briefing — Your Role Is Safety Net) if not yet
- [ ] Join your role's Teams chat channel (`#role-fde`, `#role-aipm`, etc.)
- [ ] Review EuroHealth brief thoroughly
- [ ] **Understand checkpoint timing:** 9:35 (Checkpoint 1) and 9:55 (Checkpoint 2) — you must be active in your channel at these exact times

### During session

- [ ] Watch plenary opening (or read summary posted in mentor channel)
- [ ] Monitor your role's chat channel
- [ ] **At Checkpoint 1 (9:35):** React to 3-4 student questions within 2 minutes — this breaks the ice
- [ ] **During Sprint 2 (9:40-9:55):** Answer blockers, send DM coaching
- [ ] **At Checkpoint 2 (9:55):** Read "stolen" posts, note strong performers
- [ ] Send DM coaching throughout: *"I see you struggling with X. Try this..."* or *"You're strong in Y. Help your colleague with Z."*

### After session

- [ ] Review 5-8 student `discovery-pack-[role].md` submissions (async)
- [ ] Leave DM feedback: "At a client, this question would..." / "You're missing..."
- [ ] Flag common gaps to Lecturer: "My [role]s are mostly asking about X but missing Y"
- [ ] Optional afternoon office hours (~14:00, 15 min, voluntary)
- [ ] Send 1 status message to Lecturer: participation rate, quality patterns, suggestions

### Mentor time: ~2 hours total

---

## INSTRUCTOR PREP CHECKLIST

### Before Day 11 (CRITICAL — first day back)

**Content & Video:**

- [ ] E2E video V0 (A1) recorded, edited, and published
- [ ] Welcome Back video (A2) published
- [ ] Mentor Briefing video (A3) sent to 7 mentors
- [ ] "What to Demand from the Client" video (A9) published
- [ ] "Discovery That Actually Works" video (A4) published
- [ ] Policy as Code deep-dive (B1) published
- [ ] MCP + A2A video (B2) published
- [ ] EuroHealth Brief Walkthrough (B3) published
- [ ] Peer Review Guide (B6) published

**Infrastructure:**

- [ ] EuroHealth brief document finalized and in SharePoint
- [ ] AI Tutor starting prompts tested for all 7 roles
- [ ] Teams chat channels created for all 7 roles (`#role-fde`, etc.)
- [ ] Shared folder structure ready for student submissions
- [ ] Certification study materials linked per role

**Sprint-specific:**

- [ ] **3 broadcast messages pre-written** and saved (Checkpoint 1, Checkpoint 2, Buffer)
- [ ] Timer set or alarm at 9:35 and 9:55 for checkpoint broadcast
- [ ] Mentors briefed on checkpoint timing and their reaction role

**Removed from v1 (no longer needed):**

- ~~Review Board spreadsheet~~ → replaced by channel checkpoints + Copilot tracking

### Screen shares needed

1. Three trends slide (Policy as Code, EU AI Act, MCP/A2A)
2. EuroHealth brief summary
3. Sprint schedule with checkpoint times
4. AI Tutor starting prompt (must be copy-pasteable)
5. Links (E2E video, brief, shared folder)

### Timing notes

- Opening MUST end by 9:15 — don't over-explain. Students need the full 60 min.
- **Checkpoint broadcasts at 9:35 and 9:55 are non-negotiable.** Set alarms.
- If wrap-up runs over, never cut into individual work time
- If students seem lost at 9:25, post a clarifying message in main chat: "Focus on YOUR role's questions. You don't need to cover everything."

---

## junior tier / senior tier NOTES

> Tier sorting happens informally after Day 11. Mentors assess based on discovery question quality AND checkpoint participation.

**junior tier indicators (comfortable pace):**

- Finished 5+ questions before Checkpoint 1
- Posted a strong, specific question at Checkpoint 1
- Got "stolen from" at Checkpoint 2 (influenced peers)
- Questions reference specific data from the brief (e.g., "2,000 Confluence pages — 30% outdated")
- Already giving feedback to peers during Sprint 3

**senior tier indicators (needs more time):**

- Struggled to start without additional prompting
- Missed one or both checkpoints
- Questions are generic, not brief-specific
- Didn't engage with peer posts in the channel
- May need the "Start here" prompt variation

**senior tier support prompt (share with mentors to use if needed):**

```text
I'm new to consulting and need help getting started. I'm a [ROLE].
I just received a client brief for EuroHealth Insurance — they want
an AI helpdesk assistant. I don't know where to start.

Can you help me understand:
1. What does my role do on a project like this?
2. What would be the 3 most important things I need to find out?
3. Can you give me example discovery questions and explain why
   each one matters?

Start simple. I'll build up from there.
```

---

*Document Version: 2.0*
*Updated: February 20, 2026*
*Changes from v1: Added structured sprint checkpoints, Copilot-assisted tracking, deferred cross-role collaboration to Day 12-13, removed Review Board spreadsheet, added pre-written broadcast messages, updated mentor engagement protocol for checkpoints.*
*For: AI Academy 2026 — Day 11 Instructor Materials*
