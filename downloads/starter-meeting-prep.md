---
name: meeting-prep
description: "Prepare for an upcoming meeting — gather context, draft agenda, surface relevant tasks, suggest questions. Triggers: /meeting-prep, prep for meeting, prepare for call."
version: 1.0
user_invocable: true
arguments:
  - name: meeting
    description: "Meeting name or topic to prepare for"
    required: false
---

# Meeting Prep Skill

Prepare for an upcoming meeting by gathering all relevant context, drafting an agenda, surfacing related tasks, and suggesting questions.

## Workflow

### Step 1: Identify the Meeting

If meeting name provided as argument, use it. Otherwise:

```bash
# Check calendar for upcoming meetings
"$HOME/.claude/scripts/gcal-smart.sh" today 2>/dev/null

# Or use Krisp MCP:
# mcp__krisp__list_upcoming_meetings
```

Pick the next upcoming meeting (or ask user which one).

### Step 2: Gather Context

#### 2.1 Previous meetings on same topic

```bash
# Search for notes from previous meetings with same participants/topic
find . -name "*.md" -path "*/meetings/*" 2>/dev/null | head -20

# Search meeting notes by keyword
# grep -rl "MEETING_TOPIC" ./meetings/ 2>/dev/null
```

If Krisp MCP is available:
```
mcp__krisp__search_meetings(query: "MEETING_TOPIC")
```

Extract from previous meetings:
- **Action items** that were assigned
- **Decisions** that were made
- **Open questions** that need follow-up

#### 2.2 Related tasks

If Linear/task tool configured:
```
mcp__linear__search_issues(query: "MEETING_TOPIC")
```

Or search local files:
```bash
find . -name "*.md" \( -path "*/tasks/*" -o -name "TODO.md" \) 2>/dev/null
```

#### 2.3 Related documents

```bash
# Recent files related to topic
find . -name "*.md" -mmin -10080 2>/dev/null | head -20
# Then grep for topic keywords in those files
```

### Step 3: Synthesize Prep

Generate a meeting prep document:

```markdown
## Meeting Prep: {meeting title}

**When:** {date, time, duration}
**With:** {participants}
**Type:** {1:1 / team sync / client call / strategy}

---

### Context
- {Previous meeting summary — 2-3 sentences}
- {Related project status}

### Open Action Items
- [ ] {Action from last meeting — owner}
- [ ] {Action from last meeting — owner}

### Agenda Suggestions
1. **{Topic}** — {why it matters, 1 line}
2. **{Topic}** — {why it matters, 1 line}
3. **{Topic}** — {why it matters, 1 line}

### Questions to Raise
- {Question based on gaps in context}
- {Question based on overdue items}
- {Question about blockers}

### Key Numbers
- {Relevant metric or deadline}
- {Task count or progress percentage}

### My Notes
> {Space for user to add notes before meeting}
```

### Step 4: Save

Save prep document to meetings folder:

```bash
# Default location
echo "meetings/{date}-prep-{meeting-slug}.md"
```

## Meeting Type Templates

### 1:1 Meeting
Focus on:
- Their updates first
- Blockers and support needed
- Career/growth topics
- Action items from last 1:1

### Team Sync
Focus on:
- Sprint/project status
- Blockers across team
- Decisions needed
- Cross-team dependencies

### Client Call
Focus on:
- Deliverable status
- Questions they might ask
- Next steps to propose
- Timeline updates

### Strategy Session
Focus on:
- Data to present
- Options with pros/cons
- Decision framework
- Success metrics

## After the Meeting

Prompt the user:

```
Meeting done? I can help with:
1. Write meeting notes from transcript
2. Extract and assign action items
3. Update related tasks
4. Draft follow-up message
```

## Principles

- **Context over agenda** — surface what they NEED to know, not generic topics
- **Action items carry forward** — never lose commitments from previous meetings
- **Numbers anchor discussions** — always include relevant metrics
- **Prep in 2 minutes** — if it takes longer, the skill is over-engineering
