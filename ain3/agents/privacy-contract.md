# AIN3 Tutor + Скрипка – privacy contract

## Public

Публичный Hub и презентации содержат агрегаты с датой и знаменателем, публичные профили спикеров, синтетические примеры и публичные артефакты. По умолчанию browser calls отсутствуют. Локально настроенный presenter endpoint получает только `slideId`, `question`, `mode`, `publicOnly:true` и `synthetic:true`.

## Participant Tutor

`GET /api/v1/tutor/context/me?lab=ain3`

- JWT обязателен.
- Subject берётся только из token.
- Ответ: goal summary, stack tags, LMS progress, attendance summary, next actions.
- `Cache-Control: no-store`.
- Raw chat, transcript, email, username и данные других участников исключены.

## Staff Скрипка

- Отдельный admin-only route.
- Aggregate by default.
- Individual drill-down – только с явным purpose и audit record.
- Запись – append-only; изменение внешнего состояния требует human confirm.

## Service boundary

- Dataflow → LMS: HMAC + timestamp + IP allowlist.
- Schema: `aim.participant-context.v1`.
- Context payload ≤ 8 KB.
- Logs: request id + subject hash; context body не логируется.
- Нужны consent, export/delete и 90-day redaction до подключения raw participant context.
