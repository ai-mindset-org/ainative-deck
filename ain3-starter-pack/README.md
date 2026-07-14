# AIN3 · Personal Setup – стартер-пак

Минимальная переносимая инфосистема для одного рабочего процесса. Клонируешь, заполняешь под свой процесс, запускаешь за вечер.

Собран для участников **AI-Native Sprint v3** (AI Mindset). Наследует линию `ainative-lab → ainative-lab-2`.

## Что внутри

| Файл | Зачем |
|---|---|
| [`CLAUDE.md.template`](CLAUDE.md.template) | остов файла правил: агент читает его до твоего первого сообщения |
| [`naming-convention.md`](naming-convention.md) | имя файла = база данных; одна конвенция на всё |
| [`operating-brief-template.md`](operating-brief-template.md) | паспорт процесса: 5 вопросов + матрица agent/automation/checklist |
| [`context-pack-template.md`](context-pack-template.md) | рабочее состояние: goal, current, rules, examples, boundary |
| [`evidence-log-template.md`](evidence-log-template.md) | журнал утверждений, источников, проверок и следующих шагов |
| [`agent-run-receipt.md`](agent-run-receipt.md) | воспроизводимый receipt одного агентного запуска |
| [`participant-progress-example.md`](participant-progress-example.md) | синтетическая схема прогресса без данных реального участника |
| [`skills/operating-brief/SKILL.md`](skills/operating-brief/SKILL.md) | скилл: сырой процесс → operating brief |
| [`skills/process-audit/SKILL.md`](skills/process-audit/SKILL.md) | скилл: разобрать процесс на автоматизируемые куски |
| [`skills/context-pack/SKILL.md`](skills/context-pack/SKILL.md) | скилл: передать точное состояние между людьми и агентами |
| [`skills/evidence-review/SKILL.md`](skills/evidence-review/SKILL.md) | скилл: проверить факты, источники и privacy boundary |
| [`skills/session-handoff/SKILL.md`](skills/session-handoff/SKILL.md) | скилл: продолжить работу в другой модели или на другом компьютере |
| [`refresh-ritual.md`](refresh-ritual.md) | чек-лист поддержки контура раз в 1–2 недели |
| [`demo/one-workflow-seed.md`](demo/one-workflow-seed.md) | заполненный пример целого контура – «куда дорастает» |

## Запуск

1. Поставь агентный runtime: `npm install -g @anthropic-ai/claude-code` (или Codex / Cursor – контур переносим).
2. Скопируй `CLAUDE.md.template` в корень рабочей папки как `CLAUDE.md`, заполни 5 полей.
3. Прими конвенцию из `naming-convention.md` – агент будет называть файлы по ней.
4. Возьми `operating-brief-template.md`, заполни под **один** свой процесс (тот, что повторяется чаще раза в неделю).
5. Запусти скилл `operating-brief`, получи бриф; прогони `process-audit` – увидишь, что автоматизируется.
6. Первый прогон → файл в `output/`. Это диагностика, не финал.

## Принцип

> Один процесс, один контекст, один первый прогон. Не строй идеального агента сразу.

Твоя единственная переносимая ценность – собственный **нормализованный контекст**, с которым работают и люди, и агенты. Этот пак – форма, в которую его складывают.

Вопросы – [@ai_mind_set](https://t.me/ai_mind_set).
