# Agent Registry

Реестр превращает невидимые процессы в видимый контур. Одна строка отвечает на вопросы: кто работает, по чьему решению, с каким доступом, где evidence и как остановить.

**Registry owner:** `<person or role>`  
**Scope:** `<workspace / team / product>`  
**Last verified:** `<YYYY-MM-DD>`  
**Next review:** `<YYYY-MM-DD>`

## Status vocabulary

| Status | Meaning |
|---|---|
| `draft` | контракт собирается, production trigger выключен |
| `active` | агент имеет действующий trigger и owner |
| `paused` | trigger выключен, конфигурация сохранена |
| `unknown` | процесс обнаружен, ownership или config пока не подтверждены |
| `retired` | trigger и credentials отозваны, evidence сохранён |

## Registry

| ID | Agent / process | Owner | Runtime | Status | Trigger | Scope | Tools + access | Data boundary | Risk | Last run | Log / evidence | Expiry / review | Stop / revoke | Passport |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `<agent-id>` | `<name>` | `<owner>` | `<runtime>` | `draft` | `<manual / schedule / event>` | `<projects and actions>` | `<tool: read/write>` | `<local / team / public / restricted>` | `<0–3>` | `<date + trace>` | `<path or URL>` | `<date>` | `<exact control>` | `[open](agent-passport-template.md)` |

## Visibility gaps

Для каждого обнаруженного процесса с неполным контрактом оставь строку. Поля без независимого evidence получают значение `unknown`.

| Process / signal | Seen in | Missing owner | Missing config | Missing log | Missing stop control | Next read-only probe |
|---|---|---|---|---|---|---|
| `<process name>` | `<ps output / cron / file / service>` | `yes / no` | `yes / no` | `yes / no` | `yes / no` | `<path or command>` |

## Entry-point map

```text
<trigger>
  ↓
<agent or scheduled process>
  ↓ tools: <list>
<output destination>
  ↓ evidence: <log or artifact>
<owner review / next trigger>
```

## Review log

| Date | Reviewer | Added / changed | Evidence checked | Expired / retired | Follow-up |
|---|---|---|---|---|---|
| `<YYYY-MM-DD>` | `<name>` | `<rows>` | `<paths, logs, diffs>` | `<rows>` | `<one action>` |

## Registry checks

- [ ] Every active row has an owner and passport.
- [ ] Every active trigger maps to an output and evidence location.
- [ ] Write access is visible at row level.
- [ ] Sensitive boundaries are named without copying their contents.
- [ ] Unknown processes stay visible until verified or retired.
- [ ] Expired agents have triggers and credentials revoked.
- [ ] Registry links to current passports and run logs.

