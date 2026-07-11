# AIN3 Assistant Spec

Public deck: `ain3-intro.html`

Goal: attach a small lab-specific assistant to the AIN3 intro deck without exposing participant data, tokens, private chat exports, or raw LMS content in the browser.

## Current MVP

The deck ships with a local `AIN LIVE` overlay:

- hotkey: `V`
- source: static slide context inside `ain3-intro.html`
- behavior: gives one short speaker cue and 2-3 action chips for the active slide
- privacy: no network request, no personal participant fields

This matches the useful part of the older VOX overlay: live framing while presenting. It does not yet run a full chat agent in the browser.

## Server-Backed Shape

Recommended endpoint:

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

The isolated assistant can know:

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

Server:

- keep all tokens in env vars
- isolate index to AIN3 sources only
- log request metadata without personal payload
- apply a public-safe filter before returning text
- expose health check: `GET /ain3/assistant/health`

## Browser Rule

The current overlay already follows this rule:

```text
if localStorage["ain3-assistant-endpoint"] exists:
  ask server for a presenter cue
else:
  show local slide cue
```

That gives the deck a useful live assistant now and a clean path to a Danik/ws-danik service later.
