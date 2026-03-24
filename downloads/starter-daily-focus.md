---
name: daily-focus
description: "Generate a daily focus card — top priorities, energy level, key meetings, and a metaphor of the day. Output: markdown summary + optional HTML visual card."
version: 1.0
user_invocable: true
arguments:
  - name: format
    description: "Output format: text (default), card (HTML visual), both"
    required: false
---

# Daily Focus Skill

Generate a daily focus summary with your top priorities, energy level, schedule highlights, and a creative metaphor for the day's theme.

## Workflow

### Step 1: Gather Context

Collect data from available sources (skip silently if unavailable):

**Calendar** — today's events:
```bash
# If you have a calendar script:
"$HOME/.claude/scripts/gcal-smart.sh" today 2>/dev/null

# Or use Krisp MCP if configured:
# mcp__krisp__list_upcoming_meetings
```

**Tasks** — in-progress and upcoming:
```bash
# Linear MCP if configured:
# mcp__linear__list_issues(assignee: "me", status: "started")

# Or local TODO:
find . -maxdepth 2 -name "TODO.md" 2>/dev/null | head -3
```

**Recent work** — what you did yesterday:
```bash
# Recent Claude sessions
find ~/.claude/projects -name "*.jsonl" -mmin -1440 -maxdepth 3 2>/dev/null | head -5
```

### Step 2: Derive Focus

From all gathered context, determine:

1. **Top 3 priorities** — ranked by urgency and impact
2. **Energy level** — estimate 1-10 based on schedule density
3. **Day metaphor** — one word that captures the day's theme
4. **Bottom stats** — meetings count, task count, focus hours available

**Priority derivation rules:**

| Signal | Priority |
|--------|----------|
| Meeting in <2 hours needing prep | HIGH |
| Overdue task | HIGH |
| In-progress task with deadline today | HIGH |
| Scheduled deep work block | MEDIUM |
| Backlog task, no deadline | LOW |

**Metaphor examples:**

| Day pattern | Metaphor |
|-------------|----------|
| Back-to-back meetings | MARATHON |
| One big deliverable | LAUNCH |
| Many small tasks | MOSAIC |
| Empty calendar, deep work | FORTRESS |
| Strategy/planning day | COMPASS |
| Wrapping up projects | CONVERGENCE |
| Starting new initiative | IGNITION |

### Step 3: Output

#### Text format (default)

```markdown
## #FOCUS — {weekday} {date}

> {metaphor}: {one-sentence theme}

### Priorities
1. **{project}** — {task description}
2. **{project}** — {task description}
3. **{project}** — {task description}

### Schedule
- {time} — {event}
- {time} — {event}
- {time-time} — focus block

### Stats
{N} meetings · {N} tasks · {N}h focus time · energy {N}/10
```

#### Card format (HTML visual)

Generate a single-file HTML card (1200x500px, dark theme) with:

```html
<!DOCTYPE html>
<html>
<head>
<style>
  html, body {
    margin: 0; padding: 0;
    width: 1200px; height: 500px;
    font-family: 'IBM Plex Mono', monospace;
    background: #0c0c0c; color: #e5e5e5;
    overflow: hidden;
  }

  .container {
    display: grid;
    grid-template-columns: 1fr 300px;
    height: 100%; padding: 40px;
    box-sizing: border-box;
  }

  /* Left: priorities */
  .tag { font-size: 18px; font-weight: 700; letter-spacing: 3px; }
  .date { font-size: 11px; color: #555; margin-top: 4px; }
  .priority {
    margin-top: 16px; padding: 12px 18px;
    background: rgba(255,255,255,0.025);
    border-left: 3px solid var(--accent, #DC2626);
  }
  .priority-label { font-size: 11px; font-weight: 600; color: var(--accent, #DC2626); text-transform: uppercase; }
  .priority-text { font-size: 13px; color: #999; margin-top: 4px; }

  /* Right: metaphor area */
  .metaphor {
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center;
  }
  .metaphor-word { font-size: 16px; font-weight: 700; letter-spacing: 4px; }
  .metaphor-sub { font-size: 11px; color: #666; font-style: italic; margin-top: 8px; }

  /* Bottom stats */
  .stats {
    position: absolute; bottom: 28px; left: 40px;
    display: flex; gap: 24px;
    font-size: 13px; color: #666;
  }
  .stat-value { color: #e5e5e5; font-weight: 700; font-size: 15px; }
</style>
</head>
<body>
  <!-- Fill with actual data -->
</body>
</html>
```

**Accent colors** — choose based on day type:

| Color | Hex | When |
|-------|-----|------|
| Red | `#DC2626` | Urgent, deadline day |
| Blue | `#3B82F6` | Deep work, calm day |
| Amber | `#D97706` | Creative, launch day |
| Green | `#059669` | Growth, learning day |
| Purple | `#7C3AED` | Strategy, planning |

Save HTML to project root or specified path. Open in browser and screenshot for sharing.

## Customization

- **Add your project names** to priority labels
- **Connect your calendar** by updating the script path
- **Change accent logic** to match your energy patterns
- **Add new metaphors** that resonate with your work

## Principles

- **ONE focus** — if you can't pick one priority, the skill isn't working
- **Specific, not generic** — "finalize Q1 report" not "work on documents"
- **Visual consistency** — dark theme, monospace, minimal decoration
- **Weekday-aware** — Friday = retrospective, Monday = week overview
