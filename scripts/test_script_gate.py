#!/usr/bin/env python3
"""
A quick check on script_gate.py, standalone. ← CAPSTONE, Milestone 2.

Not part of unit 7 or unit 8's test.py — this is this unit's own extension,
checked the same way the course has checked everything else: run it, read
the output, don't trust that it works just because it imports.

    python scripts/test_script_gate.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import script_gate as sg

CASES = [
    ("Arabic — the real MF07 finding", (
        "هذا نص باللغة العربية لاختبار كيفية تعامل النظام مع النصوص التي لا "
        "تستخدم الأبجدية اللاتينية على الإطلاق."
    ), False),
    ("Russian — different non-Latin script", (
        "Это обычное предложение на русском языке для проверки системы."
    ), False),
    ("Plain English", "I made coffee this morning and forgot to drink it.", True),
    ("Formal English", "This report sets out the findings of the working group.", True),
    ("Mostly English, one Arabic word", "Hello world, this has one Arabic word: مرحبا in it.", True),
    ("Too short to judge (two letters)", "Hi.", True),
    ("Emoji only — not this gate's job", "🙂🙃😀😃😄", True),
    ("Punctuation only — not this gate's job", "!!! ??? ... ,,,", True),
]

failures = 0
for name, text, expected_scorable in CASES:
    actual = sg.is_scorable_script(text)
    ok = actual == expected_scorable
    mark = "PASS" if ok else "FAIL"
    if not ok:
        failures += 1
    ratio, total = sg.latin_letter_ratio(text)
    print(f"[{mark}] {name:45s} scorable={actual!s:5s} "
          f"(ratio={ratio:.3f}, letters={total})")

print()
if failures:
    print(f"{failures} of {len(CASES)} checks failed.")
    sys.exit(1)
print(f"All {len(CASES)} checks passed.")
