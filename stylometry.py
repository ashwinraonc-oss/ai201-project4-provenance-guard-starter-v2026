"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies, in words per sentence.

    Scale and direction, decided and written down: standard deviation of
    per-sentence word counts, divided by the mean so a long text and a short
    one are comparable. **Higher means MORE human-like** — a one-sentence
    submission (or one where every sentence is the same length) has zero
    spread, which reads as the most machine-uniform case on this measure, not
    a missing value. `style_signal` below is the thing that flips this to
    match `detector.model_signal`'s "higher = more AI" direction.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    if mean == 0:
        return 0.0
    return statistics.stdev(lengths) / mean


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. 0 to 1. **Higher means more human-like**
    (more varied vocabulary) — same "flip before combining" note as above.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    w = words(text)
    if not w:
        return 0.0
    return len(set(w)) / len(w)


def punctuation_density(text: str) -> float:
    """
    How much *distinctive* punctuation per 100 words — semicolons, colons, and
    em/en dashes, not full stops or commas. Full stops are load-bearing
    grammar everyone uses the same way; semicolons and dashes are a real
    stylistic choice that varies a lot writer to writer, which is why they're
    the ones worth counting here.

    **Higher means more human-like**, same flip-before-combining note as the
    other two measures.
    """
    w = words(text)
    if not w:
        return 0.0
    marks = re.findall(r"[;:—–]", text)
    return len(marks) / len(w) * 100


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    All three raw measures above point the other way (higher = more human), so
    step one is flipping each. Step two is getting them onto a comparable
    scale before averaging, since a raw type-token ratio lives on 0–1 and a
    raw punctuation count or spread ratio doesn't — averaging them unscaled
    would let whichever has the bigger raw numbers dominate by accident.

    The caps below are the normalizing choice, made and written down rather
    than left implicit:
      - sentence_length_spread capped at 0.8 (stdev/mean this high is already
        quite lumpy prose; more than that doesn't need to count for more)
      - punctuation_density capped at 3 per 100 words (three semicolons/dashes
        per 100 words is already a distinctive, heavy style)
      - type_token_ratio needs no cap; it's already 0–1

    Each capped measure is divided by its cap to land on 0–1, the three are
    averaged (equal weight — no reason yet to trust one of my own three
    measures over another), and the whole thing is flipped (`1 - `) to point
    the same way as `detector.model_signal`: higher output here means more
    AI-like, not more human-like.
    """
    spread = min(sentence_length_spread(text), 0.8) / 0.8
    ttr = type_token_ratio(text)
    punct = min(punctuation_density(text), 3.0) / 3.0

    human_likeness = (spread + ttr + punct) / 3.0
    score = 1.0 - human_likeness
    return round(min(max(score, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
