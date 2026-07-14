# Personal harness – layers and tool choices

Tools can change. The contracts between layers keep the process portable.

| Layer | Contract | Minimal implementation | Optional surface |
|---|---|---|---|
| runtime | agent can read the workspace and execute a skill | Codex / Claude Code / Cursor | desktop app, terminal, IDE |
| context | approved inputs are findable and fresh | local files + source map | Obsidian, Drive, Notion, database |
| rules | role, map, quality and boundaries load before work | `AGENTS.md` / `CLAUDE.md` | organization policy service |
| procedure | repeatable action has trigger, steps and output | `SKILL.md` | workflow engine, automation |
| connectors | tools have explicit access routes | folder export / API / MCP | Calendar, Linear, GitHub, CRM |
| history | every material change is traceable | git + evidence log | Session Inspector, observability dashboard |
| surface | people can inspect and use the result | Markdown / HTML / table | dashboard, LMS, product UI |

## Selection rule

Choose the smallest tool that satisfies the layer contract. Add a service when the process needs shared access, schedule, permissions, volume or monitoring.

## Transfer rule

The portable unit contains:

```text
brief + source map + router + skill + accepted example + evidence
```

This unit can move from one runtime to another and from Personal OS to Team OS.
