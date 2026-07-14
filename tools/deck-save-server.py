#!/usr/bin/env python3
"""deck-save-server — two-target persistence for editable AIN3 decks.

realtime  : POST /realtime  {deckId, edits}  -> writes <deck>/edits.json instantly (live overlay)
history   : POST /commit     {deckId, html, edits, msg} -> writes files + git commit + push
overlay   : GET  /overlay?deckId=...          -> latest edits.json (deck applies on load)
health    : GET  /health

Runs against the clean worktree so git history stays real. CORS-open (presenter's own machine).
Port 49666. Start:  python3 tools/deck-save-server.py &
"""
import json, os, re, subprocess, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # worktree root
PORT = int(os.environ.get("DECK_SAVE_PORT", "49666"))
SAFE = re.compile(r"^[a-z0-9][a-z0-9\-]{2,60}$")  # deckId whitelist


def deck_dir(deck_id):
    if not SAFE.match(deck_id or ""):
        raise ValueError("bad deckId")
    d = os.path.join(ROOT, "decks", deck_id)
    if not os.path.isdir(d):
        raise ValueError("no such deck")
    return d


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        pass

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _send(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/health":
            return self._send(200, {"ok": True, "root": ROOT, "port": PORT})
        if u.path == "/overlay":
            try:
                deck = parse_qs(u.query).get("deckId", [""])[0]
                p = os.path.join(deck_dir(deck), "edits.json")
                data = json.load(open(p)) if os.path.exists(p) else {}
                return self._send(200, {"ok": True, "edits": data})
            except Exception as e:
                return self._send(400, {"ok": False, "error": str(e)})
        return self._send(404, {"ok": False, "error": "not found"})

    def _body(self):
        n = int(self.headers.get("Content-Length", "0"))
        return json.loads(self.rfile.read(n) or b"{}")

    def do_POST(self):
        u = urlparse(self.path)
        try:
            payload = self._body()
            deck = payload.get("deckId", "")
            d = deck_dir(deck)
        except Exception as e:
            return self._send(400, {"ok": False, "error": str(e)})

        if u.path == "/realtime":
            # instant, no git — live overlay for the presenter's session
            edits = payload.get("edits", {})
            json.dump(edits, open(os.path.join(d, "edits.json"), "w"), ensure_ascii=False, indent=0)
            return self._send(200, {"ok": True, "saved": len(edits)})

        if u.path == "/commit":
            # durable: write html + edits.json, then git commit + push (history edit)
            html = payload.get("html")
            edits = payload.get("edits", {})
            msg = payload.get("msg") or f"deck edit: {deck}"
            if html:
                open(os.path.join(d, "index.html"), "w").write(html)
            json.dump(edits, open(os.path.join(d, "edits.json"), "w"), ensure_ascii=False, indent=0)
            git("add", os.path.join("decks", deck))
            c = git("commit", "-m", msg,
                    "-m", "Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>")
            p = git("push", "origin", "main")
            ok = p.returncode == 0
            return self._send(200 if ok else 500, {
                "ok": ok,
                "commit": c.stdout.strip()[-200:] or c.stderr.strip()[-200:],
                "push": (p.stdout + p.stderr).strip()[-200:],
            })

        return self._send(404, {"ok": False, "error": "not found"})


if __name__ == "__main__":
    print(f"deck-save-server on :{PORT} root={ROOT}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
