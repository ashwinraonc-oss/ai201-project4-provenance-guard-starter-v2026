"""
Settings for Provenance Guard.

Everything you're likely to change lives here, at the top, on purpose.

You'll edit the thresholds in Milestone 5 and the rate limits in unit 8.
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent


# ─── The service ─────────────────────────────────────────────────────────────

# `127.0.0.1` is loopback — only your own machine can reach it, which is what
# you want all through units 7 and 8. A host somewhere else has to accept
# traffic from outside the box, and that means `0.0.0.0`. Setting the env var
# is how you get it; the default keeps your local `curl` commands unchanged.
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "5000"))

# Flask's debug mode gives anyone who can reach the service an interactive
# Python prompt inside your process. Fine on loopback, a gift to strangers
# anywhere else — so it turns itself off the moment HOST isn't loopback.
DEBUG = os.getenv("AI201_DEBUG", "1") == "1" and HOST in ("127.0.0.1", "localhost")


# ─── The local model ─────────────────────────────────────────────────────────
# Your first signal runs a language model ON YOUR OWN MACHINE. No account, no
# key, no card. It downloads about 550 MB the first time — do that before
# class, not during it.
#
# What it measures: how *predictable* your text is to a language model. Text a
# model finds easy to predict tends to be text a model wrote.
#
# The first call is the slow one — ten to twenty seconds while the model loads,
# longer on an older laptop. After that it stays in memory and a submission
# takes a second or two. That cost is part of what you're learning: this is
# what running a model inline in a request actually looks like.

DETECTOR_MODEL = os.getenv("AI201_DETECTOR_MODEL", "gpt2")

# Longer text gives a steadier reading but takes longer. 400 tokens is roughly
# 300 words, which is enough for the signal to mean something.
DETECTOR_MAX_TOKENS = 400

# criteria.md #5: bad input (missing, empty, or enormous) has to get a clear
# 400, never a 500. ~5,000 words at ~6 characters/word (word + space), rounded
# up — the limit the route itself checks before anything gets scored.
MAX_SUBMISSION_CHARS = 30_000


# ─── Scoring (Milestone 4) ───────────────────────────────────────────────────
# How much each signal counts toward the combined score, decided after
# running both signals over real calibration text — see README's Signals and
# Scoring section for the worked example (varied punctuation and sentence
# length make a generic, predictable paragraph read as confidently human on
# signal two, 0.03, while signal one sits dead-center at 0.52).
#
# Model signal counts for a bit more because it's the one that's actually
# tried to read the text; style is pure shape and easier to game on purpose.
# Neither gets an overwhelming weight — both have a documented, structural
# blind spot, and trusting one of them heavily is exactly how that blind spot
# turns into a wrong accusation.
WEIGHT_MODEL_SIGNAL = 0.6
WEIGHT_STYLE_SIGNAL = 0.4

# When the two signals split by more than this, criterion 1's reasoning
# applies directly: an accusation needs the two signals to actually agree,
# not just average out to "unsure" by coincidence. combine_signals pulls the
# score toward the MORE HUMAN of the two when they disagree this much — see
# the rule itself for the exact blend.
SIGNAL_DISAGREEMENT_THRESHOLD = 0.35


# ─── Thresholds (Milestone 5) ────────────────────────────────────────────────
# Where one label becomes another. Scores run 0.0 (confidently human) to 1.0
# (confidently AI).
#
#   score < HUMAN_THRESHOLD          -> high-confidence human
#   between the two                  -> unsure
#   score > AI_THRESHOLD             -> high-confidence AI
#
# ⚠️ This is where your false-positive decision from Milestone 1 actually gets
# made. Widening the unsure band means fewer wrong accusations and more AI text
# getting through. There is no setting that avoids the trade — only settings
# that decide who pays for it.

HUMAN_THRESHOLD = 0.35

# Raised from 0.65 in unit 8, Milestone 5 — see README's "The Improvement".
# Criterion 1's run showed short, plain, declarative sentences (not AI-
# generated, just mundane) landing at 0.66-0.73 combined: both signals agree
# that kind of text is "predictable," which is a real blind spot in signal
# one, not noise. Moving this to 0.72 keeps the obviously-AI calibration
# text (0.7714) flagged while reclassifying 3 of the 4 false positives as
# unsure instead of ai. The trade this README already names: fewer wrong
# accusations, and more AI text that happens to score 0.65-0.72 now reads as
# unsure instead of ai.
AI_THRESHOLD = 0.72

# ⚠️ One thing that catches people out in Milestone 5. A weighted average can
# only land between its two inputs — so while `style_signal` is still the stub
# returning 0.5, the combined score can never leave 0.25–0.75 no matter what
# the model signal says, and the human label needs a model score below 0.20 to
# be reachable at all.
#
# If a label you can't reach is the problem, the fix is upstream of the
# thresholds: a style signal that actually varies. `scoring.label_ranges()`
# prints the bands; the reachable range is a different question.


# ─── Rate limiting (UNIT 8) ──────────────────────────────────────────────────
# Off in unit 7. You turn it on and choose the numbers in unit 8, Milestone 1.
#
# Think about two people: a real writer submitting their own work a few times
# an hour, and a script sending a thousand variations to map your thresholds.
# Your README has to say why your numbers and not others.

RATE_LIMITING_ENABLED = True

# A real writer revising their own draft might submit a handful of versions
# in one sitting — 2 to 5 is typical even when iterating hard. 8/minute is a
# generous cushion above that: nobody doing their own real work notices it.
# A script trying to map where my thresholds sit by sending many small
# variations hits the wall almost immediately instead of being able to probe
# cheaply.
RATE_LIMIT_PER_MINUTE = 8

# 100/day comfortably covers even a very active real user (20-30 genuine
# submissions in a day would be a lot), while still bounding a slow-drip
# probe that paces itself just under the per-minute limit to avoid it.
RATE_LIMIT_PER_DAY = 100

# Flask-Limiter warns loudly without this. In-memory is right for one laptop
# and wrong for anything real — a restart forgets every count, and two copies
# of the service wouldn't share limits.
RATE_LIMIT_STORAGE = "memory://"


# ─── Paths ───────────────────────────────────────────────────────────────────

LOG_DIR = ROOT / "logs"
AUDIT_LOG = LOG_DIR / "audit.jsonl"
RESULTS_DIR = ROOT / "results"
