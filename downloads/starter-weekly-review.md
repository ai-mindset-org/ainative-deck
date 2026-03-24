---
name: weekly-review
description: "Friday weekly review — summarize wins, lessons, unfinished tasks, next week priorities. Triggers: /weekly-review, /review, week review, friday review."
version: 1.0
user_invocable: true
arguments:
  - name: scope
    description: "Review scope: work (default), personal, all"
    required: false
---

# Weekly Review Skill

End-of-week review that surfaces wins, lessons, unfinished work, and priorities for next week. Run on Friday (or whenever your week ends).

## Workflow

### Step 1: Gather Week Data

#### 1.1 Completed tasks

If Linear/task tool configured:
```
mcp__linear__list_issues(assignee: "me", status: "completed")
# Filter to this week only
```

Or search local:
```bash
# Find files modified this week
find . -name "*.md" -mmin -10080 \
  -not -path "./.obsidian/*" \
  -not -path "./node_modules/*" \
  2>/dev/null | head -30
```

#### 1.2 This week's sessions

```bash
# Claude sessions from this week
WEEK_START=$(date -v-5d +%Y%m%d 2>/dev/null || date -d "5 days ago" +%Y%m%d)
touch -t ${WEEK_START}0000 /tmp/review-week-marker 2>/dev/null
find ~/.claude/projects -name "*.jsonl" -newer /tmp/review-week-marker -maxdepth 3 2>/dev/null
```

For each session, extract project + topic from first user message.

#### 1.3 Calendar events this week

```bash
"$HOME/.claude/scripts/gcal-smart.sh" week 2>/dev/null
```

Or Krisp:
```
mcp__krisp__search_meetings(query: "this week")
mcp__krisp__list_activities
```

#### 1.4 Unfinished tasks

```
mcp__linear__list_issues(assignee: "me", status: "started")
mcp__linear__list_issues(assignee: "me", status: "unstarted")
```

### Step 2: Analyze

Categorize everything into:

1. **WINS** — what shipped, what closed, what moved forward
2. **LESSONS** — what broke, what was harder than expected, what you learned
3. **UNFINISHED** — carry-forward items, why they stalled
4. **PATTERNS** — recurring themes across the week
5. **NEXT WEEK** — top 3 priorities based on momentum + deadlines

### Step 3: Output

```markdown
## Weekly Review — W{week_number} · {date_range}

### Wins
- {Completed deliverable or milestone}
- {Problem solved}
- {Progress on important project}

### Numbers
| Metric | Value |
|--------|-------|
| Tasks closed | {N} |
| Meetings | {N} |
| Focus hours | ~{N}h |
| Sessions | {N} |

### Lessons
- **{Topic}** — {what happened, what you learned}
- **{Topic}** — {insight}

### Unfinished
- [ ] {Task} — {why it stalled, what's needed}
- [ ] {Task} — {blocker}

### Patterns
> {Observation about how your week went — e.g., "too many context switches",
> "momentum on project X", "meetings clustered on Wed"}

### Next Week — Top 3
1. **{Priority}** — {specific deliverable or milestone}
2. **{Priority}** — {specific deliverable or milestone}
3. **{Priority}** — {specific deliverable or milestone}

### Energy Check
{How did energy feel this week? Which days were productive?
What drained energy? What gave energy?}
```

### Step 4: Save

Save to your notes/reviews folder:

```bash
# Suggested path
echo "reviews/weekly-review-W{week_number}-{date}.md"
```

## Friday Ritual Prompt

After generating the review, suggest:

```
Review done. Suggested actions:
1. Close stale tasks that won't happen
2. Move carry-forward items to next week
3. Block focus time for top priorities
4. Share wins with team (if applicable)
```

## Principles

- **Wins first** — start with what went right, not what failed
- **Honest lessons** — no spin, just what happened and what you learned
- **Carry-forward discipline** — if something was unfinished 2 weeks in a row, it needs a decision: do, delegate, or drop
- **Patterns over events** — weekly review is about trends, not just a list
- **5 minutes max** — if the review takes longer, you're overthinking it

## Customization

- **Add team review** — include what your reports/team accomplished
- **Add personal goals** — track non-work goals alongside work
- **Add health/energy tracking** — rate each day 1-5 for energy
- **Connect to OKRs** — map wins to quarterly objectives
