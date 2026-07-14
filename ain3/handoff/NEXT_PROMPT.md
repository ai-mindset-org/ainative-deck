# Bootstrap prompt for the next model

Продолжи AIN3 Lab Hub и презентации с текущего `main` репозитория `ai-mindset-org/ainative-deck`.

Сначала:

1. Прочитай `ain3/handoff/README.md`, `ain3/manifest.json`, `ain3/agents/privacy-contract.md` и `AIN3_ASSISTANT_SPEC.md`.
2. Открой public routes `/ain3/`, `/ain3-intro.html#cover`, `/decks/ain3-personal-setup/`.
3. Проверь `git status`, `git log -5 --oneline`, GitHub Pages deployment и актуальный private handoff в team vault.

Сохрани дизайн-систему: тёмная сетка, крупная типографика, cyan/mint/amber accents, белый прозрачный AIM logo, реальные публичные фото, короткие подписи. Презентация идёт от людей к механике лабы и заканчивается недельным маршрутом. Артефакты показываются как реальные файлы и evidence. Метафоры – короткие визуальные якоря: сито, реторта, каталог, станок, cockpit, assay. Не добавляй абстрактные slop-слайды и длинный серый текст.

Privacy boundary:

- GitHub Pages – только агрегаты, публичные профили и synthetic demo.
- Participant Tutor – self-only через LMS JWT.
- Staff Скрипка – отдельный admin-only режим, aggregate by default, audited drill-down.
- Не публикуй names, usernames, email, raw onboarding, chat, voice, transcripts, UTM, payments, individual attendance или LMS progress.

Следующие P0:

1. Исправить Labs Dataflow: producer после `94e6205` пишет rolling participant files, exporter в deployed `55e52b0` читает dated files. Сделай current-date rolling reader + legacy dated fallback + stale marker + deterministic duplicate handling + `rollups.roster_summary` + schema `1.2.0`. Добавь тесты, проведи master PR → deploy PR → restart → rerun.
2. Добавить LMS `GET /api/v1/tutor/context/me?lab=ain3` с allowlist response и `no-store`.
3. Добавить retention/consent/delete/export и запрет логирования context body в Tutor.
4. Прогнать desktop 1366×768 + 1440×900, mobile 390×844, keyboard, reduced motion, console, links/assets, secret/PII scan.
5. Публиковать обычным push без force. В финале дать commit, URLs, QA receipt и оставшиеся риски.
