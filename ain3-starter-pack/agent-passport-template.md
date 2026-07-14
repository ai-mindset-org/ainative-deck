# Agent Passport

Короткий контракт агента: кто им владеет, где он действует, к каким данным имеет доступ и как его остановить. Заполняется до первого production-run и обновляется после изменения scope, tools или risk tier.

## 1. Identity

| Поле | Значение |
|---|---|
| Agent ID | `<stable-id>` |
| Name | `<human-readable name>` |
| Owner | `<person or role>` |
| Backup owner | `<person or role>` |
| Version | `<semver or git sha>` |
| Status | `draft / active / paused / retired` |
| Runtime | `<Codex / Claude Code / custom / scheduled>` |
| Role | `<one sentence>` |
| Scope | `<projects, processes, folders, systems>` |
| Passport location | `<path or URL>` |

## 2. Invocation

| Поле | Значение |
|---|---|
| Trigger | `<manual / schedule / webhook / event>` |
| Invoker | `<who or what may start it>` |
| Inputs | `<required context and format>` |
| Output | `<artifact and destination>` |
| Definition of done | `<observable completion signal>` |
| Max runtime / iterations | `<stop limit>` |

## 3. Tools

| Tool | Capability | Access | Purpose | Revoke path |
|---|---|---|---|---|
| `<tool>` | `<read files / write issue / call API>` | `read / write / execute` | `<why required>` | `<command, config or owner>` |

## 4. Permissions

### Allowed

- `<action inside scope>`
- `<action inside scope>`

### Requires explicit approval

- `<external write, publish, payment, message, delete>`
- `<action with material impact>`

### Forbidden

- `<surface or action>`
- `<surface or action>`

## 5. Data boundary

| Поле | Значение |
|---|---|
| Allowed data scopes | `<local / team / public / named systems>` |
| Restricted scopes | `<private, financial, health, crisis, credentials>` |
| Secrets handling | `<provider and injection method; never paste values here>` |
| Storage destinations | `<paths, database, service>` |
| Retention | `<duration and cleanup owner>` |
| Export boundary | `<what may leave the local or team contour>` |
| Redaction rule | `<fields removed before sharing>` |

## 6. Risk tier

**Selected tier:** `<0 / 1 / 2 / 3>`

| Tier | Meaning | Default control |
|---|---|---|
| 0 | read-only, local, reversible | run log |
| 1 | bounded write inside owned workspace | diff review |
| 2 | external write or sensitive data | approval gate + audit |
| 3 | high-impact, financial, legal, production or identity action | named approver + kill switch + short expiry |

**Main failure modes:**

1. `<failure mode>`
2. `<failure mode>`
3. `<failure mode>`

## 7. Audit

| Поле | Значение |
|---|---|
| Log location | `<path or URL>` |
| Session / trace ID format | `<format>` |
| Events recorded | `<trigger, tools, writes, output, errors, stop>` |
| Evidence artifact | `<path or URL>` |
| Last verified run | `<YYYY-MM-DD · trace ID>` |
| Eval result | `<pass / fail / partial + link>` |
| Audit owner | `<person or role>` |

Agent self-description is marked `[unverified]`. Independent evidence comes from config, logs, diffs, process state and output artifacts.

## 8. Expiry and review

| Поле | Значение |
|---|---|
| Activated | `<YYYY-MM-DD>` |
| Expires | `<YYYY-MM-DD or event>` |
| Review cadence | `<weekly / monthly / per release>` |
| Next review | `<YYYY-MM-DD>` |
| Retirement condition | `<signal>` |

## 9. Kill switch

| Поле | Значение |
|---|---|
| Stop command / control | `<exact command, UI control or config change>` |
| Authorized operator | `<person or role>` |
| What stops immediately | `<processes, schedules, writes>` |
| Credential revocation | `<exact owner and surface>` |
| Stop verification | `<process, log or health signal>` |
| Recovery owner | `<person or role>` |

## 10. Learning loop

| Поле | Значение |
|---|---|
| Evidence source | `<run log, eval, human review>` |
| Eval rubric | `<path or URL>` |
| Update cadence | `<after 3 failures / monthly / release>` |
| Change owner | `<person or role>` |
| Self-modification | `disabled / proposal-only / bounded` |
| Versioning | `<git path, changelog or registry>` |
| Rollback | `<exact path or command>` |

## Launch gate

- [ ] Owner and backup owner are named.
- [ ] Scope, permissions and data boundary are concrete.
- [ ] Every write-capable tool has a revoke path.
- [ ] Risk tier matches the highest-impact action.
- [ ] Audit log and evidence artifact are reachable.
- [ ] Expiry or review date is set.
- [ ] Kill switch was tested.
- [ ] Passport is linked from the agent registry.

