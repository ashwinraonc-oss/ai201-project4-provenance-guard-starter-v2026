"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "false positives on plain human writing",
        "criterion": 1,
        # ⚠️ PLACEHOLDER, DISCLOSED AS SUCH — these 10 are plain diary-style
        # sentences I (an AI assistant) wrote to stand in for the real thing,
        # because criterion 1 specifically needs the submitter's OWN writing
        # and I'm not the submitter. The criteria.md docstring says this
        # straight: "it's meaningless with someone else's prose" — and that's
        # equally true of mine. This unblocks the harness so criteria 2-5 can
        # actually run, but criterion 1's verdict below is provisional until
        # these are swapped for real writing from whoever submits this repo.
        # See README's Run Log and Verdicts for the disclosure.
        "texts": [
            "I made coffee this morning and forgot to drink it until it was cold.",
            "My neighbor's dog got loose again. I helped chase it down the block.",
            "I still haven't replied to that email. I keep meaning to.",
            "Rained most of the day. I stayed in and read on the couch.",
            "I burned the toast twice before giving up and eating cereal instead.",
            "My sister called while I was driving. I called her back an hour later.",
            "I lost my keys again. Found them in the fridge, somehow.",
            "The bus was late so I walked the rest of the way. Wasn't too bad.",
            "I tried a new recipe tonight. It was fine, not great. I'd make it again.",
            "Spent an hour looking for my glasses. They were on my head the whole time.",
        ],
    },
    {
        "name": "score spread between obvious cases",
        "criterion": 2,
        # The two deliberately easy cases from unit 7's own calibration work —
        # reused here, not fresh, because criterion 2 is specifically about
        # whether the system tells these two apart AT ALL, and these are the
        # exact two it was tuned against.
        "texts": [
            "The implementation of the proposed framework requires careful consideration of several key factors. It is important to note that the system must be able to handle a wide variety of inputs. Additionally, the overall performance of the solution depends on several important variables.",
            "Honestly? I almost didn't submit this. Spent three hours yesterday rewriting the intro — twice — and still hate it; my advisor will probably hate it more. Whatever. It's done.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # Spread across the range: confidently AI, confidently human, and the
        # quarterly-update paragraph that genuinely landed "unsure" in unit 7
        # (both signals split close to the middle, not by luck).
        "texts": [
            "The implementation of the proposed framework requires careful consideration of several key factors. It is important to note that the system must be able to handle a wide variety of inputs. Additionally, the overall performance of the solution depends on several important variables.",
            "Honestly? I almost didn't submit this. Spent three hours yesterday rewriting the intro — twice — and still hate it; my advisor will probably hate it more. Whatever. It's done.",
            "Overall, the quarterly results show modest growth in most regions, though some markets underperformed expectations. The team is reviewing the data now. Next steps are still being discussed.",
        ],
    },
    {
        "name": "bad input never crashes the service",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": "word " * 10000, "creator_id": "eval_bad_huge"},  # ~60,000 chars, over MAX_SUBMISSION_CHARS
            {"text": None, "creator_id": "eval_bad_null"},
        ],
    },

    # Criterion 4 (the appeal path) is NOT in this list on purpose. run_eval.py
    # only sends to POST /submit, and an appeal needs a real content_id from a
    # submission that already happened — the exact gap this file's own
    # docstring names. I tested it by hand instead: see
    # scripts/eval_appeal_path.py and the Run Log's criterion 4 write-up,
    # rather than bending this shared harness to do something it wasn't built
    # for.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
