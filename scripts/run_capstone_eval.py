#!/usr/bin/env python3
"""
The capstone's own test harness. ← Milestone 5. Not run_eval.py.

Nobody handed this unit a test set, and run_eval.py's scenarios.py format
doesn't cleanly fit what these five criteria actually need to check (a
guess of "unscorable", a latency bound, a count of false triggers) — same
situation unit 8's appeal-path criterion was in, and the same answer: a
small standalone script, same idea (3 trials, real output saved), built
for exactly what this unit's criteria ask.

    python app.py                             # in one terminal
    python scripts/run_capstone_eval.py        # in another
    python scripts/run_capstone_eval.py --label before
    python scripts/run_capstone_eval.py --label after
"""

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).parent.parent
URL = "http://127.0.0.1:5000"
TRIALS = 3

# ─── Criterion 1 & 3's inputs: real, ordinary non-Latin-script sentences ────
NON_LATIN_SENTENCES = [
    ("ar1", "هذا نص باللغة العربية لاختبار كيفية تعامل النظام مع النصوص التي لا تستخدم الأبجدية اللاتينية على الإطلاق."),
    ("ar2", "ذهبت إلى السوق هذا الصباح لشراء الخضروات والفواكه الطازجة للعشاء."),
    ("ar3", "الطقس جميل اليوم وقررت أن أمشي إلى العمل بدلاً من ركوب الحافلة."),
    ("ar4", "قرأت كتابًا مثيرًا للاهتمام الأسبوع الماضي وأنا أفكر في قراءته مرة أخرى."),
    ("ru1", "Это обычное предложение на русском языке для проверки системы."),
    ("ru2", "Я сходил в магазин утром и купил хлеб и молоко на завтрак."),
    ("ru3", "Погода сегодня хорошая, и я решил прогуляться в парке после обеда."),
    ("el1", "Αυτή είναι μια συνηθισμένη πρόταση στα ελληνικά για τον έλεγχο του συστήματος."),
    ("el2", "Πήγα στην αγορά σήμερα το πρωί για να αγοράσω φρέσκα λαχανικά."),
    ("el3", "Ο καιρός είναι ωραίος σήμερα και αποφάσισα να περπατήσω στο πάρκο."),
]

# ─── Criterion 2 & 5's inputs: 20 real English texts, Latin-script, nothing
# constructed for this unit. The first 8 are the real false_positive family
# from unit 8's attack set (results/attack_run_*.md); the next 10 are the
# plain-writing set from scenarios.py (unit 8, criterion 1 — disclosed there
# as placeholder text for THAT criterion's purpose, authorship detection;
# reused here for a different question entirely, whether they're Latin
# script, which they plainly are regardless of who wrote them). The last 2
# are unit 7's own AI/human calibration texts, for the same reason.
ENGLISH_TEXTS = [
    ("FP01", "We got to the campsite about four. The pitch was fine, a bit sloped, but there was a tap nearby and the toilets were clean enough. Putting the tent up took longer than it should have because I had forgotten how the poles went. The weather held until Saturday night. Then it rained hard and kept raining. We stayed in the tent and played cards and ate most of the food we had brought for Sunday. On Sunday we packed up wet and drove home early. It was not the weekend we planned but the kids enjoyed it and we would go back."),
    ("FP02", "This report sets out the findings of the working group. The group met four times between January and March. Its remit was to review the current arrangements and to recommend changes where these were warranted. The group found that the existing arrangements are broadly sound. Three areas were identified where improvement is possible. These are set out in section four, together with an indicative timetable. The group recommends that the committee adopt the proposals in full."),
    ("FP03", "I want to describe my experience of the first month in this country. The weather was very different from my home. I did not expect the rain to continue for so many days. My colleagues were kind and they helped me to find an apartment. I am still learning the words that people use in the office. Sometimes I do not understand the jokes. But I am happy that I came here and I think it was a good decision for my family."),
    ("FP04", "There are three main causes of the conflict. The first cause is economic. Trade between the two regions had declined significantly in the preceding decade. The second cause is political. Neither government was able to control its own border provinces effectively. The third cause is social. Population movements had created communities on both sides with divided loyalties. In conclusion, the conflict cannot be explained by any single factor."),
    ("FP05", "To configure the service, edit the settings file in the installation directory. Set the host value to the address the service should bind to. Set the port value to an unused port above 1024. Save the file and restart the service. The service will log its startup configuration. If the port is already in use, the service will exit with an error. Check the log file for details before retrying."),
    ("FP06", "Dear Sir or Madam, I am writing to enquire about the position advertised on your website. I have five years of relevant experience and I believe I would be a strong fit for the role. I have attached my curriculum vitae for your consideration. I am available for interview at your convenience. Thank you for your time. I look forward to hearing from you."),
    ("FP07", "It rained on Monday. It rained on Tuesday. It rained on Wednesday and it rained on Thursday and by Friday I had stopped looking out of the window altogether. The forecast said it would clear. The forecast said that on Monday, and on Tuesday, and on Wednesday. I have stopped believing the forecast. I have started believing the window."),
    ("FP08", "Went for a run. Legs hurt. Worth it."),
    ("plain01", "I made coffee this morning and forgot to drink it until it was cold."),
    ("plain02", "My neighbor's dog got loose again. I helped chase it down the block."),
    ("plain03", "I still haven't replied to that email. I keep meaning to."),
    ("plain04", "Rained most of the day. I stayed in and read on the couch."),
    ("plain05", "I burned the toast twice before giving up and eating cereal instead."),
    ("plain06", "My sister called while I was driving. I called her back an hour later."),
    ("plain07", "I lost my keys again. Found them in the fridge, somehow."),
    ("plain08", "The bus was late so I walked the rest of the way. Wasn't too bad."),
    ("plain09", "I tried a new recipe tonight. It was fine, not great. I'd make it again."),
    ("plain10", "Spent an hour looking for my glasses. They were on my head the whole time."),
    ("calib_ai", "The implementation of the proposed framework requires careful consideration of several key factors. It is important to note that the system must be able to handle a wide variety of inputs. Additionally, the overall performance of the solution depends on several important variables."),
    ("calib_human", "Honestly? I almost didn't submit this. Spent three hours yesterday rewriting the intro — twice — and still hate it; my advisor will probably hate it more. Whatever. It's done."),
]

# ─── Criterion 4's inputs: constructed edge cases, 1-4 non-Latin letters ────
SHORT_NON_LATIN = [
    ("edge01", "Я!"),
    ("edge02", "42 ع"),
    ("edge03", "α?"),
    ("edge04", "Ω Ω"),
    ("edge05", "ع3"),
    ("edge06", "🙂 Я"),
    ("edge07", "... ب"),
    ("edge08", "Ωγ"),
    ("edge09", "7 д!"),
    ("edge10", "λ λ"),
]


def submit(creator_id: str, text: str, timeout: float = 30.0) -> dict:
    try:
        resp = requests.post(f"{URL}/submit", json={"text": text, "creator_id": creator_id},
                             timeout=timeout)
    except Exception as exc:  # noqa: BLE001
        return {"status": None, "error": f"{type(exc).__name__}: {exc}"}
    try:
        body = resp.json()
    except ValueError:
        body = None
    return {"status": resp.status_code, "body": body}


def run_criterion_1(trial: int) -> dict:
    """10 of 10 non-Latin sentences -> guess unscorable, status unscored."""
    results = []
    for n, (sid, text) in enumerate(NON_LATIN_SENTENCES, 1):
        r = submit(f"capstone_c1_t{trial}_{sid}", text)
        body = r.get("body") or {}
        ok = r["status"] == 200 and body.get("guess") == "unscorable"
        results.append({"id": sid, "status": r["status"], "guess": body.get("guess"), "ok": ok})
    hit = sum(1 for x in results if x["ok"])
    return {"trial": trial, "hit": hit, "of": len(results), "results": results}


def run_criterion_2(trial: int) -> dict:
    """0 of 20 real English texts -> falsely gated."""
    results = []
    for sid, text in ENGLISH_TEXTS:
        r = submit(f"capstone_c2_t{trial}_{sid}", text)
        body = r.get("body") or {}
        false_trigger = r["status"] == 200 and body.get("guess") == "unscorable"
        results.append({"id": sid, "status": r["status"], "guess": body.get("guess"),
                        "false_trigger": false_trigger, "duration_ms": None})
    triggers = sum(1 for x in results if x["false_trigger"])
    return {"trial": trial, "false_triggers": triggers, "of": len(results), "results": results}


def run_criterion_3(trial: int) -> dict:
    """Every gated submission completes in under 5ms (from the audit log)."""
    results = []
    for n, (sid, text) in enumerate(NON_LATIN_SENTENCES, 1):
        r = submit(f"capstone_c3_t{trial}_{sid}", text)
        body = r.get("body") or {}
        content_id = body.get("content_id")
        duration_ms = _lookup_duration(content_id) if content_id else None
        ok = duration_ms is not None and duration_ms < 5.0
        results.append({"id": sid, "duration_ms": duration_ms, "ok": ok})
    hit = sum(1 for x in results if x["ok"])
    return {"trial": trial, "hit": hit, "of": len(results), "results": results}


def run_criterion_4(trial: int) -> dict:
    """10 of 10 short non-Latin edge cases fall through to normal scoring, no 500."""
    results = []
    for sid, text in SHORT_NON_LATIN:
        r = submit(f"capstone_c4_t{trial}_{sid}", text)
        body = r.get("body") or {}
        crashed = r["status"] == 500
        gated = r["status"] == 200 and body.get("guess") == "unscorable"
        # "Falls through safely" = not gated AND not a 500. It may still be
        # a 400 (too short for signal one, say) -- that's an existing,
        # already-covered failure mode, not this criterion's concern.
        ok = (not crashed) and (not gated)
        results.append({"id": sid, "status": r["status"], "guess": body.get("guess"),
                        "crashed": crashed, "gated": gated, "ok": ok})
    hit = sum(1 for x in results if x["ok"])
    return {"trial": trial, "hit": hit, "of": len(results), "results": results}


def run_criterion_5(trial: int) -> dict:
    """At least 18 of 20 real English submissions score in under 100ms."""
    results = []
    for sid, text in ENGLISH_TEXTS:
        r = submit(f"capstone_c5_t{trial}_{sid}", text)
        body = r.get("body") or {}
        content_id = body.get("content_id")
        duration_ms = _lookup_duration(content_id) if content_id else None
        ok = duration_ms is not None and duration_ms < 100.0
        results.append({"id": sid, "duration_ms": duration_ms, "ok": ok})
    hit = sum(1 for x in results if x["ok"])
    return {"trial": trial, "hit": hit, "of": len(results), "results": results}


def _lookup_duration(content_id: str):
    try:
        resp = requests.get(f"{URL}/log?limit=400", timeout=10)
        entries = resp.json().get("entries", [])
    except Exception:  # noqa: BLE001
        return None
    for e in reversed(entries):
        if e.get("content_id") == content_id:
            return e.get("duration_ms")
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", default="")
    args = parser.parse_args()

    try:
        requests.get(f"{URL}/health", timeout=5)
    except Exception:
        print(f"Nothing answering at {URL}. Start it: python app.py", file=sys.stderr)
        sys.exit(1)

    all_results = {1: [], 2: [], 3: [], 4: [], 5: []}
    for trial in range(1, TRIALS + 1):
        print(f"\n=== trial {trial} ===")
        r1 = run_criterion_1(trial); all_results[1].append(r1)
        print(f"  criterion 1 (non-Latin -> unscorable):     {r1['hit']}/{r1['of']}")
        r2 = run_criterion_2(trial); all_results[2].append(r2)
        print(f"  criterion 2 (English false triggers):      {r2['false_triggers']}/{r2['of']} triggered")
        r3 = run_criterion_3(trial); all_results[3].append(r3)
        print(f"  criterion 3 (gate under 5ms):               {r3['hit']}/{r3['of']}")
        r4 = run_criterion_4(trial); all_results[4].append(r4)
        print(f"  criterion 4 (short non-Latin falls through): {r4['hit']}/{r4['of']}")
        r5 = run_criterion_5(trial); all_results[5].append(r5)
        print(f"  criterion 5 (scoring under 100ms):          {r5['hit']}/{r5['of']}")

    config_dir = ROOT / "results"
    config_dir.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    out = config_dir / f"capstone_eval_{stamp}{label}.json"
    out.write_text(json.dumps(all_results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
