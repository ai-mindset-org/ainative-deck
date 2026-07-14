# Naming convention – filename as index

Имя файла помогает человеку и агенту определить **контур, тип и дату** до чтения содержимого.

## Канон

```text
{project} {type} description – YYYY-MM-DD.ext
```

```text
{crm} {meeting} weekly pipeline sync – 2026-07-14.md
 └─ где  └─ что        └─ о чём         └─ когда
```

| Сегмент | Правило | Пример |
|---|---|---|
| `{project}` | короткий stable slug контура | `{crm}`, `{ops}`, `{launch}` |
| `{type}` | один тип из контролируемого словаря | `{meeting}`, `{process}`, `{brief}` |
| `description` | 2–6 слов на латинице, lower case | `weekly pipeline sync` |
| `–` | en dash, U+2013, с пробелами | ` … – 2026-07-14.md` |
| `YYYY-MM-DD` | дата всегда в конце | `2026-07-14` |
| `.ext` | расширение артефакта | `.md`, `.csv`, `.json`, `.html` |

## Код этой лаборатории

Canonical project slug материалов третьего потока – **`{ain3}`**. Он связывает шаблоны, правила, handoff и учебные артефакты программы.

В собственном рабочем процессе участник выбирает отдельный stable slug: `{self}`, `{crm}`, `{ops}`, `{launch}`. Так program context и operational context остаются адресуемыми и могут ссылаться друг на друга.

```text
{ain3} {rule} personal harness – 2026-07-14.md
{ain3} {template} context pack – 2026-07-14.md
{ain3} {template} agent passport – 2026-07-14.md
{ain3} {template} agent registry – 2026-07-14.md
{ain3} {skill} first workflow – 2026-07-14.md
{ain3} {handoff} harness setup – 2026-07-14.md
```

`s3`, `AIN03` и `s6-ain` остаются legacy aliases в старых материалах. Новые артефакты программы получают `{ain3}`.

## Базовый словарь типов

| Тип | Когда использовать |
|---|---|
| `{brief}` | краткая спецификация процесса или задачи |
| `{meeting}` | заметка или результат конкретной встречи |
| `{research}` | внешний или внутренний исследовательский snapshot |
| `{analysis}` | разбор данных, ситуации или вариантов |
| `{process}` | живой how-to / SOP |
| `{context}` | context pack для запуска работы |
| `{decision}` | зафиксированное решение |
| `{output}` | результат прогона без более точного типа |
| `{log}` | журнал событий или прогонов |
| `{draft}` | материал в работе |
| `{rule}` | постоянная договорённость или стандарт |
| `{template}` | заполняемый контракт или форма |
| `{skill}` | переносимая процедура с trigger и quality checks |
| `{handoff}` | точка продолжения между сессиями или операторами |
| `{registry}` | индекс агентов, capabilities или runtime state |
| `{dataset}` | набор данных с явной схемой и snapshot-датой |

Команда может расширить словарь. Один смысл получает один canonical type.

## Примеры

```text
{crm} {meeting} weekly pipeline sync – 2026-07-14.md
{lab} {research} participant context scan – 2026-07-14.md
{ops} {process} invoice approval flow – 2026-07-14.md
{launch} {brief} weekly digest workflow – 2026-07-14.md
{launch} {output} weekly digest – 2026-07-14.md
{launch} {log} workflow evidence – 2026-07-14.md
{ain3} {template} agent passport – 2026-07-14.md
{ain3} {handoff} harness setup – 2026-07-14.md
{model} {dataset} instruction corpus – 2026-07-14.jsonl
```

## Системные исключения

Некоторые файлы имеют фиксированные имена, потому что runtime ищет их по контракту:

```text
README.md
AGENTS.md
CLAUDE.md
SKILL.md
CHANGELOG.md
LICENSE
evidence-log.md
```

Эти имена не переводятся в project/type/date-формат.

## Инварианты

1. **Файлы называет агент.** Правило лежит в `AGENTS.md` / `CLAUDE.md` и применяется при каждом создании.
2. **Дата завершает имя.** Версии и статусы идут в frontmatter или git history.
3. **Описание остаётся читаемым.** Slug soup, `final-final-v3` и случайные сокращения ухудшают поиск.
4. **Тип выбирается из словаря.** Новый тип добавляется вместе с определением.
5. **Переименование сохраняет ссылки.** В knowledge-base используй среду, которая обновляет backlinks, или проверяй ссылки через поиск.

## Вставка в router-файл

```md
## File naming

- New working files: `{project} {type} description – YYYY-MM-DD.ext`.
- Description: latin, lower case, 2–6 words.
- Date: at the end. Separator: en dash (–, U+2013).
- Allowed types: brief, meeting, research, analysis, process, context,
  decision, output, log, draft, rule, template, skill, handoff, registry, dataset.
- Runtime files keep fixed names: README.md, AGENTS.md, CLAUDE.md, SKILL.md,
  evidence-log.md.
- The agent names files and checks existing siblings before creating one.
```

## Быстрый поиск

```bash
# все процессы проекта ops
rg --files | rg '^\{ops\} \{process\} '

# все meeting-артефакты
rg --files | rg ' \{meeting\} '

# всё, созданное 14 июля
rg --files | rg ' – 2026-07-14\.'
```

**Проверка:** по одному имени незнакомого файла можно восстановить, к какому контуру он относится, какой у него lifecycle и когда он создан.
