# AI Academy 2026 — Day 12 Instructor Preparation
# "First Client Meeting — What Would You Actually Ask?"

**Date:** Tuesday, February 24, 2026
**Theme:** Discovery Report — From Questions to Structured Analysis
**Day in sequence:** Day 12 (Week 4, Day 2)

---

## Day Overview

| Time | Slot | Duration | Style |
|------|------|----------|-------|
| 9:00–9:03 | Bridge from Day 11 | 3 min | Lecturer live, 200 people |
| 9:03–9:13 | Live Roleplay — Lecturer as Hans Muller | 10 min | Lecturer in character, students ask in chat |
| 9:13–9:15 | ⚡ Post-roleplay channel post | 2 min | Mandatory post in role channel |
| 9:15–9:35 | Sprint 1: Draft with AI Tutor | 20 min | Individual work |
| **9:35–9:40** | **⚡ Checkpoint 1: #1 Finding** | **5 min** | **Mandatory post in role channel** |
| 9:40–9:55 | Sprint 2: Continue + Read Peers | 15 min | Individual + channel |
| **9:55–10:00** | **⚡ Checkpoint 2: Cross-Role Dependency** | **5 min** | **Mandatory post in role channel** |
| 10:00–10:10 | Sprint 3: Refine + Self-Review | 10 min | Individual finalization |
| 10:10–10:15 | Buffer: Submit | 5 min | Upload discovery-report-[role].md |
| 10:15–10:30 | Plenary Wrap-Up | 15 min | Lecturer live, student examples, reference standard |

**OFFLINE (after session, at home):**

| Time | Activity | Duration |
|------|----------|----------|
| Offline Block 1 | Finalize discovery report + incorporate wrap-up feedback | 30 min |
| Offline Block 2 | Cross-role review: read 1 report from different role, leave feedback | 30 min |
| Offline Block 3 | Cert prep | 30 min |

---

## Operating Model Reminder

```
Same model as Day 11 — students know this now:

Lecturer sets direction        → 10% of time (plenary + roleplay)
AI Tutor teaches            → 70% of time (individual sprint work)
Peers validate              → 15% of time (channel checkpoints)
Mentor catches mistakes     → 5% of time (DM coaching, async)

NEW on Day 12: Checkpoint 2 introduces CROSS-ROLE awareness.
Students declare dependencies on other roles publicly in their channel.
This is the bridge to Day 13 Architecture (cross-role collaboration).
```

---

## PLENARY OPENING (9:00–9:15)

### 1. Bridge from Day 10 + Day 11 (3 min)

> **Say:** "Good morning. Quick bridge from yesterday."

> "On Day 10 — Friday before break — you watched what happens when a team SKIPS proper discovery. HealthCare Co. The vibe-coded prototype. Drug dosage errors. Governance failures everywhere. That was the 'what NOT to do' example."

> "Yesterday — Day 11 — you prepared YOUR discovery questions for EuroHealth Insurance. You used the sprint model, posted your best questions at Checkpoint 1, and at Checkpoint 2 you 'stole' ideas from peers. Your role channels had real energy."

> "Today is the payoff. You wrote questions. Now the CIO ANSWERS them. But here's the catch — Hans Muller doesn't speak your language. He speaks business. He doesn't care about your LLM architecture. He cares about bringing order to the AI chaos in his organization, about compliance deadlines, about cost reduction, and about keeping his job."

> "Remember from yesterday's brief: EuroHealth ALREADY has AI tools. Moveworks, shadow chatbots, unapproved prototypes. Hans doesn't need another tool — he needs someone to industrialize what he has. Your discovery report is the TRANSLATION LAYER that turns his business chaos into YOUR role's technical workplan. This is the skill that separates a technician from a consultant."

> "Ready? Let's meet the CIO."

### 2. Live Roleplay — Lecturer as Hans Muller (10 min)

> **Setup (30 sec):** "I'm now Hans Muller, CIO of EuroHealth Insurance. I'm 55, under board pressure to show AI results, skeptical but open. You have 10 minutes. Post your questions in the main Teams chat. I'll answer in character."

**Roleplay guidelines for Lecturer:**

| If they ask... | Hans Muller answers... | What this reveals |
|----------------|----------------------|-------------------|
| "What AI tools are you using today?" | "That's the problem. ServiceNow has Moveworks doing basic tickets. HR built their own chatbot. Claims has some LangChain thing nobody approved. Everyone's doing their own thing and nobody governs it." | Client already HAS AI tools — the problem is fragmentation and governance, not greenfield |
| "Can we use cloud?" | "Absolutely not. Our compliance team would have my head. Everything stays in our data center." | Constraint is firm — don't try to challenge it |
| "How outdated is the knowledge base?" | "Honestly? Katarina says about a third of it is garbage. But we don't have time to clean it up before this project." | Data quality is a known problem — factor it into the plan |
| "What does success look like?" | "Cut the remaining helpdesk costs by 30% in 6 months. Bring all these AI experiments under one roof. And if I can show the board a compliance-ready platform before August, I keep my job." | Three metrics: cost reduction, platform unification, compliance readiness. But the real driver is Hans's job security |
| "What about the helpdesk team?" | "Jan is nervous. His team thinks they're being replaced. I told them that's not the plan, but I'm not sure they believe me." | Change management is critical — ignore this and the project fails |
| "What's your ServiceNow setup?" | "Version... I'd have to ask Katarina. We use it for everything — tickets, CMDB, change management. The API is there but I don't think anyone uses it externally." | Integration exists but untested — add risk to plan |
| "EU AI Act compliance?" | "Stefan keeps sending me emails about it. I know we need to be compliant by August. That's partly why I'm doing this now — better to get ahead of it." | Compliance is a driver, not just a constraint |

**Stay in character.** Be slightly impatient (real CIOs are). Don't volunteer information — make them ask the right questions. If a question is too technical, say "I'd need to bring Katarina or Stefan into that conversation."

**If chat is slow (backup):**
- "Let me ask what a smart FDE would want to know..." → ask and answer in character
- "Anybody curious about the shadow AI problem? HR chatbot, Claims prototype — how does that affect YOUR role?" → ask and answer
- "What about budget? Any AI-PM want to know how I'm allocating €180K across unifying three different AI tools?" → ask and answer
- This models the behavior and triggers engagement

### 3. ⚡ Post-Roleplay Channel Post (2 min)

**Immediately after breaking character, paste into main Teams chat:**

```
⚡ POST-ROLEPLAY — GO TO YOUR ROLE CHANNEL NOW

Post: "Hans said [X]. For my role, this means [Y]."

Example:
- FDE: "Hans said 'no cloud.' For FDE this means on-prem LLM only → GPU sizing is my #1 task."
- AI-PM: "Hans said 'I keep my job.' For PM this means Hans needs board-ready monthly updates."
- AI-SEC: "Hans said 'Stefan keeps emailing about AI Act.' For SEC this means compliance is a selling point, not just a constraint."

Read 3 posts from peers. React to 1. You have 2 minutes.
Then: open AI Tutor and start your discovery report.
```

**Why this matters:** Creates a "wall of interpretations" in each role channel. Students see how the SAME CIO answer means different things to different people in the same role. This is intra-role comparison — pedagogically correct before the cross-role checkpoint comes later.

**Post key roleplay points in Teams chat immediately after (for students to reference):**

```
📋 KEY POINTS FROM HANS MULLER MEETING:
- EuroHealth already has AI tools (Moveworks, HR chatbot, Claims prototype) — problem is fragmentation & no governance
- Success = cut remaining helpdesk costs by 30%, unify AI platform, EU AI Act compliance by August
- On-premises only, no cloud (compliance, non-negotiable)
- Knowledge base is ~30% outdated ("garbage"), Katarina says no one has time to clean it
- Helpdesk team (Jan + 12 agents) fears replacement — morale is low
- EU AI Act deadline August 2026 — Stefan (CISO) is pushing for it
- Budget: €180K / 6 months — very tight
- ServiceNow: uses it for everything but API is untested externally
- Hans doesn't speak tech — translate everything to business value
- This is an INDUSTRIALIZATION engagement, not a chatbot build
```

---

## PRE-WRITTEN BROADCAST MESSAGES

### Post-Roleplay (paste immediately after roleplay at ~9:13):
```
⚡ POST-ROLEPLAY — GO TO YOUR ROLE CHANNEL NOW

Post: "Hans said [X]. For my role, this means [Y]."
Read 3 posts from peers. React to 1. You have 2 minutes.
Then: open AI Tutor and start your discovery report.
```

### Checkpoint 1 (paste at 9:35):
```
⚡ CHECKPOINT 1 — YOUR #1 FINDING

Post in your role's Teams channel:
"My #1 finding from Hans: [something NOT in the brief that changes my approach]"

Hans said things in the roleplay that were NOT in the written brief.
What did you catch? What changes your plan?

You have 5 minutes. Everyone posts. Then read 3 peer findings.
```

### Checkpoint 2 (paste at 9:55):
```
⚡ CHECKPOINT 2 — CROSS-ROLE DEPENDENCY

Post in your role's Teams channel:
"I need [ROLE] to tell me about [TOPIC] because my report depends on it."

Examples:
- "I need AI-SEC to clarify EU AI Act classification — it affects my architecture choices" (FDE)
- "I need FDE to confirm on-prem GPU cost — it affects my budget allocation" (AI-PM)
- "I need AI-DS to assess knowledge base quality — it affects my risk section" (AI-SEC)

This is NOT a weakness. This is how real consulting teams work.
Save these dependencies — you'll need them tomorrow (Architecture Day).
```

### Buffer (paste at 10:10):
```
⏰ 5 MINUTES LEFT

Save as discovery-report-[role].md
Upload to shared folder: [link]

Not done? Upload what you have. Finish tonight (30 min homework).
Done early? Read a peer's Checkpoint 2 dependency post — if it mentions YOUR role,
respond with a 1-line answer in their channel.
```

---

## AI TUTOR STARTING PROMPT

**Post in Teams chat after roleplay key points:**

```
I just finished a 10-minute roleplay session with the CIO of EuroHealth
Insurance AG (Hans Muller). I'm a [YOUR ROLE] on a Kyndryl AI consulting
team. Based on the client brief AND the roleplay insights, I need to
write a discovery report from my role's perspective.

First, here are my Day 11 discovery questions (paste your top 3-5):
[PASTE YOUR BEST QUESTIONS FROM discovery-pack-[role].md]

Now, here is what I learned from Hans in the roleplay:
- EuroHealth already has Moveworks/ServiceNow AI handling basic tickets
- Shadow AI problem: HR chatbot, Claims LangChain prototype, no governance
- Success = cut remaining helpdesk costs by 30%, unify AI under one platform,
  be EU AI Act compliant by August 2026
- On-premises only, no cloud (compliance, non-negotiable)
- Knowledge base is ~30% outdated, no one owns it
- Helpdesk team (Jan + 12 agents) fears replacement
- Budget: EUR 180K / 6 months — very tight

Compare my Day 11 questions against what Hans actually answered.
Which were answered? Which remain open? What new issues emerged?

Then help me write a structured discovery report that includes:
1. Stakeholder analysis (from my role's perspective)
2. Key findings and implications for my workstream
3. Technical/functional requirements I need to investigate
4. Risks specific to my area
5. Recommended next steps (first 2 weeks)
6. Dependencies on other roles in the team

Challenge me if my analysis is shallow. Push me to think about
second-order effects and hidden risks.
```

---

## INDIVIDUAL WORK — SPRINT STRUCTURE (9:15–10:15)

### Sprint 1: Draft with AI Tutor (9:15–9:35, 20 min)

**Students:**
1. Review roleplay key points posted in Teams chat (5 min)
2. Open AI Tutor, paste starting prompt (2 min)
3. Draft sections 1-3 of discovery report: Stakeholder analysis, Key findings, Requirements (13 min)

**Mentors:**
- Read role channels — post-roleplay interpretations are coming in
- If student hasn't started by 9:25, DM: "Have you pasted the prompt? Start with: what did Hans say that changes YOUR plan?"
- Don't over-coach — let them struggle with translating business language into technical requirements

### ⚡ Checkpoint 1 (9:35) — "#1 Finding"

**Lecturer pastes broadcast message at 9:35.**

**What happens:** Each role channel fills with findings — things Hans said that were NOT in the brief. This reveals who was actively listening vs. who is just repeating the brief.

**Mentors at Checkpoint 1:**
- React to 3-4 posts within 2 minutes (👍, "great catch," "dig deeper on this")
- If posts are just restating the brief, DM: "That was already in the brief. What did Hans say that was NEW? His body language, his emotion about Jan, his avoidance of tech questions..."
- Note strong performers for wrap-up showcase

### Sprint 2: Continue + Read Peers (9:40–9:55, 15 min)

**Students:**
4. Read 3 peer findings from Checkpoint 1 in role channel
5. Continue drafting sections 4-6: Risks, Next steps, Dependencies
6. Post any blockers: "🔴 I can't figure out how to classify the EU AI Act risk for this use case..."
7. Peers answer blockers, mentor DMs coaching

**Mentors:**
- Watch for common blockers — if 3+ students ask the same question, answer in channel (not DM)
- DM coaching: "Hans said 'I keep my job.' How does that change your risk register? Add a risk about stakeholder alignment, not just technical risks."

### ⚡ Checkpoint 2 (9:55) — "Cross-Role Dependency"

**Lecturer pastes broadcast message at 9:55.**

**What happens:** Students publicly declare what they need from OTHER roles. This is the first cross-role mechanism in the program. It's not pairing (which fails at 200 people) — it's a public marketplace of dependencies.

**Why this works:**
- Low barrier: one sentence, posted in YOUR channel
- Creates a paper trail for Day 13 (Architecture) — mentors can compile dependencies into a cross-role dependency map
- Students who write "I need AI-SEC for EU AI Act classification" demonstrate systems thinking
- Students who write "I don't need anyone" demonstrate blind spots

**Mentors at Checkpoint 2:**
- If student says "I don't have dependencies," DM: "Really? Your FDE assessment assumes a budget for GPU hardware. Who decides the budget? That's a dependency on AI-PM."
- If a dependency mentions YOUR role, respond briefly in their channel: "Good question — I'll ask my students to address this."
- Note cross-role patterns for Lecturer's wrap-up

### Sprint 3: Refine + Self-Review (10:00–10:10, 10 min)

**Students:**
8. Refine all 6 sections based on peer input
9. Self-review: "Could this sentence appear in any discovery report for any client? If yes, rewrite."
10. Ensure section 6 (Dependencies) reflects Checkpoint 2 declarations

### Buffer: Submit (10:10–10:15, 5 min)

**Lecturer pastes buffer message at 10:10.**

**Extra credit for early finishers:** "Read a peer's Checkpoint 2 dependency post. If it mentions YOUR role, respond with a 1-line answer." This creates organic cross-role dialogue.

---

## PLENARY WRAP-UP (10:15–10:30)

### Structure:

#### 1. Day 10-11-12 Arc (2 min)

> **Say:** "Let me connect the dots. Three days, one story."

> "Day 10: HealthCare Co. — you saw what happens when a team SKIPS discovery. Prototype first, questions later. Drug dosage errors. Governance failures. The lesson: discovery is not optional."

> "Day 11: EuroHealth Insurance — you wrote discovery QUESTIONS from your role. At Checkpoint 2, you 'stole' ideas from peers. You learned that even within one role, people notice different things."

> "Day 12: TODAY — the CIO answered those questions. But his answers weren't in the language you expected. 'Cut costs by 30%' is not a technical requirement. 'I keep my job' is not a KPI. And 'everyone's doing their own thing' is not an architecture. Your discovery report is the TRANSLATION LAYER between the client's world and your technical workplan. And you discovered this is an industrialization engagement, not a chatbot build."

> **KEY EMPHASIS (repeat in wrap-up):** "If your discovery report only contains what Hans told you, you failed. If it contains what Hans DIDN'T tell you — but needs to hear — you just became his most trusted advisor. Look at the 5 Layers of the Unsaid in the course material. Every one of you should have found something in at least 3 of those layers."

> "And at today's Checkpoint 2, something new happened: you declared dependencies on OTHER roles. That's the bridge to tomorrow. Architecture requires cross-role alignment."

#### 2. Show 2 Strong Student Examples (8 min)

**Pick 2 students from DIFFERENT roles.** Share screen of their discovery report.

Selection priority:
- Students whose Checkpoint 1 findings showed genuine insight (not just restating the brief)
- Students whose Checkpoint 2 dependencies were specific and actionable
- If data isn't clear, pick from roles that contrast well (e.g., FDE + AI-PM, or AI-SEC + AI-DA)

> **Say for each:** "Look at this — [Student name], [Role]. Notice how they..."

**What makes a good example:**
- References specific data from the roleplay (not just the brief)
- Shows clear role-specific focus (doesn't try to cover everything)
- Identifies dependencies on other roles (section 6 is non-empty)
- Includes realistic risks with mitigations (not just "there are risks")
- Has measurable next steps ("audit 50 Confluence pages in Week 1" not "investigate data quality")

**After showing examples, show reference standard:**

> **Say:** "Here's what a senior consultant's discovery report looks like. Compare yours to this structure."

**Show on screen — finished example:**

```
DISCOVERY REPORT — Reference Standard

1. STAKEHOLDER MAP
   - Decision maker: Hans Muller (CIO) — budget authority, board pressure
   - Influencer: Katarina Novak (IT Ops) — daily operations, owns infra
   - Blocker potential: Stefan Weber (CISO) — security veto, EU AI Act champion
   - End users: Jan Kovar (Helpdesk Lead) + 12 agents — fear of replacement
   - Hidden stakeholder: The Board — wants AI ROI story, Hans reports to them
   - Shadow AI owners: HR team (chatbot), Claims team (LangChain prototype)

2. USE CASE LIST (Prioritized)
   P1: Unify fragmented AI under one governed platform (the real scope)
   P2: Auto-resolve remaining L1 tickets (40% of volume, highest ROI)
   P3: Smart routing for L2/L3 tickets (reduce misrouting from 10%)
   P4: Multi-language support (EN/DE/CZ — hard requirement)
   P5: ServiceNow integration (read + update tickets)

3. KEY FINDINGS FROM MEETING
   - This is an INDUSTRIALIZATION engagement, not a chatbot build
   - EuroHealth already has AI tools (Moveworks, HR bot, Claims prototype) — scattered, ungoverned
   - CIO success metric is cost reduction (30%) + platform unification + compliance readiness
   - Knowledge base quality is acknowledged risk — no owner, 30% outdated
   - On-prem constraint is non-negotiable (compliance-driven)
   - Change management is critical — team morale is fragile
   - EU AI Act readiness is a SELLING POINT, not just compliance cost

4. RISKS
   - Data quality: 30% outdated Confluence → garbage in, garbage out
   - Shadow AI: uncontrolled experiments may conflict with unified platform
   - Budget: €180K may not cover GPU hardware for on-prem LLM
   - Timeline: 6 months for unification + build + operate on untested infra
   - Adoption: Jan's team can quietly sabotage if not engaged early
   - Scope creep: 8 countries, 3 languages, could expand beyond Phase 1

5. NEXT STEPS
   - Week 1-2: Knowledge audit (sample 200 of 2,000 Confluence pages)
   - Week 1: Shadow AI inventory (what exists, who owns it, what data it touches)
   - Week 1: Stakeholder alignment meeting with Katarina and Stefan
   - Week 2: Architecture decision (LLM selection for on-prem)
   - Week 2: ServiceNow API feasibility test

6. DEPENDENCIES ON OTHER ROLES
   - Need AI-SEC: EU AI Act risk classification (high-risk or not?)
   - Need FDE: GPU hardware sizing and cost (affects budget)
   - Need AI-DS: Knowledge base audit methodology (sample size, criteria)
   - Need AI-DA: Current baseline metrics (can't prove improvement without them)
```

> **Say:** "Notice section 6 — Dependencies. This is exactly what your Checkpoint 2 posts captured. Tomorrow, when we do Architecture, these dependencies become your agenda."

#### 3. Checkpoint 2 Patterns (3 min)

> **Say:** "Let me share what I saw at Checkpoint 2. Patterns:"

Call out 2-3 real patterns from dependency posts:
- "Many FDEs need AI-SEC for EU AI Act classification. That tells me: architecture decisions DEPEND on compliance decisions. You can't separate them."
- "AI-PMs need FDE for cost estimates. That tells me: the scope document can't be finalized until the technical assessment is done. Waterfall thinking doesn't work here — you iterate together."
- "AI-DS needs AI-DA for metrics baseline. That tells me: the data team needs to align on WHAT to measure before building any evaluation framework."
- "Some of you wrote 'I don't need anyone.' Really? Show me a discovery report section 6 that's empty, and I'll show you a consultant who's about to be surprised on Day 13."

#### 4. Tomorrow Preview (2 min)

> **Say:** "Tomorrow — Day 13 — Architecture. This is where the cross-role alignment HAPPENS. You'll take your discovery reports and your Checkpoint 2 dependencies and sit down (virtually) with the roles you depend on."

> "I'll show a live demo — VS Code, YAML policy files, what happens when an agent hits a boundary. Then you design YOUR component's architecture. But the key: your architecture must be COMPATIBLE with the person next to you."

> "Tonight: finalize your report. Read one report from a DIFFERENT role on the shared folder — leave feedback. And bring your Checkpoint 2 dependencies list to tomorrow's session."

---

## POST-SESSION: COPILOT TRACKING

### In each role channel, ask Copilot:

```
Summarize all messages posted in this channel today.
Create a table with columns:
- Name
- Post-Roleplay interpretation: "Hans said X, for my role this means Y"
- Checkpoint 1: Their #1 finding from the roleplay
- Checkpoint 2: Their cross-role dependency declaration
- Other posts (blockers, reactions, etc.)

Also list channel members who did not post anything today.
```

### Additionally, compile cross-role dependency map:

```
From ALL role channels, extract all Checkpoint 2 posts.
Create a table with columns:
- Student name
- Their role
- Role they need
- What they need from that role

Group by "Role they need" to see which roles are most in-demand.
```

**This dependency map becomes the input for Day 13 Architecture cross-role groupings.**

---

## MENTOR ACTIVITY — Day 12

### Before session:
- [ ] Review Day 11 checkpoint posts in your role channel (see what questions students prepared)
- [ ] Read the roleplay Q&A table in this prep doc
- [ ] Understand checkpoint timing: post-roleplay (9:13), Checkpoint 1 (9:35), Checkpoint 2 (9:55)

### During session:
- [ ] Watch plenary + roleplay (or read summary in mentor channel)
- [ ] **Post-roleplay (9:13):** React to 2-3 student interpretation posts — break the ice
- [ ] **At Checkpoint 1 (9:35):** React to 3-4 findings within 2 minutes
- [ ] **During Sprint 2 (9:40-9:55):** Answer blockers, DM coaching focused on "translate business to technical"
- [ ] **At Checkpoint 2 (9:55):** Read dependency posts. If a dependency references YOUR channel's role, post a brief acknowledgment
- [ ] DM students who missed checkpoints

### After session:
- [ ] Review 5-8 discovery-report-[role].md submissions
- [ ] Focus feedback on: "At a real client, this would/wouldn't work because..."
- [ ] Specifically check: does section 6 (Dependencies) exist and is it specific?
- [ ] Flag common gaps to Lecturer: "My [role]s are strong on X but missing Y"
- [ ] Look for students who incorporated roleplay context vs. those who just restate the brief
- [ ] Optional afternoon office hours (~14:00, 15 min)
- [ ] Send status to Lecturer

### What mentors should flag:
- Students with excellent Checkpoint 2 dependencies → strong cross-role awareness for Day 13
- Students whose section 6 is empty → need support for cross-role collaboration
- Common mistakes across the role (e.g., "All my FDEs forgot about ServiceNow integration despite Hans mentioning it")

---

## OFFLINE ASSIGNMENTS (90 min total)

### Block 1: Finalize Discovery Report (30 min)
- Incorporate wrap-up feedback and reference standard comparison
- Ensure section 6 (Dependencies) is complete — you'll use it tomorrow
- Make it "client-presentable" (not a rough draft)

### Block 2: Cross-Role Review (30 min)
- Go to shared folder, find ONE report from a DIFFERENT role
- Read it and leave feedback focused on:
  - Does it reference the roleplay (not just the brief)?
  - Is there something that affects YOUR workstream?
  - One specific suggestion for improvement
- Recommended pairings:
  - FDE ↔ AI-SEC: "Is my feasibility realistic?" / "Is my threat model complete?"
  - AI-PM ↔ FDE: "Does my scope match technical reality?"
  - AI-DS ↔ AI-DA: "Do my quality criteria align with your monitoring plan?"
  - AI-FE ↔ AI-PM: "Does my user analysis match your stakeholder map?"

### Block 3: Cert Prep (30 min)
- Continue study guide + practice questions

### Video (optional):

| ID | Title | Cat | Length | For whom |
|----|-------|-----|--------|----------|
| B17 | Organizational Change Management — AI Is Not an IT Upgrade | B | 12-15 min | ALL (PM) |

> **Why B17 today:** Hans mentioned helpdesk team resistance. OCM is directly relevant to discovery findings.

---

## INSTRUCTOR PREP CHECKLIST

### Before Day 12:

**Roleplay:**
- [ ] Hans Muller character prepared (personality, typical answers from Q&A table)
- [ ] 3 backup questions ready in case chat is slow
- [ ] Key roleplay points pre-written (to paste in Teams chat immediately after)

**Sprint infrastructure:**
- [ ] 4 broadcast messages pre-written (post-roleplay, Checkpoint 1, Checkpoint 2, buffer) — saved and ready to paste
- [ ] Timer/alarm set for 9:13, 9:35, 9:55, 10:10
- [ ] Role channels from Day 11 still active and accessible

**Content:**
- [ ] Reference standard discovery report ready (show during wrap-up, NOT before)
- [ ] AI Tutor prompts tested for all 7 roles with roleplay context
- [ ] Shared folder accessible for submissions

**Removed from v1 (no longer needed):**
- ~~Show finished example during opening~~ → moved to wrap-up (prevents copy-paste mentality)
- ~~Exercise 2: Cross-Role Report Review during wrap-up~~ → moved to offline homework
- ~~Peer Activity: Post-Roleplay Debrief in pairs~~ → replaced by structured channel posts

### Screen shares needed:
1. Hans Muller character card (during roleplay)
2. AI Tutor starting prompt (after roleplay)
3. 2 strong student examples (during wrap-up)
4. Reference standard discovery report (during wrap-up, AFTER student examples)

### Timing notes:
- Roleplay must end by 9:13. If questions are flowing, say "Last question — we need to get to work."
- Post-roleplay channel post takes 2 min — don't skip it, it creates the "wall of interpretations"
- Post roleplay key points in Teams chat IMMEDIATELY after — students reference them all session
- **Checkpoint broadcasts at 9:35 and 9:55 are non-negotiable. Set alarms.**
- Do NOT show reference standard during opening — show it in wrap-up after students have produced their own work

---

## STORY ARC: DAY 10 → 11 → 12 → 13

```
Day 10 (Friday):   WHAT NOT TO DO
                    HealthCare Co. — audit a failed prototype
                    Lesson: skipping discovery = governance failures

Day 11 (Monday):   ASK THE RIGHT QUESTIONS
                    EuroHealth Insurance — write discovery questions
                    Lesson: your role determines what you notice

Day 12 (Tuesday):  LISTEN TO THE ANSWERS  ← YOU ARE HERE
                    EuroHealth Insurance — CIO answers, write report
                    Lesson: translate business language into technical plans
                    Bridge: Checkpoint 2 dependencies → Day 13 cross-role

Day 13 (Wednesday): BUILD IT TOGETHER
                    EuroHealth Insurance — architecture from discovery
                    Lesson: your architecture must be compatible with other roles
                    Cross-role collaboration starts here (natural need from Day 12)
```

---

*Document Version: 3.0*
*Updated: February 23, 2026*
*Changes from v2: Aligned Hans Muller roleplay answers with Day 11 EuroHealth brief (industrialization framing, not chatbot-from-scratch). Updated AI Tutor prompt to reference Day 11 discovery packet output. Updated reference standard to include shadow AI inventory and platform unification scope. Updated broadcast key points message. Updated bridge and wrap-up scripts.*
*For: AI Academy 2026 — Day 12 Instructor Materials*
