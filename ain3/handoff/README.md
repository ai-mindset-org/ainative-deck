# AIN3 cross-session handoff – public pack

Этот пакет объединяет состояние двух рабочих веток:

- Codex: публикация и QA Personal Setup, свежий AIN3 dataflow, Lab Hub, public-safe Скрипка.
- Claude Code: подготовка занятия, артефакты Personal Setup, session inspector, naming и визуальные метафоры.

Полный private session map с локальными путями и внутренними сервисами хранится в team vault. Здесь нет персональных карточек, verbatim, токенов и private endpoints.

## Текущее состояние

- Canonical deck baseline: `93bb3b3`; версия `04777af` остаётся историческим референсом.
- Personal Setup: 18 слайдов, включая Скрипку и cross-session handoff.
- Intro: `779ed88`, 10 слайдов.
- Dataflow export: `80c80f6`, snapshot 14.07.2026.
- Public Hub: `/ain3/`.
- Public agent demo: синтетический, без сетевого запроса.
- Participant Tutor: self-only LMS JWT boundary.
- Staff Скрипка: contract готов; backend implementation остаётся следующим шагом.

## Продолжение

1. Клонировать `ai-mindset-org/ainative-deck` и открыть [`NEXT_PROMPT.md`](NEXT_PROMPT.md).
2. Проверить `git log -5 --oneline` и `ain3/manifest.json`.
3. Подтянуть private team vault и открыть актуальный AIN3 handoff.
4. Не переносить participant cards в browser или общий Tutor context.
5. После правок пройти desktop/mobile/keyboard/privacy QA.

## Известные риски

- Dataflow commit `94e6205` перевёл participant artifacts на rolling filenames. Exporter в deployed `55e52b0` продолжает читать dated filenames, поэтому export показывает `pre_lab_signals: absent` после успешного refresh.
- Прямая замена на `dated=False` может раздуть identity spine примерно до 193. Repair требует current-date rolling reader, legacy fallback, stale marker, duplicate handling, `rollups.roster_summary`, schema `1.2.0` и тесты.
- Roster и export имеют разные знаменатели: 120 rows / 112 submitted / 107 attendance identities.
- Attendance match rate недостаточен для автоматического индивидуального вывода.
- Tutor требует retention, consent, delete/export и redaction до расширенного participant context.
- LMS deploy остаётся незавершённым после `No space left on device`; production tag не создавался.
