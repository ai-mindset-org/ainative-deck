---
name: process-audit
description: Use when an operating brief or process description exists and the user needs to identify the first automation candidate, assign agent/automation/person roles, map human gates, and place each step on the adoption curve. Triggers include “разбери процесс”, “process audit”, “что автоматизировать”, and “приоритизируй шаги”.
---

# process-audit

Map one process into steps and select one high-leverage candidate for the next run.

## Inputs

- An operating brief or equivalent process description.
- Frequency, pain and current execution signals when available.

## Workflow

1. Split the process into 4–8 steps from trigger to accepted output.
2. Rate each step:
   - frequency: low / medium / high;
   - pain: time / quality / coordination / risk;
   - context readiness: missing / partial / ready.
3. Mark the adoption level:
   - `overlay` – AI assists inside the current process;
   - `abstraction` – the step has a reusable skill or template;
   - `AI-native` – the workflow is designed around the agent with human gates.
4. Assign the executor: `agent`, `automation` or `person`.
5. Mark human gates for accountability, review and external side effects.
6. Select one candidate with high frequency, high pain and ready context.
7. Define a first-run output and evidence check.
8. Save as `output/{project} {analysis} process audit – YYYY-MM-DD.md`.

## Output

| step | frequency | pain | context | level | executor | human gate |
|---|---|---|---|---|---|---|

Add:

```text
first candidate: {one step}
first-run output: {observable artifact}
evidence: {measurable check}
```

## Evidence

- The process has 4–8 steps.
- Every step has frequency, pain, context readiness, level and executor.
- Human gates are explicit.
- Exactly one first candidate is selected.
- The candidate has a first-run output and measurable evidence.
