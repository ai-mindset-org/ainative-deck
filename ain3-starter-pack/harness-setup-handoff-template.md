# Harness Setup Handoff

Transfer packet for an existing AI work contour. The sequence is fixed: **assess → compare → recommend → dashboard**. Every score points to independent evidence. Comparison moves in both directions and protects the operator's confirmed strengths.

## Re-entry card

| Field | Value |
|---|---|
| Operator / contour | `<name + short description>` |
| Workspace | `<absolute path or URL>` |
| Repository | `<remote>` |
| Branch / revision | `<branch + SHA>` |
| Runtime entry point | `<command, app or URL>` |
| Current state | `<what is running, paused, complete>` |
| Last verified | `<YYYY-MM-DD HH:MM timezone>` |
| Completed in prior rounds | `<items that stay complete>` |
| Open decision | `<one decision and owner>` |
| Exact first action | `<read-only probe or next approved build step>` |
| Expected signal | `<file, output, log line or browser state>` |
| Stop rule | `<condition that ends this run>` |

## Scope and posture

**Assessment scope:** `<systems, folders, runtimes, time range>`  
**Excluded / sensitive boundary:** `<confirm existence only>`  
**Reference pattern:** `<anonymized contour used for comparison>`  
**Write policy during assessment:** `read-only`  
**Scoring test:** `survives one week without the operator`

Working rules:

1. Capture evidence before assigning a score or suggesting an option.
2. Keep independent observations separate from agent self-description.
3. Mark missing evidence as `unknown` or `partial-unverified`.
4. Run the strength pass before the gap pass.
5. Preserve deliberate isolation and sensitive boundaries.
6. Build on completed rounds and avoid repeating prior inventory work.

## 1. Assess

### 1.1 Evidence ledger

Evidence comes from config files, process state, logs, timestamps, git history, diffs and output artifacts.

| ID | Layer / probe | Path, command or surface | Observation | Captured at | Confidence | Sensitive boundary |
|---|---|---|---|---|---|---|
| `E-01` | `<environment / tools / harness / operator>` | `<path or command>` | `<what exists independently of narration>` | `<timestamp>` | `verified / partial / unknown` | `<none / existence confirmed>` |

### 1.2 Bottom-up walk

#### Environment

- Evidence IDs: `<E-…>`
- Runtime and process state: `<observation>`
- Filesystem, network and service boundaries: `<observation>`
- Recovery path: `<observation>`

#### Tools and skills

- Evidence IDs: `<E-…>`
- Tools with read access: `<list>`
- Tools with write or execute access: `<list>`
- Skill source of truth and duplication: `<observation>`
- MCP safety and revoke path: `<observation>`

#### Harness

- Evidence IDs: `<E-…>`
- Global and local instruction entry points: `<paths>`
- Context assembly and unit of context: `<observation>`
- Permissions, lifecycle, eval and telemetry: `<observation>`
- Agent registry / passport coverage: `<observation>`

#### Operator

- Evidence IDs: `<E-…>`
- Ownership and review cadence: `<observation>`
- Decisions still held in memory: `<observation>`
- Bus-factor signal: `<observation>`

### 1.3 Scorecard

Bands: `absent 0–30` · `partial 31–70` · `mature 71–100`. A score requires two independent observations. Each evidence-to-band line states what was seen, why it fits the band and what pain it maps to.

| Axis | Band | Score | Evidence IDs | Evidence → band reasoning | Pain / dependency |
|---|---:|---:|---|---|---|
| Entry-point legibility | `<band>` | `<0–100 / unknown>` | `<E-…>` | `<observation → band>` | `<pain>` |
| Version control of infra and prompts | `<band>` | `<score>` | `<E-…>` | `<reasoning>` | `<pain>` |
| Observability of agent actions | `<band>` | `<score>` | `<E-…>` | `<reasoning>` | `<pain>` |
| Progress / convergence signal | `<band>` | `<score>` | `<E-…>` | `<reasoning>` | `<pain>` |
| Unit of context | `<band>` | `<score>` | `<E-…>` | `<reasoning>` | `<pain>` |
| Agent isolation and safety | `<band>` | `<score>` | `<E-…>` | `<reasoning>` | `<pain>` |
| Knowledge, backup and recovery | `<band>` | `<score>` | `<E-…>` | `<reasoning>` | `<pain>` |
| Operator load / bus-factor | `<band>` | `<score>` | `<E-…>` | `<reasoning>` | `<pain>` |
| Naming convention | `<band>` | `<score>` | `<E-…>` | `<reasoning>` | `<pain>` |
| Cross-linking | `<band>` | `<score>` | `<E-…>` | `<reasoning>` | `<pain>` |

#### Naming lens

- Filename grammar: `<example and source>`
- Controlled type vocabulary: `<where defined>`
- Root `AGENTS.md` / index as context unit: `<path and coverage>`
- Session and artifact addressability: `<ID / deeplink pattern>`

#### Cross-linking lens

- Visibility: `<session lists, logs and deeplinks across runtimes>`
- Reuse: `<canonical skill + router→spoke pull path>`
- Isolation preserved: `<surfaces that stay separate>`
- Sensitive surfaces excluded from bridging: `<boundary>`

### 1.4 Refusals and blind spots

| Item | Why evidence is insufficient or access is excluded | Safe next probe |
|---|---|---|
| `<axis or claim>` | `<reason>` | `<read-only option>` |

## 2. Compare

### 2.1 Strength pass

At least one confirmed strength is required. A strength includes evidence and a protection rule.

| Current contour is stronger at | Evidence IDs | Why it works here | Protection rule | What the reference can learn |
|---|---|---|---|---|
| `<strength>` | `<E-…>` | `<reason>` | `KEEP: <choice>` | `<bidirectional transfer>` |

### 2.2 Layer comparison

Verdicts: `PARITY` · `GAP` · `DIVERGENCE→WEAKER` · `DIVERGENCE→EQUAL` · `DIVERGENCE→STRONGER`.

| Layer / axis | Reference pattern | Current contour | Verdict | Evidence IDs | Fit 0–5 | Friction 0–5 | Note |
|---|---|---|---|---|---:|---:|---|
| `<layer>` | `<anonymized pattern>` | `<specific observation>` | `<verdict>` | `<E-…>` | `<score>` | `<score>` | `<1–3 lines>` |

## 3. Recommend

Use a small set: `MUST 1–3` · `COULD 2–4` · `LATER 2–3`. Rank inside each tier by `fit − friction`. Each move is an option grounded in a named pain and a refusal threshold.

### `<MUST / COULD / LATER>` · `<move name>`

- Evidence IDs: `<E-…>`
- Named pain: `<pain from scorecard>`
- Thin version: `<smallest useful contour>`
- Why it fits: `<operator constraint and evidence>`
- One option: `<non-prescriptive sketch>`
- First step, ≤20 min: `<one action>`
- Refusal threshold: `<skip or stop condition>`
- Fit / friction: `<0–5> / <0–5>`
- Depends on: `<dependency or none>`
- Strength protected: `<strength from 2.1>`
- Evidence of completion: `<artifact or signal>`

### Ranked moves

| Tier | Move | Fit | Friction | First step | Refusal threshold | Evidence of completion |
|---|---|---:|---:|---|---|---|
| `MUST` | `<move>` | `<0–5>` | `<0–5>` | `<≤20 min>` | `<condition>` | `<signal>` |

**If you do one thing:** `<highest-leverage move>`  
**Strength to protect:** `<confirmed strength>`  
**Genuinely blocked:** `<item + what unblocks it>`

## 4. Dashboard

**Dashboard path:** `<self-contained .html>`  
**Source assessment:** `<this file or linked report>`  
**Last rendered:** `<timestamp>`

Dashboard contract:

- [ ] One HTML file with inline CSS and JS; opens from `file://`.
- [ ] Black, white and paper surface; red marks gaps and live attention.
- [ ] Per-axis lanes show the maturity profile before any composite.
- [ ] Naming and cross-linking render as axes in this dashboard.
- [ ] `STRONGER` contains at least one evidence-backed item.
- [ ] Compare and recommendations come from sections 2 and 3.
- [ ] One clearly marked `FILL START / FILL END` data block drives the UI.
- [ ] Reference names, paths, team labels and codenames are anonymized.
- [ ] Copyable handoff prompt is available in a readonly textarea.
- [ ] Browser QA covers desktop, mobile, tabs, theme and copy action.

## Transfer ledger

### Current contour → reference

- `<strength or pattern worth carrying back>`

### Reference → current contour

- `<selected option with fit and friction>`

### Deliberate divergences to keep

- `<choice + evidence + owner>`

## Restart handoff

### Artifacts

| Artifact | Path / URL | Status | Last verified | Owner |
|---|---|---|---|---|
| Assessment | `<path>` | `<draft / complete>` | `<timestamp>` | `<owner>` |
| Dashboard | `<path>` | `<draft / complete>` | `<timestamp>` | `<owner>` |
| Agent registry | `<path>` | `<status>` | `<timestamp>` | `<owner>` |
| Passports | `<path or index>` | `<status>` | `<timestamp>` | `<owner>` |
| Evidence archive | `<path>` | `<status>` | `<timestamp>` | `<owner>` |

### Session continuity

| Runtime | Session / task ID | Resume command or deeplink | State |
|---|---|---|---|
| `<runtime>` | `<ID>` | `<exact command or URL>` | `<what this session knows>` |

### Exact restart

```text
Working directory: <absolute path>
Branch / revision: <branch + SHA>
Open first: <file or URL>
Run first: <exact command>
Expected result: <observable signal>
Next action: <one action>
Stop when: <condition>
Do not redo: <completed inventory or round>
Escalate to: <owner + decision boundary>
```

### Open questions

1. `<question · owner · deadline>`
2. `<question · owner · deadline>`

### Final integrity check

- [ ] Every score links to evidence.
- [ ] Every recommendation follows its evidence and score.
- [ ] Agent self-report is labeled `[unverified]`.
- [ ] Sensitive boundaries remain unopened.
- [ ] At least one current strength is named and protected.
- [ ] Naming and cross-linking axes are scored.
- [ ] Dashboard matches the latest assessment.
- [ ] Restart command, expected signal and stop rule are concrete.
- [ ] Cross-links open and session IDs resume.

