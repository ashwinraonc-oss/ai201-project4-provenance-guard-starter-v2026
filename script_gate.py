"""
Signal zero. ← CAPSTONE EXTENSION — not part of units 7 or 8.

Decides whether this service should attempt a verdict on a piece of text at
all, before either real signal runs.

Added because unit 8's own attack run found MF07: one ordinary Arabic
sentence scored 0.9438 combined — the single highest-confidence `ai`
accusation this service produced on the entire attack set, against the one
input that had nothing adversarial about it. Both existing signals were
built and tuned on English: signal one is a GPT-2 perplexity read, and GPT-2
was trained mostly on English text; signal two's punctuation set (`;:—–`)
and its word/sentence splitting both assume Latin-script conventions.
Neither signal has any real basis for a confident claim about a script
nothing here was built to read, and MF07's 0.9438 wasn't a fluke of one
sentence — it's what happens whenever a predictability-based signal meets
text it can't actually judge.

This module decides script, not language. Script is cheap, deterministic,
and exactly what the risk above is actually about — the signals don't fail
because the writing is Spanish or French, they fail because it isn't in
letters shaped the way Latin letters are. A real language identifier would
be the better tool for a bigger version of this; for one unit, checking
`unicodedata`'s own idea of script is honest about what it can tell you,
costs nothing to run, and needs no new dependency.
"""

import unicodedata

LATIN_SCRIPT_PREFIX = "LATIN"

# Below this many letters, there isn't enough text to tell a script from
# noise — a two-letter submission made entirely of punctuation and emoji
# shouldn't trip this gate just because its one letter happens to be Greek.
MIN_LETTERS_TO_JUDGE = 5

# Below this fraction of Latin-script letters, the text is predominantly in
# a script neither signal was built around.
MIN_LATIN_RATIO = 0.5


def latin_letter_ratio(text: str) -> tuple[float, int]:
    """
    (fraction of the text's letters that are Latin-script, how many letters
    there were in total). Punctuation, digits, whitespace, and emoji don't
    count toward either number — this is about script, not character
    variety.

    A letter's Unicode name starts with its script — "LATIN SMALL LETTER A",
    "ARABIC LETTER ALEF", "CYRILLIC SMALL LETTER A" — which is a simpler and
    more honest check for this than trying to guess a whole language.
    """
    total = 0
    latin = 0
    for ch in text:
        if not ch.isalpha():
            continue
        total += 1
        try:
            name = unicodedata.name(ch)
        except ValueError:
            # No Unicode name at all (rare, some combining marks). Doesn't
            # count as Latin, but it also shouldn't crash the gate.
            continue
        if name.startswith(LATIN_SCRIPT_PREFIX):
            latin += 1
    ratio = (latin / total) if total else 1.0
    return ratio, total


def is_scorable_script(text: str) -> bool:
    """
    False means: don't run either signal, don't make a guess. True covers
    both "this looks like Latin-script writing" and "there weren't enough
    letters to judge" — the latter on purpose, so this gate stays about the
    one failure mode it was built for (MF07) and doesn't grow into a general
    gibberish filter, which was never the extension's job.
    """
    ratio, total = latin_letter_ratio(text)
    if total < MIN_LETTERS_TO_JUDGE:
        return True
    return ratio >= MIN_LATIN_RATIO


UNSCORABLE_LABEL = (
    "We can't make a call on this one. Our signals were built and tuned on "
    "English, Latin-script writing, and this doesn't look like that — we're "
    "not saying this looks like AI, and we're not vouching for it as human "
    "either. We just don't have a signal here that was built to read it."
)
