# AIN3 Intro Deck Pipeline

Public deck: `ain3-intro.html`

This file documents the repeatable deck-kit pattern for AI Mindset lab intros. It is intentionally public-safe: no personal participant fields, no private contacts, no tokens.

## Sources

1. `Labs/22 – ain3/` in the team vault:
   - weekly plan
   - speakers CRM
   - curators CRM
   - chat navigation
   - dataflow artifacts
2. LMS public hub:
   - `learn.aimindset.org/ain3`
   - participant content is behind Telegram auth
3. Deck repo assets:
   - `logo.png`
   - `speakers/`
   - `curators/`
4. Previous deck references:
   - `intro-call.html`
   - local intelligence-style decks

## Regeneration Flow

1. Refresh participant layer with `/AIM-labs-dataflow ain3 participants`.
2. Read the newest AIN3 roster/context artifacts.
3. Keep only public-safe aggregates:
   - cohort size
   - onboarding count
   - visible chat count
   - route signals
   - repeated process themes
4. Read weekly plan and turn it into timeline blocks.
5. Read speaker/curator CRM and map people to photo assets.
6. Render the deck as a single public HTML file.
7. Run browser QA:
   - slide count
   - image load
   - console errors
   - overflow
   - editor hidden by default
   - `E` opens edit mode
   - EN/RU editor toggle works
8. Commit and push to GitHub Pages.

## Deck Blocks

The current intro format uses these blocks:

- cover with logo rail
- cohort map
- route map
- W0 intro call
- Monday kickoff
- program spine
- live-session timeline
- speaker stickers
- curator stickers
- LMS hub
- participant brief
- lightweight `AIN LIVE` assistant overlay

## Editor

Keyboard:

- `E` toggles edit mode
- `V` toggles the AIN LIVE context overlay
- `S` saves to localStorage
- `P` publishes through GitHub Contents API
- arrow keys navigate slides
- `Esc` exits edit mode and closes panels

Runtime storage:

- deck state: `ain3-intro-live-assistant-v5-state`
- history: `ain3-intro-live-assistant-v5-history`
- UI language: `ain3-intro-ui-lang`
- GitHub token: `ainative-deck-gh-token`
- optional assistant endpoint: `ain3-assistant-endpoint`

GitHub tokens stay in browser localStorage only. Never hardcode or paste them into repo files, chat, screenshots, or notes.

## Live Assistant

`ain3-intro.html` includes a lightweight local `AIN LIVE` overlay. It reads the current slide id and shows a short speaker cue. This is intentionally local-first and has no token, participant data, or network calls by default.

For a server-backed isolated assistant, use `AIN3_ASSISTANT_SPEC.md`:

- the browser stores only the endpoint URL
- secrets live on the server
- participant fields remain private
- public deck answers use aggregates, timeline, speakers, curators, LMS, and repo history

## Multigen Pattern

Use four independent lanes, then merge into one public deck:

| Lane | Output |
| --- | --- |
| Data | public-safe cohort stats and routing signals |
| People | speaker and curator stickers with correct photos |
| Program | weekly spine and live-session timeline |
| Publish | editor, QA, commit, Pages smoke test |

The deck can become a future skill by wrapping these lanes as:

```text
/AIM-deck-ainative ain3 intro
  sources: vault + LMS + deck assets
  outputs: ain3-intro.html + QA report + optional Telegram summary
```
