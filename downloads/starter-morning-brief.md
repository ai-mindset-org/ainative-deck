---
name: morning-brief
description: "Morning brief pipeline — gathers calendar + tasks + recent sessions, synthesizes ONE focus sentence. Three output modes: brief, full, telegram."
version: 1.0
user_invocable: true
arguments:
  - name: style
    description: "Output: brief (default), full, telegram"
    required: false
---

# Morning Brief — Daily Pipeline

Generate a morning brief by auto-detecting your integrations, gathering context from every available source, and synthesizing ONE focused sentence for the day. Works with zero setup — adapts to whatever you have connected.

This is the **"aha moment"** of a Personal OS — the first time all your data sources produce a single actionable priority.

## Step 0: Detect Available Integrations

Read MCP config to know what's available BEFORE gathering data:

```bash
cat ~/.claude/mcp.json 2>/dev/null
```

Build integrations map from configured servers:

| Server | Capability | How to check |
|--------|-----------|--------------|
| krisp | Meetings, transcripts, action items | `ToolSearch: "+krisp"` |
| linear | Tasks, projects, sprints | `ToolSearch: "+linear list"` |
| notion | Notes, databases | `ToolSearch: "+notion search"` |

**Only ToolSearch servers found in mcp.json.** Don't guess — if not configured, don't try.

Also check for local tools:

```bash
# Google Calendar script (bash wrapper, if user has one)
ls ~/.claude/scripts/gcal*.sh 2>/dev/null

# TODO files in current project
find . -maxdepth 2 \( -name "TODO.md" -o -name "tasks.md" \) 2>/dev/null | head -3
```

## Step 1: Gather Context

Try each source in degradation order. **Skip silently** if unavailable — never error, never ask to install.

### 1.1 Calendar

**Degradation chain** (stop at first success):

1. **Krisp MCP** (if in mcp.json):
   - `mcp__krisp__list_upcoming_meetings`
   - Also provides action items from yesterday's meetings

2. **Google Calendar script** (if exists):
   ```bash
   "$HOME/.claude/scripts/gcal-smart.sh" today
   ```

3. **Skip** — note "no calendar" in output header.

### 1.2 Tasks

**Degradation chain:**

1. **Linear MCP** (if configured):
   - `mcp__linear__list_issues(assignee: "me", status: "started")`
   - `mcp__linear__list_issues(assignee: "me", status: "unstarted")`

2. **Local TODO files**:
   ```bash
   find . -maxdepth 2 \( -name "TODO.md" -o -name "tasks.md" \) 2>/dev/null | head -3
   ```

3. **Skip** — note "no task source".

### 1.3 Recent Sessions

```bash
# Find today's Claude sessions
touch -t $(date +%Y%m%d)0000 /tmp/brief-today-marker 2>/dev/null
find ~/.claude/projects -name "*.jsonl" -newer /tmp/brief-today-marker -maxdepth 3 2>/dev/null | head -5
```

For each session, read first 20 and last 20 lines to extract:
- Project name (from path)
- Topic (from first user message)

### 1.4 Vault State (optional)

If working directory contains markdown files:

```bash
find . -name "*.md" -mmin -720 \
  -not -path "./.obsidian/*" \
  -not -path "./.trash/*" \
  -not -path "./node_modules/*" \
  2>/dev/null | head -10
```

## Step 2: Synthesize

### Weekday-aware mode

| Day | Mode | Extra |
|-----|------|-------|
| Monday | Week overview | Show full week calendar, sprint status |
| Tuesday-Thursday | Standard | Focus on today's blocks |
| Friday | Wins + lessons | Show completed tasks this week |

### FOCUS derivation

The single most important output. Derive ONE sentence from ALL context:

1. Check today's calendar — what's the biggest time commitment?
2. Check in-progress tasks — what's most urgent or overdue?
3. Check yesterday's sessions — what was the user mid-work on?
4. Combine: **"[Action verb] [specific thing] [by when / why]"**

Examples:
- "Finalize proposal before 14:00 client call"
- "Close 3 overdue tasks — sprint ends Friday"
- "No meetings today — deep work on feature X"

**NEVER** generic focus like "have a productive day" — must be specific.

### Output structure

```
┌─────────────────────────────────────────────────┐
│  MORNING BRIEF · {weekday} {date}               │
│  sources: {list of what connected}              │
└─────────────────────────────────────────────────┘

  FOCUS
  > {main priority — 1 sentence from all context}

  CALENDAR ({count} events)
  ├─ {time}  {title}  ({duration})
  ├─ {time}  {title}  ({duration})
  └─ {time}  {title}  ({duration})

  TASKS ({in_progress} IP · {todo} todo)
  ├─ {id}  {title}                           ◐ IP
  ├─ {id}  {title}                           ◐ IP
  └─ +{N} in backlog

  YESTERDAY
  > {1-2 sentences: what you worked on, based on sessions}

  OBSERVATIONS
  · {schedule insight — conflicts, free blocks}
  · {task insight — overdue items, deadlines}
  · {pattern — "3 sessions on X, close it today?"}
```

## Step 3: Output Modes

### brief (default)
Terminal output as above.

### full
Same + additional sections:

```
  RECENT FILES ({count})
  ├─ {filename}  {modified time ago}
  └─ {filename}  {modified time ago}

  INTEGRATIONS
  ├─ calendar     {krisp|gcal|none}
  ├─ tasks        {linear|local|none}
  ├─ meetings     {krisp|none}
  └─ sessions     {N found}
```

### telegram
Compact version for messaging:

```
#morning {weekday}

focus: {priority}

{time} {event}
{time} {event}

tasks: {count} IP · {count} todo
· {most important}
· {second}

> {one observation}
```

## Principles

- **Graceful degradation**: 0 integrations = minimal brief; full stack = rich brief
- **Never error on missing source**: skip silently, note what connected in header
- **Opinionated focus**: ALWAYS synthesize ONE focus — this is the core value
- **Fast**: direct tool calls only, no background agents, <30 seconds
- **Weekday-aware**: Monday overview, Friday retrospective, standard midweek

## Customization

To adapt this skill to your setup:

1. **Add your calendar script path** in Step 1.1
2. **Add your task management tool** in Step 1.2 (GitHub Issues, Todoist, etc.)
3. **Adjust weekday modes** in Step 2 to match your work rhythm
4. **Change output format** to match your terminal preferences

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Generic focus: "be productive" | Focus MUST be specific: action + object + deadline |
| Failing when no calendar | Skip silently — brief with just tasks is valuable |
| Hardcoded tool names | ToolSearch first — tool names vary across setups |
| Reading entire session files | First 20 + last 20 lines is enough for topic |
