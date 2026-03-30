# Handoff: ainative-deck Session 2026-03-20

## Current State
- **Repo:** ai-mindset-org/ainative-deck (GitHub Pages live)
- **Gershuni W1:** `decks/gershuni-w1/index.html` — 87 slides, PPTX v2 synced
- **Intro Call:** `intro-call.html` — 30 slides, full redesign done
- **Last commit:** OG covers + Vox fix + AI gen fix + edit mode fix

## What Works
- E = edit mode (draggable fix applied)
- T = TOC / presenter notes
- V = Vox bot (lab context loaded)
- AI = SVG diagram + Imagen 4 (OpenRouter key updated)
- push = GitHub API save
- OG covers for social preview

## Next Tasks (from user's last message)

### 1. Vox Bot as "Oksi" Character
- Vox should be a persistent AI character ("Oksi") that:
  - Knows full lab context (all sessions, speakers, history)
  - Suggests talking points during presentation
  - Can pull context from Saturday sessions and bot chat history
  - Appears as a floating character, toggleable by button
  - Generates live content from lab data

### 2. Live Generators
- SVG metaphor generators that work in real-time
- Image generation integrated into slide creation flow

### 3. OpenSpec Specification
- Create `/openspec/changes/ainative-deck-vox/` with:
  - proposal.md — Oksi character + live generators
  - design.md — architecture
  - tasks.md — implementation checklist

### 4. Multi-agent Implementation
- Use agent team / tmux mode for parallel work

## Key Files
- Lab structure: `/tmp/lab-structure.md`
- SKU data: `/tmp/sku-data.md`
- PPTX v2 summary: `/tmp/pptx-v2-summary.md`
- Text verification: `/tmp/text-verification.md`
- OpenRouter key: stored in localStorage ('ainative-or-key') — enter at runtime

## Prompt for Next Session
```
Продолжи ainative-deck. Прочитай HANDOFF.md.

1. Создай OpenSpec спецификацию для "Oksi" — AI-персонаж в презентации
2. Реализуй в мультиагентном режиме
3. Добавь live SVG генераторы
4. Интегрируй контекст лабы (сессии, чат-бот, Saturday sessions)
5. Деплой на GitHub Pages
```
