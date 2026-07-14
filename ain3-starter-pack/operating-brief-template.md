# Operating brief – process contract

Fill this for **one process** that repeats at least weekly. The brief becomes the handoff contract for a person or agent.

## Identity

- **project slug:** `{project}`
- **process name:** {2–6 words}
- **owner:** {person or role accountable for the result}
- **frequency:** {daily / weekly / event-driven}

## Five fields

1. **Trigger** – what starts the process?
2. **Inputs** – which approved data enters the process?
3. **Output** – which observable artifact or state appears?
4. **Owner** – who accepts the result and remains accountable?
5. **Definition of done** – which measurable checks prove quality?

```yaml
trigger: "{event or schedule}"
inputs:
  - "{input 1}"
  - "{input 2}"
output: "{file, record, message draft, table update or decision card}"
owner: "{person or role}"
definition_of_done:
  - "{observable check 1}"
  - "{observable check 2}"
```

## Source map

Keep 3–5 minimum sufficient sources. Use `source-map-template.md` for the full version.

| source | why it matters | access | boundary |
|---|---|---|---|
| {source 1} | {fact, decision, example or constraint} | {folder / API / MCP / export} | {public / external / team / local} |
| {source 2} | | | |
| {source 3} | | | |

## Process steps

The five-field brief is the portable contract. A runnable path expands it into the M1 process view:

```text
trigger · input · action · review · output · metric
```

`action` becomes the procedure inside a skill. `review` becomes the human gate. `metric` sharpens the definition of done.

| step | input | action | output | executor | human gate |
|---|---|---|---|---|---|
| 1 | | | | agent / automation / person | |
| 2 | | | | | |
| 3 | | | | | |

## First candidate

Choose one step with high frequency and high pain:

```text
candidate: {step}
reason: {frequency + pain + accessible context}
```

## First run contract

- Output filename: `{project} {output} description – YYYY-MM-DD.ext`
- Review owner: {person or role}
- Maximum run time: {minutes}
- Evidence line: `result · evidence · gap · system update`
- Next run: {date or trigger}
