# AIN3 Assistant Spec

Public deck: `ain3-intro.html`

Goal: attach lab-specific assistants to AIN3 surfaces without exposing participant data, tokens, private chat exports, or raw LMS content in the browser.

## Product split

- **Tutor** – participant-facing in LMS, authenticated by JWT and limited to the current participant.
- **Скрипка** – staff-facing progress agent, aggregate by default with audited drill-down.
- **Public demo** – static/synthetic fallback in GitHub Pages; never calls private services by default.

## Current MVP

The Intro deck ships with a local `Tutor` overlay. Personal Setup ships with a public-safe `Скрипка` fallback:

- hotkey: `V`
- source: static slide context inside each deck
- behavior: gives one short cue or artifact-specific answer for the active slide
- privacy: no network request by default, no personal participant fields
- optional endpoint: configured locally in `localStorage`; every request sends `slideId`, `question`, `mode`, `publicOnly: true` and `synthetic: true`

This keeps the useful part of the older VOX overlay: live framing while presenting. Full participant context stays inside the authenticated LMS Tutor.

## Server-Backed Shape

Recommended public presenter endpoint:

```http
POST /ain3/assistant/ask
```

Request:

```json
{
  "slideId": "speakers",
  "question": "what should I say here?",
  "mode": "presenter-cue",
  "publicOnly": true
}
```

Response:

```json
{
  "answer": "Talk about each speaker as a lens, not a biography.",
  "sources": ["deck", "lms_public", "program_plan"],
  "risk": "public-safe"
}
```

## Knowledge Scope

The public assistant can know:

- this GitHub deck repo and commit history
- AIN3 public deck structure
- weekly plan and public schedule
- speaker and curator public cards
- LMS public hub structure
- dataflow aggregates from `Labs/22 – ain3/_artifacts/participants`
- transcript summaries that have been explicitly marked public-safe

It must not return:

- participant emails, handles, phone numbers, private onboarding answers
- raw Telegram dumps
- private LMS transcripts
- auth tokens or server secrets
- GitHub publish tokens

## Integration Contract

Browser:

- keep `ain3-assistant-endpoint` in `localStorage`
- send `slideId`, `question`, and `publicOnly: true`
- render answer as a short presenter cue
- fall back to local static cues when endpoint is missing or down
- do not ask for or store an LLM provider key in the public deck

Server:

- keep all tokens in env vars
- isolate index to AIN3 sources only
- log request metadata without personal payload
- apply a public-safe filter before returning text
- expose health check: `GET /ain3/assistant/health`

Participant self-context and staff progress tracking are defined separately in [`ain3/agents/privacy-contract.md`](ain3/agents/privacy-contract.md).

## Browser Rule

The current overlay already follows this rule:

```text
if localStorage["ain3-assistant-endpoint"] exists:
  ask server for a presenter cue
else:
  show local slide cue
```

That gives the deck a useful live assistant now and a clean path to a Danik/ws-danik service later.
