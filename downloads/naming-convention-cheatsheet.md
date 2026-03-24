# Naming Convention Cheatsheet

> A consistent naming convention is the foundation of a Personal OS.
> Without it, your vault becomes unsearchable in 2 weeks.
> With it, both you AND your AI agent can find anything instantly.

## The Format

```
{type} description – YYYY-MM-DD.md
```

**Key rules:**
- **Type in curly braces** — `{meeting}`, `{research}`, `{rule}`
- **Date always at the end** after en dash (–)
- **Lowercase description** — natural language, no camelCase
- **No special characters** except braces and en dash

## Standard Types

| Type | When to use | Example |
|------|-------------|---------|
| `{meeting}` | Meeting notes, syncs | `{meeting} team standup – 2026-03-24.md` |
| `{decision}` | Decision records | `{decision} switch to Linear – 2026-03-20.md` |
| `{research}` | Analysis, exploration | `{research} MCP server comparison – 2026-03-18.md` |
| `{draft}` | Work in progress | `{draft} onboarding flow – 2026-03-15.md` |
| `{rule}` | Standards, policies | `{rule} code review process – 2026-03-10.md` |
| `{prd}` | Product requirements | `{prd} notification system – 2026-03-08.md` |
| `{guide}` | How-to guides | `{guide} MCP setup – 2026-03-05.md` |
| `{transcript}` | Call/meeting transcripts | `{transcript} client call – 2026-03-24.md` |
| `{skill}` | Skill documentation | `{skill} morning brief – 2026-03-01.md` |
| `{overview}` | High-level summaries | `{overview} Q1 progress – 2026-03-24.md` |

## With Project Prefix

For multi-project work, add a project code before the type:

```
{PROJECT} {type} description – YYYY-MM-DD.md
```

**Examples:**
- `{ACME} {meeting} sprint review – 2026-03-24.md`
- `{ACME} {prd} user dashboard – 2026-03-20.md`
- `{SIDE} {research} market analysis – 2026-03-18.md`

## Why This Works

### For humans
- **Sortable** — files group by type naturally
- **Scannable** — type tag tells you what it is at a glance
- **Searchable** — `{meeting}` finds all meeting notes instantly

### For AI agents
- **Parseable** — structured format = reliable extraction
- **Discoverable** — agents can `find . -name "{meeting}*"` to get all meetings
- **Predictable** — agents know where to save new files

## Anti-Patterns

| Bad | Why | Good |
|-----|-----|------|
| `Meeting Notes 03-24.md` | No type tag, ambiguous date | `{meeting} team sync – 2026-03-24.md` |
| `meeting-notes-2026-03-24.md` | No type system, harder to parse | `{meeting} client review – 2026-03-24.md` |
| `2026-03-24 research.md` | Date first breaks alphabetical grouping | `{research} competitor analysis – 2026-03-24.md` |
| `RESEARCH_competitive_analysis.md` | No date, screaming case | `{research} competitive analysis – 2026-03-24.md` |
| `notes.md` | No context at all | `{meeting} onboarding sync – 2026-03-24.md` |

## Quick Rules

1. **Always use a type** — even for quick notes, pick `{draft}`
2. **Always add a date** — you'll thank yourself in 3 months
3. **Keep descriptions short** — 3-5 words max
4. **Use en dash** (–) before the date, not hyphen (-) or em dash (—)
5. **One file = one topic** — don't dump everything into one note

## YAML Frontmatter (Optional)

For Obsidian/vault users, add frontmatter:

```yaml
---
tags:
  - type/meeting
  - project/acme
date: 2026-03-24
type: meeting
status: done
---
```

## Interactive Tool

Try the naming convention formatter:
**https://ai-mindset-org.github.io/pos-stack-explorer/naming.html**

Type your file description and it generates the correct name with proper format, type tag, and date.

## Teaching Your Agent

Add this to your CLAUDE.md:

```markdown
## File Naming Convention

Format: `{type} description – YYYY-MM-DD.md`

Types: meeting, decision, research, draft, rule, prd, guide, transcript

ALWAYS follow this format when creating files.
NEVER create files without a type tag and date.
```

Your agent will follow the convention automatically for every new file.
