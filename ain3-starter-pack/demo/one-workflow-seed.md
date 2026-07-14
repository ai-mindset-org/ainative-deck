# {launch} {context} one workflow seed – 2026-07-14

Synthetic, sanitized example of a complete contour: a weekly product-launch digest.

## Operating brief

```yaml
trigger: "Friday 16:00"
inputs:
  - "team call transcripts from the last 7 days"
  - "tickets changed during the week"
  - "sanitized project-chat export"
output: "one-page weekly launch digest"
owner: "launch lead"
definition_of_done:
  - "sections: done / risks / next"
  - "every factual claim links to a source"
  - "the lead understands status and decisions in two minutes"
```

## Source map

| source | why it matters | access | freshness | boundary |
|---|---|---|---|---|
| team-call transcripts | decisions and blockers | `sources/transcripts/` | weekly | team |
| task export | planned and completed work | `sources/tasks/` | live export | team |
| sanitized project chat | current signals and risks | `sources/chat/` | weekly export | team |

## Context pack

- **goal:** one-page weekly launch digest;
- **current:** manual assembly takes about two hours;
- **rules:** done / risks / next, every factual claim has a source link;
- **examples:** `{launch} {output} weekly digest – 2026-07-04.md`;
- **boundary:** draft stays internal, sending requires owner approval, `private/` stays local.

## First skill

- **trigger:** “собери дайджест недели по запуску”;
- **steps:** read approved sources for 7 days → draft three sections → compare with accepted example → verify source links → save;
- **output:** `output/{launch} {output} weekly digest – YYYY-MM-DD.md`;
- **evidence:** file exists, fits one page, contains three sections, every claim links to a source.

## Process audit

| step | frequency | pain | context | level | executor | human gate |
|---|---|---|---|---|---|---|
| collect three sources | weekly | high time cost | ready | abstraction | agent | |
| draft three sections | weekly | high manual load | ready | abstraction | agent | |
| verify facts and links | weekly | quality risk | ready | overlay | person | review |
| send to leadership | weekly | external side effect | ready | overlay | person | approve + send |

**First candidate:** collect sources and draft the three-section digest. Context is ready; the step is frequent and time-consuming.

## First run

```text
output: output/{launch} {output} weekly digest – 2026-07-14.md
reviewer: launch lead
time budget: 10 minutes
```

## Evidence log

```text
2026-07-14 16:20 · weekly digest · draft in 4m · 8/9 claims linked · one risk missing · add project chat to source map · Friday 16:00
2026-07-04 16:30 · accepted example · manual version approved · baseline recorded · add to sources/examples · next Friday
```

## System update

The missing risk existed only in project chat. The source map now includes a sanitized weekly chat export. The skill keeps the same structure and quality contract.
