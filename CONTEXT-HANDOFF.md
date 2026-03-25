# Handoff — Team Workshop Presentation

## Проект
- **team-workshop.html** — `/Users/alex/Documents/_code/_decks/ainative-deck/team-workshop.html`
- **URL:** `https://ai-mindset-org.github.io/ainative-deck/team-workshop.html`
- **pos-setup-v2.html** — вчерашняя преза, 39 слайдов, задеплоена, спикеры удалены

## Сделано (15 слайдов)
- S1: Cover (4 спикера — Alex + Denis + Alexander + Sereja)
- S2: Agenda (5 блоков)
- S3: Denis Smirnov — скучные агенты
- S4: Alexander Vasiliev — лиминальное пространство
- S5: Sereja Ris — персональная корпорация
- S6: Q&A — 9 вопросов карточками
- S7: Team Stack overview
- S8: Alex Povaliaev — командный стек (8/50+/9/15K+)
- S9: Roles — 8 карточек
- S10: Skills map — 6 категорий
- S11: MCP — 9 серверов
- S12: Eval + Linear Awareness
- S13: Naming + Vault Structure
- S14: Communication Rules — 5 тонов
- S15: Dashboard — 8 блоков

## Осталось

### 1. Вставить Team Stack Explorer
**Файл:** `/Users/alex/Library/CloudStorage/Dropbox/notes/AI mindset {shared}/ai-mindset-2026/inbox/{AIM} {tool} Team Stack Explorer – 2026-03-25.html`
— добавить как iframe или взять из него визуалы/данные для слайдов

### 2. Развёрнутые Q&A слайды (после S6)
Каждый вопрос = отдельный слайд с конкретным ответом:

| Вопрос | Ответ (суть) |
|--------|-------------|
| **Harness vs база** (@antoncp) | навык orchestration не устареет. markdown portable. harness = moat |
| **Obsidian Sync на команду** (@olegpotem) | Dropbox shared + Obsidian Sync. AGENTS.md индекс. naming = машиночитаемость |
| **Claude + Codex** (@artveretevo) | один CLAUDE.md, одна .claude/skills/. settings.json раздельные |
| **Прошлые сессии** (@dmezhov) | `claude --continue`, `--resume`, episodic-memory plugin, memory/ files, /sessions |
| **CLAUDE.md как роутер** | не хранит данные, ссылается. AGENTS.md = индекс. naming = grep по паттерну |
| **По слоям** (@fshkn) | Context: Obsidian. Rules: CLAUDE.md. Skills: .claude/skills/. MCP: Calendar+Linear+TG. Связать с лекцией Gershuni |
| **4000 заметок iCloud→Obsidian** (@tonkolytko) | export .md, bulk rename, кластеризация через /research |
| **Telegram MCP** (@dmezhov) | Telethon MTProto, MCP server, чтение/отправка |
| **Другие форматы в Obsidian** (@dmezhov) | md основное, PDF/images через ссылки, _data/ для медиа |
| **Онтология контекста** (@principal_andrew) | алгоритм: dump → кластеризация → naming → AGENTS.md → iterate |

### 3. Добавить слайды про механику
- **Symlinks** — sync-team-skills.sh создаёт symlinks из team vault в .claude/skills/
- **Obsidian integration** — vault = рабочая директория Claude Code. .claude/ внутри vault
- **Obsidian Sync** — Dropbox для shared vault, Obsidian Sync для personal
- **Raycast + Obsidian** — URI protocol, quick scripts
- **Дашборд как зеркало** — больше про скиллы и конкретные примеры из блога

### 4. Больше визуалов
- Взять блоки из старой презы: `/Users/alex/Documents/_code/_decks/ainative-pos-setup/index.html`
- Добавить POS layers SVG диаграмму (есть в ainative-pos-setup S4)

## Prompt для продолжения
```
Продолжи работу над team-workshop.html. Прочитай CONTEXT-HANDOFF.md в той же папке.

1. Прочитай Team Stack Explorer HTML из vault inbox
2. Добавь Q&A слайды с развёрнутыми ответами (1 вопрос = 1 слайд)
3. Добавь слайды про symlinks, Obsidian Sync, Raycast integration
4. Больше визуалов из ainative-pos-setup/index.html
5. Задеплой на GitHub Pages
```

## Ключевые файлы
- Deck: `/Users/alex/Documents/_code/_decks/ainative-deck/team-workshop.html`
- Team Stack Explorer: `/Users/alex/Library/CloudStorage/Dropbox/notes/AI mindset {shared}/ai-mindset-2026/inbox/{AIM} {tool} Team Stack Explorer – 2026-03-25.html`
- Old deck visuals: `/Users/alex/Documents/_code/_decks/ainative-pos-setup/index.html`
- Speaker notes: `/Users/alex/Library/CloudStorage/Dropbox/notes/AI mindset {shared}/ai-mindset-2026/Labs/s2 – ai-native sprint/{AIM} {guide} POS Setup Speaker Notes – 2026-03-24.md`
- Skills sync script: `/Users/alex/Library/CloudStorage/Dropbox/notes/.claude/sync-team-skills.sh`
