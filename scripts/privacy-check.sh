#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

fail=0

report_paths() {
  local label="$1"
  shift
  local matches
  matches="$(find . -path './.git' -prune -o "$@" -print | sed 's#^./##' || true)"
  if [[ -n "$matches" ]]; then
    printf 'privacy check failed: %s\n%s\n' "$label" "$matches" >&2
    fail=1
  fi
}

report_paths "private runtime/session file" \
  \( -path '*/.claude/*' -o -path '*/.codex/*' -o -path '*/.cursor/*' \
     -o -path '*/_sessions/*' -o -path '*/file-history/*' \
     -o -iname '*.jsonl' -o -iname '*.sqlite' -o -iname '*.sqlite3' \
     -o -iname '*.db' -o -iname '*.pem' -o -iname '*.key' \
     -o -name 'HANDOFF.md' -o -name 'CONTEXT-HANDOFF.md' \
     -o -name 'SESSION-*-HANDOFF.md' -o -path './ain3/handoff/*' \
     -o -name '*.backup-*' \)

content_pattern='(/Users/[A-Za-z0-9._-]+/|/home/[A-Za-z0-9._-]+/|[A-Za-z]:\\\\Users\\\\[^\\\\[:space:]]+|\.claude/(projects|file-history)|\.codex/sessions|session\.jsonl|"(sessionId|parentUuid|isSidechain|toolUseResult|transcript_path)"[[:space:]]*:|sk-or-v1-|sk-[A-Za-z0-9_-]{20,}|\.chatgpt\.site)'
if git grep -IEn "$content_pattern" -- . \
  ':(exclude)scripts/privacy-check.sh' \
  ':(exclude).github/workflows/privacy.yml'; then
  printf 'privacy check failed: private runtime, credential, or forbidden hosting marker found\n' >&2
  fail=1
fi

if command -v gitleaks >/dev/null 2>&1; then
  gitleaks git --redact --no-banner --exit-code 1 . || fail=1
else
  printf 'privacy check failed: gitleaks is required\n' >&2
  fail=1
fi

exit "$fail"
