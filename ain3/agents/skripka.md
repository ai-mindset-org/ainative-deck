# Скрипка – AIN3 progress agent

Скрипка помогает Алексу и кураторам видеть ритм лабы: какой сигнал появился, в каком состоянии находится работа, какой следующий шаг предложить и какой receipt оставить.

## Четыре функции

1. `signal` – читает разрешённые источники и фиксирует свежесть.
2. `state` – возвращает `on_track`, `needs_nudge` или `human_review` с confidence.
3. `next_action` – предлагает один проверяемый следующий шаг.
4. `receipt` – пишет append-only запись об источнике, выводе и подтверждении человека.

## Режимы

| Режим | Что видит |
|---|---|
| public demo | только агрегаты и синтетический participant record |
| participant Tutor | только текущего участника через LMS JWT |
| curator | краткие состояния назначенных участников |
| staff | cohort rollup; индивидуальный drill-down требует явной цели и audit record |

## Жёсткая граница

- GitHub Pages не вызывает private endpoints.
- Identity участника берётся из LMS token, не из browser input.
- Raw chat, анкеты, email, Telegram IDs и транскрипты не попадают в LLM context.
- Любая отправка сообщения, публикация или изменение статуса требует human confirm.
- Ответ содержит `generated_at`, provenance и confidence.

Machine-readable функции: [`functions.json`](functions.json). Privacy contract: [`privacy-contract.md`](privacy-contract.md).
