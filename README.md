# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

Provenance Guard takes a piece of writing and tells the submitter whether it looks human-written, AI-written, or genuinely unclear — and lets them push back if they think it got it wrong. The path one submission takes, arrival to label:

1. A writer `POST`s `{"text": "...", "creator_id": "..."}` to `/submit`.
2. The route pulls `text` and `creator_id` out of the body and mints a `content_id` (a UUID) — this id is the thread that ties the decision, the log entry, and any later appeal together.
3. **Signal one** (`detector.model_signal`) runs a small language model (GPT-2) on the text locally and measures how *predictable* it is (perplexity), squashed to a 0–1 `model_score` where higher means more AI-like.
4. **Signal two** (`stylometry.style_signal`) measures the text's shape — sentence-length variety, vocabulary repetition, punctuation density — with no idea what the words mean, into its own 0–1 `style_score`.
5. `scoring.combine_signals` turns those two numbers into one `combined_score`, deciding what happens when they disagree.
6. `scoring.score_to_label` turns that single number into a `guess` (`human` / `unsure` / `ai`) and a full sentence a reader actually sees — not a confidence number.
7. `audit.log_decision` writes every field of that decision to `logs/audit.jsonl` before the response goes out, and the response itself carries the `content_id`, the guess, the label, and both signal scores. If the writer disagrees, `POST /appeal` with that `content_id` moves the entry to `under_review` and records their reasoning next to the original decision — it doesn't re-score anything automatically.



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** perplexity — how surprised a local GPT-2 model is by the text's actual sequence of words, i.e. how predictable the text is to a model that's just trying to guess the next token. Turned into a 0–1 score where higher means more AI-like.

**Why that might differ between human and AI writing:** a language model writes by repeatedly picking a likely next word, so text it produced tends to be text it (or a similar model) also finds easy to predict. Human writing wanders more — odd word choices, abrupt turns, the specific rather than the typical — which reads as higher perplexity.

**What it can't see:** who wrote it. It measures predictability, not authorship, and those aren't the same thing. It rewards common words in short, ordinary sentences regardless of who's writing them — someone writing in a second language and staying with vocabulary they're sure of, a younger writer, anyone writing plainly on purpose all score about as machine-like as machine writing does. It runs backwards on dense, ornate human prose too: rare words are exactly what trip the model up, so formal or unusual human writing often reads as *more* human on this signal than it deserves to. The writers this signal is most likely to accuse are the ones with the least room to argue back — that's structural, not a bug I can tune away.

### Signal two — the style signal

**What it measures:** the text's shape, not its meaning — how much sentence length varies, how much the vocabulary repeats (unique words over total words), and how dense and varied the punctuation is.

**Why that might differ between human and AI writing:** "most likely next word," applied over and over, tends to produce even, mid-length sentences and a narrower vocabulary band on average. Human writing is lumpier on purpose and by accident — a three-word sentence next to a forty-word one, a vocabulary that drifts, punctuation habits that are specific to one writer.

**What it can't see:** the text at all, semantically. It has no idea what the words mean, so anything that changes the *shape* without changing the *substance* moves the score — adding typos, breaking one long sentence into three short ones, pasting in a block quotation with a different rhythm than the surrounding prose. All of that is cheap to do on purpose, which is exactly what next unit's attack set is built to exploit.

### The combining rule

**The rule:** start with a weighted average. Then check how far apart the two signals are — if they disagree by more than 0.35, don't let that just average out to "unsure" by coincidence: pull the result halfway toward whichever of the two signals reads *more human*. When the evidence disagrees, I'd rather undercount an AI submission than overcount a human one — criterion 1 says a wrong accusation costs more than a missed detection, and there's no version of this rule that avoids that trade entirely, only a choice of which way to lean when it comes up.

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.6`, `WEIGHT_STYLE_SIGNAL = 0.4`, disagreement threshold `0.35` — all in `config.py`. Model signal counts for a bit more because it's the one that's actually tried to read the text; style is pure shape and cheaper to game on purpose. Neither is weighted heavily, because both have a documented, structural blind spot, and leaning hard on one is exactly how a blind spot becomes a wrong accusation.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** a paragraph of otherwise generic, predictable prose, written with heavy em dashes, a semicolon, and short-long-short sentence variety — mimicking a known real tendency of LLMs to overuse exactly that kind of punctuation even in formulaic text. ("The results were clear — remarkably so. Users reported satisfaction; engagement metrics improved across the board. It's worth noting, however, that further testing — ideally over a longer period — would help confirm these initial findings. The team is optimistic. Cautiously so.")

- `model_score` = 0.5221 (dead center — genuinely unsure)
- `style_score` = 0.0256 (confidently human — the dashes and variety read as a distinctive personal style, not as AI mimicking one)
- A plain weighted average would land at 0.3235. The disagreement rule instead pulls it to **0.1746** — solidly human — because the two signals split by more than the 0.35 threshold (0.4965 apart) and the rule explicitly favors the more-human reading when that happens.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | "We think this was probably written by a person." |
| unsure | 0.35 – 0.65 | "Our signals don't agree clearly either way on this one. We're not saying this looks like AI — we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so." |
| high-confidence AI | 0.65 – 1.00 | "Our signals suggest this was likely written, or heavily assisted, by an AI tool rather than by a person. If that's not right, please appeal — tell us what happened and we'll have a person look at it." |

All three confirmed reachable with real submissions, not just by inspecting `scoring.label_ranges()`: a generic AI-sounding paragraph landed `ai` (0.77), a casually-written personal paragraph landed `human` (0.16), and a plain quarterly-update paragraph landed `unsure` (0.51, both signals genuinely split down the middle rather than agreeing).

**Why I worded the "unsure" one this way:** the honest version of "unsure" is "our tools couldn't tell," not "this looks suspicious." I deliberately put the uncertainty on the system ("that's on us, not you") rather than on the writer, and explicitly said doing nothing is fine — because the person reading this may well have written every single word themselves, and a label that reads as a soft accusation would make them defend something they didn't do. The `ai` label still names what it is (a suggestion, not a verdict) and points straight at the appeal path, for the same reason: it's the one message that lands on someone who, more likely than not given criterion 1's own numbers, is telling the truth when they push back.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Our team completed the migration ahead of schedule this week, and early feedback from users has been largely positive. A few minor bugs surfaced; we are addressing them in the next release cycle.", "creator_id": "sample_writer"}'
```

```json
{
  "content_id": "176e47aa-5eba-4b2a-82d4-23b462e090bc",
  "guess": "unsure",
  "confidence": 0.24,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI — we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "model_score": 0.6737,
  "style_score": 0.2542
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "176e47aa-5eba-4b2a-82d4-23b462e090bc", "reasoning": "This is my own weekly status update, written by me, no AI tools used."}'
```

```json
{
  "ok": true,
  "content_id": "176e47aa-5eba-4b2a-82d4-23b462e090bc",
  "status": "under_review",
  "message": "Your appeal has been recorded. A person will review this decision — no automatic re-checking happens."
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "timestamp": "2026-11-03T22:26:27+00:00",
      "content_id": "176e47aa-5eba-4b2a-82d4-23b462e090bc",
      "creator_id": "sample_writer",
      "guess": "unsure",
      "model_score": 0.6737,
      "style_score": 0.2542,
      "combined_score": 0.38,
      "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI — we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
      "status": "decided"
    },
    {
      "timestamp": "2026-11-03T22:26:33+00:00",
      "content_id": "176e47aa-5eba-4b2a-82d4-23b462e090bc",
      "creator_id": "sample_writer",
      "event": "appeal",
      "status": "under_review",
      "reasoning": "This is my own weekly status update, written by me, no AI tools used."
    }
  ]
}
```

The original `decided` entry stays exactly where it was — the appeal is a second, later entry for the same `content_id`, not an edit to the first. That's the audit log doing its job: anyone reading it back can see what was decided, that it was challenged, and in what order.

---

## How I Used AI

**Moment 1**

- *What I asked for:* before writing `combine_signals`, I asked Claude to actually run both signals over the same three test pieces and find a case where they split, rather than designing the combining rule from the docstrings alone.
- *What came back:* the three obvious pieces (clearly AI, clearly human, plain human) all had both signals agreeing. Finding a real split meant deliberately constructing a paragraph that mimics a known real LLM tic — overusing em dashes and semicolons even in otherwise generic, predictable prose. That piece scored `model_score` 0.52 (dead center) against `style_score` 0.03 (confidently human) — a 0.50 gap.
- *What I changed:* a plain weighted average would have landed that case at 0.32 — already "human," by luck. I added the explicit disagreement rule (pull toward the more-human signal when the two split by more than 0.35) specifically because I wanted that case to land there *by design*, not by whatever the weights happened to produce, and because criterion 1 says that's the direction I should be wrong in when the evidence disagrees.

**Moment 2**

- *What I asked for:* Milestone 4's four calibration inputs explicitly include "plain conventional human writing," not just the easy clearly-AI/clearly-human ends. I asked for that one to be tested for real rather than assumed to be fine.
- *What came back:* a four-sentence, plainly-written paragraph about walking to the store scored `combined_score` 0.69 — solidly in the `ai` band. Both signals contributed: low vocabulary variety and short, even sentences read as AI-like on signal two, and a predictable, common-word paragraph reads as AI-like on signal one, exactly as both files' own docstrings warned.
- *What I changed:* nothing in the code — this is the real version of the false positive Milestone 1 asked me to trace on paper, now showing up in my own numbers on my first real test rather than staying hypothetical. I didn't retune the thresholds to make this one example pass, because that would be fitting the system to a single input rather than fixing the underlying blind spot. I wrote it up honestly here and flagged it as the concrete evidence criterion 1 will actually be measured against next unit.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
