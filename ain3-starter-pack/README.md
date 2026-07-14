# AIN3 · Personal Setup – стартер-пак

Минимальная переносимая инфосистема для одного рабочего процесса. Не идея, а работающий контур: клонируешь, заполняешь под свой процесс, запускаешь за вечер.

Собран для участников **AI-Native Sprint v3** (AI Mindset). Наследует линию `ainative-lab → ainative-lab-2`.

## Что внутри

| Файл | Зачем |
|---|---|
| [`CLAUDE.md.template`](CLAUDE.md.template) | остов файла правил: агент читает его до твоего первого сообщения |
| [`naming-convention.md`](naming-convention.md) | имя файла = база данных; одна конвенция на всё |
| [`operating-brief-template.md`](operating-brief-template.md) | паспорт процесса: 5 вопросов + матрица agent/automation/checklist |
| [`skills/operating-brief/SKILL.md`](skills/operating-brief/SKILL.md) | скилл: сырой процесс → operating brief |
| [`skills/process-audit/SKILL.md`](skills/process-audit/SKILL.md) | скилл: разобрать процесс на автоматизируемые куски |
| [`refresh-ritual.md`](refresh-ritual.md) | чек-лист поддержки контура раз в 1–2 недели |
| [`demo/one-workflow-seed.md`](demo/one-workflow-seed.md) | заполненный пример целого контура – «куда дорастает» |

## Запуск за 25 минут

1. Поставь агентный runtime: `npm install -g @anthropic-ai/claude-code` (или Codex / Cursor – контур переносим).
2. Скопируй `CLAUDE.md.template` в корень рабочей папки как `CLAUDE.md`, заполни 5 полей.
3. Прими конвенцию из `naming-convention.md` – с этого момента файлы называет агент, не ты.
4. Возьми `operating-brief-template.md`, заполни под **один** свой процесс (тот, что повторяется чаще раза в неделю).
5. Запусти скилл `operating-brief`, получи бриф; прогони `process-audit` – увидишь, что автоматизируется.
6. Первый прогон → файл в `output/`. Это диагностика, не финал.

## Принцип

> Один процесс, один контекст, один первый прогон. Не строй идеального агента сразу.

Твоя единственная переносимая ценность – собственный **нормализованный контекст**, с которым работают и люди, и агенты. Этот пак – форма, в которую его складывают.

Лицензия: MIT. Вопросы – [@ai_mind_set](https://t.me/ai_mind_set).
