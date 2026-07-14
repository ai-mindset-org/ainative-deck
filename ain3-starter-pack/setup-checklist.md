# Personal harness – setup checklist

## 0. Choose the unit of work

- [ ] The process repeats at least weekly.
- [ ] One person owns the result.
- [ ] The result can be shown as a file, record, message draft, table update or decision card.
- [ ] A human quality check can be stated before the run.

Write one sentence:

```text
When {trigger}, turn {inputs} into {output}; {owner} accepts it when {definition of done}.
```

## 1. Create the workspace

```text
my-workspace/
├── AGENTS.md or CLAUDE.md
├── sources/
├── output/
├── evidence-log.md
└── .agents/skills/ or .claude/skills/
```

- [ ] Copy the runtime router template.
- [ ] Fill operator, process, map, quality contract and autonomy boundaries.
- [ ] Add the canonical naming rule.
- [ ] Keep secrets and personal material outside the public/team source map.

## 2. Add minimum context

- [ ] Fill `operating-brief-template.md`.
- [ ] Fill `source-map-template.md` with 3–5 inputs.
- [ ] Add one accepted example to `sources/examples/` when available.
- [ ] Mark who approves the result.

## 3. Make agents visible

Before adding a scheduled or autonomous route, make the agent visible:

- [ ] Fill `agent-passport-template.md` with owner, scope, tools and data boundary.
- [ ] Add one row to `agent-registry-template.md`.
- [ ] Set an expiry or review date.
- [ ] Test the revoke route or local kill switch.

## 4. Install the first skill

- [ ] Copy `skills/operating-brief/SKILL.md` into the runtime skills folder.
- [ ] Copy `skills/process-audit/SKILL.md` into the runtime skills folder.
- [ ] Ask the agent to run `process-audit` against the brief.
- [ ] Select one high-frequency, high-pain step.

## 5. Run once

- [ ] Ask for one observable output.
- [ ] Save it in `output/` using the naming convention.
- [ ] Review facts, links, boundaries and definition of done.
- [ ] Record one evidence line.

## 6. Improve the system

Choose one update:

- source missing → update `source-map`;
- repeated instruction → update router or extract a skill;
- quality gap → sharpen definition of done;
- unsafe action → tighten autonomy boundary;
- good pattern → add an accepted example.

**Done for today:** the workspace contains a brief, source map, router, visible agent contract when relevant, first output and evidence line.
