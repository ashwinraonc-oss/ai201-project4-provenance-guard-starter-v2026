#!/usr/bin/env python3
"""
Criterion 4 ("the appeal path is reliable") — run by hand, not through
run_eval.py.

scenarios.py's own docstring names the gap: run_eval.py only sends to
POST /submit, and testing an appeal needs a real content_id from a
submission that already happened. Bending the shared harness to do a
submit-then-appeal round trip for exactly one criterion wasn't worth it, so
this is a small standalone script instead — same idea (3 trials... here, 5,
since that's what criterion 4 in criteria.md actually asks for), same
honesty about what came back.

    python app.py                        # in one terminal
    python scripts/eval_appeal_path.py   # in another
"""

import json
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).parent.parent
URL = "http://127.0.0.1:5000"
TRIALS = 5


def one_trial(n: int) -> dict:
    submit_body = {
        "text": f"Trial {n} of the appeal-path check. Submitting a fresh piece "
                f"each time so every content_id is genuinely new.",
        "creator_id": f"eval_appeal_{n}",
    }
    submit_resp = requests.post(f"{URL}/submit", json=submit_body, timeout=30)
    submit_json = submit_resp.json() if submit_resp.content else {}
    content_id = submit_json.get("content_id")

    if submit_resp.status_code != 200 or not content_id:
        return {
            "trial": n, "ok": False,
            "reason": f"submit itself failed: {submit_resp.status_code} {submit_json}",
        }

    appeal_body = {"content_id": content_id, "reasoning": "I wrote this myself."}
    appeal_resp = requests.post(f"{URL}/appeal", json=appeal_body, timeout=30)
    appeal_json = appeal_resp.json() if appeal_resp.content else {}

    log_resp = requests.get(f"{URL}/log?limit=20", timeout=30)
    log_entries = log_resp.json().get("entries", []) if log_resp.content else []
    matching = [e for e in log_entries if e.get("content_id") == content_id]
    appeal_entry = next((e for e in matching if e.get("event") == "appeal"), None)

    status_changed = appeal_resp.status_code == 200 and appeal_json.get("status") == "under_review"
    recorded = appeal_entry is not None and appeal_entry.get("status") == "under_review"

    return {
        "trial": n,
        "ok": status_changed and recorded,
        "content_id": content_id,
        "appeal_status_code": appeal_resp.status_code,
        "appeal_response": appeal_json,
        "found_in_log": appeal_entry,
    }


def main():
    try:
        requests.get(f"{URL}/health", timeout=5)
    except Exception:
        print(f"Nothing answering at {URL}. Start it: python app.py", file=sys.stderr)
        sys.exit(1)

    results = [one_trial(n) for n in range(1, TRIALS + 1)]
    passed = sum(1 for r in results if r["ok"])

    for r in results:
        mark = "PASS" if r["ok"] else "FAIL"
        print(f"trial {r['trial']}: {mark}  content_id={r.get('content_id')}")

    print(f"\n{passed} of {TRIALS} — status changed to under_review AND appeared in /log.")

    out = ROOT / "results" / "appeal_path_eval.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
