# AIN3 state – 2026-07-14

## Release state

- Repository: `ai-mindset-org/ainative-deck`
- Branch: `main`
- Canonical Personal Setup baseline: `93bb3b3`
- Current release: Lab Hub + 18-slide Personal Setup + public-safe Скрипка + portable handoff pack
- Intro deck: `779ed88`, 10 slides
- LMS: PR `#769`, merge `42a5473fb`, 71 tests and build passed
- LMS deploy remains open: self-hosted dev failed with `No space left on device`; production tag was not created

## Data snapshot

- Snapshot: 14.07.2026
- NocoDB: 120 rows, 112 submitted, 4 staff/test
- Rolling participant files: 118; unique non-staff handles: 114
- Submitted participant cards with chat match: 108
- Intro posts captured: 45; intro-call matches: 19
- Attendance identity records: 107; kickoff 95; intro 40; both 28
- `pre_lab_signals` task: `5733fc8fc79540978d13823690b20f66`
- Export task: `5852b406ebe4487a8169c5543d83cef2`
- Export vault commit: `80c80f60adc225ebe8deafadc0e0dbf8f67cd860`

Each count has its own denominator. `participants.length`, attendance identities and onboarding rows describe different source sets. `paid: 1` is a technical row status.

## Dataflow defect

- Commit `94e6205` switched participant artifacts to rolling filenames.
- Deployed code `55e52b0` still reads dated participant files in `modules/export/module.py` with `dated=True`.
- Refreshed artifacts exist, while export reports `pre_lab_signals: absent`.
- A direct `dated=False` reader can inflate the identity spine to about 193 through an unsafe union of attendance and profile identities.

Safe repair: current-date rolling reader, legacy dated fallback, stale-date marker, deterministic duplicate handling, additive `rollups.roster_summary`, schema `1.2.0`, tests, master PR, deploy PR, restart and rerun.

## Architecture decision

- Public Pages: aggregates, public profiles, public artifacts and synthetic examples
- Participant Tutor: self-only via LMS JWT
- Staff Скрипка: separate admin-only route, aggregate by default, purpose and audited drill-down
- Dataflow to LMS: HMAC, timestamp, IP allowlist, `aim.participant-context.v1`, payload up to 8 KB
- Human confirmation: outreach, publication and state changes

## Definition of done for the backend pass

1. Dataflow export includes the refreshed pre-lab signal module with stable denominators.
2. LMS returns an allowlisted self-context with `Cache-Control: no-store`.
3. Tutor has consent, retention, 90-day redaction, delete/export and a context-body log ban.
4. Tests prove one participant cannot access another participant’s context.
5. `/reset` handles retained analytics explicitly.
