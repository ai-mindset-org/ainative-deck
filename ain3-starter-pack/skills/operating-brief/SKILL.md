---
name: operating-brief
description: Use when a user describes a repeatable process and needs a process contract with trigger, inputs, output, owner, definition of done, source map and first-run contract. Triggers include “собери бриф процесса”, “operating brief”, “опиши процесс”, and “спецификация процесса”.
---

# operating-brief

Turn a raw process description into a concise contract that can be handed to a person or agent.

## Inputs

- User description of one repeatable process.
- Existing examples, rules or source paths when available.

## Workflow

1. Extract `trigger`, `inputs`, `output`, `owner`, `definition_of_done`.
2. Ask only for missing fields that materially change the contract.
3. Create a 3–5 item source map: `source · why · access · boundary`.
4. Break the process into 4–8 steps.
5. Mark the executor for each step: `agent`, `automation` or `person`.
6. Mark human gates for sending, publishing, deleting, spending and permission changes.
7. Choose one first candidate with high frequency, high pain and accessible context.
8. Define the first-run output, reviewer, time budget, evidence line and next trigger.
9. Save as `output/{project} {brief} <description> – YYYY-MM-DD.md`.

## Output

Use this self-contained structure so the skill stays portable after installation:

```md
# {process name} – operating brief

## Identity
- project slug:
- owner:
- frequency:

## Five fields
- trigger:
- inputs:
- output:
- owner:
- definition of done:

## Source map
| source | why it matters | access | boundary |
|---|---|---|---|

## Process steps
| step | input | action | output | executor | human gate |
|---|---|---|---|---|---|

## First candidate
- candidate:
- reason:

## First run contract
- output filename:
- review owner:
- maximum run time:
- evidence line: result · evidence · gap · system update
- next run:
```

## Evidence

- All five fields are present.
- Definition of done contains observable checks.
- Source map contains 3–5 sources with access and boundary.
- Every process step has an executor.
- Human gates are explicit.
- One first candidate is selected.
- Filename follows the canonical naming rule.
