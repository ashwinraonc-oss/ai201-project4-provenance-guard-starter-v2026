# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives on plain human writing

Of 10 short (3–5 sentence) pieces of plain, ordinary writing that I compose myself — common words, short sentences, no attempt to sound formal — at most 2 are labelled high-confidence AI, holding across 3 trials.

**Why this target:** this is the exact blind spot signal one names in its own docstring: it rewards common words in short sentences regardless of who wrote them, so plain writers are the ones most likely to get falsely accused. On a writing site, a wrong accusation costs the writer far more than a missed detection costs the site, so I'm deliberately not treating the two error types as equally bad. I picked 2 of 10 rather than 0 or 1 because the blind spot is structural, not a bug I can fully tune away — a target of 0 would be a number I'm certain to miss for a reason that has nothing to do with my code being wrong, which teaches me nothing. 2 of 10 is a real bar I have to actually defend against with my combining rule and thresholds, not a number chosen to be impossible to fail by design.

---

## 2. Score spread between the obvious cases

A clearly AI-generated paragraph and a clearly human, casually-written paragraph score at least 0.40 apart on the combined 0–1 score, holding across 3 trials.

**Why this target:** 0.40 is close to half the available range. If the system can't put real daylight between the two *easy* cases, the harder calibration cases (plain human writing, lightly-edited AI) don't matter yet — there's nothing to protect against misclassifying if the signal barely discriminates at the extremes in the first place. This has to come before criteria 1 and 5 can mean anything.

---

## 3. Every label is reachable

Each of the three labels — `human`, `unsure`, `ai` — is produced by at least one real submission I construct myself, in every one of 3 trials.

**Why this target:** `config.py`'s own comments flag a real, specific way this can silently fail: a weighted average can only land between its two inputs, so while one signal is still a stub returning a constant, an entire label can become mathematically unreachable no matter what text anyone submits. This isn't a hypothetical edge case for this project — it's a documented risk in the exact code I'm about to write — so I'm holding myself to proving all three labels actually exist, not assuming they do because the thresholds look reasonable on paper.

---

## 4. The appeal path is reliable

A `/appeal` call with a valid `content_id` changes that entry's status to `under_review` and shows up in `GET /log` with the new status, in 3 of 3 trials (100%).

**Why this target:** unlike the two signals, this is plain application logic with no model call and no reason to vary run to run — find the entry, change its status, write it, confirm it. There's no legitimate reason for this to work sometimes and not others, so 100% is the right bar, not a generous one. This is the one thing standing between a wrong accusation and nothing at all, so it failing silently even occasionally would be worse than most other misses in this project.

---

## 5. Bad input never crashes the service

Submitting `text` that's missing, an empty string, or over 5,000 words never returns a `500` — each case gets a clear `4xx` response naming what's wrong, in 3 of 3 trials.

**Why this target:** `app.py`'s own docstring names a crash on malformed input as one of the most common real failures a service like this has. It's also not just a robustness nicety here: a writer who pastes in something a little unusual — too short, a huge document, a copy-paste glitch that drops the text field — is a real person who deserves a message telling them what to fix, not a stack trace that looks like the whole service is broken. 100% because, like criterion 4, this is deterministic code with no model variance involved — missing it even once means the handler has a real bug, not bad luck.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
