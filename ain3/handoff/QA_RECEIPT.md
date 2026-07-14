# QA receipt

Status: local release candidate passed; GitHub Pages smoke pending first release commit.

## Viewports

| Surface | Viewport | Result |
|---|---:|---|
| Lab Hub | 1366×768 | pass; horizontal overflow 0 |
| Lab Hub | 1440×900 | pass; horizontal overflow 0; 22/22 images loaded |
| Lab Hub | 390×844 | pass; document and body width 390 |
| Personal Setup | 1366×768 | 18/18; horizontal overflow 0 |
| Personal Setup | 1440×900 | 18/18; horizontal overflow 0 |
| Personal Setup | 390×844 | 18/18; horizontal overflow 0 |

Slides 6, 8, 10, 11 and 15 use intentional `overflow-y:auto` on mobile. Slides 17 and 18 fit 390×844 without vertical clipping.

## Interaction

- Hub synthetic controls: `next`, `state`, `sources` pass.
- Personal Setup local Скрипка answer: pass.
- Keyboard: `V`, `Esc`, `ArrowLeft`, `ArrowRight` pass.
- Direct fresh hash routes `#17` and `#18`: pass.
- Reduced motion: media query matches; slide and scout animation duration `1e-06s`.

## Static and privacy

- JS syntax: pass for Hub and Personal Setup.
- JSON: `manifest.json` and `functions.json` pass.
- Internal local routes: Hub, Intro, Personal Setup, Process M1, Focus W2 and manifest return 200.
- Console errors: 0.
- Broken loaded images: 0.
- OpenRouter code: absent from Personal Setup production path.
- Public session map excludes exact IDs and local paths.
- Secret pattern scan: 0 findings.
- Participant PII scan: 0 published identities or raw records.
- `git diff --check`: pass.

Local preview calls the optional save-server only on `127.0.0.1` or `localhost`. Public hostname behavior and request log are verified after Pages deployment.
