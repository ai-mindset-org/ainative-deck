# CLAUDE.md — Personal Operating System

> Drop this file into your project root. Claude Code reads it automatically on every session.
> This is your "constitution" — rules, context, and preferences that shape how Claude works with you.

## About Me

<!-- Fill in your context so Claude understands your role -->

- **Role:** [Your role — e.g., Product Manager, Engineer, Founder]
- **Company:** [Your company/project]
- **Timezone:** [Your timezone — e.g., Europe/Berlin, US/Pacific]
- **Language:** [Primary language for responses — e.g., English, Russian, mixed]

## Response Style

<!-- How you want Claude to communicate -->

- Be **concise** — short sentences, no filler
- Use **bold** for key concepts
- Use **en dash** (–) not em dash (—)
- Format responses in **markdown**
- When suggesting actions, provide **ready-to-run commands**

## Project Structure

<!-- Help Claude navigate your codebase/vault -->

```
project/
├── .claude/
│   ├── CLAUDE.md          ← this file
│   └── skills/            ← your custom skills
├── docs/                  ← documentation
├── src/                   ← source code
└── notes/                 ← meeting notes, decisions
```

## File Naming Convention

<!-- Consistent naming = agent can find things -->

**Format:** `{type} description – YYYY-MM-DD.md`

| Type | When to use |
|------|-------------|
| `{meeting}` | Meeting notes |
| `{decision}` | Decision records |
| `{research}` | Research and analysis |
| `{draft}` | Work in progress |
| `{rule}` | Rules and standards |

**Example:** `{meeting} Q1 planning – 2026-03-24.md`

## Skills

<!-- List your active skills so Claude knows what's available -->

| Skill | Trigger | What it does |
|-------|---------|-------------|
| `/morning-brief` | Morning routine | Gathers calendar + tasks, synthesizes focus |
| `/daily-focus` | Daily planning | Top priorities + energy level |
| `/meeting-prep` | Before meetings | Context + agenda + questions |
| `/weekly-review` | Fridays | Wins, lessons, next week priorities |

## Integrations

<!-- What tools/APIs are connected via MCP -->

| Tool | Purpose | Status |
|------|---------|--------|
| Calendar | Schedule awareness | [ ] connected / [ ] not yet |
| Linear/Jira | Task tracking | [ ] connected / [ ] not yet |
| Notion | Knowledge base | [ ] connected / [ ] not yet |

## Rules

<!-- Hard rules Claude must always follow -->

### ALWAYS
- Check calendar before scheduling suggestions
- Use the naming convention for new files
- Provide file paths as absolute paths
- Ask before creating new directories

### NEVER
- Create files without following naming convention
- Send messages to external channels without confirmation
- Delete files without asking
- Make assumptions about deadlines — check the data

## Context Management

<!-- For long sessions -->

When context gets heavy (>70% used), Claude should:
1. Save progress to files
2. Generate a handoff summary
3. Not start new complex tasks

## Evaluation

<!-- Self-check on every response -->

After each substantive response, evaluate:
- **T (Text):** Clear structure, actionable insights?
- **R (Rules):** Followed naming, formatting, folder rules?
- **C (Code):** If code involved — does it work, is it minimal?

---

## Quick Start

1. **Copy this file** to your project root as `CLAUDE.md`
2. **Fill in** the "About Me" section
3. **Add your skills** to `.claude/skills/`
4. **Connect integrations** via MCP servers
5. Run `claude` in your project — it reads CLAUDE.md automatically

## Next Steps

- [ ] Fill in "About Me" section
- [ ] Set up 1 skill (start with `/morning-brief`)
- [ ] Connect 1 integration (calendar recommended)
- [ ] Write 3 rules in ALWAYS/NEVER format
- [ ] Run your first `/morning-brief`
