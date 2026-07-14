# AIN3 · Personal Harness

Публичный harness для **одного повторяемого процесса**. Пакет превращает операционный бриф в контур, который агент открывает, выполняет, проверяет и продолжает с точной точки.

Собран для **AI-Native Sprint III** · W1 · Personal OS + Skills.

## Что получится

За 25–40 минут у тебя появятся:

- один выбранный процесс и проверяемый результат;
- карта из 3–5 источников;
- единая конвенция имён;
- интерактивный naming builder для personal, team и model-data контуров;
- Agent Passport и Agent Registry с owner, scope, audit и stop controls;
- `AGENTS.md` или `CLAUDE.md` с картой среды и границами;
- первый `SKILL.md`;
- первый результат в `output/`;
- строка evidence, по которой улучшается следующий прогон.

## Живые поверхности

| Поверхность | Что можно сделать |
|---|---|
| [`rules/`](rules/) | открыть 13 договорённостей в 6 зонах harness и скопировать deep link |
| [`naming/`](naming/) | собрать canonical filename для personal, team и model-data контуров |
| [`playground/`](playground/) | скомпилировать сырой процесс в компактный context pack и скачать Markdown |
| [`graph/`](graph/) | пройти Harness Atlas: люди, артефакты, skills, маршруты и evidence |
| [публичный дек](https://ain3-personal-harness.alex-named.chatgpt.site/deck/) | 21 слайд, кликабельный процесс и заметки спикера |

## Маршрут

1. Открой [`setup-checklist.md`](setup-checklist.md) и выбери один процесс.
2. Скопируй подходящий router-template в корень рабочей папки:
   - Codex и совместимые среды – [`AGENTS.md.template`](AGENTS.md.template) → `AGENTS.md`;
   - Claude Code – [`CLAUDE.md.template`](CLAUDE.md.template) → `CLAUDE.md`.
3. Собери пример в интерактивном [`naming builder`](naming/) и прими [`naming-convention.md`](naming-convention.md) как правило для новых файлов.
4. Если в контуре есть агенты или расписания, заполни [`agent-passport-template.md`](agent-passport-template.md) и добавь строки в [`agent-registry-template.md`](agent-registry-template.md).
5. Заполни [`operating-brief-template.md`](operating-brief-template.md), [`source-map-template.md`](source-map-template.md) и переносимый [`context-pack-template.md`](context-pack-template.md).
6. Выбери starter skills из `skills/`: operating brief, process audit, context pack, evidence review и session handoff.
7. Сделай первый прогон, сохрани [`agent-run-receipt.md`](agent-run-receipt.md) и запиши результат в [`evidence-log-template.md`](evidence-log-template.md).
8. Для передачи действующего контура используй [`harness-setup-handoff-template.md`](harness-setup-handoff-template.md).
9. Через 1–2 недели пройди [`refresh-ritual.md`](refresh-ritual.md).

Brief хранит portable contract из пяти полей: `trigger · inputs · output · owner · DoD`. M1 process view добавляет `action · review · metric`; процедура уходит в skill, human gate – в review, metric – в definition of done.

## Состав пакета

| Артефакт | Роль в системе |
|---|---|
| [`setup-checklist.md`](setup-checklist.md) | запуск контура за один вечер |
| [`stack-map.md`](stack-map.md) | карта слоёв, инструментов и переносимости |
| [`AGENTS.md.template`](AGENTS.md.template) | router для Codex и agent-compatible сред |
| [`CLAUDE.md.template`](CLAUDE.md.template) | router для Claude Code |
| [`naming/`](naming/) | интерактивный builder для personal, team и model-data имён |
| [`naming-convention.md`](naming-convention.md) | filename как общий индекс и canonical rule |
| [`rules/`](rules/) | explorer 13 правил и связанных артефактов |
| [`playground/`](playground/) | context pack compiler с autosave и Markdown export |
| [`graph/`](graph/) | кастомный Harness Atlas с фильтрами и deep links |
| [`agent-passport-template.md`](agent-passport-template.md) | identity, owner, scope, permissions, audit, expiry и kill switch |
| [`agent-registry-template.md`](agent-registry-template.md) | видимый реестр агентов, triggers, evidence и stop controls |
| [`operating-brief-template.md`](operating-brief-template.md) | trigger · inputs · output · owner · DoD |
| [`source-map-template.md`](source-map-template.md) | 3–5 минимально достаточных источников |
| [`context-pack-template.md`](context-pack-template.md) | goal · current · rules · examples · boundary для передачи состояния |
| [`agent-run-receipt.md`](agent-run-receipt.md) | воспроизводимый receipt одного агентного запуска |
| [`participant-progress-example.md`](participant-progress-example.md) | synthetic-схема прогресса без данных реального участника |
| [`skills/operating-brief/SKILL.md`](skills/operating-brief/SKILL.md) | описание процесса → operating brief |
| [`skills/process-audit/SKILL.md`](skills/process-audit/SKILL.md) | шаги процесса → первый кандидат на автоматизацию |
| [`skills/context-pack/SKILL.md`](skills/context-pack/SKILL.md) | точное рабочее состояние → переносимый context pack |
| [`skills/evidence-review/SKILL.md`](skills/evidence-review/SKILL.md) | claims, sources и privacy boundary → review receipt |
| [`skills/session-handoff/SKILL.md`](skills/session-handoff/SKILL.md) | текущая сессия → точный restart в другом runtime |
| [`evidence-log-template.md`](evidence-log-template.md) | факт прогона → точечное изменение системы |
| [`demo/one-workflow-seed.md`](demo/one-workflow-seed.md) | заполненный synthetic example |
| [`refresh-ritual.md`](refresh-ritual.md) | поддержка контура раз в 1–2 недели |
| [`harness-setup-handoff-template.md`](harness-setup-handoff-template.md) | assess → compare → recommend → dashboard и точный restart |

## Структура рабочей папки

```text
my-workspace/
├── AGENTS.md               # или CLAUDE.md
├── sources/                # входы процесса
├── output/                 # проверяемые результаты
├── evidence-log.md         # история прогонов
└── .agents/skills/         # Codex
    └── <skill>/SKILL.md
```

Для Claude Code используй `.claude/skills/`. Можно хранить один canonical `SKILL.md` и синхронизировать его в runtime-папки.

## Принцип

**Один процесс → один контекст → один прогон → один evidence-сигнал.** Следующий прогон становится лучше через правку источников, правил или skill.

Переносимая ценность контура – **нормализованный контекст**, который одинаково читают человек, команда и агент.

AI Mindset · [программа AIN3](https://ai-native.aimindset.org/) · [public site](https://ain3-personal-harness.alex-named.chatgpt.site/) · [публичный дек](https://ain3-personal-harness.alex-named.chatgpt.site/deck/) · [@ai_mind_set](https://t.me/ai_mind_set)
